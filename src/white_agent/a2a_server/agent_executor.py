import asyncio
import json
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

from .agent import CodingSolverAgent


class CodingSolverAgentExecutor(AgentExecutor):
    def __init__(self, **benchmarking_kwargs):
        self.agent = CodingSolverAgent(**benchmarking_kwargs)

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        message = context.get_user_input()
        input = json.loads(message)

        skill = input.get("skill")
        match skill:
            case "start_solving":
                # start the solving process in the background
                asyncio.create_task(self.agent.start_solving())
                result = json.dumps({"status": "accepted"})
            case _:
                result = json.dumps({"status": "rejected", "error": "Invalid skill"})

        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        pass
