# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(cookies = [1, 1, 1, 1, 1, 1, 1, 100000],k = 7) == 100000
    assert candidate(cookies = [8, 15, 10, 20, 8],k = 2) == 31
    assert candidate(cookies = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 8) == 100000
    assert candidate(cookies = [1, 100000, 1, 1, 1, 1, 1, 1],k = 3) == 100000
    assert candidate(cookies = [10, 20, 30, 40, 50, 60, 70, 80],k = 2) == 180
    assert candidate(cookies = [10, 20, 30, 40, 50, 60, 70, 80],k = 8) == 80
    assert candidate(cookies = [1, 3, 2, 4, 5, 6, 7, 8],k = 2) == 18
    assert candidate(cookies = [100000, 1, 1, 1, 1, 1, 1, 1],k = 2) == 100000
    assert candidate(cookies = [5, 5, 5, 5, 5, 5, 5, 5],k = 8) == 5
    assert candidate(cookies = [2, 2, 2, 2, 2, 2, 2, 2],k = 2) == 8
    assert candidate(cookies = [6, 1, 3, 2, 2, 4, 1, 2],k = 3) == 7
    assert candidate(cookies = [8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 9
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8],k = 4) == 9
    assert candidate(cookies = [100000, 1, 1, 1, 1, 1, 1, 1],k = 7) == 100000
    assert candidate(cookies = [5, 5, 5, 5, 5, 5, 5, 5],k = 2) == 20
    assert candidate(cookies = [8, 6, 7, 5, 3, 0, 9, 1],k = 5) == 9
    assert candidate(cookies = [8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 18
    assert candidate(cookies = [15, 20, 25, 30, 35, 40, 45, 50],k = 7) == 50
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8],k = 7) == 8
    assert candidate(cookies = [9, 8, 7, 6, 5, 4, 3, 2],k = 5) == 9
    assert candidate(cookies = [100, 200, 300, 400, 500, 600, 700, 800],k = 5) == 800
    assert candidate(cookies = [1, 1, 2, 2, 3, 3, 4, 4],k = 5) == 4
    assert candidate(cookies = [7, 14, 21, 28, 35, 42, 49, 56],k = 2) == 126
    assert candidate(cookies = [80, 70, 60, 50, 40, 30, 20, 10],k = 4) == 90
    assert candidate(cookies = [1, 1, 2, 2, 3, 3, 4, 4],k = 2) == 10
    assert candidate(cookies = [10, 20, 30, 40, 50, 60, 70, 80],k = 4) == 90
    assert candidate(cookies = [12, 11, 10, 9, 8, 7, 6, 5],k = 3) == 23
    assert candidate(cookies = [100, 200, 300, 150, 50, 25, 25, 50],k = 4) == 300
    assert candidate(cookies = [30, 20, 10, 40, 60, 50, 70, 80],k = 5) == 80
    assert candidate(cookies = [30, 20, 10, 20, 30, 20, 10, 20],k = 5) == 40
    assert candidate(cookies = [10, 20, 30, 40, 50, 60, 70, 80],k = 5) == 80
    assert candidate(cookies = [100000, 1, 2, 3, 4, 5, 6, 7],k = 2) == 100000
    assert candidate(cookies = [1, 10, 100, 1000, 10000, 100000, 5, 50],k = 5) == 100000
    assert candidate(cookies = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],k = 4) == 10000000
    assert candidate(cookies = [9, 6, 12, 4, 7, 11, 5, 3],k = 4) == 15
    assert candidate(cookies = [1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 2
    assert candidate(cookies = [9, 9, 9, 9, 9, 9, 9, 9],k = 4) == 18
    assert candidate(cookies = [1, 2, 4, 8, 16, 32, 64, 128],k = 5) == 128
    assert candidate(cookies = [10, 10, 10, 10, 10, 10, 10, 10],k = 7) == 20
    assert candidate(cookies = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 4
    assert candidate(cookies = [18, 23, 45, 12, 34, 56, 78, 90],k = 3) == 123
    assert candidate(cookies = [100, 200, 300, 400, 500, 600, 700, 800],k = 6) == 800
    assert candidate(cookies = [100, 200, 300, 400, 500, 600, 700, 800],k = 4) == 900
    assert candidate(cookies = [8, 1, 5, 7, 3, 6, 4, 2],k = 3) == 12
    assert candidate(cookies = [9, 8, 7, 6, 5, 4, 3, 2],k = 6) == 9
    assert candidate(cookies = [16, 14, 12, 10, 8, 6, 4, 2],k = 4) == 18
    assert candidate(cookies = [5, 10, 15, 20, 25, 30, 35, 40],k = 5) == 40
    assert candidate(cookies = [5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 15
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8],k = 7) == 8
    assert candidate(cookies = [9, 18, 27, 36, 45, 54, 63, 72],k = 4) == 81
    assert candidate(cookies = [1, 1, 1, 1, 1, 1, 1, 1],k = 8) == 1
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 11
    assert candidate(cookies = [15, 14, 13, 12, 11, 10, 9, 8],k = 4) == 23
    assert candidate(cookies = [15, 25, 35, 45, 55, 65, 75, 85],k = 5) == 85
    assert candidate(cookies = [12, 11, 10, 9, 8, 7, 6, 5],k = 2) == 34
    assert candidate(cookies = [1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 3
    assert candidate(cookies = [30, 20, 10, 10, 20, 30, 40, 50],k = 5) == 50
    assert candidate(cookies = [10, 20, 30, 40, 50, 60, 70, 80],k = 3) == 120
    assert candidate(cookies = [15, 15, 15, 15, 15, 15, 15, 15],k = 7) == 30
    assert candidate(cookies = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],k = 8) == 8000
    assert candidate(cookies = [1, 1, 1, 1, 1, 1, 1, 1],k = 8) == 1
    assert candidate(cookies = [8, 16, 32, 64, 128, 256, 512, 1024],k = 2) == 1024
    assert candidate(cookies = [30, 20, 10, 60, 50, 40, 70, 80],k = 5) == 80
    assert candidate(cookies = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 3) == 150
    assert candidate(cookies = [5, 10, 15, 20, 25, 30, 35, 40],k = 6) == 40
    assert candidate(cookies = [9, 3, 10, 12, 8, 15, 5, 7],k = 3) == 24
    assert candidate(cookies = [3, 1, 2, 4, 5, 6, 7, 8],k = 4) == 9
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8],k = 4) == 9
    assert candidate(cookies = [12, 17, 22, 14, 29, 18, 15, 20],k = 4) == 41
    assert candidate(cookies = [1, 2, 4, 8, 16, 32, 64, 128],k = 3) == 128
    assert candidate(cookies = [100, 100, 100, 100, 100, 100, 100, 100],k = 5) == 200
    assert candidate(cookies = [12, 23, 34, 45, 56, 67, 78, 89],k = 3) == 135
    assert candidate(cookies = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],k = 4) == 200000
    assert candidate(cookies = [10, 20, 30, 40, 50, 60, 70, 80],k = 6) == 80
    assert candidate(cookies = [7, 8, 9, 10, 11, 12, 13, 14],k = 6) == 17
    assert candidate(cookies = [100, 200, 300, 400, 500, 600, 700, 800],k = 3) == 1200
    assert candidate(cookies = [8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 8
    assert candidate(cookies = [8, 15, 10, 20, 8, 5, 3, 7],k = 3) == 26
    assert candidate(cookies = [5, 15, 25, 35, 45, 55, 65, 75],k = 3) == 110
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8],k = 8) == 8
    assert candidate(cookies = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 8) == 10
    assert candidate(cookies = [100, 200, 300, 400, 500, 600, 700, 800],k = 4) == 900
    assert candidate(cookies = [15, 15, 15, 15, 15, 15, 15, 15],k = 6) == 30
    assert candidate(cookies = [100, 200, 300, 400, 500, 600, 700, 800],k = 5) == 800
    assert candidate(cookies = [2, 4, 6, 8, 10, 12, 14, 16],k = 3) == 24
    assert candidate(cookies = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],k = 2) == 18000
    assert candidate(cookies = [50, 40, 30, 20, 10, 5, 3, 1],k = 4) == 50
    assert candidate(cookies = [5, 5, 15, 15, 25, 25, 35, 35],k = 4) == 40
    assert candidate(cookies = [15, 15, 15, 15, 15, 15, 15, 15],k = 2) == 60
    assert candidate(cookies = [2, 2, 2, 2, 2, 2, 2, 2],k = 7) == 4
    assert candidate(cookies = [25, 25, 25, 25, 25, 25, 25, 25],k = 8) == 25
    assert candidate(cookies = [8, 15, 10, 20, 8, 12, 15, 10],k = 3) == 33
    assert candidate(cookies = [8, 1, 2, 3, 4, 5, 6, 7],k = 2) == 18
    assert candidate(cookies = [10, 20, 10, 20, 10, 20, 10, 20],k = 4) == 30
    assert candidate(cookies = [50, 40, 30, 20, 10, 1, 2, 3],k = 3) == 53
    assert candidate(cookies = [1, 1, 2, 2, 3, 3, 4, 4],k = 4) == 5
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8],k = 8) == 8
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],k = 4) == 34
    assert candidate(cookies = [1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 4
    assert candidate(cookies = [1, 2, 3, 4, 5, 6, 7, 8],k = 3) == 12
    assert candidate(cookies = [10, 10, 20, 20, 30, 30, 40, 40],k = 4) == 50
    assert candidate(cookies = [9, 18, 27, 36, 45, 54, 63, 72],k = 4) == 81
    assert candidate(cookies = [8, 1, 2, 3, 4, 5, 6, 7],k = 8) == 8
    assert candidate(cookies = [100, 200, 300, 400, 500, 600, 700, 800],k = 7) == 800
