# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 5) == 51
    assert candidate(damage = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],armor = 5) == 10
    assert candidate(damage = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],armor = 5) == 46
    assert candidate(damage = [3, 3, 3],armor = 0) == 10
    assert candidate(damage = [2, 7, 4, 3],armor = 4) == 13
    assert candidate(damage = [100, 0, 0, 0],armor = 50) == 51
    assert candidate(damage = [2, 5, 3, 4],armor = 7) == 10
    assert candidate(damage = [100000],armor = 100000) == 1
    assert candidate(damage = [0, 0, 0, 0],armor = 0) == 1
    assert candidate(damage = [5, 5, 5, 5, 5],armor = 3) == 23
    assert candidate(damage = [1, 2, 3, 4, 5],armor = 10) == 11
    assert candidate(damage = [0, 0, 0],armor = 5) == 1
    assert candidate(damage = [1, 1, 1, 1, 1],armor = 0) == 6
    assert candidate(damage = [0, 0, 0, 0],armor = 100) == 1
    assert candidate(damage = [5, 10, 15],armor = 10) == 21
    assert candidate(damage = [100, 200, 300, 400, 500],armor = 150) == 1351
    assert candidate(damage = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],armor = 25) == 251
    assert candidate(damage = [23, 45, 67, 89, 12, 34, 56, 78, 90],armor = 100) == 405
    assert candidate(damage = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],armor = 5) == 96
    assert candidate(damage = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1],armor = 100000) == 400006
    assert candidate(damage = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],armor = 1) == 30
    assert candidate(damage = [10, 20, 30, 40, 50],armor = 0) == 151
    assert candidate(damage = [99999, 1, 1, 1, 1, 1, 1, 1, 1, 1],armor = 50000) == 50009
    assert candidate(damage = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10],armor = 10) == 66
    assert candidate(damage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],armor = 100000) == 1
    assert candidate(damage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 0) == 56
    assert candidate(damage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],armor = 100) == 451
    assert candidate(damage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],armor = 0) == 551
    assert candidate(damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 15) == 46
    assert candidate(damage = [3, 6, 9, 12, 15, 18, 21],armor = 15) == 70
    assert candidate(damage = [99999, 1, 99999, 1, 99999],armor = 50000) == 250000
    assert candidate(damage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],armor = 60) == 491
    assert candidate(damage = [100, 200, 300, 400, 500],armor = 0) == 1501
    assert candidate(damage = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],armor = 1000) == 4501
    assert candidate(damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 15) == 46
    assert candidate(damage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],armor = 90) == 461
    assert candidate(damage = [100, 50, 25, 12, 6],armor = 100) == 94
    assert candidate(damage = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],armor = 50000) == 949991
    assert candidate(damage = [100000, 0, 0, 0, 0, 0, 0, 0, 0, 0],armor = 90000) == 10001
    assert candidate(damage = [10000, 20000, 30000, 40000, 50000],armor = 25000) == 125001
    assert candidate(damage = [100000, 100000, 100000, 100000, 100000],armor = 50000) == 450001
    assert candidate(damage = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],armor = 10) == 91
    assert candidate(damage = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],armor = 15000) == 45001
    assert candidate(damage = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],armor = 0) == 61
    assert candidate(damage = [10, 20, 30, 40, 50],armor = 15) == 136
    assert candidate(damage = [100, 50, 25, 10],armor = 150) == 86
    assert candidate(damage = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],armor = 30) == 471
    assert candidate(damage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],armor = 0) == 5501
    assert candidate(damage = [1, 10, 100, 1000, 10000, 100000],armor = 50000) == 61112
    assert candidate(damage = [99999, 1, 99999, 1, 99999],armor = 99999) == 200001
    assert candidate(damage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],armor = 500) == 5001
    assert candidate(damage = [100, 0, 100, 0, 100, 0, 100],armor = 100) == 301
    assert candidate(damage = [5, 8, 12, 15, 10, 3],armor = 10) == 44
    assert candidate(damage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 5) == 51
    assert candidate(damage = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],armor = 100) == 5401
    assert candidate(damage = [5, 2, 9, 3, 7, 1, 8, 4, 6, 10],armor = 10) == 46
    assert candidate(damage = [100000, 0, 100000, 0, 100000],armor = 50000) == 250001
    assert candidate(damage = [1000, 2000, 3000, 4000, 5000],armor = 10000) == 10001
    assert candidate(damage = [1, 2, 3, 4, 5],armor = 0) == 16
    assert candidate(damage = [100, 200, 300, 400, 500],armor = 100) == 1401
    assert candidate(damage = [99999, 99999, 99999, 99999],armor = 99999) == 299998
    assert candidate(damage = [50, 25, 12, 6, 3, 1, 0, 0, 0, 0],armor = 20) == 78
    assert candidate(damage = [9, 7, 5, 3, 1],armor = 3) == 23
    assert candidate(damage = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],armor = 512) == 512
    assert candidate(damage = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],armor = 20) == 150
    assert candidate(damage = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],armor = 3) == 48
    assert candidate(damage = [1, 3, 2, 6, 4, 5],armor = 4) == 18
    assert candidate(damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 5) == 51
    assert candidate(damage = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],armor = 3) == 28
    assert candidate(damage = [10, 20, 30, 40, 50],armor = 60) == 101
    assert candidate(damage = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],armor = 10) == 71
    assert candidate(damage = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],armor = 99) == 902
    assert candidate(damage = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],armor = 25) == 251
    assert candidate(damage = [100, 200, 300, 400, 500],armor = 250) == 1251
    assert candidate(damage = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195],armor = 50000) == 149804
    assert candidate(damage = [90000, 10000, 1000, 100, 10, 1],armor = 20000) == 81112
    assert candidate(damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],armor = 10) == 111
    assert candidate(damage = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],armor = 8) == 48
    assert candidate(damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],armor = 7) == 114
    assert candidate(damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 100000) == 46
    assert candidate(damage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 0) == 56
    assert candidate(damage = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],armor = 10) == 20
    assert candidate(damage = [1, 2, 4, 8, 16, 32, 64, 128],armor = 100) == 156
    assert candidate(damage = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],armor = 100000) == 450001
    assert candidate(damage = [100000, 100000, 100000, 100000],armor = 200000) == 300001
    assert candidate(damage = [100000, 50000, 75000, 25000, 10000],armor = 100000) == 160001
    assert candidate(damage = [9, 8, 7, 6, 5, 4, 3, 2, 1],armor = 5) == 41
    assert candidate(damage = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],armor = 1) == 100
    assert candidate(damage = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],armor = 20) == 71
    assert candidate(damage = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],armor = 10) == 101
    assert candidate(damage = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],armor = 75) == 476
    assert candidate(damage = [10, 20, 30, 40, 50],armor = 25) == 126
    assert candidate(damage = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],armor = 1) == 1
    assert candidate(damage = [10, 20, 30, 40, 50],armor = 25) == 126
    assert candidate(damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],armor = 1) == 55
