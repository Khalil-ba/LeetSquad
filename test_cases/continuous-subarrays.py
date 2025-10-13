# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 4, 2, 4]) == 8
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 4]) == 27
    assert candidate(nums = [9, 7, 5, 3, 1]) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 24
    assert candidate(nums = [1, 3, 5, 7, 9]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5]) == 15
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 210
    assert candidate(nums = [1000000000, 1000000000, 1000000000]) == 6
    assert candidate(nums = [2, 2, 2, 1, 1, 3, 3, 3]) == 36
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 19
    assert candidate(nums = [10, 9, 8, 8, 7, 6, 5, 5, 4, 3, 2, 1]) == 39
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
    assert candidate(nums = [1, 2, 2, 2, 3, 3]) == 21
    assert candidate(nums = [1, 2, 2, 2, 1]) == 15
    assert candidate(nums = [1, 1, 1, 1, 1]) == 15
    assert candidate(nums = [1, 3, 1, 3, 1, 3]) == 21
    assert candidate(nums = [1, 2, 2, 2, 3]) == 15
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 27
    assert candidate(nums = [1, 3, 5, 4, 6, 7, 8, 2]) == 17
    assert candidate(nums = [1, 2, 3]) == 6
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 55
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == 21
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 57
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 42
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 31
    assert candidate(nums = [100, 101, 102, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 60
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 210
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]) == 63
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 57
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 69
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 97
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 210
    assert candidate(nums = [1, 5, 2, 3, 7, 4, 8, 6, 10, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 42
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]) == 90
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 59
    assert candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 508, 507, 506, 505, 504, 503, 502, 501, 500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490]) == 87
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 57
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 2, 2, 1, 1, 2, 2]) == 210
    assert candidate(nums = [4, 4, 5, 4, 4, 6, 5, 4, 4, 3]) == 49
    assert candidate(nums = [1, 5, 4, 2, 4, 1, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 37
    assert candidate(nums = [1, 4, 2, 3, 2, 3, 4, 1, 2, 3, 2, 3, 4, 1]) == 43
    assert candidate(nums = [10, 10, 9, 11, 12, 8, 7, 6, 10, 10, 9, 11, 12, 8, 7, 6]) == 36
    assert candidate(nums = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0, -1, -1, -2, -2, -3, -3, -4, -4, -5, -5]) == 153
    assert candidate(nums = [2, 4, 6, 8, 10, 8, 6, 4, 2, 0, 2, 4, 6, 8, 10, 8, 6, 4, 2, 0]) == 42
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 72
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 210
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 10
    assert candidate(nums = [3, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 162
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 33
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 210
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 210
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 20
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 98
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 325
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 210
    assert candidate(nums = [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == 1081
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 69
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 57
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 45
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 27
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 72
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 72
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 60
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 39
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 465
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 54
    assert candidate(nums = [1000000000, 999999999, 1000000000, 999999998, 1000000000, 1000000001, 999999997, 1000000000, 1000000002, 999999996]) == 22
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4]) == 60
    assert candidate(nums = [1000000000, 999999998, 1000000001, 999999997, 1000000002, 999999996, 1000000003, 999999995, 1000000004, 999999994]) == 11
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5]) == 69
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 38
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 2, 1, 1, 1, 2, 3, 3, 2, 1]) == 120
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3]) == 117
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(nums = [1000000000, 999999998, 1000000002, 1000000001, 999999999, 1000000003, 999999997, 1000000004, 999999996, 1000000005]) == 13
    assert candidate(nums = [5, 1, 5, 3, 3, 5, 2, 4, 4, 2, 3, 5, 6, 8, 7, 9, 10, 8, 6, 4, 2, 1]) == 52
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 19
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 55
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 820
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 78
    assert candidate(nums = [5, 7, 8, 5, 6, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 59
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 990
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 55
    assert candidate(nums = [10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11]) == 210
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 39
    assert candidate(nums = [5, 4, 4, 4, 4, 5, 6, 7, 8, 7, 6, 5, 4, 4, 4, 4, 5]) == 71
    assert candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 210
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2]) == 54
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == 210
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 496
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10]) == 267
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 87
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 55
    assert candidate(nums = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 472
    assert candidate(nums = [100, 99, 100, 98, 99, 100, 97, 98, 99, 100]) == 30
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 63
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 69
    assert candidate(nums = [5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 141
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == 55
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 57
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 55
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 39
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 54
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 20
    assert candidate(nums = [1, 3, 5, 3, 1, 3, 5, 3, 1, 3]) == 23
    assert candidate(nums = [5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3, 5, 2, 5, 3]) == 80
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 81
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 60
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 147
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 65
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 210
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 55
    assert candidate(nums = [20, 18, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10, 12, 14, 16]) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 48
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 210
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 7, 4, 8, 3, 9, 2, 10, 1]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 72
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 84
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 210
    assert candidate(nums = [10, 11, 12, 10, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 58
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 2, 2, 2, 1]) == 66
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 55
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 30
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 27
    assert candidate(nums = [4, 2, 2, 2, 3, 4, 5]) == 24
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 57
    assert candidate(nums = [1, 4, 2, 3, 2, 5, 4, 3]) == 17
    assert candidate(nums = [1, 2, 3, 2, 1]) == 15
    assert candidate(nums = [1, 3, 2, 3, 1]) == 15
    assert candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002]) == 8
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 42
    assert candidate(nums = [3, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 55
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 1, 3, 2, 1]) == 55
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 48
    assert candidate(nums = [1, 2, 2, 1]) == 10
    assert candidate(nums = [3, 3, 2, 2, 1, 1, 4, 4, 5, 5]) == 31
    assert candidate(nums = [1000000000, 1000000000, 1000000000]) == 6
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 45
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 55
    assert candidate(nums = [2, 2, 2, 1, 3]) == 15
    assert candidate(nums = [100, 101, 102, 99, 98, 97, 96]) == 15
    assert candidate(nums = [10, 9, 8, 7, 6]) == 12
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 30
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 42
    assert candidate(nums = [1, 2, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10, 10, 10]) == 102
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 10
    assert candidate(nums = [1, 2, 2, 3, 2, 1, 2, 2, 3, 2]) == 55
    assert candidate(nums = [10, 20, 30, 40, 50]) == 5
    assert candidate(nums = [1, 2, 2, 3, 4]) == 14
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4]) == 60
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2]) == 78
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2850
    assert candidate(nums = [5, 4, 3, 4, 5]) == 15
    assert candidate(nums = [1, 1000000000]) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
    assert candidate(nums = [1, 3, 5, 7, 9]) == 9
    assert candidate(nums = [1, 10, 100, 1000, 10000]) == 5
    assert candidate(nums = [5, 2, 2, 4, 5, 3]) == 12
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 55
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == 37
    assert candidate(nums = [1, 1, 1, 1]) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 57
    assert candidate(nums = [1, 2, 3, 4, 5]) == 12
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 60
    assert candidate(nums = [1000000000, 999999999, 1000000001, 1000000002]) == 8
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000]) == 10
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 45
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]) == 120
    assert candidate(nums = [1, 3, 5, 3, 1, 3, 5, 3, 1]) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 3321
    assert candidate(nums = [10, 10, 10, 10, 10]) == 15
    assert candidate(nums = [10, 10, 10, 10, 10, 10]) == 21
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 4, 3, 2, 1]) == 36
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 55
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4]) == 45
    assert candidate(nums = [2, 2, 2, 1, 3, 1, 3, 2, 2, 1]) == 55
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 19
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 60
    assert candidate(nums = [1, 1, 1, 1]) == 10
    assert candidate(nums = [1, 2, 2, 1]) == 10
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 55
    assert candidate(nums = [1, 2, 2, 2, 2, 2]) == 21
    assert candidate(nums = [1, 3, 2, 2, 1, 3, 2, 2, 1]) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 33
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 55
    assert candidate(nums = [3, 1]) == 3
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1]) == 45
    assert candidate(nums = [1, 3]) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3]) == 21
    assert candidate(nums = [5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]) == 117
    assert candidate(nums = [1, 2, 2, 2, 3, 4, 5]) == 23
    assert candidate(nums = [5, 7, 7, 8, 8, 10]) == 16
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 29
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 28
    assert candidate(nums = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9]) == 24
    assert candidate(nums = [1, 2]) == 3
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000]) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 15
    assert candidate(nums = [1, 2, 3]) == 6
    assert candidate(nums = [1, 3, 2, 3, 1, 4, 2, 3, 1]) == 24
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 27
    assert candidate(nums = [10, 10, 10, 10]) == 10
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3]) == 120
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 33
    assert candidate(nums = [1, 4, 2, 3, 5, 6, 7, 8, 9]) == 20
    assert candidate(nums = [1000000000]) == 1
    assert candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10]) == 21
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 51
    assert candidate(nums = [1, 2, 2, 1, 1, 2, 2, 1]) == 36
    assert candidate(nums = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 18
    assert candidate(nums = [1, 4, 7, 10, 13]) == 5
    assert candidate(nums = [10, 9, 10, 11, 10, 9, 10, 11, 10, 9]) == 55
    assert candidate(nums = [5, 4, 2, 4]) == 8
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 55
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1]) == 21
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 57
    assert candidate(nums = [3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6]) == 57
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 45
