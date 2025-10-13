# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(stations = [1, 2, 4, 5, 0],r = 1,k = 2) == 5
    assert candidate(stations = [0, 0, 0, 0, 0],r = 2,k = 5) == 5
    assert candidate(stations = [0, 0, 0, 0, 0],r = 2,k = 10) == 10
    assert candidate(stations = [1, 3, 5, 7, 9],r = 2,k = 5) == 14
    assert candidate(stations = [3, 3, 3, 3, 3],r = 1,k = 5) == 8
    assert candidate(stations = [10, 20, 30, 40, 50],r = 3,k = 20) == 120
    assert candidate(stations = [1, 0, 1, 0, 1, 0, 1],r = 2,k = 3) == 3
    assert candidate(stations = [0, 0, 0, 0],r = 2,k = 5) == 5
    assert candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 2) == 3
    assert candidate(stations = [0, 0, 0, 0],r = 2,k = 10) == 10
    assert candidate(stations = [10, 20, 30, 40, 50],r = 3,k = 100) == 200
    assert candidate(stations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],r = 3,k = 15) == 27
    assert candidate(stations = [5, 5, 5, 5, 5],r = 2,k = 5) == 20
    assert candidate(stations = [10, 20, 30, 40, 50],r = 2,k = 10) == 70
    assert candidate(stations = [1, 0, 3, 0, 2],r = 2,k = 3) == 7
    assert candidate(stations = [4, 4, 4, 4],r = 0,k = 3) == 4
    assert candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 3,k = 15) == 27
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 5,k = 150) == 360
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],r = 5,k = 300) == 480
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 10) == 5
    assert candidate(stations = [8, 9, 8, 9, 8, 9, 8, 9, 8, 9],r = 1,k = 10) == 22
    assert candidate(stations = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],r = 5,k = 100) == 68
    assert candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 4) == 2
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 20) == 20
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 0,k = 5) == 1
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 25) == 12
    assert candidate(stations = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],r = 1,k = 50) == 37
    assert candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],r = 5,k = 300) == 405
    assert candidate(stations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],r = 5,k = 30) == 45
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 0,k = 50) == 36
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 20) == 10
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 1,k = 500) == 262
    assert candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 1,k = 50) == 25
    assert candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 5,k = 5000) == 7100
    assert candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],r = 3,k = 150) == 185
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 4,k = 50) == 52
    assert candidate(stations = [1, 3, 0, 2, 5, 4, 2, 1, 0, 5],r = 2,k = 10) == 10
    assert candidate(stations = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],r = 2,k = 50000) == 41500
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 1,k = 45) == 25
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 10,k = 50) == 61
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 5,k = 10) == 11
    assert candidate(stations = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0],r = 3,k = 50) == 35
    assert candidate(stations = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],r = 5,k = 1000000) == 1600000
    assert candidate(stations = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],r = 4,k = 30) == 60
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],r = 3,k = 50) == 40
    assert candidate(stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 4,k = 100) == 60
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 2,k = 10) == 5
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 10) == 15
    assert candidate(stations = [1, 0, 0, 0, 0, 1],r = 2,k = 3) == 2
    assert candidate(stations = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0],r = 2,k = 10) == 12
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],r = 2,k = 100) == 145
    assert candidate(stations = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],r = 1,k = 5) == 2
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 10,k = 500) == 566
    assert candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 3,k = 150) == 250
    assert candidate(stations = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],r = 6,k = 10) == 6
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],r = 4,k = 1000) == 900
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 4,k = 250) == 400
    assert candidate(stations = [50, 40, 30, 20, 10],r = 1,k = 50) == 80
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 5,k = 150) == 138
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 3,k = 100) == 80
    assert candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 2,k = 60) == 120
    assert candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 4,k = 500) == 2000
    assert candidate(stations = [100000, 0, 100000, 0, 100000, 0, 100000],r = 3,k = 500000) == 700000
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 4,k = 30) == 37
    assert candidate(stations = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],r = 5,k = 5000) == 11000
    assert candidate(stations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],r = 2,k = 50) == 39
    assert candidate(stations = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0],r = 1,k = 10) == 13
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],r = 4,k = 250) == 400
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 0,k = 45) == 10
    assert candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 10) == 3
    assert candidate(stations = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],r = 2,k = 25) == 18
    assert candidate(stations = [100, 0, 100, 0, 100],r = 2,k = 50) == 250
    assert candidate(stations = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],r = 1,k = 100) == 125
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 4,k = 10) == 10
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 2,k = 20) == 26
    assert candidate(stations = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],r = 5,k = 100) == 350
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 7,k = 100) == 134
    assert candidate(stations = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],r = 3,k = 100) == 160
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],r = 1,k = 100) == 40
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 1,k = 10) == 12
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 2,k = 30) == 28
    assert candidate(stations = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],r = 3,k = 5) == 3
    assert candidate(stations = [5, 15, 25, 35, 45, 55],r = 1,k = 100) == 110
    assert candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 3) == 4
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 8,k = 20) == 19
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 1,k = 10) == 2
    assert candidate(stations = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],r = 4,k = 20000) == 35000
    assert candidate(stations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],r = 1,k = 5) == 8
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 4,k = 50) == 25
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],r = 3,k = 30) == 33
    assert candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],r = 3,k = 150) == 125
    assert candidate(stations = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],r = 2,k = 20) == 26
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 4,k = 20) == 35
    assert candidate(stations = [0, 0, 0, 0, 0, 0],r = 1,k = 10) == 5
    assert candidate(stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],r = 5,k = 200) == 305
    assert candidate(stations = [1, 0, 0, 0, 1],r = 2,k = 2) == 3
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 2,k = 20) == 10
    assert candidate(stations = [9, 7, 5, 3, 1, 0, 2, 4, 6, 8],r = 4,k = 25) == 35
    assert candidate(stations = [1, 3, 2, 5, 7, 8, 6, 4, 9, 0],r = 2,k = 10) == 14
    assert candidate(stations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],r = 5,k = 20) == 20
    assert candidate(stations = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],r = 1,k = 5) == 2
    assert candidate(stations = [10, 20, 30, 40, 50, 40, 30, 20, 10],r = 2,k = 50) == 85
    assert candidate(stations = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],r = 5,k = 20) == 43
    assert candidate(stations = [100, 0, 100, 0, 100, 0, 100],r = 2,k = 200) == 300
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],r = 5,k = 25) == 46
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],r = 3,k = 100) == 73
    assert candidate(stations = [100, 0, 100, 0, 100, 0, 100, 0, 100, 0],r = 4,k = 100) == 300
    assert candidate(stations = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],r = 3,k = 100) == 190
    assert candidate(stations = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],r = 0,k = 500) == 100
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 50) == 35
    assert candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 4,k = 500) == 2000
    assert candidate(stations = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],r = 5,k = 2000) == 4100
    assert candidate(stations = [1, 3, 2, 5, 4, 6, 7, 8, 9, 0],r = 2,k = 20) == 21
    assert candidate(stations = [0, 0, 0, 0, 0],r = 1,k = 5) == 2
    assert candidate(stations = [9, 8, 7, 6, 5, 4, 3, 2, 1],r = 3,k = 25) == 32
    assert candidate(stations = [1, 3, 2, 1, 4, 1, 2, 3],r = 2,k = 5) == 8
    assert candidate(stations = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],r = 9,k = 20) == 20
    assert candidate(stations = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000],r = 1,k = 10000) == 3751
