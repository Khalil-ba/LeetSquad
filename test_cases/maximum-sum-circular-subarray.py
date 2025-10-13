# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, -2, 3, -2]) == 3
    assert candidate(nums = [10, -2, 5, 1, -4, 3, -1]) == 16
    assert candidate(nums = [2, 3, -4, 5, 7]) == 17
    assert candidate(nums = [5, -3, 5]) == 10
    assert candidate(nums = [3, -1, 2, -1]) == 4
    assert candidate(nums = [2, -2, 2, 7]) == 11
    assert candidate(nums = [-1, -2, -3, 4]) == 4
    assert candidate(nums = [9, -4, 7, 3, -2]) == 17
    assert candidate(nums = [10, 0, 3, 5, -10, 2, 4]) == 24
    assert candidate(nums = [1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [-1, -2, -3, -4]) == -1
    assert candidate(nums = [1, -4, 7, 2]) == 10
    assert candidate(nums = [-1, -2, -3, -4, -5]) == -1
    assert candidate(nums = [9, -4, 7, 2, -1]) == 17
    assert candidate(nums = [-3, -2, -3]) == -2
    assert candidate(nums = [100, -1, -2, -3, -4, -5, -6, -7, -8, -9, 100, 100, -200, 100, 100]) == 455
    assert candidate(nums = [-10, -20, -30, 15, 20, 25, -10, -5]) == 60
    assert candidate(nums = [5, -3, 5, -2, 3, -4, 7, -6, 8, -1]) == 18
    assert candidate(nums = [3, -1, 4, -1, 5, -9, 2, 6, -3, 8]) == 23
    assert candidate(nums = [10, -3, 4, -2, -1, 10, -10, 5, 6, -5, 2]) == 26
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [2, 4, -2, -3, 8]) == 14
    assert candidate(nums = [1, 2, 3, -6, 4, 5, 6, -10, 7, 8, 9]) == 39
    assert candidate(nums = [1, 2, 3, 4, 5, -20, 1, 2, 3, 4, 5, -20, 1, 2, 3, 4, 5]) == 30
    assert candidate(nums = [3, -2, 2, 5, -3]) == 8
    assert candidate(nums = [1, -10, 3, 4, -2, 5]) == 11
    assert candidate(nums = [100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 100
    assert candidate(nums = [-2, 4, -3, 5, 1, -5, 3, -1, 2, 4, -5]) == 10
    assert candidate(nums = [-1, -1, -1, -1, -1, 100, -1, -1, -1, -1]) == 100
    assert candidate(nums = [-5, -1, -8, 2, 6, -3, 4, 2, -8, 3, 7]) == 13
    assert candidate(nums = [-1, 4, -2, 3, -2, 4, -2, 3, -1, 2, -5, 6]) == 14
    assert candidate(nums = [2, 3, -4, 5, 7, 1, -1, -3, 4]) == 18
    assert candidate(nums = [8, -1, 3, -4, 3, 2, -2, 5, 7, -4, 5, -2, 1, 2, -1, 3, 4, -3, 4, -1, -2, 1, 5]) == 37
    assert candidate(nums = [-1, -2, -3, 20, -1, -2, -3, 20, -1, -2, -3, 20]) == 48
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 4
    assert candidate(nums = [1, 2, 3, -5, 6, 7, -8, 9, 10, -11, 12]) == 37
    assert candidate(nums = [3, -2, 2, -3, 4, -1, 2, 1, -5, 4]) == 10
    assert candidate(nums = [5, -3, 5, -3, 5, -3, 5, -3, 5, -3]) == 13
    assert candidate(nums = [-1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000]) == 5000
    assert candidate(nums = [10000, -1000, 5000, -500, 2000, -300]) == 16200
    assert candidate(nums = [1, -2, 3, -2, 4, -1, 2, 1, -5, 4]) == 10
    assert candidate(nums = [8, -1, 3, -2, 4, -3, 2, 1, -5, 4]) == 16
    assert candidate(nums = [10, -20, 5, 5, -3, 2, -1]) == 18
    assert candidate(nums = [7, 5, -3, 6, -1, 8, -4, 2]) == 24
    assert candidate(nums = [-1, -2, -3, 4, 5, -1, 2, -1]) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [3, -1, 4, -1, 5, -9, 2, 6, -5, 3, -8]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5]) == 30
    assert candidate(nums = [-5, 1, 5, 0, -7, 3, -1, 2]) == 6
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 5
    assert candidate(nums = [-2, -3, 4, -1, -2, 1, 5, -3, 2, -5]) == 7
    assert candidate(nums = [-10, 15, -20, 25, -30, 35, -40, 45, -50, 55]) == 75
    assert candidate(nums = [7, 5, -3, 6, -5, 2, -7, 8, -2, 4, 5]) == 30
    assert candidate(nums = [1, -2, 3, -2, 5, 6, -4, 2]) == 13
    assert candidate(nums = [-2, -3, -1, -4, -5, -7, -8, -6, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == -1
    assert candidate(nums = [1, 2, 3, 4, -10, 1, 2, 3, 4]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 15
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 6
    assert candidate(nums = [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1, -1, -2]) == 15
    assert candidate(nums = [-1, -2, -3, 4, 5, -10, 6, 7]) == 16
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 1000]) == 1000
    assert candidate(nums = [-5, -1, -8, -9, -2, -6, -3, -8, -4, -5]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, -5, -10, -15, -20, -25, 50, 100, -50, -100, 150, -200, 250, -300, 350, -400]) == 350
    assert candidate(nums = [3, -1, 2, -1, 4, -2, 5, -3, 6, -4, 7, -5, 8, -6, 9, -7, 10, -8]) == 25
    assert candidate(nums = [3, -2, 2, -3, 4, -1, 2, 1, -5, 4, 3, -2, 2, -3, 4, -1, 2, 1, -5, 4]) == 15
    assert candidate(nums = [-5, 5, -5, 5, -5, 5]) == 5
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == 50
    assert candidate(nums = [-2, 4, -3, 4, -1, -2, 1, 5, -3]) == 8
    assert candidate(nums = [100, -200, 300, -400, 500, -600, 700, -800, 900, -1000, 1000]) == 1500
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, -6, 7, 8, 9, 10]) == 49
    assert candidate(nums = [15, -2, 20, 4, -5, -9, -10]) == 37
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 10]) == 25
    assert candidate(nums = [1, -10, 3, 4, -5, 2, 6, -1, 4]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(nums = [3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13]) == 20
    assert candidate(nums = [10, -7, 9, -7, 9, -7, 9, 9, -6, -4, 6]) == 31
    assert candidate(nums = [100, -1, -100, 100, -1, -100, 100, -1, -100, 100]) == 200
    assert candidate(nums = [5, -2, 5, -2, 5, -2, 5, -2]) == 14
    assert candidate(nums = [-10, 2, 3, -2, 5, -6, 7, -8, 9, -10]) == 10
    assert candidate(nums = [5, 10, -20, 5, 10, 5]) == 35
    assert candidate(nums = [8, -1, 3, 4, -2, -3, 6, 1]) == 21
    assert candidate(nums = [5, 5, 5, 5, -10, 5, 5, 5, 5]) == 40
    assert candidate(nums = [10, -5, 4, -1, 12, -3, 7, -2, 8, -6]) == 30
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
    assert candidate(nums = [8, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15]) == 15
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == 90
    assert candidate(nums = [2, 3, -4, 5, 7, -10, 20, -5, 3, -2, 1, -1, 4, -3, 2, -2, 5, -7, 8, -6]) == 30
    assert candidate(nums = [-1, -2, 3, 4, -5, 6, -7, 8, -9, 10]) == 16
    assert candidate(nums = [1, 2, 3, -6, 1, 2, 3, 4, 5, -10, 1, 2, 3, 4, 5]) == 30
    assert candidate(nums = [-1, -3, -5, 2, 1, -1, -2, 3, 4]) == 7
    assert candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 15
    assert candidate(nums = [100, -100, 100, -100, 100, -100, 100]) == 200
    assert candidate(nums = [-5, 5, -5, 5, -5, 5, -5, 5]) == 5
    assert candidate(nums = [3, -1, -1, 3, 5, -7, 5]) == 14
    assert candidate(nums = [1, -2, 3, 5, -6, 4, 2]) == 13
    assert candidate(nums = [0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == 15
    assert candidate(nums = [-5000, -1000, -3000, -2000, -4000, -1500]) == -1000
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 90
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5]) == 30
    assert candidate(nums = [1, 2, 3, -6, 4, 5, 6, -10, 1, 2, 3, 4]) == 25
    assert candidate(nums = [5, -1, 5, -2, 3, 4, -5]) == 14
    assert candidate(nums = [-1, -2, -3, -4, -5, 15, 10, 5, -10, -5, 20, 25, -30]) == 60
    assert candidate(nums = [3, -4, 5, 2, -6, 1, 4, -3, 2, -5]) == 7
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -1
    assert candidate(nums = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, -10]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -100, 10, 20, 30, 40, 50]) == 195
    assert candidate(nums = [5, 1, -2, 3, -1, 2]) == 10
    assert candidate(nums = [10, -2, -3, -4, 7, 9, -20, 10, 15]) == 42
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [3, -2, 2, 5, -3, 3, 5, -2, 3, 2, 5, -3]) == 21
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 22
    assert candidate(nums = [5, -1, 5, -1, 5, -1, 5, -1, 5, -1]) == 21
    assert candidate(nums = [100, -1, 100, -1, 100, -1, 100, -1, 100]) == 497
    assert candidate(nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]) == 12
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1]) == 1
