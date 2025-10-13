# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 100, 1, 1, 1, 1, 100]) == 600
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(nums = [2, 3, 7, 8, 4]) == 28
    assert candidate(nums = [4, 5, 2, 8, 9, 1, 3]) == 42
    assert candidate(nums = [1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 880
    assert candidate(nums = [3, 5, 10, 7, 8, 2, 4, 9, 1, 6]) == 77
    assert candidate(nums = [1, 5, 8]) == 16
    assert candidate(nums = [2, 3, 4, 5, 6]) == 24
    assert candidate(nums = [2, 3, 1, 4]) == 12
    assert candidate(nums = [10, 20, 30, 40, 50]) == 200
    assert candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == 90
    assert candidate(nums = [5, 6, 7, 8, 9]) == 36
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 90
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 2450
    assert candidate(nums = [10, 1, 1, 1, 10]) == 40
    assert candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9, 1, 11, 1]) == 100
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 198
    assert candidate(nums = [100000, 50000, 100000, 50000, 100000, 50000, 100000, 50000, 100000, 50000]) == 850000
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10]) == 70
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 4608
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 72
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 190
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]) == 106
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 190
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9]) == 891
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 105
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 105
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100]) == 1000
    assert candidate(nums = [1, 1, 1, 100, 1, 1, 1, 100, 1, 1, 1, 100, 1, 1, 1, 100, 1, 1, 1, 100]) == 1900
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 406
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 741
    assert candidate(nums = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 1900000
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30]) == 270
    assert candidate(nums = [3, 2, 1, 10, 5, 6, 7]) == 51
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 210
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 90
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 1000
    assert candidate(nums = [5, 3, 8, 6, 1, 9, 4, 7, 2, 10, 1, 1, 1, 1, 100000]) == 1400000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 900000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 115
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == 1810
    assert candidate(nums = [5, 3, 7, 1, 9, 2, 8, 4, 6, 10]) == 90
    assert candidate(nums = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 900000
    assert candidate(nums = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 9000
    assert candidate(nums = [3, 1, 5, 2, 4, 6, 8, 7, 9, 10, 11]) == 110
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1225
    assert candidate(nums = [5, 1, 4, 7, 10, 2, 6, 8]) == 64
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 100000]) == 1900000
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 90
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 600
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 900
    assert candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 900
    assert candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]) == 90
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1000]) == 10000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 1100
    assert candidate(nums = [1, 3, 2, 5, 4, 8, 7, 9, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 380
    assert candidate(nums = [5, 15, 25, 10, 20, 30, 5, 10, 15, 25]) == 250
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 450
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 300
    assert candidate(nums = [1, 5, 8, 9, 10, 1, 1, 1, 1, 1]) == 45
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 210
    assert candidate(nums = [5, 3, 8, 1, 7, 4, 6, 2, 9, 10]) == 90
    assert candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16]) == 144
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 900
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10]) == 90
    assert candidate(nums = [5, 2, 9, 4, 6, 1, 8, 3, 7, 10]) == 90
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 90
    assert candidate(nums = [1, 50, 10, 20, 30, 40, 50, 60, 70, 80]) == 720
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1, 0, 0, 1]) == 100
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 14000
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 100000]) == 1500000
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 72
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 70
    assert candidate(nums = [9, 2, 3, 4, 5, 6, 7, 8, 9]) == 72
    assert candidate(nums = [100, 10, 1, 1000, 100, 1, 1000, 100, 1]) == 6101
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1350
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 380
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 1380
    assert candidate(nums = [5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 190
    assert candidate(nums = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 800001
    assert candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == 90
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 100]) == 1900
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 450000
    assert candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 900
    assert candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 90
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990]) == 899946
    assert candidate(nums = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 1400
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 900000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 1900000
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 900
    assert candidate(nums = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 1900000
    assert candidate(nums = [10, 1, 1, 1, 10]) == 40
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 900
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 80
    assert candidate(nums = [1, 10, 2, 10, 3, 10, 4, 10, 5, 10, 6, 10, 7, 10, 8, 10, 9, 10]) == 170
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1000]) == 19000
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1000]) == 30000
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 70
    assert candidate(nums = [5, 3, 7, 10, 2, 8, 6, 4, 9, 1]) == 76
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115]) == 1265
    assert candidate(nums = [50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 70]) == 700
    assert candidate(nums = [5, 3, 8, 6, 2, 9, 4, 7, 1, 10]) == 90
    assert candidate(nums = [5, 25, 5, 25, 5, 25, 5, 25, 5, 25]) == 225
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000]) == 1400000
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 190
