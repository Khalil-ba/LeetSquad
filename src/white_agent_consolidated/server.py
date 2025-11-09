"""A2A Server for the LeetCode Solver White Agent"""

import logging

import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

from .agent_executor import LeetCodeSolverExecutor

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Define the solve_problem skill
solve_problem_skill = AgentSkill(
    id="solve_problem",
    name="Solve LeetCode Problems",
    description="Continuously requests and solves LeetCode problems from green agent",
    tags=["leetcode", "coding", "problem-solving"],
    examples=["solve_problem", "start solving", "begin problem loop"],
)

# Define the agent card
agent_card = AgentCard(
    name="LeetCode Solver Agent",
    description=(
        "White agent that continuously solves LeetCode problems by interacting with "
        "the green agent"
    ),
    url="http://localhost:9998/",
    version="1.0.0",
    default_input_modes=["text"],
    default_output_modes=["text"],
    capabilities=AgentCapabilities(streaming=False),
    skills=[solve_problem_skill],
    supports_authenticated_extended_card=False,
)


def start_server(
    host: str = "0.0.0.0",
    port: int = 9998,
    agent_id: str = "white_agent_001",
    agent_name: str = "LeetCodeSolver",
):
    """
    Start the A2A server for the white agent.

    Args:
        host: Host to bind to (default: 0.0.0.0)
        port: Port to listen on (default: 9998)
        agent_id: Unique ID for this agent instance
        agent_name: Name of this agent instance
    """
    logger.info(f"Initializing LeetCode Solver Agent: {agent_name} (ID: {agent_id})")

    # Create request handler with agent executor
    request_handler = DefaultRequestHandler(
        agent_executor=LeetCodeSolverExecutor(agent_id=agent_id, agent_name=agent_name),
        task_store=InMemoryTaskStore(),
    )

    # Create A2A server application
    server = A2AStarletteApplication(agent_card=agent_card, http_handler=request_handler)

    logger.info(f"Starting LeetCode Solver Server on {host}:{port}")
    logger.info("Green agent expected at: http://localhost:9999")
    logger.info("Server will wait idle until 'solve_problem' skill is invoked")

    # Start the server
    uvicorn.run(server.build(), host=host, port=port)


if __name__ == "__main__":
    start_server()
