# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [-1, 2, -3, 4, -5],k = 3) == 1
    assert candidate(nums = [-1, 2],k = 2) == 1
    assert candidate(nums = [2, -1, 2],k = 3) == 3
    assert candidate(nums = [2, 1, 5, 1, 3, 2],k = 7) == 3
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 3) == -1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 5
    assert candidate(nums = [2, -2, 2, -4, 3, -1, 2, -1, 2, -4, 3, -1],k = 5) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 5
    assert candidate(nums = [1],k = 1) == 1
    assert candidate(nums = [5, 4, 3, 2, 1],k = 5) == 1
    assert candidate(nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8],k = 15) == 2
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 15) == -1
    assert candidate(nums = [1, 2, 3, 4, 5],k = 16) == -1
    assert candidate(nums = [48, 99, 37, 4, -31],k = 140) == 2
    assert candidate(nums = [10, 20, 30, 40, 50],k = 100) == 3
    assert candidate(nums = [8],k = 8) == 1
    assert candidate(nums = [8, 2, 4, -6, 7, -4, 3, 5],k = 10) == 2
    assert candidate(nums = [1, 2],k = 4) == -1
    assert candidate(nums = [2, -2, 2, 2, -2, 2, 2, -2, 2, 2],k = 4) == 2
    assert candidate(nums = [8],k = 10) == -1
    assert candidate(nums = [2, -1, 2],k = 2) == 1
    assert candidate(nums = [5],k = 5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],k = 15) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 250) == 3
    assert candidate(nums = [10, 5, 2, 7],k = 15) == 2
    assert candidate(nums = [10, -2, 5, -1, 3, -1, -2, 4, 7, -5, 2],k = 10) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 55) == 10
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000, 100000],k = 500000) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = -15) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -1
    assert candidate(nums = [1, 2, -1, 2, -1, 2, -1, 2, -1],k = 3) == 2
    assert candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 150) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 550) == 10
    assert candidate(nums = [8, 2, 4, -2, 3, 1, 5],k = 10) == 2
    assert candidate(nums = [100, -25, 100, -25, 100, -25, 100, -25, 100, -25],k = 200) == 5
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 25) == 3
    assert candidate(nums = [10, 20, -30, 40, 50, -60, 70, -80],k = 150) == -1
    assert candidate(nums = [-1, 2, 3, 4, -10, 5, 6],k = 10) == 2
    assert candidate(nums = [10000, 20000, -30000, 40000, 50000, -60000, 70000, -80000],k = 100000) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 3
    assert candidate(nums = [10, -1, -2, 3, 4, -5, 6, -7, 8, -9],k = 15) == 7
    assert candidate(nums = [100000, -50000, 50000, -25000, 25000, -12500, 12500, 6250],k = 250000) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1500) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 55) == 5
    assert candidate(nums = [100000, -50000, 200000, -150000, 300000],k = 600000) == -1
    assert candidate(nums = [1, 0, 1, 1, 1, 0, 1, -1, 1, 1, 1],k = 4) == 5
    assert candidate(nums = [50, 40, 30, 20, 10],k = 90) == 2
    assert candidate(nums = [100000, -100000, 100000, -100000, 100000],k = 100000) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 10
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 55) == 10
    assert candidate(nums = [-5, -4, -3, -2, -1],k = -15) == 1
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 100) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [8, 2, -4, 1, 6, -5, 4],k = 10) == 2
    assert candidate(nums = [10, -10, 10, -10, 10],k = 20) == -1
    assert candidate(nums = [100000, -50000, 50000, -25000, 25000, -12500, 12500],k = 100000) == 1
    assert candidate(nums = [5, -1, 5, -1, 5, -1, 5, -1, 5, -1],k = 15) == 7
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],k = 4000000000) == 4
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 5) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 500) == 8
    assert candidate(nums = [100000, -99999, 100000, -99999, 100000],k = 1) == 1
    assert candidate(nums = [-1, -2, -3, 10, -5, 2, -1, 3],k = 5) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 1) == 1
    assert candidate(nums = [84, -37, 32, 40, 95],k = 167) == 3
    assert candidate(nums = [10, 20, 30, 40, 50],k = 150) == 5
    assert candidate(nums = [5, -1, 5, -1, 5, -1],k = 10) == 5
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1500) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 2
    assert candidate(nums = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 7) == 1
    assert candidate(nums = [-100, 150, -200, 250, -300, 350, -400, 450, -500, 550],k = 1500) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5],k = 9) == 2
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 100) == 6
    assert candidate(nums = [3, -2, 5, -1, 2, -3, 1, 4],k = 7) == 5
    assert candidate(nums = [8, 2, -5, 7, 11, -10, 15, 1],k = 15) == 1
    assert candidate(nums = [3, 4, 5, 1, 2, 7, 8, 9, 10, 1],k = 25) == 3
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100],k = 100) == 1
    assert candidate(nums = [8, 2, 4, -1, 0, 5, -3, 2],k = 16) == 6
    assert candidate(nums = [5, 1, 3, 5, 2, 4, 6, 1, 7, 8],k = 20) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 2
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 15) == -1
    assert candidate(nums = [3, -2, 5, -1, 4],k = 6) == 3
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == 1
    assert candidate(nums = [10, 20, 30, -10, -20, -30, 40, 50, 60],k = 100) == 2
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 1) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 5) == 1
    assert candidate(nums = [5, -2, 4, 6, -1, 3, -3, 2, 7, -8],k = 12) == 4
    assert candidate(nums = [5, 1, -1, 5, 10, -10, 20, -20, 30, -30],k = 15) == 1
    assert candidate(nums = [1, -1, 5, -2, 3],k = 3) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 75) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 50) == 3
    assert candidate(nums = [10, 20, 30, -10, -20, -30, 40, 50, -40, -50, 60, 70],k = 100) == 2
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5500) == 10
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0],k = 10) == 5
    assert candidate(nums = [5, 2, 3, -2, 4, 5, 1, -1, 2, -3, 6, 7, 8, -4, 5, 6],k = 20) == 3
    assert candidate(nums = [100, -25, 25, -25, 25, -25, 25, -25, 25],k = 50) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 120) == 15
    assert candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2],k = 1) == 1
    assert candidate(nums = [8, 2, -3, 7, 2, -4, 6, -8],k = 5) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 1) == 1
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 5) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 1) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 90) == 8
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == -1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == -1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 5
    assert candidate(nums = [5, -2, 3, 8, -4, 7],k = 10) == 2
    assert candidate(nums = [10, -1, 20, -2, 30, -3, 40, -4, 50, -5],k = 100) == 5
    assert candidate(nums = [-1, 1, 1, -1, 1, 1, 1, -1, 1],k = 2) == 2
    assert candidate(nums = [100000],k = 100000) == 1
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 50) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 6
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 45) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 55) == 10
    assert candidate(nums = [1, 2, 3, 4, 5],k = 15) == 5
    assert candidate(nums = [5, -2, 5, -2, 5, -2, 5, -2, 5, -2],k = 10) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 1) == -1
    assert candidate(nums = [-100000, -100000, -100000, -100000, -100000],k = 100000) == -1
    assert candidate(nums = [1, 2, 3, -6, 4, 5, -3, 2, 1, 0, -1, 2, 3, -5, 6, 7],k = 15) == 9
    assert candidate(nums = [8, 2, -3, 4, 6, -5, 2, 7],k = 15) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100) == -1
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5],k = 20) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 550) == 10
