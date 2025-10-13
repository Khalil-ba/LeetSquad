# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-1, 0, 1, -1, 0]) == True
    assert candidate(nums = [1, 1, 1, 1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [5, -1, 5, -1]) == True
    assert candidate(nums = [1, 2, 3, 3, 2, 1]) == True
    assert candidate(nums = [-1, 0, 1, 0, -1]) == True
    assert candidate(nums = [1000000000, 1000000000]) == False
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == False
    assert candidate(nums = [-1, -2, -3, -4, -5]) == False
    assert candidate(nums = [1, 2, 3, 4, 5]) == False
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == True
    assert candidate(nums = [0, 0, 0]) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000]) == True
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == True
    assert candidate(nums = [-1, 0, 1, 0, -1, 0, 1]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000]) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [1, 2, 1, 2]) == True
    assert candidate(nums = [1, 1, 2, 3, 3, 4]) == False
    assert candidate(nums = [-1, 0, 1, -1, 0, 1]) == True
    assert candidate(nums = [-1000000000, 1000000000, -1000000000, 1000000000]) == True
    assert candidate(nums = [4, 2, 4]) == True
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1]) == True
    assert candidate(nums = [-1, -2, -3, -1, -2, -3, -1, -2, -3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == True
    assert candidate(nums = [10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]) == True
    assert candidate(nums = [7, 3, 5, 7, 9, 5, 3, 1, 5, 7, 9, 3, 5, 7, 1]) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == True
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, 200]) == True
    assert candidate(nums = [-1, -2, -3, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == True
    assert candidate(nums = [500000000, -500000000, 500000000, -500000000, 500000000, -500000000]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == True
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 250000000, -250000000, 125000000, -125000000]) == True
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90, 110]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [999999999, -999999999, 999999999, -999999999, 999999999, -999999999, 999999999, -999999999]) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == True
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True
    assert candidate(nums = [5, 5, 10, 15, 5, 5]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5]) == True
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 11]) == True
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == False
    assert candidate(nums = [5, -5, 5, -5, 5, -5]) == True
    assert candidate(nums = [5, 3, 5, 3, 5, 3]) == True
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == False
    assert candidate(nums = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == True
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1]) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]) == True
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == True
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == False
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == True
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1]) == True
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == True
    assert candidate(nums = [999999999, 999999999, -999999999, -999999999, 1, -1, 1, -1]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == True
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == False
    assert candidate(nums = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]) == True
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == True
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80, 70, 90, 80, 100, 90, 110, 100, 120, 110, 130, 120, 140, 130, 150, 140, 160]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2, -3, -4, -5]) == True
    assert candidate(nums = [5, -5, 5, -5, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]) == True
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == False
    assert candidate(nums = [-1, 2, -1, 2, -1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
    assert candidate(nums = [5, 15, -10, 5, 10, 0, -5, 15, 5]) == True
    assert candidate(nums = [100, -100, 100, -100, 100, -100]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 600]) == True
    assert candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == True
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]) == True
    assert candidate(nums = [1, 3, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == True
    assert candidate(nums = [100, 200, 300, 100, 200, 300, 100, 200, 300]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3]) == True
    assert candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]) == True
