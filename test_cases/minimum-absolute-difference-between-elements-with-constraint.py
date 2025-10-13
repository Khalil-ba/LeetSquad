# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1],x = 2) == 0
    assert candidate(nums = [10, 5, 3, 9, 2],x = 2) == 1
    assert candidate(nums = [1, 1, 1, 1, 1],x = 0) == 0
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7],x = 3) == 0
    assert candidate(nums = [1, 2, 3, 4],x = 3) == 3
    assert candidate(nums = [4, 3, 2, 4],x = 2) == 0
    assert candidate(nums = [1000000000, 1, 1000000000, 1],x = 1) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1],x = 4) == 0
    assert candidate(nums = [1, 5, 3, 19, 18, 22],x = 3) == 13
    assert candidate(nums = [10, 5, 3, 6, 8, 1, 2],x = 2) == 1
    assert candidate(nums = [10, 20, 30, 40, 50],x = 2) == 20
    assert candidate(nums = [5, 3, 2, 10, 15],x = 1) == 1
    assert candidate(nums = [10, 5, 3, 6, 8, 2, 9],x = 4) == 1
    assert candidate(nums = [10, 5, 3, 100, 20, 15],x = 2) == 5
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 4) == 2
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996],x = 2) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],x = 12) == 12
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],x = 7) == 3
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],x = 2) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 25) == 0
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998],x = 2) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 7) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 0) == 0
    assert candidate(nums = [3, 8, 15, 17, 9, 5, 12, 3],x = 3) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 3) == 30
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 8) == 80
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],x = 3) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],x = 4) == 8
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],x = 5) == 0
    assert candidate(nums = [7, 3, 2, 8, 6, 5, 4, 9, 1, 10],x = 3) == 1
    assert candidate(nums = [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],x = 3) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 2) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],x = 6) == 6
    assert candidate(nums = [5, 3, 3, 5, 5, 3, 3, 5, 5, 3, 3, 5],x = 2) == 0
    assert candidate(nums = [100, 200, 100, 200, 100, 200, 100, 200, 100, 200],x = 5) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 9) == 9
    assert candidate(nums = [7, 7, 8, 8, 9, 9, 10, 10],x = 4) == 2
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 6) == 600
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 3) == 3
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6],x = 4) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],x = 10) == 10
    assert candidate(nums = [9, 1, 5, 7, 3, 8, 2, 6, 4, 10],x = 4) == 1
    assert candidate(nums = [5, 1, 4, 2, 3],x = 2) == 1
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991],x = 4) == 4
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45],x = 3) == 5
    assert candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500],x = 5) == 500
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 5) == 50
    assert candidate(nums = [2, 5, 1, 8, 3, 7, 4, 6],x = 2) == 1
    assert candidate(nums = [1, 3, 6, 8, 9, 10, 12, 15, 18, 20],x = 6) == 11
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 4) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 3) == 30
    assert candidate(nums = [1, 5, 9, 14, 20, 25, 30],x = 2) == 8
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],x = 3) == 29
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],x = 10) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 5) == 5
    assert candidate(nums = [9, 5, 12, 6, 18, 3],x = 2) == 1
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],x = 5) == 3
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],x = 6) == 12
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],x = 5) == 2
    assert candidate(nums = [23, 1, 21, 3, 19, 5, 17, 7, 15, 9, 13, 11, 14, 12, 16, 10, 18, 8, 20, 6, 22, 4, 24, 2, 25],x = 7) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],x = 5) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],x = 9) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 6) == 600
    assert candidate(nums = [5, 8, 12, 15, 18, 21, 24, 27, 30, 33],x = 4) == 12
    assert candidate(nums = [3, 8, 15, 1, 6],x = 3) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],x = 1) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 4) == 4
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000],x = 3) == 109375000
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 2) == 2
    assert candidate(nums = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],x = 4) == 0
    assert candidate(nums = [7, 1, 14, 11],x = 2) == 4
    assert candidate(nums = [1, 3, 6, 8, 12, 15, 18, 20],x = 3) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],x = 5) == 5
    assert candidate(nums = [1000000000, 999999999, 1, 2, 3, 4, 5, 6, 7, 8, 9],x = 5) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 2) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],x = 9) == 9
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 3) == 3
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10],x = 2) == 0
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],x = 2) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 4) == 0
    assert candidate(nums = [2, 1, 2, 3, 1, 3, 4, 1, 4, 2, 4, 3, 5, 1, 5, 2, 5, 3, 5, 4],x = 4) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 4) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 5) == 5
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],x = 5) == 50
    assert candidate(nums = [9, 1, 8, 2, 7, 3, 6, 4, 5],x = 2) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 2) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],x = 8) == 40
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],x = 2) == 0
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],x = 4) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],x = 15) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 10) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],x = 2) == 200
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],x = 4) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 2) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 1) == 2
    assert candidate(nums = [100, 50, 10, 5, 1, 500, 1000, 200, 300, 400],x = 3) == 49
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],x = 5) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 4) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 5) == 50
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],x = 5) == 0
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],x = 1) == 1
    assert candidate(nums = [8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 3) == 1
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],x = 2) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],x = 4) == 8
    assert candidate(nums = [5, 3, 2, 4, 1, 6, 7, 8, 9, 10],x = 7) == 3
    assert candidate(nums = [4, 1, 7, 10, 3, 8, 2, 9, 5, 6],x = 2) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 10) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 4) == 4
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1],x = 2) == 0
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],x = 3) == 0
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],x = 8) == 0
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],x = 3) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],x = 7) == 7
    assert candidate(nums = [7, 1, 3, 4, 1, 7],x = 3) == 0
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1],x = 2) == 0
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],x = 5) == 0
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1],x = 3) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],x = 2) == 20
    assert candidate(nums = [8, 1, 5, 10, 18, 15, 22, 4, 7, 2],x = 5) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],x = 9) == 0
    assert candidate(nums = [1, 1000000000, 1, 1000000000],x = 2) == 0
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000],x = 1) == 0
    assert candidate(nums = [3, 5, 6, 7, 8, 8],x = 1) == 0
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],x = 3) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 6) == 6
    assert candidate(nums = [1],x = 0) == 0
    assert candidate(nums = [6, 2, 1, 100, 1000, 3, 4],x = 4) == 1
    assert candidate(nums = [100, 100, 100, 100],x = 0) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 3) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],x = 5) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 5) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11],x = 5) == 10
    assert candidate(nums = [10, 20, 30, 40, 50],x = 5) == inf
    assert candidate(nums = [1, 1, 1, 1, 1, 1],x = 2) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 4) == 0
    assert candidate(nums = [1, 5, 9, 14, 20],x = 2) == 8
    assert candidate(nums = [10, 20, 30, 40, 50],x = 0) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 5) == 5
    assert candidate(nums = [7, 1, 4, 5, 9, 2, 6, 3],x = 2) == 1
    assert candidate(nums = [7, 1, 4, 5, 6, 2],x = 3) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 2) == 2
    assert candidate(nums = [10, 20, 30, 40, 50],x = 4) == 40
    assert candidate(nums = [10, 5, 1, 7, 10, 3],x = 2) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50],x = 3) == 30
    assert candidate(nums = [1, 3, 6, 8, 9, 15],x = 0) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],x = 4) == 0
    assert candidate(nums = [10, 5, 3, 8, 12, 7, 6, 9, 1, 2],x = 4) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],x = 0) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 9) == 9
    assert candidate(nums = [1, 5, 3, 19, 18, 22, 6, 7],x = 3) == 1
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000],x = 4) == 0
    assert candidate(nums = [5, 8, 3, 9, 7, 6, 2, 4, 1, 10],x = 4) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 2) == 2
    assert candidate(nums = [8, 12, 4, 13, 7],x = 2) == 1
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],x = 5) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 2) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 0) == 0
    assert candidate(nums = [1, 1, 1, 1, 1],x = 2) == 0
    assert candidate(nums = [1, 100, 1, 100, 1, 100],x = 1) == 0
    assert candidate(nums = [10, 5, 3, 9, 2, 8],x = 2) == 1
    assert candidate(nums = [7, 1, 3, 4, 1, 9],x = 1) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 1) == 2
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],x = 0) == 0
    assert candidate(nums = [7, 1, 3, 4, 1, 9],x = 4) == 2
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1],x = 3) == 0
    assert candidate(nums = [7, 1, 3, 4, 1, 7],x = 2) == 0
    assert candidate(nums = [5, 1, 4, 1, 2],x = 2) == 0
    assert candidate(nums = [1000000000, 1, 1000000000, 1],x = 2) == 0
    assert candidate(nums = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997],x = 2) == 1
    assert candidate(nums = [1, 5, 3, 19, 18, 22, 6, 7, 20, 15],x = 4) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 4) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],x = 0) == 0
    assert candidate(nums = [3, 5, 4, 2, 4],x = 1) == 0
    assert candidate(nums = [100, 200, 300, 400, 500],x = 0) == 0
    assert candidate(nums = [7, 1, 3, 8, 6, 2, 5, 4],x = 2) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 1) == 0
    assert candidate(nums = [10, 5, 4, 7, 8, 9],x = 4) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1],x = 0) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],x = 3) == 3
    assert candidate(nums = [1, 1000000000, 1, 1000000000],x = 1) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],x = 9) == 0
    assert candidate(nums = [3, 5, 9, 8, 10, 1],x = 2) == 1
    assert candidate(nums = [1, 10, 3, 7, 5, 8, 6, 2, 4, 9],x = 5) == 1
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 1000000000, 999999999, 1],x = 3) == 0
    assert candidate(nums = [10, 5, 3, 9, 2, 8, 6],x = 2) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 8) == 16
    assert candidate(nums = [10, 5, 1, 15, 3, 7, 8],x = 2) == 2
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],x = 5) == 50
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1],x = 3) == 0
    assert candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000],x = 2) == 0
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],x = 0) == 0
    assert candidate(nums = [1, 5, 3, 19, 18, 25],x = 3) == 13
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 0) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 5) == 5
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],x = 4) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 0) == 0
    assert candidate(nums = [1, 5, 3, 19, 18, 25],x = 2) == 2
    assert candidate(nums = [10, 5, 3, 8, 12],x = 2) == 2
    assert candidate(nums = [3, 5, 3, 5, 3, 5, 3, 5],x = 3) == 0
    assert candidate(nums = [10, 5, 4, 7, 8, 3, 6, 1],x = 4) == 1
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],x = 9) == 90
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 5) == 0
    assert candidate(nums = [10, 5, 1, 9, 4, 8, 3, 7, 2, 6],x = 4) == 1
    assert candidate(nums = [7, 10, 4, 3, 20, 15],x = 2) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 2) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],x = 3) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],x = 0) == 0
    assert candidate(nums = [1, 2, 3, 100, 101, 102],x = 2) == 2
    assert candidate(nums = [1, 5, 9, 13, 17],x = 4) == 16
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],x = 4) == 40
    assert candidate(nums = [10, 5, 1, 100, 1000],x = 2) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],x = 3) == 3
    assert candidate(nums = [100, 200, 300, 400, 500, 100, 200, 300],x = 3) == 0
