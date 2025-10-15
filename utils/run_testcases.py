# ...Testcase on two_sum...
import os
import sys
import importlib.util
from testcase_utils import*
test_cases_dir = os.path.abspath(os.path.join(os.getcwd(), "test_cases"))
if test_cases_dir not in sys.path:
    sys.path.insert(0, test_cases_dir)

spec = importlib.util.spec_from_file_location("two_sum_test", os.path.join(test_cases_dir, "two-sum.py")) # use {task_id}.py 
two_sum_test = importlib.util.module_from_spec(spec)
spec.loader.exec_module(two_sum_test)

#Assume this is the result that the LLM generated
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} 

        for i, num in enumerate(nums):
            
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]
            else:
                num_map[num] = i
#############################################################

solution = Solution()
candidate = solution.twoSum # use 'entry_point' for dynamic

passed, total, accuracy = two_sum_test.calculate_accuracy(candidate)
print(f"Accuracy: {accuracy:.1f}% ({passed}/{total})")
print(f'Passed: {passed}/{total} ({accuracy:.1f}%)')
