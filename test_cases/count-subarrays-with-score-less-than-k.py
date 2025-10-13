# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5],k = 100) == 15
    assert candidate(nums = [10, 10, 10],k = 100) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 24
    assert candidate(nums = [1, 1, 1],k = 5) == 5
    assert candidate(nums = [1],k = 2) == 1
    assert candidate(nums = [5, 5, 5, 5],k = 20) == 4
    assert candidate(nums = [10, 20, 30],k = 100) == 4
    assert candidate(nums = [5, 5, 5, 5],k = 25) == 7
    assert candidate(nums = [2, 1, 4, 3, 5],k = 10) == 6
    assert candidate(nums = [10, 5, 2, 6],k = 100) == 10
    assert candidate(nums = [5, 5, 5, 5, 5],k = 25) == 9
    assert candidate(nums = [1, 2, 3, 4, 5],k = 75) == 14
    assert candidate(nums = [10, 20, 30, 40, 50],k = 200) == 10
    assert candidate(nums = [5, 5, 5, 5],k = 15) == 4
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 10) == 19
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1000) == 32
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 50) == 19
    assert candidate(nums = [3, 5, 2, 8, 6, 1],k = 25) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 30) == 24
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 30) == 19
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 50) == 74
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 74
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 20) == 23
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 100) == 26
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 100) == 34
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 10000) == 54
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 200) == 32
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 100) == 29
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == 34
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 18
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 100) == 23
    assert candidate(nums = [100, 200, 300, 400, 500],k = 100000) == 15
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000],k = 500000000000) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 24
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500000) == 55
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 400) == 37
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],k = 100000000000) == 21
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9],k = 50) == 13
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 200) == 101
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],k = 500) == 37
    assert candidate(nums = [3, 5, 7, 2, 8, 10],k = 100) == 17
    assert candidate(nums = [100, 200, 300, 400, 500],k = 10000) == 15
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100000) == 55
    assert candidate(nums = [5, 1, 3, 2, 5, 1, 2],k = 20) == 14
    assert candidate(nums = [9, 7, 5, 3, 1, 9, 7, 5, 3, 1],k = 100) == 34
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 300) == 32
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10000) == 55
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],k = 30) == 57
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 999990000000) == 55
    assert candidate(nums = [7, 3, 2, 8, 1, 2, 4],k = 20) == 11
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 20) == 20
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 81) == 19
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 57
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 25) == 22
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 50) == 54
    assert candidate(nums = [3, 2, 1, 4, 5],k = 20) == 10
    assert candidate(nums = [5, 4, 3, 2, 1],k = 15) == 8
    assert candidate(nums = [10, 1, 2, 3, 10, 2, 3, 10, 2, 3],k = 50) == 27
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 150) == 30
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50000) == 54
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 150) == 38
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 100) == 27
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 11) == 27
    assert candidate(nums = [50, 40, 30, 20, 10],k = 1000) == 15
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 22
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 10000000) == 28
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 100) == 203
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 150) == 29
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 50) == 34
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5000) == 55
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 27
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 500) == 40
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 150) == 53
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 54
    assert candidate(nums = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 150) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100) == 32
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5000) == 54
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 200) == 61
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 100) == 44
