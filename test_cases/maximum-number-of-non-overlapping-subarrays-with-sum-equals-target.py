# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 5, 5, 5, 5],target = 10) == 2
    assert candidate(nums = [1, 2, 3, 4, 5],target = 9) == 1
    assert candidate(nums = [-1, 3, 5, 1, 4, 2, -9],target = 6) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5],target = 15) == 2
    assert candidate(nums = [0, 0, 0, 0, 0],target = 0) == 5
    assert candidate(nums = [1, -1, 2, -2, 3, -3],target = 0) == 3
    assert candidate(nums = [1, 1, 1, 1, 1],target = 2) == 2
    assert candidate(nums = [5, 5, 5, 5, 5],target = 15) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 3
    assert candidate(nums = [10, -5, 5, -3, 2, 3, -1, 7],target = 5) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == 1
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 38) == 1
    assert candidate(nums = [-2, 2, -2, 2, -2, 2, -2, 2, -2, 2],target = 0) == 5
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],target = 0) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -1, -2, -3, -4, -5, -1, -2, -3, -4, -5],target = -15) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 2
    assert candidate(nums = [100, -25, 25, -50, 50, 150, -150, 200, -200],target = 100) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 0, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = 5) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5, -10, 1, 2, 3],target = 10) == 2
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],target = 0) == 10
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -15) == 2
    assert candidate(nums = [1000, -500, 500, -300, 200, 300, -100, 700],target = 500) == 3
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 9) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == 30
    assert candidate(nums = [5, -2, 5, -2, 5, -2, 5, -2, 5, -2],target = 3) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == 10
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 6) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == 1
    assert candidate(nums = [100, -50, 50, -25, 25, 125, -125, 62, -62, 31, -31],target = 50) == 2
    assert candidate(nums = [5, 1, 3, 7, 8, 2, 4, 6, 9, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9],target = 5) == 2
    assert candidate(nums = [10, 5, 5, 15, 10, 10, 5, 5, 20, 15],target = 20) == 3
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000],target = 10000) == 3
    assert candidate(nums = [3, 4, -2, 3, -2, 5, -5, 1, 1, 1],target = 3) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 2) == 10
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],target = 2) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 4
    assert candidate(nums = [2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],target = 9) == 3
    assert candidate(nums = [10, 5, -5, 10, 15, -25, 30, -30, 35, -35, 40, -40, 45, -45, 50, -50, 55, -55, 60, -60],target = 10) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],target = 55) == 2
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],target = -5) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5],target = 9) == 2
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 1500) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 3
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],target = -30) == 2
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],target = 0) == 10
    assert candidate(nums = [100, -100, 200, -200, 300, -300, 400, -400, 500, -500],target = 100) == 5
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],target = 0) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1) == 20
    assert candidate(nums = [100, -25, 25, -50, 50, -75, 75, -100, 100, -125, 125],target = 50) == 2
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],target = 0) == 27
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == 3
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 9) == 3
    assert candidate(nums = [100, -25, 25, -25, 25, 25, -50, 25, -25, 25, 25, -50, 100, -200, 100],target = 25) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 1, 2, 3, 4, 5],target = 5) == 4
    assert candidate(nums = [5, 1, 3, 7, 2, 8, 6, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == 5
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10],target = 0) == 10
    assert candidate(nums = [9, 3, 6, 9, 3, 6, 9, 3, 6, 9],target = 12) == 3
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 10
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],target = 0) == 10
    assert candidate(nums = [1, -1, 0, 1, 0, -1, 1],target = 0) == 4
    assert candidate(nums = [3, 2, 1, 6, 3, 3, 2, 1, 6, 3, 3, 2, 1, 6, 3],target = 9) == 4
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],target = 0) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 55) == 1
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 3) == 5
    assert candidate(nums = [100, -50, 50, -25, 25, -10, 10, 5, -5, 15, -15],target = 25) == 3
    assert candidate(nums = [-1, -2, -3, -4, -5, 10, 5, 0, -5, -10, 1, 2, 3, 4, 5],target = 0) == 3
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == 10
    assert candidate(nums = [1000, -500, 500, -250, 250, -125, 125, 0, 0, 0, 0, 0, 0, 0, 0],target = 250) == 2
    assert candidate(nums = [-2, 2, 3, -3, 4, 5, -5, 4, 6, -6, 7, -7, 8, -8],target = 0) == 6
    assert candidate(nums = [5, 1, 3, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 6) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 8
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],target = 0) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 150) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 8
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],target = 75) == 2
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 20) == 1
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5],target = 5) == 5
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100, 110, -120, 130, -140, 150, -160, 170, -180, 190, -200],target = 100) == 1
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 100) == 2
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1],target = 0) == 6
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6],target = 10) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == 20
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000],target = 10000) == 3
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 75) == 2
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],target = -15) == 3
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10],target = 0) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == 3
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5],target = 0) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == 15
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 100) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 15) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 28) == 1
