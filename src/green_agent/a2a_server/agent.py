import json
import logging
import uuid

from ...run_test import run_green_tests
from ..benchmarking_manager import BenchmarkingManager

logger = logging.getLogger(__name__)


class CodingEvaluationAgent:
    # Singleton manager instance
    _manager: BenchmarkingManager = None

    @classmethod
    def get_manager(cls) -> BenchmarkingManager:
        """Get or create the singleton BenchmarkingManager instance."""
        if cls._manager is None:
            cls._manager = BenchmarkingManager()
        return cls._manager

    @classmethod
    def initialize_manager(
        cls,
        csv_path: str = "dataset/LeetCodeQuestions.csv",
        model: str = None,
        skip_tests: bool = False,
        skip_llm_judge: bool = False,
    ) -> None:
        """
        Initialize the manager with custom settings.
        Should be called before any agent operations.
        """
        cls._manager = BenchmarkingManager(
            csv_path=csv_path,
            model=model,
            skip_tests=skip_tests,
            skip_llm_judge=skip_llm_judge,
        )

    async def register(self, input) -> str:
        """
        Register the white agent with the green agent.
        See README.md for input and output schema.
        """
        try:
            if "name" not in input:
                return json.dumps({"status": "rejected", "error": "Missing name"})

            # Generate random ID for white agent
            agent_id = uuid.uuid4().hex[:8]
            agent_name = input.get("name")

            # Register with manager
            manager = self.get_manager()
            manager.register_agent(agent_id, agent_name)

            result = {"status": "accepted", "id": agent_id}
            return json.dumps(result)
        except Exception as e:
            logger.error(f"Internal error registering agent: {e}")
            return json.dumps({"status": "rejected", "error": "Server-side error"})

    async def distribute_problem(self, input) -> str:
        """
        Distribute a new coding problem to the white agent.
        See README.md for input and output schema.
        """
        try:
            agent_id = input.get("id")
            agent_name = input.get("name")

            if not agent_id or not agent_name:
                return json.dumps({"status": "rejected", "error": "Missing id or name"})

            manager = self.get_manager()

            # Check if agent is registered
            if not manager.is_registered(agent_id):
                return json.dumps(
                    {"status": "rejected", "error": "Agent ID not registered"}
                )

            # Validate agent credentials
            if not manager.validate_agent(agent_id, agent_name):
                return json.dumps(
                    {"status": "rejected", "error": "Agent name does not match ID."}
                )

            # Get next problem
            try:
                problem = manager.get_next_problem(agent_id)
                result = {
                    "status": "accepted",
                    "problem_description": problem["problem_description"],
                    "starter_code": problem["starter_code"],
                    "entry_point": problem["entry_point"],
                    "prompt": problem["prompt"],
                }
                return json.dumps(result)
            except ValueError as e:  # ValueError is client-side error
                return json.dumps({"status": "rejected", "error": str(e)})

        except Exception as e:
            logger.error(f"Internal error distributing problem: {e}")
            return json.dumps({"status": "rejected", "error": "Server-side error"})

    async def process_answer(self, input) -> str:
        """
        Process the answer from the white agent.
        See README.md for input and output schema.
        """
        try:
            agent_id = input.get("id")
            agent_name = input.get("name")
            solution = input.get("solution")

            if not agent_id or not agent_name or not solution:
                return json.dumps(
                    {"status": "rejected", "error": "Missing id, name, or solution"}
                )

            manager = self.get_manager()

            # Submit answer for evaluation (includes all validation)
            try:
                results = manager.submit_answer(agent_id, agent_name, solution)
                logger.info(f"Processed answer for agent {agent_id}: {results}")
                return json.dumps({"status": "accepted"})
            except ValueError as e:
                return json.dumps({"status": "rejected", "error": str(e)})

        except Exception as e:
            logger.error(f"Error processing answer: {e}")
            return json.dumps({"status": "rejected", "error": str(e)})

    async def start_benchmarking(self, input) -> str:
        """
        Start benchmarking by running tests and/or LLM judgement on
        LeetCode problems. See README.md for input and output schema.

        Expected input fields:
        - model: Optional[str] - Model ID to use for LLM judge
        - skip_tests: Optional[bool] - Skip running test cases
          (default: False)
        - skip_llm_judge: Optional[bool] - Skip LLM judgement
          (default: False)
        - limit: Optional[int] - Number of tests to run (None for all)
        - task_id: Optional[str] - Specific task ID to run (None for all)
        - agents: Optional[str] - Comma-separated list of agent names
          (default: "agent_alpha,agent_beta,agent_gamma")
        - csv_path: Optional[str] - Path to CSV file
          (default: "dataset/LeetCodeQuestions.csv")
        """
        try:
            # Extract parameters from input with defaults
            model = input.get("model")
            skip_tests = input.get("skip_tests", False)
            skip_llm_judge = input.get("skip_llm_judge", False)
            limit = input.get("limit")
            task_id = input.get("task_id")
            agents = input.get("agents", "agent_alpha,agent_beta,agent_gamma")
            csv_path = input.get("csv_path", "dataset/LeetCodeQuestions.csv")

            # Call run_green_tests with the extracted parameters
            results_map = run_green_tests(
                model=model,
                skip_tests=skip_tests,
                skip_llm_judge=skip_llm_judge,
                limit=limit,
                task_id=task_id,
                agents=agents,
                csv_path=csv_path,
            )

            return json.dumps({"status": "accepted", "results": results_map})

        except FileNotFoundError as e:
            return json.dumps(
                {"status": "rejected", "error": f"File not found: {str(e)}"}
            )
        except Exception as e:
            return json.dumps(
                {"status": "rejected", "error": f"Benchmarking failed: {str(e)}"}
            )
