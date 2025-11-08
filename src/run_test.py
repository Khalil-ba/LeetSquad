"""Test execution logic for LeetCode problems"""

import logging
import textwrap
from typing import Dict, Optional

from .green_agent.benchmarking_manager import BenchmarkingManager

logger = logging.getLogger(__name__)


def retrieve_solution(
    problem_description: str,
    starter_code: str,
    entry_point: str,
    query: str,
    agent_name: str,
) -> str:
    """
    TODO: Implement actual solution retrieval logic.
    For now, returns a hardcoded dummy solution.
    """
    logger.info(f"Retrieving solution from agent: {agent_name}")

    return textwrap.dedent(
        """
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            num_map = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in num_map:
                    return [num_map[complement], i]
                else:
                    num_map[num] = i
    """
    )


def run_green_tests(
    model: Optional[str] = None,
    skip_tests: bool = False,
    skip_llm_judge: bool = False,
    limit: Optional[int] = None,
    task_id: Optional[str] = None,
    agents: str = "agent_alpha,agent_beta,agent_gamma",
    csv_path: str = "dataset/LeetCodeQuestions.csv",
) -> Dict[str, Dict]:
    """
    Execute tests and/or LLM judgement on LeetCode problems for green agent.

    Args:
        model: Model ID to use for LLM judge
        skip_tests: Skip running test cases
        skip_llm_judge: Skip LLM judgement
        limit: Number of tests to run (None for all)
        task_id: Specific task ID to run (None for all)
        agents: Comma-separated list of agent names to test
        csv_path: Path to LeetCode questions CSV file

    Returns:
        Dict mapping "agent_name:task_id" to results

    Raises:
        FileNotFoundError: If CSV file not found
        Exception: For other errors during test execution
    """
    logger.info("Starting green agent test execution")

    # Parse agent list
    agent_list = [a.strip() for a in agents.split(",")]

    # Create manager and run batch benchmark
    try:
        manager = BenchmarkingManager(
            csv_path=csv_path,
            model=model,
            skip_tests=skip_tests,
            skip_llm_judge=skip_llm_judge,
        )

        results_map = manager.run_batch_benchmark(
            agents=agent_list, limit=limit, task_id=task_id
        )

        return results_map

    except FileNotFoundError:
        logger.error(f"CSV file not found: {csv_path}")
        raise
