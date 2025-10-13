# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(plants = [1000000],capacity = 1000000) == 1
    assert candidate(plants = [3, 2, 4, 2, 1],capacity = 6) == 17
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = 1) == 100
    assert candidate(plants = [5, 5, 5, 5, 5],capacity = 5) == 25
    assert candidate(plants = [10, 10, 10],capacity = 10) == 9
    assert candidate(plants = [1, 1, 1, 4, 2, 3],capacity = 4) == 30
    assert candidate(plants = [1, 2, 3, 4, 5],capacity = 10) == 13
    assert candidate(plants = [1, 2, 3],capacity = 6) == 3
    assert candidate(plants = [5, 8, 6],capacity = 10) == 9
    assert candidate(plants = [1, 1, 1, 1, 1],capacity = 5) == 5
    assert candidate(plants = [2, 2, 3, 3],capacity = 5) == 14
    assert candidate(plants = [3, 2, 4, 2, 1],capacity = 4) == 17
    assert candidate(plants = [7, 7, 7, 7, 7, 7, 7],capacity = 8) == 49
    assert candidate(plants = [2, 4, 5, 1, 2],capacity = 6) == 17
    assert candidate(plants = [10],capacity = 10) == 1
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 15) == 146
    assert candidate(plants = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],capacity = 5) == 961
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 25) == 242
    assert candidate(plants = [9, 8, 7, 6, 5, 4, 3, 2, 1],capacity = 10) == 41
    assert candidate(plants = [2, 3, 2, 1, 4, 2, 1, 3, 2, 1, 4, 2, 1],capacity = 6) == 77
    assert candidate(plants = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],capacity = 3) == 138
    assert candidate(plants = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],capacity = 50) == 88
    assert candidate(plants = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],capacity = 10) == 362
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 10) == 200
    assert candidate(plants = [2, 4, 5, 1, 2],capacity = 5) == 17
    assert candidate(plants = [7, 2, 5, 9, 3, 8, 4, 6, 1, 1, 1, 1],capacity = 15) == 42
    assert candidate(plants = [1, 3, 2, 4, 2, 1, 3, 2, 1, 4, 2, 1],capacity = 5) == 78
    assert candidate(plants = [5, 8, 6, 10, 2, 1, 1, 1, 1, 1],capacity = 12) == 32
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacity = 20) == 152
    assert candidate(plants = [2, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8],capacity = 12) == 71
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacity = 10) == 54
    assert candidate(plants = [9, 1, 5, 3, 7, 8, 4, 2],capacity = 10) == 42
    assert candidate(plants = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],capacity = 20) == 213
    assert candidate(plants = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],capacity = 30) == 2881
    assert candidate(plants = [2, 4, 6, 8, 10],capacity = 10) == 23
    assert candidate(plants = [1000000, 500000, 1000000, 500000, 1000000, 500000],capacity = 1000000) == 36
    assert candidate(plants = [100, 200, 300, 400, 500],capacity = 1000) == 13
    assert candidate(plants = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],capacity = 3) == 900
    assert candidate(plants = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capacity = 150) == 68
    assert candidate(plants = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],capacity = 15) == 4499
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacity = 10) == 88
    assert candidate(plants = [1, 3, 2, 5, 4, 3, 2, 1],capacity = 5) == 50
    assert candidate(plants = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],capacity = 3) == 400
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacity = 18) == 52
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacity = 10) == 249
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacity = 15) == 68
    assert candidate(plants = [9, 1, 2, 3, 4, 5, 6, 7, 8],capacity = 10) == 65
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 10) == 200
    assert candidate(plants = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],capacity = 20) == 88
    assert candidate(plants = [5, 8, 6, 7, 4, 9],capacity = 12) == 28
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 4) == 400
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacity = 5) == 84
    assert candidate(plants = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],capacity = 5) == 200
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 25) == 180
    assert candidate(plants = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],capacity = 15) == 225
    assert candidate(plants = [2, 4, 6, 8, 10],capacity = 12) == 19
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 10) == 127
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = 2) == 511
    assert candidate(plants = [3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],capacity = 4) == 407
    assert candidate(plants = [5, 8, 6, 7, 9, 4, 2],capacity = 10) == 37
    assert candidate(plants = [7, 3, 5, 8, 10, 2, 6, 4, 9, 1],capacity = 15) == 52
    assert candidate(plants = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],capacity = 20) == 78
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = 1) == 6724
    assert candidate(plants = [7, 3, 6, 2, 5, 4, 9, 1, 8],capacity = 12) == 49
    assert candidate(plants = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9],capacity = 15) == 126
    assert candidate(plants = [100, 200, 100],capacity = 150) == 9
    assert candidate(plants = [100, 200, 300, 400, 500],capacity = 1000) == 13
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacity = 15) == 38
    assert candidate(plants = [100, 200, 300, 400, 500],capacity = 500) == 23
    assert candidate(plants = [5, 8, 6, 10, 2, 9, 4],capacity = 12) == 41
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = 5) == 2878
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 10) == 10082
    assert candidate(plants = [1000000, 1000000, 1000000],capacity = 1000000) == 9
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacity = 10) == 249
    assert candidate(plants = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],capacity = 10) == 146
    assert candidate(plants = [9, 8, 7, 6, 5, 4, 3, 2, 1],capacity = 5) == 67
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = 15) == 46
    assert candidate(plants = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],capacity = 14) == 200
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],capacity = 25) == 296
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],capacity = 20) == 177
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],capacity = 15) == 368
    assert candidate(plants = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],capacity = 14) == 200
    assert candidate(plants = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],capacity = 10) == 276
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = 1) == 900
