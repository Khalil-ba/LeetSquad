# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 1, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(nums = [1, 3, 5, 7, 9]) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(nums = [1, 0, 0, 8, 6]) == 14
    assert candidate(nums = [1, 2, 3, 4, 5]) == 6
    assert candidate(nums = [-1, 1, 1, 0, -1, -1]) == 5
    assert candidate(nums = [1, 10, 2, 9]) == 16
    assert candidate(nums = [1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500]) == 600
    assert candidate(nums = [-10, -20, -30, -40, -50]) == 60
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 8
    assert candidate(nums = [10, 5, 15, 20, 0]) == 30
    assert candidate(nums = [1000000000, -1000000000, 0]) == 2000000000
    assert candidate(nums = [1000000000, -1000000000, 0]) == 2000000000
    assert candidate(nums = [1, 2, 3]) == 2
    assert candidate(nums = [1, 2, 9, 10]) == 16
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [-1, 1, 0]) == 2
    assert candidate(nums = [-1, 0, 1]) == 2
    assert candidate(nums = [100, 100, 100]) == 0
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 30
    assert candidate(nums = [10, 1, 2, 7, 5]) == 14
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 10000
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 250
    assert candidate(nums = [100, 200, 300, 400, 500]) == 600
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 200]) == 190
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 225
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000]) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7]) == 19
    assert candidate(nums = [-10, -20, -30, -40, -50]) == 60
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 31
    assert candidate(nums = [1, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 1110988899
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 110
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 50
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 50
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 60
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == 999999999
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 25
    assert candidate(nums = [1000000000, -1000000000, 0, 500000000, -500000000]) == 3000000000
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 10
    assert candidate(nums = [-1000000000, -2000000000, -3000000000, -4000000000, -5000000000, -6000000000, -7000000000, -8000000000, -9000000000, -10000000000]) == 25000000000
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5]) == 3999999984
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(nums = [-100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 3000
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000]) == 3000000000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 250
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [-5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 112
    assert candidate(nums = [1, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 219
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 450
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 156
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) == 7
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 30
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 9, 10, 11, 20]) == 29
    assert candidate(nums = [-5, -4, -3, -2, -1, 0]) == 9
    assert candidate(nums = [1000000000, -1000000000, 2000000000, -2000000000]) == 6000000000
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 10000000000]) == 25000000000
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7]) == 34
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 300
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 560
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 25
    assert candidate(nums = [10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12]) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11]) == 18
    assert candidate(nums = [100, 101, 102, 103, 104]) == 6
