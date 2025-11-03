import logging

import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore

from .a2a_server.agent_executor import CodingEvaluationAgentExecutor
from .a2a_server.docs import agent_card

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def start_server(host: str, port: int):
    """Start the green agent (coding evaluation agent)"""
    logger.info(f"Starting green agent on {host}:{port}")

    request_handler = DefaultRequestHandler(
        agent_executor=CodingEvaluationAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )
    server = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )
    uvicorn.run(server.build(), host=host, port=port)
