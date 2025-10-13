# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 29
    assert candidate(nums = [1, 2, 3, 8, 9]) == 1
    assert candidate(nums = [2, 4, 6, 8, 10]) == 7
    assert candidate(nums = [1, 3, 5, 7, 9]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 55
    assert candidate(nums = [1, 1, 2, 5, 7]) == 0
    assert candidate(nums = [0, 2000000000, -294967296, -294967296]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [10, 9, 4, 6, 8, 4, 3, 9, 1, 3, 5, 7]) == 10
    assert candidate(nums = [1, 2, 3, 8, 13, 18]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1]) == 99
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34]) == 6
    assert candidate(nums = [7, 7, 7, 7, 7]) == 16
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 968
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 12
    assert candidate(nums = [1, 2]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3]) == 99
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 0
    assert candidate(nums = [1, 2, 3]) == 1
    assert candidate(nums = [1, 2, 3, 8, 9, 10]) == 2
    assert candidate(nums = [3, 1, 2, 2, 4, 5]) == 1
    assert candidate(nums = [3, 1, 2, 5, 7]) == 1
    assert candidate(nums = [1, 7, 10, 15, 27, 29]) == 1
    assert candidate(nums = [1, 2, 1, 2, 1]) == 1
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 9
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 968
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 194
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 55
    assert candidate(nums = [1, 2, 3, 6, 9, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]) == 198
    assert candidate(nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 55
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 90
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(nums = [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 602
    assert candidate(nums = [10, 7, 4, 3, 2, 1, -1, -2, -3, -4]) == 20
    assert candidate(nums = [1000, 990, 980, 970, 960, 950, 940, 930, 920, 910, 900, 890, 880, 870, 860, 850, 840, 830, 820, 810, 800]) == 390
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52]) == 263
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256]) == 0
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]) == 13
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 164
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]) == 72
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45]) == 1
    assert candidate(nums = [-5, -1, 3, 7, 11, 15, 19, 23]) == 29
    assert candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55]) == 55
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 72
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1048365
    assert candidate(nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == 55
    assert candidate(nums = [10, 10, 10, 20, 20, 20, 30, 30, 30, 40, 40, 40]) == 139
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 164
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 344
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 946
    assert candidate(nums = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]) == 72
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 60
    assert candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]) == 72
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 1152921504606845145
    assert candidate(nums = [1, 3, 5, 7, 9, 12, 15, 18, 21, 24]) == 22
    assert candidate(nums = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47]) == 164
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 55
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 604
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 0
    assert candidate(nums = [10, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]) == 55
    assert candidate(nums = [1, 7, 10, 15, 27, 29, 33, 51]) == 3
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(nums = [1, 3, 5, 9, 15, 25, 39, 57, 79, 105, 135]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 164
    assert candidate(nums = [10, 12, 14, 18, 22, 26, 30, 34, 38, 42, 46]) == 56
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 55
    assert candidate(nums = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 72
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1981
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 4172
    assert candidate(nums = [1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 62
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 65294
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1048365
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 32647
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4256
    assert candidate(nums = [1, 7, 10, 15, 27, 29, 33, 37, 41, 45, 49]) == 13
    assert candidate(nums = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32]) == 55
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 160
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 164
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 32
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 90
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57]) == 164
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 1936
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40]) == 137
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 8
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 604
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 772
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == 344
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1294
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]) == 263
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 344
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58]) == 344
    assert candidate(nums = [1, 2, 4, 6, 8, 10, 14, 16, 18, 20, 24, 26, 28, 30, 34, 36, 38, 40]) == 72
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 344
    assert candidate(nums = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 114
    assert candidate(nums = [1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 56
    assert candidate(nums = [-2, -1, 1, 4, 8, 13, 19, 26, 34, 43, 53, 64]) == 4
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 946
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 391
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 41
    assert candidate(nums = [2, 4, 6, 8, 12, 14, 16, 20, 22, 24, 28]) == 32
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 72
    assert candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 28
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 164
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 72
    assert candidate(nums = [1, 2, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54]) == 264
    assert candidate(nums = [10, 7, 4, 1, -2, -5, -8, -11, -14]) == 41
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 41
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 364
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 113
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]) == 3
    assert candidate(nums = [1, 3, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]) == 355
    assert candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73]) == 113
    assert candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61]) == 72
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 57
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 48
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40]) == 164
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 968
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 90
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == 25208
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 344
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]) == 72
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800]) == 29
    assert candidate(nums = [1, 7, 13, 19, 25, 31, 37, 43, 49]) == 41
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45]) == 90
    assert candidate(nums = [10, 7, 4, 3, 2, 1, -1, -4, -7, -10]) == 16
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 55
    assert candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100]) == 90
    assert candidate(nums = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 17
    assert candidate(nums = [1, 3, 5, 3, 1, -1, -3, -5, -3, -1, 1, 3, 5]) == 53
    assert candidate(nums = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 72
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39]) == 113
    assert candidate(nums = [1, 2, 3, 6, 9, 12, 15, 18, 21]) == 21
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 1584
    assert candidate(nums = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]) == 323
    assert candidate(nums = [1, 2, 3, 2, 1, 0, -1, -2, -1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]) == 1370
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 55
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 55
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
    assert candidate(nums = [3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 160
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 72
    assert candidate(nums = [3, 6, 9, 15, 18, 21, 27, 30, 33, 39, 42, 45]) == 40
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 968
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7]) == 165
    assert candidate(nums = [5, 10, 15, 25, 35, 45, 55, 65, 75, 85]) == 42
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 32647
    assert candidate(nums = [1, 7, 10, 15, 27, 29, 33, 18]) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 5029
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 90
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]) == 164
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 55
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 164
    assert candidate(nums = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79]) == 4
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 32647
