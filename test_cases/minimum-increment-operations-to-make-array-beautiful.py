# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [10, 9, 8, 7, 6],k = 10) == 2
    assert candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000],k = 1000000000) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1],k = 3) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 2
    assert candidate(nums = [1, 0, 0, 0, 1],k = 2) == 2
    assert candidate(nums = [1000000000, 1000000000, 1000000000],k = 1000000000) == 0
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1],k = 2) == 3
    assert candidate(nums = [5, 5, 5, 5],k = 3) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5],k = 10) == 3
    assert candidate(nums = [2, 3, 0, 0, 2],k = 4) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 12
    assert candidate(nums = [0, 1, 3, 3],k = 5) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6],k = 7) == 5
    assert candidate(nums = [5, 5, 5, 5, 5],k = 3) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0],k = 0) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 12
    assert candidate(nums = [1, 1, 2],k = 1) == 0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 5) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0],k = 1) == 2
    assert candidate(nums = [0, 0, 0, 0, 0],k = 3) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 5) == 3
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],k = 1000000000) == 2
    assert candidate(nums = [3, 2, 1, 5, 4, 6, 7, 8, 9, 10],k = 5) == 2
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 5) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 12
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 200
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 25) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 7) == 5
    assert candidate(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],k = 1) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 10) == 15
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 7) == 14
    assert candidate(nums = [3, 0, 0, 3, 0, 0, 3, 0, 0],k = 3) == 0
    assert candidate(nums = [5, 1, 4, 2, 8, 3, 6, 9, 7],k = 5) == 1
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0],k = 5) == 6
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 2) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 3
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 12
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 12
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == 10
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 10) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 15
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],k = 3) == 3
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 3
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1) == 0
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],k = 4) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 20) == 27
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 50) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 3) == 4
    assert candidate(nums = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],k = 2) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 15
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 6
    assert candidate(nums = [5, 1, 9, 3, 7, 8, 2, 6, 4],k = 6) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 100) == 120
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 100) == 0
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],k = 4) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 5) == 3
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 4) == 1
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 3) == 9
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 0) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 0
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 105) == 3
    assert candidate(nums = [8, 6, 7, 5, 3, 0, 9],k = 8) == 3
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 3) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 15) == 12
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 4) == 6
    assert candidate(nums = [10, 15, 0, 20, 5, 25, 1, 30],k = 10) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 25) == 0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 6) == 3
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 15) == 12
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 35
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5],k = 5) == 3
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8) == 7
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8) == 7
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6) == 3
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 200
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
    assert candidate(nums = [5, 3, 2, 1, 0, 6, 4, 8, 7],k = 5) == 3
    assert candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555, 444444444, 333333333, 222222222, 111111111],k = 900000000) == 800000001
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 7) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1],k = 4) == 2
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],k = 2) == 6
    assert candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666, 555555555],k = 777777777) == 0
    assert candidate(nums = [10, 0, 10, 0, 10, 0, 10, 0, 10],k = 5) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 6
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 10) == 3
    assert candidate(nums = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 50) == 132
    assert candidate(nums = [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0],k = 2) == 0
    assert candidate(nums = [5, 3, 2, 7, 1, 4, 6, 8, 0],k = 6) == 1
    assert candidate(nums = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],k = 10) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 12
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 25
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 5
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 10) == 3
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 12
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6],k = 6) == 5
    assert candidate(nums = [2, 1, 0, 1, 2, 1, 0, 2, 1, 0],k = 2) == 1
    assert candidate(nums = [5, 3, 2, 8, 6, 7, 10, 1, 4],k = 6) == 1
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 2) == 5
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 25
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 600) == 300
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == 7
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 30
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 55) == 25
