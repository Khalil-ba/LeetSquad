# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(banned = [],n = 10,maxSum = 55) == 10
    assert candidate(banned = [1, 2, 3],n = 5,maxSum = 10) == 2
    assert candidate(banned = [5],n = 5,maxSum = 5) == 2
    assert candidate(banned = [1, 4, 6],n = 6,maxSum = 4) == 1
    assert candidate(banned = [2, 5, 8],n = 10,maxSum = 20) == 4
    assert candidate(banned = [1, 2, 3, 4, 5],n = 10,maxSum = 30) == 4
    assert candidate(banned = [10, 20, 30],n = 50,maxSum = 150) == 16
    assert candidate(banned = [],n = 10,maxSum = 50) == 9
    assert candidate(banned = [1],n = 100,maxSum = 5000) == 98
    assert candidate(banned = [10],n = 10,maxSum = 10) == 4
    assert candidate(banned = [2, 4, 6, 8, 10],n = 10,maxSum = 25) == 5
    assert candidate(banned = [1, 3, 5, 7, 9],n = 10,maxSum = 25) == 4
    assert candidate(banned = [4, 3, 5, 6],n = 7,maxSum = 18) == 3
    assert candidate(banned = [5, 6, 7, 8, 9],n = 10,maxSum = 15) == 4
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20,maxSum = 100) == 9
    assert candidate(banned = [1],n = 1000000000,maxSum = 1000000000000000) == 44721358
    assert candidate(banned = [],n = 1000000000,maxSum = 1000000000000000) == 44721359
    assert candidate(banned = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],n = 500,maxSum = 2500) == 69
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],n = 50,maxSum = 500) == 21
    assert candidate(banned = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99],n = 100,maxSum = 2500) == 60
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9],n = 10,maxSum = 45) == 1
    assert candidate(banned = [100, 200, 300, 400, 500, 600, 700, 800, 900],n = 1000,maxSum = 40000) == 281
    assert candidate(banned = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50,maxSum = 125) == 14
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],n = 30,maxSum = 240) == 15
    assert candidate(banned = [999999999],n = 1000000000,maxSum = 1000000000) == 44720
    assert candidate(banned = [100, 200, 300, 400, 500],n = 1000,maxSum = 100000) == 444
    assert candidate(banned = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],n = 500,maxSum = 1500) == 54
    assert candidate(banned = [500000000, 600000000, 700000000, 800000000, 900000000],n = 1000000000,maxSum = 1000000000000000) == 44721359
    assert candidate(banned = [5, 15, 25, 35, 45],n = 50,maxSum = 150) == 15
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9],n = 9,maxSum = 45) == 0
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 100,maxSum = 1000) == 28
    assert candidate(banned = [1],n = 1000000,maxSum = 500000000000) == 999998
    assert candidate(banned = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],n = 30,maxSum = 100) == 11
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 1000000,maxSum = 500000000) == 31612
    assert candidate(banned = [500000000],n = 1000000000,maxSum = 1000000000000) == 1414213
    assert candidate(banned = [1, 3, 5, 7, 9],n = 100,maxSum = 2500) == 65
    assert candidate(banned = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],n = 1000,maxSum = 500000) == 980
    assert candidate(banned = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],n = 1000000000,maxSum = 5500000000) == 104875
    assert candidate(banned = [10, 20, 30, 40, 50],n = 100,maxSum = 450) == 28
    assert candidate(banned = [5, 7, 8, 10],n = 15,maxSum = 50) == 8
    assert candidate(banned = [1000000],n = 1000000,maxSum = 1000000) == 1413
    assert candidate(banned = [999999995, 999999996, 999999997, 999999998, 999999999],n = 1000000000,maxSum = 1000000000000) == 1414213
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 10,maxSum = 50) == 0
    assert candidate(banned = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],n = 1024,maxSum = 500000) == 990
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 20,maxSum = 50) == 4
    assert candidate(banned = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98],n = 100,maxSum = 2500) == 60
    assert candidate(banned = [3, 4, 7, 8, 11, 12, 15, 16, 19, 20],n = 25,maxSum = 150) == 12
    assert candidate(banned = [3, 6, 9, 12, 15, 18],n = 25,maxSum = 150) == 14
    assert candidate(banned = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],n = 100,maxSum = 450) == 28
    assert candidate(banned = [500000000, 500000001, 500000002, 500000003, 500000004],n = 1000000000,maxSum = 1000000000000) == 1414213
    assert candidate(banned = [10, 20, 30, 40, 50],n = 50,maxSum = 125) == 14
    assert candidate(banned = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96],n = 100,maxSum = 1500) == 50
    assert candidate(banned = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 100,maxSum = 350) == 25
    assert candidate(banned = [1, 2, 3, 4, 5],n = 10,maxSum = 10) == 1
    assert candidate(banned = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],n = 10000,maxSum = 10000000) == 4467
    assert candidate(banned = [5, 7, 9, 11, 13],n = 20,maxSum = 100) == 11
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15],n = 20,maxSum = 100) == 9
    assert candidate(banned = [9, 18, 27, 36, 45],n = 50,maxSum = 200) == 18
    assert candidate(banned = [1, 2, 3, 4, 5],n = 5,maxSum = 10) == 0
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 10,maxSum = 55) == 0
    assert candidate(banned = [1, 3, 5, 7, 9],n = 1000,maxSum = 10000) == 136
    assert candidate(banned = [5],n = 100,maxSum = 5000) == 98
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,maxSum = 190) == 0
    assert candidate(banned = [5, 10, 15, 20, 25, 30],n = 1000,maxSum = 50000) == 310
    assert candidate(banned = [1000000000],n = 1000000000,maxSum = 1000000000000000) == 44721359
    assert candidate(banned = [2, 3, 5, 7, 11, 13, 17, 19],n = 20,maxSum = 15) == 3
    assert candidate(banned = [100, 200, 300, 400, 500],n = 1000,maxSum = 50000) == 314
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 30,maxSum = 240) == 15
    assert candidate(banned = [100, 200, 300, 400, 500],n = 1000,maxSum = 5000) == 99
    assert candidate(banned = [1],n = 1000000000,maxSum = 1000000000000) == 1414212
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 30,maxSum = 225) == 15
    assert candidate(banned = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],n = 30,maxSum = 120) == 12
    assert candidate(banned = [100],n = 100,maxSum = 5000) == 99
    assert candidate(banned = [100, 200, 300, 400, 500, 600, 700, 800, 900],n = 1000,maxSum = 4500) == 94
    assert candidate(banned = [1],n = 1000000,maxSum = 500000000) == 31621
    assert candidate(banned = [999999, 999998, 999997, 999996, 999995],n = 1000000,maxSum = 500000000000) == 999995
    assert candidate(banned = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],n = 100,maxSum = 2500) == 60
    assert candidate(banned = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],n = 500,maxSum = 125000) == 490
    assert candidate(banned = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50],n = 50,maxSum = 200) == 16
    assert candidate(banned = [50, 60, 70, 80, 90, 100],n = 100,maxSum = 5000) == 94
    assert candidate(banned = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],n = 500,maxSum = 12500) == 156
    assert candidate(banned = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 100,maxSum = 500) == 29
    assert candidate(banned = [5, 10, 15, 20, 25],n = 1000,maxSum = 500000) == 994
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 20,maxSum = 100) == 10
    assert candidate(banned = [2, 3, 5, 7, 11, 13],n = 15,maxSum = 30) == 5
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 100,maxSum = 100) == 4
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],n = 20,maxSum = 190) == 1
    assert candidate(banned = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],n = 10000,maxSum = 50000000) == 9989
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,maxSum = 210) == 0
    assert candidate(banned = [1, 2, 3, 4, 5],n = 10,maxSum = 20) == 2
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 30,maxSum = 150) == 12
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 15,maxSum = 50) == 4
    assert candidate(banned = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],n = 10000000,maxSum = 55000000) == 10487
    assert candidate(banned = [6, 7, 8, 9, 10],n = 10,maxSum = 15) == 5
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],n = 30,maxSum = 450) == 0
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9],n = 10,maxSum = 25) == 1
    assert candidate(banned = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],n = 30,maxSum = 150) == 13
    assert candidate(banned = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],n = 50,maxSum = 300) == 19
    assert candidate(banned = [5, 10, 15, 20, 25],n = 30,maxSum = 150) == 15
    assert candidate(banned = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],n = 100,maxSum = 4000) == 75
    assert candidate(banned = [1, 2, 3, 4, 5],n = 10,maxSum = 30) == 4
    assert candidate(banned = [10, 20, 30, 40, 50],n = 100,maxSum = 2000) == 60
    assert candidate(banned = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50,maxSum = 300) == 21
    assert candidate(banned = [1000000000],n = 1000000000,maxSum = 1000000000) == 44720
    assert candidate(banned = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],n = 50,maxSum = 100) == 10
    assert candidate(banned = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],n = 10000,maxSum = 55000) == 331
    assert candidate(banned = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 100,maxSum = 4500) == 90
