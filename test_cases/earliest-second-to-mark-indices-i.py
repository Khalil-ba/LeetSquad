# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 0, 1, 0],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 6
    assert candidate(nums = [10, 0, 10],changeIndices = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == -1
    assert candidate(nums = [0, 0, 0, 0],changeIndices = [1, 2, 3, 4]) == 4
    assert candidate(nums = [1, 3],changeIndices = [1, 1, 1, 2, 1, 1, 1]) == 6
    assert candidate(nums = [0, 0, 0],changeIndices = [1, 2, 3]) == 3
    assert candidate(nums = [5, 4, 3],changeIndices = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == -1
    assert candidate(nums = [1, 2, 3, 4],changeIndices = [4, 3, 2, 1, 4, 3, 2, 1]) == -1
    assert candidate(nums = [10, 20, 30, 40],changeIndices = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == -1
    assert candidate(nums = [3, 3, 3, 3],changeIndices = [4, 3, 2, 1, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 1, 1, 1],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [10, 10, 10, 10],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
    assert candidate(nums = [0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4]) == 4
    assert candidate(nums = [100, 200, 300],changeIndices = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == -1
    assert candidate(nums = [10, 10, 10],changeIndices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == -1
    assert candidate(nums = [0, 1],changeIndices = [2, 2, 2]) == -1
    assert candidate(nums = [1000000000, 1000000000],changeIndices = [1, 2, 1, 2, 1, 2]) == -1
    assert candidate(nums = [100, 0, 50],changeIndices = [1, 1, 1, 3, 3, 3, 2, 2, 2]) == -1
    assert candidate(nums = [2, 2, 0],changeIndices = [2, 2, 2, 2, 3, 2, 2, 1]) == 8
    assert candidate(nums = [5, 5, 5],changeIndices = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == -1
    assert candidate(nums = [1, 0, 3],changeIndices = [3, 3, 3, 1, 1, 2, 2, 2]) == -1
    assert candidate(nums = [1, 2, 3, 4],changeIndices = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 14
    assert candidate(nums = [3, 2, 1],changeIndices = [3, 2, 1, 3, 2, 1]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [10, 20, 30],changeIndices = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == -1
    assert candidate(nums = [10, 10, 10],changeIndices = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]) == 16
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],changeIndices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [100, 200, 300, 400],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 4
    assert candidate(nums = [1, 0, 1, 0, 1, 0],changeIndices = [2, 4, 6, 1, 3, 5, 1, 3, 5, 2, 4, 6]) == 9
    assert candidate(nums = [0, 0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [5, 5, 5, 5, 5],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],changeIndices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5],changeIndices = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [2, 3, 5, 7, 11, 13],changeIndices = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]) == -1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],changeIndices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9],changeIndices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
    assert candidate(nums = [10, 20, 30, 40],changeIndices = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == -1
    assert candidate(nums = [100, 200, 300],changeIndices = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],changeIndices = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50],changeIndices = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == -1
    assert candidate(nums = [100, 100, 100, 100],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
    assert candidate(nums = [10, 0, 0, 10],changeIndices = [4, 4, 4, 1, 1, 1, 4, 4, 4, 1, 1, 1]) == -1
    assert candidate(nums = [5, 7, 9, 10],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
    assert candidate(nums = [5, 5, 5, 5, 5],changeIndices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [5, 5, 5, 5, 5, 5],changeIndices = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [100, 200, 300, 400],changeIndices = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]) == 7
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],changeIndices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],changeIndices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [0, 10, 20, 30, 40],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 0, 2, 3, 4],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70],changeIndices = [7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [100, 200, 300],changeIndices = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],changeIndices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],changeIndices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == -1
    assert candidate(nums = [5, 0, 2, 7, 3],changeIndices = [1, 5, 3, 4, 4, 2, 5, 3, 1, 2, 4, 3]) == -1
    assert candidate(nums = [10, 20, 30, 40],changeIndices = [4, 3, 2, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
    assert candidate(nums = [999999999, 999999999, 999999999],changeIndices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == -1
    assert candidate(nums = [5, 10, 15, 20],changeIndices = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1000000000, 1000000000, 1000000000],changeIndices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == -1
    assert candidate(nums = [0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 4
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0],changeIndices = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],changeIndices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1000000000, 1000000000, 1000000000],changeIndices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [5, 0, 8, 3],changeIndices = [4, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums = [9, 8, 7, 6, 5],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [100, 200, 300, 400],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1000000000, 1000000000, 1000000000],changeIndices = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == -1
    assert candidate(nums = [1000000000, 1000000000, 1000000000],changeIndices = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == -1
    assert candidate(nums = [5, 5, 5, 5, 5],changeIndices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [100, 0, 50, 25, 75],changeIndices = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [100, 200, 300, 400, 500],changeIndices = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50],changeIndices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == -1
    assert candidate(nums = [0, 0, 1, 1, 2, 2],changeIndices = [3, 3, 4, 4, 5, 5, 1, 1, 2, 2]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [0, 0, 0, 0],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4]) == 4
    assert candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1000000000, 1000000000],changeIndices = [1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == -1
    assert candidate(nums = [100, 200, 300, 400],changeIndices = [4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1000, 1000, 1000, 1000],changeIndices = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == -1
    assert candidate(nums = [1, 0, 0, 1],changeIndices = [4, 4, 4, 1, 1, 1, 4, 4, 4, 1, 1, 1, 4, 4, 4, 1, 1, 1]) == -1
    assert candidate(nums = [10, 20, 30],changeIndices = [1, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3]) == -1
    assert candidate(nums = [1, 0, 0, 0, 1],changeIndices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],changeIndices = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8],changeIndices = [8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1],changeIndices = [1, 3, 5, 7, 2, 4, 6, 1, 3, 5, 7, 2, 4, 6]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],changeIndices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],changeIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums = [10, 20, 30, 40],changeIndices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == -1
