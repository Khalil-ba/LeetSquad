# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [0, 1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [1, 0, 1, 0, 1]) == 1
    assert candidate(nums = [1, 5, 0, 3, 5]) == 3
    assert candidate(nums = [0, 1, 0, 1, 0]) == 1
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4]) == 4
    assert candidate(nums = [100, 0, 50, 50]) == 2
    assert candidate(nums = [100, 0, 50, 50, 0]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50]) == 5
    assert candidate(nums = [5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [99, 99, 99, 99, 99]) == 1
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [1, 0, 1, 0, 1, 0]) == 1
    assert candidate(nums = [100, 100, 100, 100, 100]) == 1
    assert candidate(nums = [100, 0, 50, 25, 75]) == 4
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [2, 2, 2, 2]) == 1
    assert candidate(nums = [5, 5, 5, 0, 0, 5, 0]) == 1
    assert candidate(nums = [2, 2, 2, 2, 2]) == 1
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == 5
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]) == 10
    assert candidate(nums = [50, 25, 12, 6, 3, 1, 0, 0, 0, 0]) == 6
    assert candidate(nums = [42, 84, 126, 168, 210, 252, 294]) == 7
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [7, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0]) == 10
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 10
    assert candidate(nums = [5, 0, 3, 3, 5, 0, 2]) == 3
    assert candidate(nums = [10, 20, 30, 40, 50, 0, 10, 20, 30, 40, 50, 0]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 10
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == 9
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [5, 10, 15, 20, 25]) == 5
    assert candidate(nums = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5]) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 0, 0, 0, 0, 0]) == 5
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
    assert candidate(nums = [5, 3, 8, 6, 2, 0, 7]) == 6
    assert candidate(nums = [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
    assert candidate(nums = [5, 3, 2, 1, 4, 0, 2, 3]) == 5
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0]) == 10
    assert candidate(nums = [42, 0, 42, 0, 42, 0, 42, 0, 42, 0, 42, 0, 42, 0, 42, 0, 42, 0, 42, 0]) == 1
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93]) == 7
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == 5
    assert candidate(nums = [5, 3, 2, 1, 4, 3, 5, 0, 1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == 5
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 1
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 15
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 3
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == 10
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == 5
    assert candidate(nums = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 25
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 15
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 20
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 10
    assert candidate(nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0, 10, 20, 30, 40, 50, 60, 70, 80]) == 10
    assert candidate(nums = [50, 25, 75, 50, 25, 75, 50, 25, 75, 50, 25, 75, 50, 25, 75]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [0, 2, 3, 2, 1, 3, 4, 3, 2, 1]) == 4
    assert candidate(nums = [5, 1, 4, 2, 3, 1, 0, 2, 4, 3]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0]) == 9
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [7, 14, 21, 28, 35, 42]) == 6
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 0, 10, 20, 30]) == 5
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 0, 0, 0]) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 0, 0, 0, 0, 0]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 3
    assert candidate(nums = [1, 10, 100, 1000, 10000, 0, 0, 0, 0, 0]) == 5
    assert candidate(nums = [0, 23, 46, 69, 92, 115]) == 5
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 0, 10, 20, 30, 40]) == 5
