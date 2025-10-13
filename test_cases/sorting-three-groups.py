# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 3, 2, 2, 1]) == 3
    assert candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 6
    assert candidate(nums = [1, 2, 3, 1, 2, 3]) == 2
    assert candidate(nums = [1, 1, 1]) == 0
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1]) == 4
    assert candidate(nums = [1, 2, 2, 1, 3]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3]) == 0
    assert candidate(nums = [1, 2, 3, 3, 3, 2, 1]) == 2
    assert candidate(nums = [1, 1, 1, 2, 2, 3]) == 0
    assert candidate(nums = [1, 3, 2, 1, 3, 3]) == 2
    assert candidate(nums = [1, 2, 2, 2, 2, 3, 3, 3]) == 0
    assert candidate(nums = [2, 1, 3, 2, 1]) == 3
    assert candidate(nums = [3, 2, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2]) == 3
    assert candidate(nums = [2, 2, 2, 2, 3, 3]) == 0
    assert candidate(nums = [3, 1, 2, 3, 1, 2]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [3, 3, 2, 2, 1]) == 3
    assert candidate(nums = [2, 2, 1, 1, 3, 3]) == 2
    assert candidate(nums = [3, 2, 1]) == 2
    assert candidate(nums = [3, 2, 1, 2, 1]) == 3
    assert candidate(nums = [3, 3, 3]) == 0
    assert candidate(nums = [1, 2, 3, 3, 3, 2, 2, 1, 1, 1]) == 5
    assert candidate(nums = [1, 2, 3]) == 0
    assert candidate(nums = [1, 2, 3, 3, 3]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3]) == 0
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1]) == 4
    assert candidate(nums = [3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 1, 1]) == 9
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1]) == 2
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1]) == 4
    assert candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3]) == 12
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 12
    assert candidate(nums = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 7
    assert candidate(nums = [2, 2, 3, 1, 1, 2, 3, 3, 2, 1]) == 5
    assert candidate(nums = [3, 2, 1, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 3, 2, 1, 3, 2]) == 5
    assert candidate(nums = [2, 3, 2, 1, 2, 3, 2, 1, 2]) == 4
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
    assert candidate(nums = [3, 3, 2, 1, 1, 1, 2, 3]) == 3
    assert candidate(nums = [2, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 3]) == 5
    assert candidate(nums = [3, 3, 3, 1, 1, 1, 2, 2, 2]) == 3
    assert candidate(nums = [3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1]) == 8
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 13
    assert candidate(nums = [3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == 0
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3]) == 3
    assert candidate(nums = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3]) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2]) == 8
    assert candidate(nums = [1, 3, 1, 2, 3, 1, 2, 3, 1]) == 4
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(nums = [3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3]) == 1
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 10
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 7
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 7
    assert candidate(nums = [3, 1, 2, 2, 1, 3, 3, 2, 1, 1, 3, 3, 2, 2, 1, 1]) == 9
    assert candidate(nums = [3, 2, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 10
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 20
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [1, 1, 2, 2, 2, 1, 1, 3, 3, 3, 1, 1]) == 4
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [2, 1, 1, 3, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 0
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 12
    assert candidate(nums = [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [3, 2, 1, 2, 1, 3, 1]) == 4
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 8
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [3, 1, 3, 2, 3, 1, 2, 1, 3]) == 5
    assert candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1, 2, 3, 1]) == 21
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1]) == 4
    assert candidate(nums = [3, 3, 3, 1, 2, 2, 1, 1]) == 5
    assert candidate(nums = [2, 3, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 11
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 11
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 5
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 21
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2]) == 4
    assert candidate(nums = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 6
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3]) == 4
    assert candidate(nums = [2, 2, 1, 1, 3, 3, 2, 2, 3, 3]) == 4
    assert candidate(nums = [1, 3, 3, 1, 2, 2, 1, 3, 3, 2]) == 4
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5
    assert candidate(nums = [2, 2, 3, 1, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]) == 9
    assert candidate(nums = [2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 19
    assert candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1, 3, 2, 1]) == 7
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 12
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 2, 3]) == 5
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1, 1]) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 12
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 7
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 6
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2]) == 6
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2]) == 4
    assert candidate(nums = [2, 1, 2, 1, 3, 2, 1, 2, 3, 3]) == 4
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
    assert candidate(nums = [2, 2, 3, 1, 2, 3, 1, 2]) == 4
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 13
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 4
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 8
    assert candidate(nums = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 10
    assert candidate(nums = [3, 2, 2, 1, 1, 1, 2, 3, 3, 3]) == 3
    assert candidate(nums = [3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3]) == 8
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 5
    assert candidate(nums = [1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3]) == 6
    assert candidate(nums = [1, 3, 3, 3, 2, 2, 1, 1, 3]) == 4
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 6
    assert candidate(nums = [2, 3, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 9
    assert candidate(nums = [2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 6
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1]) == 6
    assert candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 6
    assert candidate(nums = [2, 3, 1, 3, 2, 1, 2, 3, 1]) == 5
