# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [10, 5, 7]) == 22
    assert candidate(nums = [10, 5, 1, 8, 12, 10, 5, 15]) == 37
    assert candidate(nums = [7, 10, 5, 2, 8, 7]) == 25
    assert candidate(nums = [1, 1, 1, 1]) == 3
    assert candidate(nums = [1, 1, 1]) == 3
    assert candidate(nums = [1, 1000000, 1000000]) == 2000001
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
    assert candidate(nums = [10, 5, 7, 8, 2, 12]) == 30
    assert candidate(nums = [3, 6, 2, 3]) == 8
    assert candidate(nums = [2, 1, 2]) == 5
    assert candidate(nums = [2, 3, 4, 5, 6]) == 15
    assert candidate(nums = [10, 20, 30, 40, 50]) == 120
    assert candidate(nums = [7, 10, 5, 2, 8, 4, 6]) == 25
    assert candidate(nums = [5, 5, 5, 5]) == 15
    assert candidate(nums = [1, 1, 1, 2, 2, 2]) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 27
    assert candidate(nums = [2, 3, 3, 4, 5, 6, 7]) == 18
    assert candidate(nums = [1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [7, 10, 5, 2]) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 15
    assert candidate(nums = [6, 4, 10, 3]) == 13
    assert candidate(nums = [3, 6, 2, 3, 5, 4, 1]) == 15
    assert candidate(nums = [6, 4, 2, 8, 5, 7]) == 21
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 8]) == 21
    assert candidate(nums = [6, 6, 6, 10]) == 22
    assert candidate(nums = [1, 2, 1, 10]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3]) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [3, 2, 3, 4]) == 10
    assert candidate(nums = [7, 10, 5, 2, 8, 7, 3, 5]) == 25
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 4200
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]) == 2700000
    assert candidate(nums = [3, 6, 2, 3, 5, 4, 8, 7]) == 21
    assert candidate(nums = [5, 5, 5, 1, 1, 1, 10, 10, 10, 20]) == 30
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 81
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996]) == 2999997
    assert candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996, 6, 999995, 7, 999994, 8, 999993]) == 2999997
    assert candidate(nums = [1000000, 999999, 1000000, 1000000, 999998]) == 3000000
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 30
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 500000, 600000, 700000]) == 2300000
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 30
    assert candidate(nums = [999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, 999989]) == 2999991
    assert candidate(nums = [1000000, 999999, 999998, 1, 2, 3]) == 2999997
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == 81
    assert candidate(nums = [9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 69
    assert candidate(nums = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]) == 3024
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 29
    assert candidate(nums = [10, 20, 25, 30, 40, 50, 60, 70, 80, 90]) == 240
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 20, 22, 21, 23, 25, 24, 26, 28, 27, 29, 30]) == 87
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == 3000000
    assert candidate(nums = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 84
    assert candidate(nums = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]) == 81
    assert candidate(nums = [3, 6, 2, 3, 5, 40, 41]) == 87
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 2999997
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 9
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 36
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 57
    assert candidate(nums = [7, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]) == 300
    assert candidate(nums = [1000000, 999999, 1000001, 1000002, 1000003]) == 3000006
    assert candidate(nums = [1000000, 2, 1000000, 3, 1000000, 4, 1000000, 5, 1000000]) == 3000000
    assert candidate(nums = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1]) == 9
    assert candidate(nums = [1, 200000, 200000, 200000, 200000]) == 600000
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, 999989, 999988, 999987, 999986, 999985, 999984, 999983, 999982, 999981, 999980]) == 2999994
    assert candidate(nums = [2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 57
    assert candidate(nums = [999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999]) == 2999997
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(nums = [5, 10, 25, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 51
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 57
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 300000
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == 26
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 29
    assert candidate(nums = [1, 2, 3, 6, 7, 8, 12, 14, 15, 18, 20, 21, 24, 25, 28, 30, 32, 33, 36, 39]) == 108
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 4200
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 42
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 27
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000]) == 1500000
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 9
    assert candidate(nums = [10, 5, 7, 3, 9, 8]) == 27
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1000000]) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 23
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 20
    assert candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509]) == 1524
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995]) == 2999997
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 330
    assert candidate(nums = [1000, 2000, 1500, 2500, 1800, 3000, 2200, 3500]) == 9000
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]) == 324
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 57
    assert candidate(nums = [10, 5, 7, 2, 8, 4, 6]) == 25
    assert candidate(nums = [1, 1000000, 2, 999999, 3, 999998, 4, 999997, 5, 999996, 6, 999995, 7, 999994, 8, 999993, 9, 999992]) == 2999997
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == 3600
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 357
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 6
    assert candidate(nums = [1, 2, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 9
    assert candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500]) == 1250
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 9
    assert candidate(nums = [12, 25, 10, 15, 30, 18, 20, 22, 28, 35, 40]) == 105
    assert candidate(nums = [7, 10, 5, 3, 8, 9, 2, 6, 4, 1]) == 27
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == 2999997
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 27
    assert candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]) == 294
    assert candidate(nums = [1, 1000000, 1000000, 1000000, 1000000]) == 3000000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 420
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 17
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 44
    assert candidate(nums = [1000000, 999999, 1000000, 999998, 999997]) == 2999999
