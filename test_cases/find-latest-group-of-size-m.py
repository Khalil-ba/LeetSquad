# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [1, 2, 3, 4, 5],m = 3) == 3
    assert candidate(arr = [1, 3, 5, 2, 4],m = 1) == 4
    assert candidate(arr = [2, 1, 3, 5, 4],m = 1) == 4
    assert candidate(arr = [3, 5, 1, 2, 4],m = 1) == 4
    assert candidate(arr = [5, 4, 3, 2, 1],m = 1) == 1
    assert candidate(arr = [5, 4, 3, 2, 1],m = 2) == 2
    assert candidate(arr = [3, 1, 5, 4, 2],m = 2) == -1
    assert candidate(arr = [1, 3, 2, 5, 4],m = 1) == 4
    assert candidate(arr = [1, 3, 5, 2, 4],m = 2) == -1
    assert candidate(arr = [2, 5, 8, 1, 4, 7, 10, 3, 6, 9],m = 3) == -1
    assert candidate(arr = [15, 1, 13, 2, 14, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8],m = 5) == 11
    assert candidate(arr = [1, 2, 3, 4, 5, 6],m = 3) == 3
    assert candidate(arr = [8, 5, 10, 1, 9, 3, 6, 7, 4, 2],m = 2) == 7
    assert candidate(arr = [3, 2, 5, 1, 4, 6, 7, 8],m = 3) == 4
    assert candidate(arr = [3, 6, 2, 8, 1, 9, 4, 7, 5, 10],m = 3) == 6
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 6) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 3) == 3
    assert candidate(arr = [5, 10, 1, 2, 6, 8, 4, 7, 9, 3],m = 5) == 8
    assert candidate(arr = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9],m = 3) == -1
    assert candidate(arr = [1, 10, 5, 6, 7, 8, 9, 2, 3, 4],m = 3) == 9
    assert candidate(arr = [5, 3, 1, 2, 4, 9, 7, 6, 8, 10],m = 1) == 8
    assert candidate(arr = [1, 2, 5, 6, 3, 4, 7, 8, 10, 9],m = 3) == 5
    assert candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],m = 2) == -1
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 5) == 5
    assert candidate(arr = [1, 4, 7, 10, 2, 5, 8, 11, 3, 6, 9, 12],m = 2) == 10
    assert candidate(arr = [5, 1, 9, 2, 6, 3, 7, 4, 8, 10],m = 3) == 7
    assert candidate(arr = [10, 1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 11],m = 7) == 16
    assert candidate(arr = [1, 5, 9, 2, 6, 3, 7, 4, 8, 10],m = 2) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 1) == 1
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 6) == 6
    assert candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9],m = 2) == 3
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 10) == 10
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 1) == 1
    assert candidate(arr = [2, 4, 1, 6, 5, 3],m = 2) == 5
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 5) == 5
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 4) == 4
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 10) == 10
    assert candidate(arr = [6, 2, 5, 9, 7, 8, 3, 1, 10, 4],m = 5) == 8
    assert candidate(arr = [1, 6, 4, 3, 2, 5],m = 1) == 5
    assert candidate(arr = [5, 1, 6, 3, 8, 2, 7, 10, 4, 9],m = 3) == 8
    assert candidate(arr = [1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8],m = 7) == 14
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 2) == 2
    assert candidate(arr = [10, 5, 2, 7, 1, 8, 3, 6, 9, 4],m = 3) == 9
    assert candidate(arr = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9],m = 1) == 9
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 5) == 5
    assert candidate(arr = [6, 5, 4, 3, 2, 1],m = 3) == 3
    assert candidate(arr = [7, 3, 10, 8, 6, 9, 1, 5, 4, 2],m = 4) == -1
    assert candidate(arr = [1, 2, 5, 4, 3, 6, 7, 8, 9, 10],m = 2) == 4
    assert candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],m = 9) == -1
    assert candidate(arr = [3, 6, 1, 9, 7, 8, 2, 5, 10, 4],m = 3) == 9
    assert candidate(arr = [3, 1, 7, 5, 9, 2, 8, 6, 10, 4],m = 4) == -1
    assert candidate(arr = [6, 7, 8, 1, 2, 3, 4, 5, 12, 11, 9, 10],m = 6) == -1
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 1) == 1
    assert candidate(arr = [10, 5, 1, 6, 3, 8, 9, 2, 7, 4],m = 2) == 8
    assert candidate(arr = [3, 5, 2, 1, 4, 6, 8, 7, 10, 9],m = 1) == 9
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],m = 4) == 9
    assert candidate(arr = [1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19, 10, 20],m = 10) == -1
    assert candidate(arr = [3, 1, 5, 7, 6, 2, 8, 4, 9, 10],m = 2) == -1
    assert candidate(arr = [1, 2, 5, 6, 3, 4, 9, 10, 7, 8],m = 2) == 9
    assert candidate(arr = [1, 10, 3, 8, 5, 12, 7, 2, 9, 4, 6, 11],m = 4) == 10
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 5) == 5
    assert candidate(arr = [6, 5, 8, 4, 7, 10, 9, 1, 2, 3],m = 3) == 4
    assert candidate(arr = [9, 5, 10, 1, 2, 3, 4, 6, 7, 8],m = 4) == -1
    assert candidate(arr = [3, 1, 4, 2, 5, 6, 7, 8, 9, 10],m = 3) == -1
    assert candidate(arr = [6, 2, 3, 1, 5, 4],m = 2) == 5
    assert candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],m = 1) == 8
    assert candidate(arr = [6, 3, 1, 5, 4, 2],m = 1) == 5
    assert candidate(arr = [5, 1, 9, 3, 7, 2, 8, 6, 4, 10],m = 2) == -1
    assert candidate(arr = [5, 2, 1, 8, 3, 4, 7, 6, 10, 9],m = 2) == 7
    assert candidate(arr = [10, 2, 8, 4, 6, 3, 9, 5, 7, 1],m = 3) == 8
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 3) == 3
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],m = 5) == 5
    assert candidate(arr = [5, 1, 6, 3, 4, 2],m = 1) == 5
    assert candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],m = 4) == 5
    assert candidate(arr = [5, 1, 9, 10, 3, 7, 4, 6, 8, 2],m = 3) == 7
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 3) == 3
    assert candidate(arr = [6, 4, 2, 8, 10, 1, 3, 5, 7, 9],m = 2) == 6
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 1) == 1
    assert candidate(arr = [3, 1, 4, 2, 6, 5, 7, 10, 9, 8],m = 4) == 5
    assert candidate(arr = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],m = 2) == 6
    assert candidate(arr = [5, 1, 7, 10, 3, 8, 4, 6, 9, 2],m = 4) == -1
    assert candidate(arr = [3, 6, 1, 8, 2, 7, 4, 9, 5, 10],m = 1) == 5
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16],m = 8) == -1
    assert candidate(arr = [1, 2, 4, 5, 3, 7, 6, 8, 10, 9],m = 2) == 4
    assert candidate(arr = [6, 3, 5, 1, 2, 4, 9, 7, 8, 10],m = 4) == -1
    assert candidate(arr = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],m = 5) == -1
    assert candidate(arr = [1, 5, 3, 9, 7, 2, 6, 10, 4, 8],m = 1) == 7
    assert candidate(arr = [7, 5, 3, 1, 9, 10, 8, 6, 4, 2],m = 5) == -1
    assert candidate(arr = [5, 3, 8, 6, 2, 4, 1, 7, 9, 10],m = 3) == -1
    assert candidate(arr = [3, 2, 5, 4, 8, 7, 10, 9, 6, 1],m = 4) == 8
    assert candidate(arr = [1, 6, 10, 3, 5, 9, 2, 4, 8, 7],m = 4) == -1
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],m = 4) == 9
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 2) == 2
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 4) == 4
    assert candidate(arr = [5, 3, 1, 2, 4, 6, 7, 8, 9, 10],m = 3) == 4
    assert candidate(arr = [5, 1, 9, 3, 7, 2, 8, 10, 4, 6],m = 5) == 9
    assert candidate(arr = [3, 6, 9, 2, 5, 8, 1, 4, 7, 10],m = 2) == 8
    assert candidate(arr = [10, 2, 6, 4, 7, 9, 1, 8, 5, 3],m = 5) == 8
    assert candidate(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],m = 3) == 9
    assert candidate(arr = [5, 2, 8, 10, 3, 7, 4, 6, 9, 1],m = 2) == 7
    assert candidate(arr = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9],m = 2) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 4) == 4
    assert candidate(arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5],m = 4) == 9
    assert candidate(arr = [1, 2, 5, 4, 7, 3, 8, 6, 9, 10],m = 2) == 7
    assert candidate(arr = [5, 3, 1, 7, 9, 10, 8, 6, 4, 2],m = 3) == -1
    assert candidate(arr = [6, 1, 4, 5, 3, 7, 9, 8, 10, 2],m = 2) == -1
