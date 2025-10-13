# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(costs = [10, 10, 10, 10, 10],k = 4,candidates = 2) == 40
    assert candidate(costs = [10, 10, 10, 10, 10],k = 5,candidates = 5) == 50
    assert candidate(costs = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5,candidates = 5) == 10
    assert candidate(costs = [5, 4, 3, 2, 1],k = 5,candidates = 1) == 15
    assert candidate(costs = [5, 4, 3, 2, 1],k = 3,candidates = 1) == 6
    assert candidate(costs = [5, 5, 5, 5],k = 2,candidates = 2) == 10
    assert candidate(costs = [10, 20, 30, 40, 50],k = 5,candidates = 5) == 150
    assert candidate(costs = [17, 12, 10, 2, 7, 2, 11, 20, 8],k = 3,candidates = 4) == 11
    assert candidate(costs = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 10,candidates = 10) == 90
    assert candidate(costs = [3, 2, 7, 7, 1, 2],k = 2,candidates = 2) == 3
    assert candidate(costs = [10, 20, 30, 40, 50],k = 2,candidates = 3) == 30
    assert candidate(costs = [1, 2, 4, 1],k = 3,candidates = 3) == 4
    assert candidate(costs = [10, 20, 30, 40, 50],k = 3,candidates = 1) == 60
    assert candidate(costs = [5, 4, 3, 2, 1],k = 2,candidates = 1) == 3
    assert candidate(costs = [25, 15, 30, 20, 10],k = 4,candidates = 2) == 70
    assert candidate(costs = [31, 25, 72, 79, 74],k = 3,candidates = 2) == 128
    assert candidate(costs = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5,candidates = 3) == 150
    assert candidate(costs = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 7,candidates = 3) == 280
    assert candidate(costs = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9,candidates = 4) == 45
    assert candidate(costs = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],k = 15,candidates = 15) == 300
    assert candidate(costs = [50, 20, 30, 40, 10, 60, 70, 80, 90, 100],k = 6,candidates = 4) == 210
    assert candidate(costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10,candidates = 4) == 55
    assert candidate(costs = [1, 3, 2, 4, 5, 7, 6, 8, 10, 9, 11, 13, 12, 14, 15],k = 8,candidates = 4) == 36
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,candidates = 3) == 5
    assert candidate(costs = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15,candidates = 6) == 80
    assert candidate(costs = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 10,candidates = 3) == 955
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,candidates = 6) == 55
    assert candidate(costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15,candidates = 8) == 120
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10,candidates = 5) == 31
    assert candidate(costs = [10, 20, 30, 15, 25, 5, 40, 35, 2, 1],k = 5,candidates = 3) == 33
    assert candidate(costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10,candidates = 2) == 55
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,candidates = 5) == 10
    assert candidate(costs = [9, 7, 5, 3, 1, 1, 3, 5, 7, 9, 9, 7, 5, 3, 1, 1, 3, 5, 7, 9],k = 10,candidates = 5) == 26
    assert candidate(costs = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 7,candidates = 3) == 28
    assert candidate(costs = [50, 20, 30, 10, 40, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10,candidates = 4) == 550
    assert candidate(costs = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 10,candidates = 5) == 110
    assert candidate(costs = [5, 3, 8, 6, 2, 7, 4, 1, 10, 15, 20, 25, 30],k = 8,candidates = 4) == 36
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 6,candidates = 5) == 210
    assert candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 7,candidates = 8) == 2800
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10,candidates = 5) == 55
    assert candidate(costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,candidates = 10) == 55
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7,candidates = 4) == 280
    assert candidate(costs = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],k = 15,candidates = 7) == 255
    assert candidate(costs = [5, 3, 8, 6, 2, 7, 4, 1],k = 4,candidates = 4) == 10
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15,candidates = 4) == 120
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],k = 15,candidates = 10) == 1200
    assert candidate(costs = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7,candidates = 5) == 280
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,candidates = 3) == 150
    assert candidate(costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 7,candidates = 5) == 280
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 5,candidates = 3) == 150
    assert candidate(costs = [2, 1, 3, 4, 5, 6, 7, 8, 9],k = 5,candidates = 2) == 15
    assert candidate(costs = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],k = 8,candidates = 5) == 19
    assert candidate(costs = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 5,candidates = 2) == 15000
    assert candidate(costs = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5],k = 5,candidates = 2) == 15
    assert candidate(costs = [30, 20, 10, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10,candidates = 6) == 550
    assert candidate(costs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20,candidates = 10) == 400
    assert candidate(costs = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],k = 5,candidates = 2) == 150000
    assert candidate(costs = [30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165],k = 10,candidates = 5) == 305
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,candidates = 5) == 55
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,candidates = 1) == 10
    assert candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5,candidates = 2) == 50
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7,candidates = 6) == 280
    assert candidate(costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15,candidates = 7) == 205
    assert candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10,candidates = 5) == 100
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10,candidates = 5) == 55
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7,candidates = 5) == 280
    assert candidate(costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8,candidates = 5) == 36
    assert candidate(costs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 10,candidates = 6) == 110
    assert candidate(costs = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 12],k = 6,candidates = 4) == 21
    assert candidate(costs = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5,candidates = 2) == 50
    assert candidate(costs = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 15,candidates = 7) == 12222222
    assert candidate(costs = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 10,candidates = 1) == 5500
    assert candidate(costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5,candidates = 2) == 150
    assert candidate(costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5,candidates = 5) == 15
    assert candidate(costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,candidates = 3) == 150
    assert candidate(costs = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 5,candidates = 2) == 18
    assert candidate(costs = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],k = 10,candidates = 5) == 550000
    assert candidate(costs = [5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2],k = 10,candidates = 5) == 23
    assert candidate(costs = [5, 1, 4, 2, 3],k = 3,candidates = 1) == 9
    assert candidate(costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10,candidates = 5) == 55
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,candidates = 5) == 55
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,candidates = 5) == 10
    assert candidate(costs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15,candidates = 6) == 120
    assert candidate(costs = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 10,candidates = 10) == 1000
    assert candidate(costs = [5, 3, 8, 6, 2, 7, 4, 1],k = 4,candidates = 2) == 10
    assert candidate(costs = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 7,candidates = 4) == 700
    assert candidate(costs = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],k = 8,candidates = 4) == 19
    assert candidate(costs = [10, 5, 15, 20, 25, 30, 35, 40, 45, 50],k = 5,candidates = 3) == 75
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 25,candidates = 5) == 325
    assert candidate(costs = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3,candidates = 2) == 6
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,candidates = 2) == 10
    assert candidate(costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 15,candidates = 10) == 120
    assert candidate(costs = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],k = 5,candidates = 5) == 90
    assert candidate(costs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5,candidates = 3) == 1500
    assert candidate(costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15,candidates = 5) == 15
    assert candidate(costs = [8, 6, 4, 2, 0, 0, 2, 4, 6, 8, 8, 6, 4, 2, 0, 0, 2, 4, 6, 8],k = 5,candidates = 2) == 12
    assert candidate(costs = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5,candidates = 4) == 150
    assert candidate(costs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 10,candidates = 5) == 275
    assert candidate(costs = [1, 3, 2, 4, 5, 7, 6, 9, 8, 10, 12, 11, 14, 13, 15, 17, 16, 19, 18, 20],k = 10,candidates = 5) == 55
