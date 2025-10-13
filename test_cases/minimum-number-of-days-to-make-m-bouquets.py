# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(bloomDay = [1, 10, 3, 10, 2],m = 3,k = 1) == 3
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 5,k = 2) == 1
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 5,k = 1) == 5
    assert candidate(bloomDay = [1],m = 1,k = 1) == 1
    assert candidate(bloomDay = [1000000000, 1000000000, 1000000000],m = 1,k = 3) == 1000000000
    assert candidate(bloomDay = [1, 10, 3, 10, 2],m = 3,k = 2) == -1
    assert candidate(bloomDay = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 5,k = 2) == 10
    assert candidate(bloomDay = [1000000000, 1000000000, 1000000000],m = 1,k = 2) == 1000000000
    assert candidate(bloomDay = [7, 7, 7, 7, 12, 7, 7],m = 2,k = 3) == 12
    assert candidate(bloomDay = [1, 3, 2],m = 1,k = 2) == 3
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 1,k = 10) == 10
    assert candidate(bloomDay = [1, 2, 4, 9, 3, 4, 1],m = 2,k = 2) == 4
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 2,k = 5) == 1
    assert candidate(bloomDay = [5, 8, 6, 9, 3, 2, 7, 4],m = 3,k = 2) == 8
    assert candidate(bloomDay = [5, 5, 5, 5, 5, 5],m = 2,k = 3) == 5
    assert candidate(bloomDay = [5, 8, 6, 9, 7],m = 2,k = 2) == 9
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 5,k = 2) == 10
    assert candidate(bloomDay = [2, 1, 3, 1, 2],m = 3,k = 1) == 2
    assert candidate(bloomDay = [100, 100, 100, 100],m = 1,k = 4) == 100
    assert candidate(bloomDay = [1, 2, 3, 4, 5],m = 1,k = 5) == 5
    assert candidate(bloomDay = [1000000000],m = 1,k = 1) == 1000000000
    assert candidate(bloomDay = [5, 8, 6, 9, 2, 5, 9, 1, 1, 5, 1, 8, 9, 1, 8],m = 3,k = 1) == 1
    assert candidate(bloomDay = [5, 8, 6, 9, 2, 4, 7, 1, 3, 10],m = 4,k = 2) == 9
    assert candidate(bloomDay = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],m = 10,k = 2) == 20
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 2,k = 7) == 1
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],m = 5,k = 3) == 15
    assert candidate(bloomDay = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 5,k = 3) == 6
    assert candidate(bloomDay = [30, 10, 20, 30, 20, 10, 30, 20, 10, 30],m = 3,k = 3) == 30
    assert candidate(bloomDay = [9, 1, 2, 3, 4, 5, 6, 7, 8, 1000000000],m = 1,k = 1) == 1
    assert candidate(bloomDay = [3, 5, 1, 5, 9, 6, 2, 10, 8, 7],m = 3,k = 3) == 10
    assert candidate(bloomDay = [9, 8, 7, 6, 5, 4, 3, 2, 1],m = 3,k = 3) == 9
    assert candidate(bloomDay = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],m = 3,k = 3) == 9
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 5,k = 5) == 1
    assert candidate(bloomDay = [2, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15, 1],m = 8,k = 2) == 10
    assert candidate(bloomDay = [5, 3, 8, 1, 9, 2, 4, 6, 7],m = 3,k = 2) == 7
    assert candidate(bloomDay = [5, 1, 10, 2, 8, 3, 5, 10],m = 2,k = 2) == 5
    assert candidate(bloomDay = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000],m = 4,k = 2) == 1000000000
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],m = 3,k = 5) == -1
    assert candidate(bloomDay = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 2,k = 5) == 10
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 1,k = 10) == 1
    assert candidate(bloomDay = [5, 8, 4, 3, 7, 1, 9],m = 3,k = 2) == 8
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 10,k = 1) == 1
    assert candidate(bloomDay = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],m = 4,k = 3) == 3
    assert candidate(bloomDay = [9, 8, 7, 6, 5, 4, 3, 2, 1],m = 3,k = 2) == 6
    assert candidate(bloomDay = [3, 1, 5, 1, 3, 2, 5, 7, 5, 8, 4, 3],m = 3,k = 2) == 4
    assert candidate(bloomDay = [1000000000, 1000000000, 1000000000, 1000000000],m = 1,k = 4) == 1000000000
    assert candidate(bloomDay = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1],m = 4,k = 2) == 10
    assert candidate(bloomDay = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],m = 3,k = 4) == 2
    assert candidate(bloomDay = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],m = 5,k = 3) == -1
    assert candidate(bloomDay = [6, 5, 8, 10, 6, 11, 5, 3],m = 4,k = 1) == 6
    assert candidate(bloomDay = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],m = 3,k = 3) == 3
    assert candidate(bloomDay = [1, 2, 2, 1, 2, 1, 1, 2, 2, 1],m = 2,k = 3) == 2
    assert candidate(bloomDay = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],m = 5,k = 4) == 20
    assert candidate(bloomDay = [9, 8, 7, 6, 5, 4, 3, 2, 1],m = 4,k = 2) == 8
    assert candidate(bloomDay = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10],m = 4,k = 2) == 8
    assert candidate(bloomDay = [5, 3, 3, 3, 5, 5, 2, 2, 2, 5],m = 3,k = 3) == 5
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 100,k = 5) == -1
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],m = 3,k = 5) == 5
    assert candidate(bloomDay = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],m = 5,k = 1) == 1
    assert candidate(bloomDay = [5, 8, 9, 6, 4, 3, 7, 2, 1],m = 4,k = 2) == 8
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],m = 10,k = 2) == 20
    assert candidate(bloomDay = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10],m = 1,k = 10) == 10
    assert candidate(bloomDay = [2, 4, 1, 1, 1, 1, 2, 3, 3],m = 2,k = 3) == 3
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 4,k = 3) == -1
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 5,k = 3) == 1
    assert candidate(bloomDay = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],m = 1,k = 8) == 1000000000
    assert candidate(bloomDay = [5, 8, 6, 9, 10, 11, 12, 13, 14, 15],m = 4,k = 2) == 13
    assert candidate(bloomDay = [7, 7, 7, 12, 7, 7, 7, 12, 7, 7, 7, 12],m = 4,k = 3) == 12
    assert candidate(bloomDay = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9],m = 1,k = 1) == 1
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 5,k = 3) == 1
    assert candidate(bloomDay = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],m = 5,k = 3) == 2
    assert candidate(bloomDay = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],m = 5,k = 2) == 20
    assert candidate(bloomDay = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],m = 10,k = 5) == -1
    assert candidate(bloomDay = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],m = 5,k = 4) == 10
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],m = 15,k = 2) == 30
    assert candidate(bloomDay = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],m = 5,k = 3) == 30
    assert candidate(bloomDay = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],m = 10,k = 2) == 1
    assert candidate(bloomDay = [3, 2, 1, 6, 5, 4, 9, 8, 7, 12, 11, 10],m = 3,k = 3) == 9
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],m = 10,k = 1) == 10
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],m = 3,k = 5) == 5
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 15,k = 5) == 10
    assert candidate(bloomDay = [1, 10, 3, 10, 2, 1, 10, 3, 10, 2],m = 4,k = 2) == 10
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],m = 5,k = 3) == 15
    assert candidate(bloomDay = [9, 3, 5, 7, 2, 8, 10, 6, 4],m = 2,k = 3) == 9
    assert candidate(bloomDay = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],m = 5,k = 4) == 7
    assert candidate(bloomDay = [5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5, 1, 3, 1, 5],m = 10,k = 2) == 3
    assert candidate(bloomDay = [5, 8, 6, 9, 7, 2, 4, 3, 10, 1],m = 2,k = 4) == 9
    assert candidate(bloomDay = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9],m = 3,k = 3) == 9
    assert candidate(bloomDay = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],m = 5,k = 3) == 5
    assert candidate(bloomDay = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],m = 5,k = 4) == 200
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],m = 3,k = 3) == 9
    assert candidate(bloomDay = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],m = 5,k = 5) == 25
    assert candidate(bloomDay = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],m = 10,k = 3) == 3
