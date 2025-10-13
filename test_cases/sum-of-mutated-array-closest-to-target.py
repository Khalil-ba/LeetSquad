# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [1, 2, 3, 4, 5],target = 11) == 3
    assert candidate(arr = [5, 5, 5, 5, 5],target = 17) == 3
    assert candidate(arr = [10, 20, 30, 40, 50],target = 100) == 23
    assert candidate(arr = [2, 3, 5],target = 10) == 5
    assert candidate(arr = [9, 9, 9, 9, 9],target = 40) == 8
    assert candidate(arr = [10000, 10000, 10000],target = 10000) == 3333
    assert candidate(arr = [99999, 99999, 99999, 99999],target = 100000) == 25000
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 50) == 7
    assert candidate(arr = [60864, 25176, 27249, 21296, 20204],target = 56803) == 11361
    assert candidate(arr = [100000, 100000, 100000],target = 100000) == 33333
    assert candidate(arr = [100000, 100000, 100000],target = 299999) == 100000
    assert candidate(arr = [5, 5, 5, 5, 5],target = 20) == 4
    assert candidate(arr = [10, 20, 30],target = 25) == 8
    assert candidate(arr = [1, 1, 1, 1, 1],target = 3) == 1
    assert candidate(arr = [1, 2, 3, 4, 5],target = 15) == 5
    assert candidate(arr = [100000, 100000, 100000],target = 250000) == 83333
    assert candidate(arr = [4, 9, 3],target = 10) == 3
    assert candidate(arr = [1, 1, 1, 1, 1],target = 5) == 1
    assert candidate(arr = [10000, 20000, 30000, 40000, 50000],target = 100000) == 23333
    assert candidate(arr = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],target = 95000) == 9500
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 100) == 7
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 0
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 50) == 0
    assert candidate(arr = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],target = 30000) == 3429
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5],target = 20) == 2
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 1
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 100) == 5
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 4500) == 600
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 100) == 9
    assert candidate(arr = [50000, 25000, 75000, 12500, 100000],target = 100000) == 21875
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 150) == 13
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 50) == 1
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 500) == 95
    assert candidate(arr = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],target = 45000) == 4500
    assert candidate(arr = [1, 2, 3, 100000, 99999, 1, 2, 3, 100000, 99999],target = 300000) == 74997
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 200) == 16
    assert candidate(arr = [10000, 20000, 30000, 40000, 50000],target = 150000) == 50000
    assert candidate(arr = [23, 1, 32, 43, 54, 65, 76, 87, 98, 109, 120, 131, 142, 153, 164],target = 900) == 76
    assert candidate(arr = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],target = 100000) == 10000
    assert candidate(arr = [23, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90],target = 1500) == 48
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 40) == 5
    assert candidate(arr = [99999, 99999, 99999, 99999, 99999],target = 499995) == 99999
    assert candidate(arr = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],target = 500000) == 50000
    assert candidate(arr = [10, 20, 30, 40, 50],target = 120) == 30
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 50) == 5
    assert candidate(arr = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 1000],target = 300000) == 39833
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 1
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 550) == 100
    assert candidate(arr = [1, 1000, 100000, 1000000, 10000000],target = 5000000) == 3898999
    assert candidate(arr = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],target = 550000) == 100000
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 20) == 2
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 150) == 10
    assert candidate(arr = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],target = 900000) == 90000
    assert candidate(arr = [5, 15, 25, 35, 45, 55],target = 150) == 35
    assert candidate(arr = [1, 10, 100, 1000, 10000],target = 12345) == 10000
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 4500) == 600
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 210) == 20
    assert candidate(arr = [100, 150, 200, 250, 300],target = 800) == 183
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 30) == 3
    assert candidate(arr = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],target = 500000) == 50000
    assert candidate(arr = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],target = 150) == 7
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 75) == 10
    assert candidate(arr = [1, 100000, 2, 99999, 3, 99998],target = 100000) == 33331
    assert candidate(arr = [1, 3, 5, 7, 9],target = 25) == 9
    assert candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995],target = 300000) == 50000
    assert candidate(arr = [100000, 1, 50000, 25000, 75000],target = 150000) == 41666
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],target = 10000) == 567
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 250) == 27
    assert candidate(arr = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50],target = 200) == 23
    assert candidate(arr = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 300) == 37
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 1000) == 92
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 1500) == 95
    assert candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],target = 1000) == 50
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],target = 7500) == 600
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 200) == 12
    assert candidate(arr = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],target = 8000) == 800
    assert candidate(arr = [50, 50, 50, 50, 50, 50],target = 200) == 33
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1000) == 1
    assert candidate(arr = [1000, 2000, 3000, 4000, 5000],target = 10000) == 2333
    assert candidate(arr = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],target = 450) == 45
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 20) == 2
    assert candidate(arr = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],target = 550000) == 100000
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 3
    assert candidate(arr = [10, 20, 30, 40, 50],target = 150) == 50
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 45) == 6
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 733
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 225) == 30
    assert candidate(arr = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],target = 550) == 59
    assert candidate(arr = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],target = 300000) == 100000
    assert candidate(arr = [50, 40, 30, 20, 10],target = 150) == 50
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 45) == 6
    assert candidate(arr = [1, 10, 100, 1000, 10000],target = 11111) == 10000
    assert candidate(arr = [99999, 1, 99998, 2, 99997, 3, 99996, 4, 99995, 5],target = 499950) == 99987
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 50) == 3
    assert candidate(arr = [100, 200, 300, 400, 500],target = 1400) == 400
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 0
    assert candidate(arr = [50000, 50000, 50000, 50000, 50000],target = 200000) == 40000
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 55) == 10
    assert candidate(arr = [1, 100, 1000, 10000, 100000],target = 12345) == 5622
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 1000) == 92
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 3000) == 343
    assert candidate(arr = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],target = 200) == 20
    assert candidate(arr = [1, 2, 3, 4, 5],target = 15) == 5
    assert candidate(arr = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],target = 55000) == 10000
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 25) == 2
    assert candidate(arr = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000],target = 80000) == 9000
    assert candidate(arr = [1, 10000, 2, 9999, 3, 9998, 4, 9997, 5, 9996],target = 50000) == 9997
    assert candidate(arr = [50000, 40000, 30000, 20000, 10000],target = 100000) == 23333
    assert candidate(arr = [10000, 20000, 30000, 40000, 50000],target = 120000) == 30000
    assert candidate(arr = [100, 200, 300, 400, 500],target = 1000) == 233
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],target = 25) == 3
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 100) == 19
