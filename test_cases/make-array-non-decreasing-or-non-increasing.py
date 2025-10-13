# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 2, 1, 2]) == 1
    assert candidate(nums = [1, 5, 2, 4, 3]) == 4
    assert candidate(nums = [1000, 0, 1000, 0, 1000]) == 2000
    assert candidate(nums = [3, 2, 4, 5, 0]) == 4
    assert candidate(nums = [1000, 999, 998, 997, 996]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums = [1, 3, 2, 1, 2]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [2, 2, 3, 4]) == 0
    assert candidate(nums = [1000, 500, 1000, 500, 1000]) == 1000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [1, 3, 2]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [10, 5, 7, 10]) == 5
    assert candidate(nums = [10, 5, 7, 10, 6]) == 5
    assert candidate(nums = [1, 3, 2, 1, 3, 2]) == 3
    assert candidate(nums = [1, 1000, 1, 1000, 1]) == 1998
    assert candidate(nums = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 3, 2, 1]) == 2
    assert candidate(nums = [10, 5, 15, 20, 25, 30]) == 5
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 1]) == 4
    assert candidate(nums = [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 0
    assert candidate(nums = [100, 50, 100, 50, 100, 50, 100]) == 150
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 0
    assert candidate(nums = [7, 9, 5, 3, 6, 2, 8, 4, 10, 1]) == 17
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 370
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5]) == 45
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 9
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40]) == 70
    assert candidate(nums = [2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 10
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4]) == 16
    assert candidate(nums = [200, 150, 250, 100, 300, 50, 350, 0, 400, 450, 500, 550, 600]) == 800
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 300
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 7
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 19
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 10
    assert candidate(nums = [3, 1, 2, 4, 3, 5, 6, 5, 4, 7]) == 5
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 30
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(nums = [100, 50, 150, 100, 200, 150, 250, 200, 300, 250, 350, 300, 400, 350, 450, 400, 500, 450, 550, 500]) == 500
    assert candidate(nums = [5, 1, 3, 8, 2, 9, 4, 7, 6, 0]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 100, 6, 7, 8, 9, 10]) == 94
    assert candidate(nums = [5, 3, 6, 7, 10, 4, 8, 11, 1, 9]) == 18
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 25
    assert candidate(nums = [10, 9, 10, 8, 9, 7, 8, 6, 7, 5, 6, 4, 5, 3, 4, 2, 3, 1, 2, 1]) == 9
    assert candidate(nums = [1, 3, 2, 1, 0, 2, 3, 4, 2, 1]) == 8
    assert candidate(nums = [20, 30, 25, 35, 40, 50, 45, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20]) == 455
    assert candidate(nums = [3, 1, 2, 4, 3, 5, 4, 6, 5, 7]) == 5
    assert candidate(nums = [100, 50, 75, 25, 125, 80, 60, 40, 30, 90]) == 190
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 9
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 9
    assert candidate(nums = [5, 3, 8, 6, 7, 2, 4, 9, 1, 10]) == 19
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 6
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 130
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [50, 40, 30, 20, 10, 20, 30, 40, 50, 60]) == 70
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 10, 9, 1]) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 254
    assert candidate(nums = [10, 5, 5, 5, 10, 15, 10, 5, 15, 20, 15, 10, 5, 25]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 127
    assert candidate(nums = [6, 2, 4, 10, 3, 8, 1]) == 13
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 0
    assert candidate(nums = [10, 15, 12, 14, 13, 17, 20, 16]) == 8
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 10
    assert candidate(nums = [5, 3, 6, 7, 2, 8, 1, 4]) == 14
    assert candidate(nums = [1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1]) == 7
    assert candidate(nums = [100, 200, 150, 100, 50, 250, 200, 150, 100, 50]) == 400
    assert candidate(nums = [100, 200, 300, 100, 150, 250, 200, 300, 100, 50]) == 500
    assert candidate(nums = [10, 15, 20, 25, 30, 5, 10, 15, 20, 25]) == 45
    assert candidate(nums = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 3996
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 4
    assert candidate(nums = [3, 8, 5, 12, 7, 9, 2, 15]) == 15
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 87
    assert candidate(nums = [500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]) == 1850
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 37
    assert candidate(nums = [1, 3, 5, 2, 4, 6, 3, 5, 7, 4, 6, 8]) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 14
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == 0
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 0
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 20
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 30
    assert candidate(nums = [500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500]) == 1000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 30
    assert candidate(nums = [500, 250, 750, 100, 400, 600, 300, 800, 1000, 500, 250, 750, 100, 400, 600]) == 3000
    assert candidate(nums = [500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]) == 4700
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6]) == 5
    assert candidate(nums = [500, 400, 300, 200, 100, 200, 300, 400, 500, 600, 500, 400, 300, 200, 100]) == 1300
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 15
    assert candidate(nums = [1, 10, 100, 1000, 100, 10, 1]) == 1089
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95, 110, 105, 120, 115]) == 55
    assert candidate(nums = [1, 5, 3, 6, 7, 4, 8, 2, 9, 10]) == 11
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(nums = [10, 20, 30, 25, 35, 40, 30, 45, 50, 40, 55, 60, 50, 65]) == 35
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 81
    assert candidate(nums = [1, 3, 5, 3, 1, 3, 5, 3, 1, 3]) == 8
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 7, 4, 8, 3, 9, 2, 10, 1]) == 45
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == 7
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1, 11]) == 45
    assert candidate(nums = [8, 6, 9, 5, 7, 3, 4, 6, 8, 7]) == 13
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]) == 165
    assert candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 8
    assert candidate(nums = [1, 3, 5, 4, 3, 2, 3, 5, 7, 6, 5, 4, 3, 2, 1]) == 16
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5]) == 6
    assert candidate(nums = [100, 200, 300, 200, 100, 200, 300, 200, 100]) == 400
    assert candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40]) == 20
