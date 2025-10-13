# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],minK = 3,maxK = 7) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],minK = 3,maxK = 7) == 1
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5],minK = 2,maxK = 4) == 4
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],minK = 3,maxK = 7) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],minK = 1,maxK = 10) == 1
    assert candidate(nums = [2, 4, 3, 2, 4, 6],minK = 2,maxK = 4) == 8
    assert candidate(nums = [10, 9, 8, 7, 6],minK = 6,maxK = 10) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],minK = 2,maxK = 8) == 1
    assert candidate(nums = [1, 2, 3, 2, 1],minK = 1,maxK = 3) == 5
    assert candidate(nums = [10, 20, 30, 40, 50],minK = 10,maxK = 50) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],minK = 2,maxK = 5) == 4
    assert candidate(nums = [1, 2, 3, 4, 5],minK = 2,maxK = 4) == 1
    assert candidate(nums = [1, 3, 5, 2, 7, 5],minK = 1,maxK = 5) == 2
    assert candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],minK = 6,maxK = 6) == 55
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],minK = 1,maxK = 5) == 4
    assert candidate(nums = [5, 5, 5, 5, 5],minK = 5,maxK = 5) == 15
    assert candidate(nums = [5, 4, 3, 2, 1],minK = 2,maxK = 4) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],minK = 5,maxK = 5) == 55
    assert candidate(nums = [1, 1, 1, 1],minK = 1,maxK = 1) == 10
    assert candidate(nums = [2, 3, 5, 1, 5, 7, 5],minK = 1,maxK = 5) == 7
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],minK = 2,maxK = 9) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],minK = 2,maxK = 8) == 1
    assert candidate(nums = [2, 1, 5, 1, 3, 5, 4, 2],minK = 1,maxK = 5) == 20
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],minK = 5,maxK = 20) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],minK = 1,maxK = 5) == 108
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],minK = 2,maxK = 2) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],minK = 2,maxK = 9) == 3
    assert candidate(nums = [6, 2, 5, 3, 4, 2, 3, 2, 2, 3, 5, 4, 3, 2, 1],minK = 2,maxK = 5) == 47
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],minK = 2,maxK = 2) == 120
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1],minK = 1,maxK = 3) == 39
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],minK = 7,maxK = 7) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10],minK = 1,maxK = 10) == 38
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],minK = 3,maxK = 12) == 1
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8],minK = 3,maxK = 5) == 3
    assert candidate(nums = [10, 7, 5, 3, 2, 2, 5, 7, 10],minK = 2,maxK = 7) == 8
    assert candidate(nums = [3, 1, 5, 4, 2, 5, 1, 3, 4],minK = 1,maxK = 5) == 26
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],minK = 3,maxK = 3) == 210
    assert candidate(nums = [7, 9, 5, 6, 3, 1, 8, 4, 2, 5],minK = 3,maxK = 7) == 0
    assert candidate(nums = [7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10, 7, 8, 9, 10],minK = 7,maxK = 10) == 246
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1],minK = 1,maxK = 8) == 225
    assert candidate(nums = [5, 3, 3, 3, 1, 4, 5, 5, 2, 5],minK = 1,maxK = 5) == 22
    assert candidate(nums = [5, 3, 4, 5, 3, 5, 3, 4, 5, 3],minK = 3,maxK = 5) == 41
    assert candidate(nums = [1, 5, 3, 5, 2, 3, 5, 1, 2, 5],minK = 1,maxK = 5) == 28
    assert candidate(nums = [6, 4, 5, 1, 2, 3, 1, 5, 4, 6, 1, 2, 3, 1, 5, 4, 6, 1, 2, 3, 1, 5, 4, 6],minK = 1,maxK = 5) == 36
    assert candidate(nums = [1, 3, 2, 5, 4, 6, 5, 3, 2, 1, 4, 5, 6, 7, 8, 9],minK = 2,maxK = 8) == 0
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],minK = 5,maxK = 10) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1],minK = 1,maxK = 3) == 20
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],minK = 10,maxK = 15) == 1
    assert candidate(nums = [7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],minK = 1,maxK = 7) == 9
    assert candidate(nums = [10, 20, 10, 20, 30, 10, 20, 10],minK = 10,maxK = 20) == 9
    assert candidate(nums = [1, 5, 4, 5, 1, 1, 5, 2, 1, 3, 4, 5],minK = 1,maxK = 5) == 53
    assert candidate(nums = [7, 3, 3, 5, 7, 3, 5, 7, 3, 5],minK = 3,maxK = 7) == 38
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minK = 1,maxK = 1) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],minK = 4,maxK = 12) == 1
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],minK = 2,maxK = 4) == 2
    assert candidate(nums = [5, 4, 5, 3, 5, 4, 5, 2, 5, 4, 5, 3, 5, 4, 5, 1, 5, 4, 5, 3],minK = 1,maxK = 5) == 79
    assert candidate(nums = [1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],minK = 1,maxK = 3) == 103
    assert candidate(nums = [5, 3, 1, 4, 5, 2, 3, 4, 5, 2, 1, 4, 5, 3, 2, 1, 5],minK = 1,maxK = 5) == 100
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],minK = 2,maxK = 6) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],minK = 2,maxK = 5) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],minK = 1,maxK = 10) == 303
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8],minK = 5,maxK = 8) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],minK = 1,maxK = 10) == 102
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],minK = 8,maxK = 8) == 210
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7],minK = 3,maxK = 6) == 2
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1],minK = 1,maxK = 10) == 21
    assert candidate(nums = [1, 5, 3, 5, 2, 3, 1, 5, 2],minK = 1,maxK = 5) == 23
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],minK = 2,maxK = 4) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],minK = 3,maxK = 7) == 2
    assert candidate(nums = [5, 5, 3, 5, 2, 3, 3, 5, 3, 3, 5, 3, 2, 5, 5, 3, 3, 5, 5, 5],minK = 2,maxK = 5) == 139
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],minK = 1,maxK = 5) == 154
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],minK = 1,maxK = 5) == 106
    assert candidate(nums = [1, 3, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1],minK = 1,maxK = 5) == 175
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],minK = 6,maxK = 24) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160],minK = 10,maxK = 150) == 1
    assert candidate(nums = [7, 8, 9, 10, 7, 8, 9, 10, 7, 8],minK = 7,maxK = 10) == 34
    assert candidate(nums = [7, 3, 5, 1, 5, 2, 5, 5, 2, 5, 1, 5, 3, 7],minK = 1,maxK = 7) == 21
    assert candidate(nums = [2, 1, 3, 3, 2, 3, 1, 2, 3, 2, 1, 2, 3],minK = 1,maxK = 3) == 63
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],minK = 1,maxK = 5) == 312
    assert candidate(nums = [1, 3, 1, 3, 5, 1, 3, 5, 2, 5, 3, 2, 3, 1, 2, 3, 5, 1, 3, 5, 2, 5],minK = 1,maxK = 5) == 181
    assert candidate(nums = [100, 200, 100, 300, 200, 100, 300, 200, 100],minK = 100,maxK = 300) == 29
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 9, 7, 5, 3, 1, 2, 4, 6, 8],minK = 3,maxK = 9) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 2, 3, 4, 5],minK = 2,maxK = 5) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],minK = 3,maxK = 8) == 1
    assert candidate(nums = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6],minK = 5,maxK = 6) == 190
    assert candidate(nums = [2, 4, 2, 1, 5, 4, 2, 3, 5, 1],minK = 1,maxK = 5) == 29
    assert candidate(nums = [8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 7, 8, 9],minK = 6,maxK = 9) == 10
    assert candidate(nums = [3, 6, 3, 7, 3, 5, 3, 4, 3, 3],minK = 3,maxK = 7) == 27
    assert candidate(nums = [5, 1, 3, 5, 7, 5, 3, 1, 5],minK = 1,maxK = 5) == 8
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],minK = 1,maxK = 2) == 45
    assert candidate(nums = [5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5],minK = 1,maxK = 5) == 110
    assert candidate(nums = [1, 5, 3, 5, 3, 5, 3, 5, 3, 1],minK = 1,maxK = 5) == 16
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],minK = 3,maxK = 7) == 1
    assert candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],minK = 6,maxK = 6) == 55
    assert candidate(nums = [2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4],minK = 2,maxK = 4) == 120
    assert candidate(nums = [1000000, 999999, 1000000, 999999, 1000000, 999999, 1000000],minK = 999999,maxK = 1000000) == 21
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],minK = 5,maxK = 10) == 4
    assert candidate(nums = [2, 1, 5, 3, 5, 1, 5, 2, 5, 1, 5, 3, 2, 1],minK = 1,maxK = 5) == 79
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],minK = 3,maxK = 8) == 2
    assert candidate(nums = [2, 1, 3, 4, 5, 1, 5, 2],minK = 1,maxK = 5) == 19
    assert candidate(nums = [3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 5, 5, 5, 5],minK = 1,maxK = 5) == 48
    assert candidate(nums = [1, 3, 2, 5, 4, 6, 5, 4, 3, 2, 1, 3, 5, 2, 4, 6, 5, 4, 3, 2, 1],minK = 2,maxK = 5) == 10
    assert candidate(nums = [5, 3, 1, 3, 1, 5, 3, 1, 3, 1, 5, 3, 1, 3, 1],minK = 1,maxK = 5) == 84
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],minK = 5,maxK = 10) == 3
    assert candidate(nums = [1, 2, 2, 3, 4, 3, 5, 2, 3, 4, 5, 3, 4, 5, 3, 4, 2, 3, 4, 5, 3, 4, 2, 5, 3, 4, 5],minK = 2,maxK = 5) == 256
    assert candidate(nums = [6, 4, 5, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],minK = 2,maxK = 5) == 4
    assert candidate(nums = [5, 1, 2, 3, 4, 5, 6, 7, 8, 9],minK = 5,maxK = 9) == 1
    assert candidate(nums = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4],minK = 1,maxK = 4) == 75
    assert candidate(nums = [2, 1, 5, 3, 4, 2, 1, 5, 3, 4, 2, 1, 5, 3, 4],minK = 1,maxK = 5) == 83
    assert candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 1, 5, 2, 5, 3, 5, 4, 5, 1, 5, 2],minK = 1,maxK = 5) == 147
    assert candidate(nums = [1, 5, 3, 4, 2, 1, 5, 4, 3, 2],minK = 2,maxK = 5) == 2
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],minK = 1,maxK = 5) == 51
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],minK = 3,maxK = 7) == 4
    assert candidate(nums = [1, 1000000, 1, 1000000, 1, 1000000, 1, 1000000, 1, 1000000, 1, 1000000],minK = 1,maxK = 1000000) == 66
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1],minK = 1,maxK = 4) == 46
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4],minK = 2,maxK = 4) == 8
