# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(rungs = [1, 3, 5, 10],dist = 2) == 2
    assert candidate(rungs = [1, 2, 3, 4, 5],dist = 1) == 0
    assert candidate(rungs = [3, 6, 8, 10],dist = 3) == 0
    assert candidate(rungs = [10],dist = 10) == 0
    assert candidate(rungs = [1000000000],dist = 1) == 999999999
    assert candidate(rungs = [1, 1000000000],dist = 1) == 999999998
    assert candidate(rungs = [1, 5, 11, 20],dist = 4) == 3
    assert candidate(rungs = [3, 4, 6, 7],dist = 2) == 1
    assert candidate(rungs = [5],dist = 10) == 0
    assert candidate(rungs = [1, 5, 10, 16, 23, 31, 40, 50, 61, 73, 86, 100],dist = 14) == 0
    assert candidate(rungs = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],dist = 1) == 89
    assert candidate(rungs = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],dist = 10) == 0
    assert candidate(rungs = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],dist = 2) == 502
    assert candidate(rungs = [2, 8, 16, 32, 64, 128],dist = 15) == 7
    assert candidate(rungs = [100, 200, 300, 400, 500],dist = 150) == 0
    assert candidate(rungs = [2, 5, 10, 20, 35, 55, 80, 110, 145, 185, 230],dist = 5) == 36
    assert candidate(rungs = [1, 8, 15, 22, 29],dist = 5) == 4
    assert candidate(rungs = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],dist = 10) == 0
    assert candidate(rungs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],dist = 15) == 0
    assert candidate(rungs = [5, 10, 20, 40, 80, 160],dist = 10) == 11
    assert candidate(rungs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],dist = 3) == 24
    assert candidate(rungs = [1, 7, 15, 30, 60],dist = 10) == 3
    assert candidate(rungs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],dist = 1) == 502
    assert candidate(rungs = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],dist = 20) == 47
    assert candidate(rungs = [10, 25, 45, 70, 100, 130, 160, 190, 220, 250],dist = 30) == 0
    assert candidate(rungs = [1, 6, 15, 30, 50],dist = 10) == 2
    assert candidate(rungs = [1, 1000000000],dist = 100000000) == 9
    assert candidate(rungs = [100, 200, 300, 400, 500],dist = 99) == 5
    assert candidate(rungs = [1, 8, 15, 22, 30],dist = 5) == 4
    assert candidate(rungs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],dist = 9) == 10
    assert candidate(rungs = [10, 15, 25, 40, 50],dist = 10) == 1
    assert candidate(rungs = [2, 5, 11, 21, 35, 50],dist = 5) == 6
    assert candidate(rungs = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59],dist = 6) == 0
    assert candidate(rungs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],dist = 1) == 90
    assert candidate(rungs = [1, 1000000000],dist = 100000000) == 9
    assert candidate(rungs = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105],dist = 14) == 0
    assert candidate(rungs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],dist = 1) == 0
    assert candidate(rungs = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],dist = 50) == 0
    assert candidate(rungs = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 100],dist = 10) == 0
    assert candidate(rungs = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],dist = 20) == 0
    assert candidate(rungs = [10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105],dist = 10) == 4
    assert candidate(rungs = [5, 10, 20, 40, 80, 160],dist = 25) == 4
    assert candidate(rungs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],dist = 1) == 10
    assert candidate(rungs = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120],dist = 4) == 21
    assert candidate(rungs = [1, 4, 10, 20, 30],dist = 5) == 3
    assert candidate(rungs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],dist = 10) == 98
    assert candidate(rungs = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000],dist = 100000) == 6
    assert candidate(rungs = [3, 15, 25, 30, 45, 60, 85, 100],dist = 12) == 5
    assert candidate(rungs = [1, 3, 6, 10, 15, 21, 28],dist = 3) == 5
    assert candidate(rungs = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],dist = 100) == 8
    assert candidate(rungs = [2, 6, 10, 14, 18, 22, 26],dist = 4) == 0
    assert candidate(rungs = [100, 200, 300, 400, 500],dist = 90) == 5
    assert candidate(rungs = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],dist = 100000) == 9995
    assert candidate(rungs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],dist = 1024) == 1013
    assert candidate(rungs = [5, 11, 19, 29, 41, 55, 71, 89, 109, 131],dist = 6) == 15
    assert candidate(rungs = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],dist = 9) == 9
    assert candidate(rungs = [2, 8, 14, 20, 26, 32, 38, 44, 50],dist = 6) == 0
    assert candidate(rungs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],dist = 3) == 0
    assert candidate(rungs = [1, 2, 4, 7, 13, 21],dist = 3) == 3
    assert candidate(rungs = [1000000000],dist = 500000000) == 1
    assert candidate(rungs = [1, 5, 15, 30, 50, 70, 100, 150, 200, 300],dist = 25) == 6
    assert candidate(rungs = [2, 8, 14, 22, 30, 40, 50],dist = 6) == 4
    assert candidate(rungs = [1, 1000000000],dist = 1) == 999999998
    assert candidate(rungs = [1, 100, 200, 300],dist = 50) == 3
    assert candidate(rungs = [3, 15, 35, 65, 100, 145, 195, 250, 310, 375],dist = 10) == 31
    assert candidate(rungs = [10, 25, 45, 60, 75, 90],dist = 15) == 1
    assert candidate(rungs = [10, 25, 45, 70, 100],dist = 15) == 3
    assert candidate(rungs = [1, 1000000000],dist = 500000000) == 1
    assert candidate(rungs = [5, 12, 24, 40, 60, 85, 100],dist = 10) == 6
    assert candidate(rungs = [1, 1000000000],dist = 1000000) == 999
    assert candidate(rungs = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65],dist = 4) == 10
    assert candidate(rungs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],dist = 2) == 0
    assert candidate(rungs = [1, 9, 15, 25, 30],dist = 5) == 3
    assert candidate(rungs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],dist = 9) == 0
    assert candidate(rungs = [2, 8, 18, 32, 50, 72, 98],dist = 15) == 3
    assert candidate(rungs = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120],dist = 500) == 8
    assert candidate(rungs = [5, 10, 20, 40, 80, 160],dist = 10) == 11
    assert candidate(rungs = [1, 6, 11, 16, 21, 26],dist = 5) == 0
    assert candidate(rungs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],dist = 10) == 0
    assert candidate(rungs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],dist = 2) == 0
    assert candidate(rungs = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],dist = 5) == 5
    assert candidate(rungs = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],dist = 1000000) == 996
    assert candidate(rungs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],dist = 3) == 0
    assert candidate(rungs = [1000000000],dist = 100000000) == 9
    assert candidate(rungs = [1, 1000000000],dist = 500000000) == 1
    assert candidate(rungs = [10, 1000000000],dist = 500000000) == 1
    assert candidate(rungs = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],dist = 9) == 9
    assert candidate(rungs = [1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106],dist = 5) == 13
    assert candidate(rungs = [2, 3, 6, 8, 15, 22, 30, 35, 40, 50],dist = 5) == 4
    assert candidate(rungs = [3, 9, 12, 21, 23, 29, 30],dist = 6) == 1
    assert candidate(rungs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],dist = 2) == 0
    assert candidate(rungs = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],dist = 3) == 12
    assert candidate(rungs = [1, 10, 15, 20, 25, 30],dist = 5) == 1
    assert candidate(rungs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],dist = 15) == 0
    assert candidate(rungs = [5, 12, 22, 35, 50, 68, 89, 113, 141, 173, 209],dist = 7) == 23
    assert candidate(rungs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],dist = 1) == 0
    assert candidate(rungs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],dist = 1) == 10
    assert candidate(rungs = [1, 2, 4, 8, 16, 32, 64],dist = 15) == 3
    assert candidate(rungs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],dist = 2) == 38
    assert candidate(rungs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],dist = 9) == 10
    assert candidate(rungs = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],dist = 1000000) == 996
    assert candidate(rungs = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],dist = 100) == 8
