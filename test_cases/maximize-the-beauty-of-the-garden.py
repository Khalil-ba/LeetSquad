# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(flowers = [-10000, 10000, -10000, 10000, -10000, 10000]) == 30000
    assert candidate(flowers = [5, 8, 5, 3, 5, 2, 5]) == 33
    assert candidate(flowers = [100, 1, 1, -3, 1]) == 3
    assert candidate(flowers = [2, 3, 4, 5, 4, 3, 2, 1, 2]) == 26
    assert candidate(flowers = [5, 3, 5, 2, 5]) == 20
    assert candidate(flowers = [1, 2, 3, 1, 2]) == 8
    assert candidate(flowers = [3, 2, 1, 2, 3, 2, 1]) == 11
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 46
    assert candidate(flowers = [2, 3, 2, 1, 2, 3, 2, 2]) == 17
    assert candidate(flowers = [1, -1, 1, -1, 1]) == 3
    assert candidate(flowers = [-1, -2, 0, -1]) == -2
    assert candidate(flowers = [-1, -2, -3, -4, -1]) == -2
    assert candidate(flowers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 1]) == 26
    assert candidate(flowers = [-10000, 0, 10000, 0, -10000]) == 10000
    assert candidate(flowers = [5, 5, 5, 5, 5]) == 25
    assert candidate(flowers = [-10000, 10000, -10000, 10000]) == 20000
    assert candidate(flowers = [1, -1, 2, -2, 1, -1]) == 4
    assert candidate(flowers = [-10000, 10000, -10000]) == -10000
    assert candidate(flowers = [-5, -5, -5, -5, -5]) == -10
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(flowers = [10000, 10000, 10000]) == 30000
    assert candidate(flowers = [2, 4, 6, 8, 10, 8, 6, 4, 2]) == 50
    assert candidate(flowers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(flowers = [5, 1, 5, 2, 5, 3, 5]) == 26
    assert candidate(flowers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 110
    assert candidate(flowers = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(flowers = [1, -1, 1, -1, 1, -1, 1, -1]) == 4
    assert candidate(flowers = [0, 0, 1, 2, 1, 2, 1, 0, 0]) == 7
    assert candidate(flowers = [1, 3, 2, 4, 2, 3, 1]) == 16
    assert candidate(flowers = [10000, -10000, 10000, -10000, 10000]) == 30000
    assert candidate(flowers = [-1, -2, -3, -4, -5, -4, -3, -2, -1]) == -2
    assert candidate(flowers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 200
    assert candidate(flowers = [10, -10, 20, -20, 30, 20, -10, 10]) == 90
    assert candidate(flowers = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]) == -10
    assert candidate(flowers = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 10]) == 20
    assert candidate(flowers = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 104
    assert candidate(flowers = [100, -200, 300, -400, 500, -300, 200, 100, -100, 200, -300, 400, -500, 300, -200, 100]) == 2200
    assert candidate(flowers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 80
    assert candidate(flowers = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]) == 55
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 121
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 46
    assert candidate(flowers = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 5
    assert candidate(flowers = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 49
    assert candidate(flowers = [1, 3, -2, 4, 3, 1, 5, 1]) == 18
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]) == 360
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 211
    assert candidate(flowers = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]) == 55
    assert candidate(flowers = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1]) == 110
    assert candidate(flowers = [-1, -2, -3, -4, -5, -4, -3, -2, -1, -2, -3, -4, -5, -4, -3, -2, -1]) == -2
    assert candidate(flowers = [-10, 20, -30, 40, -50, 40, -30, 20, -10, 20]) == 140
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 12, 13, 14, 15, 1]) == 122
    assert candidate(flowers = [5, 3, 1, 3, 5, 2, 5, 1, 3, 5, 4, 3, 5]) == 45
    assert candidate(flowers = [10, 20, 30, -10, 20, -10, 40, 30, 20, 10]) == 180
    assert candidate(flowers = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 40, 40, 30, 30, 20, 20, 10, 10, 20, 20, 30, 30, 40, 40, 50, 50]) == 580
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 166
    assert candidate(flowers = [-5, -4, -3, -2, -1, -2, -3, -4, -5]) == -4
    assert candidate(flowers = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == 25
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 12
    assert candidate(flowers = [1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1]) == 141
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 81
    assert candidate(flowers = [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]) == 39
    assert candidate(flowers = [3, -1, 2, -1, 3, -1, 2, -1, 3]) == 13
    assert candidate(flowers = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 65
    assert candidate(flowers = [1, -2, 3, 4, -2, 3, 1, -1, 1]) == 13
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 56
    assert candidate(flowers = [10, -20, 30, -40, 50, -40, 30, -20, 10]) == 130
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(flowers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 20
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 440
    assert candidate(flowers = [10, 20, 30, 40, 50, 10, -10, -20, -30, -40, -50]) == 160
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(flowers = [1, -2, 3, 4, 3, 2, 1]) == 14
    assert candidate(flowers = [1000, -500, 2000, -1000, 1000, 3000, 4000, -500, 1000]) == 12000
    assert candidate(flowers = [7, 1, 3, 3, 1, 7, 2, 5, 2, 7]) == 38
    assert candidate(flowers = [-5, -5, -5, -5, -5, -5, -5]) == -10
    assert candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 75
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 176
    assert candidate(flowers = [10, 20, -10, 30, -20, 40, -10, 20, 10, 50]) == 130
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 225
    assert candidate(flowers = [-5, -1, -5, -2, -3, -1, -4, -1, -5]) == -2
    assert candidate(flowers = [100, -1, 200, -2, 300, -3, 100, -1, 200, -2, 300, -3]) == 900
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 175
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 196
    assert candidate(flowers = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1]) == -2
    assert candidate(flowers = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3]) == 102
    assert candidate(flowers = [-1, -2, -3, -4, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 25
    assert candidate(flowers = [5, 3, -2, 5, 7, -2, 5, 3, 5, 8, 5, 3, -2, 5, 7, -2, 5, 3, 5, 8, 5]) == 87
    assert candidate(flowers = [10000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10000]) == 20045
    assert candidate(flowers = [1, -2, 3, 4, -2, 3, 1, 5, 1]) == 18
    assert candidate(flowers = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 420
    assert candidate(flowers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 75
    assert candidate(flowers = [100, 200, 300, 400, 500, 400, 300, 200, 100]) == 2500
    assert candidate(flowers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == 40
    assert candidate(flowers = [-1, -2, -3, -4, -5, -4, -3, -2, -1, -2, -1]) == -2
    assert candidate(flowers = [0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1]) == 0
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 144
    assert candidate(flowers = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1, 2, 3, 4, 3, 2, 1, 2, 1]) == 64
    assert candidate(flowers = [1, -2, 3, 4, 5, 3, 2, 1]) == 19
    assert candidate(flowers = [1, -2, 3, 4, -1, 5, 6, 3, -2, 1]) == 23
    assert candidate(flowers = [1, -2, 3, 4, -5, 3, 2, -1, 3]) == 15
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000]) == 5600
    assert candidate(flowers = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 10000, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 10000]) == 119955
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 65
    assert candidate(flowers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 100]) == 5600
    assert candidate(flowers = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 1]) == 28
    assert candidate(flowers = [7, -3, 5, -3, 2, 5, -3, 7, 5, 7]) == 38
    assert candidate(flowers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, -1, -2, -3, -4, -5]) == 46
    assert candidate(flowers = [10000, -10000, 10000, -10000, 10000, -10000, 10000]) == 40000
    assert candidate(flowers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 5
    assert candidate(flowers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == 50
    assert candidate(flowers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 30
    assert candidate(flowers = [100, 200, 300, 200, 100, 200, 300, 200, 100, 200, 300, 200, 100]) == 2500
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 1]) == 103
    assert candidate(flowers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]) == 75
    assert candidate(flowers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 1000
    assert candidate(flowers = [10, 20, -30, 10, 20, 10, 20, 30, 20, 10]) == 150
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 110
    assert candidate(flowers = [10, 20, -30, 40, -50, 60, -70, 80, -90, 100, 20, 30, 40]) == 370
    assert candidate(flowers = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 6
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 169
    assert candidate(flowers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 199
    assert candidate(flowers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 100
