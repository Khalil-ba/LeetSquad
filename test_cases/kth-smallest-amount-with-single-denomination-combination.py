# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(coins = [10, 20, 30],k = 5) == 50
    assert candidate(coins = [15, 20, 25],k = 15) == 125
    assert candidate(coins = [15, 25, 35],k = 8) == 70
    assert candidate(coins = [25, 50, 75],k = 20) == 500
    assert candidate(coins = [1, 10, 100],k = 100) == 100
    assert candidate(coins = [4, 8, 12],k = 10) == 40
    assert candidate(coins = [7, 14, 28],k = 5) == 35
    assert candidate(coins = [2, 3, 5, 7],k = 12) == 15
    assert candidate(coins = [10, 20, 30],k = 20) == 200
    assert candidate(coins = [7, 11, 13],k = 15) == 52
    assert candidate(coins = [3, 6, 9],k = 3) == 9
    assert candidate(coins = [7, 11, 13],k = 10) == 35
    assert candidate(coins = [9, 18, 27, 36],k = 15) == 135
    assert candidate(coins = [15, 20, 25],k = 8) == 60
    assert candidate(coins = [2, 3, 5],k = 30) == 40
    assert candidate(coins = [1, 2, 3],k = 10) == 10
    assert candidate(coins = [5, 2],k = 7) == 12
    assert candidate(coins = [1, 2, 3],k = 5) == 5
    assert candidate(coins = [8, 16, 24],k = 12) == 96
    assert candidate(coins = [17, 19, 23],k = 8) == 57
    assert candidate(coins = [3, 5, 7],k = 20) == 36
    assert candidate(coins = [17, 23, 29],k = 20) == 153
    assert candidate(coins = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 75) == 150
    assert candidate(coins = [2, 5, 7, 10],k = 30) == 46
    assert candidate(coins = [1, 3, 6, 9, 12, 15],k = 100) == 100
    assert candidate(coins = [2, 5, 10, 20],k = 25) == 42
    assert candidate(coins = [2, 4, 8, 16, 32, 64],k = 200) == 400
    assert candidate(coins = [1, 3, 5, 7, 9],k = 100) == 100
    assert candidate(coins = [3, 5, 7, 9, 11, 13],k = 100) == 165
    assert candidate(coins = [2, 5, 10, 20],k = 30) == 50
    assert candidate(coins = [3, 5, 7, 9],k = 20) == 36
    assert candidate(coins = [2, 3, 5, 7, 11, 13, 17, 19],k = 150) == 185
    assert candidate(coins = [6, 12, 18, 24, 30],k = 25) == 150
    assert candidate(coins = [2, 5, 10, 20, 25],k = 200) == 334
    assert candidate(coins = [1, 3, 5, 7, 9, 11],k = 100) == 100
    assert candidate(coins = [2, 4, 8, 16, 32, 64],k = 150) == 300
    assert candidate(coins = [4, 6, 8, 10, 12, 14],k = 60) == 156
    assert candidate(coins = [7, 14, 21, 28, 35],k = 75) == 525
    assert candidate(coins = [15, 25, 35, 45, 55, 65, 75],k = 300) == 2430
    assert candidate(coins = [13, 26, 39, 52, 65, 78, 91],k = 100) == 1300
    assert candidate(coins = [1, 4, 9, 16, 25],k = 100) == 100
    assert candidate(coins = [2, 3, 5, 7],k = 50) == 65
    assert candidate(coins = [13, 17, 19],k = 30) == 169
    assert candidate(coins = [7, 14, 21, 28],k = 25) == 175
    assert candidate(coins = [8, 16, 24, 32, 40, 48],k = 100) == 800
    assert candidate(coins = [3, 5, 7],k = 15) == 27
    assert candidate(coins = [11, 22, 33, 44, 55],k = 50) == 550
    assert candidate(coins = [11, 13, 17, 19],k = 50) == 190
    assert candidate(coins = [1, 3, 7, 9, 11, 13],k = 40) == 40
    assert candidate(coins = [11, 13, 17],k = 15) == 68
    assert candidate(coins = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42],k = 700) == 700
    assert candidate(coins = [7, 14, 21, 28],k = 25) == 175
    assert candidate(coins = [4, 7, 10, 13, 16],k = 75) == 169
    assert candidate(coins = [5, 10, 15, 20, 25, 30, 35],k = 100) == 500
    assert candidate(coins = [15, 21, 27, 33, 39],k = 40) == 234
    assert candidate(coins = [2, 5, 10, 20, 25, 50],k = 1000) == 1666
    assert candidate(coins = [11, 13, 17],k = 20) == 91
    assert candidate(coins = [6, 12, 18, 24, 30],k = 50) == 300
    assert candidate(coins = [1, 2, 4, 8, 16, 32],k = 1000) == 1000
    assert candidate(coins = [17, 19, 23, 29, 31, 37, 41, 43, 47],k = 400) == 1410
    assert candidate(coins = [5, 10, 15, 20, 25, 30],k = 150) == 750
    assert candidate(coins = [2, 3, 5, 7, 11],k = 100) == 126
    assert candidate(coins = [1, 3, 5, 7, 9, 11, 13],k = 50) == 50
    assert candidate(coins = [2, 3, 5, 7, 11],k = 50) == 64
    assert candidate(coins = [21, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79],k = 1000) == 3161
    assert candidate(coins = [11, 22, 33, 44],k = 100) == 1100
    assert candidate(coins = [18, 24, 30, 36, 42],k = 70) == 648
    assert candidate(coins = [17, 23, 29],k = 12) == 92
    assert candidate(coins = [10, 15, 20, 25, 30],k = 300) == 2050
    assert candidate(coins = [25, 50, 75, 100, 125],k = 35) == 875
    assert candidate(coins = [6, 9, 12, 18],k = 50) == 225
    assert candidate(coins = [3, 5, 7, 9, 11],k = 30) == 50
    assert candidate(coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 600) == 3000
    assert candidate(coins = [18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102],k = 1500) == 12312
    assert candidate(coins = [3, 5, 15],k = 25) == 54
    assert candidate(coins = [11, 22, 33, 44, 55],k = 100) == 1100
    assert candidate(coins = [15, 25, 35, 45],k = 60) == 555
    assert candidate(coins = [6, 12, 18, 24],k = 100) == 600
    assert candidate(coins = [5, 10, 15, 20, 25, 30, 35],k = 200) == 1000
    assert candidate(coins = [11, 22, 33],k = 25) == 275
    assert candidate(coins = [5, 10, 15, 20, 25],k = 250) == 1250
    assert candidate(coins = [19, 21, 23, 25],k = 40) == 228
    assert candidate(coins = [15, 25, 35, 45, 55, 65, 75],k = 200) == 1635
    assert candidate(coins = [2, 3, 5, 7, 11, 13, 17, 19],k = 300) == 365
    assert candidate(coins = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],k = 1000) == 2000
    assert candidate(coins = [2, 4, 8, 16, 32, 64, 128],k = 200) == 400
    assert candidate(coins = [7, 11, 13],k = 15) == 52
    assert candidate(coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 500) == 5000
    assert candidate(coins = [7, 11, 13, 17, 19],k = 35) == 91
    assert candidate(coins = [15, 25, 35, 45],k = 200) == 1845
    assert candidate(coins = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],k = 800) == 6400
    assert candidate(coins = [3, 6, 9, 12, 15],k = 50) == 150
    assert candidate(coins = [1, 4, 9, 16, 25],k = 150) == 150
    assert candidate(coins = [3, 6, 12, 18, 24, 30],k = 150) == 450
    assert candidate(coins = [3, 5, 7, 9],k = 20) == 36
    assert candidate(coins = [17, 19, 23],k = 20) == 136
    assert candidate(coins = [11, 22, 33, 44, 55],k = 45) == 495
    assert candidate(coins = [13, 26, 39, 52, 65],k = 50) == 650
    assert candidate(coins = [19, 31, 37, 41],k = 25) == 190
    assert candidate(coins = [7, 14, 21],k = 15) == 105
    assert candidate(coins = [3, 6, 9, 12, 15],k = 30) == 90
    assert candidate(coins = [6, 10, 14],k = 30) == 110
    assert candidate(coins = [2, 4, 6, 8, 10],k = 30) == 60
    assert candidate(coins = [15, 20, 25],k = 50) == 420
    assert candidate(coins = [13, 26, 39, 52, 65, 78],k = 150) == 1950
    assert candidate(coins = [2, 3, 5, 7],k = 25) == 33
    assert candidate(coins = [9, 18, 27, 36, 45],k = 30) == 270
    assert candidate(coins = [8, 16, 24, 32, 40, 48],k = 200) == 1600
    assert candidate(coins = [7, 14, 28],k = 15) == 105
    assert candidate(coins = [2, 5, 10, 25],k = 50) == 84
