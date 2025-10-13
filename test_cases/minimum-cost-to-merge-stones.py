# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == 135
    assert candidate(stones = [3, 2, 4, 1],k = 3) == -1
    assert candidate(stones = [1, 2, 3, 4, 5],k = 3) == 21
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == -1
    assert candidate(stones = [4, 3, 2],k = 2) == 14
    assert candidate(stones = [10, 20, 30, 40, 50],k = 2) == 330
    assert candidate(stones = [4, 4, 4, 4, 4],k = 2) == 48
    assert candidate(stones = [15, 10, 5, 10, 15],k = 2) == 125
    assert candidate(stones = [3, 2, 1],k = 3) == 6
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11],k = 2) == 85
    assert candidate(stones = [7, 3, 8, 1, 12, 10, 6],k = 3) == 87
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 88
    assert candidate(stones = [4, 4, 4, 4],k = 2) == 32
    assert candidate(stones = [3, 2, 4, 1],k = 2) == 20
    assert candidate(stones = [5, 1, 2, 4, 3],k = 2) == 33
    assert candidate(stones = [1, 2, 3, 4, 5, 6],k = 3) == -1
    assert candidate(stones = [3, 5, 1, 2, 6],k = 3) == 25
    assert candidate(stones = [10, 20, 30, 40, 50],k = 5) == 150
    assert candidate(stones = [5, 17, 19, 8, 45, 30],k = 3) == -1
    assert candidate(stones = [7, 7, 7, 7, 7, 7],k = 3) == -1
    assert candidate(stones = [10, 15, 20, 25],k = 2) == 140
    assert candidate(stones = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 5) == -1
    assert candidate(stones = [5, 17, 9, 4, 13, 8, 11],k = 3) == 123
    assert candidate(stones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 4) == -1
    assert candidate(stones = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 4) == 910
    assert candidate(stones = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],k = 6) == -1
    assert candidate(stones = [22, 15, 33, 11, 7, 19, 25, 28],k = 4) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],k = 5) == 269
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == -1
    assert candidate(stones = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 6) == -1
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 450
    assert candidate(stones = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],k = 10) == -1
    assert candidate(stones = [1, 3, 2, 5, 4, 6, 9, 8, 7, 10, 13, 12, 11, 14, 17, 16, 15, 18, 21, 20, 19, 22, 25, 24, 23, 26, 29, 28, 27, 30],k = 3) == -1
    assert candidate(stones = [10, 15, 20, 25, 30, 35, 40, 45, 50],k = 3) == 535
    assert candidate(stones = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],k = 4) == -1
    assert candidate(stones = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == -1
    assert candidate(stones = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 2175
    assert candidate(stones = [5, 3, 8, 6, 2, 7, 4, 9, 1, 12, 11, 10, 15, 13, 14, 19, 17, 18, 23, 21, 22, 27, 25, 26, 31, 29, 30, 35, 33, 34],k = 7) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 5) == -1
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == -1
    assert candidate(stones = [1, 10, 100, 1000, 10000, 100000, 1000000],k = 2) == 1234566
    assert candidate(stones = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 6) == -1
    assert candidate(stones = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 300],k = 5) == -1
    assert candidate(stones = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 4) == -1
    assert candidate(stones = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 5) == -1
    assert candidate(stones = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 4) == -1
    assert candidate(stones = [5, 3, 8, 1, 9, 2, 6, 4, 7, 10],k = 4) == 91
    assert candidate(stones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == -1
    assert candidate(stones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 6) == -1
    assert candidate(stones = [7, 13, 8, 9, 12, 5, 6, 3, 1, 4],k = 3) == -1
    assert candidate(stones = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 4) == 1092
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == -1
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 8) == -1
    assert candidate(stones = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109],k = 7) == -1
    assert candidate(stones = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 3) == -1
    assert candidate(stones = [14, 29, 10, 21, 3, 16, 24, 20, 30],k = 3) == 334
    assert candidate(stones = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == -1
    assert candidate(stones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == 198
    assert candidate(stones = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 7) == -1
    assert candidate(stones = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 164
    assert candidate(stones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 2) == 17300
    assert candidate(stones = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == -1
    assert candidate(stones = [3, 8, 3, 9, 3, 8, 3, 9, 3, 8, 3, 9, 3, 8, 3, 9, 3, 8, 3, 9],k = 3) == -1
    assert candidate(stones = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],k = 3) == -1
    assert candidate(stones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],k = 4) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 3) == -1
    assert candidate(stones = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 135
    assert candidate(stones = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91, 11, 90, 12, 89, 13, 88, 14, 87],k = 3) == -1
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 5) == 600
    assert candidate(stones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == -1
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70],k = 3) == 490
    assert candidate(stones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 2) == 296
    assert candidate(stones = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 60
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 2) == 2175
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 10) == -1
    assert candidate(stones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 4) == 455
    assert candidate(stones = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101],k = 6) == 2076
    assert candidate(stones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 7) == -1
    assert candidate(stones = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 6) == -1
    assert candidate(stones = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 2) == 296
    assert candidate(stones = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 9) == -1
    assert candidate(stones = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 5) == -1
    assert candidate(stones = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == -1
    assert candidate(stones = [9, 5, 7, 3, 8, 6, 2, 4, 1, 10],k = 2) == 177
    assert candidate(stones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 4) == -1
    assert candidate(stones = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180, 189, 198, 207, 216, 225, 234, 243, 252, 261, 270],k = 3) == -1
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 34
    assert candidate(stones = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27],k = 5) == -1
    assert candidate(stones = [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],k = 2) == 193
    assert candidate(stones = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],k = 5) == 515
    assert candidate(stones = [4, 8, 15, 16, 23, 42, 7, 11, 18, 29, 37, 45, 1, 3, 6, 10, 14, 19],k = 4) == -1
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 148
    assert candidate(stones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 4) == -1
    assert candidate(stones = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 87
    assert candidate(stones = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175],k = 5) == 4480
    assert candidate(stones = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 7) == -1
    assert candidate(stones = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210],k = 7) == -1
    assert candidate(stones = [15, 10, 5, 1, 20, 30, 25, 35, 40, 45, 50, 55],k = 5) == -1
    assert candidate(stones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == -1
    assert candidate(stones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 3) == -1
    assert candidate(stones = [5, 15, 10, 25, 30, 20, 5, 10, 40],k = 3) == 310
    assert candidate(stones = [5, 10, 15, 20, 25, 30, 35, 40],k = 4) == -1
    assert candidate(stones = [31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33, 83, 27, 95],k = 3) == -1
    assert candidate(stones = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],k = 6) == -1
    assert candidate(stones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 91
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == -1
    assert candidate(stones = [5, 3, 8, 9, 1, 2, 4, 7, 6, 0],k = 3) == -1
    assert candidate(stones = [7, 1, 4, 5, 6],k = 2) == 51
    assert candidate(stones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == -1
    assert candidate(stones = [7, 7, 7, 7, 7, 7, 7],k = 2) == 140
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],k = 4) == -1
    assert candidate(stones = [7, 7, 7, 7, 7, 7, 7, 7],k = 2) == 168
    assert candidate(stones = [7, 7, 7, 7, 7, 7],k = 3) == -1
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 2) == 1730
    assert candidate(stones = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15],k = 4) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6],k = 2) == 51
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15],k = 3) == -1
    assert candidate(stones = [3, 2, 4, 1],k = 3) == -1
    assert candidate(stones = [5, 3, 8, 12, 6],k = 3) == 50
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 148
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 465
    assert candidate(stones = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 5) == -1
    assert candidate(stones = [1, 3, 2, 1, 2, 3, 1],k = 3) == 25
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == -1
    assert candidate(stones = [10, 4, 3, 5, 1],k = 2) == 49
    assert candidate(stones = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == -1
    assert candidate(stones = [10, 20, 30, 40, 50, 60],k = 3) == -1
    assert candidate(stones = [10, 10, 10, 10],k = 2) == 80
    assert candidate(stones = [10, 22, 9, 33, 21, 50, 41, 60, 80],k = 3) == 613
    assert candidate(stones = [1, 3, 3, 3, 2, 4, 1],k = 3) == 31
    assert candidate(stones = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 2) == 136
    assert candidate(stones = [8, 32, 25, 35, 25, 32, 25, 32, 31, 21, 34, 35, 31, 30, 29, 35, 32, 29, 29, 26, 30, 24, 26, 33, 38, 29, 21, 20, 34, 31],k = 3) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 173
    assert candidate(stones = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 2) == 68
    assert candidate(stones = [7, 4, 5, 9, 2],k = 2) == 63
    assert candidate(stones = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 4) == -1
    assert candidate(stones = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 2) == 136
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == -1
    assert candidate(stones = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 3) == -1
    assert candidate(stones = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == -1
    assert candidate(stones = [5, 3, 8, 3, 5, 3, 8, 5],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 310
    assert candidate(stones = [5, 3, 8, 3, 8, 3, 8, 3, 8, 3],k = 4) == 93
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 3) == 87
    assert candidate(stones = [10, 20, 30, 40, 50],k = 5) == 150
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90],k = 3) == 870
    assert candidate(stones = [2, 2, 2, 2, 2, 2, 2],k = 3) == 26
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 173
    assert candidate(stones = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 4) == -1
    assert candidate(stones = [7, 8, 9, 10, 11, 12],k = 3) == -1
    assert candidate(stones = [5, 5, 5, 5, 5, 5],k = 3) == -1
    assert candidate(stones = [10, 12, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 126
    assert candidate(stones = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 2) == 51
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 2) == 740
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 315
    assert candidate(stones = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 2) == 1730
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1],k = 2) == 20
    assert candidate(stones = [5, 3, 3, 3, 5],k = 2) == 44
    assert candidate(stones = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 5) == -1
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 3) == -1
    assert candidate(stones = [7, 8, 9, 10, 11, 12, 13],k = 3) == 127
    assert candidate(stones = [4, 4, 4, 4, 4, 4, 4],k = 2) == 80
    assert candidate(stones = [5, 3, 8, 1, 9, 2, 7, 4, 6],k = 3) == 90
    assert candidate(stones = [7, 3, 2, 1, 8],k = 3) == 27
    assert candidate(stones = [10, 4, 3, 5, 10, 7, 9, 6],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9],k = 4) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],k = 5) == -1
    assert candidate(stones = [15, 10, 20, 5, 25],k = 3) == 110
    assert candidate(stones = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 3) == -1
    assert candidate(stones = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 4) == -1
    assert candidate(stones = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 135
    assert candidate(stones = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 10) == -1
    assert candidate(stones = [8, 8, 8, 8, 8, 8, 8, 8],k = 4) == -1
    assert candidate(stones = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],k = 3) == 4644
    assert candidate(stones = [5, 17, 100, 11],k = 2) == 266
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 29
    assert candidate(stones = [1, 3, 2, 4, 5],k = 2) == 34
    assert candidate(stones = [2, 4, 6, 8, 10, 12, 14, 16, 18],k = 5) == 120
    assert candidate(stones = [4, 4, 4, 4, 4, 4],k = 3) == -1
    assert candidate(stones = [10, 4, 3, 5, 1],k = 2) == 49
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 34
    assert candidate(stones = [5, 17, 23, 26, 32, 48],k = 2) == 369
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 5) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == 135
    assert candidate(stones = [2, 3, 5, 7, 11, 13, 17],k = 3) == 96
    assert candidate(stones = [1, 2, 3, 4, 5, 6],k = 2) == 51
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 154
    assert candidate(stones = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 2) == 1480
    assert candidate(stones = [1, 2, 3],k = 4) == -1
    assert candidate(stones = [4, 3, 6, 7, 8, 2, 4, 1, 2, 3],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30],k = 5) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 29) == -1
    assert candidate(stones = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == -1
    assert candidate(stones = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 4) == -1
    assert candidate(stones = [1, 3, 1, 3, 1, 3],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30],k = 2) == 958
    assert candidate(stones = [3, 2, 4, 1],k = 2) == 20
    assert candidate(stones = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 4) == 182
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 3) == 1452
    assert candidate(stones = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 2) == 444
    assert candidate(stones = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 3) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 91
    assert candidate(stones = [7, 8, 9, 10, 11, 12],k = 4) == -1
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 2) == 2175
    assert candidate(stones = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 2) == 346
    assert candidate(stones = [10, 4, 3, 5, 3, 3, 9, 4, 8, 7, 7, 2, 2, 4, 1, 6, 5],k = 3) == 213
    assert candidate(stones = [3, 5, 1, 2, 6],k = 3) == 25
    assert candidate(stones = [4, 4, 4, 4, 4, 4],k = 2) == 64
    assert candidate(stones = [10, 5, 10, 15, 20],k = 2) == 135
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == -1
    assert candidate(stones = [10, 4, 3, 5, 9],k = 2) == 69
    assert candidate(stones = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1],k = 3) == 176
    assert candidate(stones = [9, 9, 9, 9, 9, 9, 9, 9, 9],k = 3) == 162
    assert candidate(stones = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 3) == 523
    assert candidate(stones = [5, 17, 100, 11],k = 3) == -1
    assert candidate(stones = [1, 3, 5, 7, 9],k = 2) == 54
    assert candidate(stones = [5, 17, 19, 19, 5, 19, 8, 13, 18, 3, 18, 1, 17, 1, 11, 17, 1, 20, 18, 3, 18, 17, 1, 20, 20, 9, 2, 11, 17, 2],k = 3) == -1
    assert candidate(stones = [5, 17, 12, 2, 9, 13, 11, 16, 1, 12, 18, 10, 20, 8],k = 2) == 583
    assert candidate(stones = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 2) == 592
    assert candidate(stones = [7, 1, 5, 9, 3, 2, 4, 6],k = 3) == -1
    assert candidate(stones = [5, 5, 5, 5, 5, 5, 5],k = 5) == -1
    assert candidate(stones = [15, 18, 6, 11, 13, 18, 5, 12, 8],k = 3) == 212
    assert candidate(stones = [10, 5, 9, 1],k = 2) == 50
    assert candidate(stones = [4, 10, 3, 5],k = 2) == 44
    assert candidate(stones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 465
