import json

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

from a2a_server.agent import CodingEvaluationAgent


class CodingEvaluationAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = CodingEvaluationAgent()


    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        message = context.get_user_input()
        input = json.loads(message)

        # TODO: validate input schema

        skill = input.get("skill")
        match skill:
            case "register":
                result = await self.agent.register(input)
            case "distribute_problem":
                result = await self.agent.distribute_problem(input)
            case "process_answer":
                result = await self.agent.process_answer(input)
            case _:
                result = json.dumps({
                    "status": "rejected",
                    "error": "Invalid skill"
                })

        await event_queue.enqueue_event(new_agent_text_message(result))


    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        pass
