import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a_server.agent_executor import CodingEvaluationAgentExecutor
from a2a_server.docs import agent_card

if __name__ == "__main__":
    request_handler = DefaultRequestHandler(
        agent_executor=CodingEvaluationAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )
    server = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )
    uvicorn.run(server.build(), host="0.0.0.0", port=9999)
