# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 1) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 8) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8],k = 4) == 4
    assert candidate(nums = [6, 3, 8, 1, 3, 1, 2, 2],k = 4) == 6
    assert candidate(nums = [1, 2, 1, 4],k = 2) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8],k = 2) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 4) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 16) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4],k = 4) == 4
    assert candidate(nums = [5, 3, 3, 6, 3, 3],k = 3) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],k = 1) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 2) == 14
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4],k = 8) == 0
    assert candidate(nums = [1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14],k = 2) == 18
    assert candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 4) == 12
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7],k = 4) == 14
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],k = 4) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3],k = 3) == -1
    assert candidate(nums = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8, 9, 10, 11, 12],k = 3) == -1
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],k = 6) == 10
    assert candidate(nums = [1, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10],k = 2) == -1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 6) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9],k = 7) == 9
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6],k = 4) == 14
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 1],k = 2) == 14
    assert candidate(nums = [2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],k = 6) == 9
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],k = 8) == 8
    assert candidate(nums = [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],k = 4) == 12
    assert candidate(nums = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11],k = 4) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 2) == 14
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7],k = 2) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15],k = 5) == -1
    assert candidate(nums = [1, 3, 2, 6, 4, 5, 7, 8, 10, 9, 12, 11, 14, 13, 16, 15],k = 4) == 12
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 20
    assert candidate(nums = [1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 9, 9],k = 3) == -1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9],k = 4) == 13
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14],k = 4) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 14, 15, 16],k = 6) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11],k = 3) == -1
    assert candidate(nums = [1, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10, 10, 11, 12],k = 4) == 15
    assert candidate(nums = [1, 3, 3, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17],k = 8) == 16
    assert candidate(nums = [1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17],k = 4) == 24
    assert candidate(nums = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12],k = 8) == 11
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6],k = 4) == -1
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13],k = 4) == 17
    assert candidate(nums = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5],k = 5) == -1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],k = 4) == 13
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 4) == 13
    assert candidate(nums = [1, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11],k = 4) == 22
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],k = 4) == 13
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 4) == 12
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 6) == 8
    assert candidate(nums = [2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9],k = 3) == -1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],k = 8) == 8
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16],k = 4) == 16
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7],k = 8) == 8
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == -1
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6],k = 4) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 8) == 8
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8],k = 8) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 10, 11, 12, 13, 13],k = 4) == 16
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 10],k = 5) == -1
    assert candidate(nums = [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],k = 2) == -1
    assert candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 2) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13],k = 4) == 15
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 8) == 9
    assert candidate(nums = [6, 3, 8, 1, 3, 1, 2, 2, 4, 5, 7, 9, 10, 11, 12, 13],k = 4) == 13
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],k = 2) == 14
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 17
    assert candidate(nums = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],k = 4) == 12
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 9) == 10
    assert candidate(nums = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 13],k = 4) == 16
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],k = 2) == -1
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 9) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15],k = 8) == 9
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11],k = 4) == 14
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 4) == 16
    assert candidate(nums = [2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 10, 11, 12, 12],k = 8) == 10
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7],k = 4) == 12
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],k = 4) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == -1
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],k = 2) == 14
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6],k = 3) == -1
    assert candidate(nums = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],k = 3) == -1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9],k = 3) == -1
    assert candidate(nums = [1, 3, 3, 3, 3, 5, 5, 5, 7, 7, 7, 7, 9, 9, 9, 9],k = 2) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 12, 13, 14, 15, 16],k = 8) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 1) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8],k = 4) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10, 10, 11, 12, 13],k = 4) == 13
