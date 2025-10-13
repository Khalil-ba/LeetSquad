# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [10, 5, 10, 4, 15]) == 7
    assert candidate(nums = [0, 1, 2, 3, 4, 5]) == 21
    assert candidate(nums = [1, 2, 2, 1]) == 8
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [2, 2, 2]) == 6
    assert candidate(nums = [0, 0, 0, 0, 0]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [10, 5, 8, 3, 9, 4, 6]) == 12
    assert candidate(nums = [1, 1, 1, 1, 1]) == 15
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5]) == 25
    assert candidate(nums = [3, 2, 1]) == 3
    assert candidate(nums = [1, 3, 2, 4, 3]) == 11
    assert candidate(nums = [5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [100000, 0, 100000, 0, 100000]) == 9
    assert candidate(nums = [5, 4, 3, 2, 1, 0]) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 29
    assert candidate(nums = [1, 0, 2, 0, 3, 0]) == 12
    assert candidate(nums = [1, 4, 2, 5, 3]) == 11
    assert candidate(nums = [10, 5, 9, 2, 3, 1]) == 8
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996]) == 5
    assert candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 210
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 11
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == 30
    assert candidate(nums = [5, 6, 7, 8, 9, 5, 6, 7, 8, 9]) == 35
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2]) == 36
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 60
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 41
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]) == 55
    assert candidate(nums = [7, 8, 9, 10, 5, 6, 2, 3, 4, 1]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 29
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 120
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 55
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 109
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 15
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 55
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 35
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 15
    assert candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 30
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 87
    assert candidate(nums = [7, 1, 5, 2, 6, 3, 4, 8, 9, 10, 1]) == 36
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 55
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == 35
    assert candidate(nums = [100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0]) == 30
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 71
    assert candidate(nums = [10, 10, 10, 10, 1, 1, 1, 1, 1, 10]) == 31
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 55
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 265
    assert candidate(nums = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == 37
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 11
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 55
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 210
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 10
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 109
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55
    assert candidate(nums = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 55
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 210
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 35
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 11
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == 110
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 25
    assert candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 30
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 78
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 35
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 11
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 29
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 47
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 96
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 92
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 55
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 63
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700]) == 48
    assert candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == 45
    assert candidate(nums = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 15
    assert candidate(nums = [5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1]) == 19
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 91
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9]) == 89
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 80
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 210
    assert candidate(nums = [1, 3, 2, 3, 4, 2, 1, 5, 6, 7, 8]) == 35
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 35
    assert candidate(nums = [1, 3, 5, 2, 4, 6, 7, 8, 9, 10]) == 41
    assert candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50]) == 110
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 76
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 76
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 46
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 30
    assert candidate(nums = [5, 3, 5, 2, 5, 1, 4, 3]) == 12
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 10
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 30
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 60
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 66
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 35
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 35
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 75
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 104
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 120
    assert candidate(nums = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 60
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 3, 3, 2, 2]) == 39
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 120
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 210
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 120
    assert candidate(nums = [100, 100, 99, 99, 98, 98, 97, 97, 96, 96]) == 15
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 55
    assert candidate(nums = [5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 30
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 120
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 120
    assert candidate(nums = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 78
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 55
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2]) == 73
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 64
    assert candidate(nums = [5, 3, 6, 7, 2, 4, 1, 8, 9, 0]) == 17
    assert candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 100, 200, 150, 300]) == 47
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4]) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 125
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 43
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 120
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 29
