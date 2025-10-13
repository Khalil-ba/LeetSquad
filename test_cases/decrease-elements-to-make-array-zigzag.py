# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 3, 2, 2, 3, 1]) == 4
    assert candidate(nums = [1, 1, 1]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8
    assert candidate(nums = [9, 6, 1, 6, 2]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9]) == 6
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3]) == 3
    assert candidate(nums = [10, 9, 4, 7, 3, 8, 15]) == 10
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1]) == 6
    assert candidate(nums = [1000, 999, 998, 997, 996]) == 4
    assert candidate(nums = [2, 7, 10, 9, 8, 9]) == 4
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [4, 3, 2, 1, 0]) == 4
    assert candidate(nums = [4, 3, 2, 1, 2, 3]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == 4
    assert candidate(nums = [1, 4, 3, 2, 5]) == 4
    assert candidate(nums = [1, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1000, 1, 1000, 1, 1000]) == 0
    assert candidate(nums = [1, 1000, 1, 1000, 1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5]) == 3
    assert candidate(nums = [1, 2, 2, 3, 4]) == 3
    assert candidate(nums = [1, 2]) == 0
    assert candidate(nums = [10, 4, 4, 10, 10]) == 8
    assert candidate(nums = [1, 2, 3]) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7]) == 6
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000]) == 2
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 20
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 4, 3]) == 4
    assert candidate(nums = [1, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 5
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 12
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == 0
    assert candidate(nums = [1, 4, 2, 5, 3, 6, 4, 7, 5, 8]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10
    assert candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 0
    assert candidate(nums = [9, 8, 9, 8, 9, 8, 9, 8, 9, 8]) == 0
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == 12
    assert candidate(nums = [100, 101, 102, 101, 100, 101, 102, 101, 100, 101]) == 4
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 14
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 8
    assert candidate(nums = [3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [5, 3, 8, 1, 6, 2, 9, 4]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == 6
    assert candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35]) == 0
    assert candidate(nums = [5, 1, 3, 1, 3, 1, 3]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 6
    assert candidate(nums = [1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 5
    assert candidate(nums = [999, 1000, 999, 1000, 999, 1000, 999, 1000]) == 0
    assert candidate(nums = [7, 1, 8, 2, 9, 3, 10, 4, 11, 5]) == 0
    assert candidate(nums = [4, 1, 1, 3, 2, 1, 5]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 0
    assert candidate(nums = [5, 1, 3, 1, 5, 1, 3, 1, 5]) == 0
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 6
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 0
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 4, 5, 6, 7, 8, 9]) == 10
    assert candidate(nums = [5, 1, 4, 2, 3, 1, 3, 2, 1, 4, 5, 2, 1, 3]) == 11
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 18
    assert candidate(nums = [1, 1000, 2, 1000, 3, 1000, 4, 1000, 5, 1000]) == 0
    assert candidate(nums = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 0
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1]) == 0
    assert candidate(nums = [2, 3, 1, 4, 5, 3, 6, 7, 5, 8, 9, 7]) == 10
    assert candidate(nums = [10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 4, 5, 6, 7]) == 8
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 8, 7, 9]) == 0
    assert candidate(nums = [2, 1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9, 10, 9, 10, 11]) == 10
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 5
    assert candidate(nums = [3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(nums = [1, 10, 3, 8, 5, 6, 7, 2, 9, 4, 11]) == 18
    assert candidate(nums = [100, 1, 101, 1, 102, 1, 103, 1, 104, 1, 105, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991]) == 8
    assert candidate(nums = [1, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 2
    assert candidate(nums = [1000, 999, 1000, 999, 1000, 999, 1000]) == 0
    assert candidate(nums = [10, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9, 8, 9]) == 2
    assert candidate(nums = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]) == 8
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 10
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 4, 2]) == 4
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
    assert candidate(nums = [1000, 999, 1000, 999, 1000, 999, 1000, 999]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 8
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 0
    assert candidate(nums = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]) == 0
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6]) == 8
    assert candidate(nums = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8]) == 12
    assert candidate(nums = [8, 9, 7, 6, 7, 8, 9, 10, 11]) == 7
    assert candidate(nums = [3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]) == 0
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 18
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 0
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 24
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == 66
    assert candidate(nums = [7, 10, 9, 10, 7, 10, 9, 10, 7]) == 0
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 88
    assert candidate(nums = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3, 2, 3]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 44
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [10, 1, 20, 3, 30, 5, 40, 7, 50, 9, 60, 11, 70, 13, 80, 15, 90, 17, 100, 19]) == 0
    assert candidate(nums = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == 0
    assert candidate(nums = [2, 10, 3, 8, 4, 7, 5, 6, 6, 5]) == 2
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7]) == 4
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 0
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 4, 3, 2, 5]) == 8
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 0
    assert candidate(nums = [1, 3, 2, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1]) == 3
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 99
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 0
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 8
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 0
    assert candidate(nums = [1, 3, 5, 3, 1, 3, 5, 3, 1]) == 6
    assert candidate(nums = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9]) == 0
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 10
    assert candidate(nums = [1, 3, 2, 2, 3, 1, 4, 4, 5]) == 5
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986]) == 14
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 7
    assert candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5, 994, 6, 993, 7]) == 0
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 6
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6]) == 0
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 25
