# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 5,batteries = [1, 2, 3, 4, 5]) == 1
    assert candidate(n = 4,batteries = [10, 10, 3, 5]) == 3
    assert candidate(n = 2,batteries = [1000000000, 1000000000]) == 1000000000
    assert candidate(n = 2,batteries = [9, 4, 10]) == 11
    assert candidate(n = 3,batteries = [10, 20, 30, 40]) == 30
    assert candidate(n = 3,batteries = [5, 8, 5]) == 5
    assert candidate(n = 10,batteries = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000000
    assert candidate(n = 5,batteries = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 18
    assert candidate(n = 4,batteries = [1, 2, 3, 4, 5]) == 3
    assert candidate(n = 2,batteries = [1, 1, 1, 1]) == 2
    assert candidate(n = 2,batteries = [3, 3, 3]) == 4
    assert candidate(n = 1,batteries = [5]) == 5
    assert candidate(n = 1,batteries = [100]) == 100
    assert candidate(n = 1,batteries = [10]) == 10
    assert candidate(n = 5,batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(n = 10,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(n = 3,batteries = [10, 10, 3, 5]) == 8
    assert candidate(n = 3,batteries = [1, 2, 3, 4, 5, 6]) == 7
    assert candidate(n = 3,batteries = [10, 10, 10]) == 10
    assert candidate(n = 5,batteries = [1, 1, 1, 1, 1000000000]) == 1
    assert candidate(n = 3,batteries = [2, 6, 4, 5]) == 5
    assert candidate(n = 4,batteries = [5, 5, 5, 5, 5]) == 6
    assert candidate(n = 5,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert candidate(n = 3,batteries = [1, 2, 999999999]) == 1
    assert candidate(n = 2,batteries = [10, 20]) == 10
    assert candidate(n = 2,batteries = [2, 3, 4, 5]) == 7
    assert candidate(n = 3,batteries = [5, 5, 5, 5, 5]) == 8
    assert candidate(n = 4,batteries = [8, 8, 8, 8, 8, 8]) == 12
    assert candidate(n = 10,batteries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 110
    assert candidate(n = 5,batteries = [500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 350
    assert candidate(n = 10,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 11
    assert candidate(n = 4,batteries = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 2500000000
    assert candidate(n = 5,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert candidate(n = 15,batteries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000]) == 3100
    assert candidate(n = 5,batteries = [10, 20, 30, 40, 50, 60]) == 30
    assert candidate(n = 5,batteries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 420
    assert candidate(n = 4,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 13
    assert candidate(n = 10,batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == 1
    assert candidate(n = 4,batteries = [100, 100, 100, 1]) == 1
    assert candidate(n = 5,batteries = [1000000, 2000000, 3000000, 4000000, 5000000]) == 1000000
    assert candidate(n = 3,batteries = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 70
    assert candidate(n = 3,batteries = [1000000000, 1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 13
    assert candidate(n = 15,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 100]) == 3
    assert candidate(n = 2,batteries = [1, 1000000000]) == 1
    assert candidate(n = 5,batteries = [10, 20, 30, 40, 50]) == 10
    assert candidate(n = 10,batteries = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(n = 10,batteries = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 1]) == 50
    assert candidate(n = 3,batteries = [1000000000, 1000000000, 1000000000, 1]) == 1000000000
    assert candidate(n = 6,batteries = [100, 100, 100, 100, 100, 100, 1]) == 100
    assert candidate(n = 7,batteries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 1714
    assert candidate(n = 4,batteries = [100, 100, 100, 100, 1, 1, 1, 1]) == 101
    assert candidate(n = 5,batteries = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 18
    assert candidate(n = 5,batteries = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 18
    assert candidate(n = 1,batteries = [1000000000]) == 1000000000
    assert candidate(n = 4,batteries = [2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == 16
    assert candidate(n = 2,batteries = [1000000000, 1]) == 1
    assert candidate(n = 4,batteries = [1, 1, 1, 1, 1000000000, 1000000000, 1000000000, 1000000000]) == 1000000001
    assert candidate(n = 4,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 52
    assert candidate(n = 8,batteries = [8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(n = 7,batteries = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 46
    assert candidate(n = 7,batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(n = 5,batteries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 110
    assert candidate(n = 10,batteries = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(n = 5,batteries = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 2000
    assert candidate(n = 10,batteries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 500
    assert candidate(n = 3,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 108
    assert candidate(n = 6,batteries = [100, 100, 100, 100, 100, 100, 1, 1, 1, 1]) == 100
    assert candidate(n = 8,batteries = [8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 24
    assert candidate(n = 5,batteries = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999]) == 1999999998
    assert candidate(n = 4,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 13
    assert candidate(n = 5,batteries = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == 125
    assert candidate(n = 3,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(n = 15,batteries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 110
    assert candidate(n = 6,batteries = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]) == 30
    assert candidate(n = 8,batteries = [50, 40, 30, 20, 10, 5, 3, 1, 2, 4, 6, 8, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 75
    assert candidate(n = 5,batteries = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == 200
    assert candidate(n = 8,batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(n = 4,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 116
    assert candidate(n = 9,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 23
    assert candidate(n = 3,batteries = [1, 1000000000, 1]) == 1
    assert candidate(n = 3,batteries = [1000, 1000, 1000, 1, 1, 1, 1, 1, 1, 1]) == 1002
    assert candidate(n = 7,batteries = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 85
    assert candidate(n = 2,batteries = [1000000000, 1000000000]) == 1000000000
    assert candidate(n = 5,batteries = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 250
    assert candidate(n = 3,batteries = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 1333333333
    assert candidate(n = 5,batteries = [1, 1, 1, 1, 1, 1000]) == 1
    assert candidate(n = 7,batteries = [50, 40, 30, 20, 10, 5, 1, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(n = 8,batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(n = 5,batteries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1100
    assert candidate(n = 2,batteries = [1000000000, 1000000000, 1000000000, 1000000000]) == 2000000000
    assert candidate(n = 3,batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(n = 7,batteries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 70
    assert candidate(n = 4,batteries = [100, 100, 100, 100, 1]) == 100
    assert candidate(n = 6,batteries = [100, 100, 100, 100, 100, 100, 1, 1, 1, 1, 1, 1]) == 101
    assert candidate(n = 10,batteries = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == 999999991
    assert candidate(n = 3,batteries = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 30
    assert candidate(n = 10,batteries = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10
    assert candidate(n = 4,batteries = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 1000000000
    assert candidate(n = 5,batteries = [10, 20, 30, 40, 50, 60]) == 30
    assert candidate(n = 6,batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(n = 3,batteries = [10, 20, 30, 40, 50]) == 50
    assert candidate(n = 10,batteries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 100
    assert candidate(n = 7,batteries = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 14
    assert candidate(n = 6,batteries = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 90
    assert candidate(n = 7,batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(n = 4,batteries = [10, 20, 30, 40, 50]) == 30
    assert candidate(n = 2,batteries = [999999999, 1]) == 1
    assert candidate(n = 6,batteries = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == 57
    assert candidate(n = 7,batteries = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 28
    assert candidate(n = 6,batteries = [1000, 2000, 3000, 4000, 5000, 6000]) == 1000
    assert candidate(n = 10,batteries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 1100
    assert candidate(n = 3,batteries = [1000000000, 1000000000, 1000000000, 1000000000]) == 1333333333
    assert candidate(n = 5,batteries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1100
    assert candidate(n = 20,batteries = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
