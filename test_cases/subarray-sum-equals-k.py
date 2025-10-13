# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [2, 2, 2, 2, 2],k = 4) == 4
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 8
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 55
    assert candidate(nums = [1, 2, 1, 2, 1],k = 3) == 4
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1500) == 1
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000],k = 0) == 6
    assert candidate(nums = [1, 2, 3, 4, 5],k = 9) == 2
    assert candidate(nums = [1],k = 1) == 1
    assert candidate(nums = [1, 1, 1],k = 2) == 2
    assert candidate(nums = [100, -100, 200, -200, 300, -300],k = 0) == 6
    assert candidate(nums = [-1, -1, 1],k = 0) == 1
    assert candidate(nums = [10, 20, 30, 40, 50],k = 100) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 3
    assert candidate(nums = [1, -1, 5, -2, 3],k = 3) == 3
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4],k = 0) == 10
    assert candidate(nums = [1, 0, -1, 0, -1, 0, 1],k = 0) == 8
    assert candidate(nums = [10, 20, 30, 40, 50],k = 150) == 1
    assert candidate(nums = [3, 4, 7, 2, -3, 1, 4, 2],k = 7) == 4
    assert candidate(nums = [1, -1, 0],k = 0) == 3
    assert candidate(nums = [-1, -2, -3],k = -6) == 1
    assert candidate(nums = [-1, -1, 1, 1, 0],k = 0) == 4
    assert candidate(nums = [1, 2, 3],k = 3) == 2
    assert candidate(nums = [-1, -1, 2],k = 1) == 1
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000],k = 0) == 6
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 16
    assert candidate(nums = [1000, -1000, 2000, -2000, 3000],k = 0) == 3
    assert candidate(nums = [1, -1, 0, 1, -1, 1, -1],k = 0) == 13
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 10000) == 1
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],k = 1000) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1],k = 0) == 16
    assert candidate(nums = [1, 3, -2, 5, 6, -4, 2, 3],k = 5) == 3
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 6
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15) == 8
    assert candidate(nums = [10, 20, 30, -10, -20, -30, 40, 50, -40, -50],k = 30) == 5
    assert candidate(nums = [1, -1, 0, 1, -1, 2],k = 0) == 7
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5],k = 10) == 6
    assert candidate(nums = [100, -100, 50, 50, -50, 50, -100, 100],k = 0) == 10
    assert candidate(nums = [-10, 0, 10, -10, 0, 10],k = 0) == 9
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5000) == 0
    assert candidate(nums = [10, -5, 10, -5, 10],k = 5) == 4
    assert candidate(nums = [1, -1, 1, -1, 1, -1],k = 0) == 9
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1000) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0],k = 0) == 28
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = -15) == 3
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 100) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1500) == 3
    assert candidate(nums = [1, -2, 1, 2, -1, 2, 3, 4, -2, 1],k = 3) == 5
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = -3) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],k = 5) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 16
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 3000) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 3) == 9
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 55
    assert candidate(nums = [0, 0, 0, 0, 0],k = 0) == 15
    assert candidate(nums = [-10, -20, -30, -40, -50],k = -70) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 6
    assert candidate(nums = [1, 3, 4, 5, 7, 8, 10, 11, 12, 13],k = 20) == 2
    assert candidate(nums = [1, -1, 0, 0, 1, -1],k = 0) == 11
    assert candidate(nums = [10, -5, 2, -3, 1, 5, -2],k = 7) == 1
    assert candidate(nums = [1, -1, 0, 0, 1],k = 0) == 7
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2500) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 6
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10],k = 0) == 25
    assert candidate(nums = [-10, 100, -100, 50, -50, 25, -25],k = 0) == 6
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 0) == 15
    assert candidate(nums = [1, 2, 3, -6, 2, 3, 4, -10, 2, 3, 4, 5],k = 5) == 6
    assert candidate(nums = [-10, -20, 10, 20, 10, -10, -20, 10, 20],k = 0) == 6
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 0) == 16
    assert candidate(nums = [10, 20, 30, 40, 50],k = 70) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 150) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 15) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 3
    assert candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],k = -5000) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 0) == 25
    assert candidate(nums = [1, -1, 5, -2, 3],k = 3) == 3
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000],k = 0) == 25
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 50) == 2
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1],k = 0) == 12
    assert candidate(nums = [100, 200, 300, 400, 500, 600],k = 1500) == 2
    assert candidate(nums = [5, 5, 5, 5, 5],k = 15) == 3
    assert candidate(nums = [0, 0, 0, 0, 0],k = 0) == 15
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 2) == 0
    assert candidate(nums = [1, 2, -1, 2, -1, 1],k = 2) == 5
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9],k = -5) == 3
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 5) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 2
    assert candidate(nums = [1, 2, 3, 4, 5],k = 9) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 6
    assert candidate(nums = [-1000, 1000, -1000, 1000, -1000, 1000],k = 0) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 50) == 1
    assert candidate(nums = [1, 2, 1, 2, 1],k = 3) == 4
    assert candidate(nums = [3, 4, 7, 2, -3, 1, 4, 2, 0, 1],k = 7) == 7
    assert candidate(nums = [10, 2, -2, -20, 10],k = -10) == 3
    assert candidate(nums = [0, 0, 0, 0, 0, 0],k = 0) == 21
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000],k = 0) == 9
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 30) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],k = 15) == 1
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],k = -150) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 1
    assert candidate(nums = [-1, 0, 1, -1, 0, 1],k = 0) == 9
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5],k = 5) == 10
