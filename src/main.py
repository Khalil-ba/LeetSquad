import json
import textwrap

from accuracy_check.run_testcases import str_to_func, test_accuracy
from judge.llm_judge import LLMJudge


def main():
    code_str = textwrap.dedent("""
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            num_map = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in num_map:
                    return [num_map[complement], i]
                else:
                    num_map[num] = i
    """)

    soln_func = str_to_func(code_str)
    task_id = "two-sum"
    test_accuracy(task_id, soln_func)

    judge = LLMJudge(verbose=False)

    print("Analyzing time & space complexity...")
    complexity = judge.analyze_complexity(code_str)
    print(json.dumps(complexity, indent=4))

    print("Analyzing readability...")
    readability = judge.analyze_readability(code_str)
    print(json.dumps(readability, indent=4))


if __name__ == "__main__":
    main()
