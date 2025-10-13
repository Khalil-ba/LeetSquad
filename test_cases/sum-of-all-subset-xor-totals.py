# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 1, 6]) == 28
    assert candidate(nums = [10, 20, 30]) == 120
    assert candidate(nums = [1, 1, 1, 1]) == 8
    assert candidate(nums = [1, 2, 4, 8, 16]) == 496
    assert candidate(nums = [10, 11, 12]) == 60
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14]) == 896
    assert candidate(nums = [2, 3, 5]) == 28
    assert candidate(nums = [11, 2, 3, 14, 7]) == 240
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [7, 8, 9, 10, 11]) == 240
    assert candidate(nums = [1, 2, 3, 4]) == 56
    assert candidate(nums = [3, 4, 5, 6, 7, 8]) == 480
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 30720
    assert candidate(nums = [12, 34, 56]) == 248
    assert candidate(nums = [10, 15, 20, 25]) == 248
    assert candidate(nums = [2, 3, 5, 7]) == 56
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9]) == 63488
    assert candidate(nums = [1, 3]) == 6
    assert candidate(nums = [2, 2, 2, 2]) == 16
    assert candidate(nums = [1, 2, 4, 8, 16, 32]) == 2016
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 15360
    assert candidate(nums = [15, 16, 17, 18, 19, 20]) == 992
    assert candidate(nums = [1, 2, 3]) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2048
    assert candidate(nums = [6, 3, 5, 2, 1, 9]) == 480
    assert candidate(nums = [31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2, 1]) == 63488
    assert candidate(nums = [1, 2, 4, 8, 16, 32]) == 2016
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]) == 516096
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 67092480
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == 1984
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16252928
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]) == 8386560
    assert candidate(nums = [15, 20, 25, 30]) == 248
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]) == 129024
    assert candidate(nums = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 1073479680
    assert candidate(nums = [3, 3, 3, 5, 5, 5, 7, 7, 7, 11, 11, 11]) == 30720
    assert candidate(nums = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 130560
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64]) == 8128
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75]) == 8128
    assert candidate(nums = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8]) == 63488
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84]) == 260096
    assert candidate(nums = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == 260096
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 245760
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 16773120
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]) == 260096
    assert candidate(nums = [31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 1015808
    assert candidate(nums = [31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9]) == 63488
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]) == 516096
    assert candidate(nums = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 63488
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 4186112
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 16773120
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41]) == 8064
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 129024
    assert candidate(nums = [13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113, 123]) == 260096
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 63488
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 30720
    assert candidate(nums = [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168]) == 520192
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 14336
    assert candidate(nums = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8]) == 63488
    assert candidate(nums = [14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91]) == 260096
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 4186112
    assert candidate(nums = [2, 3, 4, 5, 6]) == 112
    assert candidate(nums = [12, 14, 18, 22, 26, 30]) == 960
    assert candidate(nums = [10, 15, 20, 25]) == 248
    assert candidate(nums = [17, 19, 21, 23, 25, 27, 29, 31]) == 3968
    assert candidate(nums = [3, 5, 7, 9, 11, 13]) == 480
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 8386560
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 16128
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]) == 8386560
    assert candidate(nums = [15, 25, 35, 45, 55]) == 1008
    assert candidate(nums = [10, 20, 30, 40, 50]) == 992
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 15360
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41]) == 8064
    assert candidate(nums = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]) == 129024
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 129024
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 258048
    assert candidate(nums = [3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91]) == 251904
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104]) == 16256
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14]) == 896
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 258048
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9]) == 63488
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 14336
    assert candidate(nums = [31, 33, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]) == 260096
    assert candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]) == 129024
    assert candidate(nums = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]) == 129024
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512]) == 65024
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132]) == 522240
    assert candidate(nums = [19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == 260096
    assert candidate(nums = [15, 20, 25, 30, 35, 40, 45]) == 4032
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 15360
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7]) == 1984
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]) == 245760
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]) == 129024
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4]) == 30720
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 63488
    assert candidate(nums = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30720
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 30720
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == 16128
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19]) == 3968
