# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-1, -2, -3, -4]) == 10
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 165
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165
    assert candidate(nums = [1, -1, 1, -1, 1, -1]) == 30
    assert candidate(nums = [4, -2, -3, 4, 1]) == 59
    assert candidate(nums = [3, 2, 2, 2, 1]) == 8
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 20000000000
    assert candidate(nums = [10, 20, 30, 40, 50]) == 200
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 20
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 20
    assert candidate(nums = [100, 100, 100, 100]) == 0
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000]) == 12000000000
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [10, -10, 20, -20, 30, -30]) == 700
    assert candidate(nums = [10, 20, 30, 40, 50]) == 200
    assert candidate(nums = [1, 2, 2, 2, 3]) == 8
    assert candidate(nums = [5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [-10, -20, -30, -40, -50]) == 200
    assert candidate(nums = [1, 3, 3]) == 4
    assert candidate(nums = [1, 2, 3]) == 4
    assert candidate(nums = [-10, 100, -20, 200, -30, 300]) == 3580
    assert candidate(nums = [5]) == 0
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1]) == 66
    assert candidate(nums = [-1, 4, -2, 3, -3]) == 60
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 45
    assert candidate(nums = [1, 0, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 384
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 16500
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 64
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 2400
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 190
    assert candidate(nums = [10, 20, 30, 25, 15, 10, 5, 2, 1, 0]) == 743
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 105
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 560
    assert candidate(nums = [5, 3, 8, 1, 4]) == 57
    assert candidate(nums = [10, 20, 30, 25, 15, 5]) == 240
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 168
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000]) == 12000000000
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 330
    assert candidate(nums = [5, 1, 4, 2, 8, 3]) == 77
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == 60
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 1540
    assert candidate(nums = [100, 200, 300, 400, 500, -500, -400, -300, -200, -100]) == 29000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 560
    assert candidate(nums = [100, 200, 300, 400, 500]) == 2000
    assert candidate(nums = [10, 20, 30, 40, 50, -50, -40, -30, -20, -10]) == 2900
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == 20000000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 635
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500]) == 36000
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1540
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 40
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [100, 10, 1, 0, 1, 10, 100]) == 1149
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1]) == 66
    assert candidate(nums = [9, -8, 7, -6, 5, -4, 3, -2, 1]) == 444
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 330
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 80
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1]) == 28
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 480
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 1655
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 240
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40]) == 1680
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10]) == 210
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 45
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000]) == 21000000000
    assert candidate(nums = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 5600
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1650
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 330
    assert candidate(nums = [5, 8, 6, 7, 9, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1736
    assert candidate(nums = [9, 7, 5, 3, 1]) == 40
    assert candidate(nums = [5, 8, 3, 7, 9, 1]) == 87
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]) == 22000
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == 180
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 20
    assert candidate(nums = [10, -5, 3, 7, -2, 8]) == 172
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1]) == 42
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 165
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 330
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 90
    assert candidate(nums = [-1, -5, -9, -3, -6]) == 59
    assert candidate(nums = [100, 200, 300, 400, 500, 600]) == 3500
    assert candidate(nums = [1, 5, 3, 7, 9, 2, 6, 8, 4, 10]) == 283
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 560
    assert candidate(nums = [5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5]) == 240
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 1650
    assert candidate(nums = [5, 2, 9, 1, 5, 6]) == 99
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 328
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 651
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1540
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 285
    assert candidate(nums = [100, -100, 200, -200, 300]) == 4000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 8550
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 235
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 6150
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1000000000, 1000000000, -1000000000, -1000000000]) == 8000000000
    assert candidate(nums = [-1, 2, -3, 4, -5]) == 70
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000]) == 15250000000
    assert candidate(nums = [100, -200, 300, -400, 500]) == 7000
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 220
    assert candidate(nums = [5, 3, 1, 2, 4]) == 27
    assert candidate(nums = [5, 2, 3, 1, 4, 6, 8, 7, 9, 0]) == 244
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 2660
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 45
    assert candidate(nums = [5, 3, 8, 1, 4]) == 57
    assert candidate(nums = [5, 2, 4, 6, 1, 3]) == 60
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1]) == 56
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 330
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1650
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 90
    assert candidate(nums = [5, 3, 8, 2, 7]) == 53
    assert candidate(nums = [5, 1, 4, 3, 2]) == 29
    assert candidate(nums = [1, 2, 3, -1, -2, -3, 4, 5, 6]) == 201
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 2135
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 1650
    assert candidate(nums = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3]) == 392
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 165000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 5600
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == 560
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1540
