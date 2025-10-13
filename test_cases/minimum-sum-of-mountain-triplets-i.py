# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 4, 8, 7, 10, 2]) == 13
    assert candidate(nums = [1, 5, 3, 6, 4, 7, 2]) == 6
    assert candidate(nums = [10, 20, 15, 30, 25, 40]) == 45
    assert candidate(nums = [3, 3, 3, 3, 3, 3]) == -1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 6
    assert candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9]) == -1
    assert candidate(nums = [1, 3, 1, 3, 1]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5]) == -1
    assert candidate(nums = [10, 20, 3, 40, 5, 60, 70, 8]) == 33
    assert candidate(nums = [1, 3, 2, 1, 2, 3]) == 4
    assert candidate(nums = [1, 2, 1, 2, 1, 2]) == 4
    assert candidate(nums = [2, 1, 3, 4, 3, 2, 1]) == 4
    assert candidate(nums = [3, 1, 4, 2, 5]) == 7
    assert candidate(nums = [6, 5, 4, 3, 4, 5]) == -1
    assert candidate(nums = [5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8]) == 6
    assert candidate(nums = [1, 5, 3, 5, 1]) == 5
    assert candidate(nums = [7, 1, 3, 2, 4, 6, 5]) == 6
    assert candidate(nums = [8, 6, 1, 5, 3]) == 9
    assert candidate(nums = [3, 2, 1, 4, 5, 3, 2, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2, 8, 7, 6, 5, 4, 3, 2]) == 6
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 40, 35, 45]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(nums = [7, 8, 9, 1, 10, 2, 11, 3, 12, 4, 13, 5, 14, 6, 15]) == 13
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
    assert candidate(nums = [42, 21, 31, 41, 10, 20, 30, 50, 15, 25, 35, 45, 5, 1, 6, 11, 16, 26, 36, 46]) == 26
    assert candidate(nums = [8, 7, 10, 9, 12, 11, 14, 13, 16, 15]) == 26
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == 8
    assert candidate(nums = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 4
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == -1
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [5, 3, 1, 2, 4, 6, 7, 8, 10, 9]) == 20
    assert candidate(nums = [30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == -1
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 6
    assert candidate(nums = [2, 1, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 8
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 4
    assert candidate(nums = [8, 1, 5, 10, 3, 12, 7, 9]) == 9
    assert candidate(nums = [40, 20, 30, 10, 50, 35, 45, 25, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110, 105]) == 60
    assert candidate(nums = [2, 3, 1, 4, 5, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 45, 50]) == 30
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 50]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 50]) == -1
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5]) == 12
    assert candidate(nums = [47, 45, 43, 41, 39, 40, 42, 44, 46, 48, 50, 49, 47, 45, 43]) == 126
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15]) == 12
    assert candidate(nums = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1]) == 5
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10]) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 4
    assert candidate(nums = [30, 20, 10, 5, 15, 25, 35, 40, 30, 25, 20, 15, 10, 5, 0]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 4
    assert candidate(nums = [15, 10, 12, 11, 13, 9, 14, 8, 16, 7, 17, 6, 18, 5, 19, 4, 20, 3, 21, 2]) == 23
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [50, 1, 50, 2, 50, 3, 50, 4, 50, 5, 50, 6, 50, 7, 50]) == 53
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19]) == 70
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == -1
    assert candidate(nums = [30, 10, 20, 15, 25, 5, 35, 5, 10, 40]) == 30
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11]) == 14
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 40, 35]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [2, 1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]) == 6
    assert candidate(nums = [10, 20, 15, 25, 5, 30, 22, 18, 17, 28]) == 30
    assert candidate(nums = [2, 5, 3, 8, 6, 4, 9, 7, 10, 1]) == 6
    assert candidate(nums = [4, 5, 1, 6, 2, 7, 3, 8, 9, 10, 11]) == 9
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
    assert candidate(nums = [20, 15, 10, 5, 6, 7, 8, 12, 11, 16]) == 28
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == -1
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == -1
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 4
    assert candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [10, 20, 30, 40, 35, 25, 15, 10, 20, 30, 40, 35, 25, 15]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [50, 1, 50, 1, 50, 1, 50, 1, 50, 1]) == 52
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 51, 52, 53, 54, 55]) == -1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 6
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 6
    assert candidate(nums = [10, 20, 30, 25, 15, 5, 25, 30, 10]) == 30
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8]) == 18
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 13
    assert candidate(nums = [25, 20, 15, 30, 25, 20, 35, 30, 25, 40, 35, 30, 45, 40, 35]) == 60
    assert candidate(nums = [5, 3, 8, 6, 7, 4, 9, 2, 10, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [20, 15, 10, 25, 30, 5, 40, 45, 50]) == 40
    assert candidate(nums = [9, 1, 2, 3, 8, 5, 6, 4, 7]) == 10
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == -1
    assert candidate(nums = [10, 20, 5, 15, 25, 10, 30, 5, 40]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 5, 3, 4, 2, 6, 8, 7, 9, 10, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(nums = [25, 20, 15, 10, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == -1
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 13
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5]) == 8
    assert candidate(nums = [2, 1, 3, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10]) == 8
    assert candidate(nums = [10, 20, 15, 25, 5, 30, 10]) == 30
    assert candidate(nums = [10, 20, 30, 25, 15, 27, 17, 28, 18, 29, 9, 19, 21, 22, 23]) == 34
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5]) == 8
    assert candidate(nums = [3, 2, 1, 4, 3, 2, 5, 4, 3, 6, 5, 4, 7, 6, 5, 8, 7, 6, 9, 8, 7, 10, 9, 8]) == 6
    assert candidate(nums = [3, 5, 1, 4, 2, 6, 7, 8, 9, 10, 11, 12, 13]) == 7
    assert candidate(nums = [2, 1, 3, 4, 3, 2, 4, 3, 2, 1, 3, 4, 3, 2, 4, 3, 2, 1, 3, 4, 3, 2]) == 4
    assert candidate(nums = [30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30]) == -1
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [8, 1, 9, 3, 7, 5, 11, 2, 13, 4]) == 6
    assert candidate(nums = [30, 20, 10, 25, 15, 35, 40, 45, 50]) == 50
