# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 2, 4, 5]) == 9
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 230
    assert candidate(nums = [1, -1, 2, -2, 3, -3]) == 22
    assert candidate(nums = [1, -1, 1, -1, 1]) == 8
    assert candidate(nums = [1, -1, 1, -1, 1, -1]) == 10
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000]) == 800000
    assert candidate(nums = [-10, -5, 0, 5, 10]) == 40
    assert candidate(nums = [-1, -2, -3, -4, -5]) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 230
    assert candidate(nums = [2, 4, 9, 24, 2, 1, 10]) == 68
    assert candidate(nums = [1, 2, 3, 4, 5]) == 8
    assert candidate(nums = [1, 3, 2, 1, 2, 3, 1]) == 9
    assert candidate(nums = [-1, 4, -2, 3]) == 16
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [-100000, 100000, -100000, 100000]) == 600000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 200
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 100000, 1, 100000, 1]) == 399996
    assert candidate(nums = [100, -100, 100, -100]) == 600
    assert candidate(nums = [100000, -100000, 100000, -100000]) == 600000
    assert candidate(nums = [-100000, 100000, -100000, 100000, -100000]) == 800000
    assert candidate(nums = [5, 4, 3, 2, 1]) == 8
    assert candidate(nums = [2, 3, 1, 5, 4]) == 10
    assert candidate(nums = [1, 2, 1, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 38
    assert candidate(nums = [5, 3, 8, 6, 7, 2, 4, 1, 9]) == 33
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [100000, -100000, 50000, -50000, 25000, -25000, 12500]) == 687500
    assert candidate(nums = [-10, 10, -10, 10, -10, 10, -10, 10, -10, 10]) == 180
    assert candidate(nums = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]) == 29
    assert candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50]) == 580
    assert candidate(nums = [100000, 0, -100000, 100000, 0, -100000, 100000]) == 900000
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17, 16, 18, 17, 19, 18, 20, 19, 21, 20]) == 91
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995]) == 11
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 9
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]) == 38
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 53
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1]) == 39
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 38
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400]) == 2900
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [-50000, 50000, -50000, 50000, -50000]) == 400000
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 9
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 38
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000]) == 1000000
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 21
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [100000, 0, -100000, 0, 100000, 0, -100000, 0, 100000]) == 900000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 580
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 23
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 53
    assert candidate(nums = [1, -100000, 2, -99999, 3, -99998, 4, -99997, 5, -99996]) == 900013
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 23
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 36
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9, 10]) == 43
    assert candidate(nums = [10000, 1000, 100, 10, 1, 0, -1, -10, -100, -1000, -10000]) == 31000
    assert candidate(nums = [1, 2, 3, -1, -2, -3, 4, 5, 6, -4, -5, -6, 7, 8, 9]) == 70
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 28
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]) == 219
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 38
    assert candidate(nums = [-100000, 100000, -100000, 100000, -100000, 100000, -100000, 100000, -100000, 100000]) == 1800000
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000]) == 800000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 23
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97]) == 675
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 17
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 320
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [-5, 5, -15, 15, -25, 25, -35, 35, -45, 45, -55, 55]) == 710
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 0, 6, 4, 3, 2, 1]) == 59
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 107
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == 38
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 33
    assert candidate(nums = [1, 2, 3, 100, 3, 2, 1, 99, 2, 1, 0]) == 399
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40]) == 380
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 68
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000, -100000, 100000, -100000]) == 1400000
    assert candidate(nums = [-100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000, -100000]) == 0
    assert candidate(nums = [-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991]) == 23
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 36
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 236
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 32
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 49
    assert candidate(nums = [1, 2, 3, 4, 5, 10000, 6, 7, 8, 9, 10]) == 20011
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 230
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 53
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500]) == 5800
    assert candidate(nums = [1, 200000, 3, 400000, 5, 600000, 7, 800000, 9, 1000000]) == 5799951
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000]) == 12000
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 31
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 859
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9]) == 48
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]) == 140
