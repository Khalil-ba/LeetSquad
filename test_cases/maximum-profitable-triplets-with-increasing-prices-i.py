# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(prices = [3, 1, 2, 4],profits = [5, 6, 7, 8]) == 21
    assert candidate(prices = [100, 200, 300, 400],profits = [1000, 2000, 3000, 4000]) == 9000
    assert candidate(prices = [1, 2, 2, 2, 3],profits = [1, 2, 3, 4, 5]) == 10
    assert candidate(prices = [1, 2, 3, 4, 5],profits = [1, 5, 3, 4, 6]) == 15
    assert candidate(prices = [100, 101, 102],profits = [1000, 1001, 1002]) == 3003
    assert candidate(prices = [5, 6, 7, 8, 9],profits = [9, 8, 7, 6, 5]) == 24
    assert candidate(prices = [5, 5, 5, 5],profits = [1, 2, 3, 4]) == -1
    assert candidate(prices = [1, 1, 1],profits = [1, 1, 1]) == -1
    assert candidate(prices = [4, 3, 2, 1],profits = [33, 20, 19, 87]) == -1
    assert candidate(prices = [2, 3, 5, 7, 11],profits = [11, 7, 5, 3, 2]) == 23
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(prices = [10, 20, 30, 40, 50, 60],profits = [60, 50, 40, 30, 20, 10]) == 150
    assert candidate(prices = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [3, 1, 5, 2, 4],profits = [10, 20, 30, 40, 50]) == 110
    assert candidate(prices = [1, 2, 3],profits = [1000, 2000, 3000]) == 6000
    assert candidate(prices = [1, 2, 3],profits = [3, 2, 1]) == 6
    assert candidate(prices = [8, 6, 7, 5, 3, 0, 9],profits = [1, 2, 3, 4, 5, 6, 7]) == 12
    assert candidate(prices = [1, 3, 5, 7, 9],profits = [9, 7, 5, 3, 1]) == 21
    assert candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],profits = [5, 3, 8, 3, 9, 7, 9, 3, 2, 3, 8]) == 24
    assert candidate(prices = [1, 3, 2, 4, 5],profits = [5, 10, 6, 8, 3]) == 23
    assert candidate(prices = [3, 1, 4, 2, 5],profits = [50, 10, 40, 20, 30]) == 120
    assert candidate(prices = [5, 4, 3, 2, 1, 6],profits = [10, 20, 30, 40, 50, 60]) == -1
    assert candidate(prices = [10, 2, 3, 4],profits = [100, 2, 7, 10]) == 19
    assert candidate(prices = [1, 1, 1, 1, 1],profits = [1, 1, 1, 1, 1]) == -1
    assert candidate(prices = [3, 5, 2, 7, 6],profits = [50, 20, 40, 10, 30]) == 100
    assert candidate(prices = [1, 3, 5, 7, 9],profits = [1000, 2000, 3000, 4000, 5000]) == 12000
    assert candidate(prices = [5, 3, 7, 9, 2, 6, 8, 4],profits = [10, 20, 30, 40, 50, 60, 70, 80]) == 180
    assert candidate(prices = [100, 200, 300],profits = [50, 60, 70]) == 180
    assert candidate(prices = [1, 2, 100, 101, 102],profits = [1000, 1001, 1, 2, 3]) == 2004
    assert candidate(prices = [10, 20, 30, 40, 50],profits = [1, 2, 3, 4, 5]) == 12
    assert candidate(prices = [10, 20, 30, 40, 50],profits = [5, 4, 3, 2, 1]) == 12
    assert candidate(prices = [5, 6, 7, 8, 9, 10],profits = [10, 20, 30, 40, 50, 60]) == 150
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15],profits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 24
    assert candidate(prices = [1000000, 500000, 1500000, 750000, 2000000, 1250000, 2500000, 1750000, 3000000, 2250000],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 240
    assert candidate(prices = [100000, 50000, 150000, 250000, 200000, 300000],profits = [1000, 2000, 3000, 4000, 5000, 6000]) == 14000
    assert candidate(prices = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],profits = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 120
    assert candidate(prices = [8, 5, 1, 9, 2, 10, 3, 11, 4, 12, 6, 7],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 32
    assert candidate(prices = [8, 6, 7, 5, 3, 0, 9],profits = [10, 20, 30, 40, 50, 60, 70]) == 120
    assert candidate(prices = [100000, 200000, 50000, 150000, 250000, 300000, 350000, 400000, 450000, 500000],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18
    assert candidate(prices = [10, 20, 30, 25, 40, 50, 45, 60, 70, 80],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 42
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2700
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 30, 40],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == 51
    assert candidate(prices = [10, 20, 30, 40, 50, 60],profits = [1, 2, 3, 4, 5, 6]) == 15
    assert candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 42
    assert candidate(prices = [2, 1, 3, 5, 4, 6, 8, 7, 9, 11, 10, 12],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 32
    assert candidate(prices = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13],profits = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == -1
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [5, 1, 4, 3, 6, 2, 7, 8, 9, 10],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2700
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],profits = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1
    assert candidate(prices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],profits = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 269
    assert candidate(prices = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 27
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profits = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 2700
    assert candidate(prices = [10, 2, 5, 1, 8, 3, 7, 4, 6, 9],profits = [100, 200, 150, 10, 250, 60, 210, 30, 180, 350]) == 800
    assert candidate(prices = [100, 200, 150, 300, 250, 400, 350],profits = [50, 150, 100, 200, 10, 300, 20]) == 650
    assert candidate(prices = [5, 3, 8, 6, 7, 9],profits = [20, 15, 30, 25, 40, 50]) == 115
    assert candidate(prices = [1, 2, 5, 4, 6, 3, 7, 8, 10, 9],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2500
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profits = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17]) == 59
    assert candidate(prices = [8, 1, 5, 3, 6, 2, 9],profits = [3, 10, 7, 4, 8, 5, 6]) == 25
    assert candidate(prices = [100, 200, 150, 300, 250, 400, 350, 500, 450],profits = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000, 4500]) == 12000
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profits = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 51
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profits = [500, 400, 300, 200, 100, 50, 45, 40, 35, 30]) == 1200
    assert candidate(prices = [5, 3, 6, 7, 2, 9, 10, 1, 4, 8, 11, 12, 13],profits = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 69
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 27
    assert candidate(prices = [5, 3, 6, 7, 2, 9, 10, 1],profits = [1, 2, 3, 4, 5, 6, 7, 8]) == 18
    assert candidate(prices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],profits = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],profits = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 114
    assert candidate(prices = [100, 10, 20, 30, 40, 50],profits = [1, 100, 200, 300, 400, 500]) == 1200
    assert candidate(prices = [5, 4, 3, 2, 1, 0],profits = [100, 200, 300, 400, 500, 600]) == -1
    assert candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 7, 8, 10],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 39
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profits = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 135
    assert candidate(prices = [5, 1, 9, 2, 8, 3, 7, 4, 6],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 2300
    assert candidate(prices = [5, 1, 6, 2, 7, 3, 8, 4, 9, 10],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [2, 3, 1, 5, 4, 8, 7, 10, 9, 12, 11],profits = [20, 30, 10, 50, 40, 80, 70, 100, 90, 120, 110]) == 300
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profits = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 27
    assert candidate(prices = [2, 3, 1, 5, 4, 8, 7, 6, 9, 10],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [1000000, 500000, 750000, 250000, 1250000, 375000, 625000, 875000, 1125000, 1375000],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2700
    assert candidate(prices = [2, 1, 5, 3, 6, 4, 7, 8, 9],profits = [50, 100, 150, 200, 250, 300, 350, 400, 450]) == 1200
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 45
    assert candidate(prices = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 260
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],profits = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 87
    assert candidate(prices = [5, 3, 8, 6, 7, 2, 9, 4],profits = [10, 20, 30, 40, 50, 60, 70, 80]) == 160
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],profits = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == -1
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profits = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 57
    assert candidate(prices = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [8, 6, 7, 5, 3, 0, 9],profits = [100, 200, 300, 400, 500, 600, 700]) == 1200
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],profits = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 33
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 42
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],profits = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 270
    assert candidate(prices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],profits = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]) == 42
    assert candidate(prices = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profits = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 56
    assert candidate(prices = [100, 200, 150, 250, 300, 350],profits = [10, 20, 30, 40, 50, 60]) == 150
    assert candidate(prices = [100, 200, 150, 300, 250, 400, 350, 500],profits = [50, 45, 40, 35, 30, 25, 20, 15]) == 130
    assert candidate(prices = [2, 1, 5, 4, 7, 6, 9, 8, 11, 10],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 24
    assert candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],profits = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 101, 102]) == 303
    assert candidate(prices = [3, 5, 2, 7, 6, 8, 9, 1, 4, 10],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2700
    assert candidate(prices = [8, 6, 7, 5, 3, 0, 9],profits = [80, 60, 70, 50, 30, 0, 90]) == 220
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 57
    assert candidate(prices = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 270
    assert candidate(prices = [10, 20, 30, 25, 40, 50],profits = [5, 10, 15, 20, 25, 30]) == 75
    assert candidate(prices = [1, 3, 2, 5, 4, 7, 6, 9, 8],profits = [10, 30, 20, 50, 40, 70, 60, 90, 80]) == 210
    assert candidate(prices = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],profits = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]) == 19
    assert candidate(prices = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20],profits = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 56
    assert candidate(prices = [3, 5, 1, 7, 2, 8, 4, 6, 9],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 2400
    assert candidate(prices = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],profits = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 120
    assert candidate(prices = [5, 3, 8, 6, 7, 2, 9, 1, 4],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 160
    assert candidate(prices = [8, 6, 7, 5, 3, 0, 9],profits = [30, 20, 100, 40, 70, 10, 150]) == 270
    assert candidate(prices = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],profits = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]) == 59
    assert candidate(prices = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2500
    assert candidate(prices = [15, 10, 5, 20, 25, 30, 35, 40, 45, 50],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 270
    assert candidate(prices = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],profits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(prices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 54
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],profits = [49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 141
    assert candidate(prices = [7, 3, 5, 1, 6, 4, 9, 8, 2, 10],profits = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 2400
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],profits = [120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 330
    assert candidate(prices = [10, 20, 15, 30, 25, 35],profits = [100, 200, 150, 300, 250, 350]) == 850
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],profits = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 69
    assert candidate(prices = [2, 2, 3, 3, 5, 5, 7, 7, 11, 11, 13, 13, 17, 17, 19, 19, 23, 23, 29, 29],profits = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 54
