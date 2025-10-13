# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 1]) == 0
    assert candidate(nums = [3, 3, 3, 3, 7, 2, 2]) == -1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 2, 2, 2]) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]) == 4
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 3]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == -1
    assert candidate(nums = [7, 7, 7, 7, 7, 1, 1, 1, 1, 1]) == -1
