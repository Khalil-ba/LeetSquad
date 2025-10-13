# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(customers = [3, 1, 4, 2, 2],grumpy = [0, 0, 1, 1, 1],minutes = 1) == 8
    assert candidate(customers = [5, 5, 5, 5, 5],grumpy = [0, 0, 0, 0, 0],minutes = 1) == 25
    assert candidate(customers = [2, 3, 4, 5],grumpy = [1, 0, 1, 1],minutes = 2) == 12
    assert candidate(customers = [2, 3, 4, 5, 6],grumpy = [1, 0, 1, 0, 1],minutes = 2) == 14
    assert candidate(customers = [2, 3, 4, 5],grumpy = [1, 0, 1, 0],minutes = 2) == 12
    assert candidate(customers = [10, 20, 30, 40, 50],grumpy = [0, 1, 0, 1, 0],minutes = 1) == 130
    assert candidate(customers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 5) == 25
    assert candidate(customers = [2, 4, 2, 5, 0],grumpy = [0, 1, 0, 1, 1],minutes = 2) == 9
    assert candidate(customers = [1, 2, 3, 4, 5],grumpy = [1, 0, 1, 0, 1],minutes = 4) == 14
    assert candidate(customers = [5, 5, 5, 5, 5, 5],grumpy = [1, 1, 1, 1, 1, 1],minutes = 2) == 10
    assert candidate(customers = [10, 1, 2, 3, 4, 5],grumpy = [1, 0, 1, 0, 1, 0],minutes = 2) == 19
    assert candidate(customers = [1, 0, 1, 2, 1, 1, 7, 5],grumpy = [0, 1, 0, 1, 0, 1, 0, 1],minutes = 3) == 16
    assert candidate(customers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 5) == 50
    assert candidate(customers = [1],grumpy = [0],minutes = 1) == 1
    assert candidate(customers = [2, 3, 4, 5],grumpy = [1, 1, 1, 1],minutes = 2) == 9
    assert candidate(customers = [10, 20, 30, 40, 50],grumpy = [0, 1, 0, 1, 0],minutes = 4) == 150
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grumpy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],minutes = 5) == 55
    assert candidate(customers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 1) == 10
    assert candidate(customers = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],grumpy = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],minutes = 4) == 8
    assert candidate(customers = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 7) == 1140
    assert candidate(customers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],grumpy = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],minutes = 3) == 60
    assert candidate(customers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 5) == 35
    assert candidate(customers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 10) == 550
    assert candidate(customers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],grumpy = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],minutes = 5) == 45
    assert candidate(customers = [90, 0, 40, 0, 20, 0, 70, 0, 50, 0, 10, 0, 30, 0, 60, 0, 80, 0, 100, 0],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 5) == 240
    assert candidate(customers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grumpy = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],minutes = 5) == 4500
    assert candidate(customers = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0, 111, 222, 333, 444, 555],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],minutes = 7) == 6438
    assert candidate(customers = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 4) == 500
    assert candidate(customers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 10) == 100
    assert candidate(customers = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],minutes = 7) == 828
    assert candidate(customers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],grumpy = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],minutes = 6) == 770
    assert candidate(customers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],grumpy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],minutes = 10) == 20
    assert candidate(customers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 7) == 110
    assert candidate(customers = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 3) == 4300
    assert candidate(customers = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1],grumpy = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],minutes = 5) == 25
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 7) == 108
    assert candidate(customers = [30, 20, 10, 0, 5, 15, 25, 35, 45, 55],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 5) == 200
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],grumpy = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],minutes = 5) == 105
    assert candidate(customers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],grumpy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],minutes = 10) == 45
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 2) == 19
    assert candidate(customers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 5) == 490
    assert candidate(customers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 9) == 1850
    assert candidate(customers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],grumpy = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],minutes = 8) == 354
    assert candidate(customers = [50, 25, 75, 100, 50, 25, 75, 100, 50, 25, 75, 100],grumpy = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],minutes = 4) == 600
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grumpy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 7) == 174
    assert candidate(customers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 6) == 189
    assert candidate(customers = [5, 3, 8, 2, 10, 15, 7, 1, 4, 6],grumpy = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1],minutes = 4) == 47
    assert candidate(customers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grumpy = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],minutes = 3) == 4000
    assert candidate(customers = [3, 5, 0, 4, 7, 9, 6, 2, 5, 8],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 4) == 34
    assert candidate(customers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],grumpy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],minutes = 3) == 45
    assert candidate(customers = [200, 150, 100, 50, 0, 50, 100, 150, 200],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 3) == 700
    assert candidate(customers = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 5) == 10
    assert candidate(customers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 3) == 79
    assert candidate(customers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 3) == 60
    assert candidate(customers = [5, 1, 3, 4, 6, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15],grumpy = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],minutes = 6) == 99
    assert candidate(customers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],grumpy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],minutes = 5) == 20
    assert candidate(customers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 5) == 5100
    assert candidate(customers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 8) == 16800
    assert candidate(customers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 10) == 75
    assert candidate(customers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 2) == 390
    assert candidate(customers = [50, 20, 30, 10, 40, 60, 70, 80, 90, 100, 110, 120],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 4) == 610
    assert candidate(customers = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 10) == 75
    assert candidate(customers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 5) == 130
    assert candidate(customers = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],grumpy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],minutes = 2) == 27500
    assert candidate(customers = [10, 0, 5, 2, 3, 8, 6, 4, 7, 9],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 5) == 52
    assert candidate(customers = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 6) == 197
    assert candidate(customers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 6) == 90
    assert candidate(customers = [100, 200, 0, 300, 400, 0, 500, 0, 600, 700],grumpy = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0],minutes = 5) == 2400
    assert candidate(customers = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 3) == 15
    assert candidate(customers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 9) == 925
    assert candidate(customers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 2) == 0
    assert candidate(customers = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 3) == 11
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 3) == 90
    assert candidate(customers = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 10) == 1
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 2) == 19
    assert candidate(customers = [200, 300, 400, 500, 600, 700, 800, 900, 1000],grumpy = [1, 1, 0, 0, 1, 1, 0, 0, 1],minutes = 4) == 4300
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 4) == 90
    assert candidate(customers = [9, 8, 7, 6, 5, 4, 3, 2, 1],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 3) == 36
    assert candidate(customers = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 4) == 140
    assert candidate(customers = [23, 15, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 7) == 264
    assert candidate(customers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 5) == 5100
    assert candidate(customers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grumpy = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],minutes = 6) == 154
    assert candidate(customers = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 10) == 197
    assert candidate(customers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000],grumpy = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],minutes = 10) == 1000
    assert candidate(customers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 5) == 5100
    assert candidate(customers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 5) == 255
    assert candidate(customers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],grumpy = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],minutes = 5) == 8000
    assert candidate(customers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grumpy = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],minutes = 5) == 510
    assert candidate(customers = [5, 1, 3, 0, 2, 7, 8, 9, 10, 1],grumpy = [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],minutes = 4) == 38
