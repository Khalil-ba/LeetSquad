# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 100, 8, 6, 90, 101]) == 1
    assert candidate(nums = [9, 7, 5, 3, 1]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 3, 4, 2, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 16
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 0
    assert candidate(nums = [2, 4, 6, 4]) == 1
    assert candidate(nums = [1, 100, 101, 102, 99]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 1, 4, 3, 6, 7]) == 2
    assert candidate(nums = [5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 16
    assert candidate(nums = [100000, 99999, 100001, 99998, 100002]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 14
    assert candidate(nums = [3, 2, 1]) == 0
    assert candidate(nums = [1, 5, 2, 5, 3, 5, 4, 5]) == 0
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0
    assert candidate(nums = [1, 3, 2, 3, 5, 2, 6, 2]) == 1
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 0
    assert candidate(nums = [1, 2, 3]) == 2
    assert candidate(nums = [1, 3, 2, 5, 4, 6]) == 0
    assert candidate(nums = [1, 6, 4, 3, 5, 7, 8]) == 3
    assert candidate(nums = [1, 5, 2, 4, 3, 6]) == 0
    assert candidate(nums = [1, 5, 3, 7, 9, 11, 13, 2, 14]) == 3
    assert candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35, 45, 40, 50, 45]) == 0
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9, 8, 9, 10]) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 94, 93, 92, 91]) == 16
    assert candidate(nums = [5, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15]) == 10
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 0
    assert candidate(nums = [10, 20, 30, 25, 24, 35, 40, 39, 45, 50]) == 6
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3]) == 2
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [3, 1, 4, 2, 5, 8, 7, 10, 9, 12, 11]) == 2
    assert candidate(nums = [1, 5, 3, 4, 2, 8, 6, 7, 9, 11, 10]) == 3
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 24
    assert candidate(nums = [5, 3, 4, 2, 6, 1, 7, 9, 8, 10]) == 2
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8]) == 0
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 2, 45]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == 4
    assert candidate(nums = [10, 20, 11, 30, 12, 40, 13, 50, 14, 60, 15]) == 0
    assert candidate(nums = [1, 2, 3, 100, 2, 3, 4, 5, 6, 7]) == 6
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == 0
    assert candidate(nums = [1, 10, 3, 5, 8, 12, 7, 6, 9, 11, 15, 14, 13, 16, 18, 17, 20, 19, 21, 22]) == 8
    assert candidate(nums = [90, 100, 110, 120, 115, 130, 140, 150, 145, 160, 170, 180, 175, 190, 200]) == 14
    assert candidate(nums = [1, 3, 5, 4, 6, 7, 2, 8, 9, 10]) == 6
    assert candidate(nums = [1, 2, 3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 22
    assert candidate(nums = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 46
    assert candidate(nums = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 8
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 0
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11]) == 2
    assert candidate(nums = [1, 20, 3, 40, 5, 60, 7, 80, 9, 100]) == 0
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [1, 2, 3, 100, 4, 5, 6, 7, 8, 9]) == 8
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 0
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]) == 16
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 46
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5]) == 8
    assert candidate(nums = [1, 2, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == 3
    assert candidate(nums = [5, 1, 4, 3, 6, 8, 2, 9, 7, 10]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24]) == 0
    assert candidate(nums = [1, 20, 3, 15, 4, 10, 5, 25, 6]) == 0
    assert candidate(nums = [1, 3, 5, 2, 4, 6, 8, 7, 9, 11]) == 6
    assert candidate(nums = [5, 1, 4, 3, 6, 2, 8, 7, 10, 9]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 28
    assert candidate(nums = [5, 1, 3, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 23
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [10, 20, 30, 25, 40, 35, 50, 45, 60, 55]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 56
    assert candidate(nums = [10, 20, 30, 25, 40, 35, 50, 45, 60]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 25
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == 4
    assert candidate(nums = [10, 20, 30, 25, 35, 40, 45, 50, 39, 41]) == 6
    assert candidate(nums = [1, 100, 50, 200, 150, 250, 200, 300, 250, 350, 300, 400, 350, 450, 400, 500, 450, 550, 500, 600]) == 0
    assert candidate(nums = [10, 20, 30, 15, 25, 35, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 14
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 0
    assert candidate(nums = [30, 20, 10, 25, 15, 5, 35, 25, 15, 40, 30, 20, 50, 40, 30]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 26
    assert candidate(nums = [5, 3, 4, 2, 1, 6, 7, 8]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 20]) == 17
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 22
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 14
    assert candidate(nums = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 99999]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11]) == 8
    assert candidate(nums = [1, 2, 5, 3, 6, 4, 7, 8, 10, 9]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10]) == 21
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 0
    assert candidate(nums = [5, 8, 3, 9, 4, 10, 6, 11, 7, 12]) == 0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 1
    assert candidate(nums = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996, 6, 995, 7, 994, 8, 993, 9, 992, 10, 991]) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 0
    assert candidate(nums = [20, 10, 30, 5, 25, 15, 35, 40, 50, 60]) == 6
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 0, 8, 7, 9]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 36
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 25
    assert candidate(nums = [1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [100, 1, 101, 2, 102, 3, 103, 4, 104]) == 0
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 9, 10, 11, 12, 13, 14, 15]) == 12
    assert candidate(nums = [3, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 16
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15]) == 4
    assert candidate(nums = [1, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 22
    assert candidate(nums = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 0
    assert candidate(nums = [10, 11, 9, 12, 8, 13, 7, 14, 6, 15, 5, 16, 4, 17, 3, 18, 2, 19, 1, 20]) == 0
    assert candidate(nums = [5, 1, 4, 3, 6, 8, 2, 9, 7]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]) == 11
    assert candidate(nums = [50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90, 110, 100, 120, 110, 130, 120, 140, 130]) == 0
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 22, 23, 24, 25, 26]) == 8
    assert candidate(nums = [1, 5, 3, 4, 6, 2, 7, 8, 9, 10]) == 7
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4]) == 16
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 0
    assert candidate(nums = [10, 20, 30, 29, 28, 27, 26, 25, 24, 23]) == 2
    assert candidate(nums = [1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 14
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 16
    assert candidate(nums = [1, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 10]) == 21
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10, 11, 12, 13, 14, 15]) == 14
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 11, 10, 13, 15]) == 8
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 35, 40, 2, 45, 50]) == 4
    assert candidate(nums = [1, 2, 100, 3, 4, 101, 5, 6, 102, 7, 8]) == 4
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 0
    assert candidate(nums = [10, 20, 30, 25, 35, 40, 36, 45, 50, 55]) == 8
    assert candidate(nums = [5, 1, 4, 3, 6, 2, 7, 8, 10, 9]) == 4
