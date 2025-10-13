# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [7, 8, 9, 10, 5, 6],k = 3,dist = 4) == 18
    assert candidate(nums = [5, 4, 3, 2, 1],k = 2,dist = 2) == 6
    assert candidate(nums = [1, 3, 2, 6, 4, 2],k = 3,dist = 3) == 5
    assert candidate(nums = [10, 8, 18, 9],k = 3,dist = 1) == 36
    assert candidate(nums = [5, 1, 4, 3, 2],k = 3,dist = 2) == 9
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4,dist = 4) == 15
    assert candidate(nums = [7, 8, 9, 10, 11, 12],k = 3,dist = 4) == 24
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5,dist = 4) == 15
    assert candidate(nums = [10, 1, 2, 2, 2, 1],k = 4,dist = 3) == 15
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0],k = 15,dist = 20) == 45
    assert candidate(nums = [5, 1, 4, 2, 8, 7, 3, 6, 9, 10],k = 4,dist = 5) == 11
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5,dist = 4) == 50
    assert candidate(nums = [100, 200, 10, 20, 30, 40, 50, 5, 15, 25, 35, 45],k = 5,dist = 6) == 150
    assert candidate(nums = [100, 101, 102, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88],k = 7,dist = 9) == 643
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,dist = 4) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,dist = 5) == 5
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 3,dist = 5) == 6
    assert candidate(nums = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5],k = 3,dist = 9) == 103
    assert candidate(nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 8,dist = 8) == 36
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],k = 10,dist = 10) == 855
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 1, 2, 3, 4, 5],k = 6,dist = 9) == 1000000015
    assert candidate(nums = [31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 7,dist = 6) == 259
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10,dist = 10) == 65
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15,dist = 15) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8,dist = 6) == 36
    assert candidate(nums = [5, 1, 9, 3, 7, 2, 8, 6, 4, 10, 11, 12],k = 5,dist = 6) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7,dist = 7) == 28
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10,dist = 10) == 65
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8,dist = 6) == 360
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5,dist = 3) == 19
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100],k = 10,dist = 15) == 145
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1, 9, 10],k = 4,dist = 5) == 12
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],k = 4,dist = 3) == 100
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10,dist = 15) == 550
    assert candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 11, 12, 13, 14, 15],k = 7,dist = 8) == 28
    assert candidate(nums = [1, 3, 2, 6, 4, 2, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 6,dist = 5) == 17
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 10,dist = 12) == 550
    assert candidate(nums = [5, 3, 8, 1, 4, 9, 2, 6, 7],k = 4,dist = 5) == 11
    assert candidate(nums = [1, 1000000000, 2, 1000000000, 3, 1000000000, 4, 1000000000, 5],k = 5,dist = 4) == 1000000010
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 6,dist = 7) == 36
    assert candidate(nums = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5],k = 6,dist = 9) == 115
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,dist = 10) == 55
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7,dist = 10) == 280
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 5,dist = 5) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,dist = 10) == 55
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 6,dist = 7) == 2100
    assert candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10],k = 5,dist = 4) == 17
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,dist = 10) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8,dist = 7) == 36
    assert candidate(nums = [1, 3, 5, 2, 8, 7, 4, 6, 9, 10],k = 4,dist = 5) == 10
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,dist = 10) == 1000000045
    assert candidate(nums = [100, 200, 150, 10, 50, 300, 400, 250, 350, 100, 500],k = 6,dist = 8) == 610
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16],k = 8,dist = 7) == 38
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,dist = 10) == 10
    assert candidate(nums = [1000000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,dist = 10) == 1000000045
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15,dist = 15) == 15
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],k = 5,dist = 10) == 15
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5,dist = 5) == 25
    assert candidate(nums = [100, 200, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 6,dist = 6) == 250
    assert candidate(nums = [15, 3, 8, 7, 5, 2, 9, 1, 10, 4, 6, 11, 13, 12],k = 5,dist = 5) == 27
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 20,dist = 20) == 100
    assert candidate(nums = [3, 1, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],k = 7,dist = 6) == 13
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],k = 10,dist = 10) == 35
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 6,dist = 5) == 24
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5],k = 5,dist = 7) == 15
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 8,dist = 10) == 72
    assert candidate(nums = [100, 99, 98, 97, 96, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 7,dist = 7) == 121
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10,dist = 9) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5,dist = 5) == 11
    assert candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 10, 11, 12, 13, 14, 15],k = 7,dist = 8) == 28
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],k = 6,dist = 7) == 105
    assert candidate(nums = [3, 1, 2, 1, 3, 2, 1, 3, 2, 1],k = 4,dist = 4) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10,dist = 10) == 550
    assert candidate(nums = [100, 1, 50, 2, 99, 3, 49, 4, 98, 5],k = 5,dist = 5) == 155
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5,dist = 3) == 19
    assert candidate(nums = [5, 1, 3, 8, 12, 7, 9, 2, 6, 4],k = 4,dist = 5) == 16
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],k = 5,dist = 5) == 7
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10,dist = 10) == 70
    assert candidate(nums = [9, 3, 7, 2, 8, 6, 5, 1, 4, 10],k = 4,dist = 5) == 16
    assert candidate(nums = [10, 20, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 6,dist = 5) == 25
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 7,dist = 10) == 49
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 10,dist = 15) == 55
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5,dist = 5) == 15
    assert candidate(nums = [15, 20, 25, 10, 30, 35, 5, 40, 45, 4, 50],k = 6,dist = 7) == 89
    assert candidate(nums = [200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 10,dist = 10) == 650
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,dist = 20) == 34
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15,dist = 15) == 135
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5,dist = 15) == 16
    assert candidate(nums = [5, 8, 3, 9, 2, 7, 4, 6, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7,dist = 15) == 21
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 6,dist = 7) == 210
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3],k = 7,dist = 10) == 19
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 5,dist = 3) == 200
    assert candidate(nums = [9, 3, 1, 5, 2, 8, 6, 7, 4, 10],k = 5,dist = 5) == 20
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 5,dist = 12) == 30
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15,dist = 25) == 76
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5,dist = 5) == 25
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 6,dist = 8) == 30
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 8, 7, 9, 10],k = 4,dist = 6) == 11
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,dist = 8) == 101
    assert candidate(nums = [5, 3, 8, 12, 4, 6, 7, 10, 2, 9],k = 4,dist = 6) == 17
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 9,dist = 10) == 25
    assert candidate(nums = [200, 100, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],k = 5,dist = 10) == 1500
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5,dist = 4) == 15
    assert candidate(nums = [1000000000, 1, 1000000000, 1, 1000000000],k = 3,dist = 3) == 1000000002
    assert candidate(nums = [5, 1, 4, 2, 8, 7, 3],k = 4,dist = 5) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 6,dist = 7) == 21
    assert candidate(nums = [7, 8, 9, 10, 5, 6, 2, 3, 4, 1],k = 5,dist = 5) == 17
    assert candidate(nums = [5, 4, 3, 2, 1],k = 3,dist = 4) == 8
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3,dist = 5) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5,dist = 5) == 15
    assert candidate(nums = [5, 3, 8, 1, 4, 7, 9, 2],k = 4,dist = 4) == 12
    assert candidate(nums = [5, 1, 3, 7, 9, 2, 6, 8, 4],k = 4,dist = 5) == 11
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4,dist = 2) == 20
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5,dist = 5) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,dist = 7) == 6
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 7, 8, 9],k = 4,dist = 5) == 11
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3,dist = 2) == 15
    assert candidate(nums = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10],k = 4,dist = 5) == 10
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 6,dist = 5) == 16
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3,dist = 4) == 12
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3,dist = 6) == 12
    assert candidate(nums = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5],k = 4,dist = 5) == 56
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5,dist = 5) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 6,dist = 10) == 21
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3,dist = 7) == 3
    assert candidate(nums = [5, 2, 3, 1, 4, 6, 7, 8, 9],k = 5,dist = 4) == 15
    assert candidate(nums = [100, 200, 300, 400, 500],k = 3,dist = 2) == 600
    assert candidate(nums = [7, 3, 5, 10, 6, 9],k = 4,dist = 5) == 21
    assert candidate(nums = [9, 7, 5, 3, 1],k = 4,dist = 3) == 18
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5,dist = 5) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 6,dist = 7) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,dist = 5) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3,dist = 2) == 3
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 5,dist = 5) == 11
    assert candidate(nums = [7, 9, 3, 1, 5, 6, 2],k = 5,dist = 5) == 18
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9],k = 3,dist = 4) == 8
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5,dist = 4) == 19
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5,dist = 5) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4,dist = 6) == 100
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000],k = 3,dist = 4) == 111
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 6,dist = 5) == 2100
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1],k = 3,dist = 2) == 3
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1],k = 3,dist = 4) == 10
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3,dist = 5) == 9
    assert candidate(nums = [5, 1, 4, 3, 2],k = 3,dist = 2) == 9
    assert candidate(nums = [10, 8, 18, 9],k = 3,dist = 1) == 36
    assert candidate(nums = [7, 8, 9, 10, 2, 1, 3, 4, 5, 6],k = 4,dist = 4) == 13
    assert candidate(nums = [5, 1, 4, 2, 8, 3, 7, 6],k = 4,dist = 4) == 11
    assert candidate(nums = [5, 1, 4, 3, 2, 6, 7],k = 3,dist = 4) == 8
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3,dist = 7) == 9
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5,dist = 6) == 1500
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 4,dist = 7) == 1000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5,dist = 6) == 15
    assert candidate(nums = [7, 8, 9, 10, 2, 1, 3, 4, 5, 6],k = 4,dist = 5) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5,dist = 10) == 15
    assert candidate(nums = [1, 3, 2, 6, 4, 2],k = 3,dist = 3) == 5
    assert candidate(nums = [3, 1, 5, 2, 4, 6, 8, 7],k = 3,dist = 4) == 6
    assert candidate(nums = [7, 8, 9, 10, 11, 12],k = 4,dist = 5) == 34
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5,dist = 10) == 5
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3,dist = 4) == 9
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 5,dist = 5) == 107
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7],k = 5,dist = 5) == 15
    assert candidate(nums = [7, 1, 5, 3, 6, 4, 8, 2],k = 5,dist = 5) == 20
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],k = 5,dist = 5) == 19
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5,dist = 4) == 25
    assert candidate(nums = [5, 4, 3, 2, 1],k = 3,dist = 2) == 8
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3,dist = 7) == 600
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4,dist = 6) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 4,dist = 4) == 1000
    assert candidate(nums = [5, 1, 3, 8, 6, 7, 4, 2],k = 4,dist = 4) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5,dist = 6) == 150
    assert candidate(nums = [7, 8, 9, 1, 2, 3, 4, 5, 6],k = 5,dist = 5) == 17
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3,dist = 8) == 600
    assert candidate(nums = [7, 8, 9, 10, 2, 1],k = 4,dist = 4) == 18
    assert candidate(nums = [1000000000, 1000000000, 1000000000],k = 3,dist = 2) == 3000000000
    assert candidate(nums = [5, 1, 4, 2, 3],k = 3,dist = 4) == 8
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 4,dist = 4) == 9
    assert candidate(nums = [5, 1, 3, 7, 9, 2, 6, 4, 8],k = 4,dist = 5) == 11
    assert candidate(nums = [9, 3, 7, 6, 2, 5, 8, 4],k = 5,dist = 4) == 25
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4,dist = 4) == 10
    assert candidate(nums = [5, 1, 3, 7, 9, 2, 6, 8, 4, 10],k = 5,dist = 4) == 18
    assert candidate(nums = [10, 1, 2, 2, 2, 1],k = 4,dist = 3) == 15
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5,dist = 5) == 25
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10],k = 4,dist = 5) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4,dist = 5) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600],k = 3,dist = 2) == 600
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63],k = 4,dist = 6) == 70
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4,dist = 5) == 15
    assert candidate(nums = [5, 1, 4, 2, 3],k = 3,dist = 4) == 8
    assert candidate(nums = [5, 1, 4, 2, 8, 3],k = 4,dist = 4) == 11
    assert candidate(nums = [5, 1, 4, 2, 8, 3],k = 3,dist = 4) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 3,dist = 6) == 6
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7],k = 7,dist = 6) == 19
