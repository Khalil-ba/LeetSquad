# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(price = [10, 10, 10, 10, 10],tastiness = [1, 2, 3, 4, 5],maxAmount = 15,maxCoupons = 3) == 12
    assert candidate(price = [1, 2, 3, 4, 5],tastiness = [5, 4, 3, 2, 1],maxAmount = 10,maxCoupons = 2) == 15
    assert candidate(price = [1000, 500, 250, 125, 62],tastiness = [5, 10, 15, 20, 25],maxAmount = 1000,maxCoupons = 5) == 75
    assert candidate(price = [100, 100, 100, 100, 100],tastiness = [50, 50, 50, 50, 50],maxAmount = 250,maxCoupons = 2) == 150
    assert candidate(price = [1, 2, 3, 4, 5],tastiness = [10, 20, 30, 40, 50],maxAmount = 10,maxCoupons = 2) == 150
    assert candidate(price = [5, 5, 5],tastiness = [10, 10, 10],maxAmount = 10,maxCoupons = 0) == 20
    assert candidate(price = [1, 2, 3, 4, 5],tastiness = [10, 20, 30, 40, 50],maxAmount = 10,maxCoupons = 3) == 150
    assert candidate(price = [1000, 1000, 1000],tastiness = [1000, 1000, 1000],maxAmount = 1000,maxCoupons = 1) == 1000
    assert candidate(price = [5, 10, 15],tastiness = [3, 6, 9],maxAmount = 15,maxCoupons = 0) == 9
    assert candidate(price = [100, 200, 300],tastiness = [50, 60, 70],maxAmount = 150,maxCoupons = 1) == 70
    assert candidate(price = [10, 15, 7],tastiness = [5, 8, 20],maxAmount = 10,maxCoupons = 2) == 28
    assert candidate(price = [1, 2, 3, 4, 5],tastiness = [10, 20, 30, 40, 50],maxAmount = 15,maxCoupons = 3) == 150
    assert candidate(price = [10, 20, 20],tastiness = [5, 8, 8],maxAmount = 20,maxCoupons = 1) == 13
    assert candidate(price = [5, 5, 5, 5, 5],tastiness = [1, 1, 1, 1, 1],maxAmount = 10,maxCoupons = 0) == 2
    assert candidate(price = [5, 5, 5, 5],tastiness = [1, 2, 3, 4],maxAmount = 10,maxCoupons = 0) == 7
    assert candidate(price = [10, 10, 10, 10],tastiness = [1, 2, 3, 4],maxAmount = 20,maxCoupons = 2) == 9
    assert candidate(price = [10, 10, 10, 10, 10],tastiness = [1, 2, 3, 4, 5],maxAmount = 30,maxCoupons = 3) == 14
    assert candidate(price = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],tastiness = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maxAmount = 5,maxCoupons = 5) == 10
    assert candidate(price = [50, 50, 50, 50, 50],tastiness = [1, 1, 1, 1, 1],maxAmount = 150,maxCoupons = 3) == 4
    assert candidate(price = [100, 200, 300],tastiness = [50, 100, 150],maxAmount = 500,maxCoupons = 1) == 300
    assert candidate(price = [100, 200, 300],tastiness = [10, 20, 30],maxAmount = 150,maxCoupons = 1) == 30
    assert candidate(price = [100, 200, 300],tastiness = [10, 20, 30],maxAmount = 300,maxCoupons = 2) == 50
    assert candidate(price = [300, 200, 100],tastiness = [150, 100, 50],maxAmount = 300,maxCoupons = 2) == 250
    assert candidate(price = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],tastiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxAmount = 200,maxCoupons = 5) == 450
    assert candidate(price = [7, 14, 21, 28, 35],tastiness = [3, 6, 9, 12, 15],maxAmount = 50,maxCoupons = 3) == 39
    assert candidate(price = [20, 30, 40, 50, 60, 70],tastiness = [3, 4, 5, 6, 7, 8],maxAmount = 120,maxCoupons = 3) == 25
    assert candidate(price = [20, 30, 40, 50, 60, 70],tastiness = [10, 20, 30, 40, 50, 60],maxAmount = 150,maxCoupons = 3) == 190
    assert candidate(price = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],maxAmount = 50,maxCoupons = 10) == 155
    assert candidate(price = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxAmount = 250,maxCoupons = 3) == 49
    assert candidate(price = [200, 100, 300, 400, 500, 600, 700, 800, 900, 1000],tastiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],maxAmount = 1500,maxCoupons = 4) == 3000
    assert candidate(price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],maxAmount = 200,maxCoupons = 5) == 321
    assert candidate(price = [100, 200, 300, 400, 500],tastiness = [10, 20, 30, 40, 50],maxAmount = 700,maxCoupons = 3) == 130
    assert candidate(price = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],maxAmount = 400,maxCoupons = 3) == 130
    assert candidate(price = [150, 100, 75, 200, 125],tastiness = [15, 10, 7, 20, 12],maxAmount = 250,maxCoupons = 2) == 42
    assert candidate(price = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tastiness = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],maxAmount = 200,maxCoupons = 1) == 450
    assert candidate(price = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],tastiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],maxAmount = 1000,maxCoupons = 5) == 4000
    assert candidate(price = [50, 75, 100, 25, 125, 150, 75, 100],tastiness = [15, 25, 35, 5, 40, 45, 20, 25],maxAmount = 250,maxCoupons = 4) == 150
    assert candidate(price = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],maxAmount = 300,maxCoupons = 2) == 185
    assert candidate(price = [15, 25, 35, 45, 55, 65, 75],tastiness = [5, 8, 10, 12, 15, 20, 25],maxAmount = 120,maxCoupons = 4) == 72
    assert candidate(price = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],tastiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],maxAmount = 500,maxCoupons = 4) == 147
    assert candidate(price = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],tastiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxAmount = 500,maxCoupons = 5) == 100
    assert candidate(price = [120, 130, 140, 150, 160, 170, 180, 190, 200, 210],tastiness = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],maxAmount = 300,maxCoupons = 2) == 1900
    assert candidate(price = [12, 24, 36, 48, 60],tastiness = [1, 3, 5, 7, 9],maxAmount = 80,maxCoupons = 2) == 19
    assert candidate(price = [10, 20, 30, 40, 50],tastiness = [5, 10, 15, 20, 25],maxAmount = 100,maxCoupons = 2) == 70
    assert candidate(price = [30, 60, 90, 120, 150, 180],tastiness = [10, 20, 30, 40, 50, 60],maxAmount = 300,maxCoupons = 4) == 190
    assert candidate(price = [20, 40, 50, 30, 60],tastiness = [15, 20, 25, 10, 30],maxAmount = 100,maxCoupons = 2) == 75
    assert candidate(price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],tastiness = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],maxAmount = 30,maxCoupons = 2) == 92
    assert candidate(price = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],tastiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxAmount = 500,maxCoupons = 5) == 490
    assert candidate(price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tastiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxAmount = 50,maxCoupons = 3) == 550
    assert candidate(price = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxAmount = 1000,maxCoupons = 5) == 54
    assert candidate(price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],tastiness = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],maxAmount = 50,maxCoupons = 3) == 165
    assert candidate(price = [50, 100, 150, 200, 250],tastiness = [50, 100, 150, 200, 250],maxAmount = 500,maxCoupons = 2) == 700
    assert candidate(price = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxAmount = 150,maxCoupons = 3) == 28
    assert candidate(price = [200, 150, 100, 50, 25],tastiness = [1, 2, 3, 4, 5],maxAmount = 250,maxCoupons = 3) == 14
    assert candidate(price = [90, 80, 70, 60, 50, 40, 30, 20, 10],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45],maxAmount = 200,maxCoupons = 2) == 195
    assert candidate(price = [20, 30, 40, 50, 60, 70, 80, 90, 100],tastiness = [1, 3, 5, 7, 9, 11, 13, 15, 17],maxAmount = 300,maxCoupons = 4) == 73
    assert candidate(price = [120, 150, 180, 200, 220, 250, 280, 300, 320, 350],tastiness = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],maxAmount = 500,maxCoupons = 5) == 180
    assert candidate(price = [90, 80, 70, 60, 50, 40, 30, 20, 10, 5],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],maxAmount = 100,maxCoupons = 2) == 200
    assert candidate(price = [50, 40, 30, 20, 10],tastiness = [1, 2, 3, 4, 5],maxAmount = 80,maxCoupons = 4) == 15
    assert candidate(price = [100, 200, 300, 400, 500],tastiness = [10, 20, 30, 40, 50],maxAmount = 800,maxCoupons = 3) == 140
    assert candidate(price = [100, 200, 150, 50, 300],tastiness = [50, 80, 60, 30, 100],maxAmount = 300,maxCoupons = 2) == 210
    assert candidate(price = [10, 20, 30, 40, 50],tastiness = [5, 15, 25, 35, 45],maxAmount = 80,maxCoupons = 2) == 105
    assert candidate(price = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],tastiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxAmount = 50,maxCoupons = 5) == 490
    assert candidate(price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],maxAmount = 200,maxCoupons = 4) == 275
    assert candidate(price = [10, 20, 30, 40, 50],tastiness = [5, 10, 15, 20, 25],maxAmount = 100,maxCoupons = 2) == 70
    assert candidate(price = [50, 75, 100, 125, 150],tastiness = [10, 20, 30, 40, 50],maxAmount = 200,maxCoupons = 2) == 100
    assert candidate(price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],maxAmount = 100,maxCoupons = 4) == 185
    assert candidate(price = [30, 60, 90, 120, 150],tastiness = [30, 60, 90, 120, 150],maxAmount = 300,maxCoupons = 3) == 450
    assert candidate(price = [50, 25, 100, 75, 125],tastiness = [8, 5, 15, 10, 20],maxAmount = 200,maxCoupons = 2) == 48
    assert candidate(price = [5, 15, 25, 35, 45],tastiness = [1, 2, 3, 4, 5],maxAmount = 50,maxCoupons = 2) == 10
    assert candidate(price = [30, 45, 55, 60, 70],tastiness = [5, 7, 9, 11, 13],maxAmount = 100,maxCoupons = 2) == 29
    assert candidate(price = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],maxAmount = 150,maxCoupons = 3) == 170
    assert candidate(price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tastiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],maxAmount = 15,maxCoupons = 3) == 45
    assert candidate(price = [100, 200, 300, 400, 500],tastiness = [5, 10, 15, 20, 25],maxAmount = 600,maxCoupons = 3) == 60
    assert candidate(price = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maxAmount = 100,maxCoupons = 3) == 75
    assert candidate(price = [20, 30, 40, 50],tastiness = [100, 200, 300, 400],maxAmount = 80,maxCoupons = 1) == 700
    assert candidate(price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],tastiness = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],maxAmount = 15,maxCoupons = 1) == 40
    assert candidate(price = [50, 40, 30, 20, 10, 5, 1, 2, 3, 4, 5],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],maxAmount = 100,maxCoupons = 5) == 330
    assert candidate(price = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tastiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxAmount = 200,maxCoupons = 4) == 370
    assert candidate(price = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],tastiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],maxAmount = 200,maxCoupons = 5) == 97
    assert candidate(price = [8, 16, 24, 32, 40],tastiness = [4, 8, 12, 16, 20],maxAmount = 60,maxCoupons = 3) == 52
    assert candidate(price = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],maxAmount = 150,maxCoupons = 5) == 29
    assert candidate(price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],tastiness = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],maxAmount = 20,maxCoupons = 2) == 75
    assert candidate(price = [150, 200, 250, 300, 350, 400],tastiness = [50, 100, 150, 200, 250, 300],maxAmount = 600,maxCoupons = 4) == 800
    assert candidate(price = [30, 60, 90, 120, 150],tastiness = [20, 40, 60, 80, 100],maxAmount = 150,maxCoupons = 2) == 180
    assert candidate(price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxAmount = 100,maxCoupons = 5) == 40
    assert candidate(price = [30, 60, 90, 120, 150],tastiness = [15, 30, 45, 60, 75],maxAmount = 200,maxCoupons = 2) == 165
    assert candidate(price = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maxAmount = 150,maxCoupons = 5) == 65
    assert candidate(price = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],tastiness = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],maxAmount = 150,maxCoupons = 3) == 155
    assert candidate(price = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxAmount = 30,maxCoupons = 5) == 40
    assert candidate(price = [10, 20, 30, 40, 50],tastiness = [1, 4, 9, 16, 25],maxAmount = 60,maxCoupons = 1) == 34
    assert candidate(price = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxAmount = 50,maxCoupons = 2) == 10
    assert candidate(price = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],tastiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxAmount = 500,maxCoupons = 3) == 330
    assert candidate(price = [20, 40, 60, 80, 100],tastiness = [15, 25, 35, 45, 55],maxAmount = 200,maxCoupons = 3) == 175
    assert candidate(price = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],tastiness = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],maxAmount = 250,maxCoupons = 5) == 47
    assert candidate(price = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750],tastiness = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maxAmount = 1500,maxCoupons = 5) == 60
    assert candidate(price = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],tastiness = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxAmount = 200,maxCoupons = 3) == 330
    assert candidate(price = [7, 14, 21, 28, 35, 42],tastiness = [2, 4, 6, 8, 10, 12],maxAmount = 50,maxCoupons = 3) == 28
    assert candidate(price = [20, 40, 60, 80, 100],tastiness = [10, 20, 30, 40, 50],maxAmount = 120,maxCoupons = 1) == 80
    assert candidate(price = [30, 50, 20, 60, 40],tastiness = [10, 20, 30, 40, 50],maxAmount = 100,maxCoupons = 2) == 130
    assert candidate(price = [10, 20, 30, 40, 50],tastiness = [3, 5, 7, 10, 12],maxAmount = 70,maxCoupons = 2) == 27
    assert candidate(price = [5, 15, 25, 35, 45],tastiness = [10, 20, 30, 40, 50],maxAmount = 50,maxCoupons = 0) == 60
    assert candidate(price = [40, 80, 120, 160, 200, 240, 280, 320],tastiness = [2, 4, 6, 8, 10, 12, 14, 16],maxAmount = 200,maxCoupons = 5) == 20
    assert candidate(price = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],tastiness = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],maxAmount = 400,maxCoupons = 4) == 310
    assert candidate(price = [10, 20, 30, 40, 50],tastiness = [1, 2, 3, 4, 5],maxAmount = 100,maxCoupons = 2) == 14
    assert candidate(price = [10, 20, 30, 40, 50],tastiness = [5, 10, 15, 20, 25],maxAmount = 60,maxCoupons = 2) == 50
    assert candidate(price = [30, 20, 10, 40, 50],tastiness = [8, 5, 3, 10, 12],maxAmount = 50,maxCoupons = 1) == 18
    assert candidate(price = [15, 25, 35, 45, 55],tastiness = [10, 20, 30, 40, 50],maxAmount = 150,maxCoupons = 3) == 150
    assert candidate(price = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],tastiness = [250, 225, 200, 175, 150, 125, 100, 75, 50, 25],maxAmount = 500,maxCoupons = 2) == 1125
    assert candidate(price = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],tastiness = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],maxAmount = 100,maxCoupons = 2) == 220
    assert candidate(price = [10, 15, 20, 25, 30],tastiness = [5, 10, 15, 20, 25],maxAmount = 60,maxCoupons = 1) == 60
