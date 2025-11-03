"""CLI entry point for LeetSquad"""

import asyncio
import logging
import sys

import click

from .green_agent.start_server import start_server as start_green_server
from .run_servers import launch_both_agents
from .run_test import run_green_tests
from .white_agent_consolidated.server import start_server as start_white_server

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@click.group()
def cli():
    """LeetSquad - Benchmark white agents on LeetCode problems"""
    pass


@cli.group()
def launch():
    """Launch agents (green, white, or both)"""
    pass


@launch.command(name="green")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=9999, help="Port to listen on")
def launch_green(host: str, port: int):
    start_green_server(host=host, port=port)


@launch.command(name="white")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=9998, help="Port to listen on")
@click.option("--agent-id", default="white_agent_001", help="Agent ID")
@click.option("--agent-name", default="LeetCodeSolver", help="Agent name")
def launch_white(host: str, port: int, agent_id: str, agent_name: str):
    """Start the white agent (LeetCode solver agent)"""
    logger.info(f"Starting white agent on {host}:{port}")
    start_white_server(host=host, port=port, agent_id=agent_id, agent_name=agent_name)


@launch.command(name="both")
@click.option("--green-port", default=9999, help="Port for green agent")
@click.option("--white-port", default=9998, help="Port for white agent")
def launch_both(green_port: int, white_port: int):
    """Start both green and white agents"""
    logger.info("Launching both agents...")
    asyncio.run(
        launch_both_agents(
            green_host="localhost",
            green_port=green_port,
            white_host="localhost",
            white_port=white_port,
        )
    )


@cli.group()
def test():
    """Run tests and benchmarks"""
    pass


@test.command(name="green")
@click.option(
    "--model",
    type=str,
    default=None,
    help=(
        "Model ID to use for LLM judge (e.g., anthropic.claude-3-5-haiku-20241022-v1:0)"
    ),
)
@click.option(
    "--skip-tests",
    is_flag=True,
    default=False,
    help="Skip running test cases",
)
@click.option(
    "--skip-llm-judge",
    is_flag=True,
    default=False,
    help="Skip LLM judgement",
)
@click.option(
    "--limit",
    type=int,
    default=None,
    help="Number of tests to run (default: all)",
)
@click.option(
    "--task-id",
    type=str,
    default=None,
    help="Specific task ID to run",
)
@click.option(
    "--agents",
    type=str,
    default="agent_alpha,agent_beta,agent_gamma",
    help="Comma-separated list of agent names to test",
)
@click.option(
    "--csv-path",
    type=str,
    default="dataset/LeetCodeQuestions.csv",
    help="Path to LeetCode questions CSV file",
)
def test_green(
    model: str,
    skip_tests: bool,
    skip_llm_judge: bool,
    limit: int,
    task_id: str,
    agents: str,
    csv_path: str,
):
    """
    Execute tests and/or LLM judgement on LeetCode problems for green agent.

    By default, both tests and LLM judgement are run unless
    --skip-tests or --skip-llm-judge is specified.
    """
    try:
        run_green_tests(
            model=model,
            skip_tests=skip_tests,
            skip_llm_judge=skip_llm_judge,
            limit=limit,
            task_id=task_id,
            agents=agents,
            csv_path=csv_path,
        )
    except Exception as e:
        logger.error(f"Error during test execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    cli()
