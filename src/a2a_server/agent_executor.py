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
        skill_name = input.get("skill")

        if skill_name == "register":
            result = await self.agent.register(input)
        elif skill_name == "distribute_problem":
            result = await self.agent.distribute_problem(input)
        elif skill_name == "process_answer":
            result = await self.agent.process_answer(input)
        else:
            result = "Invalid skill"

        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        pass
