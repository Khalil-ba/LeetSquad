# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 6
    assert candidate(nums = [3, 3, 3, 3],k = 6) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 8
    assert candidate(nums = [10, 5, 2, 4, 2],k = 20) == 3
    assert candidate(nums = [10, 5, 2, 1],k = 50) == 2
    assert candidate(nums = [0, 0, 0, 0, 0],k = 1) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 5
    assert candidate(nums = [10, 10, 10, 10],k = 100) == 2
    assert candidate(nums = [1, 0, 1, 0, 1],k = 1) == 1
    assert candidate(nums = [1, 0, 0, 1],k = 0) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],k = 20) == 2
    assert candidate(nums = [1000000000, 1000000000],k = 1000000000000000000) == 1
    assert candidate(nums = [5, 1, 2, 4, 6],k = 10) == 3
    assert candidate(nums = [1, 0, 1, 0, 1],k = 0) == 1
    assert candidate(nums = [0, 0, 0, 0],k = 1) == 1
    assert candidate(nums = [1, 2, 2, 3],k = 5) == 2
    assert candidate(nums = [1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [5, 5, 5, 5, 5],k = 25) == 3
    assert candidate(nums = [1, 0, 1, 1],k = 0) == 1
    assert candidate(nums = [2, 3, 3, 7, 3, 5],k = 20) == 3
    assert candidate(nums = [5, 5, 5, 5],k = 25) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 6
    assert candidate(nums = [2, 4, 8, 16, 32, 64],k = 1024) == 3
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1000) == 9
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5],k = 20) == 4
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 10
    assert candidate(nums = [9, 3, 9, 3, 9, 3, 9, 3, 9, 3],k = 27) == 5
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 4) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 5
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 150) == 9
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 18) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 24) == 10
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],k = 6) == 8
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 2, 1],k = 500) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 16
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 10000000000) == 6
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 4) == 5
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 4) == 5
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 500) == 4
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1],k = 10000) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 7
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 9) == 10
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 4) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 81) == 5
    assert candidate(nums = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3],k = 6) == 5
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 4) == 7
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1000000000) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 10
    assert candidate(nums = [9, 3, 2, 2, 3, 9, 3, 2, 2, 3],k = 18) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000000000000) == 5
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 100) == 5
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 4) == 5
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 36) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 100) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 8
    assert candidate(nums = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5],k = 50) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 24) == 7
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 30) == 6
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 49) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 500) == 9
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 21) == 8
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],k = 12) == 7
    assert candidate(nums = [1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999],k = 1000000000000) == 6
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 1000) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 6
    assert candidate(nums = [3, 3, 1, 1, 3, 3, 1, 1, 3, 3],k = 9) == 3
    assert candidate(nums = [3, 1, 3, 1, 3, 1, 3, 1, 3, 1],k = 4) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 10) == 1
    assert candidate(nums = [3, 6, 2, 8, 1, 4, 7, 5],k = 24) == 5
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6],k = 10) == 18
    assert candidate(nums = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10],k = 30) == 7
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 16) == 5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 50) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 25) == 8
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 10) == 9
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 50) == 8
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 6
    assert candidate(nums = [2, 5, 1, 3, 4, 2, 6, 1],k = 12) == 3
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1024) == 7
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10],k = 20) == 15
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 36) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 25) == 12
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1024) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 25) == 7
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 100) == 3
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 100) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1000) == 9
    assert candidate(nums = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 4) == 5
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995],k = 999999999999999999) == 3
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 81) == 5
    assert candidate(nums = [2, 4, 2, 4, 2, 4, 2, 4, 2, 4],k = 16) == 5
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10],k = 100) == 2
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 50) == 18
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 18) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],k = 20) == 4
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1) == 1
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000000) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 100) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 30) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 20) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2000) == 8
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 8) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 5
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 256) == 7
    assert candidate(nums = [3, 6, 2, 8, 1, 4, 5, 3, 2, 9, 10, 7],k = 30) == 7
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],k = 1000) == 14
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 30) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 8
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 5
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 50) == 8
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],k = 9) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 100) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 100) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 25) == 7
