# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 6, 4, 1, 2],target = 3) == 5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],target = 9) == 9
    assert candidate(nums = [1, 5, 10, 15, 20],target = 4) == -1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],target = 9) == 9
    assert candidate(nums = [10, 8, 6, 4, 2],target = 2) == 4
    assert candidate(nums = [0, 0, 0, 0, 0],target = 0) == 4
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000],target = 500000000) == 4
    assert candidate(nums = [-1, 0, 1, 2, 3],target = 2) == 4
    assert candidate(nums = [1000000000, -1000000000, 1000000000, -1000000000],target = 2000000000) == 3
    assert candidate(nums = [10, 8, 6, 4, 2],target = 1) == -1
    assert candidate(nums = [1, 3, 6, 4, 1, 2],target = 0) == -1
    assert candidate(nums = [1, 5, 9, 14, 20],target = 4) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == 9
    assert candidate(nums = [10, 20, 30, 40, 50],target = 10) == 4
    assert candidate(nums = [1, 5, 10, 15, 20],target = 9) == 4
    assert candidate(nums = [1, 2, 3, 5, 6, 8, 9],target = 2) == 6
    assert candidate(nums = [10, 20, 30, 40, 50],target = 15) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1) == 9
    assert candidate(nums = [1, 1, 1, 1, 1],target = 1) == 4
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 1) == 9
    assert candidate(nums = [1, 1, 1, 1, 1],target = 0) == 4
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],target = 10) == -1
    assert candidate(nums = [1, 3, 5, 7, 9],target = 2) == 4
    assert candidate(nums = [5, 4, 3, 2, 1],target = 1) == 4
    assert candidate(nums = [1, 3, 6, 4, 1, 2],target = 2) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],target = 1) == 4
    assert candidate(nums = [2, 4, 5, 7, 9, 11],target = 2) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 0) == 9
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],target = 4) == 9
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 2) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 2) == 12
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 0) == 9
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],target = 99) == 9
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],target = 1) == 9
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 4) == 19
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50],target = 5) == -1
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],target = 9) == 19
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 15) == 9
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 20) == 9
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 10) == 9
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],target = 2) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 0) == -1
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765],target = 20) == -1
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],target = 15) == 9
    assert candidate(nums = [1, 5, 3, 7, 9, 12, 10, 15, 20, 18],target = 5) == 9
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],target = 4) == 19
    assert candidate(nums = [1, 10, 21, 32, 43, 54, 65, 76, 87, 98],target = 9) == -1
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],target = 4) == 9
    assert candidate(nums = [-10, -5, 0, 5, 10, 15],target = 10) == 5
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],target = 9) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == 19
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == 9
    assert candidate(nums = [5, 15, 10, 20, 25, 30],target = 5) == -1
    assert candidate(nums = [9, 7, 5, 3, 1, 0, -2, -4, -6, -8, -10],target = 3) == 10
    assert candidate(nums = [1, 5, 10, 15, 20, 25, 30],target = 5) == 6
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 1) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 1) == 14
    assert candidate(nums = [1, 3, 6, 4, 1, 2, 1, 3, 6, 4, 1, 2, 1, 3, 6, 4, 1, 2, 1, 3],target = 2) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == 21
    assert candidate(nums = [1, 4, 3, 2, 5, 6, 7, 8, 9, 10],target = 3) == 9
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 1) == 19
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 0) == -1
    assert candidate(nums = [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4],target = 3) == 19
    assert candidate(nums = [1000000000, 999999998, 999999996, 999999994, 999999992],target = 2) == 4
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],target = 1) == 19
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 1) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == 19
    assert candidate(nums = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14, 16, 17, 19, 18, 20],target = 2) == 19
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],target = 6) == 19
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 1) == -1
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],target = 50) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 20) == 9
    assert candidate(nums = [5, 1, 4, 2, 8, 7, 3, 6],target = 3) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 15) == 9
    assert candidate(nums = [5, 15, 10, 20, 25, 30, 35],target = 10) == 6
    assert candidate(nums = [1, 3, 6, 4, 1, 2, 8, 5, 7, 10],target = 3) == 8
    assert candidate(nums = [-10, -20, -30, -40, -50],target = 10) == 4
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6],target = 1) == 5
    assert candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],target = 10) == -1
    assert candidate(nums = [1, 5, 3, 7, 2, 6, 4, 8, 1, 9, 5, 10, 6, 11, 7],target = 4) == 10
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],target = 1) == 14
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],target = 500) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 2) == 19
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 0) == 19
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],target = 20) == -1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 1) == 19
    assert candidate(nums = [1, 4, 2, 7, 5, 9, 8, 11, 10],target = 3) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],target = 1) == 19
    assert candidate(nums = [1, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11],target = 3) == 14
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],target = 8) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == 19
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 100) == 9
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 15) == 9
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],target = 9) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 1) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3],target = 2) == 14
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 3) == 9
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],target = 0) == 4
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],target = 1000000) == 19
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 10) == 9
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],target = 20) == -1
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14],target = 1) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 5) == 19
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],target = 30) == 9
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],target = 1) == 10
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],target = 15) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 1) == 29
    assert candidate(nums = [1, 3, 6, 4, 1, 2, 5, 7, 8, 9],target = 2) == 6
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 1) == 19
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],target = 15) == 9
    assert candidate(nums = [1, 5, 10, 15, 20, 25, 30],target = 5) == 6
    assert candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],target = 4) == 19
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 10) == 9
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4],target = 3) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 0) == -1
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],target = 1) == 4
    assert candidate(nums = [10, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],target = 10) == 19
    assert candidate(nums = [2, 3, 1, 1, 4, 2, 3, 1, 1, 4, 2, 3, 1, 1, 4, 2, 3, 1, 1, 4],target = 2) == 14
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],target = 1) == 19
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],target = 1) == 14
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 20) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == 19
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 100) == -1
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10],target = 4) == 11
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8],target = 2) == 14
    assert candidate(nums = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2, 3],target = 2) == 14
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 9) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1) == 9
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],target = 1) == -1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 5) == 9
    assert candidate(nums = [1, 3, 6, 7, 10, 12, 15],target = 2) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 2) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],target = 10) == 19
    assert candidate(nums = [1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000],target = 999999999) == 9
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],target = 999999999) == 9
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 2) == 9
    assert candidate(nums = [10, 5, 10, 15, 20, 25, 30, 35, 40, 45],target = 10) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 15) == 9
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 2) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == 9
