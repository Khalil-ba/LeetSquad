# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(blocks = [10, 20, 30],split = 10) == 40
    assert candidate(blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],split = 1) == 5
    assert candidate(blocks = [1, 2],split = 5) == 7
    assert candidate(blocks = [1, 2, 3],split = 1) == 4
    assert candidate(blocks = [4, 2, 3, 1],split = 2) == 8
    assert candidate(blocks = [5, 5, 5, 5],split = 2) == 9
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],split = 1) == 11
    assert candidate(blocks = [4, 5, 6, 7],split = 10) == 27
    assert candidate(blocks = [1, 2, 3],split = 1) == 4
    assert candidate(blocks = [1],split = 1) == 1
    assert candidate(blocks = [100000],split = 100000) == 100000
    assert candidate(blocks = [10, 20, 30, 40],split = 10) == 50
    assert candidate(blocks = [10, 20, 30, 40],split = 5) == 45
    assert candidate(blocks = [10, 20, 30],split = 5) == 35
    assert candidate(blocks = [4, 2, 3, 1],split = 2) == 8
    assert candidate(blocks = [1, 2],split = 5) == 7
    assert candidate(blocks = [10, 20, 30, 40, 50],split = 5) == 55
    assert candidate(blocks = [5, 5, 5, 5, 5],split = 2) == 11
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],split = 10) == 110
    assert candidate(blocks = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],split = 100) == 100393
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],split = 10) == 53
    assert candidate(blocks = [5, 8, 12, 15, 3],split = 7) == 29
    assert candidate(blocks = [100, 200, 300, 400, 500],split = 200) == 900
    assert candidate(blocks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],split = 3) == 21
    assert candidate(blocks = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],split = 5000) == 30000
    assert candidate(blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],split = 10) == 41
    assert candidate(blocks = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],split = 1) == 513
    assert candidate(blocks = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],split = 1000) == 14000
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],split = 2) == 19
    assert candidate(blocks = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],split = 1000) == 101000
    assert candidate(blocks = [50, 25, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300],split = 50) == 400
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],split = 25) == 165
    assert candidate(blocks = [5, 9, 1, 12, 7],split = 3) == 17
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],split = 20) == 140
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],split = 5) == 47
    assert candidate(blocks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],split = 1) == 14
    assert candidate(blocks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],split = 100) == 1100
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],split = 20) == 240
    assert candidate(blocks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],split = 10) == 42
    assert candidate(blocks = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],split = 10) == 74
    assert candidate(blocks = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],split = 10000) == 110000
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],split = 15) == 180
    assert candidate(blocks = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],split = 20) == 150
    assert candidate(blocks = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],split = 10000) == 139993
    assert candidate(blocks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],split = 10) == 45
    assert candidate(blocks = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],split = 50) == 250
    assert candidate(blocks = [10000, 20000, 30000],split = 5000) == 35000
    assert candidate(blocks = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],split = 20) == 135
    assert candidate(blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],split = 2) == 9
    assert candidate(blocks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],split = 10) == 120
    assert candidate(blocks = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],split = 10) == 159
    assert candidate(blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],split = 1) == 8
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],split = 20) == 190
    assert candidate(blocks = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000],split = 1000) == 103000
    assert candidate(blocks = [50, 40, 30, 20, 10],split = 15) == 80
    assert candidate(blocks = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],split = 50) == 1050
    assert candidate(blocks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],split = 3) == 21
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],split = 3) == 18
    assert candidate(blocks = [50000, 40000, 30000, 20000, 10000, 5000, 4000, 3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 1],split = 1000) == 51000
    assert candidate(blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],split = 10) == 51
    assert candidate(blocks = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1],split = 1) == 100003
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],split = 5) == 105
    assert candidate(blocks = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],split = 3) == 22
    assert candidate(blocks = [3, 5, 1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],split = 2) == 24
    assert candidate(blocks = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1],split = 50) == 1050
    assert candidate(blocks = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],split = 5) == 29
    assert candidate(blocks = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],split = 3) == 53
    assert candidate(blocks = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111],split = 10000) == 109999
    assert candidate(blocks = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],split = 25000) == 150000
    assert candidate(blocks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],split = 150) == 2300
    assert candidate(blocks = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000],split = 300) == 3600
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],split = 15) == 130
    assert candidate(blocks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],split = 2) == 13
    assert candidate(blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],split = 1) == 5
    assert candidate(blocks = [5, 8, 12, 3, 9, 7],split = 4) == 20
    assert candidate(blocks = [5, 8, 3, 6, 2, 7],split = 3) == 15
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],split = 3) == 23
    assert candidate(blocks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],split = 50) == 1050
    assert candidate(blocks = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000],split = 1000) == 11000
    assert candidate(blocks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],split = 5) == 30
    assert candidate(blocks = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],split = 1500) == 13000
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],split = 1) == 16
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],split = 5) == 205
    assert candidate(blocks = [1, 1000, 10000, 100000, 50, 500, 5000, 50000, 10, 100],split = 100) == 100100
    assert candidate(blocks = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],split = 5000) == 30000
    assert candidate(blocks = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],split = 1) == 100000
    assert candidate(blocks = [300, 200, 100, 250, 150, 50, 400, 350, 10, 500],split = 5) == 505
    assert candidate(blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],split = 1) == 6
    assert candidate(blocks = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],split = 50) == 300
    assert candidate(blocks = [100, 200, 300, 400, 500],split = 150) == 800
    assert candidate(blocks = [10, 20, 30, 40, 50, 60],split = 15) == 90
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],split = 10) == 60
    assert candidate(blocks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],split = 20) == 119
    assert candidate(blocks = [8, 7, 6, 5, 4, 3, 2, 1],split = 1) == 9
    assert candidate(blocks = [5, 8, 12, 3, 9],split = 4) == 20
    assert candidate(blocks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],split = 10) == 210
    assert candidate(blocks = [90, 45, 60, 75, 30, 15, 0, 105, 120, 135],split = 15) == 150
    assert candidate(blocks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],split = 2) == 15
    assert candidate(blocks = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],split = 50) == 1550
    assert candidate(blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],split = 2) == 34
