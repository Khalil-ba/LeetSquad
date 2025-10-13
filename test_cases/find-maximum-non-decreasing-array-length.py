# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]) == 10
    assert candidate(nums = [1, 100, 1000]) == 3
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [3, 3, 3, 3]) == 4
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8]) == 4
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, 2, 3, 4]) == 4
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 7
    assert candidate(nums = [1, 2, 4, 3, 5]) == 4
    assert candidate(nums = [4, 3, 2, 6]) == 3
    assert candidate(nums = [100, 10, 1]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
    assert candidate(nums = [7, 7, 7, 7, 7]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [9, 4, 3, 2, 1]) == 2
    assert candidate(nums = [1, 1, 1, 1, 1]) == 5
    assert candidate(nums = [10, 5, 7, 10]) == 2
    assert candidate(nums = [10, 5, 7, 10, 6]) == 3
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000]) == 5
    assert candidate(nums = [1, 100, 2, 101, 1]) == 3
    assert candidate(nums = [5, 2, 2]) == 1
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000]) == 2
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 4
    assert candidate(nums = [3, 5, 2, 5, 6]) == 3
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996]) == 2
    assert candidate(nums = [5, 6, 2, 8, 3, 9, 1, 10, 4, 11]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [1, 10, 1, 10, 1, 10]) == 4
    assert candidate(nums = [2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 19
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9, 10]) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 500, 600, 700, 800, 900]) == 12
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 4
    assert candidate(nums = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 12
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 11
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 12
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93]) == 9
    assert candidate(nums = [10, 20, 15, 25, 30, 35, 40, 45, 50]) == 5
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 40, 45]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 12
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 12
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10]) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 13
    assert candidate(nums = [100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1]) == 4
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 6
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 10
    assert candidate(nums = [3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 10
    assert candidate(nums = [100, 200, 100, 300, 200, 400, 300, 500]) == 5
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15]) == 20
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 6
    assert candidate(nums = [10, 5, 3, 8, 12, 7, 9, 11]) == 4
    assert candidate(nums = [1, 3, 5, 4, 6, 7, 5, 8, 9, 10, 11, 9, 12, 13, 14]) == 9
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 3
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 8
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 3
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 6
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 6
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 6, 7, 8, 9]) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 20
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 5
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6]) == 5
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]) == 13
    assert candidate(nums = [1, 100, 2, 101, 3, 102, 4, 103, 5, 104]) == 6
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 6
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [1, 10, 100, 1000, 10000, 1, 10, 100, 1000, 10000]) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 3
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 5]) == 6
    assert candidate(nums = [5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 10
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 4
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 13
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 10
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == 8
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 11
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == 7
    assert candidate(nums = [100, 200, 150, 250, 300, 100, 400, 500, 350, 450]) == 7
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 11
    assert candidate(nums = [10, 5, 3, 7, 8, 12, 1]) == 3
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 8, 5, 9, 10]) == 7
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [10, 5, 1, 1, 1, 15, 20, 25, 30]) == 5
    assert candidate(nums = [10, 20, 30, 25, 35, 40, 45, 50]) == 5
    assert candidate(nums = [5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 7
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9]) == 5
