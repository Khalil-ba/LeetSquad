# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 2, 3, 4, 5]) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15]) == 22
    assert candidate(nums = [1, 1, 1, 1]) == 4
    assert candidate(nums = [4, 2, 3, 4]) == 4
    assert candidate(nums = [0, 1, 0, 1]) == 0
    assert candidate(nums = [10, 21, 32, 43, 54, 65]) == 7
    assert candidate(nums = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 52
    assert candidate(nums = [10, 20, 30, 40, 50]) == 3
    assert candidate(nums = [5, 5, 5, 5]) == 4
    assert candidate(nums = [2, 2, 3, 4]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5]) == 3
    assert candidate(nums = [0, 1, 1, 1]) == 1
    assert candidate(nums = [10, 21, 22, 100, 101, 200, 300]) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 120
    assert candidate(nums = [0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 7
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25]) == 3
    assert candidate(nums = [1, 2, 2, 3, 4]) == 4
    assert candidate(nums = [1000, 1000, 1000, 1000]) == 4
    assert candidate(nums = [1, 2, 2, 3, 4, 6]) == 5
    assert candidate(nums = [1, 2, 3]) == 0
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 1, 1, 2]) == 10
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 1028
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11]) == 333
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 9500
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 252
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10]) == 150
    assert candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515]) == 560
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
    assert candidate(nums = [3, 4, 5, 6, 7, 8]) == 17
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]) == 372
    assert candidate(nums = [5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums = [0, 0, 0, 0, 1, 2, 3, 4, 5]) == 3
    assert candidate(nums = [10, 21, 31, 41, 51, 61, 71, 81, 91, 101]) == 62
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 1370
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 230
    assert candidate(nums = [1, 2, 2, 3, 4, 5]) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1140
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 525
    assert candidate(nums = [990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]) == 165
    assert candidate(nums = [5, 10, 25, 50, 100]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 1395
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8]) == 48
    assert candidate(nums = [3, 3, 3, 3, 3]) == 10
    assert candidate(nums = [1, 3, 3, 4, 5, 6, 7, 8, 9]) == 40
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 203
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 7
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) == 156
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 512
    assert candidate(nums = [1, 1000, 500, 300, 200, 100, 50, 25, 10, 5, 1]) == 0
    assert candidate(nums = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 24
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 486
    assert candidate(nums = [250, 500, 750, 1000, 250, 500, 750, 1000, 250, 500]) == 45
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 530
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 7
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 367
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40]) == 22
    assert candidate(nums = [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]) == 602
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 5]) == 31
    assert candidate(nums = [10, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]) == 94
    assert candidate(nums = [0, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500]) == 50
    assert candidate(nums = [33, 33, 33, 66, 66, 66, 99, 99, 99, 132, 132, 132]) == 103
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 34
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) == 165
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77]) == 525
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 444
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]) == 372
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 120
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]) == 372
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 444
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2]) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 525
    assert candidate(nums = [5, 25, 45, 65, 85, 105, 125, 145, 165, 185, 205]) == 70
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 24
    assert candidate(nums = [998, 999, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 220
    assert candidate(nums = [333, 333, 333, 333, 333, 333, 333, 333, 333, 333, 333, 333, 333]) == 286
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 1945
    assert candidate(nums = [2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 325
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 1078
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 50
    assert candidate(nums = [8, 15, 17, 10, 12, 6, 9, 11, 7, 4, 3, 2, 1]) == 108
    assert candidate(nums = [10, 20, 20, 20, 30, 30, 40, 50, 60]) == 35
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == 56
    assert candidate(nums = [10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 283
    assert candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]) == 1140
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 203
    assert candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 508
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 1140
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128]) == 0
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == 24
    assert candidate(nums = [3, 3, 3, 3, 3, 3]) == 20
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]) == 898
    assert candidate(nums = [2, 3, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 525
    assert candidate(nums = [1000, 0, 500, 500, 0, 500, 500, 0, 500, 500]) == 20
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]) == 420
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1140
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 211
    assert candidate(nums = [5, 6, 7, 8, 9]) == 10
    assert candidate(nums = [1, 10, 100, 1000, 2, 20, 200, 2000, 3, 30, 300, 3000, 4, 40, 400, 4000]) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 50
    assert candidate(nums = [300, 200, 100, 400, 500, 600, 700, 800, 900, 1000]) == 50
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 4, 5]) == 10
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 1591
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 50
    assert candidate(nums = [999, 1000, 1000, 1000, 1000, 999, 999, 999, 999, 998, 998, 998, 998]) == 286
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 455
    assert candidate(nums = [1, 10, 100, 1000, 10, 100, 1000, 10, 100, 1000]) == 39
