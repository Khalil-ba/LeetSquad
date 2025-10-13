# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1]) == -1
    assert candidate(nums = [1, 3, 2]) == 2
    assert candidate(nums = [9, 5, 6]) == 6
    assert candidate(nums = [9, 11, 10]) == 10
    assert candidate(nums = [1, 2]) == -1
    assert candidate(nums = [7, 8, 9]) == 8
    assert candidate(nums = [100, 1, 50]) == 50
    assert candidate(nums = [5, 3, 4, 1, 2]) == 3
    assert candidate(nums = [2, 1, 3]) == 2
    assert candidate(nums = [5, 10, 3, 8, 1]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50]) == 20
    assert candidate(nums = [7]) == -1
    assert candidate(nums = [5, 1, 4, 3, 2]) == 4
    assert candidate(nums = [3, 2, 1, 4]) == 3
    assert candidate(nums = [7, 8, 9]) == 8
    assert candidate(nums = [42, 24, 36, 12, 60, 72, 48]) == 42
    assert candidate(nums = [2, 1, 3, 5, 4, 6]) == 2
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35]) == 10
    assert candidate(nums = [30, 1, 29, 2, 28, 3, 27, 4, 26, 5]) == 29
    assert candidate(nums = [42, 35, 28, 21, 14, 7]) == 35
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94]) == 99
    assert candidate(nums = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]) == 59
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 5
    assert candidate(nums = [1, 100, 50, 75, 25]) == 50
    assert candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 8
    assert candidate(nums = [6, 4, 2, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == 6
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 3
    assert candidate(nums = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 59
    assert candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 22
    assert candidate(nums = [33, 11, 22, 44, 55, 66, 77, 88, 99, 111, 222, 333, 444, 555]) == 33
    assert candidate(nums = [5, 10, 15, 20, 25]) == 10
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93]) == 2
    assert candidate(nums = [100, 1, 50, 25, 75, 33, 67, 88, 99, 2]) == 50
    assert candidate(nums = [7, 3, 9, 11, 5]) == 7
    assert candidate(nums = [42]) == -1
    assert candidate(nums = [45, 23, 67, 89, 12, 34, 56, 78, 90, 10, 20]) == 45
    assert candidate(nums = [100]) == -1
    assert candidate(nums = [42, 3, 7, 18, 29, 1]) == 3
    assert candidate(nums = [8, 6, 4, 2, 1, 3, 5, 7, 9, 10]) == 8
    assert candidate(nums = [7, 77, 777, 7777]) == 77
    assert candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 22
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 25
    assert candidate(nums = [100, 1, 50, 25, 75]) == 50
    assert candidate(nums = [8, 6, 4, 2, 0, -2, -4]) == 6
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88]) == 16
    assert candidate(nums = [101, 99, 98, 100, 97, 96, 95, 94, 93, 92, 91]) == 99
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 98
    assert candidate(nums = [4, 1, 3, 2, 5, 7, 6, 8]) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 20
    assert candidate(nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 12
    assert candidate(nums = [88, 99, 77, 66, 55, 44]) == 88
    assert candidate(nums = [45, 30, 15, 60, 75, 90]) == 45
    assert candidate(nums = [31, 1, 41, 59, 26, 53, 58, 97, 93, 23]) == 31
    assert candidate(nums = [5, 1, 9, 3, 7]) == 5
    assert candidate(nums = [5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [55, 45, 35, 25, 15, 5, 10, 20, 30, 40]) == 45
    assert candidate(nums = [7, 3, 5, 1, 9, 11]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50]) == 20
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 3
    assert candidate(nums = [45, 30, 60, 20, 70]) == 45
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 3
    assert candidate(nums = [5, 3, 7, 1, 9, 11, 13, 15, 17, 19, 21]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2
    assert candidate(nums = [100, 1, 50, 2, 99]) == 50
    assert candidate(nums = [33, 22, 11, 44, 55, 66, 77, 88, 99]) == 33
    assert candidate(nums = [7, 1, 5, 3, 6, 4]) == 5
    assert candidate(nums = [10, 5, 15, 20, 25]) == 10
    assert candidate(nums = [42, 27, 58, 19, 33, 49, 21]) == 42
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70]) == 20
    assert candidate(nums = [99, 100]) == -1
    assert candidate(nums = [25, 20, 15, 10, 5]) == 20
    assert candidate(nums = [7, 14, 21, 28, 35, 42]) == 14
    assert candidate(nums = [100, 1, 2, 3, 99, 50]) == 2
    assert candidate(nums = [66, 33, 99, 22, 44, 77, 55, 11, 88]) == 66
    assert candidate(nums = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]) == 34
    assert candidate(nums = [5, 3, 8, 1, 4]) == 5
    assert candidate(nums = [100, 1, 50, 99, 2, 98]) == 50
    assert candidate(nums = [8, 15, 3, 12, 7, 18]) == 8
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 29
    assert candidate(nums = [7, 14, 9, 11, 6, 12]) == 7
    assert candidate(nums = [5, 1, 100, 10, 50, 20, 60, 30, 40, 70, 80, 90]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 10
    assert candidate(nums = [3, 1, 2, 4, 5]) == 3
    assert candidate(nums = [50, 40]) == -1
    assert candidate(nums = [10, 5, 3, 8, 2]) == 5
    assert candidate(nums = [100, 1, 50, 75, 25, 125, 62]) == 100
    assert candidate(nums = [97, 98, 95, 96, 99]) == 97
    assert candidate(nums = [8, 6, 7, 5, 3, 0, 9]) == 8
    assert candidate(nums = [100, 1, 50, 99, 2]) == 50
    assert candidate(nums = [47, 29, 83, 61, 95, 17, 53]) == 47
