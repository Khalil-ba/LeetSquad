# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(maxHeights = [1, 2, 3, 4, 5]) == 15
    assert candidate(maxHeights = [5, 4, 3, 2, 1]) == 15
    assert candidate(maxHeights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
    assert candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5]) == 30
    assert candidate(maxHeights = [10, 10, 10, 10, 10]) == 50
    assert candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(maxHeights = [1, 3, 2, 3, 1]) == 9
    assert candidate(maxHeights = [1, 3, 2, 1, 2, 3, 1, 2, 1]) == 12
    assert candidate(maxHeights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
    assert candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(maxHeights = [3, 2, 5, 5, 2, 3]) == 18
    assert candidate(maxHeights = [7, 8, 9, 10, 9, 8, 7]) == 58
    assert candidate(maxHeights = [5, 3, 4, 1, 1]) == 13
    assert candidate(maxHeights = [4, 4, 4, 4, 4, 4, 4]) == 28
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(maxHeights = [1, 1, 1, 1, 1]) == 5
    assert candidate(maxHeights = [6, 5, 3, 9, 2, 7]) == 22
    assert candidate(maxHeights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]) == 66
    assert candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 114
    assert candidate(maxHeights = [5, 5, 5, 5, 9, 5, 5, 5, 5]) == 49
    assert candidate(maxHeights = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 70
    assert candidate(maxHeights = [1, 10, 2, 8, 3, 7, 4, 6, 5]) == 30
    assert candidate(maxHeights = [3, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 6, 6]) == 54
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 120
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 20
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 34
    assert candidate(maxHeights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 40
    assert candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == 36
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3]) == 44
    assert candidate(maxHeights = [5, 6, 7, 8, 9, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4]) == 114
    assert candidate(maxHeights = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 26
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 4, 5, 4, 3]) == 46
    assert candidate(maxHeights = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 111
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 118
    assert candidate(maxHeights = [1, 3, 2, 5, 4, 6, 5, 7, 6, 8]) == 43
    assert candidate(maxHeights = [3, 3, 3, 3, 3, 5, 5, 5, 5, 5]) == 40
    assert candidate(maxHeights = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 500
    assert candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 44
    assert candidate(maxHeights = [7, 7, 7, 7, 1, 7, 7, 7, 7, 7]) == 40
    assert candidate(maxHeights = [5, 4, 4, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7]) == 85
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
    assert candidate(maxHeights = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1]) == 39
    assert candidate(maxHeights = [1, 5, 3, 7, 5, 9, 7, 11, 9, 13, 11, 9, 7, 5, 3, 1]) == 98
    assert candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 60
    assert candidate(maxHeights = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10]) == 300
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 120
    assert candidate(maxHeights = [3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3, 3, 3]) == 68
    assert candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6]) == 25
    assert candidate(maxHeights = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 45
    assert candidate(maxHeights = [2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 2, 2]) == 73
    assert candidate(maxHeights = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 19
    assert candidate(maxHeights = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
    assert candidate(maxHeights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 26
    assert candidate(maxHeights = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == 250
    assert candidate(maxHeights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 65
    assert candidate(maxHeights = [1, 3, 5, 7, 9, 11, 9, 7, 5, 3, 1, 3, 5, 7, 9, 11, 9, 7, 5]) == 69
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 3, 2, 1]) == 41
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == 35
    assert candidate(maxHeights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]) == 42
    assert candidate(maxHeights = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(maxHeights = [5, 5, 5, 5, 6, 5, 5, 5, 5]) == 46
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]) == 29
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(maxHeights = [5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 51
    assert candidate(maxHeights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 19
    assert candidate(maxHeights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 110
    assert candidate(maxHeights = [1, 1, 1, 10, 1, 1, 10, 1, 1, 10, 1, 1, 1]) == 22
    assert candidate(maxHeights = [1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]) == 29
    assert candidate(maxHeights = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]) == 360
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1]) == 104
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]) == 70
    assert candidate(maxHeights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7]) == 68
    assert candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == 19
    assert candidate(maxHeights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 210
    assert candidate(maxHeights = [5, 5, 5, 5, 1, 5, 5, 5, 5]) == 25
    assert candidate(maxHeights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000
    assert candidate(maxHeights = [5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5, 10, 5, 5, 5, 5, 5]) == 90
    assert candidate(maxHeights = [3, 1, 3, 1, 3, 1, 3]) == 9
    assert candidate(maxHeights = [1, 5, 3, 8, 7, 2, 6, 4, 9, 0]) == 30
    assert candidate(maxHeights = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 85
    assert candidate(maxHeights = [3, 3, 3, 3, 10, 3, 3, 3, 3, 10, 3, 3, 3, 3]) == 49
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1]) == 65
    assert candidate(maxHeights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 650
    assert candidate(maxHeights = [1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 20
    assert candidate(maxHeights = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 20
    assert candidate(maxHeights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 150
    assert candidate(maxHeights = [1, 3, 2, 3, 4, 3, 2, 3, 1]) == 20
    assert candidate(maxHeights = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 113
    assert candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
    assert candidate(maxHeights = [2, 2, 3, 4, 5, 6, 5, 5, 5, 5, 6, 7, 8, 9, 10]) == 81
    assert candidate(maxHeights = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 101
    assert candidate(maxHeights = [9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7]) == 111
    assert candidate(maxHeights = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 103
    assert candidate(maxHeights = [9, 9, 9, 9, 9, 1, 1, 1, 1, 1]) == 50
    assert candidate(maxHeights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(maxHeights = [100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100]) == 700
    assert candidate(maxHeights = [9, 7, 5, 3, 1, 1, 3, 5, 7, 9]) == 30
    assert candidate(maxHeights = [1, 3, 5, 7, 9, 7, 5, 3, 1]) == 41
    assert candidate(maxHeights = [1, 3, 5, 7, 9, 7, 5, 3, 1, 1, 3, 5, 7, 9, 7, 5, 3, 1]) == 50
    assert candidate(maxHeights = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1]) == 27
    assert candidate(maxHeights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 53
    assert candidate(maxHeights = [100, 50, 50, 100, 50, 50, 100, 50, 50, 100]) == 550
    assert candidate(maxHeights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 64
    assert candidate(maxHeights = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 19
    assert candidate(maxHeights = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 1000000008
    assert candidate(maxHeights = [1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1]) == 28
