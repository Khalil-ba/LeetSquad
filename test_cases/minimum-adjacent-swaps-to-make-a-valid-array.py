# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 17
    assert candidate(nums = [10, 1, 10, 2, 10, 3, 10]) == 1
    assert candidate(nums = [1, 2, 3, 5, 4]) == 1
    assert candidate(nums = [5, 1, 2, 3, 4]) == 4
    assert candidate(nums = [100000, 1, 2, 3, 4, 100000]) == 1
    assert candidate(nums = [3, 4, 5, 5, 3, 1]) == 6
    assert candidate(nums = [7, 10, 4, 3, 20, 15]) == 4
    assert candidate(nums = [9]) == 0
    assert candidate(nums = [1, 3, 2, 3, 1]) == 1
    assert candidate(nums = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 9
    assert candidate(nums = [5, 1, 3, 1, 5]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [1, 5, 3, 4, 2]) == 3
    assert candidate(nums = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9]) == 0
    assert candidate(nums = [2, 1, 3, 4, 5]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1]) == 7
    assert candidate(nums = [1, 100000, 2, 3, 4, 100000]) == 0
    assert candidate(nums = [1, 3, 5, 2, 4]) == 2
    assert candidate(nums = [1, 3, 2, 2, 1]) == 3
    assert candidate(nums = [1, 5, 2, 3, 4]) == 3
    assert candidate(nums = [1, 3, 5, 2, 4, 6]) == 0
    assert candidate(nums = [2, 1, 3, 1, 2]) == 3
    assert candidate(nums = [3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [100000, 1, 100000]) == 1
    assert candidate(nums = [10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [100, 100, 100, 1, 100, 100, 100]) == 3
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10]) == 5
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 1]) == 19
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10]) == 1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 6
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 37
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [1, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 100000]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 1
    assert candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(nums = [3, 1, 2, 4, 5, 3, 2, 1]) == 4
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]) == 8
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 9
    assert candidate(nums = [7, 3, 1, 5, 4, 6, 2, 8]) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
    assert candidate(nums = [3, 1, 2, 5, 4, 5, 1, 2]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3]) == 3
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1]) == 10
    assert candidate(nums = [1, 3, 2, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [5, 5, 5, 5, 1, 5, 5, 5, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 1
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 2, 1, 3, 5]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]) == 2
    assert candidate(nums = [5, 5, 5, 5, 1, 5, 5, 5, 5, 5]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]) == 5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2]) == 7
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 15, 13, 11, 9, 7, 5, 3, 1]) == 22
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 38
    assert candidate(nums = [3, 1, 2, 2, 3, 1, 4, 5, 6, 1]) == 2
    assert candidate(nums = [1, 3, 2, 3, 1, 2, 1, 3, 2, 1, 2, 1]) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995, 7, 99994, 8, 99993, 9, 99992, 10, 99991]) == 18
    assert candidate(nums = [7, 3, 5, 4, 6, 2, 8, 1, 9]) == 7
    assert candidate(nums = [7, 3, 5, 1, 2, 8, 4, 6, 9, 7, 5, 3, 1]) == 7
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 2
    assert candidate(nums = [2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1]) == 5
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 0
    assert candidate(nums = [7, 3, 5, 1, 6, 4, 2, 8]) == 3
    assert candidate(nums = [7, 3, 5, 1, 9, 9, 2, 5, 6]) == 6
    assert candidate(nums = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 7
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15]) == 4
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 18
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 10
    assert candidate(nums = [5, 4, 3, 2, 1, 9, 8, 7, 6]) == 7
    assert candidate(nums = [6, 6, 6, 1, 6, 6, 6, 6, 6, 6]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]) == 1
    assert candidate(nums = [4, 1, 2, 3, 5, 1, 5, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 13
    assert candidate(nums = [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11]) == 18
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
