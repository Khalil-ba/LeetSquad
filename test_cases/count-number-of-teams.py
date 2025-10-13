# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(rating = [2, 1, 3]) == 0
    assert candidate(rating = [3, 1, 2, 5, 4]) == 2
    assert candidate(rating = [1, 5, 2, 4, 3]) == 3
    assert candidate(rating = [10, 6, 5, 8]) == 1
    assert candidate(rating = [5, 4, 3, 2, 1]) == 10
    assert candidate(rating = [7, 9, 1, 10, 4, 8]) == 2
    assert candidate(rating = [5, 3, 2, 1, 4]) == 4
    assert candidate(rating = [5, 3, 1, 2, 4]) == 3
    assert candidate(rating = [3, 6, 7, 5, 10, 8]) == 9
    assert candidate(rating = [2, 5, 3, 4, 1]) == 3
    assert candidate(rating = [6, 3, 8, 1, 2, 9, 7]) == 6
    assert candidate(rating = [1, 3, 2, 4, 5]) == 7
    assert candidate(rating = [6, 9, 1, 3, 5, 7, 8, 2, 4]) == 23
    assert candidate(rating = [100, 200, 300, 400, 500]) == 10
    assert candidate(rating = [3, 2, 1, 5, 4]) == 1
    assert candidate(rating = [1, 2, 3, 4]) == 4
    assert candidate(rating = [5, 1, 4, 2, 3]) == 3
    assert candidate(rating = [100, 200, 150, 300, 250, 400, 350]) == 20
    assert candidate(rating = [4, 1, 5, 3, 2, 7, 6, 8, 10, 9]) == 66
    assert candidate(rating = [1, 5, 2, 6, 3, 7, 4, 8, 9]) == 50
    assert candidate(rating = [3, 6, 1, 5, 9, 2, 8, 4, 7, 10]) == 41
    assert candidate(rating = [5, 3, 8, 1, 7, 2, 6, 4]) == 9
    assert candidate(rating = [1, 5, 3, 7, 9, 2, 4, 8, 6, 10]) == 50
    assert candidate(rating = [7, 1, 3, 5, 9, 6, 2, 8, 4]) == 24
    assert candidate(rating = [9, 5, 7, 3, 8, 1, 6, 4, 2, 10]) == 41
    assert candidate(rating = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 455
    assert candidate(rating = [100, 200, 150, 250, 300, 10, 50, 350]) == 19
    assert candidate(rating = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1140
    assert candidate(rating = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 120
    assert candidate(rating = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16]) == 600
    assert candidate(rating = [15, 12, 14, 11, 13, 10, 16, 17, 9, 8, 7, 6]) == 122
    assert candidate(rating = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 88
    assert candidate(rating = [50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 60, 70, 80, 90, 100, 110]) == 594
    assert candidate(rating = [50, 25, 75, 100, 60, 30, 80, 40, 90]) == 25
    assert candidate(rating = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 40
    assert candidate(rating = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 120
    assert candidate(rating = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 84
    assert candidate(rating = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
    assert candidate(rating = [3, 1, 2, 6, 5, 4, 9, 8, 7, 10, 12, 11, 14, 13, 15, 16, 17]) == 537
    assert candidate(rating = [23, 17, 11, 5, 29, 25, 19, 13, 31, 27, 21, 15, 33, 28, 22, 16, 35, 30, 24, 18, 37, 32, 26, 20, 39, 34, 28, 23, 41, 36, 31, 25]) == 1835
    assert candidate(rating = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 980
    assert candidate(rating = [2, 1, 3, 6, 5, 4, 8, 7, 9]) == 52
    assert candidate(rating = [3, 1, 2, 4, 6, 5]) == 9
    assert candidate(rating = [5, 7, 9, 3, 6, 2, 8, 4, 1]) == 28
    assert candidate(rating = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 120
    assert candidate(rating = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55, 5, 1, 6, 2, 7, 3, 8, 4, 9, 11]) == 320
    assert candidate(rating = [5, 2, 1, 7, 3, 8, 4, 6, 9, 10]) == 57
    assert candidate(rating = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 50
    assert candidate(rating = [1, 5, 2, 8, 3, 7, 4, 6]) == 19
    assert candidate(rating = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 430
    assert candidate(rating = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1]) == 525
    assert candidate(rating = [2, 5, 1, 6, 3, 4]) == 3
    assert candidate(rating = [3, 1, 2, 6, 5, 4, 9, 8, 7, 10]) == 63
    assert candidate(rating = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11]) == 170
    assert candidate(rating = [5, 3, 1, 7, 9, 6, 10, 2, 4, 8]) == 30
    assert candidate(rating = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19, 10, 20]) == 570
    assert candidate(rating = [15, 25, 10, 20, 5, 30, 35, 50, 45, 40]) == 57
    assert candidate(rating = [5, 1, 2, 4, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 398
    assert candidate(rating = [5, 1, 6, 2, 7, 3, 8, 4, 9, 10]) == 60
    assert candidate(rating = [50, 1, 51, 2, 52, 3, 53, 4, 54, 5]) == 40
    assert candidate(rating = [8, 1, 2, 7, 4, 3, 6, 5]) == 21
    assert candidate(rating = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 60
    assert candidate(rating = [3, 1, 5, 2, 8, 4, 6, 7, 9, 10]) == 71
    assert candidate(rating = [10, 15, 20, 25, 30, 5, 12, 18, 24, 35]) == 44
    assert candidate(rating = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15]) == 239
    assert candidate(rating = [2, 10, 4, 3, 8, 1, 6, 5]) == 15
    assert candidate(rating = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 84
    assert candidate(rating = [15, 18, 12, 19, 21, 14, 22, 20, 23, 24, 25]) == 104
    assert candidate(rating = [7, 6, 9, 10, 5, 8, 2, 1, 4, 3]) == 43
    assert candidate(rating = [25, 20, 30, 10, 40, 50, 15, 25, 35, 45]) == 33
    assert candidate(rating = [5, 2, 8, 3, 1, 9, 4, 6, 7]) == 20
    assert candidate(rating = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 455
    assert candidate(rating = [100, 101, 99, 98, 102, 103, 97, 96, 104, 105, 95, 94]) == 98
    assert candidate(rating = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 120
    assert candidate(rating = [5, 50, 15, 40, 25, 35, 10, 20, 30, 45]) == 47
    assert candidate(rating = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21, 22, 23, 24, 25]) == 1350
    assert candidate(rating = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 120
    assert candidate(rating = [5, 3, 7, 1, 9, 4, 6, 8, 2, 10, 11]) == 67
    assert candidate(rating = [20, 50, 40, 60, 10, 70, 30]) == 9
    assert candidate(rating = [20, 30, 10, 40, 50, 15, 25, 35, 45, 5]) == 36
    assert candidate(rating = [30, 20, 10, 50, 40, 60, 80, 70]) == 29
    assert candidate(rating = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 455
    assert candidate(rating = [9, 6, 7, 3, 8, 2, 5, 4, 10, 1]) == 47
    assert candidate(rating = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 120
    assert candidate(rating = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 455
    assert candidate(rating = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 84
    assert candidate(rating = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 50
    assert candidate(rating = [8, 1, 2, 3, 4, 5, 6, 7]) == 35
    assert candidate(rating = [5, 3, 7, 1, 9, 2, 8, 4, 6, 10]) == 34
    assert candidate(rating = [1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8]) == 203
    assert candidate(rating = [1, 3, 5, 2, 4, 6, 7]) == 22
    assert candidate(rating = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 444
    assert candidate(rating = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 120
    assert candidate(rating = [2, 1, 3, 6, 5, 7, 4, 8, 9, 10]) == 85
    assert candidate(rating = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 84
    assert candidate(rating = [8, 5, 12, 9, 15, 6, 13, 7, 14, 4, 11, 3, 10, 2, 1]) == 179
    assert candidate(rating = [7, 6, 5, 4, 3, 2, 1]) == 35
    assert candidate(rating = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 978
    assert candidate(rating = [10, 20, 30, 15, 25, 35, 5, 12, 18, 28, 50]) == 56
    assert candidate(rating = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 70
    assert candidate(rating = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == 881
    assert candidate(rating = [1, 2, 10, 4, 3, 8, 7, 9, 6, 5]) == 50
    assert candidate(rating = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]) == 560
    assert candidate(rating = [1, 9, 3, 6, 5, 8, 4, 7, 2]) == 32
    assert candidate(rating = [7, 8, 9, 1, 2, 3, 4, 5, 6]) == 21
    assert candidate(rating = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15]) == 355
    assert candidate(rating = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 444
    assert candidate(rating = [1, 2, 3, 5, 4, 6, 8, 7, 9, 10]) == 104
    assert candidate(rating = [50, 25, 75, 10, 40, 60, 90, 5, 30, 65, 80, 100, 15, 45, 70, 85, 95]) == 238
    assert candidate(rating = [1, 3, 5, 7, 9, 11, 13]) == 35
    assert candidate(rating = [13, 11, 9, 7, 5, 3, 1]) == 35
    assert candidate(rating = [9, 5, 3, 7, 2, 8, 1, 6, 4, 10]) == 37
    assert candidate(rating = [20, 18, 19, 15, 17, 13, 16, 12, 14, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1036
    assert candidate(rating = [100, 200, 150, 300, 50, 400, 250, 350, 10, 20]) == 35
