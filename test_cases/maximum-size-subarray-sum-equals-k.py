# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5],k = 100) == 0
    assert candidate(nums = [5, 5, 5, 5, 5],k = 10) == 2
    assert candidate(nums = [1, 2, 3, 4, 5],k = 9) == 3
    assert candidate(nums = [0, 0, 0, 0, 0],k = 0) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 0) == 0
    assert candidate(nums = [0, 0, 0, 0, 0],k = 1) == 0
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 0) == 4
    assert candidate(nums = [1, 2, 3, 4, 5],k = 20) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5],k = -15) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5],k = -9) == 3
    assert candidate(nums = [10, 20, 30, 40, 50],k = 100) == 4
    assert candidate(nums = [10, -10, 10, -10, 10],k = 0) == 4
    assert candidate(nums = [1, -1, 5, -2, 3],k = 3) == 4
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 0) == 8
    assert candidate(nums = [-1, 2, -3, 4, -5],k = -3) == 5
    assert candidate(nums = [-2, -1, 2, 1],k = 1) == 2
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 10000) == 5
    assert candidate(nums = [10, 20, 30, 40, 50],k = 150) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 10
    assert candidate(nums = [-1, -2, -3, -4, -5],k = -1) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],k = 0) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5],k = -20) == 0
    assert candidate(nums = [1, 0, -1],k = 0) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 1
    assert candidate(nums = [10, 20, 30, 40, 50],k = 0) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],k = 15) == 5
    assert candidate(nums = [100, -50, 200, -300, 400, -500, 600, -700, 800, -900],k = 100) == 2
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = -15) == 5
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = -15) == 5
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 0) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 45) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 5
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 15) == 0
    assert candidate(nums = [10000, -5000, 5000, 20000, -10000, 0, 10000],k = 20000) == 6
    assert candidate(nums = [10, 20, -30, 40, -50, 60, -70, 80, -90, 100],k = 100) == 1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 0) == 10
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = -25) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 200) == 16
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0],k = 0) == 9
    assert candidate(nums = [-100, 100, -100, 100, -100, 100],k = 0) == 6
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],k = -15) == 5
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = -5) == 9
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = -15) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = -15) == 5
    assert candidate(nums = [10000, -10000, 20000, -20000, 30000, -30000, 40000, -40000, 50000],k = 150000) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 27) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 30) == 5
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = -5) == 9
    assert candidate(nums = [100, -50, 50, -50, 50, -50, 50],k = 50) == 6
    assert candidate(nums = [10, 20, -30, 30, 10, -20, 40, -10],k = 10) == 5
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000],k = 10000) == 5
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 0) == 10
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20],k = -50) == 0
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000, -1000000],k = 0) == 10
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 0) == 28
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 130) == 13
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],k = 0) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 5
    assert candidate(nums = [100, -50, 50, -25, 25, -10, 10, -5, 5, 0, 0, 0],k = 75) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5],k = 9) == 8
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 5) == 9
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 100],k = 100) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400],k = 0) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 25) == 5
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 0) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 100) == 8
    assert candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],k = 10) == 17
    assert candidate(nums = [-1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000],k = 0) == 10
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 2) == 5
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 5) == 10
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 0) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5],k = 15) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 5
    assert candidate(nums = [1, 2, 3, -6, 5, 4, -3, 2, 1],k = 7) == 7
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 0) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = -1) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2500) == 5
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 5) == 9
    assert candidate(nums = [1, 2, -3, 4, 5, 6, -7, 8, 9, -10],k = 10) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 15) == 6
    assert candidate(nums = [1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2],k = 3) == 9
    assert candidate(nums = [5, -3, 5, -3, 5, -3, 5, -3, 5, -3, 5, -3, 5, -3, 5],k = 5) == 9
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = -5) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 90) == 12
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = -100) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 25) == 5
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 15) == 6
    assert candidate(nums = [10000, -9999, 10000, -9999, 10000, -9999, 10000, -9999, 10000, -9999],k = 10000) == 1
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 35000) == 7
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 5) == 10
    assert candidate(nums = [1, 2, -3, 3, -1, 2, -1, 1, -1, 2, -1, 1, -1, 2, -1],k = 2) == 13
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 10) == 5
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3500) == 7
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3000) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 5
    assert candidate(nums = [100, -50, 25, -25, 10, -10, 5, -5, 2, -2, 1, -1],k = 50) == 12
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 70) == 0
    assert candidate(nums = [3, -2, -1, 5, 6, -2, 1, 4, -1, 2],k = 7) == 6
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 0) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 8
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 0) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 15) == 5
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 0) == 0
    assert candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 5) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55],k = 0) == 11
    assert candidate(nums = [10, 20, 30, -10, -20, 10, 20, -30],k = 20) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10],k = 10) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100) == 0
