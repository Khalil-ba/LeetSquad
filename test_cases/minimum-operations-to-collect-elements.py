# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [2, 1, 2, 1, 2],k = 2) == 2
    assert candidate(nums = [2, 3, 1, 4, 5],k = 4) == 5
    assert candidate(nums = [3, 1, 5, 4, 2],k = 5) == 5
    assert candidate(nums = [4, 3, 2, 1, 5],k = 5) == 5
    assert candidate(nums = [2, 4, 6, 8, 10],k = 3) == None
    assert candidate(nums = [1, 2, 2, 3, 3],k = 3) == 5
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 5
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(nums = [5, 4, 3, 2, 1],k = 5) == 5
    assert candidate(nums = [1, 3, 2, 5, 4],k = 4) == 5
    assert candidate(nums = [2, 2, 2, 1, 3],k = 3) == 3
    assert candidate(nums = [5, 1, 2, 3, 4],k = 1) == 4
    assert candidate(nums = [3, 1, 5, 4, 2],k = 2) == 4
    assert candidate(nums = [1, 3, 5, 7, 9],k = 1) == 5
    assert candidate(nums = [1, 3, 5, 7, 9],k = 4) == None
    assert candidate(nums = [1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [2, 4, 3, 1, 5],k = 4) == 5
    assert candidate(nums = [2, 4, 1, 3, 5],k = 2) == 5
    assert candidate(nums = [2, 4, 1, 3, 5],k = 4) == 5
    assert candidate(nums = [5, 3, 1, 4, 2],k = 2) == 3
    assert candidate(nums = [3, 2, 5, 3, 1],k = 3) == 4
    assert candidate(nums = [5, 4, 3, 2, 1],k = 3) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 10
    assert candidate(nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],k = 5) == 10
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 2, 3, 4, 5, 6],k = 6) == 6
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1],k = 7) == 7
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],k = 1) == 1
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 10
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 50
    assert candidate(nums = [5, 3, 2, 1, 4, 6, 7],k = 7) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 25) == 25
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1],k = 7) == 7
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],k = 5) == 5
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1],k = 3) == 3
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1],k = 3) == 10
    assert candidate(nums = [5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 20
    assert candidate(nums = [5, 3, 2, 1, 4, 6, 7, 8, 9, 10],k = 10) == 10
    assert candidate(nums = [4, 5, 3, 2, 1, 6, 7],k = 5) == 7
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 5) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(nums = [3, 6, 5, 2, 8, 7, 4, 1, 9, 10],k = 5) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 3) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],k = 1) == 1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],k = 1) == 1
    assert candidate(nums = [2, 1, 1, 3, 1, 2, 1, 2, 3],k = 3) == 3
    assert candidate(nums = [2, 1, 5, 4, 3, 6, 8, 7, 10, 9, 12, 11],k = 6) == 12
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13],k = 13) == 13
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 15
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 50) == 50
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2],k = 20) == 20
    assert candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 15
    assert candidate(nums = [5, 1, 3, 2, 4, 6, 7],k = 5) == 7
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 15
    assert candidate(nums = [6, 3, 1, 5, 4, 2, 7, 8, 9, 10],k = 10) == 10
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 20
    assert candidate(nums = [7, 1, 6, 2, 5, 3, 4, 8, 9, 10],k = 10) == 10
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3],k = 3) == 3
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10],k = 5) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],k = 10) == 10
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 1, 2, 3],k = 3) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 9
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 1) == None
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == None
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 15
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 25) == 25
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1) == None
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 45) == 50
    assert candidate(nums = [7, 3, 5, 1, 2, 6, 4],k = 7) == 7
    assert candidate(nums = [5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2],k = 5) == 5
    assert candidate(nums = [4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2],k = 4) == 4
    assert candidate(nums = [3, 2, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 15) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(nums = [5, 3, 1, 2, 4, 6],k = 4) == 5
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 5) == 9
    assert candidate(nums = [5, 1, 3, 4, 2, 5, 4, 3, 2, 1],k = 5) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 15
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 10
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 5) == 5
    assert candidate(nums = [5, 3, 6, 1, 2, 8, 4, 7, 9, 10],k = 10) == 10
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 10
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],k = 10) == 10
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6],k = 6) == 21
    assert candidate(nums = [5, 3, 1, 4, 2, 3, 1, 4, 2, 5],k = 5) == 5
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == None
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 5
    assert candidate(nums = [4, 3, 2, 1, 4, 3, 2, 1],k = 4) == 4
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 10) == 10
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 15
    assert candidate(nums = [3, 5, 1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 15
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 10) == 18
    assert candidate(nums = [3, 6, 5, 3, 7, 8, 9, 1, 2, 4, 5, 6, 7, 8, 9],k = 9) == 12
    assert candidate(nums = [4, 4, 4, 4, 4, 1, 2, 3, 4, 5],k = 5) == 5
