# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [2, -5, -2, -4, 3]) == 24
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [-2, 3, -4]) == 24
    assert candidate(nums = [10, -20, 0, 5, 1]) == 10
    assert candidate(nums = [3, -1, 4]) == 4
    assert candidate(nums = [-1, -2, -3, 0]) == 6
    assert candidate(nums = [0, 2]) == 2
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 3628800
    assert candidate(nums = [2, 3, -2, 4]) == 6
    assert candidate(nums = [1, 2, -1, 4]) == 4
    assert candidate(nums = [0, 2, 0]) == 2
    assert candidate(nums = [-1, -2, -3, -4]) == 24
    assert candidate(nums = [-1]) == -1
    assert candidate(nums = [-2, 0, -1]) == 0
    assert candidate(nums = [-2, 3, -4, 5, 7, -8, 2, 3]) == 20160
    assert candidate(nums = [1, 2, 3, 4, 5]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3628800
    assert candidate(nums = [0, 2, 3, -2, 4, -1, 5]) == 240
    assert candidate(nums = [-10, 0, 10, 20, 30, -40, 50, 60, -70, 80]) == 4032000000000
    assert candidate(nums = [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0]) == 0
    assert candidate(nums = [2, 3, -2, 4, -1, 5, 6]) == 1440
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50]) == 2880000000000
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [-2, -3, 7, -4, 0, 5, -8, 3, 6]) == 84
    assert candidate(nums = [5, 0, 5, -1, 0, 5, -1, 0, 5, -1]) == 5
    assert candidate(nums = [0, 2, -3, 4, -5, 6]) == 720
    assert candidate(nums = [0, 2, -3, 4, -5, 6]) == 720
    assert candidate(nums = [2, 3, 0, -1, 4, 5, 0, -2, 3, 0]) == 20
    assert candidate(nums = [2, 3, 0, -1, -2, 4, 0, 5, 6, 0, -7, 8, -9]) == 504
    assert candidate(nums = [1, 0, -1, 0, 1, -1, 0, 1, 0]) == 1
    assert candidate(nums = [5, 6, -3, 4, 0, 2, 3, -2, 4]) == 30
    assert candidate(nums = [10, -10, 10, -10, 10, -10]) == 100000
    assert candidate(nums = [5, 6, -3, 4, 0, -1, 2, -5]) == 30
    assert candidate(nums = [0, 2, 3, -2, 4, -1, 5, 6]) == 1440
    assert candidate(nums = [2, -5, 3, 1, -4, 2]) == 240
    assert candidate(nums = [5, 3, -1, 2, 0, -6, -2, 0, 5, 3, -1, 2, 0, -6, -2]) == 15
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [-2, -3, 0, -2, -40, 0, -10]) == 80
    assert candidate(nums = [0, 2, -3, 4, -1, 2, 1, -5, 4]) == 160
    assert candidate(nums = [10, -2, -3, 5, -10, 0, 9, 6]) == 300
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 10, -10, 5, -5]) == 7812500000000
    assert candidate(nums = [-2, 0, -1, 0, 1, 2, -3]) == 2
    assert candidate(nums = [5, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 1814400
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 2880
    assert candidate(nums = [-1, -2, 0, 1, -3, 4, -5, 6, -7, 8, -9, 10]) == 1814400
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1]) == 1
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10]) == 100000
    assert candidate(nums = [-10, 0, 0, 0, 0, 0, 0, 0, 0, -10]) == 0
    assert candidate(nums = [-10, 0, 10, 0, -10, 0, 10, 0, -10, 0]) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3628800
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(nums = [-3, -1, 0, 2, 4, -2, 0, -1]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3628800
    assert candidate(nums = [3, -1, 4, 1, 5, -9, 2, 6, 5, 3, 5]) == 486000
    assert candidate(nums = [5, 3, -2, 5, -1, 5, -1, 0, 5]) == 750
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 1814400
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 120
    assert candidate(nums = [-10, 0, 5, 2, -3, -2, 4, 5, 0, -1, 2]) == 1200
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 1814400
    assert candidate(nums = [3, -1, 4, 1, 5, -9, 2, 6, -5, 3, 5]) == 162000
    assert candidate(nums = [0, 2, -3, 4, -1, 0, 5, -2]) == 24
    assert candidate(nums = [2, -5, -2, -4, 3]) == 24
    assert candidate(nums = [-10, 9, -10, 10, -1, -100]) == 900000
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 3628800
    assert candidate(nums = [3, -1, 4, -1, 5, -9, 2, 6, -5, 3, 5]) == 486000
    assert candidate(nums = [1, 0, -1, 0, -2, 0, 1, 0, -1, 0, -2, 0]) == 1
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == 1000000000000000000
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 3628800
    assert candidate(nums = [10, -10, 0, 10, -10, 0, 10]) == 10
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 362880
    assert candidate(nums = [0, 2, -3, -4, 5, 0, 1]) == 120
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [-10, -10, -10, -10, -10]) == 10000
    assert candidate(nums = [-2, 3, -4, 5, -6, 7, -8, 9, -10, 11]) == 19958400
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 3628800
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [1, 2, 3, -4, -5, -6, 7, 8, 9, 10, -11]) == 39916800
    assert candidate(nums = [10, -10, 10, -10, 10]) == 100000
    assert candidate(nums = [5, -3, 1, -2, 0, 4, -2, 3, -1]) == 30
    assert candidate(nums = [10, -10, 10, -10, 10, -10]) == 100000
    assert candidate(nums = [-10, -20, 0, -5, -7, 0, 2, -1]) == 200
    assert candidate(nums = [1, 2, 3, 0, -1, -2, -3, -4, 5, 6]) == 720
    assert candidate(nums = [1, 2, 3, 0, -1, -2, -3, 0, 4, 5, 6, 0, -7, -8, -9, 0, 10, 11, 12]) == 1320
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8]) == 40320
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10]) == 100000000
    assert candidate(nums = [2, 0, 1, 0, 2, 3, -2, 4, -1, 5]) == 240
