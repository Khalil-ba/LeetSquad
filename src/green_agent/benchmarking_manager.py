import csv
import json
import logging
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
        model: Optional[str] = None,
        skip_tests: bool = False,
        skip_llm_judge: bool = False,
    ):
        """
        Initialize the benchmarking manager.

        Args:
            csv_path: Path to the LeetCode questions CSV file
            model: Model ID to use for LLM judge
            skip_tests: Skip running test cases
            skip_llm_judge: Skip LLM judgement
        """
        self.csv_path = csv_path
        self.skip_tests = skip_tests
        self.skip_llm_judge = skip_llm_judge

        # Initialize LLM judge if needed
        self.judge = (
            LLMJudge(model_id=model, verbose=False) if not skip_llm_judge else None
        )

        # In-memory storage (designed for easy migration to DB)
        self._agents: Dict[str, str] = {}  # agent_id -> agent_name
        self._progress: Dict[str, int] = {}  # agent_id -> current_index
        self._pending: Dict[str, str] = {}  # agent_id -> pending_task_id
        self._results: Dict[str, Dict[str, Dict]] = {}  # agent_id -> {task_id -> scores}
        self._dataset: List[Dict] = []  # loaded problems

        # Load dataset
        self._load_dataset()

    def _load_dataset(self) -> None:
        """Load the dataset from CSV file."""
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
            "task_id": problem["task_id"],
            "problem_description": problem["problem_description"],
            "starter_code": problem["starter_code"],
            "entry_point": problem["entry_point"],
            "prompt": problem["query"],
        }

    def submit_answer(self, agent_id: str, agent_name: str, solution: str) -> Dict:
        """
        Evaluate a solution, store results, and advance agent progress.

        Args:
            agent_id: Agent identifier
            agent_name: Agent name
            solution: Code solution to evaluate

        Returns:
            Dict with evaluation results

        Raises:
            ValueError: If agent not registered, credentials invalid,
                       or no pending problem
        """
        if not self.is_registered(agent_id):
            raise ValueError("Agent not registered")

        if not self.validate_agent(agent_id, agent_name):
            raise ValueError("Name does not match ID")

        if agent_id not in self._pending:
            raise ValueError("No pending problem to submit answer for")

        # Get the pending task
        task_id = self._pending[agent_id]

        logger.info(f"Evaluating solution for task {task_id} from agent {agent_id}")

        # Evaluate the solution
        tests_percent = None
        time_complexity_num = None
        space_complexity_num = None
        readability_overall = None

        # Run test cases
        if not self.skip_tests:
            try:
                soln_func = str_to_func(solution)
                accuracy = test_accuracy(task_id, soln_func)
                tests_percent = (
                    round(float(accuracy), 1) if accuracy is not None else None
                )
                logger.info(f"Test accuracy: {tests_percent}%")
            except Exception as e:
                logger.error(f"Error testing accuracy for {agent_id}:{task_id}: {e}")

        # Run LLM judge analysis
        if not self.skip_llm_judge and self.judge is not None:
            try:
                logger.info("Analyzing time & space complexity...")
                complexity = self.judge.analyze_complexity(solution)
                logger.info(json.dumps(complexity, indent=2))
                time_complexity_num = int(complexity["time"]["complexity_enum"])
                space_complexity_num = int(complexity["space"]["complexity_enum"])

                logger.info("Analyzing readability...")
                readability = self.judge.analyze_readability(solution)
                logger.info(json.dumps(readability, indent=2))
                readability_overall = int(readability.get("overall", 0))
            except Exception as e:
                logger.error(f"Error in LLM analysis for {agent_id}:{task_id}: {e}")

        # Store results
        results = {
            "tests_percent": tests_percent,
            "time_complexity": time_complexity_num,
            "space_complexity": space_complexity_num,
            "readability_overall": readability_overall,
        }
        self._results[agent_id][task_id] = results

        # Clear pending and advance progress
        del self._pending[agent_id]
        self._progress[agent_id] += 1

        logger.info(f"Stored results for {agent_id}:{task_id}")

        return results

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

    def run_batch_benchmark(
        self,
        agents: List[str],
        limit: Optional[int] = None,
        task_id: Optional[str] = None,
    ) -> Dict[str, Dict]:
        """
        Run benchmarks for multiple agents (legacy mode for CLI).

        This method simulates the old run_green_tests behavior where
        solutions are retrieved via a placeholder function and evaluated.

        Args:
            agents: List of agent names to benchmark
            limit: Number of tests to run (None for all)
            task_id: Specific task ID to run (None for all/limit)

        Returns:
            Dict mapping "agent_name:task_id" to results
        """
        logger.info("Starting batch benchmark execution")
        logger.info(f"Testing agents: {agents}")

        results_map = {}

        # Determine which problems to process
        problems_to_process = []
        if task_id:
            # Find specific task
            for problem in self._dataset:
                if problem["task_id"] == task_id:
                    problems_to_process.append(problem)
                    break
        elif limit:
            # Process limited number
            problems_to_process = self._dataset[:limit]
        else:
            # Process all
            problems_to_process = self._dataset

        # Process each problem for each agent
        for problem in problems_to_process:
            current_task_id = problem["task_id"]

            logger.info(f"\n{'=' * 80}")
            logger.info(f"Processing: {current_task_id}")
            logger.info(f"{'=' * 80}")

            for agent_name in agents:
                # TODO: Replace with actual solution retrieval logic
                # For now, using placeholder
                from ..run_test import retrieve_solution

                code_str = retrieve_solution(
                    problem["problem_description"],
                    problem["starter_code"],
                    problem["entry_point"],
                    problem["query"],
                    agent_name,
                )

                # Evaluate
                tests_percent = None
                time_complexity_num = None
                space_complexity_num = None
                readability_overall = None

                if not self.skip_tests:
                    try:
                        soln_func = str_to_func(code_str)
                        accuracy = test_accuracy(current_task_id, soln_func)
                        tests_percent = (
                            round(float(accuracy), 1) if accuracy is not None else None
                        )
                    except Exception as e:
                        logger.error(
                            f"Error testing accuracy for "
                            f"{agent_name}:{current_task_id}: {e}"
                        )

                if not self.skip_llm_judge and self.judge is not None:
                    try:
                        logger.info("\nAnalyzing time & space complexity...")
                        complexity = self.judge.analyze_complexity(code_str)
                        logger.info(json.dumps(complexity, indent=2))
                        time_complexity_num = int(complexity["time"]["complexity_enum"])
                        space_complexity_num = int(
                            complexity["space"]["complexity_enum"]
                        )

                        logger.info("\nAnalyzing readability...")
                        readability = self.judge.analyze_readability(code_str)
                        logger.info(json.dumps(readability, indent=2))
                        readability_overall = int(readability.get("overall", 0))
                    except Exception as e:
                        logger.error(
                            f"Error in LLM analysis for "
                            f"{agent_name}:{current_task_id}: {e}"
                        )

                key = f"{agent_name}:{current_task_id}"
                results_map[key] = {
                    "tests_percent": tests_percent,
                    "time_complexity": time_complexity_num,
                    "space_complexity": space_complexity_num,
                    "readability_overall": readability_overall,
                }

        logger.info("\nAll results:")
        logger.info(json.dumps(results_map, indent=2))

        return results_map
