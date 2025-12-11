import json
import re

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

from .agent import CodingEvaluationAgent


class CodingEvaluationAgentExecutor(AgentExecutor):
    """
    Executor class for the CodingEvaluationAgent.

    This class bridges the A2A agent execution framework with the green agent's
    core evaluation logic. It receives A2A user requests, parses the skill invocation,
    delegates the request to the appropriate method on CodingEvaluationAgent, and
    returns the result to the event queue.
    """

    def __init__(self, **benchmarking_kwargs):
        """
        Constructor args are used directly to initialize BenchmarkingManager
        """
        CodingEvaluationAgent.initialize_manager(**benchmarking_kwargs)
        self.agent = CodingEvaluationAgent()

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        message = context.get_user_input()

        try:
            input = json.loads(message)
        except json.JSONDecodeError as e:
            # AgentBeats blog says we should be able to specify our own assessment startup
            # structure, but for now it is a hardcoded string with a tag <white_agent_url>
            if message and parse_tags(message).get("white_agent_url"):
                result = json.dumps({"status": "accepted"})
            else:
                result = json.dumps(
                    {
                        "status": "rejected",
                        "error": (
                            "Does not match AgentBeats startup string "
                            f"or contain valid JSON: {str(e)}"
                        ),
                    }
                )

        skill = input.get("skill")
        match skill:
            case "register":
                result = await self.agent.register(input)
            case "distribute_problem":
                result = await self.agent.distribute_problem(input)
            case "process_answer":
                result = await self.agent.process_answer(input)
            case "report_results":
                # convenience skill for getting results, shouldn't be used by white agents
                result = await self.agent.report_results(input)
            case _:
                result = json.dumps({"status": "rejected", "error": "Invalid skill"})

        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        pass


def parse_tags(str_with_tags: str) -> dict[str, str]:
    """the target str contains tags in the format of <tag_name> ... </tag_name>, parse them out and return a dict"""

    tags = re.findall(r"<(.*?)>(.*?)</\1>", str_with_tags, re.DOTALL)
    return {tag: content.strip() for tag, content in tags}
