import json
import logging
import uuid

from .agent_docs import kick_off_message

from ..evaluation import BenchmarkingManager

logger = logging.getLogger(__name__)


class CodingEvaluationAgent:
    # Singleton manager instance
    _manager: BenchmarkingManager = None

    @classmethod
    def get_manager(cls) -> BenchmarkingManager:
        """Get or create the singleton BenchmarkingManager instance."""
        if cls._manager is None:
            raise RuntimeError("BenchmarkingManager not initialized.")
        return cls._manager

    @classmethod
    def initialize_manager(
        cls,
        csv_path: str = "dataset/LeetCodeQuestions.csv",
        llm_judge_model: str = None,
        skip_tests: bool = False,
        skip_llm_judge: bool = False,
        limit_problems=None,
    ) -> None:
        """
        Initialize the manager with custom settings.
        Must be called before any agent operations.
        """
        cls._manager = BenchmarkingManager(
            csv_path=csv_path,
            llm_judge_model=llm_judge_model,
            skip_tests=skip_tests,
            skip_llm_judge=skip_llm_judge,
            limit_problems=limit_problems,
        )

    async def get_instructions(self, input) -> str:
        """
        Sends a high-level kick-off message to white agents, detailing their overall
        task, benchmarking workflow, skills they can invoke, etc.

        The green agent assumes white agents have prior knowledge to invoke this skill
        as the starting point of interactions.
        """
        return json.dumps({"status": "accepted", "instructions": kick_off_message})

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
                result = {"status": "accepted", **problem}
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
                manager.submit_answer(agent_id, agent_name, solution)
                return json.dumps({"status": "accepted"})
            except ValueError as e:
                return json.dumps({"status": "rejected", "error": str(e)})

        except Exception as e:
            logger.error(f"Internal error processing answer: {e}")
            return json.dumps({"status": "rejected", "error": "Server-side error"})

    async def report_results(self, input) -> str:
        """
        Report the benchmarking results.
        See README.md for input and output schema.
        """
        try:
            manager = self.get_manager()
            results = manager.report_results()
            return json.dumps({"status": "accepted", "results": results})
        except Exception as e:
            logger.error(f"Internal error processing answer: {e}")
            return json.dumps({"status": "rejected", "error": "Server-side error"})
