import csv
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional

from .accuracy_check import str_to_func, test_accuracy
from .llm_judge import LLMJudge

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
            return {
                "message": "You have completed all problems. No more problems available."
            }

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

    # Aggregate results for all agents and overall summary
    def report_results(self) -> Dict:
        """Return aggregated benchmarking results across all registered agents.

        Structure:
        {
          "agents": {
             "<agent_id>": {
                 "name": "<agent_name>",
                 "problems_scored": <int>,
                 "tests": {
                     "total_passed": <int>,
                     "total": <int>,
                     "percent": <float|null>,
                     "avg_tests_percent": <float|null>
                 },
                 "llm": {
                     "avg_readability_overall": <float|null>
                 }
             },
             ...
          },
          "overall": { ...same fields aggregated across agents... }
        }
        """
        agents_summary: Dict[str, Dict] = {}

        overall_total_passed = 0
        overall_total_tests = 0
        overall_tests_percents: List[float] = []
        overall_readability_scores: List[int] = []
        overall_problems_scored = 0

        for agent_id, task_results in self._results.items():
            agent_name = self._agents.get(agent_id, agent_id)

            total_passed = 0
            total_tests = 0
            tests_percents: List[float] = []
            time_complexities: List[int] = []
            space_complexities: List[int] = []
            readability_scores: List[int] = []

            # Pull accuracy details from detailed results if available
            detailed = self._detailed_results.get(agent_id, {})

            for task_id, scores in task_results.items():
                # Tests percent at per-task level
                tp = scores.get("tests_percent")
                if isinstance(tp, (int, float)):
                    tests_percents.append(float(tp))
                    overall_tests_percents.append(float(tp))

                # Sum passed/total when recorded in detailed results
                acc = detailed.get(task_id, {}).get("accuracy", {})
                p = acc.get("passed")
                t = acc.get("total")
                if isinstance(p, int) and isinstance(t, int):
                    total_passed += p
                    total_tests += t

                # LLM judge aggregates when available
                tc = scores.get("time_complexity")
                sc = scores.get("space_complexity")
                rd = scores.get("readability_overall")
                if isinstance(tc, int):
                    time_complexities.append(tc)
                if isinstance(sc, int):
                    space_complexities.append(sc)
                if isinstance(rd, int):
                    readability_scores.append(rd)
                    overall_readability_scores.append(rd)

            # Build per-agent summary
            problems_scored = len(task_results)
            agents_summary[agent_id] = {
                "name": agent_name,
                "problems_scored": problems_scored,
                "tests": {
                    "total_passed": total_passed,
                    "total": total_tests,
                    "percent": round(100.0 * total_passed / total_tests, 1)
                    if total_tests > 0
                    else None,
                    "avg_tests_percent": round(
                        sum(tests_percents) / len(tests_percents), 1
                    )
                    if tests_percents
                    else None,
                },
                "llm": {
                    "avg_time_complexity": round(
                        sum(time_complexities) / len(time_complexities), 2
                    )
                    if time_complexities
                    else None,
                    "avg_space_complexity": round(
                        sum(space_complexities) / len(space_complexities), 2
                    )
                    if space_complexities
                    else None,
                    "avg_readability_overall": round(
                        sum(readability_scores) / len(readability_scores), 2
                    )
                    if readability_scores
                    else None,
                },
            }

            overall_total_passed += total_passed
            overall_total_tests += total_tests
            overall_problems_scored += problems_scored

        overall = {
            "agents_count": len(self._agents),
            "problems_scored": overall_problems_scored,
            "tests": {
                "total_passed": overall_total_passed,
                "total": overall_total_tests,
                "percent": round(100.0 * overall_total_passed / overall_total_tests, 1)
                if overall_total_tests > 0
                else None,
                "avg_tests_percent": round(
                    sum(overall_tests_percents) / len(overall_tests_percents), 1
                )
                if overall_tests_percents
                else None,
            },
            "llm": {
                "avg_readability_overall": round(
                    sum(overall_readability_scores) / len(overall_readability_scores),
                    2,
                )
                if overall_readability_scores
                else None,
            },
        }

        return {"agents": agents_summary, "overall": overall}
