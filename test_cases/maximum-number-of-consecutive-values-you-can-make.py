# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(coins = [1, 3]) == 2
    assert candidate(coins = [1, 2, 5]) == 4
    assert candidate(coins = [2, 2, 2, 2]) == 1
    assert candidate(coins = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 56
    assert candidate(coins = [1]) == 2
    assert candidate(coins = [1, 4, 10, 3, 1]) == 20
    assert candidate(coins = [40000, 40000, 40000, 40000]) == 1
    assert candidate(coins = [4, 3, 2, 1]) == 11
    assert candidate(coins = [100, 200, 300, 400, 500]) == 1
    assert candidate(coins = [1, 2, 3, 4, 5]) == 16
    assert candidate(coins = [1, 1, 1, 1, 1]) == 6
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1024
    assert candidate(coins = [1, 1, 3, 4]) == 10
    assert candidate(coins = [1, 2, 5, 10]) == 4
    assert candidate(coins = [100, 400, 200, 300]) == 1
    assert candidate(coins = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 1
    assert candidate(coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 21
    assert candidate(coins = [2]) == 1
    assert candidate(coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(coins = [10000, 20000, 30000, 40000]) == 1
    assert candidate(coins = [100, 400, 1, 1, 1]) == 4
    assert candidate(coins = [2, 2, 3, 3, 3, 4]) == 1
    assert candidate(coins = [1, 1, 3, 4, 10]) == 20
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 56
    assert candidate(coins = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]) == 84
    assert candidate(coins = [1, 1, 1, 4]) == 8
    assert candidate(coins = [2, 4, 6, 8]) == 1
    assert candidate(coins = [1, 1, 2, 2, 3, 3]) == 13
    assert candidate(coins = [40000]) == 1
    assert candidate(coins = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 2
    assert candidate(coins = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 1
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100]) == 4
    assert candidate(coins = [5, 7, 11, 13, 17, 19, 23, 29, 31]) == 1
    assert candidate(coins = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 31
    assert candidate(coins = [2, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]) == 1
    assert candidate(coins = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 1
    assert candidate(coins = [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == 3073
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]) == 4
    assert candidate(coins = [1, 5, 10, 25, 50, 100, 200, 500, 1000]) == 2
    assert candidate(coins = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 1
    assert candidate(coins = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 1
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2048
    assert candidate(coins = [2, 3, 6, 12, 24, 48, 96, 192, 384, 768]) == 1
    assert candidate(coins = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 111
    assert candidate(coins = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5]) == 41
    assert candidate(coins = [1, 3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576]) == 2
    assert candidate(coins = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 1
    assert candidate(coins = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 73
    assert candidate(coins = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128, 256, 256]) == 1023
    assert candidate(coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 2
    assert candidate(coins = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]) == 1597
    assert candidate(coins = [1, 2, 3, 6, 11, 20, 37, 68, 129, 254]) == 532
    assert candidate(coins = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(coins = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 1
    assert candidate(coins = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 821
    assert candidate(coins = [100, 200, 200, 300, 400, 400, 400, 500, 600, 600, 700, 800, 800, 900, 1000]) == 1
    assert candidate(coins = [2, 2, 3, 3, 3, 5, 5, 5, 5, 7, 7, 7, 7, 7]) == 1
    assert candidate(coins = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 46
    assert candidate(coins = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 1
    assert candidate(coins = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 56
    assert candidate(coins = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 2
    assert candidate(coins = [1, 10, 100, 1000, 10000, 100000, 1000000]) == 2
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048576
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == 8192
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]) == 4
    assert candidate(coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 1
    assert candidate(coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 2
    assert candidate(coins = [10, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10000]) == 1
    assert candidate(coins = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) == 144
    assert candidate(coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 121
    assert candidate(coins = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 1
    assert candidate(coins = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(coins = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 166
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64]) == 128
    assert candidate(coins = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 111
    assert candidate(coins = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 2
    assert candidate(coins = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 2
    assert candidate(coins = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == 1
    assert candidate(coins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 1
    assert candidate(coins = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) == 2
    assert candidate(coins = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]) == 28656
    assert candidate(coins = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 213
    assert candidate(coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 26
    assert candidate(coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 1
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 32768
    assert candidate(coins = [1, 2, 3, 4, 5, 10, 20, 50, 100, 200]) == 46
    assert candidate(coins = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32, 32, 64, 64, 128, 128]) == 511
    assert candidate(coins = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 4, 9, 6, 2, 4, 9]) == 395
    assert candidate(coins = [1, 1, 2, 2, 4, 4, 8, 8, 16, 16]) == 63
    assert candidate(coins = [1, 2, 4, 8, 16, 32, 64, 128]) == 256
    assert candidate(coins = [1, 10, 100, 1000, 10000, 100000]) == 2
    assert candidate(coins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(coins = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 164
    assert candidate(coins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 151
    assert candidate(coins = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]) == 1
    assert candidate(coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]) == 4
    assert candidate(coins = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000, 5000, 10000]) == 2
