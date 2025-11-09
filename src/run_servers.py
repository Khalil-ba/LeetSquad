"""Launcher module for starting both green and white agents"""

import asyncio
import logging
import multiprocessing
import signal
import sys
import time

import httpx

logger = logging.getLogger(__name__)


async def wait_agent_ready(
    url: str, timeout: int = 30, check_interval: float = 0.5
) -> bool:
    """
    Wait for an agent to be ready by checking its agent card endpoint.

    Args:
        url: Base URL of the agent (e.g., http://localhost:9999)
        timeout: Maximum time to wait in seconds
        check_interval: Time between checks in seconds

    Returns:
        True if agent is ready, False if timeout
    """
    agent_card_url = f"{url}/.well-known/agent.json"
    start_time = time.time()

    async with httpx.AsyncClient() as client:
        while time.time() - start_time < timeout:
            try:
                response = await client.get(agent_card_url, timeout=2.0)
                if response.status_code == 200:
                    logger.info(f"Agent at {url} is ready")
                    return True
            except (httpx.ConnectError, httpx.TimeoutException, httpx.ReadTimeout):
                pass  # Agent not ready yet

            await asyncio.sleep(check_interval)

    logger.error(f"Agent at {url} did not become ready within {timeout}s")
    return False


def start_green_agent_process(host: str = "0.0.0.0", port: int = 9999):
    """Start the green agent server (for multiprocessing)"""
    # Import here to avoid issues with multiprocessing
    import uvicorn
    from a2a.server.apps import A2AStarletteApplication
    from a2a.server.request_handlers import DefaultRequestHandler
    from a2a.server.tasks import InMemoryTaskStore

    from .green_agent.a2a_server.agent_executor import CodingEvaluationAgentExecutor
    from .green_agent.a2a_server.docs import agent_card

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    logger.info(f"Starting green agent on {host}:{port}")

    request_handler = DefaultRequestHandler(
        agent_executor=CodingEvaluationAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )
    server = A2AStarletteApplication(agent_card=agent_card, http_handler=request_handler)
    uvicorn.run(server.build(), host=host, port=port)


def start_white_agent_process(host: str = "0.0.0.0", port: int = 9998):
    """Start the white agent server (for multiprocessing)"""
    # Import here to avoid issues with multiprocessing
    from .white_agent_consolidated.server import start_server

    start_server(host=host, port=port)


async def launch_both_agents(
    green_host: str = "localhost",
    green_port: int = 9999,
    white_host: str = "localhost",
    white_port: int = 9998,
):
    """
    Launch both green and white agents in separate processes.

    Args:
        green_host: Host for green agent
        green_port: Port for green agent
        white_host: Host for white agent
        white_port: Port for white agent
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Start green agent
    logger.info("Launching green agent...")
    green_url = f"http://{green_host}:{green_port}"
    p_green = multiprocessing.Process(
        target=start_green_agent_process,
        args=("0.0.0.0", green_port),
    )
    p_green.start()

    # Wait for green agent to be ready
    if not await wait_agent_ready(green_url):
        logger.error("Green agent failed to start")
        p_green.terminate()
        p_green.join()
        sys.exit(1)
    logger.info("Green agent is ready")

    # Start white agent
    logger.info("Launching white agent...")
    white_url = f"http://{white_host}:{white_port}"
    p_white = multiprocessing.Process(
        target=start_white_agent_process, args=("0.0.0.0", white_port)
    )
    p_white.start()

    # Wait for white agent to be ready
    if not await wait_agent_ready(white_url):
        logger.error("White agent failed to start")
        p_white.terminate()
        p_white.join()
        p_green.terminate()
        p_green.join()
        sys.exit(1)
    logger.info("White agent is ready")

    logger.info("Both agents are running")
    logger.info(f"Green agent: {green_url}")
    logger.info(f"White agent: {white_url}")
    logger.info("Press Ctrl+C to stop both agents")

    # Setup signal handlers for graceful shutdown
    def signal_handler(sig, frame):
        logger.info("\nShutting down agents...")
        p_green.terminate()
        p_white.terminate()
        p_green.join()
        p_white.join()
        logger.info("Agents terminated")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Keep the main process alive
    try:
        p_green.join()
        p_white.join()
    except KeyboardInterrupt:
        logger.info("\nShutting down agents...")
        p_green.terminate()
        p_white.terminate()
        p_green.join()
        p_white.join()
        logger.info("Agents terminated")
