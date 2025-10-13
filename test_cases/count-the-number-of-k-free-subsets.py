# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [2, 3, 5, 8],k = 5) == 12
    assert candidate(nums = [100, 200, 300],k = 50) == 8
    assert candidate(nums = [5, 4, 6],k = 1) == 5
    assert candidate(nums = [7, 14, 21, 28],k = 7) == 8
    assert candidate(nums = [3, 7, 11, 15],k = 4) == 8
    assert candidate(nums = [20, 40, 60, 80, 100],k = 20) == 13
    assert candidate(nums = [50, 100, 150, 200, 250, 300],k = 50) == 21
    assert candidate(nums = [1, 2, 3, 4, 5],k = 2) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 200
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21],k = 3) == 80
    assert candidate(nums = [1, 3, 5, 7, 9],k = 2) == 13
    assert candidate(nums = [100, 200, 300, 400, 500],k = 150) == 32
    assert candidate(nums = [30, 40, 50, 60],k = 10) == 8
    assert candidate(nums = [1, 3, 5, 7, 9],k = 1) == 32
    assert candidate(nums = [10, 5, 9, 11],k = 20) == 16
    assert candidate(nums = [5, 10, 15, 20, 25, 30],k = 5) == 21
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 144
    assert candidate(nums = [7, 14, 21, 28, 35],k = 7) == 13
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 13
    assert candidate(nums = [500, 501, 502, 503, 504, 505],k = 1) == 21
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 144
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43],k = 3) == 1597
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 144
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 2) == 2178309
    assert candidate(nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29],k = 3) == 144
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],k = 3) == 1597
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7],k = 2) == 40
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 10) == 144
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110],k = 1) == 233
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 4) == 20736
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 169
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 3) == 17711
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 200
    assert candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89],k = 6) == 1597
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 2) == 233
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3) == 1024
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 100) == 1597
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 3) == 144
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 1870
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],k = 10) == 1597
    assert candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],k = 1) == 243
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5) == 1024
    assert candidate(nums = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50],k = 3) == 2584
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1) == 768
    assert candidate(nums = [1, 3, 5, 7, 9, 11],k = 2) == 21
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 5) == 10946
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42],k = 4) == 233
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10) == 1597
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],k = 4) == 144
    assert candidate(nums = [1, 3, 6, 8, 11, 13, 16, 18, 21, 23, 26, 28, 31, 33, 36, 38, 41, 43, 46, 48],k = 2) == 59049
    assert candidate(nums = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96],k = 5) == 17711
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220],k = 11) == 17711
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13],k = 2) == 34
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 1024
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49],k = 3) == 4181
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],k = 3) == 144
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 28561
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 11) == 144
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],k = 4) == 1597
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 10) == 233
    assert candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],k = 2) == 324
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],k = 5) == 2178309
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 144
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 144
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 17711
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 8) == 144
    assert candidate(nums = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250],k = 25) == 144
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512],k = 2) == 384
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 9) == 200
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 3125
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 1024
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 15) == 200
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 144
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 144
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 169
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48],k = 4) == 377
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120],k = 5) == 18432
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 7) == 768
    assert candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14],k = 3) == 169
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 150) == 1024
    assert candidate(nums = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47],k = 3) == 2584
    assert candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519],k = 1) == 17711
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 10) == 144
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31],k = 3) == 233
    assert candidate(nums = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48],k = 2) == 17711
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],k = 3) == 640
    assert candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50],k = 1) == 129140163
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],k = 6) == 144
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 3) == 17711
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97],k = 4) == 196418
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 17711
    assert candidate(nums = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],k = 10) == 144
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 2) == 1597
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 144
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 17711
