# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(stoneValue = [1, 2, 3, 4, 5]) == 10
    assert candidate(stoneValue = [5, 3, 1, 4, 2]) == 9
    assert candidate(stoneValue = [1, 3, 5, 7, 9, 11, 13]) == 35
    assert candidate(stoneValue = [3, 6, 2, 8, 7, 4, 5]) == 23
    assert candidate(stoneValue = [3, 2, 4, 1, 4, 1, 3, 2]) == 17
    assert candidate(stoneValue = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 40
    assert candidate(stoneValue = [3, 1, 5, 4, 2]) == 8
    assert candidate(stoneValue = [4]) == 0
    assert candidate(stoneValue = [1, 100, 1]) == 1
    assert candidate(stoneValue = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 35
    assert candidate(stoneValue = [6, 2, 3, 4, 5, 5]) == 18
    assert candidate(stoneValue = [7, 7, 7, 7, 7, 7, 7]) == 28
    assert candidate(stoneValue = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(stoneValue = [10, 10, 10, 10, 10, 10]) == 40
    assert candidate(stoneValue = [3, 6, 1, 2, 5, 4]) == 13
    assert candidate(stoneValue = [1000000, 1000000]) == 1000000
    assert candidate(stoneValue = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 37
    assert candidate(stoneValue = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 84
    assert candidate(stoneValue = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 35
    assert candidate(stoneValue = [1000000, 1000000]) == 1000000
    assert candidate(stoneValue = [10, 10, 10, 10, 10]) == 30
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 277
    assert candidate(stoneValue = [100, 200, 300, 400, 500, 400, 300, 200, 100]) == 1400
    assert candidate(stoneValue = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 366
    assert candidate(stoneValue = [15, 20, 5, 10, 25, 30, 5]) == 70
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 92
    assert candidate(stoneValue = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 125
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 1179
    assert candidate(stoneValue = [1000000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]) == 3700000
    assert candidate(stoneValue = [1000000, 1, 1000000, 1, 1000000]) == 1000002
    assert candidate(stoneValue = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 35
    assert candidate(stoneValue = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 194
    assert candidate(stoneValue = [1000000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 35
    assert candidate(stoneValue = [5, 1, 4, 9, 7, 2, 8, 6, 3]) == 31
    assert candidate(stoneValue = [5, 3, 8, 2, 7, 9, 1, 4, 6, 10]) == 36
    assert candidate(stoneValue = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 184
    assert candidate(stoneValue = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(stoneValue = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 137
    assert candidate(stoneValue = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 35
    assert candidate(stoneValue = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 26
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 92
    assert candidate(stoneValue = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 920
    assert candidate(stoneValue = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 79
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 80
    assert candidate(stoneValue = [100, 200, 300, 400, 500, 150, 250, 350, 450, 550]) == 2500
    assert candidate(stoneValue = [1, 2, 3, 4, 3, 2, 1]) == 10
    assert candidate(stoneValue = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 184
    assert candidate(stoneValue = [1000000, 1, 1000000, 1, 1000000, 1, 1000000, 1, 1000000, 1, 1000000, 1, 1000000, 1, 1000000]) == 7000004
    assert candidate(stoneValue = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == 55
    assert candidate(stoneValue = [1000000, 500000, 750000, 250000, 600000, 400000]) == 2000000
    assert candidate(stoneValue = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 74
    assert candidate(stoneValue = [1000000, 999999, 999998, 999997, 999996, 999995]) == 3999985
    assert candidate(stoneValue = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 357
    assert candidate(stoneValue = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 21
    assert candidate(stoneValue = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 460
    assert candidate(stoneValue = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 35
    assert candidate(stoneValue = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(stoneValue = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 800
    assert candidate(stoneValue = [10, 5, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 945
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 189
    assert candidate(stoneValue = [100, 50, 30, 20, 10, 5, 1]) == 100
    assert candidate(stoneValue = [8, 6, 4, 2, 1, 3, 5, 7, 9]) == 32
    assert candidate(stoneValue = [23, 45, 12, 67, 89, 34, 56, 78, 90, 12, 34, 56, 78, 90]) == 606
    assert candidate(stoneValue = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 90
    assert candidate(stoneValue = [1000000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]) == 3700000
    assert candidate(stoneValue = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 1780
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 25
    assert candidate(stoneValue = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3700
    assert candidate(stoneValue = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 555
    assert candidate(stoneValue = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == 165
    assert candidate(stoneValue = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 1890
    assert candidate(stoneValue = [20, 30, 10, 40, 50, 15, 25, 35]) == 170
    assert candidate(stoneValue = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 278
    assert candidate(stoneValue = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 35
    assert candidate(stoneValue = [50, 25, 75, 100, 200, 150, 300, 50, 25, 75, 100, 200, 150, 300, 50]) == 1625
    assert candidate(stoneValue = [42, 33, 24, 15, 6, 3, 12, 21, 30, 39, 48, 57, 66]) == 327
    assert candidate(stoneValue = [1, 3, 2, 4, 7, 6, 5, 8, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 189
    assert candidate(stoneValue = [500000, 400000, 300000, 200000, 100000, 50000, 40000, 30000, 20000, 10000]) == 1140000
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 59
    assert candidate(stoneValue = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 3700
    assert candidate(stoneValue = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]) == 92000
    assert candidate(stoneValue = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 89
    assert candidate(stoneValue = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 800
    assert candidate(stoneValue = [50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 1980
    assert candidate(stoneValue = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55]) == 355
    assert candidate(stoneValue = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 18900
    assert candidate(stoneValue = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1]) == 32
    assert candidate(stoneValue = [5, 12, 8, 4, 9, 2, 7]) == 33
    assert candidate(stoneValue = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 140
    assert candidate(stoneValue = [5, 3, 8, 7, 1, 9, 4, 6, 2, 10]) == 36
    assert candidate(stoneValue = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == 11000000
    assert candidate(stoneValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 37
    assert candidate(stoneValue = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2]) == 76
