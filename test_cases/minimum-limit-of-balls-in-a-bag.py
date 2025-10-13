# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 5, 5, 5, 5],maxOperations = 10) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],maxOperations = 9) == 5
    assert candidate(nums = [1000000000],maxOperations = 1) == 500000000
    assert candidate(nums = [3, 3, 3, 3],maxOperations = 0) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],maxOperations = 5) == 2
    assert candidate(nums = [100, 100, 100, 100],maxOperations = 10) == 34
    assert candidate(nums = [1, 1, 1, 1, 1],maxOperations = 0) == 1
    assert candidate(nums = [1000000000],maxOperations = 999999999) == 1
    assert candidate(nums = [1000000000],maxOperations = 1000000000) == 1
    assert candidate(nums = [7, 17],maxOperations = 2) == 7
    assert candidate(nums = [9],maxOperations = 2) == 3
    assert candidate(nums = [10, 20, 30, 40, 50],maxOperations = 10) == 10
    assert candidate(nums = [2, 4, 8, 2],maxOperations = 4) == 2
    assert candidate(nums = [1000000000, 1000000000],maxOperations = 1) == 1000000000
    assert candidate(nums = [10, 10, 10],maxOperations = 6) == 4
    assert candidate(nums = [10, 10, 10],maxOperations = 3) == 5
    assert candidate(nums = [7, 14, 21, 28],maxOperations = 3) == 14
    assert candidate(nums = [1, 1, 1, 1],maxOperations = 2) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxOperations = 5) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maxOperations = 5) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxOperations = 5) == 50
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000],maxOperations = 9) == 100000000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],maxOperations = 25) == 180
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000],maxOperations = 30) == 3449
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maxOperations = 29) == 1
    assert candidate(nums = [1000000000, 1000000000, 1000000000],maxOperations = 3) == 500000000
    assert candidate(nums = [999999999, 1],maxOperations = 1) == 500000000
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],maxOperations = 9) == 100
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000],maxOperations = 10) == 142857143
    assert candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],maxOperations = 5) == 999
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000],maxOperations = 3) == 333333334
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000],maxOperations = 5) == 250000000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],maxOperations = 20) == 44
    assert candidate(nums = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],maxOperations = 9) == 100000000
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],maxOperations = 15) == 10
    assert candidate(nums = [999999999, 999999998, 999999997, 999999996, 999999995],maxOperations = 10) == 333333333
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],maxOperations = 10) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],maxOperations = 14) == 5
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],maxOperations = 50) == 18
    assert candidate(nums = [1000000000],maxOperations = 0) == 1000000000
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],maxOperations = 50) == 3
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],maxOperations = 19) == 1000
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],maxOperations = 10) == 500
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],maxOperations = 9) == 50
    assert candidate(nums = [1000000000, 500000000, 250000000],maxOperations = 3) == 333333334
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],maxOperations = 10) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxOperations = 15) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],maxOperations = 30) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maxOperations = 0) == 1
    assert candidate(nums = [1, 1000000000, 1],maxOperations = 1000000000) == 1
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999],maxOperations = 5) == 500000000
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9],maxOperations = 5) == 166666667
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],maxOperations = 19) == 7
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999],maxOperations = 10) == 333333333
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],maxOperations = 50) == 10000
    assert candidate(nums = [1, 1, 1, 1, 1000000000],maxOperations = 999999) == 1000
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],maxOperations = 30) == 6
    assert candidate(nums = [1000000000, 1000000000, 1000000000],maxOperations = 2999999997) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxOperations = 20) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],maxOperations = 20) == 20
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999],maxOperations = 4999999995) == 2
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],maxOperations = 10) == 142857143
    assert candidate(nums = [500000000, 500000000, 500000000, 500000000, 500000000],maxOperations = 1000000) == 2500
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],maxOperations = 15) == 7
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],maxOperations = 50) == 9
    assert candidate(nums = [500000000, 500000000, 500000000, 500000000, 500000000],maxOperations = 10) == 166666667
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],maxOperations = 30) == 50
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],maxOperations = 45) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxOperations = 10) == 4
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],maxOperations = 20) == 5
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],maxOperations = 15) == 114
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999],maxOperations = 4) == 500000000
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],maxOperations = 20) == 5
    assert candidate(nums = [2, 3, 6, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],maxOperations = 100) == 6
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],maxOperations = 50) == 1171
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],maxOperations = 20) == 19
    assert candidate(nums = [100, 200, 300, 400, 500],maxOperations = 15) == 84
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],maxOperations = 10) == 74
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maxOperations = 5) == 1
    assert candidate(nums = [999999999, 999999998, 999999997],maxOperations = 2) == 999999997
    assert candidate(nums = [100, 200, 300, 400, 500],maxOperations = 50) == 29
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],maxOperations = 5) == 5
    assert candidate(nums = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999],maxOperations = 10) == 500000000
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],maxOperations = 5) == 500000
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],maxOperations = 9999999990) == 2
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],maxOperations = 45) == 100
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],maxOperations = 10) == 10000000
    assert candidate(nums = [500000000, 500000000, 500000000, 500000000],maxOperations = 3) == 500000000
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000],maxOperations = 50) == 28572
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],maxOperations = 100) == 500
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],maxOperations = 20) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],maxOperations = 0) == 10
    assert candidate(nums = [1000000000, 1000000000, 1000000000],maxOperations = 2) == 1000000000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maxOperations = 30) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],maxOperations = 10) == 350
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],maxOperations = 9) == 8
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],maxOperations = 25) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],maxOperations = 9) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],maxOperations = 10) == 7
