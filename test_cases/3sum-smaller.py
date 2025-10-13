# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 2, 3, 1],target = 7) == 1
    assert candidate(nums = [5, 0, 1, 3, -1],target = 4) == 3
    assert candidate(nums = [5, 2, 6, -1, 3, 1],target = 4) == 2
    assert candidate(nums = [5, 2, 6, 4, 5, 1, 6],target = 13) == 19
    assert candidate(nums = [-2, 0, 1, 3, 5],target = 4) == 4
    assert candidate(nums = [0],target = 0) == 0
    assert candidate(nums = [-5, 1, 3, 4, 5],target = 5) == 6
    assert candidate(nums = [-2, 0, 1, 3],target = 2) == 2
    assert candidate(nums = [-1, 0, 1, 2, -1, -4],target = 0) == 12
    assert candidate(nums = [-2, 0, 1, 3, 2],target = 3) == 5
    assert candidate(nums = [-2, 0, -1, 1, -3, 2],target = 2) == 18
    assert candidate(nums = [-1, -1, -1, -1],target = -3) == 0
    assert candidate(nums = [-1, 0, 1, 2, -1, -4],target = -1) == 10
    assert candidate(nums = [1, 2, 3, 4, 5],target = 0) == 0
    assert candidate(nums = [1, 1, 1, 1],target = 4) == 4
    assert candidate(nums = [-2, 0, -1, 3, -4],target = 2) == 9
    assert candidate(nums = [],target = 0) == 0
    assert candidate(nums = [100, -100, 50, -50, 25, -25],target = 0) == 10
    assert candidate(nums = [1, 2, 3, 4, 5],target = 15) == 10
    assert candidate(nums = [0, 0, 0, 0],target = 1) == 4
    assert candidate(nums = [1, 1, 1, 1, 1],target = 5) == 10
    assert candidate(nums = [1, 1, 1, 1],target = 5) == 4
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],target = -15) == 64
    assert candidate(nums = [30, 20, 10, 0, -10, -20, -30, 5, -5, 15, -15],target = 10) == 100
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1],target = 0) == 476
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -15) == 70
    assert candidate(nums = [30, -40, 50, 10, -20, 0, 5],target = 10) == 14
    assert candidate(nums = [-1, -1, -1, 0, 0, 0, 1, 1, 1, 2],target = 0) == 28
    assert candidate(nums = [-1, 0, 1, 2, -1, -4, 3, 5],target = 3) == 31
    assert candidate(nums = [-10, -20, 10, 20, 30, -30, 0, 5, 15],target = 0) == 31
    assert candidate(nums = [-1, -1, -1, 0, 0, 0, 1, 1, 1],target = 1) == 56
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 0) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 8) == 30
    assert candidate(nums = [100, -50, 25, -25, 0, -100, 50],target = 20) == 19
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 15) == 392
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 116
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3],target = 0) == 15
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 120
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 0
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85],target = 250) == 0
    assert candidate(nums = [-10, -20, -30, 0, 10, 20, 30],target = -5) == 15
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -10) == 109
    assert candidate(nums = [-1, 0, 1, 2, -1, -4, 3, 2, 1, -2],target = 3) == 89
    assert candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95],target = 1) == 60
    assert candidate(nums = [-50, -25, -10, -5, 0, 5, 10, 25, 50],target = 0) == 40
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 56
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 300) == 120
    assert candidate(nums = [-50, -40, -30, -20, -10, 10, 20, 30, 40, 50],target = 10) == 64
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],target = 1) == 64
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],target = 0) == 76
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],target = 100) == 60
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 15) == 0
    assert candidate(nums = [-10, -5, -3, -2, 1, 2, 3, 5, 7, 10],target = 0) == 44
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 10) == 455
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],target = 0) == 40
    assert candidate(nums = [30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30],target = -10) == 99
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 180) == 70
    assert candidate(nums = [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 0) == 640
    assert candidate(nums = [50, 25, 75, 100, 0, -25, -50, -75, -100, 200],target = 100) == 72
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 20) == 89
    assert candidate(nums = [-10, -5, -3, 0, 1, 2, 3, 5, 6, 10],target = 0) == 42
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 455
    assert candidate(nums = [-10, -5, -3, -2, 0, 1, 2, 3, 5, 7],target = -1) == 53
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 30) == 67
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = -1) == 64
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 3) == 0
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 200) == 89
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 150) == 40
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 250) == 116
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3],target = 9) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 200) == 89
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],target = 285) == 76
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 30) == 353
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],target = -3) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9],target = -15) == 41
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 40
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],target = -5) == 0
    assert candidate(nums = [-5, 0, 5, 10, 15, 20, -10, -15, -20],target = 5) == 46
    assert candidate(nums = [-10, 0, 10, 20, 30, -30],target = 0) == 6
    assert candidate(nums = [-10, -5, 0, 2, 5, 8],target = 0) == 9
    assert candidate(nums = [35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35],target = 0) == 215
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],target = 0) == 56
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 6) == 6
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 10) == 70
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86],target = 270) == 41
    assert candidate(nums = [10, 20, 30, 40, 50, 60],target = 150) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 20) == 122
    assert candidate(nums = [-10, 0, 10, 20, -20, 30],target = 0) == 4
    assert candidate(nums = [-10, -5, -1, 0, 1, 2, 5, 10],target = 3) == 33
    assert candidate(nums = [100, -100, 50, -50, 25, -25],target = 0) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 20) == 16
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 1140
    assert candidate(nums = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90],target = -285) == 40
    assert candidate(nums = [-10, -5, -1, 0, 1, 2, 3, 4, 5, 10],target = 0) == 42
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = 1) == 89
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 40
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],target = -2) == 120
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],target = 0) == 83
    assert candidate(nums = [-1, -2, -3, -4, -5],target = -7) == 8
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],target = -5) == 31
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5],target = 0) == 63
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 75, -75, 0, 1, -1],target = 0) == 78
    assert candidate(nums = [100, -100, 50, -50, 20, -20, 30, -30, 40, -40],target = 0) == 59
    assert candidate(nums = [100, -100, 99, -99, 98, -98, 97, -97, 96, -96, 95, -95, 94, -94, 93],target = 0) == 203
