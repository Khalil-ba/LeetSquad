"""A2A Server for the LeetCode Solver White Agent"""

import logging
import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore

from ..a2a_server.agent_docs import agent_card
from ..a2a_server.agent_executor import CodingSolverAgentExecutor

logger = logging.getLogger(__name__)


def start_server(
    host: str = "0.0.0.0",
    port: int = 9998,
    name: str = "LeetCodeSolver",
):
    """
    Start the A2A server for the white agent.

    Args:
        host: Host to bind to (default: 0.0.0.0)
        port: Port to listen on (default: 9998)
        name: Name of this agent instance
    """
    logger.info(f"Initializing LeetCode Solver Agent: {name}")

    # Create request handler with agent executor
    request_handler = DefaultRequestHandler(
        agent_executor=CodingSolverAgentExecutor(name=name),
        task_store=InMemoryTaskStore(),
    )

    # Create A2A server application
    server = A2AStarletteApplication(agent_card=agent_card, http_handler=request_handler)

    logger.info(f"Starting LeetCode Solver Server on {host}:{port}")
    logger.info("Green agent expected at: http://localhost:9999")
    logger.info("Server will wait idle until 'start_solving' skill is invoked")

    # Start the server
    uvicorn.run(server.build(), host=host, port=port)
