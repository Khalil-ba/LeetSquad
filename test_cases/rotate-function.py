# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, -1, 1, -1, 1]) == 6
    assert candidate(nums = [1, 0, 0, 0, 1]) == 7
    assert candidate(nums = [10, -10, 20, -20]) == 50
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 330
    assert candidate(nums = [1, 0, 0, 0]) == 3
    assert candidate(nums = [100]) == 0
    assert candidate(nums = [1, -1, 1, -1]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50]) == 400
    assert candidate(nums = [4, 3, 2, 6]) == 26
    assert candidate(nums = [-1, -2, -3, -4, -5]) == -25
    assert candidate(nums = [5, 5, 5, 5, 5]) == 50
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [5, 5, 5, 5]) == 30
    assert candidate(nums = [1, 2, 3, 4, 5]) == 40
    assert candidate(nums = [100, -100, 100, -100, 100]) == 600
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [-1, -2, -3, -4]) == -12
    assert candidate(nums = [1, 0, 0, 0, 0]) == 4
    assert candidate(nums = [1, 2]) == 2
    assert candidate(nums = [5, 3, 1, 2, 4]) == 37
    assert candidate(nums = [-1, 0, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 41650
    assert candidate(nums = [-10, -20, -30, -40, -50, -60]) == -430
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 266000
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 56
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == -5115
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 4295
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 9
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 21750
    assert candidate(nums = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == -4170
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 4500
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 33000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70]) == 1120
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 29
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 285
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == 700
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 5280
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == -700
    assert candidate(nums = [-10, 20, -30, 40, -50, 60]) == 180
    assert candidate(nums = [-10, 1, -20, 2, -30, 3, -40, 4]) == -206
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 15
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40]) == 210
    assert candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000]) == 35000
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 9
    assert candidate(nums = [-10, 0, 10, -20, 20, -30, 30, -40, 40, -50]) == 110
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 435
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 350
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 2]) == 17
    assert candidate(nums = [-50, -50, -50, -50, -50]) == -500
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1050
    assert candidate(nums = [5, 1, 4, 2, 8, 3, 7, 6, 9, 0]) == 263
    assert candidate(nums = [100, 0, -100, 200, 0, -200, 300, 0, -300, 400]) == 3000
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
    assert candidate(nums = [-50, -50, -50, -50, -50, -50, -50, -50, -50, -50]) == -2250
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14, 14, -15, 15]) == 120
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 21
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 1120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 330
    assert candidate(nums = [50, 50, 50, 50, 50]) == 500
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 715
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 3300
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [50, -50, 40, -40, 30, -30, 20, -20, 10, -10]) == 350
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 26600
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 190
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 5
    assert candidate(nums = [-10, 0, 10, -20, 0, 20, -30, 0, 30, -40]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 5200
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 110
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 1900
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [100, 0, -100, 50, 0, -50, 25, 0, -25, 12]) == 746
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000]) == 3000
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5]) == 35
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1140
    assert candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95]) == 505
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50]) == 550
    assert candidate(nums = [100, 0, -100, 200, 0, -200, 300, 0, -300, 400, 0, -400]) == 2800
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2660
    assert candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50]) == 3500
    assert candidate(nums = [7, 1, 3, 4, 6, 5]) == 84
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000]) == 14500
    assert candidate(nums = [100, -50, 200, -25, 300, -75]) == 2000
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 2250
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 190
