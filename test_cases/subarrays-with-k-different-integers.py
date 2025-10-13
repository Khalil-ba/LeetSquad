# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [4, 2, 4, 5, 6],k = 2) == 5
    assert candidate(nums = [1, 2, 1, 3, 4],k = 3) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 55
    assert candidate(nums = [1, 2, 2, 1, 1, 3],k = 2) == 10
    assert candidate(nums = [1, 2, 3],k = 2) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6],k = 3) == 4
    assert candidate(nums = [1, 2],k = 1) == 2
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 3, 4],k = 3) == 9
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6
    assert candidate(nums = [1],k = 1) == 1
    assert candidate(nums = [1, 2, 1, 2, 3],k = 2) == 7
    assert candidate(nums = [5, 5, 5, 5, 5],k = 1) == 15
    assert candidate(nums = [1, 2, 2, 1, 1],k = 2) == 8
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 6
    assert candidate(nums = [1, 2, 2, 1, 3],k = 2) == 6
    assert candidate(nums = [1, 1, 1, 1, 1],k = 1) == 15
    assert candidate(nums = [1, 2, 2, 1, 2],k = 2) == 9
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1],k = 2) == 11
    assert candidate(nums = [1, 1, 2, 2, 3, 3],k = 2) == 8
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 55
    assert candidate(nums = [1, 2, 3, 2, 2, 3, 1, 2, 3],k = 3) == 22
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3],k = 2) == 18
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 5
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 253
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 21
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9],k = 5) == 143
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 11
    assert candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],k = 4) == 91
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 210
    assert candidate(nums = [1, 2, 2, 1, 3, 1, 4, 2],k = 3) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 26
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2],k = 2) == 13
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 3) == 18
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 3) == 19
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 3) == 35
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 66
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 237
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1],k = 2) == 42
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20],k = 10) == 44
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 4],k = 2) == 9
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 2, 3, 1, 4],k = 3) == 14
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 2, 1, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 29
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],k = 4) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 6
    assert candidate(nums = [1, 1, 2, 3, 2, 3, 3, 4, 4, 4, 4, 4],k = 3) == 23
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3],k = 4) == 18
    assert candidate(nums = [1, 2, 2, 1, 3, 4, 3, 2, 1],k = 2) == 11
    assert candidate(nums = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2],k = 2) == 100
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 2) == 14
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 5) == 0
    assert candidate(nums = [1, 1, 2, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 75
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 20, 30, 10, 40],k = 3) == 14
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 7) == 24
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 16
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],k = 4) == 36
    assert candidate(nums = [10, 20, 30, 10, 20, 30, 10, 20, 30],k = 2) == 8
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 136
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == 7
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9],k = 3) == 63
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 4) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 1
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 378
    assert candidate(nums = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1],k = 2) == 21
    assert candidate(nums = [1, 2, 1, 2, 3, 3, 4, 4, 5, 5],k = 3) == 12
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 120
    assert candidate(nums = [5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 253
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 136
    assert candidate(nums = [1, 2, 2, 1, 1, 3, 4, 3, 2, 1],k = 2) == 15
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 190
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 3) == 11
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8],k = 4) == 20
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 16
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 190
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2],k = 2) == 28
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 3) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 0
    assert candidate(nums = [1, 2, 2, 1, 3, 2, 4, 5, 3],k = 3) == 10
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8],k = 3) == 48
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],k = 2) == 36
    assert candidate(nums = [1, 2, 3, 2, 2, 3, 1, 1, 2, 3, 3, 3, 2, 1],k = 2) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 3) == 13
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 24
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 66
    assert candidate(nums = [4, 2, 4, 4, 2, 2, 3, 1, 1, 4],k = 2) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 4) == 20
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 93
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 4) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 16
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 2) == 29
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12],k = 5) == 32
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 3, 2, 1],k = 2) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == 22
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 3, 2, 1, 4, 4, 5, 5, 5, 5, 5],k = 3) == 27
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 55
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 11
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 1, 1, 2, 2, 3, 3],k = 4) == 72
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],k = 3) == 72
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 5) == 106
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 2, 1, 1, 1],k = 3) == 162
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 2, 1, 4, 4, 3, 2, 1],k = 2) == 16
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],k = 5) == 80
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 4) == 24
    assert candidate(nums = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 5) == 6
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],k = 3) == 36
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 45
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 2, 1, 4, 4, 3, 2, 1, 5, 5, 4, 3, 2, 1, 6, 6, 5, 4, 3, 2, 1, 7, 7, 6, 5, 4, 3, 2, 1, 8, 8, 7, 6, 5, 4, 3, 2, 1, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 541
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 21
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 2],k = 3) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5],k = 5) == 21
