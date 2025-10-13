# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 3, 3, 7, 7, 9],k = 3) == 0
    assert candidate(nums = [5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3],k = 500000000) == 499999997
    assert candidate(nums = [2, 5, 6, 8, 5],k = 7) == 3
    assert candidate(nums = [1, 1, 1, 1, 1],k = 3) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6],k = 4) == 0
    assert candidate(nums = [2, 5, 6, 8, 5],k = 4) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 100, 101],k = 3) == 0
    assert candidate(nums = [1, 3, 3, 3, 7],k = 3) == 0
    assert candidate(nums = [1, 3, 3, 3, 7, 7, 9],k = 5) == 2
    assert candidate(nums = [10, 20, 30, 40, 50],k = 30) == 0
    assert candidate(nums = [10, 20, 30, 40, 50],k = 35) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 8
    assert candidate(nums = [2, 3, 1, 5, 4, 6, 8, 7, 9],k = 6) == 1
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 20) == 100
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],k = 5) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 40
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999],k = 1000000000) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],k = 6) == 0
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],k = 4) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 55) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13],k = 8) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],k = 11) == 0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 4) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 14
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 10
    assert candidate(nums = [5, 1, 9, 3, 7, 11, 13, 15, 17, 19],k = 10) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100],k = 600) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 40) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 15) == 0
    assert candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000],k = 500000000) == 500000000
    assert candidate(nums = [1000000000, 500000000, 750000000, 250000000, 1000],k = 500000000) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 105) == 5
    assert candidate(nums = [2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],k = 11) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 10) == 0
    assert candidate(nums = [1, 3, 3, 6, 7, 8, 9, 10, 11],k = 8) == 1
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2],k = 10) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 4) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6],k = 3) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 0
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000],k = 6500) == 500
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 6) == 0
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996],k = 500000000) == 499999996
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000) == 0
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],k = 1000000000) == 3062500000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 50) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],k = 7) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 80) == 0
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],k = 95) == 0
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4],k = 2) == 0
    assert candidate(nums = [9, 3, 5, 7, 1, 8, 2, 4, 6],k = 5) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],k = 10) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 3) == 0
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1) == 5999999994
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 5) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 11) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 12
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 30) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 500000000) == 1500000000
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 5) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 35) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5],k = 6) == 4
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],k = 29) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 6) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 65
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 25
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130],k = 65) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],k = 7) == 0
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 0],k = 5) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 1
    assert candidate(nums = [9, 3, 7, 5, 1, 8, 6, 4, 2, 0],k = 5) == 0
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 999999999) == 3
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 45) == 5
