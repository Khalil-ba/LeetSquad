# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(banned = [11],n = 7,maxSum = 50) == 7
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7],n = 8,maxSum = 1) == 0
    assert candidate(banned = [],n = 10,maxSum = 55) == 10
    assert candidate(banned = [1, 6, 5],n = 5,maxSum = 6) == 2
    assert candidate(banned = [2, 4, 6, 8],n = 10,maxSum = 30) == 5
    assert candidate(banned = [2, 4, 6, 8],n = 10,maxSum = 15) == 3
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 10,maxSum = 55) == 0
    assert candidate(banned = [5, 6, 7, 8, 9, 10],n = 10,maxSum = 1) == 1
    assert candidate(banned = [100, 200, 300],n = 500,maxSum = 1500) == 54
    assert candidate(banned = [10],n = 10,maxSum = 10) == 4
    assert candidate(banned = [1, 3, 5, 7, 9],n = 10,maxSum = 25) == 4
    assert candidate(banned = [3, 5, 7],n = 10,maxSum = 25) == 5
    assert candidate(banned = [2, 4, 6, 8],n = 10,maxSum = 15) == 3
    assert candidate(banned = [1, 2, 3],n = 3,maxSum = 5) == 0
    assert candidate(banned = [3, 5, 7, 9],n = 15,maxSum = 40) == 6
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20,maxSum = 100) == 9
    assert candidate(banned = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],n = 100,maxSum = 1000) == 41
    assert candidate(banned = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 100,maxSum = 1500) == 51
    assert candidate(banned = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 100,maxSum = 450) == 28
    assert candidate(banned = [9996, 9997, 9998, 9999, 10000],n = 10000,maxSum = 50000000) == 9995
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 20,maxSum = 150) == 5
    assert candidate(banned = [10, 20, 30, 40, 50],n = 50,maxSum = 1275) == 45
    assert candidate(banned = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 100,maxSum = 4950) == 89
    assert candidate(banned = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50,maxSum = 125) == 14
    assert candidate(banned = [5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009],n = 10000,maxSum = 25000000) == 7067
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 15,maxSum = 45) == 3
    assert candidate(banned = [100, 200, 300, 400],n = 500,maxSum = 10000) == 140
    assert candidate(banned = [1, 3, 5, 7, 9],n = 15,maxSum = 50) == 6
    assert candidate(banned = [5000, 5001, 5002, 5003, 5004],n = 10000,maxSum = 25000000) == 7069
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 30,maxSum = 250) == 15
    assert candidate(banned = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],n = 100,maxSum = 2500) == 67
    assert candidate(banned = [1000],n = 10000,maxSum = 1000000) == 1413
    assert candidate(banned = [100, 200, 300, 400, 500],n = 1000,maxSum = 10000) == 140
    assert candidate(banned = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],n = 100,maxSum = 5000) == 89
    assert candidate(banned = [15, 25, 35, 45, 55, 65, 75, 85, 95],n = 100,maxSum = 4500) == 90
    assert candidate(banned = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50,maxSum = 1000) == 40
    assert candidate(banned = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 100,maxSum = 3000) == 70
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 20,maxSum = 150) == 9
    assert candidate(banned = [1, 2, 3, 4, 5],n = 10000,maxSum = 1000000000) == 9995
    assert candidate(banned = [1000, 2000, 3000, 4000],n = 5000,maxSum = 12500000) == 4996
    assert candidate(banned = [9999],n = 10000,maxSum = 10000) == 140
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],n = 50,maxSum = 600) == 24
    assert candidate(banned = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192],n = 10000,maxSum = 10000000) == 4460
    assert candidate(banned = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],n = 30,maxSum = 150) == 12
    assert candidate(banned = [1, 10, 100, 1000, 10000],n = 10000,maxSum = 50005000) == 9995
    assert candidate(banned = [50, 51, 52, 53, 54, 55],n = 100,maxSum = 1000) == 44
    assert candidate(banned = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99],n = 100,maxSum = 1500) == 47
    assert candidate(banned = [],n = 10000,maxSum = 50000000) == 9999
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 25,maxSum = 100) == 4
    assert candidate(banned = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50,maxSum = 1275) == 40
    assert candidate(banned = [1, 3, 5, 7, 9],n = 10,maxSum = 25) == 4
    assert candidate(banned = [],n = 100,maxSum = 5000) == 99
    assert candidate(banned = [],n = 50,maxSum = 1275) == 50
    assert candidate(banned = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],n = 30,maxSum = 250) == 18
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20,maxSum = 190) == 10
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,maxSum = 190) == 0
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],n = 20,maxSum = 90) == 5
    assert candidate(banned = [2, 3, 5, 7, 11, 13, 17, 19],n = 20,maxSum = 50) == 7
    assert candidate(banned = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 1000,maxSum = 500500) == 990
    assert candidate(banned = [100, 200, 300, 400, 500],n = 1000,maxSum = 5000) == 99
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],n = 30,maxSum = 225) == 15
    assert candidate(banned = [15, 16, 17, 18, 19, 20],n = 20,maxSum = 150) == 14
    assert candidate(banned = [1],n = 10000,maxSum = 5000000) == 3160
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16],n = 20,maxSum = 100) == 10
    assert candidate(banned = [2, 4, 6, 8, 10],n = 15,maxSum = 50) == 7
    assert candidate(banned = [1, 10, 100, 1000, 10000],n = 10000,maxSum = 50000000) == 9995
    assert candidate(banned = [101, 102, 103, 104, 105],n = 150,maxSum = 10000) == 139
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],n = 40,maxSum = 400) == 19
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 20,maxSum = 100) == 10
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],n = 20,maxSum = 190) == 1
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],n = 20,maxSum = 210) == 0
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],n = 100,maxSum = 2500) == 49
    assert candidate(banned = [1, 2, 3, 4, 5],n = 10,maxSum = 20) == 2
    assert candidate(banned = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],n = 15,maxSum = 50) == 4
    assert candidate(banned = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 1500,maxSum = 100000) == 444
    assert candidate(banned = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 1000,maxSum = 5000) == 99
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15],n = 15,maxSum = 60) == 7
    assert candidate(banned = [2, 4, 6, 8, 10],n = 20,maxSum = 100) == 10
    assert candidate(banned = [15, 30, 45, 60, 75],n = 100,maxSum = 3775) == 83
    assert candidate(banned = [1],n = 10000,maxSum = 50005000) == 9999
    assert candidate(banned = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],n = 150,maxSum = 1000) == 42
    assert candidate(banned = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],n = 10000,maxSum = 1000000) == 1413
    assert candidate(banned = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],n = 150,maxSum = 1000) == 41
    assert candidate(banned = [1000],n = 2000,maxSum = 1000000) == 1413
    assert candidate(banned = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],n = 110,maxSum = 1050) == 45
    assert candidate(banned = [15, 16, 17, 18, 19, 20],n = 20,maxSum = 190) == 14
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],n = 20,maxSum = 150) == 10
    assert candidate(banned = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],n = 50,maxSum = 200) == 17
    assert candidate(banned = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],n = 1000,maxSum = 20000) == 198
    assert candidate(banned = [100, 101, 102, 103, 104],n = 110,maxSum = 500) == 31
    assert candidate(banned = [5, 10, 15, 20, 25],n = 30,maxSum = 200) == 17
    assert candidate(banned = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],n = 100,maxSum = 2500) == 63
    assert candidate(banned = [10, 20, 30, 40, 50],n = 60,maxSum = 1770) == 55
    assert candidate(banned = [10000],n = 10000,maxSum = 10000000) == 4471
    assert candidate(banned = [50, 51, 52, 53, 54, 55],n = 100,maxSum = 2500) == 68
    assert candidate(banned = [20, 40, 60, 80, 100],n = 100,maxSum = 500) == 30
    assert candidate(banned = [1, 3, 5, 7, 9],n = 15,maxSum = 60) == 7
    assert candidate(banned = [2500, 5000, 7500],n = 10000,maxSum = 25000000) == 7069
    assert candidate(banned = [1],n = 100,maxSum = 5050) == 99
    assert candidate(banned = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],n = 20,maxSum = 90) == 9
    assert candidate(banned = [1, 3, 5, 7, 9, 11, 13, 15],n = 15,maxSum = 100) == 7
