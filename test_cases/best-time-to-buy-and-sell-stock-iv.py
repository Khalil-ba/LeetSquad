# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(k = 2,prices = [10, 22, 5, 75, 65, 80]) == 87
    assert candidate(k = 5,prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(k = 2,prices = [2, 4, 1]) == 2
    assert candidate(k = 1,prices = [7, 1, 5, 3, 6, 4]) == 5
    assert candidate(k = 1,prices = [3, 3, 3, 3, 3]) == 0
    assert candidate(k = 1,prices = [7, 6, 4, 3, 1]) == 0
    assert candidate(k = 100,prices = [10, 22, 5, 75, 65, 80]) == 97
    assert candidate(k = 5,prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 15
    assert candidate(k = 1,prices = [1]) == 0
    assert candidate(k = 10,prices = [30, 80, 60, 90, 50, 120, 30, 10, 50, 60]) == 200
    assert candidate(k = 0,prices = [1, 2, 3, 4, 5]) == 0
    assert candidate(k = 2,prices = [3, 2, 6, 5, 0, 3]) == 7
    assert candidate(k = 3,prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 8
    assert candidate(k = 2,prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 9
    assert candidate(k = 0,prices = [7, 6, 4, 3, 1]) == 0
    assert candidate(k = 3,prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(k = 1,prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 4
    assert candidate(k = 4,prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 15
    assert candidate(k = 3,prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 15
    assert candidate(k = 10,prices = [8, 6, 4, 5, 3, 8, 9, 10, 11, 12, 13, 14, 15]) == 13
    assert candidate(k = 5,prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 24
    assert candidate(k = 5,prices = [7, 6, 4, 3, 1, 2, 3, 5, 6, 8, 10, 1, 2, 2, 4, 5, 7, 8, 8, 9, 10]) == 18
    assert candidate(k = 1,prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(k = 5,prices = [12, 14, 17, 10, 14, 13, 12, 15]) == 12
    assert candidate(k = 4,prices = [30, 80, 50, 90, 100, 150]) == 150
    assert candidate(k = 5,prices = [10, 22, 5, 75, 65, 80, 120, 130, 70, 50, 60, 100, 180]) == 277
    assert candidate(k = 50,prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 27
    assert candidate(k = 2,prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(k = 3,prices = [12, 14, 17, 10, 14, 13, 12, 15]) == 12
    assert candidate(k = 10,prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32
    assert candidate(k = 6,prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(k = 3,prices = [3, 3, 5, 0, 0, 3, 1, 4, 7, 8, 9, 10]) == 14
    assert candidate(k = 5,prices = [10, 22, 5, 75, 65, 80]) == 97
    assert candidate(k = 3,prices = [5, 2, 4, 0, 0, 3, 1, 4, 3, 6, 5, 0, 3, 8, 6, 8, 10, 1, 2, 3, 4, 5]) == 20
    assert candidate(k = 4,prices = [8, 5, 12, 19, 21, 10]) == 16
    assert candidate(k = 3,prices = [7, 6, 4, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(k = 3,prices = [1, 2, 2, 4, 5, 7, 8, 8, 9, 10]) == 9
    assert candidate(k = 5,prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(k = 3,prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(k = 5,prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 14
    assert candidate(k = 3,prices = [1, 3, 2, 8, 4, 9, 10, 11, 10, 9, 10, 11, 10, 9, 10, 11, 10, 9]) == 16
    assert candidate(k = 2,prices = [7, 6, 4, 3, 1]) == 0
    assert candidate(k = 10,prices = [2, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1]) == 5
    assert candidate(k = 4,prices = [10, 22, 5, 75, 65, 80]) == 97
    assert candidate(k = 5,prices = [31, 31, 27, 39, 59, 91, 92, 58, 84, 100]) == 107
    assert candidate(k = 3,prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(k = 1,prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(k = 10,prices = [8, 9, 8, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9, 10, 9]) == 8
    assert candidate(k = 4,prices = [1, 2, 2, 4, 5, 7, 8, 8, 9, 10, 1, 2, 2, 4, 5, 7, 8, 8, 9, 10]) == 18
    assert candidate(k = 5,prices = [30, 10, 20, 40, 50, 15, 35, 60, 70, 25, 45, 80, 90]) == 160
    assert candidate(k = 5,prices = [10, 22, 5, 75, 65, 80, 90, 100, 110, 120, 130, 140, 150]) == 167
    assert candidate(k = 2,prices = [3, 3, 5, 0, 0, 3, 1, 4, 7, 11, 10, 13, 12, 9, 15, 18, 17, 20, 22, 21]) == 26
    assert candidate(k = 3,prices = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 0
    assert candidate(k = 4,prices = [7, 6, 4, 3, 1, 2, 5, 6, 4, 3, 1, 2]) == 6
    assert candidate(k = 4,prices = [30, 25, 20, 15, 10, 5]) == 0
    assert candidate(k = 2,prices = [3, 2, 1, 4, 3, 5, 3, 6, 4, 7, 8, 10, 6, 12, 14, 8, 15, 16, 18, 20]) == 25
    assert candidate(k = 6,prices = [8, 1, 9, 5, 7, 4, 3, 6, 0, 9, 2, 6, 10, 14]) == 34
    assert candidate(k = 4,prices = [10, 1, 1, 10, 3, 5, 10, 9, 1, 3, 5, 6, 8, 9, 0, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 34
    assert candidate(k = 4,prices = [3, 5, 0, 0, 3, 1, 4, 7, 9, 8, 5, 3, 2, 10, 12, 14, 16, 18, 20, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 31
    assert candidate(k = 4,prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2]) == 16
    assert candidate(k = 5,prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(k = 4,prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(k = 20,prices = [5, 2, 8, 3, 10, 4, 12, 5, 14, 6, 16, 7, 18, 8, 20, 9, 22, 10, 24, 11]) == 90
    assert candidate(k = 5,prices = [1, 3, 2, 8, 4, 9, 5, 11, 6, 10, 7, 12, 8, 13, 9, 14, 10, 15, 11, 16]) == 32
    assert candidate(k = 2,prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(k = 2,prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(k = 1,prices = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 0
    assert candidate(k = 4,prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 22
    assert candidate(k = 1,prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(k = 3,prices = [7, 6, 4, 3, 1]) == 0
    assert candidate(k = 10,prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(k = 2,prices = [3, 2, 6, 5, 0, 3, 1, 4, 7, 8, 5]) == 12
    assert candidate(k = 2,prices = [1, 3, 2, 8, 4, 9]) == 12
    assert candidate(k = 1,prices = [100, 180, 260, 310, 40, 535, 695]) == 655
    assert candidate(k = 5,prices = [3, 3, 5, 0, 0, 3, 1, 4, 7, 9, 8, 5, 3, 2, 10]) == 21
    assert candidate(k = 2,prices = [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 9, 7, 10, 11, 12, 10, 13, 14, 15, 13, 16, 17, 18, 16, 19, 20, 21, 19]) == 22
    assert candidate(k = 10,prices = [100, 300, 200, 400, 500, 800, 300, 600, 500, 700]) == 1300
    assert candidate(k = 2,prices = [100, 180, 260, 310, 40, 535, 695]) == 865
    assert candidate(k = 3,prices = [3, 3, 5, 0, 0, 3, 1, 4, 7, 8, 2]) == 12
    assert candidate(k = 2,prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9, 1, 2, 3, 5]) == 17
    assert candidate(k = 3,prices = [8, 3, 6, 2, 8, 8, 8, 4, 2, 0, 1, 2, 5, 1, 0, 3, 6, 1, 1, 9]) == 20
    assert candidate(k = 4,prices = [3, 3, 5, 0, 0, 3, 1, 4, 7, 8, 5]) == 12
    assert candidate(k = 3,prices = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 4
    assert candidate(k = 100,prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 52
    assert candidate(k = 2,prices = [5, 4, 3, 2, 1]) == 0
    assert candidate(k = 100,prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(k = 3,prices = [5, 2, 3, 0, 3, 5, 6, 8, 1, 9]) == 17
    assert candidate(k = 3,prices = [1, 3, 2, 8, 4, 9, 5, 10, 11, 15, 13, 14, 16, 17]) == 24
    assert candidate(k = 5,prices = [50, 30, 20, 40, 90, 100, 40, 80, 60, 50, 70, 120, 150, 130, 170]) == 260
    assert candidate(k = 3,prices = [10, 22, 5, 75, 65, 80]) == 97
    assert candidate(k = 4,prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 24
    assert candidate(k = 3,prices = [3, 3, 5, 0, 0, 3, 1, 4, 7, 11, 10, 13, 12, 9]) == 17
    assert candidate(k = 1,prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 8
    assert candidate(k = 100,prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 68
    assert candidate(k = 7,prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(k = 10,prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(k = 5,prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
