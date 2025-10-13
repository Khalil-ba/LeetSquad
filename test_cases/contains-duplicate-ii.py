# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 8) == False
    assert candidate(nums = [1, 0, 1, 1],k = 1) == True
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0],k = 10) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9],k = 1) == True
    assert candidate(nums = [1, 2, 2, 1],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5],k = 4) == False
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 9) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 18) == True
    assert candidate(nums = [9, 9],k = 1) == True
    assert candidate(nums = [9, 1, 2, 3, 9],k = 4) == True
    assert candidate(nums = [1],k = 0) == False
    assert candidate(nums = [1, 2, 3, 1],k = 3) == True
    assert candidate(nums = [999999999, 999999999, 1, 1],k = 2) == True
    assert candidate(nums = [999999999, -999999999, 999999999],k = 2) == True
    assert candidate(nums = [1, 2, 2],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 8) == False
    assert candidate(nums = [1, 1],k = 0) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1],k = 20) == True
    assert candidate(nums = [1, 2, 3, 1, 2, 3],k = 2) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == True
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3) == True
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2],k = 1) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 7) == False
    assert candidate(nums = [1, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1) == False
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999999],k = 9) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1],k = 1) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10],k = 10) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50],k = 49) == True
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1],k = 20) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5],k = 49) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 10) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1],k = 10) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 9) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1],k = 20) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],k = 10) == True
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1],k = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],k = 10) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30],k = 29) == True
    assert candidate(nums = [1000000000, 1000000000, 1, 2, 3],k = 1) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000, 1000000000],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1],k = 14) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 9) == True
    assert candidate(nums = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4],k = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 8) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 17) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1],k = 0) == False
    assert candidate(nums = [1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999],k = 2) == True
    assert candidate(nums = [1000000000, 1000000000],k = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 4) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1],k = 29) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == False
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10],k = 9) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 9) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1],k = 49) == False
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],k = 10) == True
    assert candidate(nums = [-1000000000, -2000000000, -1000000000, -3000000000, -2000000000],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1],k = 100000) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 18) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 8) == False
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007, 1000000008, 1000000009, 1000000000],k = 10) == True
    assert candidate(nums = [10, 1, 2, 10, 3, 4, 5, 10, 6, 7, 8, 9, 10],k = 8) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 1],k = 24) == False
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 1],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1],k = 19) == False
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20],k = 20) == True
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1) == True
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 5) == False
    assert candidate(nums = [1000000000, 2000000000, 1000000000, 3000000000, 2000000000],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1],k = 20) == True
    assert candidate(nums = [1000000000, 2000000000, 1000000000],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],k = 10) == True
    assert candidate(nums = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],k = 2) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 10) == True
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 10) == True
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1],k = 30) == True
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == False
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5],k = 10) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 1],k = 39) == False
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1],k = 2) == True
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],k = 2) == True
    assert candidate(nums = [1, 0, 1, 1, 0, 1],k = 2) == True
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0],k = 5) == False
    assert candidate(nums = [1000000000, 1000000001, 1000000000, 1000000001, 1000000000],k = 2) == True
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 1) == True
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],k = 4) == False
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 1],k = 20) == True
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990, 999999999],k = 9) == False
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],k = 10) == True
