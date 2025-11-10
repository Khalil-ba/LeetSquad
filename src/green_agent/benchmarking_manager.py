import csv
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional

from .accuracy_check.run_testcases import str_to_func, test_accuracy
from .judge.llm_judge import LLMJudge

logger = logging.getLogger(__name__)


class BenchmarkingManager:
    """
    Manages benchmarking workflow including dataset loading, agent registration,
    progress tracking, problem distribution, and result evaluation.

    Designed with in-memory storage that can be easily replaced with
    persistent storage later.
    """

    def __init__(
        self,
        csv_path: str = "dataset/LeetCodeQuestions.csv",
        llm_judge_model: Optional[str] = None,
        skip_tests: bool = False,
        skip_llm_judge: bool = False,
        limit_problems: Optional[int] = None,
    ):
        """
        Initialize the benchmarking manager.

        Args:
            csv_path: Path to the LeetCode questions CSV file
            model: Model ID to use for LLM judge
            skip_tests: Skip running test cases
            skip_llm_judge: Skip LLM judgement
            limit_problems: Only load the specified number of problems
        """
        self.csv_path = csv_path
        self.skip_tests = skip_tests
        self.skip_llm_judge = skip_llm_judge

        # Initialize LLM judge if needed
        self.judge = (
            LLMJudge(model_id=llm_judge_model, verbose=False)
            if not skip_llm_judge
            else None
        )
        # keep max_workers small due to AWS Bedrock quota limit
        self.llm_judge_executor = ThreadPoolExecutor(max_workers=1)

        # In-memory storage (designed for easy migration to DB)
        self._agents: Dict[str, str] = {}  # agent_id -> agent_name
        self._progress: Dict[str, int] = {}  # agent_id -> current_index
        self._pending: Dict[str, str] = {}  # agent_id -> pending_task_id
        self._results: Dict[str, Dict[str, Dict]] = {}  # agent_id -> {task_id -> scores}
        self._detailed_results: Dict[str, Dict[str, Dict]] = {}  # detailed LLM results
        self._dataset: List[Dict] = []  # loaded problems

        # Load dataset
        self._load_dataset(limit_problems)

        # Log args
        logger.info(
            "Initialized BenchmarkingManager with following args: "
            f"csv_path={csv_path}, "
            f"llm_judge_model={llm_judge_model}, "
            f"skip_tests={skip_tests}, "
            f"skip_llm_judge={skip_llm_judge}, "
            f"limit_problems={limit_problems}"
        )

    def _load_dataset(self, limit_problems: Optional[int]) -> None:
        """
        Load the dataset from CSV file.

        Args:
            limit_problems: Only load the specified number of problems
        """
        try:
            with open(self.csv_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) < 5:
                        logger.warning("Encountered invalid row, skipping...")
                        continue
                    self._dataset.append(
                        {
                            "task_id": row[0],
                            "problem_description": row[1],
                            "starter_code": row[2],
                            "entry_point": row[3],
                            "query": row[4],
                        }
                    )
                    if limit_problems and len(self._dataset) >= limit_problems:
                        break
            logger.info(f"Loaded {len(self._dataset)} problems from {self.csv_path}")
        except FileNotFoundError:
            logger.error(f"Dataset CSV file not found: {self.csv_path}")
            raise

    def register_agent(self, agent_id: str, agent_name: str) -> None:
        """
        Register an agent and initialize their progress tracking.

        Args:
            agent_id: Unique agent identifier
            agent_name: Agent name
        """
        self._agents[agent_id] = agent_name
        self._progress[agent_id] = 0
        self._results[agent_id] = {}
        self._detailed_results[agent_id] = {}
        logger.info(f"Registered agent: {agent_name} (ID: {agent_id})")

    def is_registered(self, agent_id: str) -> bool:
        """
        Check if an agent is registered.

        Args:
            agent_id: Agent identifier

        Returns:
            True if agent is registered, False otherwise
        """
        return agent_id in self._agents

    def validate_agent(self, agent_id: str, agent_name: str) -> bool:
        """
        Validate agent credentials (ID and name for now).

        Args:
            agent_id: Agent identifier
            agent_name: Agent name

        Returns:
            True if credentials are valid, False otherwise
        """
        return self.is_registered(agent_id) and self._agents[agent_id] == agent_name

    def get_next_problem(self, agent_id: str) -> Dict:
        """
        Get the next problem for an agent.

        Args:
            agent_id: Agent identifier

        Returns:
            Dict with problem details

        Raises:
            ValueError: If client-side error (e.g. has a pending problem,
            reached end of dataset, not registered, etc.)
        """
        if not self.is_registered(agent_id):
            raise ValueError("Agent not registered")

        # Check if agent has a pending problem
        if agent_id in self._pending:
            raise ValueError("Problem already distributed. Please submit answer first.")

        # Get current progress
        current_idx = self._progress[agent_id]

        # Check if agent has completed all problems
        if current_idx >= len(self._dataset):
            raise ValueError("No more problems available")

        # Get the next problem
        problem = self._dataset[current_idx]

        # Mark as pending
        self._pending[agent_id] = problem["task_id"]

        logger.info(f"Distributed problem {problem['task_id']} to agent {agent_id}")

        return {
            "problem_description": problem["problem_description"],
            "starter_code": problem["starter_code"],
            "entry_point": problem["entry_point"],
        }

    def submit_answer(self, agent_id: str, agent_name: str, solution: str) -> None:
        """
        Receive a solution and advance agent progress.
        Start an asynchronous eval progress.

        Args:
            agent_id: Agent identifier
            agent_name: Agent name
            solution: Code solution to evaluate

        Raises:
            ValueError: If agent not registered, credentials invalid,
                       or no pending problem
        """
        if not self.is_registered(agent_id):
            raise ValueError("Agent not registered")

        if not self.validate_agent(agent_id, agent_name):
            raise ValueError("Agent name does not match ID")

        if agent_id not in self._pending:
            raise ValueError("No pending problem to submit answer for")

        # Get the pending task
        task_id = self._pending[agent_id]

        # Start eval process asynchronously (not blocking networking call)
        self.llm_judge_executor.submit(self._evaluate_answer, agent_id, task_id, solution)

        # Clear pending and advance progress
        del self._pending[agent_id]
        self._progress[agent_id] += 1

        logger.info(f"Received solution for task {task_id} from agent {agent_id}")

    def _evaluate_answer(self, agent_id: str, task_id: str, solution: str) -> None:
        """
        Evaluate a solution and stores the results.

        Args:
            agent_id: Agent identifier
            task_id: Task identifier
            solution: Code solution to evaluate
        """
        # Evaluate the solution
        tests_percent = None
        time_complexity_num = None
        space_complexity_num = None
        readability_overall = None
        if task_id not in self._detailed_results[agent_id]:
            self._detailed_results[agent_id][task_id] = {}

        # Run test cases
        if not self.skip_tests:
            try:
                soln_func = str_to_func(solution)
                passed, total, accuracy = test_accuracy(task_id, soln_func)
                tests_percent = (
                    round(float(accuracy), 1) if accuracy is not None else None
                )
                self._detailed_results[agent_id][task_id]["accuracy"] = {
                    "passed": passed,
                    "total": total,
                }
            except Exception as e:
                logger.error(
                    f"[async] Error testing accuracy for {agent_id}:{task_id}: {e}"
                )

        # Run LLM judge analysis
        if not self.skip_llm_judge and self.judge is not None:
            try:
                complexity = self.judge.analyze_complexity(solution)
                readability = self.judge.analyze_readability(solution)

                time_complexity_num = int(complexity["time"]["complexity_enum"])
                space_complexity_num = int(complexity["space"]["complexity_enum"])
                readability_overall = int(readability.get("overall", 0))

                self._detailed_results[agent_id][task_id]["complexity"] = complexity
                self._detailed_results[agent_id][task_id]["readability"] = readability
            except Exception as e:
                logger.error(
                    f"[async] Error in LLM analysis for {agent_id}:{task_id}: {e}"
                )

        # Store results
        results = {
            "tests_percent": tests_percent,
            "time_complexity": time_complexity_num,
            "space_complexity": space_complexity_num,
            "readability_overall": readability_overall,
        }
        self._results[agent_id][task_id] = results
        logger.info(
            f"[async] Evaluated solution for task {task_id} from agent {agent_id}. "
            f"Result: {results}"
        )

    # TODO: this function can be deleted in favor of report_results
    def get_results(self, agent_id: Optional[str] = None) -> Dict:
        """
        Get evaluation results.

        Args:
            agent_id: Optional agent identifier. If None, returns all results.

        Returns:
            Dict with results for specified agent or all agents
        """
        if agent_id is not None:
            if not self.is_registered(agent_id):
                raise ValueError("Agent not registered")
            return self._results[agent_id]

        # Return all results in the format: agent_id:task_id -> scores
        all_results = {}
        for aid, task_results in self._results.items():
            for task_id, scores in task_results.items():
                key = f"{aid}:{task_id}"
                all_results[key] = scores

        return all_results

    # TODO: implement this function. Some ideas:
    #  - Aggregate results for each agent ID
    #  - Think of a way to incorporate complexity
    def report_results(self) -> str:
        return json.dumps(self._results, indent=4)
