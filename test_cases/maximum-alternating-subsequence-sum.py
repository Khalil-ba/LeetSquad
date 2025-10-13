# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996]) == 100000
    assert candidate(nums = [4, 2, 5, 3]) == 7
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [6, 2, 1, 2, 4, 5]) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [100]) == 100
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50]) == 50
    assert candidate(nums = [1, 100000, 1, 100000, 1]) == 199999
    assert candidate(nums = [5, 6, 7, 8]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [100000, 1, 100000, 1, 100000]) == 299998
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 54
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1]) == 5
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 100000
    assert candidate(nums = [100, 0, 100, 0, 100]) == 300
    assert candidate(nums = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 499996
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 991
    assert candidate(nums = [100, 50, 100, 50, 100, 50, 100]) == 250
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 24
    assert candidate(nums = [100, 10, 200, 20, 300, 30, 400, 40, 500, 50]) == 1400
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 499976
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]) == 106
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]) == 10
    assert candidate(nums = [100000, 50000, 100000, 50000, 100000, 50000, 100000, 50000, 100000, 50000]) == 300000
    assert candidate(nums = [5, 3, 8, 1, 4, 7, 2, 6, 9]) == 23
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1000
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 70]) == 110
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 6
    assert candidate(nums = [9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9]) == 65
    assert candidate(nums = [120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 120
    assert candidate(nums = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 499996
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 9
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(nums = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == 30
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991]) == 100000
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 19
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 11
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == 15
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 7
    assert candidate(nums = [5, 3, 8, 12, 4, 9, 2, 7, 6, 10]) == 28
    assert candidate(nums = [10, 15, 10, 5, 20, 25, 30, 35, 40, 45]) == 55
    assert candidate(nums = [100000, 99999, 100000, 99998, 100000, 99997, 100000, 99996, 100000, 99995]) == 100010
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]) == 15
    assert candidate(nums = [5, 3, 8, 6, 7, 2, 9, 4, 1, 10]) == 27
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 140
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 11
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60, 50]) == 100
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 29
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 28
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 17
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 17
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 0, 9, 1, 8, 2, 7, 3, 6, 4, 5, 0]) == 50
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [9, 7, 8, 5, 6, 3, 4, 1, 2, 10]) == 21
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 20
    assert candidate(nums = [5, 3, 8, 6, 11, 9, 14, 12, 17, 15, 20, 18, 23, 21, 25]) == 39
    assert candidate(nums = [5, 3, 6, 7, 2, 9, 4, 10, 1, 11]) == 32
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 11
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == 13
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 20
    assert candidate(nums = [75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 75
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 21
    assert candidate(nums = [5, 1, 4, 2, 7, 3, 6, 8]) == 18
    assert candidate(nums = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == 46
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 13
    assert candidate(nums = [99999, 1, 99998, 2, 99997, 3, 99996, 4]) == 399984
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 120
    assert candidate(nums = [10, 5, 15, 10, 20, 15, 25, 20, 30, 25]) == 50
    assert candidate(nums = [5, 1, 4, 2, 3]) == 9
    assert candidate(nums = [8, 6, 7, 5, 3, 0, 9, 1, 4, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 38
    assert candidate(nums = [5, 1, 4, 2, 3, 1, 2, 1, 3, 2, 1]) == 12
    assert candidate(nums = [5, 3, 8, 12, 7, 10, 1, 15, 9, 20]) == 42
    assert candidate(nums = [100000, 1, 100000, 2, 100000, 3, 100000, 4, 100000, 5]) == 499990
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 110
    assert candidate(nums = [100, 200, 150, 300, 250, 350, 400, 300, 450, 500]) == 700
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 3, 7, 2, 8, 1, 9]) == 45
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 150
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 476
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 10000, 1000, 100, 10]) == 100000
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 75
    assert candidate(nums = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 150
