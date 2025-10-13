# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50],x = 10) == 90
    assert candidate(nums = [10, 20, 30, 40],x = 10) == 70
    assert candidate(nums = [1, 1, 1, 1, 1],x = 1) == 5
    assert candidate(nums = [7, 7, 7, 7, 7, 7],x = 2) == 42
    assert candidate(nums = [10, 20, 30, 40, 50],x = 1) == 54
    assert candidate(nums = [3, 1, 2],x = 3) == 6
    assert candidate(nums = [100, 200, 300],x = 50) == 400
    assert candidate(nums = [1, 2, 3],x = 4) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 10
    assert candidate(nums = [1000000000, 1000000000, 1000000000],x = 1000000000) == 3000000000
    assert candidate(nums = [1],x = 100) == 1
    assert candidate(nums = [5, 5, 5, 5],x = 10) == 20
    assert candidate(nums = [1, 3, 5, 7, 9],x = 2) == 13
    assert candidate(nums = [20, 1, 15],x = 5) == 13
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 10) == 45
    assert candidate(nums = [5, 5, 5, 5],x = 1) == 20
    assert candidate(nums = [10, 20, 30, 40],x = 5) == 55
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],x = 1) == 21
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],x = 30) == 540
    assert candidate(nums = [100, 200, 300, 400, 500],x = 500) == 1500
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],x = 10) == 190
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 3) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 1) == 39
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 100) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 2) == 27
    assert candidate(nums = [5, 8, 6, 3, 4, 7, 2, 9, 1],x = 3) == 26
    assert candidate(nums = [8, 6, 4, 2, 0, 2, 4, 6, 8],x = 1) == 8
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],x = 10) == 100
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 100) == 10
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10],x = 10) == 55
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3],x = 7) == 52
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],x = 2) == 70
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],x = 5) == 75
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],x = 20) == 200
    assert candidate(nums = [1000000000, 1000000000, 1000000000],x = 1000000000) == 3000000000
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],x = 15) == 55
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 2) == 28
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 100) == 10
    assert candidate(nums = [10, 20, 30, 40, 50],x = 3) == 62
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 5) == 45
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 10
    assert candidate(nums = [1, 1000000000, 1, 1000000000, 1],x = 500000000) == 500000005
    assert candidate(nums = [10, 20, 30, 40, 50],x = 15) == 105
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000],x = 500000000) == 1000000005
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 5) == 105
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 5) == 96
    assert candidate(nums = [7, 8, 9, 10, 11, 7, 8, 9, 10, 11],x = 2) == 78
    assert candidate(nums = [100, 200, 150, 100, 50],x = 75) == 500
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 5) == 90
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],x = 7) == 92
    assert candidate(nums = [3, 1, 2, 1, 3, 1, 2, 1, 3, 1],x = 1) == 11
    assert candidate(nums = [1, 10, 100, 1000, 10000],x = 1000) == 2112
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 3) == 34
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],x = 100000000) == 100000010
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 1) == 17
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],x = 2) == 24
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],x = 25) == 525
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20],x = 10) == 165
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],x = 1) == 10000
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8],x = 2) == 23
    assert candidate(nums = [5, 9, 3, 8, 2, 7, 4, 6, 1],x = 10) == 35
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],x = 7) == 34
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 25) == 305
    assert candidate(nums = [29, 10, 6, 3, 5, 30, 50, 100, 3, 8, 9, 12, 15, 16, 20, 23, 25, 28, 30, 32],x = 15) == 220
    assert candidate(nums = [1, 3, 2, 4, 5],x = 10) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 20
    assert candidate(nums = [7, 8, 9, 1, 2, 3, 4, 5, 6],x = 3) == 30
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 10) == 190
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 1) == 17
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],x = 500000000) == 4000000000
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7],x = 8) == 56
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 500) == 4500
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 15) == 55
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],x = 7) == 248
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],x = 5) == 145
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],x = 7) == 34
    assert candidate(nums = [10, 20, 30, 40, 50],x = 7) == 78
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],x = 5) == 145
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 5) == 51
    assert candidate(nums = [5, 4, 3, 2, 1],x = 1) == 9
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],x = 1000000000) == 4000000000
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],x = 10) == 135
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 0],x = 4) == 21
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 10) == 80
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],x = 100000000) == 100000010
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],x = 3) == 140
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 10) == 45
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 50) == 1450
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 2) == 27
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 100) == 100
    assert candidate(nums = [3, 2, 1, 4, 5],x = 2) == 12
    assert candidate(nums = [10, 1, 10, 1, 10],x = 5) == 15
    assert candidate(nums = [10, 10, 1, 10, 10],x = 2) == 13
    assert candidate(nums = [50, 40, 30, 20, 10, 100, 90, 80, 70, 60],x = 15) == 230
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],x = 20) == 231
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000],x = 50000) == 61112
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 100) == 1900
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10],x = 1) == 19
    assert candidate(nums = [1000000000, 1000000000, 1000000000],x = 500000000) == 3000000000
    assert candidate(nums = [10, 20, 30, 40, 50],x = 5) == 70
