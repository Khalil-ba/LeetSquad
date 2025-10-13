# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 3, 2, 4, 5]) == 3
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(nums = [9, 7, 5, 3, 1]) == 0
    assert candidate(nums = [2, 1]) == 0
    assert candidate(nums = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9]) == 5
    assert candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == 0
    assert candidate(nums = [10, 20, 15, 30, 25, 40]) == 2
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 8
    assert candidate(nums = [10, 5, 15, 3, 7, 12, 18]) == 1
    assert candidate(nums = [-1, 5, 2]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
    assert candidate(nums = [1, 10, 3, 9, 5, 8, 6, 7, 4, 2]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5]) == 5
    assert candidate(nums = [1, 5, 3, 4, 2]) == 1
    assert candidate(nums = [10, 5, 15, 3, 7, 18]) == 1
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35]) == 1
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]) == 0
    assert candidate(nums = [3, 1, 4, 2]) == 0
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 1
    assert candidate(nums = [20, 10, 30, 5, 15, 25, 35, 0, 2, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36]) == 1
    assert candidate(nums = [1, 3, 2, 4, 5, 6]) == 4
    assert candidate(nums = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2]) == 2
    assert candidate(nums = [7]) == 1
    assert candidate(nums = [3, 1, 2]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 50
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7]) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 190, 200]) == 2
    assert candidate(nums = [100000, -100000, 0, 50000, -50000]) == 0
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 37
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 1, 2, 3, 4, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 15
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == 2
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]) == 7
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 4, 6, 10]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15]) == 5
    assert candidate(nums = [20, 30, 10, 40, 50, 60, 5, 15, 25, 35, 45, 55, 65]) == 1
    assert candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10]) == 1
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == 4
    assert candidate(nums = [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [9, 4, 2, 1, 3, 6, 5, 7, 8]) == 0
    assert candidate(nums = [10, 20, 30, 25, 26, 27, 28, 29, 15, 16, 17, 18, 19, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(nums = [5, 3, 8, 6, 7, 2, 4, 1, 9]) == 1
    assert candidate(nums = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 2, 1]) == 1
    assert candidate(nums = [1, 5, 3, 7, 6, 11, 10, 13, 12, 17, 16, 19, 18, 21, 20, 23, 22, 25, 24, 26]) == 2
    assert candidate(nums = [1, 5, 2, 3, 6, 4, 7, 8, 9, 10]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 11
    assert candidate(nums = [50, 10, 30, 20, 40, 60, 50, 70, 80, 90]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]) == 5
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 30, 29]) == 0
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250, -300, -350, -400, -450, -500, -550, -600, -650, -700, -750, -800, -850, -900, -950]) == 0
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 1
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [20, 15, 25, 10, 30, 5, 27, 35, 17, 18, 19, 32, 31, 33, 34, 36, 37, 38, 39, 40]) == 5
    assert candidate(nums = [1, 5, 3, 7, 9, 11, 13, 15, 17, 19]) == 8
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 25
    assert candidate(nums = [1, 2, 4, 3, 5, 7, 6, 8, 10, 9]) == 4
    assert candidate(nums = [10, 5, 3, 1, 2, 8, 6, 4, 7, 9]) == 0
    assert candidate(nums = [5, 8, 6, 7, 9, 2, 1, 3, 4, 10]) == 1
    assert candidate(nums = [5, 9, 3, 7, 1, 8, 2, 6, 4, 10]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 40
    assert candidate(nums = [3, 1, 4, 2, 5]) == 1
    assert candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20, 23, 22]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [9, 5, 7, 3, 8, 6, 4, 2, 1, 10, 11, 12, 13]) == 4
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 15
    assert candidate(nums = [30, 20, 10, 15, 25, 5, 40, 50, 60, 70]) == 4
    assert candidate(nums = [10, 5, 15, 3, 7, 18, 25, 2, 8, 13, 20, 28, 1, 4, 6, 9, 11, 14, 16, 17, 19, 21, 22, 23, 24, 26, 27, 29, 30]) == 2
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 30
    assert candidate(nums = [1, 2, 3, 10, 5, 6, 7, 8, 9, 4]) == 3
    assert candidate(nums = [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 15, 25, 35, 45, 55]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(nums = [25, 20, 26, 15, 21, 30, 22, 27, 23, 28, 24, 29, 10, 16, 35, 12, 17, 40, 13, 18]) == 0
    assert candidate(nums = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums = [24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3]) == 1
    assert candidate(nums = [100000, -100000, 50000, 25000, -50000, 75000]) == 0
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(nums = [5, 4, 3, 2, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == 8
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10]) == 4
    assert candidate(nums = [5, 3, 8, 1, 9, 7, 2, 6, 4, 10]) == 1
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 0
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 1
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 2
    assert candidate(nums = [42, 23, 65, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 1
    assert candidate(nums = [3, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10]) == 0
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 1
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == 5
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == 15
    assert candidate(nums = [1, 3, 2, 4, 5]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]) == 5
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == 0
    assert candidate(nums = [100, 50, 25, 75, 125, 10, 60, 40, 90, 130, 30, 80, 110, 70, 140, 20, 150, 160, 105, 170]) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == 5
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(nums = [10, 5, 1, 8, 12, 15, 7, 9, 14, 3, 2, 11, 6]) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == 0
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 11
    assert candidate(nums = [20, 15, 25, 10, 18, 22, 30, 5, 8]) == 0
    assert candidate(nums = [1, 2, 5, 4, 3, 6, 7, 8, 9, 10]) == 7
    assert candidate(nums = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 0
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 0
    assert candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 2, 1]) == 1
    assert candidate(nums = [33, 21, 45, 19, 50, 27, 39, 40, 25, 31, 29, 42]) == 0
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20]) == 2
    assert candidate(nums = [15, 10, 20, 5, 12, 18, 3, 7, 17, 25]) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 12
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 0
    assert candidate(nums = [100, 1, 101, 2, 102, 3, 103, 4, 104, 5]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 15
    assert candidate(nums = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]) == 0
