# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [6, 5, 7, 8]) == 7
    assert candidate(nums = [1, 3, 2, 4, 5]) == 11
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, 2, 2, 3, 4]) == 11
    assert candidate(nums = [1, 2, 2, 3]) == 8
    assert candidate(nums = [1, 2, 3, 4]) == 10
    assert candidate(nums = [1, 2]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7]) == 19
    assert candidate(nums = [10, 20, 15, 25, 30]) == 11
    assert candidate(nums = [1, 2, 3, 2, 3, 4]) == 13
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 3]) == 8
    assert candidate(nums = [8, 7, 6, 6]) == 3
    assert candidate(nums = [1, 2, 3, 3, 4]) == 11
    assert candidate(nums = [10, 20, 15, 30, 25, 40]) == 9
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 8, 9, 10]) == 22
    assert candidate(nums = [5, 3, 4, 6, 7, 2, 3, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10]) == 22
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 25
    assert candidate(nums = [3, 5, 2, 8, 7, 10, 9, 11, 13, 12]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == 26
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 12
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]) == 9
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9]) == 29
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 71
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
    assert candidate(nums = [5, 10, 15, 20, 18, 25, 30, 35, 40]) == 29
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 21
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 13
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 11
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 12
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 14, 16, 18, 20, 19, 21, 23, 25, 24, 26, 28, 30]) == 45
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12]) == 6
    assert candidate(nums = [3, 1, 2, 1, 3, 4, 5, 6, 7]) == 12
    assert candidate(nums = [9, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == 12
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 11
    assert candidate(nums = [1, 2, 3, 2, 1]) == 5
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 9
    assert candidate(nums = [1, 5, 3, 7, 9, 2, 11, 13, 12, 14]) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10, 11]) == 46
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]) == 25
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 26
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 51
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 12
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13]) == 9
    assert candidate(nums = [30, 20, 10, 20, 30, 40, 30, 20, 10]) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 4
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4
    assert candidate(nums = [5, 6, 2, 7, 8, 10]) == 13
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
    assert candidate(nums = [5, 1, 2, 3, 4, 5, 6]) == 9
    assert candidate(nums = [3, 5, 6, 7, 8, 2, 3, 4, 5, 6]) == 15
    assert candidate(nums = [1, 2, 3, 6, 5, 4, 7, 8, 9, 10]) == 29
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 10, 20, 30]) == 9
    assert candidate(nums = [3, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12]) == 28
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 10, 9, 11]) == 15
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6]) == 22
    assert candidate(nums = [10, 20, 30, 25, 35, 40, 30, 45]) == 11
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 4
    assert candidate(nums = [2, 2, 2, 2, 2]) == 3
    assert candidate(nums = [10, 20, 30, 25, 40, 50, 15, 25, 35, 45]) == 17
    assert candidate(nums = [10, 20, 30, 25, 35, 40, 38, 45]) == 12
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 38
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 11]) == 43
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == 8
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 4
    assert candidate(nums = [1, 3, 5, 4, 6, 7, 8, 9]) == 23
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 17
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4]) == 10
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 41
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 3
    assert candidate(nums = [20, 25, 15, 30, 35, 28, 40, 45, 50, 55, 60]) == 21
    assert candidate(nums = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10]) == 38
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8, 9]) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9]) == 42
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == 5
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8, 7, 9]) == 9
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 9
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 21
    assert candidate(nums = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 29
    assert candidate(nums = [5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 81
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 7
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50]) == 9
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 92
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [1, 2, 3, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 6
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9]) == 11
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == 28
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 5, 8, 9, 7, 10, 11, 8]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 36
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 10, 12, 14, 16]) == 34
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 66
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == 18
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5]) == 18
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 26
    assert candidate(nums = [1, 3, 5, 7, 9, 10, 8, 11, 12]) == 26
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]) == 9
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 3
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 29
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 21
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5]) == 18
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 7, 5, 3, 1]) == 7
    assert candidate(nums = [8, 9, 7, 10, 11, 12, 13, 6]) == 4
