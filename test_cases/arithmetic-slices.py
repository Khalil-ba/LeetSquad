# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 36
    assert candidate(nums = [1, 2, 4, 5, 6, 7]) == 3
    assert candidate(nums = [3, -1, -5, -9]) == 3
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(nums = [1, 3, 5, 7, 9]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [10, 7, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4]) == 3
    assert candidate(nums = [7, 7, 7, 7]) == 3
    assert candidate(nums = [10, 7, 7, 7, 7, 7, 10]) == 6
    assert candidate(nums = [3, -1, -5, -9]) == 3
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
    assert candidate(nums = [2]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5]) == 6
    assert candidate(nums = [1, 3, 5, 7, 9]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5]) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 28
    assert candidate(nums = [1, 2, 2, 3]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1]) == 6
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6]) == 6
    assert candidate(nums = [1, 2, 3, 5, 7, 9]) == 4
    assert candidate(nums = [1, 2]) == 0
    assert candidate(nums = [1, 2, 4, 5, 6, 7, 8]) == 6
    assert candidate(nums = [7, 7, 7, 7]) == 3
    assert candidate(nums = [1, 2, 3, 8, 9, 10]) == 2
    assert candidate(nums = [0, 1, 2, 3, 6, 9, 12, 15, 18, 21]) == 18
    assert candidate(nums = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 29
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 21
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 1
    assert candidate(nums = [1, 2, 3, 5, 7, 9, 11, 13, 15]) == 16
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, -1]) == 25
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 7, 9, 11, 13, 15]) == 16
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 36
    assert candidate(nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 36
    assert candidate(nums = [1, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(nums = [10, 5, 0, -5, -10, -15, -20]) == 15
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == 78
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 171
    assert candidate(nums = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 29
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 72
    assert candidate(nums = [5, 7, 9, 11, 13, 15, 17, 19, 21]) == 28
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]) == 45
    assert candidate(nums = [10, 5, 0, -5, -10, -15, -20, -25]) == 21
    assert candidate(nums = [10, 11, 12, 10, 11, 12, 14, 16, 18, 20]) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 18
    assert candidate(nums = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 91
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 171
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5]) == 28
    assert candidate(nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 406
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 28
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 406
    assert candidate(nums = [1, 2, 3, 4, 2, 4, 6, 8, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, -8, -6, -4, -2]) == 60
    assert candidate(nums = [1, 3, 5, 7, 9, 12, 15, 18, 21, 24]) == 16
    assert candidate(nums = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 36
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 5, 6]) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 72
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 10
    assert candidate(nums = [10, 20, 30, 20, 10, 20, 30, 20, 10]) == 4
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 15
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8]) == 16
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 276
    assert candidate(nums = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17]) == 22
    assert candidate(nums = [1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6]) == 9
    assert candidate(nums = [2, 4, 6, 8, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 42
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 91
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 36
    assert candidate(nums = [100, 200, 300, 200, 100, 200, 300, 400]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 0, -10]) == 21
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 55
    assert candidate(nums = [1, 2, 3, 4, 2, 4, 6, 8, 10, 12]) == 13
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 0
    assert candidate(nums = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 92
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 36
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 91
    assert candidate(nums = [1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 0, -10, -20, -30]) == 34
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45]) == 0
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 36
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 28
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 91
    assert candidate(nums = [7, 7, 7, 7, 7, 8, 9, 10, 11, 12]) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 141
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1, 0, -1, -2, -3]) == 21
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7]) == 46
    assert candidate(nums = [1, 2, 3, 4, 3, 3, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 43
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 171
    assert candidate(nums = [1, 3, 5, 6, 8, 10, 12, 14, 16, 18]) == 16
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 812
    assert candidate(nums = [3, -1, -5, -9, -13, -17, -21, -25, -29, -33]) == 36
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 406
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 45
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 78
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == 45
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 36
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 91
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 5]) == 13
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 36
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 276
    assert candidate(nums = [10, 5, 0, -5, -10, -15, -20, -25]) == 21
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 36
    assert candidate(nums = [5, 5, 5, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 4
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 105
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]) == 120
    assert candidate(nums = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17]) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 91
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 36
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 28
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 21
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 171
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 91
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 91
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 36
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40]) == 42
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 91
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]) == 66
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 171
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 5, 6, 7, 8, 9]) == 18
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 55
    assert candidate(nums = [1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9, 10]) == 12
    assert candidate(nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 78
    assert candidate(nums = [1, 3, 5, 7, 9, 12, 15, 18, 21, 24]) == 16
    assert candidate(nums = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 78
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 4
    assert candidate(nums = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1]) == 17
    assert candidate(nums = [-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]) == 45
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9]) == 55
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 171
    assert candidate(nums = [5, 7, 9, 11, 13, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10]) == 51
    assert candidate(nums = [1, 2, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 45
    assert candidate(nums = [1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9]) == 18
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1770
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 171
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -1, 0, 1, 2, 3]) == 30
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]) == 36
    assert candidate(nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]) == 36
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 36
    assert candidate(nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == 28
    assert candidate(nums = [3, 1, -1, -3, -5, -7, -9, -11]) == 21
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 36
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 36
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 36
    assert candidate(nums = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]) == 55
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12]) == 17
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 45
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == 75
    assert candidate(nums = [7, 7, 7, 8, 9, 10, 11, 12, 13, 14]) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 35
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 0
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == 12
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 153
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 903
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 36
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55]) == 1
    assert candidate(nums = [3, -3, -9, -15, -21, -27, -33, -39, -45, -51, -57, -63, -69, -75, -81]) == 91
