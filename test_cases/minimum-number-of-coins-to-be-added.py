# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(coins = [3, 6, 9],target = 15) == 2
    assert candidate(coins = [2, 5, 10],target = 20) == 2
    assert candidate(coins = [1, 4, 10],target = 19) == 2
    assert candidate(coins = [1, 1, 1],target = 20) == 3
    assert candidate(coins = [1, 4, 10, 5, 7, 19],target = 19) == 1
    assert candidate(coins = [1, 2, 4, 8, 16],target = 31) == 0
    assert candidate(coins = [1, 3, 7, 15, 31, 63, 127],target = 256) == 2
    assert candidate(coins = [1, 2, 5, 10, 20],target = 99) == 3
    assert candidate(coins = [1, 5, 10, 25, 50, 100],target = 500) == 5
    assert candidate(coins = [1, 10, 25, 50, 100],target = 300) == 4
    assert candidate(coins = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],target = 150) == 1
    assert candidate(coins = [1, 3, 6, 13, 26, 52],target = 100) == 1
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 100) == 1
    assert candidate(coins = [2, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101],target = 100000) == 8
    assert candidate(coins = [1, 2, 3, 5, 10, 20, 50, 100],target = 1000) == 4
    assert candidate(coins = [10, 20, 30, 40, 50],target = 150) == 4
    assert candidate(coins = [1, 3, 6, 12, 24, 48],target = 100) == 2
    assert candidate(coins = [5, 11, 17, 23, 29, 35, 41, 47, 53],target = 200) == 3
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256],target = 512) == 1
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 0
    assert candidate(coins = [1, 2, 5, 10, 20, 50],target = 99) == 2
    assert candidate(coins = [2, 6, 18, 54],target = 150) == 5
    assert candidate(coins = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 400) == 4
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],target = 2048) == 1
    assert candidate(coins = [1, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432],target = 1000000) == 1
    assert candidate(coins = [1, 1, 2, 2, 5, 5, 10, 10],target = 50) == 1
    assert candidate(coins = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23],target = 100) == 0
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100],target = 500) == 4
    assert candidate(coins = [2, 4, 6, 8, 10],target = 25) == 1
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000],target = 100000) == 5
    assert candidate(coins = [3, 7, 15, 23],target = 50) == 3
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 30) == 0
    assert candidate(coins = [1, 3, 6, 12],target = 50) == 3
    assert candidate(coins = [2, 6, 10, 14, 18, 22],target = 50) == 2
    assert candidate(coins = [2, 6, 10, 14, 18, 22],target = 100) == 3
    assert candidate(coins = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99],target = 100) == 2
    assert candidate(coins = [3, 6, 9, 12, 15, 18, 21, 24, 27],target = 100) == 2
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64],target = 128) == 1
    assert candidate(coins = [1, 2, 3, 6, 12, 24, 48],target = 100) == 1
    assert candidate(coins = [5, 12, 19, 26, 33, 40, 47, 54, 61, 68, 75],target = 200) == 3
    assert candidate(coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 250) == 3
    assert candidate(coins = [1, 3, 7, 11, 15],target = 30) == 1
    assert candidate(coins = [2, 3, 6, 9, 18],target = 50) == 2
    assert candidate(coins = [3, 6, 9, 12],target = 45) == 3
    assert candidate(coins = [1, 3, 5, 7, 9, 11],target = 50) == 2
    assert candidate(coins = [5, 9, 12, 18, 23, 34, 41, 50, 65, 78, 90, 100, 120, 150, 200],target = 500) == 3
    assert candidate(coins = [1, 3, 6, 12, 24, 48, 96, 192],target = 500) == 2
    assert candidate(coins = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 8, 16, 16, 16],target = 100) == 1
    assert candidate(coins = [1, 2, 3, 5, 11, 21, 41],target = 100) == 1
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000],target = 100000) == 5
    assert candidate(coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 100) == 4
    assert candidate(coins = [2, 6, 18, 54],target = 100) == 4
    assert candidate(coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],target = 200) == 3
    assert candidate(coins = [1, 5, 10, 25, 50],target = 120) == 3
    assert candidate(coins = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],target = 999999) == 1
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64],target = 127) == 0
    assert candidate(coins = [2, 3, 5, 7, 11, 13],target = 50) == 2
    assert candidate(coins = [1, 5, 10, 25],target = 100) == 4
    assert candidate(coins = [1, 1, 2, 2, 5, 5],target = 50) == 2
    assert candidate(coins = [5, 10, 20, 50],target = 100) == 4
    assert candidate(coins = [2, 3, 5, 7, 11],target = 30) == 2
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],target = 32767) == 0
    assert candidate(coins = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],target = 200) == 0
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 50) == 0
    assert candidate(coins = [1, 5, 10, 25, 50],target = 99) == 3
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1024) == 1
    assert candidate(coins = [5, 7, 11, 23],target = 100) == 4
    assert candidate(coins = [1, 3, 9, 30],target = 50) == 3
    assert candidate(coins = [1, 5, 10, 25, 50],target = 100) == 3
    assert candidate(coins = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023],target = 2047) == 2
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128],target = 255) == 0
    assert candidate(coins = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000],target = 99999) == 6
    assert candidate(coins = [7, 14, 21, 28, 35, 42, 49],target = 100) == 3
    assert candidate(coins = [5, 10, 20, 50, 100],target = 200) == 4
    assert candidate(coins = [1, 3, 4, 7, 10, 12, 15, 18],target = 100) == 2
    assert candidate(coins = [5, 10, 20, 50, 100, 200],target = 1000) == 6
    assert candidate(coins = [1, 5, 10, 20, 50, 100],target = 300) == 4
    assert candidate(coins = [1, 1, 2, 4, 8, 16, 32, 64, 128],target = 255) == 0
    assert candidate(coins = [10, 20, 30, 40, 50],target = 100) == 4
    assert candidate(coins = [1, 2, 5, 10, 20, 50],target = 100) == 2
    assert candidate(coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 100) == 3
    assert candidate(coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 550) == 4
    assert candidate(coins = [1, 5, 10, 25, 50, 100],target = 300) == 4
    assert candidate(coins = [1, 5, 10, 25],target = 100) == 4
    assert candidate(coins = [2, 4, 8, 16, 32],target = 100) == 2
    assert candidate(coins = [2, 3, 6, 11],target = 30) == 2
    assert candidate(coins = [1, 2, 5, 10, 20, 50],target = 100) == 2
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000],target = 5000000) == 7
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 55) == 0
    assert candidate(coins = [1, 2, 4, 8, 16],target = 100) == 2
    assert candidate(coins = [1, 3, 5, 7, 9, 11, 13, 15],target = 100) == 2
    assert candidate(coins = [7, 14, 28, 56],target = 100) == 3
    assert candidate(coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],target = 60) == 2
    assert candidate(coins = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210],target = 210) == 3
    assert candidate(coins = [1, 2, 3, 5, 8, 13, 21],target = 50) == 0
    assert candidate(coins = [1, 3, 7, 15, 31, 63],target = 128) == 2
    assert candidate(coins = [10, 20, 30, 40, 50],target = 200) == 5
    assert candidate(coins = [5, 10, 20, 40, 80],target = 200) == 4
    assert candidate(coins = [1, 2, 6, 14, 30],target = 63) == 2
    assert candidate(coins = [2, 6, 14, 30, 62, 126],target = 255) == 3
    assert candidate(coins = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60],target = 60) == 1
    assert candidate(coins = [3, 9, 27, 81],target = 243) == 6
    assert candidate(coins = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98],target = 100) == 3
    assert candidate(coins = [1, 3, 6, 12, 24],target = 100) == 3
    assert candidate(coins = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],target = 200) == 2
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 50) == 0
    assert candidate(coins = [3, 7, 11, 25],target = 60) == 3
    assert candidate(coins = [1, 2, 5, 10, 25],target = 100) == 3
    assert candidate(coins = [5, 10, 25],target = 100) == 5
    assert candidate(coins = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300],target = 300) == 1
