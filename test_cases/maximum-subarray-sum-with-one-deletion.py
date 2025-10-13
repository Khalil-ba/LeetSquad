# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [-1, 0, -2, 3, 4, -5, 3]) == 10
    assert candidate(arr = [5, -1, 5, -1, 5]) == 14
    assert candidate(arr = [2, 3, -2, 5, -3]) == 10
    assert candidate(arr = [-10000]) == -10000
    assert candidate(arr = [5, -3, -2, 7, 1]) == 11
    assert candidate(arr = [2, 1, -2, -5, -2]) == 3
    assert candidate(arr = [5, 5, 5, 5, 5]) == 25
    assert candidate(arr = [1, -2, 0, 3]) == 4
    assert candidate(arr = [10000, -5000, 3000, -2000, 1000]) == 13000
    assert candidate(arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 10
    assert candidate(arr = [-1, -1, -1, -1]) == -1
    assert candidate(arr = [100, -1, 50, -100, 200]) == 349
    assert candidate(arr = [-10000, 5000, -3000, 2000, -1000]) == 7000
    assert candidate(arr = [1]) == 1
    assert candidate(arr = [-1, 0, -2, 3, 4, -5, 1]) == 8
    assert candidate(arr = [10000, -5000, 5000, -10000, 10000]) == 20000
    assert candidate(arr = [5, -1, 5, -2, 3, -3, 7]) == 17
    assert candidate(arr = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 2
    assert candidate(arr = [1, 2, 3, 4, 5]) == 15
    assert candidate(arr = [-1, 0, 1, -2, 2]) == 3
    assert candidate(arr = [0, 0, 0, 0, 0]) == 0
    assert candidate(arr = [-10000, 10000]) == 10000
    assert candidate(arr = [-10000, 10000, -10000, 10000]) == 20000
    assert candidate(arr = [5, -1, 5]) == 10
    assert candidate(arr = [1, -2, -2, 3]) == 3
    assert candidate(arr = [-5, -4, -3, -2, -1]) == -1
    assert candidate(arr = [-2, -3, 4, -1, -2, 1, 5, -3]) == 9
    assert candidate(arr = [0, 0, 0, 0, 0]) == 0
    assert candidate(arr = [-2, -3, -1, -5]) == -1
    assert candidate(arr = [100, -50, 50, -25, 25, -75, 75, -100, 100]) == 200
    assert candidate(arr = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == 28
    assert candidate(arr = [1, 2, 3, 4, -10, 5, 6, 7]) == 28
    assert candidate(arr = [-1, -2, -3, -4, 5, 4, 3, 2, 1, -5, -1, -1, -1, 10]) == 22
    assert candidate(arr = [1, -3, 2, 1, -1, 3, -2, 3, 4, -5]) == 12
    assert candidate(arr = [10, -3, 4, -2, -1, 10, -5, 20, -15]) == 38
    assert candidate(arr = [100, -1, 200, -2, 300, -3, 400, -4, 500, -5]) == 1494
    assert candidate(arr = [-1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1]) == 4
    assert candidate(arr = [-10, 1, 2, 3, -4, 5, 6, -7, 8, 9, -10, 11, 12, -13]) == 46
    assert candidate(arr = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8]) == 15
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, -9, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 18
    assert candidate(arr = [10, 20, 30, -5, -10, -15, -20, 50, 60, 70]) == 210
    assert candidate(arr = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 9
    assert candidate(arr = [100, -50, 50, -100, 200, -300, 400, -500, 600]) == 1000
    assert candidate(arr = [3, -2, 5, -1, 4, -3, 2, -2]) == 11
    assert candidate(arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 15
    assert candidate(arr = [-1, -2, -3, -4, 5, 6, 7, -8, 9, -10, 11]) == 30
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -50]) == 28
    assert candidate(arr = [1, 2, 3, -6, 4, 5, -3, 2]) == 15
    assert candidate(arr = [5, -3, 8, -1, 6, -4, 9, -2, 7, -5, 10]) == 35
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -100, 11, 12, 13, 14, 15]) == 120
    assert candidate(arr = [1, 2, -5, 1, 2, -1, 5, -1, -2, 3, 4, -2, 3, 4]) == 19
    assert candidate(arr = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11]) == 20
    assert candidate(arr = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5]) == 9
    assert candidate(arr = [-10, 100, -50, 50, -25, 25, -75, 75]) == 175
    assert candidate(arr = [1, -2, 3, -4, 5, -6, 7, -8, 9]) == 16
    assert candidate(arr = [10, -3, 4, -2, -1, 10, -5, 1, 2, -1]) == 21
    assert candidate(arr = [10, 20, 30, 40, 50, -100, 10, 20, 30, 40, 50, -100, 10, 20, 30, 40, 50]) == 350
    assert candidate(arr = [-10, -20, 30, -40, 50, -60, 70, -80, 90]) == 160
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == 1
    assert candidate(arr = [1, -4, 2, -3, 5, -6, 7]) == 12
    assert candidate(arr = [10, -5, -7, 3, 15, -10, 6, -4, 5]) == 25
    assert candidate(arr = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 36
    assert candidate(arr = [-10, -20, -30, 15, 25, 35, -45, 55, 65, 75]) == 270
    assert candidate(arr = [10, -1, 20, -2, 30, -3, 40, -4, 50, -5, 60, -6, 70, -7]) == 265
    assert candidate(arr = [100, 200, 300, -500, 100, 200, 300, -500, 100, 200, 300]) == 1300
    assert candidate(arr = [1, 2, 3, -6, 1, 2, 3, -6, 1, 2, 3, -6, 1, 2, 3]) == 12
    assert candidate(arr = [0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 18
    assert candidate(arr = [1, -1, 2, -2, 3, -3, 4, -4]) == 7
    assert candidate(arr = [20, -10, -5, -1, 5, 10, -15, 5, 10, -10, -5, 5]) == 34
    assert candidate(arr = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100, -110, 120]) == 220
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]) == -1
    assert candidate(arr = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 2
    assert candidate(arr = [-1, -1, -1, -1, 5, -1, -1, -1, -1]) == 5
    assert candidate(arr = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14]) == 26
    assert candidate(arr = [1000, -500, 2000, -1000, 3000, -1500, 4000, -2000, 5000]) == 12000
    assert candidate(arr = [5, -2, -3, 5, -2, -3, 5]) == 8
    assert candidate(arr = [-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100]) == -100
    assert candidate(arr = [-5, -2, -4, -1, -3, -2, -5]) == -1
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 55
    assert candidate(arr = [1, 2, 3, -6, 4, 5, 6, -10, 7, 8, 9]) == 39
    assert candidate(arr = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 2
    assert candidate(arr = [3, -1, -1, -1, 3, -1, -1, -1, 3]) == 4
    assert candidate(arr = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6]) == 11
    assert candidate(arr = [1000, 2000, 3000, 4000, 5000, -5000, 6000, 7000, 8000, 9000]) == 45000
    assert candidate(arr = [10, -3, 4, -1, -2, 1, 5, -3, 4, -2, 0, 1]) == 18
    assert candidate(arr = [100, -101, 200, -201, 300, -301, 400, -401]) == 700
    assert candidate(arr = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 16
    assert candidate(arr = [-15, 14, -13, 12, -11, 10, -9, 8, -7, 6, -5, 4, -3, 2, -1]) == 26
    assert candidate(arr = [10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 10
    assert candidate(arr = [1, 1, 1, 1, -1, -1, -1, -1, 2, 2, 2, 2, -2, -2, -2, -2]) == 9
    assert candidate(arr = [1, 2, 3, -1, -2, -3, 4, 5, 6, -7, 8, 9, 10]) == 42
    assert candidate(arr = [100, -50, 200, -100, 300, -150, 400, -200, 500]) == 1200
    assert candidate(arr = [-1, -2, 3, 4, -5, 6, -7, 8]) == 16
    assert candidate(arr = [0, 1, -1, 2, -2, 3, -3, 4, -4, 5]) == 9
    assert candidate(arr = [1, 2, 3, -6, 1, 2, 3, -6, 1, 2, 3]) == 12
    assert candidate(arr = [-5, 4, -2, 3, -4, 4, -1, -2, 4, 3]) == 13
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(arr = [-1, -2, -3, -4, -5, 10, 1, 2, 3, -1, -2, -3, -4, -5]) == 16
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(arr = [1, -10, 2, -20, 3, -30, 4, -40, 5, -50]) == 9
    assert candidate(arr = [-1, 4, -2, 3, -2, 3, 7, -5, 1]) == 15
    assert candidate(arr = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0]) == 2
    assert candidate(arr = [-100, 200, -300, 400, -500, 600, -700, 800, -900, 1000]) == 1800
    assert candidate(arr = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -1
    assert candidate(arr = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 15
    assert candidate(arr = [100, -1, -1, -1, -1, -1, -1, -1, 100]) == 194
    assert candidate(arr = [5, -3, 8, -1, -2, 7, -4, 9, -6, 10]) == 29
    assert candidate(arr = [100, -100, 200, -200, 300, -300, 400, -400]) == 700
    assert candidate(arr = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100]) == 180
    assert candidate(arr = [3, -1, -1, 4, -10, 2, 1, -1, 2, 1, -5, 4]) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, -10, 6, 7, 8, 9, 10]) == 55
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
    assert candidate(arr = [10, -5, 1, -3, 2, -1, 5, -2, 3, -4, 6]) == 17
    assert candidate(arr = [1, 2, 3, 4, 5, -100, 1, 2, 3, 4, 5]) == 30
    assert candidate(arr = [1000, -500, 100, -50, 10, -5, 1, -1, 0, 1, -1, 10, -10, 100, -100, 500, -500]) == 1555
    assert candidate(arr = [100, -50, 200, -300, 400, -500, 600, -700, 800]) == 1400
    assert candidate(arr = [1, -3, 2, 1, -1, 3, -2, 3]) == 8
    assert candidate(arr = [100, -1000, 500, -300, 200, -100, 400, -500, 600]) == 1300
    assert candidate(arr = [1, 2, -3, 4, -5, 6, -7, 8, -9]) == 14
    assert candidate(arr = [1, 2, -5, 1, 2, -1]) == 6
    assert candidate(arr = [-1, 4, -2, 5, -5, 2, -1, 3, -3, 2]) == 11
    assert candidate(arr = [-100, -101, -102, -103, -104, -105]) == -100
    assert candidate(arr = [1, 1, 1, 1, -5, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(arr = [1, 2, 3, 4, -10, 1, 2, 3, 4]) == 20
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
    assert candidate(arr = [-5, -2, -1, -3, -4, -6, -1, -2, -3]) == -1
    assert candidate(arr = [3, -2, 2, -3, 4, -1, -2, 1, 5, -3]) == 10
    assert candidate(arr = [10, -20, 30, -40, 50, -60, 70, -80, 90]) == 160
    assert candidate(arr = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]) == 15
    assert candidate(arr = [1, 2, 3, -6, 4, 5, 6, 7, 8, 9, 10]) == 55
    assert candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1]) == 1
    assert candidate(arr = [1, 2, 3, 4, 5, -15, 6, 7, 8, 9, 10]) == 55
    assert candidate(arr = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000]) == 7000
    assert candidate(arr = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 18
    assert candidate(arr = [-1, 4, -2, 3, -2, 3, -1, 2, -3, 5]) == 12
    assert candidate(arr = [-1, 4, -2, 3, -2, 3, -1, 2, 1]) == 10
    assert candidate(arr = [100, -1, -2, -3, 100, -1, -2, -3, 100]) == 291
    assert candidate(arr = [7, -4, 3, -6, 2, 1, -5, 4, 3, -1]) == 11
    assert candidate(arr = [3, -1, -1, 3, -1, 3, -1, 3, -1, 3, -1]) == 11
