# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 4, 3, 2, 1]) == False
    assert candidate(nums = [0, -1, 2, -3, 4, -5, 6, -7]) == True
    assert candidate(nums = [-1, 0, 1, 2, -1, -4]) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1]) == False
    assert candidate(nums = [20, 100, 10, 12, 5, 13]) == True
    assert candidate(nums = [1, 1, 1, 1, 1]) == False
    assert candidate(nums = [1, 2]) == False
    assert candidate(nums = [0, -1, 1]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1]) == False
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2]) == False
    assert candidate(nums = [0, 4, 2, 1, 0, -1, -3]) == False
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == True
    assert candidate(nums = [2, 1, 5, 0, 4, 6]) == True
    assert candidate(nums = [1, 2, 0, 4, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5]) == True
    assert candidate(nums = [20, 100, 10, 12, 5, 13]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 6]) == True
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3]) == True
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 4, 5, 6, 5, 7, 5]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5]) == True
    assert candidate(nums = [2147483647, -2147483648, 0, 1, -1, 2, -2, 3, -3]) == True
    assert candidate(nums = [1000000000, 999999999, 1, 1000000001]) == False
    assert candidate(nums = [10, 20, 30, 15, 25, 35]) == True
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3]) == True
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 1, 9, 2, 5, 1]) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 3]) == True
    assert candidate(nums = [1, 2, 0, 4, 5, 3, 6]) == True
    assert candidate(nums = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10, 0]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 7]) == True
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == False
    assert candidate(nums = [9, 11, 13, 12, 14, 15, 16]) == True
    assert candidate(nums = [3, 1, 4, 2, 5, 7, 8]) == True
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 1]) == False
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 8, 10, 9]) == True
    assert candidate(nums = [5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7]) == True
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8]) == True
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5]) == True
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21, 22, 23]) == True
    assert candidate(nums = [7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3]) == True
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 4, 7]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7]) == True
    assert candidate(nums = [2, 1, 5, 0, 4, 6, 3, 8, 7, 9]) == True
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == True
    assert candidate(nums = [1, 20, 3, 10, 5, 15, 8, 25, 12]) == True
    assert candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == False
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1, -2, -3, -4, -5]) == False
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 5]) == True
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18, 102, 103]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True
    assert candidate(nums = [-1000000000, -999999999, -1000000001, -1000000002, -1000000003]) == False
    assert candidate(nums = [10, 1, 11, 1, 12, 1, 13, 1]) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == False
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == True
    assert candidate(nums = [8, 10, 4, 6, 9, 1, 5, 3, 7, 2]) == True
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]) == True
    assert candidate(nums = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == True
    assert candidate(nums = [3, 1, 4, 2, 5]) == True
    assert candidate(nums = [3, 5, 0, 2, 1, 4, 6, 7, 8, 9]) == True
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == False
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == True
    assert candidate(nums = [1000000000, 999999999, 1000000001, 1000000002, 999999998]) == True
    assert candidate(nums = [7, 7, 7, 8, 7, 7, 7, 7, 9, 7]) == True
    assert candidate(nums = [8, 1, 2, 3, 7, 4, 5]) == True
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 1, 2, 3, 4, 5]) == True
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5]) == True
    assert candidate(nums = [8, 1, 3, 7, 4, 6, 2, 9, 5, 10]) == True
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == False
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10, 11, 12, 13, 14]) == True
    assert candidate(nums = [6, 5, 4, 8, 7, 9, 2, 1, 3, 4]) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000, -1000000000, 1000000000]) == False
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == True
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == False
    assert candidate(nums = [1000000000, 999999999, 1000000001, 999999998, 1000000002, 999999997, 1000000003]) == True
    assert candidate(nums = [1, 2, 0, 4, 5, 3, 7, 8, 6, 9]) == True
    assert candidate(nums = [-10, -20, -15, -25, -30, -5, -35]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]) == True
    assert candidate(nums = [1000000000, 999999999, 1000000001, 1000000002, 1000000003]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == True
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8]) == False
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == True
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8]) == False
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [1000000000, 500000000, 750000000, 1000000001, 1000000002]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 0, 6, 7, 8]) == True
    assert candidate(nums = [3, 2, 1, 2, 1, 0, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [3, 1, 2, 4, 6, 5, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6]) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]) == False
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 100000000, -100000000, 50000000, -50000000]) == True
    assert candidate(nums = [1, 5, 0, 4, 2, 3, 6]) == True
    assert candidate(nums = [1, 2, 3, 4, 3, 5, 4, 6, 5, 7, 6, 8]) == True
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 4]) == True
    assert candidate(nums = [3, 1, 2, 4, 3, 5, 6, 1, 2, 7]) == True
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 35]) == True
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8]) == True
    assert candidate(nums = [1, 3, 2, 4, 3, 5]) == True
    assert candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == True
    assert candidate(nums = [8, 9, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [1000000000, 999999999, 1000000001, 1000000002, 999999998, 1000000003]) == True
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 3, 5]) == True
    assert candidate(nums = [7, 7, 7, 1, 2, 8, 10, 9, 11]) == True
    assert candidate(nums = [9, 11, 8, 9, 10, 7, 10]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9]) == False
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 1, 9, 5, 5, 5]) == True
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == False
    assert candidate(nums = [5, 1, 5, 5, 2, 5, 4, 7, 6, 8, 9]) == True
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
    assert candidate(nums = [5, 1, 4, 2, 3, 6]) == True
    assert candidate(nums = [2, 1, 3, 0, 4, -1, 5, 6, 7, 8]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5]) == True
    assert candidate(nums = [1, 2, 2, 1, 2, 3]) == True
