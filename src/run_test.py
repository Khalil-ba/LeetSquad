"""Test execution logic for LeetCode problems"""

import csv
import json
import logging
import textwrap
from typing import Dict, List, Optional

from .green_agent.accuracy_check.run_testcases import str_to_func, test_accuracy
from .green_agent.judge.llm_judge import LLMJudge

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


def process_row(
    row: List[str],
    task_id: str,
    judge: Optional[LLMJudge],
    skip_tests: bool,
    skip_llm_judge: bool,
    agents: List[str],
    results_map: Dict[str, Dict],
) -> None:
    """Process a single row from the dataset for all agents and collect results."""
    problem_description, starter_code, entry_point, query = row

    logger.info(f"\n{'=' * 80}")
    logger.info(f"Processing: {task_id}")
    logger.info(f"{'=' * 80}")

    # TODO: Parallelize by submitting tasks to ThreadPoolExecutor
    # Retrieve futures as_completed and store results in map
    for agent_name in agents:
        code_str = retrieve_solution(
            problem_description, starter_code, entry_point, query, agent_name
        )

        tests_percent = None
        time_complexity_num = None
        space_complexity_num = None
        readability_overall = None

        if not skip_tests:
            try:
                soln_func = str_to_func(code_str)
                accuracy = test_accuracy(task_id, soln_func)
                tests_percent = (
                    round(float(accuracy), 1) if accuracy is not None else None
                )
            except Exception as e:
                logger.error(f"Error testing accuracy for {agent_name}:{task_id}: {e}")

        if not skip_llm_judge and judge is not None:
            try:
                logger.info("\nAnalyzing time & space complexity...")
                complexity = judge.analyze_complexity(code_str)
                logger.info(json.dumps(complexity, indent=2))
                time_complexity_num = int(complexity["time"]["complexity_enum"])
                space_complexity_num = int(complexity["space"]["complexity_enum"])

                logger.info("\nAnalyzing readability...")
                readability = judge.analyze_readability(code_str)
                logger.info(json.dumps(readability, indent=2))
                readability_overall = int(readability.get("overall", 0))
            except Exception as e:
                logger.error(f"Error in LLM analysis for {agent_name}:{task_id}: {e}")

        key = f"{agent_name}:{task_id}"
        results_map[key] = {
            "tests_percent": tests_percent,
            "time_complexity": time_complexity_num,
            "space_complexity": space_complexity_num,
            "readability_overall": readability_overall,
        }


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

    judge = LLMJudge(model_id=model, verbose=False) if not skip_llm_judge else None

    # Parse agent list
    agent_list = [a.strip() for a in agents.split(",")]
    logger.info(f"Testing agents: {agent_list}")

    # TODO: Store results in database instead of in-memory map
    results_map = {}

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            count = 0

            for row in reader:
                if len(row) < 5:
                    logger.warning("Row is too short, skipping...")
                    continue

                current_task_id = row[0]

                # Filter by task_id if specified
                if task_id and current_task_id != task_id:
                    continue
                elif task_id and current_task_id == task_id:
                    # Found the specific task, process it and break
                    other_columns = row[1:5]
                    process_row(
                        other_columns,
                        current_task_id,
                        judge,
                        skip_tests,
                        skip_llm_judge,
                        agent_list,
                        results_map,
                    )
                    break

                # If limit is set, check if we've reached it
                if limit is not None:
                    count += 1
                    if count > limit:
                        break

                other_columns = row[1:5]
                process_row(
                    other_columns,
                    current_task_id,
                    judge,
                    skip_tests,
                    skip_llm_judge,
                    agent_list,
                    results_map,
                )

        logger.info("\nAll results:")
        logger.info(json.dumps(results_map, indent=2))

        return results_map

    except FileNotFoundError:
        logger.error(f"CSV file not found: {csv_path}")
        raise
