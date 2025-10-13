import textwrap
import json
from judge.llm_judge import LLMJudge


# Use this function to test LLM's judging capabilities
def test_llm_judge():
    simple_example = textwrap.dedent("""
        def hasDuplicate(self, nums: List[int]) -> bool:
            seen = set()
            for num in nums:
                if num in seen:
                    return True
                seen.add(num)
            return False
    """)

    complex_example = textwrap.dedent("""
        def largestRectangleArea(self, heights: List[int]) -> int:
            n = len(heights)
            stack = []

            leftMost = [-1] * n
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    leftMost[i] = stack[-1]
                stack.append(i)

            stack = []
            rightMost = [n] * n
            for i in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    rightMost[i] = stack[-1]
                stack.append(i)

            maxArea = 0
            for i in range(n):
                leftMost[i] += 1
                rightMost[i] -= 1
                maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
            return maxArea
    """)

    judge = LLMJudge(verbose=True)
    example = simple_example
    
    print("Analyzing time & space complexity...")
    complexity = judge.analyze_complexity(example)
    print(json.dumps(complexity, indent=4))

    print("Analyzing readability...")
    readability = judge.analyze_readability(example)
    print(json.dumps(readability, indent=4))


if __name__ == '__main__':
    test_llm_judge()
