# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(prices = [10, 20, 30, 40, 50],fee = 5) == 35
    assert candidate(prices = [1, 3, 2, 8, 4, 9],fee = 2) == 8
    assert candidate(prices = [1, 2, 3, 4, 5],fee = 1) == 3
    assert candidate(prices = [50, 40, 30, 20, 10],fee = 5) == 0
    assert candidate(prices = [5, 4, 3, 2, 1],fee = 1) == 0
    assert candidate(prices = [1, 2, 3, 4, 5],fee = 0) == 4
    assert candidate(prices = [10, 22, 5, 75, 65, 80],fee = 3) == 88
    assert candidate(prices = [1, 5, 1, 5, 1, 5, 1, 5],fee = 2) == 8
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4],fee = 2) == 2
    assert candidate(prices = [1, 2, 3, 4, 5, 0, 0, 0, 0, 6],fee = 3) == 4
    assert candidate(prices = [1, 3, 7, 5, 10, 3],fee = 3) == 6
    assert candidate(prices = [1, 3, 2, 1, 4, 5, 2, 11],fee = 1) == 12
    assert candidate(prices = [10, 5, 5, 5, 15, 5, 5, 20],fee = 3) == 19
    assert candidate(prices = [10, 10, 10, 10, 10],fee = 1) == 0
    assert candidate(prices = [1, 5, 1, 5, 1, 5, 1, 5, 1],fee = 2) == 8
    assert candidate(prices = [1, 3, 2, 4, 3, 5],fee = 1) == 3
    assert candidate(prices = [10, 1, 2, 7, 1, 3, 4, 10],fee = 2) == 11
    assert candidate(prices = [1, 5, 1, 5, 1, 5],fee = 2) == 6
    assert candidate(prices = [5, 4, 3, 2, 1],fee = 0) == 0
    assert candidate(prices = [1, 3, 2, 8, 4, 9, 2, 8, 4, 9, 2, 8, 4, 9],fee = 2) == 22
    assert candidate(prices = [100, 180, 260, 310, 40, 535, 695],fee = 100) == 665
    assert candidate(prices = [100, 180, 260, 310, 40, 535, 695, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],fee = 150) == 1325
    assert candidate(prices = [3, 15, 18, 14, 19, 20, 22, 17, 21, 23],fee = 5) == 15
    assert candidate(prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0],fee = 2) == 9
    assert candidate(prices = [90, 80, 70, 60, 50, 40, 30, 20, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],fee = 5) == 10
    assert candidate(prices = [100, 98, 95, 97, 96, 99, 101, 102, 100, 104, 105, 107, 108, 105, 109],fee = 4) == 10
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],fee = 1) == 6
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],fee = 20) == 130
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1],fee = 5) == 12
    assert candidate(prices = [10, 22, 5, 75, 65, 80],fee = 3) == 88
    assert candidate(prices = [10, 20, 15, 25, 10, 30, 5, 35, 40, 45],fee = 3) == 68
    assert candidate(prices = [1, 2, 5, 3, 8, 9, 2, 10, 3, 7, 15, 10, 20, 15, 25, 20, 30, 25, 35, 30],fee = 3) == 47
    assert candidate(prices = [1, 3, 7, 5, 10, 3, 15, 12, 18, 20, 5, 10, 15, 25, 30],fee = 4) == 39
    assert candidate(prices = [1, 2, 5, 3, 8, 9, 2, 10, 3, 7],fee = 2) == 14
    assert candidate(prices = [100, 180, 260, 40, 310, 535, 695],fee = 10) == 795
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],fee = 2) == 22
    assert candidate(prices = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],fee = 5) == 70
    assert candidate(prices = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],fee = 0) == 16
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50],fee = 10) == 30
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],fee = 1) == 0
    assert candidate(prices = [7, 9, 10, 11, 5, 3, 6, 8, 15, 20],fee = 2) == 17
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 5, 4, 5, 4, 5],fee = 1) == 3
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],fee = 1) == 8
    assert candidate(prices = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],fee = 1) == 4
    assert candidate(prices = [5, 3, 8, 12, 10, 14, 18, 15, 20, 25, 23, 28, 30],fee = 6) == 21
    assert candidate(prices = [8, 6, 4, 2, 10, 8, 6, 14, 12, 10, 18, 16, 14, 20, 18, 22],fee = 4) == 16
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],fee = 0) == 0
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 8, 2, 1, 5, 3, 6, 4, 8, 2, 1, 5, 3, 6, 4, 8, 2, 1, 5, 3, 6, 4, 8, 2, 1],fee = 2) == 20
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],fee = 0) == 9
    assert candidate(prices = [1, 7, 4, 11, 8, 16, 13, 20, 17, 25, 22, 30],fee = 5) == 24
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],fee = 10) == 0
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],fee = 5) == 8
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],fee = 2) == 0
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1],fee = 5) == 24
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],fee = 5) == 24
    assert candidate(prices = [30, 50, 10, 5, 100, 50, 20, 10, 5, 30, 200, 150, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],fee = 30) == 1100
    assert candidate(prices = [1, 4, 3, 2, 5, 6, 3, 7, 8, 2, 4, 9],fee = 3) == 8
    assert candidate(prices = [1, 2, 3, 0, 100, 2, 100, 3],fee = 50) == 98
    assert candidate(prices = [30, 25, 28, 32, 27, 35, 40, 38, 42, 45, 48, 47, 49, 50, 51, 52, 50, 53],fee = 7) == 21
    assert candidate(prices = [30, 28, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40],fee = 10) == 30
    assert candidate(prices = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],fee = 50) == 225
    assert candidate(prices = [7, 6, 4, 3, 1],fee = 1) == 0
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2],fee = 1) == 9
    assert candidate(prices = [10, 15, 12, 18, 14, 20, 16, 22, 18, 25],fee = 3) == 15
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 50, 40, 30, 20, 10, 50, 60, 70, 80, 90, 100, 50, 40, 30, 20, 10, 50],fee = 10) == 190
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],fee = 1) == 0
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4],fee = 2) == 2
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],fee = 0) == 8
    assert candidate(prices = [1, 2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8, 6, 7, 8, 9],fee = 2) == 6
    assert candidate(prices = [1, 7, 4, 11, 10, 5, 11, 5, 1, 5, 11, 5, 1, 5, 11, 5, 1, 5, 11, 5, 1, 5, 11, 5, 1, 5, 11, 5],fee = 5) == 31
    assert candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],fee = 5) == 25
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],fee = 1) == 0
    assert candidate(prices = [100, 98, 102, 97, 99, 103, 101, 98, 104, 106],fee = 4) == 6
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],fee = 2) == 0
    assert candidate(prices = [10, 22, 5, 75, 65, 80, 100, 90, 110],fee = 3) == 125
    assert candidate(prices = [8, 12, 10, 15, 20, 17, 22, 25, 30, 35, 28, 33, 40],fee = 5) == 29
    assert candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4],fee = 2) == 4
    assert candidate(prices = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],fee = 2) == 0
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1],fee = 1) == 0
    assert candidate(prices = [3, 2, 6, 5, 0, 3],fee = 2) == 3
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],fee = 1) == 13
    assert candidate(prices = [5, 2, 6, 1, 9, 4, 7, 3, 8, 5],fee = 3) == 8
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],fee = 1) == 0
    assert candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],fee = 10) == 0
    assert candidate(prices = [1, 2, 3, 10, 5, 6, 7, 100, 1, 2, 3, 10, 5, 6, 7, 100],fee = 10) == 178
    assert candidate(prices = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],fee = 6) == 10
    assert candidate(prices = [1, 10, 3, 100, 4, 101, 5, 102, 6, 103, 7, 104, 8, 105],fee = 5) == 556
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],fee = 5) == 85
    assert candidate(prices = [10, 11, 7, 10, 15, 10, 18, 20, 21, 10],fee = 4) == 11
    assert candidate(prices = [10, 15, 14, 20, 17, 22, 18, 25],fee = 5) == 10
    assert candidate(prices = [7, 6, 4, 3, 1, 8, 9, 10, 5, 4, 3, 2, 1, 10],fee = 2) == 14
    assert candidate(prices = [1, 4, 2, 6, 3, 7, 4, 8, 5, 9],fee = 2) == 9
    assert candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],fee = 1) == 24
    assert candidate(prices = [1, 4, 5, 6, 7, 8, 10, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],fee = 4) == 11
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],fee = 3) == 0
    assert candidate(prices = [10, 14, 13, 11, 5, 7, 9, 8, 10, 12, 15, 14, 20, 18],fee = 3) == 13
    assert candidate(prices = [8, 3, 6, 2, 8, 8, 8, 4, 2, 0, 4, 2, 2, 0, 0, 1, 8, 5, 5, 5, 0, 7, 7, 5, 0, 1, 1, 8, 5, 5, 6, 1, 1, 1, 0, 6, 5, 1, 1, 3, 5, 0, 0, 5, 3, 0, 6, 6, 6, 6, 5, 0, 4, 7, 0, 3, 1, 1, 7, 6, 6, 0, 1, 6, 5, 0, 1, 1, 7, 6, 1, 7, 0, 6, 5, 0, 1, 7, 5, 5, 6, 0, 0, 0, 1],fee = 4) == 36
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],fee = 1) == 13
    assert candidate(prices = [1, 10, 3, 15, 20, 18, 25, 27, 23, 30],fee = 7) == 22
    assert candidate(prices = [5, 2, 3, 7, 3, 9, 10, 4, 8, 10, 12, 15, 20, 18, 16, 14, 13, 11, 9, 7, 5, 3, 1],fee = 2) == 22
    assert candidate(prices = [1, 2, 5, 4, 8, 11, 10, 13, 12, 15, 18, 20],fee = 5) == 14
    assert candidate(prices = [10, 22, 5, 75, 65, 80, 90, 60, 70, 100, 110, 120, 130, 140, 150, 2, 3, 4, 5],fee = 10) == 157
    assert candidate(prices = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10],fee = 4) == 5
    assert candidate(prices = [10, 1, 1, 1, 1, 1, 10],fee = 1) == 8
    assert candidate(prices = [2, 5, 1, 6, 3, 7, 4, 8, 5, 9],fee = 2) == 10
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],fee = 1) == 8
    assert candidate(prices = [80, 70, 60, 50, 40, 30, 20, 10],fee = 5) == 0
