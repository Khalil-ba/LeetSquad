# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [7, 7, 7, 7, 7],k = 2) == 7
    assert candidate(nums = [9, 8, 7, 6, 5],k = 5) == 9
    assert candidate(nums = [10],k = 2) == 10
    assert candidate(nums = [8, 6, 4, 2, 0],k = 7) == 8
    assert candidate(nums = [7, 7, 7, 7, 7],k = 3) == 7
    assert candidate(nums = [1000000000],k = 0) == 1000000000
    assert candidate(nums = [5, 4, 3, 2, 1],k = 2) == 5
    assert candidate(nums = [1],k = 2) == 1
    assert candidate(nums = [1, 3, 5, 7, 9],k = 10) == 9
    assert candidate(nums = [3, 3, 3, 3, 3, 3],k = 1000000000) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],k = 3) == 4
    assert candidate(nums = [2],k = 1) == -1
    assert candidate(nums = [9, 7, 5, 3, 1],k = 5) == 9
    assert candidate(nums = [10],k = 0) == 10
    assert candidate(nums = [1, 3, 5, 7, 9],k = 2) == 5
    assert candidate(nums = [9],k = 0) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 10
    assert candidate(nums = [0, 0, 0, 0, 0],k = 5) == 0
    assert candidate(nums = [1, 3, 5, 7, 9],k = 0) == 1
    assert candidate(nums = [1000000000],k = 1000000000) == 1000000000
    assert candidate(nums = [1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(nums = [5, 2, 2, 4, 0, 6],k = 4) == 5
    assert candidate(nums = [1, 2],k = 2) == 1
    assert candidate(nums = [3, 3, 3, 3, 3],k = 5) == 3
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 5) == 9
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 9) == 9
    assert candidate(nums = [1, 1, 1, 1, 1],k = 0) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],k = 0) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 5) == 5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 5) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 11) == 10
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6
    assert candidate(nums = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2],k = 9) == 20
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 15) == 19
    assert candidate(nums = [3, 7, 2, 8, 6, 4, 1, 9],k = 3) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 11) == 10
    assert candidate(nums = [5, 2, 9, 1, 5, 6, 7, 3, 4, 8],k = 15) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 7) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 19) == 10
    assert candidate(nums = [5, 2, 2, 4, 0, 6],k = 6) == 5
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 9
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 7) == 9
    assert candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10],k = 7) == 90
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 90
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 60
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],k = 9) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 18) == 19
    assert candidate(nums = [1],k = 1000000000) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 8) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 90
    assert candidate(nums = [1000000000, 1000000000, 1000000000],k = 2) == 1000000000
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 20) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 8
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 11) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 10
    assert candidate(nums = [10, 20, 30, 40, 50],k = 2) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 21) == 10
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 25) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 19
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 10) == 9
    assert candidate(nums = [5, 1, 3, 2, 8, 7],k = 3) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1],k = 7) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 10) == 7
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == 9
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 10) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 11) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13],k = 3) == 7
    assert candidate(nums = [5, 2, 9, 1, 5, 6],k = 3) == 5
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 8) == 45
    assert candidate(nums = [10, 20, 30, 40, 50],k = 3) == 40
    assert candidate(nums = [7, 3, 5, 4, 1, 9, 8, 6, 2],k = 6) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 60
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 8) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 1
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 10) == 100
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 10) == 7
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 999999) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 10
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 8) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 14) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 12) == 13
    assert candidate(nums = [1, 2, 3, 4, 5],k = 100) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 13) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 17
    assert candidate(nums = [7, 1, 5, 3, 6, 4],k = 3) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 9) == 1
    assert candidate(nums = [3, 7, 2, 5, 8, 6, 1],k = 10) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 999999999) == 100
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 6
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 100) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 19
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 9) == 100
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 7) == 9
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 10) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5],k = 9) == 5
    assert candidate(nums = [5, 1, 3, 2, 8, 7],k = 6) == 8
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 18) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 9) == 5
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],k = 12) == 14
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2) == 30
    assert candidate(nums = [1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5) == 12
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 19
    assert candidate(nums = [100, 90, 80, 70, 60],k = 6) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 4
    assert candidate(nums = [1000000000, 999999999, 888888888, 777777777],k = 4) == 1000000000
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],k = 4) == 100
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 9) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 12) == 10
    assert candidate(nums = [5, 3, 1, 4, 9, 8],k = 5) == 8
    assert candidate(nums = [100, 200, 300, 400, 500],k = 2) == 300
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 11) == 9
    assert candidate(nums = [1, 3, 5, 7, 9],k = 5) == 7
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 9) == 2
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 15) == 100
    assert candidate(nums = [1, 2, 3, 4, 5],k = 0) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 7) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 9
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 9) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 1
    assert candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666],k = 10) == 1000000000
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9],k = 8) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 9
    assert candidate(nums = [5, 4, 3, 2, 1],k = 2) == 5
    assert candidate(nums = [50, 50, 50, 50, 50],k = 4) == 50
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 9) == 5
    assert candidate(nums = [10, 20, 30, 40, 50],k = 1) == 20
