# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(plants = [5],capacityA = 10,capacityB = 8) == 0
    assert candidate(plants = [1000000, 1000000, 1000000],capacityA = 1000000,capacityB = 1000000) == 1
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacityA = 15,capacityB = 15) == 3
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacityA = 10,capacityB = 10) == 5
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacityA = 1,capacityB = 1) == 8
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacityA = 15,capacityB = 15) == 3
    assert candidate(plants = [2, 2, 3, 3],capacityA = 5,capacityB = 5) == 1
    assert candidate(plants = [1000000],capacityA = 1000000,capacityB = 1000000) == 0
    assert candidate(plants = [2, 2, 3, 3],capacityA = 3,capacityB = 4) == 2
    assert candidate(plants = [1, 10, 1, 10, 1, 10, 1, 10],capacityA = 10,capacityB = 10) == 6
    assert candidate(plants = [5, 8, 6],capacityA = 10,capacityB = 10) == 1
    assert candidate(plants = [10, 10, 10, 10, 10],capacityA = 10,capacityB = 10) == 3
    assert candidate(plants = [1, 2, 3, 4, 5],capacityA = 5,capacityB = 5) == 2
    assert candidate(plants = [10, 8, 6, 4, 2],capacityA = 10,capacityB = 8) == 2
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacityA = 5,capacityB = 5) == 8
    assert candidate(plants = [1, 1, 1, 1, 1],capacityA = 1,capacityB = 1) == 3
    assert candidate(plants = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],capacityA = 150,capacityB = 100) == 4
    assert candidate(plants = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],capacityA = 50,capacityB = 50) == 5
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacityA = 1,capacityB = 1) == 29
    assert candidate(plants = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],capacityA = 30,capacityB = 30) == 8
    assert candidate(plants = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],capacityA = 10,capacityB = 12) == 17
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacityA = 20,capacityB = 20) == 5
    assert candidate(plants = [1000000, 500000, 1000000, 500000, 1000000, 500000, 1000000, 500000, 1000000, 500000],capacityA = 1000000,capacityB = 1000000) == 8
    assert candidate(plants = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],capacityA = 15,capacityB = 15) == 18
    assert candidate(plants = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],capacityA = 20,capacityB = 30) == 9
    assert candidate(plants = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],capacityA = 10,capacityB = 10) == 12
    assert candidate(plants = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capacityA = 55,capacityB = 65) == 8
    assert candidate(plants = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],capacityA = 5,capacityB = 5) == 22
    assert candidate(plants = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],capacityA = 15,capacityB = 20) == 6
    assert candidate(plants = [10, 20, 30, 40, 50, 40, 30, 20, 10],capacityA = 25,capacityB = 25) == 7
    assert candidate(plants = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],capacityA = 1000000,capacityB = 1000000) == 8
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],capacityA = 20,capacityB = 25) == 11
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacityA = 5,capacityB = 5) == 0
    assert candidate(plants = [1000000, 1000000, 1000000, 1000000, 1000000],capacityA = 1000000,capacityB = 1000000) == 3
    assert candidate(plants = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],capacityA = 30,capacityB = 35) == 7
    assert candidate(plants = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],capacityA = 50,capacityB = 60) == 16
    assert candidate(plants = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],capacityA = 100,capacityB = 100) == 11
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacityA = 10,capacityB = 10) == 12
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],capacityA = 10,capacityB = 10) == 16
    assert candidate(plants = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],capacityA = 10,capacityB = 35) == 9
    assert candidate(plants = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacityA = 15,capacityB = 20) == 6
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacityA = 10,capacityB = 5) == 7
    assert candidate(plants = [100, 150, 200, 250, 300, 350, 400, 450, 500],capacityA = 200,capacityB = 300) == 8
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacityA = 1,capacityB = 1) == 28
    assert candidate(plants = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacityA = 10,capacityB = 10) == 16
    assert candidate(plants = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],capacityA = 50,capacityB = 50) == 8
    assert candidate(plants = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],capacityA = 150,capacityB = 150) == 8
    assert candidate(plants = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, 999989, 999988, 999987, 999986, 999985, 999984, 999983, 999982, 999981],capacityA = 2000000,capacityB = 2000000) == 8
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],capacityA = 20,capacityB = 10) == 13
    assert candidate(plants = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],capacityA = 150,capacityB = 120) == 4
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],capacityA = 15,capacityB = 15) == 19
    assert candidate(plants = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],capacityA = 30,capacityB = 60) == 8
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacityA = 2,capacityB = 2) == 8
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],capacityA = 7,capacityB = 8) == 12
    assert candidate(plants = [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250],capacityA = 500,capacityB = 500) == 11
    assert candidate(plants = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],capacityA = 25,capacityB = 25) == 7
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],capacityA = 10,capacityB = 10) == 16
    assert candidate(plants = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],capacityA = 25,capacityB = 30) == 19
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacityA = 5,capacityB = 5) == 28
    assert candidate(plants = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],capacityA = 50,capacityB = 50) == 115
    assert candidate(plants = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61],capacityA = 1000000,capacityB = 500000) == 1
    assert candidate(plants = [1000000, 500000, 1000000, 500000],capacityA = 1000000,capacityB = 1000000) == 2
    assert candidate(plants = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],capacityA = 20,capacityB = 20) == 10
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacityA = 5,capacityB = 10) == 13
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],capacityA = 5,capacityB = 5) == 8
    assert candidate(plants = [3, 2, 4, 1, 2, 4, 3, 1, 2, 3],capacityA = 5,capacityB = 5) == 4
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacityA = 1,capacityB = 1) == 28
    assert candidate(plants = [500, 400, 300, 200, 100, 100, 200, 300, 400, 500],capacityA = 500,capacityB = 500) == 6
    assert candidate(plants = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],capacityA = 15,capacityB = 15) == 7
    assert candidate(plants = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],capacityA = 100,capacityB = 100) == 18
    assert candidate(plants = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953],capacityA = 500000,capacityB = 500000) == 3
    assert candidate(plants = [5, 7, 3, 8, 6, 10, 4, 9, 2, 1],capacityA = 10,capacityB = 12) == 5
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacityA = 2,capacityB = 2) == 8
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacityA = 15,capacityB = 15) == 7
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacityA = 10,capacityB = 9) == 13
    assert candidate(plants = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],capacityA = 500000,capacityB = 500000) == 10
    assert candidate(plants = [100, 200, 150, 50, 300, 250, 350, 400, 450, 500],capacityA = 500,capacityB = 600) == 4
    assert candidate(plants = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],capacityA = 2000000,capacityB = 1500000) == 6
    assert candidate(plants = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],capacityA = 14,capacityB = 16) == 12
    assert candidate(plants = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],capacityA = 25,capacityB = 20) == 10
    assert candidate(plants = [100, 200, 300, 400, 500, 400, 300, 200, 100],capacityA = 300,capacityB = 300) == 5
    assert candidate(plants = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],capacityA = 25,capacityB = 20) == 4
    assert candidate(plants = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],capacityA = 5,capacityB = 5) == 18
    assert candidate(plants = [3, 2, 4, 2, 1, 2, 4, 3, 2, 1, 3, 2, 4, 2, 1],capacityA = 5,capacityB = 5) == 7
    assert candidate(plants = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],capacityA = 500,capacityB = 400) == 8
    assert candidate(plants = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],capacityA = 1000000,capacityB = 1000000) == 8
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],capacityA = 15,capacityB = 15) == 8
    assert candidate(plants = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71],capacityA = 150,capacityB = 150) == 26
    assert candidate(plants = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],capacityA = 10,capacityB = 10) == 7
    assert candidate(plants = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5],capacityA = 10,capacityB = 10) == 9
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],capacityA = 25,capacityB = 25) == 14
    assert candidate(plants = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],capacityA = 5,capacityB = 5) == 13
    assert candidate(plants = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],capacityA = 5,capacityB = 5) == 20
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],capacityA = 10,capacityB = 10) == 11
    assert candidate(plants = [5, 8, 6, 7, 5, 4, 3, 2, 1, 9],capacityA = 10,capacityB = 8) == 7
    assert candidate(plants = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],capacityA = 20,capacityB = 25) == 11
    assert candidate(plants = [9, 8, 7, 6, 5, 4, 3, 2, 1],capacityA = 10,capacityB = 10) == 4
    assert candidate(plants = [10, 5, 15, 20, 25, 30, 35, 40, 45, 50],capacityA = 25,capacityB = 30) == 8
    assert candidate(plants = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacityA = 1,capacityB = 1) == 18
    assert candidate(plants = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacityA = 5,capacityB = 5) == 18
    assert candidate(plants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],capacityA = 12,capacityB = 15) == 20
    assert candidate(plants = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacityA = 15,capacityB = 15) == 8
    assert candidate(plants = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],capacityA = 25,capacityB = 30) == 8
    assert candidate(plants = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],capacityA = 100,capacityB = 100) == 5
