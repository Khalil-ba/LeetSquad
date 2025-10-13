# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 3, 2, 2, 1]) == 85
    assert candidate(nums = [10, 20, 10, 20, 10]) == 45
    assert candidate(nums = [1, 2, 2, 1]) == 25
    assert candidate(nums = [1, 3, 2, 3, 1]) == 70
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [100, 100, 99, 99, 98]) == 49
    assert candidate(nums = [1, 2, 3, 4]) == 50
    assert candidate(nums = [10, 20, 30, 40, 50]) == 105
    assert candidate(nums = [5, 6, 7, 8, 9]) == 105
    assert candidate(nums = [7, 7, 7, 7, 7, 7]) == 21
    assert candidate(nums = [1, 2, 1]) == 15
    assert candidate(nums = [5, 5, 5, 5]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5]) == 105
    assert candidate(nums = [10, 10, 10]) == 6
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5]) == 184
    assert candidate(nums = [4, 4, 4, 4]) == 10
    assert candidate(nums = [4, 5, 6, 7]) == 50
    assert candidate(nums = [1, 2]) == 6
    assert candidate(nums = [2, 3, 2, 3]) == 28
    assert candidate(nums = [1, 2, 3]) == 20
    assert candidate(nums = [1, 1]) == 3
    assert candidate(nums = [5]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 1730
    assert candidate(nums = [3, 4, 3, 2, 3, 1]) == 120
    assert candidate(nums = [1, 2, 2, 1, 3, 3, 3, 4, 4, 4, 4]) == 410
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == 171
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 755
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2]) == 293
    assert candidate(nums = [10, 20, 30, 20, 10, 30, 20, 10]) == 220
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1210
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 1716
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 1811
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 825
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 551
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 778
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 210
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 551
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 78
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1]) == 220
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 1210
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 263
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 778
    assert candidate(nums = [1, 2, 3, 2, 1]) == 70
    assert candidate(nums = [3, 1, 2, 3, 4, 5, 3, 2]) == 370
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 50, 10]) == 367
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 278
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 4635
    assert candidate(nums = [1, 3, 3, 1, 2, 2, 3, 1]) == 194
    assert candidate(nums = [50, 50, 51, 51, 52, 52, 53, 53, 54, 54]) == 415
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 451
    assert candidate(nums = [5, 6, 5, 7, 8, 7, 6, 5, 9, 10, 9, 8, 7, 6]) == 1899
    assert candidate(nums = [1, 1, 2, 2, 3, 3]) == 77
    assert candidate(nums = [10, 20, 30, 20, 10, 30]) == 111
    assert candidate(nums = [10, 20, 30, 20, 10, 30, 20, 10, 30]) == 288
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 415
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4830
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 120
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4830
    assert candidate(nums = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 415
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 415
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 1210
    assert candidate(nums = [3, 1, 2, 3, 4, 2, 5]) == 240
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 55
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 778
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1210
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10560
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 438
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 5440
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1210
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 1645
    assert candidate(nums = [10, 20, 30, 40, 50]) == 105
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == 861
    assert candidate(nums = [10, 20, 10, 30, 20, 30, 40, 50]) == 298
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 930
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 1645
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 553
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 930
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5415
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 438
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 1285
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 3]) == 367
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10560
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 1794
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 825
    assert candidate(nums = [9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 3910
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10560
    assert candidate(nums = [7, 8, 9, 7, 8, 9, 7, 8, 9, 7, 8, 9]) == 551
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5415
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 962
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8670850
    assert candidate(nums = [1, 1, 2, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 751
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 6455
    assert candidate(nums = [1, 3, 2, 3, 4, 5, 4, 3, 2, 1]) == 611
    assert candidate(nums = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 415
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1210
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 55
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3]) == 419
    assert candidate(nums = [10, 20, 30, 20, 10, 30]) == 111
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 4635
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 1285
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 2366
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 350
