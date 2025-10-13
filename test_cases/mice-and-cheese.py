# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(reward1 = [10, 20, 30, 40],reward2 = [40, 30, 20, 10],k = 3) == 130
    assert candidate(reward1 = [5, 4, 3, 2, 1],reward2 = [1, 2, 3, 4, 5],k = 3) == 21
    assert candidate(reward1 = [10, 20, 30],reward2 = [40, 50, 60],k = 0) == 150
    assert candidate(reward1 = [1, 2, 3, 4, 5],reward2 = [5, 4, 3, 2, 1],k = 3) == 21
    assert candidate(reward1 = [7, 5, 3, 1],reward2 = [6, 4, 2, 0],k = 4) == 16
    assert candidate(reward1 = [5, 4, 3],reward2 = [1, 2, 3],k = 1) == 10
    assert candidate(reward1 = [7, 8, 9],reward2 = [10, 11, 12],k = 3) == 24
    assert candidate(reward1 = [100, 100, 100],reward2 = [1, 1, 1],k = 0) == 3
    assert candidate(reward1 = [10, 20, 30],reward2 = [30, 20, 10],k = 2) == 80
    assert candidate(reward1 = [7, 8, 9],reward2 = [1, 2, 3],k = 3) == 24
    assert candidate(reward1 = [1, 1, 3, 4],reward2 = [4, 4, 1, 1],k = 2) == 15
    assert candidate(reward1 = [5, 4, 3],reward2 = [1, 1, 1],k = 1) == 7
    assert candidate(reward1 = [1, 2, 3, 4, 5],reward2 = [5, 4, 3, 2, 1],k = 5) == 15
    assert candidate(reward1 = [100, 200, 300, 400],reward2 = [400, 300, 200, 100],k = 2) == 1400
    assert candidate(reward1 = [10, 20, 30],reward2 = [3, 6, 9],k = 0) == 18
    assert candidate(reward1 = [10, 20, 30],reward2 = [30, 20, 10],k = 0) == 60
    assert candidate(reward1 = [1, 1],reward2 = [1, 1],k = 2) == 2
    assert candidate(reward1 = [1, 3, 5, 7, 9],reward2 = [2, 4, 6, 8, 10],k = 2) == 28
    assert candidate(reward1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],reward2 = [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2],k = 10) == 330
    assert candidate(reward1 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],reward2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 10
    assert candidate(reward1 = [1, 3, 5, 7, 9, 11, 13, 15],reward2 = [2, 4, 6, 8, 10, 12, 14, 16],k = 4) == 68
    assert candidate(reward1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],reward2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 0) == 550
    assert candidate(reward1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 55
    assert candidate(reward1 = [100, 200, 300, 400, 500, 600],reward2 = [10, 20, 30, 40, 50, 60],k = 2) == 1200
    assert candidate(reward1 = [100, 200, 300, 400, 500],reward2 = [10, 20, 30, 40, 50],k = 2) == 960
    assert candidate(reward1 = [50, 40, 30, 20, 10],reward2 = [10, 20, 30, 40, 50],k = 0) == 150
    assert candidate(reward1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 4040
    assert candidate(reward1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],reward2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 7) == 176
    assert candidate(reward1 = [100, 200, 300, 400, 500],reward2 = [5, 10, 15, 20, 25],k = 2) == 930
    assert candidate(reward1 = [1, 1, 1, 1, 1, 1],reward2 = [999, 999, 999, 999, 999, 999],k = 3) == 3000
    assert candidate(reward1 = [5, 5, 5, 5, 5],reward2 = [1, 2, 3, 4, 5],k = 5) == 25
    assert candidate(reward1 = [999, 1, 1, 1, 1, 1],reward2 = [1, 999, 1, 1, 1, 1],k = 1) == 2002
    assert candidate(reward1 = [500, 500, 500, 500, 500],reward2 = [500, 500, 500, 500, 500],k = 2) == 2500
    assert candidate(reward1 = [1, 2, 3, 4, 5],reward2 = [200, 200, 200, 200, 200],k = 3) == 412
    assert candidate(reward1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],reward2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 0) == 55
    assert candidate(reward1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],reward2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 0) == 110
    assert candidate(reward1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],reward2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 55
    assert candidate(reward1 = [100, 200, 300, 400, 500],reward2 = [90, 190, 290, 390, 490],k = 2) == 1470
    assert candidate(reward1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],reward2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == 800
    assert candidate(reward1 = [500, 400, 300, 200, 100],reward2 = [100, 200, 300, 400, 500],k = 0) == 1500
    assert candidate(reward1 = [500, 400, 300, 200, 100],reward2 = [50, 100, 150, 200, 250],k = 4) == 1650
    assert candidate(reward1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],reward2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 405
    assert candidate(reward1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],reward2 = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],k = 5) == 42
    assert candidate(reward1 = [100, 200, 300, 400, 500],reward2 = [500, 400, 300, 200, 100],k = 0) == 1500
    assert candidate(reward1 = [200, 200, 200, 200, 200],reward2 = [1, 2, 3, 4, 5],k = 2) == 412
    assert candidate(reward1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],reward2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 30
    assert candidate(reward1 = [8, 6, 7, 5, 3, 0, 9],reward2 = [1, 2, 3, 4, 5, 6, 7],k = 4) == 45
    assert candidate(reward1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 5500
    assert candidate(reward1 = [1000, 1000, 1000, 1000],reward2 = [1, 1, 1, 1],k = 0) == 4
    assert candidate(reward1 = [1, 3, 5, 7, 9, 11, 13, 15],reward2 = [2, 4, 6, 8, 10, 12, 14, 16],k = 4) == 68
    assert candidate(reward1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],reward2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 10
    assert candidate(reward1 = [90, 80, 70, 60, 50],reward2 = [10, 20, 30, 40, 50],k = 2) == 290
    assert candidate(reward1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 415
    assert candidate(reward1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 550
    assert candidate(reward1 = [100, 100, 100, 100, 100],reward2 = [1, 2, 3, 4, 5],k = 3) == 309
    assert candidate(reward1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],reward2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 30
    assert candidate(reward1 = [1, 2, 3, 4, 5],reward2 = [5, 4, 3, 2, 1],k = 5) == 15
    assert candidate(reward1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 4) == 65
    assert candidate(reward1 = [100, 100, 100, 100],reward2 = [50, 50, 50, 50],k = 2) == 300
    assert candidate(reward1 = [1000, 1000, 1000, 1000, 1000],reward2 = [900, 900, 900, 900, 900],k = 5) == 5000
    assert candidate(reward1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],reward2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5) == 105
    assert candidate(reward1 = [10, 20, 30, 40, 50],reward2 = [5, 15, 25, 35, 45],k = 3) == 140
    assert candidate(reward1 = [900, 800, 700, 600, 500, 400, 300, 200, 100, 0],reward2 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900],k = 5) == 7000
    assert candidate(reward1 = [900, 800, 700, 600, 500],reward2 = [100, 200, 300, 400, 500],k = 2) == 2900
    assert candidate(reward1 = [800, 900, 700, 600, 500],reward2 = [100, 200, 300, 400, 500],k = 1) == 2200
    assert candidate(reward1 = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 5025
    assert candidate(reward1 = [10, 20, 30, 40, 50],reward2 = [500, 400, 300, 200, 100],k = 2) == 1290
    assert candidate(reward1 = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],reward2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 5500
    assert candidate(reward1 = [500, 400, 300, 200, 100],reward2 = [1000, 900, 800, 700, 600],k = 5) == 1500
    assert candidate(reward1 = [9, 18, 27, 36, 45, 54],reward2 = [6, 12, 18, 24, 30, 36],k = 2) == 159
    assert candidate(reward1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],reward2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 55
    assert candidate(reward1 = [100, 200, 300, 400, 500],reward2 = [500, 400, 300, 200, 100],k = 3) == 2100
    assert candidate(reward1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],reward2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 80
    assert candidate(reward1 = [5, 5, 5, 5, 5],reward2 = [100, 200, 300, 400, 500],k = 0) == 1500
    assert candidate(reward1 = [50, 40, 30, 20, 10],reward2 = [10, 20, 30, 40, 50],k = 0) == 150
    assert candidate(reward1 = [100, 100, 100],reward2 = [10, 20, 30],k = 0) == 60
    assert candidate(reward1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 55
    assert candidate(reward1 = [1000, 900, 800, 700, 600],reward2 = [10, 20, 30, 40, 50],k = 3) == 2790
    assert candidate(reward1 = [50, 30, 10, 20, 40],reward2 = [40, 20, 30, 10, 50],k = 4) == 170
    assert candidate(reward1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],reward2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 50
    assert candidate(reward1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],reward2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == 176
    assert candidate(reward1 = [500, 400, 300, 200, 100],reward2 = [1, 2, 3, 4, 5],k = 5) == 1500
    assert candidate(reward1 = [1, 2, 3, 4, 5],reward2 = [500, 400, 300, 200, 100],k = 0) == 1500
    assert candidate(reward1 = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 55
    assert candidate(reward1 = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],reward2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 3043
    assert candidate(reward1 = [1000, 900, 800, 700, 600],reward2 = [500, 600, 700, 800, 900],k = 5) == 4000
    assert candidate(reward1 = [900, 800, 700, 600, 500],reward2 = [100, 200, 300, 400, 500],k = 4) == 3500
    assert candidate(reward1 = [100, 200, 300, 400, 500],reward2 = [50, 150, 250, 350, 450],k = 3) == 1400
    assert candidate(reward1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],reward2 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 3) == 7003
    assert candidate(reward1 = [10, 20, 30, 40, 50],reward2 = [5, 15, 25, 35, 45],k = 3) == 140
    assert candidate(reward1 = [100, 90, 80, 70, 60],reward2 = [10, 20, 30, 40, 50],k = 2) == 310
    assert candidate(reward1 = [10, 10, 10, 10, 10, 10],reward2 = [9, 9, 9, 9, 9, 9],k = 3) == 57
    assert candidate(reward1 = [100, 200, 300, 400, 500, 600],reward2 = [60, 50, 40, 30, 20, 10],k = 2) == 1280
    assert candidate(reward1 = [300, 200, 100],reward2 = [100, 200, 300],k = 1) == 800
    assert candidate(reward1 = [100, 200, 300, 400],reward2 = [150, 250, 350, 450],k = 1) == 1150
    assert candidate(reward1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],reward2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 7) == 272
