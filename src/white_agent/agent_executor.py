"""Agent executor for A2A framework integration"""

import json
import logging

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

from .agent import LeetCodeSolverAgent

logger = logging.getLogger(__name__)


class LeetCodeSolverExecutor(AgentExecutor):
    """
    Executor that wraps LeetCodeSolverAgent for A2A framework.

    This executor handles incoming A2A requests and routes them to the appropriate
    agent method based on the requested skill.
    """

    def __init__(
        self, agent_id: str = "white_agent_001", agent_name: str = "LeetCodeSolver"
    ):
        self.agent = LeetCodeSolverAgent(agent_id=agent_id, agent_name=agent_name)

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        """
        Execute the requested skill.

        Currently supports:
        - solve_problem: Starts the continuous problem-solving loop
        """
        try:
            # Get user input from context
            message = context.get_user_input()

            # Try to parse as JSON to extract skill, or treat as plain command
            try:
                input_data = json.loads(message)
                skill = input_data.get("skill", message.strip())
            except json.JSONDecodeError:
                skill = message.strip()

            logger.info(f"Executing skill: {skill}")

            # Route to appropriate skill
            if skill == "solve_problem":
                result = await self.agent.solve_problem()
                result_message = json.dumps({"status": "success", "data": result})
            else:
                result_message = json.dumps(
                    {"status": "error", "error": f"Unknown skill: {skill}"}
                )

            # Send result back through event queue
            await event_queue.enqueue_event(new_agent_text_message(result_message))

        except Exception as e:
            logger.error(f"Error executing skill: {e}", exc_info=True)
            error_message = json.dumps({"status": "error", "error": str(e)})
            await event_queue.enqueue_event(new_agent_text_message(error_message))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        """Cancel execution - not implemented"""
        logger.warning("Cancel requested but not implemented")
        await event_queue.enqueue_event(
            new_agent_text_message(
                json.dumps({"status": "error", "error": "Cancel not supported"})
            )
        )
