# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(rewardValues = [1, 2, 3, 4, 5]) == 9
    assert candidate(rewardValues = [1, 1, 3, 3]) == 4
    assert candidate(rewardValues = [50000, 40000, 30000, 20000, 10000]) == 90000
    assert candidate(rewardValues = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2]) == 3
    assert candidate(rewardValues = [1, 6, 4, 3, 2]) == 11
    assert candidate(rewardValues = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 37
    assert candidate(rewardValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(rewardValues = [10000, 10000, 10000, 10000, 10000]) == 10000
    assert candidate(rewardValues = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 17
    assert candidate(rewardValues = [10, 9, 8, 7, 6]) == 19
    assert candidate(rewardValues = [1]) == 1
    assert candidate(rewardValues = [10, 20, 30, 40, 50]) == 90
    assert candidate(rewardValues = [50000, 25000, 12500, 6250, 3125]) == 96875
    assert candidate(rewardValues = [5, 5, 5, 5, 5]) == 5
    assert candidate(rewardValues = [50000, 40000, 30000, 20000, 10000]) == 90000
    assert candidate(rewardValues = [1, 5, 1, 5, 1]) == 6
    assert candidate(rewardValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(rewardValues = [50000, 50000, 50000, 50000, 50000]) == 50000
    assert candidate(rewardValues = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023
    assert candidate(rewardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
    assert candidate(rewardValues = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 19000
    assert candidate(rewardValues = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 1023
    assert candidate(rewardValues = [1, 1, 1, 1, 1]) == 1
    assert candidate(rewardValues = [5, 4, 3, 2, 1]) == 9
    assert candidate(rewardValues = [42, 35, 18, 27, 5, 14, 8, 23, 9, 22]) == 83
    assert candidate(rewardValues = [3, 6, 2, 8, 5, 10, 4, 12, 7, 14, 1, 9, 11, 13, 15]) == 29
    assert candidate(rewardValues = [50000, 40000, 30000, 20000, 10000, 9000, 8000, 7000, 6000, 5000]) == 99000
    assert candidate(rewardValues = [50000, 10000, 20000, 30000, 40000, 5000, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 99000
    assert candidate(rewardValues = [50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50019
    assert candidate(rewardValues = [99999, 49999, 24999, 12499, 6249, 3124, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1]) == 199988
    assert candidate(rewardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 29
    assert candidate(rewardValues = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 1111111111
    assert candidate(rewardValues = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0]) == 17
    assert candidate(rewardValues = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 3900
    assert candidate(rewardValues = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 99
    assert candidate(rewardValues = [4, 3, 2, 1, 8, 7, 6, 5, 12, 11, 10, 9, 16, 15, 14, 13]) == 31
    assert candidate(rewardValues = [5, 3, 8, 6, 2, 7, 4, 1, 9, 10]) == 19
    assert candidate(rewardValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 190
    assert candidate(rewardValues = [50000, 40000, 30000, 20000, 10000, 5000, 1000, 500, 100, 50]) == 96650
    assert candidate(rewardValues = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 10000
    assert candidate(rewardValues = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 39
    assert candidate(rewardValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(rewardValues = [2, 3, 7, 8, 10, 14, 15, 18, 20, 22, 25, 28, 30]) == 59
    assert candidate(rewardValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(rewardValues = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]) == 131071
    assert candidate(rewardValues = [25000, 24000, 23000, 22000, 21000, 20000, 19000, 18000, 17000, 16000, 15000, 14000, 13000, 12000, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 49000
    assert candidate(rewardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 39
    assert candidate(rewardValues = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 2047
    assert candidate(rewardValues = [1, 2, 4, 8, 16, 32, 64, 128]) == 255
    assert candidate(rewardValues = [50000, 40000, 30000, 20000, 10000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, 9, 4, 2, 1]) == 99995
    assert candidate(rewardValues = [1, 10, 100, 1000, 10000, 100000, 50000, 25000, 12500, 6250, 3125]) == 198611
    assert candidate(rewardValues = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]) == 239
    assert candidate(rewardValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 290
    assert candidate(rewardValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(rewardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 49
    assert candidate(rewardValues = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 10000
    assert candidate(rewardValues = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 1048575
    assert candidate(rewardValues = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 17
    assert candidate(rewardValues = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 19999
    assert candidate(rewardValues = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 17
    assert candidate(rewardValues = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == 287
    assert candidate(rewardValues = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 6
    assert candidate(rewardValues = [1, 3, 2, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == 41
    assert candidate(rewardValues = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 11
    assert candidate(rewardValues = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 65535
    assert candidate(rewardValues = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 77
    assert candidate(rewardValues = [3125, 6250, 12500, 25000, 50000, 100000, 10000, 1000, 100, 10, 1]) == 198611
    assert candidate(rewardValues = [1, 10000, 2, 9999, 3, 9998, 4, 9997, 5, 9996, 6, 9995, 7, 9994, 8, 9993]) == 19999
    assert candidate(rewardValues = [50000, 45000, 40000, 35000, 30000, 25000, 20000, 15000, 10000, 5000]) == 95000
    assert candidate(rewardValues = [10000, 20000, 15000, 5000, 2500, 7500, 30000, 1000, 500, 1500]) == 59500
    assert candidate(rewardValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(rewardValues = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991]) == 19999
    assert candidate(rewardValues = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996, 6, 99995, 7, 99994, 8, 99993]) == 199999
    assert candidate(rewardValues = [20000, 18000, 16000, 14000, 12000, 10000, 8000, 6000, 4000, 2000, 1000, 500, 250, 125, 62, 31]) == 39968
    assert candidate(rewardValues = [50000, 40000, 30000, 20000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 99990
    assert candidate(rewardValues = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]) == 50000
    assert candidate(rewardValues = [25000, 20000, 15000, 10000, 5000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45019
    assert candidate(rewardValues = [100, 200, 300, 400, 500, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 990
    assert candidate(rewardValues = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]) == 65534
    assert candidate(rewardValues = [10, 15, 20, 25, 30, 35, 40, 45, 50]) == 95
    assert candidate(rewardValues = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 11
    assert candidate(rewardValues = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 17
    assert candidate(rewardValues = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 99
    assert candidate(rewardValues = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 141
    assert candidate(rewardValues = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 10000
    assert candidate(rewardValues = [10000, 20000, 30000, 40000, 50000, 50000, 40000, 30000, 20000, 10000]) == 90000
    assert candidate(rewardValues = [10000, 20000, 30000, 40000, 50000, 1, 2, 3, 4, 5]) == 90009
