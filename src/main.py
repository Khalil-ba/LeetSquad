"""CLI entry point for LeetSquad"""

import logging

import click

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s"
)


@click.group()
def cli():
    """LeetSquad - Benchmark white agents on LeetCode problems"""
    pass


@cli.group()
def launch():
    """Launch agents (green, white, or both)"""
    pass


@launch.command(name="green")
@click.option("--host", default="0.0.0.0", type=str, show_default=True, help="Host to bind to")
@click.option("--port", default=9999, type=int, show_default=True, help="Port to listen on")
@click.option("--skip-tests", default=False, type=bool, show_default=True, help="Whether to skip accuracy tests")
@click.option("--skip-llm-judge", default=False, type=bool, show_default=True, help="Whether to skip LLM judge")
@click.option("--llm-judge-model", default=None, type=str, show_default=True, help="Model for LLM judge")
@click.option("--limit-problems", default=None, type=int, show_default=True, help="Number of problems to use")
def launch_green(
    host: str,
    port: int,
    skip_tests: bool,
    skip_llm_judge: bool,
    llm_judge_model: str | None,
    limit_problems: int | None,
):
    """Start the green agent server (for multiprocessing)"""
    from .green_agent.start_server import start_server

    start_server(
        host,
        port,
        skip_tests=skip_tests,
        skip_llm_judge=skip_llm_judge,
        llm_judge_model=llm_judge_model,
        limit_problems=limit_problems,
    )


@launch.command(name="white")
@click.option("--host", default="0.0.0.0", help="Host to bind to")
@click.option("--port", default=9998, help="Port to listen on")
@click.option("--agent-id", default="white_agent_001", help="Agent ID")
@click.option("--agent-name", default="LeetCodeSolver", help="Agent name")
def launch_white(host: str, port: int, agent_id: str, agent_name: str):
    """Start the white agent (LeetCode solver agent)"""
    from .white_agent.server import start_server

    start_server(host, port, agent_id, agent_name)


if __name__ == "__main__":
    cli()
