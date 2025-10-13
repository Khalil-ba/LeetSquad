# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 2, 4, 5]) == 1
    assert candidate(nums = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]) == 4
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(nums = [1, 1, 1, 0, 6, 12]) == 4
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [3, 5, 0, 0, 8, 10, 6, 12, 15]) == 4
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1]) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(nums = [10, 10, 10, 0, 10, 10, 10, 10]) == 4
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
    assert candidate(nums = [1, 2, 3, 0, 4, 5, 6, 7, 8]) == 4
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 3, 3, 2, 2]) == 1
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 0]) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 10
    assert candidate(nums = [5, 0, 3, 8, 6]) == 3
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 1]) == 11
    assert candidate(nums = [2, 1, 3, 4, 4, 5]) == 2
    assert candidate(nums = [5, 4, 3, 2, 1, 0]) == 6
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [3, 3, 2, 2, 3, 1, 4, 5, 6]) == 6
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10]) == 12
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 14
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 1
    assert candidate(nums = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 10
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1
    assert candidate(nums = [5, 2, 1, 3, 4, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [2, 1, 3, 4, 3, 5, 6, 7, 8, 9]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 1
    assert candidate(nums = [0, 2, 1, 3, 5, 4, 7, 6, 9, 8]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]) == 20
    assert candidate(nums = [3, 3, 3, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 6
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]) == 14
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 15
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == 10
    assert candidate(nums = [2, 1, 2, 3, 2, 4, 5, 4, 6, 7, 8, 9, 0, 10, 11, 12]) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 15
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6]) == 1
    assert candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == 1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1]) == 30
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]) == 11
    assert candidate(nums = [7, 9, 7, 8, 1, 7, 10, 13, 2, 5, 6, 7, 3, 8, 9, 10]) == 16
    assert candidate(nums = [2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 5]) == 9
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(nums = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 20, 30, 40, 50]) == 10
    assert candidate(nums = [3, 2, 5, 4, 4, 4, 1, 7, 8, 9]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]) == 18
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 31
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 2]) == 11
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 21
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 20
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]) == 15
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18
    assert candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 10, 9]) == 5
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13]) == 7
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2]) == 18
    assert candidate(nums = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9]) == 6
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == 1
    assert candidate(nums = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]) == 6
    assert candidate(nums = [5, 0, 3, 8, 6, 7, 9, 1, 2, 4, 11, 10, 12, 13, 14]) == 10
    assert candidate(nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [2, 3, 1, 4, 5, 6, 7, 8, 9]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 1
