"""Core LeetCode Solver Agent that interacts with the green agent"""

import logging
from typing import Any, Dict

from .green_client import GreenAgentClient

logger = logging.getLogger(__name__)


class LeetCodeSolverAgent:
    """
    White agent that solves LeetCode problems by interacting with the green agent.

    This agent:
    1. Requests problems from the green agent via distribute_problem
    2. Returns the starter code as the solution (dummy implementation)
    3. Submits solutions via process_answer
    4. Handles accepted/rejected/finished statuses
    """

    def __init__(
        self, agent_id: str = "white_agent_001", agent_name: str = "LeetCodeSolver"
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.problems_solved = 0
        self.problems_attempted = 0

    async def solve_problem(self) -> Dict[str, Any]:
        """
        Main entry point that starts the continuous problem-solving loop.

        Returns:
            Dict with summary of the solving session

        Raises:
            Exception: If green agent rejects a solution
        """
        logger.info(f"Starting problem-solving loop for {self.agent_name}")

        async with GreenAgentClient() as green_client:
            while True:
                try:
                    # Step 1: Request a problem from green agent
                    problem_response = await green_client.distribute_problem(
                        agent_id=self.agent_id, agent_name=self.agent_name
                    )

                    # Step 2: Extract starter code (our dummy solution)
                    starter_code = problem_response.get("starter_code", "")
                    problem_desc = problem_response.get("problem_description", "Unknown")

                    logger.info(f"Received problem: {problem_desc[:50]}...")
                    logger.info(
                        f"Using starter code as solution (length: {len(starter_code)}"
                        " chars)"
                    )

                    self.problems_attempted += 1

                    # Step 3: Submit the starter code as our solution
                    answer_response = await green_client.process_answer(
                        agent_id=self.agent_id,
                        agent_name=self.agent_name,
                        solution=starter_code,
                    )

                    answer_status = answer_response.get("status")

                    if answer_status == "finished":
                        logger.info(
                            "Green agent returned 'finished' after submission. End loop"
                        )
                        break

                    if answer_status == "rejected":
                        error_msg = answer_response.get("error", "Unknown error")
                        logger.error(f"Solution rejected: {error_msg}")
                        raise Exception(f"Solution rejected: {error_msg}")

                    if answer_status == "accepted":
                        logger.info("Solution accepted! Moving to next problem.")
                        self.problems_solved += 1
                    else:
                        logger.error(
                            f"Unexpected status from process_answer: {answer_status}"
                        )
                        raise Exception(f"Unexpected answer status: {answer_status}")

                except Exception as e:
                    # Re-raise to propagate to caller
                    logger.error(f"Error in problem-solving loop: {e}")
                    raise

        # Return summary
        summary = {
            "problems_attempted": self.problems_attempted,
            "problems_solved": self.problems_solved,
            "status": "completed",
        }

        logger.info(f"Problem-solving session completed: {summary}")
        return summary
