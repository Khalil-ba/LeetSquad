# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 1, 3, 1, 4, 1, 3, 1]) == 5
    assert candidate(nums = [100000000, 1, 100000000, 2, 100000000]) == 100000003
    assert candidate(nums = [5, 4, 8, 7, 10, 2]) == 13
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 3, 1, 4, 1, 5, 1, 6, 1]) == 5
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 6
    assert candidate(nums = [1, 100000000, 2, 99999999, 3, 99999998]) == 100000003
    assert candidate(nums = [1, 3, 1, 3, 1]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5]) == -1
    assert candidate(nums = [10, 20, 30, 15, 25, 35, 40, 10]) == 35
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == -1
    assert candidate(nums = [6, 5, 4, 3, 4, 5]) == -1
    assert candidate(nums = [5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3]) == -1
    assert candidate(nums = [1, 5, 3, 7, 6, 8]) == 9
    assert candidate(nums = [8, 6, 1, 5, 3]) == 9
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 4
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
    assert candidate(nums = [8, 1, 2, 3, 4, 5, 6, 7, 8]) == -1
    assert candidate(nums = [2, 1, 2, 3, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8]) == 6
    assert candidate(nums = [5, 1, 3, 7, 2, 6, 4, 8, 9]) == 6
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 31
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 103
    assert candidate(nums = [15, 10, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == -1
    assert candidate(nums = [5, 10, 15, 10, 5, 20, 25, 20, 15, 10, 5]) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 11, 12, 13, 14, 15]) == -1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0]) == 1
    assert candidate(nums = [8, 6, 1, 5, 3, 7, 2, 4, 9, 10, 11]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [7, 7, 7, 8, 7, 7, 7]) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == -1
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == -1
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 102
    assert candidate(nums = [5, 1, 4, 2, 7, 3, 6, 8, 0, 9]) == 3
    assert candidate(nums = [3, 5, 1, 8, 4, 7, 6, 9, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 7
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 7
    assert candidate(nums = [5, 1, 4, 3, 7, 6, 8]) == 8
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == -1
    assert candidate(nums = [7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5]) == 20
    assert candidate(nums = [8, 1, 5, 6, 3, 2, 4, 7]) == 6
    assert candidate(nums = [8, 1, 5, 3, 7, 2, 6, 4, 9]) == 6
    assert candidate(nums = [8, 6, 1, 5, 3, 7, 2, 10, 4, 9, 11, 13, 12]) == 6
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 5, 1, 4, 1, 3, 1, 2, 1]) == 4
    assert candidate(nums = [100, 101, 99, 102, 98, 103, 97, 104, 96]) == 297
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 103
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15]) == 7
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 21]) == -1
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5]) == 103
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7]) == 3
    assert candidate(nums = [1, 2, 100, 2, 100, 2, 100, 2, 100, 2, 100, 2, 100, 2, 100, 2, 100, 2, 100]) == 103
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10]) == 22
    assert candidate(nums = [10, 20, 30, 40, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]) == 25
    assert candidate(nums = [5, 1, 3, 2, 4, 6, 7, 8, 9, 10, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == 4
    assert candidate(nums = [9, 8, 7, 6, 5, 10, 15, 20, 25, 1, 2, 3, 4, 5]) == 16
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 6
    assert candidate(nums = [100, 200, 150, 250, 100, 300, 50, 400, 250, 500, 200, 450, 300, 550, 600, 525, 475, 650, 700, 625]) == 300
    assert candidate(nums = [5, 1, 3, 7, 2, 6, 4, 8]) == 6
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 13
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9]) == 10
    assert candidate(nums = [10, 20, 10, 30, 5, 40, 25, 50, 15]) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 2, 2, 1, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(nums = [10, 20, 5, 15, 10, 25, 5]) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]) == -1
    assert candidate(nums = [1, 5, 3, 7, 2, 6, 4, 8]) == 6
    assert candidate(nums = [7, 1, 3, 5, 9, 6, 8, 2, 4]) == 6
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 500, 400, 300, 200, 100]) == 400
    assert candidate(nums = [100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 100000000, 1]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert candidate(nums = [2, 3, 1, 4, 6, 5, 8, 7, 9, 10, 11, 12]) == 6
    assert candidate(nums = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13]) == 12
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15]) == 13
    assert candidate(nums = [10, 20, 15, 25, 10, 30, 5, 40, 25, 50]) == 30
    assert candidate(nums = [2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1]) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == -1
    assert candidate(nums = [5, 4, 3, 2, 1, 11, 12, 13, 14, 15]) == -1
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [7, 1, 5, 3, 6, 4, 2, 8, 10, 1, 12]) == 4
