# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 5, 5, 5, 5],k = 5) == 15
    assert candidate(nums = [10, 9, 8, 7, 6],k = 10) == 1
    assert candidate(nums = [5, 5, 5, 5],k = 5) == 10
    assert candidate(nums = [3, 3, 3, 3, 3, 3],k = 3) == 21
    assert candidate(nums = [8, 8, 8, 8, 8],k = 8) == 15
    assert candidate(nums = [4, 6, 3, 7, 1],k = 3) == 2
    assert candidate(nums = [1, 2, 3],k = 2) == 2
    assert candidate(nums = [1000000000, 1000000000, 1000000000],k = 1000000000) == 6
    assert candidate(nums = [0, 0, 0, 0, 0],k = 0) == 15
    assert candidate(nums = [10, 5, 3, 1],k = 1) == 4
    assert candidate(nums = [7, 7, 7, 7],k = 7) == 10
    assert candidate(nums = [1, 3, 5, 7, 9],k = 3) == 1
    assert candidate(nums = [8, 4, 2, 1],k = 8) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 1
    assert candidate(nums = [1, 1, 1],k = 1) == 6
    assert candidate(nums = [1, 3, 5, 7, 9],k = 1) == 10
    assert candidate(nums = [5, 3, 1, 4, 2],k = 0) == 7
    assert candidate(nums = [3, 3, 3, 3, 3],k = 3) == 15
    assert candidate(nums = [5, 3, 2, 1, 4],k = 1) == 2
    assert candidate(nums = [1, 1, 2],k = 1) == 3
    assert candidate(nums = [10, 20, 30, 40, 50],k = 10) == 1
    assert candidate(nums = [7, 14, 28, 56, 112],k = 7) == 1
    assert candidate(nums = [2, 4, 6, 8],k = 2) == 1
    assert candidate(nums = [4, 6, 7, 8],k = 6) == 2
    assert candidate(nums = [0, 0, 0],k = 0) == 6
    assert candidate(nums = [1, 2, 4, 8, 16],k = 8) == 1
    assert candidate(nums = [4, 6, 5, 3, 3, 2],k = 3) == 3
    assert candidate(nums = [0, 0, 0, 0],k = 0) == 10
    assert candidate(nums = [1000000000, 1000000000, 1000000000],k = 1000000000) == 6
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1],k = 1) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 8],k = 2) == 6
    assert candidate(nums = [1023, 1023, 1023, 1022, 1023, 1022, 1022],k = 1022) == 21
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 55
    assert candidate(nums = [255, 255, 255, 255, 255, 255],k = 255) == 21
    assert candidate(nums = [7, 3, 15, 8, 8],k = 8) == 5
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31],k = 31) == 36
    assert candidate(nums = [7, 7, 3, 7, 7, 7, 7],k = 7) == 13
    assert candidate(nums = [31, 31, 31, 31, 30, 31],k = 30) == 10
    assert candidate(nums = [8, 4, 2, 1, 0],k = 0) == 11
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],k = 1) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 210
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 0) == 512
    assert candidate(nums = [15, 30, 30, 60, 60, 120],k = 30) == 3
    assert candidate(nums = [8, 8, 12, 8, 8, 8],k = 8) == 20
    assert candidate(nums = [2147483647, 2147483647, 2147483647],k = 2147483647) == 6
    assert candidate(nums = [1, 2, 4, 8, 16, 32],k = 4) == 1
    assert candidate(nums = [1023, 1023, 1023, 1023, 1023],k = 1023) == 15
    assert candidate(nums = [1023, 1023, 1023, 1022, 1023, 1023],k = 1022) == 12
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],k = 1) == 6
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 1
    assert candidate(nums = [15, 15, 15, 15, 15, 15],k = 15) == 21
    assert candidate(nums = [15, 15, 15, 15, 15, 0, 15, 15],k = 15) == 18
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 0, 0, 0, 0, 0],k = 0) == 65
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],k = 15) == 496
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 210
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 1
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 8) == 55
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],k = 255) == 55
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 0, 31],k = 31) == 56
    assert candidate(nums = [7, 6, 7, 6, 7],k = 6) == 12
    assert candidate(nums = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536],k = 3) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 1
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127],k = 1) == 7
    assert candidate(nums = [7, 7, 3, 7, 3, 3, 7],k = 3) == 23
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 1
    assert candidate(nums = [15, 15, 15, 15, 15, 15, 15, 15],k = 15) == 36
    assert candidate(nums = [15, 14, 13, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 2
    assert candidate(nums = [8, 12, 8, 12, 8, 12, 8, 12, 8, 12],k = 8) == 50
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 1
    assert candidate(nums = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256, 256, 512, 512, 1024, 1024],k = 1) == 3
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255],k = 255) == 55
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],k = 1) == 22
    assert candidate(nums = [3, 7, 5, 3, 7, 5, 3, 7, 5],k = 5) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 1
    assert candidate(nums = [7, 7, 7, 0, 7, 7],k = 7) == 9
    assert candidate(nums = [15, 15, 15, 15, 14, 14, 15],k = 14) == 17
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31],k = 31) == 28
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 10) == 210
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31],k = 31) == 210
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 1225
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 1) == 10
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 1) == 20
    assert candidate(nums = [63, 63, 63, 62, 63, 63, 63],k = 62) == 16
    assert candidate(nums = [31, 15, 7, 3, 1, 1, 3, 7, 15, 31],k = 3) == 8
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 7) == 465
    assert candidate(nums = [64, 32, 16, 8, 4, 2, 1, 2, 4, 8, 16, 32, 64],k = 1) == 1
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 1) == 120
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 8) == 210
    assert candidate(nums = [31, 31, 31, 31, 31, 31, 31],k = 31) == 28
    assert candidate(nums = [1073741824, 1073741824, 1073741824, 1073741824, 1073741824],k = 1073741824) == 15
    assert candidate(nums = [123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123],k = 123) == 496
    assert candidate(nums = [7, 14, 28, 28, 56],k = 28) == 3
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16],k = 2) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 0) == 1128
    assert candidate(nums = [4, 8, 8, 16, 32, 32, 64],k = 32) == 3
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 4) == 1
    assert candidate(nums = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 255],k = 255) == 79
    assert candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023],k = 1023) == 28
    assert candidate(nums = [255, 255, 255, 254, 255, 255, 255],k = 254) == 16
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 1128
    assert candidate(nums = [7, 14, 28, 14, 7],k = 7) == 2
    assert candidate(nums = [15, 15, 15, 14, 15, 15, 14, 15],k = 14) == 26
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256],k = 2) == 1
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 2) == 210
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1024) == 1
    assert candidate(nums = [255, 255, 255, 254, 255, 254, 255, 254, 255, 254],k = 254) == 46
    assert candidate(nums = [8, 4, 2, 1, 2, 4, 8],k = 4) == 2
    assert candidate(nums = [2, 6, 2, 2, 6, 2, 2, 6, 2, 2],k = 2) == 52
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15],k = 3) == 1
    assert candidate(nums = [255, 127, 63, 31, 15, 7, 3, 1],k = 1) == 8
    assert candidate(nums = [1023, 511, 255, 127, 63, 31, 15, 7, 3, 1],k = 1) == 10
    assert candidate(nums = [7, 7, 11, 7, 7, 7, 11, 11, 7],k = 7) == 10
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128],k = 2) == 1
    assert candidate(nums = [255, 255, 255, 255, 255],k = 255) == 15
    assert candidate(nums = [2, 3, 1, 2, 1, 1, 2, 3],k = 1) == 5
    assert candidate(nums = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38],k = 2) == 38
    assert candidate(nums = [6, 6, 6, 6, 6, 7, 6, 6, 6, 6],k = 6) == 54
    assert candidate(nums = [1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 1023, 0, 1023],k = 1023) == 56
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 1) == 38
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 8) == 1326
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],k = 1) == 10
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],k = 1000000000) == 10
    assert candidate(nums = [2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6],k = 2) == 72
