# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-1, 3, 2, 0]) == True
    assert candidate(nums = [1, 3, 2, 4, 5]) == True
    assert candidate(nums = [3, 5, 0, 2, 3]) == False
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [1]) == False
    assert candidate(nums = [1, 2, 3, 4]) == False
    assert candidate(nums = [1, 2, 3, 3, 3, 4]) == False
    assert candidate(nums = [1, 2, 3, 4, 5]) == False
    assert candidate(nums = [1, 2, 3, -4, -3, -1]) == False
    assert candidate(nums = [3, 5, 0, 2, 4]) == True
    assert candidate(nums = [8, 10, 4, 6]) == False
    assert candidate(nums = [3, 1, 4, 2]) == True
    assert candidate(nums = [5, 4, 3, 2, 1]) == False
    assert candidate(nums = [1, 2]) == False
    assert candidate(nums = [1, 2, 3, 2, 1]) == True
    assert candidate(nums = [3, 3, 3, 3, 3]) == False
    assert candidate(nums = [3, 5, 4, 2, 5]) == True
    assert candidate(nums = [1, 0, 1, -4, -3]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2]) == False
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10]) == False
    assert candidate(nums = [3, 5, 0, 3, 4]) == True
    assert candidate(nums = [3, 5, 0, 2, 4, 6, 1]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False
    assert candidate(nums = [2, 1, 3, 5, 0, 4, 6, 7]) == True
    assert candidate(nums = [5, 1, 6, 3, 4, 2, 7]) == True
    assert candidate(nums = [3, 1, 4, 2, 5, 3, 6, 4, 7]) == True
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 8, 9]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 3, 5, 7, 9]) == True
    assert candidate(nums = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [-2, -3, 0, 1, -1, -4, 2, 3]) == True
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 0]) == False
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 13, 14]) == False
    assert candidate(nums = [8, 10, 4, 6, 2, 1, 9, 5]) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, 11]) == False
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 8, 10, 9, 11]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(nums = [3, 1, 4, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 8, 10, 9, 11, 13, 12, 14, 15]) == True
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3]) == False
    assert candidate(nums = [3, 1, 4, 2, 5, 0]) == True
    assert candidate(nums = [10, 9, 8, 7, 11, 10, 12, 11, 13, 14]) == True
    assert candidate(nums = [8, 10, 4, 6, 2, 1, 9, 5, 7, 3]) == True
    assert candidate(nums = [7, 11, 5, 9, 6, 10, 3, 8, 2, 12]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, -1, 2, -2, 3, -3]) == True
    assert candidate(nums = [9, 11, 8, 9, 10, 7, 8, 9, 11, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9]) == True
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert candidate(nums = [1, 5, 3, 4, 2, 1, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 2, 4, 5, 6, 7, 8, 9, 0, 1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 15, 20]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1, 3, 2, 4, 5, 6, 7, 8, 9, 0]) == True
    assert candidate(nums = [8, 10, 4, 6, 2, 1, 9]) == True
    assert candidate(nums = [7, 1, 3, 2, 6, 5, 8, 4, 9, 0]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 0]) == True
    assert candidate(nums = [1, 2, 4, 3, 5, 6, 0]) == True
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0, 8, 9]) == False
    assert candidate(nums = [3, 1, 4, 2, 5, 6, 0, 7, 8, 9]) == True
    assert candidate(nums = [3, 5, 0, 2, 1, 4]) == True
    assert candidate(nums = [5, 1, 6, 4, 7, 3, 8, 2, 9]) == True
    assert candidate(nums = [3, 1, 4, 2, 5, 3, 6, 4, 7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]) == True
    assert candidate(nums = [3, 1, 4, 2, 5, 3]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1, 6]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2, 0]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1, 2]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12]) == False
    assert candidate(nums = [3, 5, 0, 3, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
    assert candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == False
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == False
    assert candidate(nums = [3, 1, 4, 2, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(nums = [3, 5, 0, 2, 8, 6, 7, 4, 1]) == True
    assert candidate(nums = [3, 1, 2, 4, 5, 0]) == False
    assert candidate(nums = [-1, -2, 2, 1, -3, -4, 3, 4]) == True
    assert candidate(nums = [1, 2, 0, 3, 4, -1, 5]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [1, 5, 4, 6, 7, 8, 9, 10, 2, 3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 8, 9, 10, 11]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 50, 60, 70, 80, 90, 100, 55, 65, 75, 85]) == True
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 8, 9, 10]) == True
    assert candidate(nums = [3, 5, 0, 2, 3, 1, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0]) == False
    assert candidate(nums = [1000000000, -1000000000, 500000000, 250000000, 750000000, 375000000, 625000000]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == False
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [3, 5, 0, 2, 4, 1]) == True
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == True
    assert candidate(nums = [1, 5, 3, 2, 4]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 0]) == False
    assert candidate(nums = [9, 11, 8, 9, 10, 7, 6, 5, 12]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 0]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 0, 7]) == True
    assert candidate(nums = [3, 1, 3, 2, 4, 3]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == False
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 3, 9, 3, 2, 8, 8, 4, 6]) == True
    assert candidate(nums = [8, 10, 4, 6, 2, 1, 9, 5]) == True
    assert candidate(nums = [1, 5, 3, 4, 2]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14]) == False
    assert candidate(nums = [3, 5, 0, 2, 8, 7, 6, 4, 1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == True
    assert candidate(nums = [5, 3, 4, 2, 1, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [8, 10, 4, 6, 2, 1, 9, 5, 7]) == True
    assert candidate(nums = [3, 5, 0, 2, 1]) == True
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == True
    assert candidate(nums = [3, 5, 0, 2, 8, 6, 7, 4, 1, 12, 14, 13, 11, 9, 10, 15, 16, 17, 18, 19]) == True
    assert candidate(nums = [5, 3, 1, 2, 4, 6, 7, 8, 0]) == False
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 2, 9]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 55, 65, 75]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1]) == False
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == False
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
