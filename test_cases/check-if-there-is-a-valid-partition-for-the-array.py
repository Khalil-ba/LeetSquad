# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 4, 5]) == False
    assert candidate(nums = [2, 2, 2, 3, 3, 4, 4, 4]) == True
    assert candidate(nums = [2, 2, 3, 3, 4, 4]) == True
    assert candidate(nums = [1, 2, 3, 3, 3, 4, 5, 5]) == False
    assert candidate(nums = [1, 1, 2, 3, 4, 4, 5, 6]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == True
    assert candidate(nums = [1, 1, 1, 1]) == True
    assert candidate(nums = [1, 2, 3, 3, 3, 3]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [1, 3, 5, 7, 9]) == False
    assert candidate(nums = [1, 1, 2, 2, 3, 3]) == True
    assert candidate(nums = [1000000, 1000000]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == True
    assert candidate(nums = [1, 1, 1, 2]) == False
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 5, 5]) == True
    assert candidate(nums = [1, 2, 3, 4, 5]) == False
    assert candidate(nums = [4, 4, 4, 5, 6]) == True
    assert candidate(nums = [1, 2, 2, 3, 3, 3]) == False
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == True
    assert candidate(nums = [1, 2, 3, 2, 2, 3, 4, 5]) == True
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3]) == True
    assert candidate(nums = [1, 2, 3]) == True
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [2, 2, 3, 4, 5, 5, 5]) == True
    assert candidate(nums = [2, 2]) == True
    assert candidate(nums = [4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == True
    assert candidate(nums = [1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19]) == True
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 10, 10]) == False
    assert candidate(nums = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23]) == False
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == True
    assert candidate(nums = [5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15]) == True
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8, 9]) == True
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == True
    assert candidate(nums = [3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == True
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == True
    assert candidate(nums = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16]) == True
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [9, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == True
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 9, 10, 10]) == True
    assert candidate(nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 15, 15, 15]) == True
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == True
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == True
    assert candidate(nums = [2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10, 11, 11, 11, 12, 12, 13, 13]) == True
    assert candidate(nums = [9, 9, 10, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16]) == False
    assert candidate(nums = [3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10, 10]) == True
    assert candidate(nums = [10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20]) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [5, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 13]) == True
    assert candidate(nums = [5, 6, 7, 8, 8, 9, 10, 10, 11, 11]) == False
    assert candidate(nums = [10, 10, 10, 11, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17]) == True
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23]) == False
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == True
    assert candidate(nums = [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == True
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == True
    assert candidate(nums = [5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == True
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 24, 25, 26]) == False
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [1, 2, 3, 2, 2, 3, 4, 5, 6, 6, 6]) == True
    assert candidate(nums = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 10, 10]) == True
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == True
    assert candidate(nums = [5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10, 11, 11, 12, 12]) == True
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == True
    assert candidate(nums = [5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == False
    assert candidate(nums = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == False
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == False
    assert candidate(nums = [4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]) == True
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 11, 12, 12, 12]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
    assert candidate(nums = [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == True
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21, 22, 22]) == False
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == True
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12]) == True
    assert candidate(nums = [3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 18, 19, 20]) == True
    assert candidate(nums = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 15, 15, 15, 16, 16, 16]) == True
    assert candidate(nums = [2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == True
    assert candidate(nums = [3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8]) == True
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 8]) == False
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == True
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16]) == True
    assert candidate(nums = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 13, 13, 14, 14]) == True
    assert candidate(nums = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19]) == False
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8]) == True
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == True
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 25, 26, 27, 28, 29, 30, 30, 30]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23]) == False
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 12, 13, 13]) == False
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18]) == False
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == True
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17]) == True
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14]) == False
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == True
    assert candidate(nums = [1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == True
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]) == True
    assert candidate(nums = [1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10, 10, 11, 12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25]) == False
    assert candidate(nums = [9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13]) == True
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10]) == False
    assert candidate(nums = [9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23]) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == True
    assert candidate(nums = [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19]) == True
    assert candidate(nums = [2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 11, 11]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15]) == True
    assert candidate(nums = [10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22]) == True
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17]) == False
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8]) == True
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == False
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9]) == False
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == True
    assert candidate(nums = [2, 2, 3, 3, 4, 5, 5, 6, 6, 7]) == False
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == True
