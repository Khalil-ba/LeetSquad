# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [7, 7, 7, 7, 7],k = 7) == 10
    assert candidate(nums = [10, 20, 30, 40, 50],k = 10) == 10
    assert candidate(nums = [5, 5, 5, 5],k = 5) == 6
    assert candidate(nums = [1, 2, 3, 4, 5],k = 2) == 7
    assert candidate(nums = [6, 12, 18, 24],k = 12) == 6
    assert candidate(nums = [1, 3, 5, 7, 9],k = 3) == 7
    assert candidate(nums = [7, 14, 21, 28, 35],k = 7) == 10
    assert candidate(nums = [2, 4, 6, 8, 10],k = 3) == 4
    assert candidate(nums = [10, 20, 30, 40],k = 10) == 6
    assert candidate(nums = [5, 10, 15, 20, 25],k = 5) == 10
    assert candidate(nums = [7, 14, 21, 28],k = 7) == 6
    assert candidate(nums = [1, 3, 5, 7, 9],k = 2) == 0
    assert candidate(nums = [2, 4, 6, 8, 10],k = 4) == 10
    assert candidate(nums = [1, 2, 3, 4],k = 5) == 0
    assert candidate(nums = [3, 5, 7, 11],k = 1) == 6
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 45
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240],k = 12) == 190
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 101) == 45
    assert candidate(nums = [100, 200, 300, 400, 500, 600],k = 100) == 15
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],k = 5) == 45
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 13) == 45
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],k = 13) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 6) == 185
    assert candidate(nums = [24, 48, 72, 96, 120],k = 24) == 10
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 9) == 45
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24],k = 3) == 28
    assert candidate(nums = [5, 10, 15, 20, 25, 30],k = 5) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 1) == 190
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 190
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 45
    assert candidate(nums = [8, 12, 18, 24, 30, 36, 42],k = 6) == 21
    assert candidate(nums = [10, 20, 30, 40, 50],k = 10) == 10
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255],k = 17) == 105
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 45
    assert candidate(nums = [15, 25, 35, 45, 55],k = 15) == 7
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],k = 5) == 105
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195],k = 13) == 105
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 14) == 35
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132],k = 11) == 66
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 45
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77],k = 11) == 21
    assert candidate(nums = [7, 14, 28, 56, 112],k = 14) == 10
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81],k = 9) == 36
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 100000) == 9
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],k = 100000) == 15
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],k = 9) == 55
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996],k = 5) == 4
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],k = 8) == 45
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 17
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 4) == 45
    assert candidate(nums = [17, 34, 51, 68, 85, 102, 119, 136, 153, 170],k = 17) == 45
    assert candidate(nums = [13, 26, 39, 52, 65],k = 13) == 10
    assert candidate(nums = [6, 12, 18, 24, 30],k = 12) == 10
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],k = 15) == 45
    assert candidate(nums = [77, 154, 231, 308, 385, 462, 539, 616, 693, 770],k = 11) == 45
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],k = 9) == 66
    assert candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210],k = 21) == 45
    assert candidate(nums = [6, 12, 18, 24, 30],k = 6) == 10
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010],k = 101) == 45
    assert candidate(nums = [9, 18, 27, 36, 45],k = 9) == 10
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 16) == 101
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 5) == 190
    assert candidate(nums = [21, 42, 63, 84, 105, 126, 147, 168, 189, 210],k = 21) == 45
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 1) == 190
    assert candidate(nums = [49, 98, 147, 196, 245, 294, 343, 392, 441, 490],k = 49) == 45
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 11) == 45
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 9) == 45
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 0
    assert candidate(nums = [19, 38, 57, 76, 95, 114, 133, 152, 171, 190],k = 19) == 45
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 3) == 60
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],k = 100) == 32
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105],k = 15) == 21
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],k = 7) == 105
    assert candidate(nums = [6, 8, 10, 12, 14, 16, 18],k = 12) == 15
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21],k = 3) == 21
    assert candidate(nums = [8, 16, 32, 64, 128],k = 8) == 10
    assert candidate(nums = [15, 30, 45, 60, 75],k = 15) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 3) == 112
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135],k = 9) == 105
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90],k = 6) == 105
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],k = 5) == 66
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 3) == 45
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150],k = 15) == 45
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],k = 2) == 300
    assert candidate(nums = [15, 25, 35, 45, 55],k = 5) == 10
    assert candidate(nums = [6, 12, 18, 24, 30, 36],k = 12) == 15
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],k = 9) == 45
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],k = 7) == 45
    assert candidate(nums = [11, 22, 33, 44, 55],k = 11) == 10
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],k = 8) == 105
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221, 234, 247, 260],k = 13) == 190
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 3) == 45
    assert candidate(nums = [23, 46, 69, 92, 115, 138, 161, 184, 207, 230],k = 23) == 45
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000],k = 100000) == 10
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64],k = 16) == 28
    assert candidate(nums = [25, 50, 75, 100, 125, 150],k = 25) == 15
    assert candidate(nums = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116],k = 11) == 37
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 3) == 34
    assert candidate(nums = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],k = 5) == 44
    assert candidate(nums = [10, 20, 30, 40, 50],k = 20) == 10
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],k = 11) == 45
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96],k = 8) == 66
