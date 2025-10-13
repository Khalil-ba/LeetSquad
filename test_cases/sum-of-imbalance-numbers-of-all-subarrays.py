# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [10, 1, 2, 3, 4]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2, 3, 1, 4]) == 3
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [1, 3, 3, 3, 5]) == 8
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 36
    assert candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]) == 105
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6, 10]) == 73
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11, 12, 13, 14, 15]) == 166
    assert candidate(nums = [3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 5]) == 64
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 46
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 84
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6, 10, 15, 11, 14, 12, 13]) == 204
    assert candidate(nums = [500, 501, 499, 502, 498, 503, 497, 504, 496, 505, 495, 506, 494, 507, 493, 508, 492, 509, 491, 510]) == 171
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9, 10]) == 69
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 262
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 262
    assert candidate(nums = [3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 6
    assert candidate(nums = [5, 3, 2, 4, 1, 6, 7, 8, 9, 10, 11, 12]) == 47
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [5, 1, 3, 2, 4, 6, 7, 8, 9, 10]) == 31
    assert candidate(nums = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 15, 11, 14, 12, 13]) == 118
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 0
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15]) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 30
    assert candidate(nums = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19]) == 171
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 8
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 54
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 560
    assert candidate(nums = [50, 1, 51, 2, 52, 3, 53, 4, 54, 5, 55, 6, 56, 7, 57, 8, 58, 9, 59, 10, 60, 11, 61, 12, 62, 13, 63, 14, 64, 15]) == 435
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15]) == 68
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 0
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981]) == 0
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1330
    assert candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10]) == 190
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 80
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 6
    assert candidate(nums = [100, 1, 2, 101, 3, 102, 4, 103, 5, 104, 6, 105, 7, 106, 8, 107, 9, 108, 10, 109]) == 189
    assert candidate(nums = [100, 1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93]) == 105
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24]) == 265
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [7, 3, 5, 9, 1, 4, 6, 8, 2, 10]) == 91
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 0
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10, 15, 14, 13, 18, 17, 16, 21, 20, 19, 24, 23, 22, 27, 26, 25, 29, 28]) == 461
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92]) == 153
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 72
    assert candidate(nums = [2, 1, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 85
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 9
    assert candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 560
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 154
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 3, 2, 6, 5, 4, 10, 9, 8, 15, 14, 13, 12, 11]) == 102
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 846
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
    assert candidate(nums = [5, 1, 3, 2, 4, 6, 7, 8, 10, 9]) == 39
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91, 11, 90, 12, 89, 13, 88]) == 325
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 36
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 18
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert candidate(nums = [5, 1, 4, 2, 8, 6, 3, 7, 9]) == 49
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 7
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 134
    assert candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 27, 26, 29, 28]) == 391
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 50
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9]) == 560
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 560
    assert candidate(nums = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 3, 3, 3, 3, 3]) == 250
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [1, 3, 2]) == 1
    assert candidate(nums = [1, 3, 3, 3, 5]) == 8
    assert candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 0
    assert candidate(nums = [1, 5, 3, 4, 2]) == 6
    assert candidate(nums = [1, 2, 3, 2, 1]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50]) == 20
    assert candidate(nums = [1, 2, 3, 5, 6, 8, 9, 10]) == 30
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5]) == 0
    assert candidate(nums = [1000, 999, 998, 997, 996]) == 0
    assert candidate(nums = [3, 1, 2]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [3, 2, 1]) == 0
    assert candidate(nums = [3, 1, 2, 4, 5]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [10, 1, 2, 9, 3, 8, 4, 7, 5, 6]) == 35
    assert candidate(nums = [7, 9, 5, 8, 2, 6, 3, 4, 1]) == 46
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4]) == 0
    assert candidate(nums = [1, 2, 3, 4]) == 0
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6]) == 0
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 14
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4]) == 0
    assert candidate(nums = [2]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50]) == 20
    assert candidate(nums = [7, 9, 7, 8, 7]) == 3
    assert candidate(nums = [1, 2, 2, 3, 4]) == 0
    assert candidate(nums = [10, 1, 2, 9, 3, 8, 4, 7, 5, 6]) == 35
    assert candidate(nums = [5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [2, 1]) == 0
    assert candidate(nums = [7]) == 0
    assert candidate(nums = [3, 2, 1, 2, 3]) == 0
    assert candidate(nums = [2, 3, 1, 4]) == 3
    assert candidate(nums = [1, 1000]) == 1
    assert candidate(nums = [3, 1, 2, 4, 3]) == 3
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5]) == 0
    assert candidate(nums = [2, 1]) == 0
    assert candidate(nums = [1, 2, 3, 2, 1]) == 0
    assert candidate(nums = [3, 3, 3]) == 0
    assert candidate(nums = [999, 1000]) == 0
    assert candidate(nums = [7, 9, 5, 8, 6]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [3, 2, 1, 4, 5]) == 4
    assert candidate(nums = [7, 9, 5, 8, 6, 4]) == 15
    assert candidate(nums = [1, 2, 3]) == 0
    assert candidate(nums = [4, 3, 2, 1]) == 0
    assert candidate(nums = [7, 9, 9, 7, 10, 8]) == 11
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0
    assert candidate(nums = [1, 2]) == 0
    assert candidate(nums = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1, 2, 2, 3, 4, 5]) == 0
    assert candidate(nums = [1, 4, 2, 3]) == 3
    assert candidate(nums = [1, 2, 3]) == 0
    assert candidate(nums = [2, 1, 3]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [3, 5, 7, 9, 11]) == 20
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5]) == 0
    assert candidate(nums = [1, 2, 2, 1, 2]) == 0
    assert candidate(nums = [6, 5, 4, 3, 2, 1, 1, 2, 3, 4]) == 0
    assert candidate(nums = [1, 5, 2, 4, 3]) == 6
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]) == 17
    assert candidate(nums = [1, 2]) == 0
    assert candidate(nums = [1, 2, 3, 5, 6, 8, 9]) == 22
    assert candidate(nums = [3, 3, 2, 2, 1, 1]) == 0
    assert candidate(nums = [3, 3, 2, 2, 1, 1]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 0
