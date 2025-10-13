# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [1],k = 1) == 1
    assert candidate(arr = [-1, 0, 1],k = 3) == 1
    assert candidate(arr = [1, -2, 1],k = 5) == 2
    assert candidate(arr = [3, -2, 2, -3],k = 3) == 3
    assert candidate(arr = [10000, -10000],k = 2) == 10000
    assert candidate(arr = [10000, -10000],k = 100000) == 10000
    assert candidate(arr = [-10000, 10000],k = 100000) == 10000
    assert candidate(arr = [5, -1, 5],k = 3) == 27
    assert candidate(arr = [-1],k = 1) == 0
    assert candidate(arr = [0, 0, 0],k = 100000) == 0
    assert candidate(arr = [-1, -2, -3, -4, -5],k = 1) == 0
    assert candidate(arr = [3, -2, 2, -3],k = 5) == 3
    assert candidate(arr = [5],k = 1) == 5
    assert candidate(arr = [1, 2],k = 3) == 9
    assert candidate(arr = [1, 2, 3, 4, 5],k = 1) == 15
    assert candidate(arr = [0, 0, 0],k = 1) == 0
    assert candidate(arr = [1, -1, 1, -1, 1, -1],k = 100000) == 1
    assert candidate(arr = [1, -10, 1],k = 1) == 1
    assert candidate(arr = [5],k = 10) == 50
    assert candidate(arr = [-1, -2],k = 7) == 0
    assert candidate(arr = [1, -1],k = 200000) == 1
    assert candidate(arr = [1, 1, 1],k = 100000) == 300000
    assert candidate(arr = [-5],k = 1) == 0
    assert candidate(arr = [10000, -9999],k = 2) == 10001
    assert candidate(arr = [10000, -10000, 20000, -20000, 30000],k = 20) == 600000
    assert candidate(arr = [5, -1, 3, -2, 5],k = 10) == 100
    assert candidate(arr = [1, 2, 3, 4, 5],k = 1) == 15
    assert candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 540
    assert candidate(arr = [-5, -1, -8, -9],k = 4) == 0
    assert candidate(arr = [-1, -2, -3, -4, -5],k = 50000) == 0
    assert candidate(arr = [-10, 5, -5, 10, -10, 5],k = 7) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 275
    assert candidate(arr = [100, -50, 200, -150, 300, -250, 400, -350, 500, -450],k = 7) == 2200
    assert candidate(arr = [0, 0, 0, 0, 0],k = 100000) == 0
    assert candidate(arr = [-10, -20, -30, -40, -50],k = 2) == 0
    assert candidate(arr = [10, -9, 10, -9, 10, -9, 10, -9, 10, -9],k = 50000) == 250009
    assert candidate(arr = [7, -2, 5, -1, 3, -3, 2, 1],k = 100) == 1200
    assert candidate(arr = [5, -1, 5],k = 100000) == 900000
    assert candidate(arr = [3, -4, 2, -3, -1, 7, -5],k = 10) == 7
    assert candidate(arr = [-10, 100, -1, 100, -100],k = 2) == 288
    assert candidate(arr = [-5, -3, -1, 2, 4, 6],k = 2) == 15
    assert candidate(arr = [1, 2, -3, 4, -5, 6],k = 100000) == 500001
    assert candidate(arr = [100, -200, 300, -400, 500],k = 1000) == 300200
    assert candidate(arr = [2, -1, 2, -1, 2],k = 200000) == 800000
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 100000) == 0
    assert candidate(arr = [5, -1, 5],k = 10) == 90
    assert candidate(arr = [-10, 9, -20, 10, -30, 20, -40, 30, -50, 40],k = 5) == 40
    assert candidate(arr = [1000, -1000, 2000, -2000, 3000, -3000],k = 50000) == 3000
    assert candidate(arr = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 100000) == 1
    assert candidate(arr = [5, -1, 2, 3, -2],k = 10) == 72
    assert candidate(arr = [5, -1, 3, -4, 2],k = 10) == 52
    assert candidate(arr = [5, -1, 3, -4, 2, 6, -5],k = 10) == 65
    assert candidate(arr = [10, -3, 4, -2, -1, 10],k = 7) == 126
    assert candidate(arr = [-5, -1, -2, -3, -2],k = 4) == 0
    assert candidate(arr = [-5, -1, -8, -2, -4],k = 50000) == 0
    assert candidate(arr = [10000, -9999, 10000, -9999],k = 50000) == 109999
    assert candidate(arr = [-10000, 10000, -9999, 9999, -9998, 9998],k = 50000) == 10000
    assert candidate(arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 100000) == 0
    assert candidate(arr = [0, 0, 0, 0, 0, 0, 0],k = 100000) == 0
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 550
    assert candidate(arr = [-5, 5, -10, 10, -15, 15],k = 3) == 15
    assert candidate(arr = [-1, 0, 1],k = 100000) == 1
    assert candidate(arr = [10000, -5000, 2000, -3000, 1000],k = 50000) == 250005000
    assert candidate(arr = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 50000) == 1
    assert candidate(arr = [10000, -9999, 10000, -9999, 10000],k = 50000) == 500100000
    assert candidate(arr = [1, -3, 2, 1, -1],k = 1) == 3
    assert candidate(arr = [10, 20, 30, 40, 50],k = 100000) == 15000000
    assert candidate(arr = [10000, -9999],k = 10) == 10009
    assert candidate(arr = [5, -3, 5, -2, 4, -1],k = 10) == 81
    assert candidate(arr = [0, 0, 0, 0, 0],k = 50000) == 0
    assert candidate(arr = [-1, -2, -3, -4],k = 3) == 0
    assert candidate(arr = [100, -1, 1, -1, 1, -1, 100],k = 5) == 995
    assert candidate(arr = [10, -20, 10, -20, 10],k = 4) == 20
    assert candidate(arr = [-1, -2, -3, -4, -5],k = 100000) == 0
    assert candidate(arr = [-10, 1, -2, 3, -4, 5, -6, 7, -8, 9],k = 3) == 9
    assert candidate(arr = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 100000) == 999999937
    assert candidate(arr = [1, -1, 1, -1, 1],k = 5) == 5
    assert candidate(arr = [0, 0, 0, 0],k = 100000) == 0
    assert candidate(arr = [1, -1, 1, -1, 1],k = 100000) == 100000
    assert candidate(arr = [1, -1, 1, -1, 1],k = 99999) == 99999
    assert candidate(arr = [-5, -4, -3, -2, -1],k = 50000) == 0
    assert candidate(arr = [-1, 0, -2],k = 3) == 0
    assert candidate(arr = [10, -3, 4, -1, -2, 1, 5, -3],k = 50) == 553
    assert candidate(arr = [-10, -20, -30, -40],k = 100000) == 0
    assert candidate(arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],k = 10) == 15
    assert candidate(arr = [-5, -1, -8, -9],k = 2) == 0
    assert candidate(arr = [7, 1, 5, -3, 6, 7],k = 7) == 161
    assert candidate(arr = [-1, -2, -3, -4, -5],k = 7) == 0
    assert candidate(arr = [10000, -10000, 10000, -10000],k = 10000) == 10000
    assert candidate(arr = [-1, -2, -3, -4, -5],k = 2) == 0
    assert candidate(arr = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 50000) == 10000
    assert candidate(arr = [10, -9, 1, 2, 3],k = 50000) == 350003
    assert candidate(arr = [10000, -9999, 10000, -9999, 10000],k = 100000) == 199993
    assert candidate(arr = [100, -50, 25, -25, 10],k = 6) == 400
    assert candidate(arr = [5, -3, 5, -2, 1, 3],k = 10) == 90
    assert candidate(arr = [5, -3, 5, -2, 7, -1],k = 4) == 45
    assert candidate(arr = [-1, 4, -2, 3, -2],k = 100000) == 200003
    assert candidate(arr = [5, -4, 6, -3, 4],k = 10) == 80
    assert candidate(arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 5) == 0
    assert candidate(arr = [10000, -9999],k = 10000) == 19999
    assert candidate(arr = [10000, -9999, 9998, -9997, 9996, -9995, 9994, -9993, 9992, -9991],k = 5000) == 34995
    assert candidate(arr = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 100) == 50
    assert candidate(arr = [1, -1, 1, -1, 1, -1, 1],k = 100000) == 100000
    assert candidate(arr = [9, -4, 5, 1, -2, -3, 7],k = 100) == 1300
    assert candidate(arr = [-1, -2, -3, -4, -5],k = 3) == 0
    assert candidate(arr = [-5, -2, -3, -1],k = 3) == 0
