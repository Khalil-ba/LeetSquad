# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(inventory = [10, 10, 10],orders = 5) == 48
    assert candidate(inventory = [3, 5],orders = 6) == 19
    assert candidate(inventory = [1, 2, 3, 4, 5],orders = 10) == 30
    assert candidate(inventory = [1, 1, 1, 1, 1],orders = 3) == 3
    assert candidate(inventory = [7],orders = 7) == 28
    assert candidate(inventory = [1000000000, 1000000000],orders = 1000000000) == 250000035
    assert candidate(inventory = [1000000000],orders = 1) == 1000000000
    assert candidate(inventory = [5, 5, 5, 5, 5],orders = 20) == 70
    assert candidate(inventory = [1000000000],orders = 1000000000) == 21
    assert candidate(inventory = [2, 5],orders = 4) == 14
    assert candidate(inventory = [100],orders = 10) == 955
    assert candidate(inventory = [9, 9, 9, 9, 9, 9],orders = 25) == 185
    assert candidate(inventory = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],orders = 350) == 4110
    assert candidate(inventory = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],orders = 5) == 5
    assert candidate(inventory = [100, 90, 80, 70, 60],orders = 200) == 12600
    assert candidate(inventory = [1000000, 2000000, 3000000],orders = 5000000) == 335785502
    assert candidate(inventory = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],orders = 100) == 500
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],orders = 50) == 215
    assert candidate(inventory = [1000, 2000, 3000, 4000, 5000],orders = 10000) == 25005000
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],orders = 55) == 220
    assert candidate(inventory = [5, 15, 25, 35, 45],orders = 35) == 1138
    assert candidate(inventory = [100000000, 100000000, 100000000],orders = 299999997) == 44999997
    assert candidate(inventory = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],orders = 50) == 150
    assert candidate(inventory = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],orders = 900) == 70200
    assert candidate(inventory = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],orders = 500) == 37750
    assert candidate(inventory = [1000000000, 500000000, 250000000, 125000000, 62500000],orders = 999999999) == 312500027
    assert candidate(inventory = [500000000, 400000000, 300000000, 200000000, 100000000],orders = 1500000000) == 825000014
    assert candidate(inventory = [100, 200, 300, 400, 500],orders = 1000) == 250500
    assert candidate(inventory = [100000000, 200000000, 300000000, 400000000, 500000000],orders = 900000000) == 778750014
    assert candidate(inventory = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],orders = 50) == 400
    assert candidate(inventory = [999999999, 999999999, 999999999, 999999999, 999999999],orders = 500000000) == 425000028
    assert candidate(inventory = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],orders = 500) == 37750
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],orders = 190) == 1520
    assert candidate(inventory = [50, 40, 30, 20, 10],orders = 100) == 2550
    assert candidate(inventory = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],orders = 1500) == 134972
    assert candidate(inventory = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],orders = 5000) == 1915000
    assert candidate(inventory = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],orders = 500) == 6080
    assert candidate(inventory = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],orders = 10) == 10
    assert candidate(inventory = [3, 5, 7, 9],orders = 15) == 79
    assert candidate(inventory = [1000000000, 1000000000, 1000000000, 1000000000],orders = 3000000000) == 375000084
    assert candidate(inventory = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],orders = 4500000) == 502241341
    assert candidate(inventory = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],orders = 550) == 19525
    assert candidate(inventory = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],orders = 10000) == 6071070
    assert candidate(inventory = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],orders = 1000) == 66330
    assert candidate(inventory = [1, 3, 5, 7, 9],orders = 15) == 79
    assert candidate(inventory = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],orders = 7500) == 5500000
    assert candidate(inventory = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],orders = 50) == 110
    assert candidate(inventory = [999999999, 999999999, 999999999, 999999999, 999999999],orders = 4999999995) == 140
    assert candidate(inventory = [10, 10, 20, 20, 30, 30],orders = 50) == 1012
    assert candidate(inventory = [30, 25, 20, 15, 10, 5, 0],orders = 75) == 1100
    assert candidate(inventory = [10, 20, 30, 40, 50],orders = 100) == 2550
    assert candidate(inventory = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],orders = 20) == 20
    assert candidate(inventory = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],orders = 10) == 10
    assert candidate(inventory = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],orders = 300) == 16124
    assert candidate(inventory = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],orders = 200) == 9100
    assert candidate(inventory = [10, 20, 30, 40, 50],orders = 50) == 1708
    assert candidate(inventory = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],orders = 1500) == 94500
    assert candidate(inventory = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],orders = 40) == 110
    assert candidate(inventory = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],orders = 100) == 715
    assert candidate(inventory = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],orders = 25000) == 144369642
    assert candidate(inventory = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9],orders = 1000000000) == 46
    assert candidate(inventory = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],orders = 40) == 200
    assert candidate(inventory = [10, 8, 6, 4, 2],orders = 15) == 94
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],orders = 45) == 210
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],orders = 50) == 465
    assert candidate(inventory = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],orders = 50) == 50
    assert candidate(inventory = [50, 20, 10, 5, 1],orders = 50) == 1375
    assert candidate(inventory = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],orders = 500) == 19375
    assert candidate(inventory = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],orders = 100) == 1155
    assert candidate(inventory = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],orders = 100) == 800
    assert candidate(inventory = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],orders = 10000) == 75005000
    assert candidate(inventory = [1000000000, 500000000, 250000000, 125000000, 62500000],orders = 1000000000) == 562500028
    assert candidate(inventory = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],orders = 1000000) == 499475
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],orders = 30) == 174
    assert candidate(inventory = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990],orders = 1000000000) == 350000124
    assert candidate(inventory = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],orders = 50) == 460
    assert candidate(inventory = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],orders = 1000) == 750500
    assert candidate(inventory = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],orders = 200) == 14627
    assert candidate(inventory = [1000000000, 1000000000, 1000000000, 1000000000],orders = 4000000000) == 84
    assert candidate(inventory = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],orders = 45) == 145
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],orders = 190) == 1520
    assert candidate(inventory = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],orders = 1000) == 175234
    assert candidate(inventory = [50, 40, 30, 20, 10],orders = 150) == 2825
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],orders = 150) == 1416
    assert candidate(inventory = [10, 20, 30, 40, 50],orders = 100) == 2550
    assert candidate(inventory = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],orders = 4999999995) == 100
    assert candidate(inventory = [500000000, 500000000, 500000000, 500000000, 500000000],orders = 2000000000) == 800000028
    assert candidate(inventory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],orders = 55) == 220
