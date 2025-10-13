# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-5, -4, -3, -2, -1],k = 5) == 15
    assert candidate(nums = [0, 0, 0, 0],k = 3) == 0
    assert candidate(nums = [4, 2, 3],k = 1) == 5
    assert candidate(nums = [100, -100, 50, -50],k = 3) == 200
    assert candidate(nums = [1, 2, 3, 4],k = 2) == 10
    assert candidate(nums = [100, -100, 50, -50],k = 5) == 200
    assert candidate(nums = [2, -3, -1, 5, -4],k = 2) == 13
    assert candidate(nums = [3, -1, 0, 2],k = 3) == 6
    assert candidate(nums = [-1, -2, -3, -4],k = 2) == 4
    assert candidate(nums = [0, 0, 0, 0],k = 4) == 0
    assert candidate(nums = [1, 2, 3],k = 6) == 6
    assert candidate(nums = [-1, 0, 1],k = 1) == 2
    assert candidate(nums = [-1, -2, -3, -4],k = 4) == 10
    assert candidate(nums = [0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 13
    assert candidate(nums = [1, -1, 2, -2],k = 4) == 6
    assert candidate(nums = [1, 2, 3, 4],k = 4) == 10
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4],k = 10) == 20
    assert candidate(nums = [1, -1, 2, -2, 3, -3],k = 9) == 12
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],k = 10) == 955
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 53
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3],k = 5) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 53
    assert candidate(nums = [-7, 3, -5, 2, -1],k = 6) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 53
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 15) == 8
    assert candidate(nums = [-1, 1, -1, 1, -1],k = 8) == 3
    assert candidate(nums = [-10, 20, -30, 40, -50],k = 5) == 150
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 13
    assert candidate(nums = [99, -99, 50, -50, 25, -25],k = 10) == 298
    assert candidate(nums = [1, 2, 3, 4, 5],k = 20) == 15
    assert candidate(nums = [100, -100, 100, -100, 100],k = 100) == 500
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1) == 1300
    assert candidate(nums = [-1, -2, -3, -4],k = 10) == 10
    assert candidate(nums = [-10, -9, -8, -7, -6],k = 10) == 28
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 15) == 150
    assert candidate(nums = [-10, 20, -30, 40, -50],k = 15) == 150
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],k = 6) == 250
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 55
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 15) == 550
    assert candidate(nums = [1, -1, 1, -1],k = 7) == 2
    assert candidate(nums = [5, -3, 8, -2, 9, -4],k = 3) == 31
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 10) == 13
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9999) == 8
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3, 4, -4],k = 15) == 20
    assert candidate(nums = [99, -99, 50, -50, 1],k = 10000) == 299
    assert candidate(nums = [1, -2, 3, -4, 5, -6],k = 5) == 21
    assert candidate(nums = [-1, -2, -3, -4],k = 3) == 8
    assert candidate(nums = [-1, 0, 1],k = 2) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 8
    assert candidate(nums = [0, 1, -2, 3, -4, 5, -6],k = 7) == 21
    assert candidate(nums = [1, -1, 1, -1, 1, -1],k = 100) == 4
    assert candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95],k = 15) == 970
    assert candidate(nums = [-10, -20, -30, -40],k = 6) == 100
    assert candidate(nums = [-1, 0, 1],k = 3) == 2
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 11) == 55
    assert candidate(nums = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0],k = 9) == 45
    assert candidate(nums = [-50, 50, 25, -25, 12, -12, 6, -6, 3, -3],k = 12) == 186
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 7) == 55
    assert candidate(nums = [10, 20, 30, 40, 50],k = 3) == 130
    assert candidate(nums = [0, 0, 0, 0],k = 7) == 0
    assert candidate(nums = [-1, 1, -2, 2, -3, 3],k = 5) == 12
    assert candidate(nums = [2, 4, 6, 8, 10],k = 1) == 26
    assert candidate(nums = [-10, 10, -20, 20, -30, 30],k = 6) == 100
    assert candidate(nums = [5, -3, 7, -2, 1],k = 3) == 16
    assert candidate(nums = [0, 0, 0, 0, 0],k = 1000) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 53
    assert candidate(nums = [-1, -2, -3, -4],k = 10) == 10
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 15) == 55
    assert candidate(nums = [0, 0, 0, 0],k = 100) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == 25
    assert candidate(nums = [100, 50, 25, 12, 6, 3],k = 7) == 190
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 45
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 20) == 110
    assert candidate(nums = [5, -5, 15, -15, 25, -25],k = 11) == 90
    assert candidate(nums = [100, 100, 100, 100, 100],k = 10000) == 500
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3],k = 7) == 12
    assert candidate(nums = [10, -10, 20, -20, 30, -30],k = 6) == 100
    assert candidate(nums = [100, -50, 25, -10, 5],k = 3) == 180
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 53
    assert candidate(nums = [99, -99, 50, -50, 25, -25],k = 7) == 348
    assert candidate(nums = [-1, -2, -3, 4, 5, 6],k = 4) == 19
    assert candidate(nums = [1, -1, 1, -1, 1, -1],k = 10) == 4
    assert candidate(nums = [1, 2, 3, -4, -5, -6],k = 3) == 21
    assert candidate(nums = [10, -10, 20, -20, 30, -30],k = 9) == 120
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 20) == 200
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 8) == 20
    assert candidate(nums = [0, 0, 0, 0, 0],k = 100) == 0
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40],k = 14) == 250
    assert candidate(nums = [-1, 0, 1],k = 5) == 2
    assert candidate(nums = [-99, -98, -97, -96, -95],k = 10) == 295
    assert candidate(nums = [10, -10, 20, -20, 30, -30],k = 7) == 120
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 10) == 46
    assert candidate(nums = [100, 100, 100, 100, 100],k = 3) == 300
    assert candidate(nums = [5, 5, 5, 5, 5],k = 1000) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],k = 15) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20) == 100
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 20) == 280
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = 10) == 55
    assert candidate(nums = [5, -5, 5, -5, 5, -5],k = 6) == 20
    assert candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0],k = 8) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 53
    assert candidate(nums = [5, -1, -2, -3, -4],k = 6) == 15
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 8) == 20
    assert candidate(nums = [-100, -200, -300, -400, -500],k = 2) == -1500
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 8) == 53
    assert candidate(nums = [-100, -50, 0, 50, 100],k = 3) == 300
    assert candidate(nums = [10, -20, 30, -40, 50, -60],k = 5) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 53
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 10) == 10
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 3) == 90
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 8) == 53
    assert candidate(nums = [-100, -50, -25, -12, -6, -3],k = 8) == 196
    assert candidate(nums = [-10, -20, 0, 20, 10],k = 5) == 60
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 20) == 130
    assert candidate(nums = [-1, 0, 1],k = 1) == 2
    assert candidate(nums = [-100, -100, -100, -100, -100],k = 10001) == 500
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 6) == 130
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6],k = 20) == 374
