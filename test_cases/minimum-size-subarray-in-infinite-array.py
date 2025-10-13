# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50],target = 150) == 5
    assert candidate(nums = [7, 7, 7, 7, 7],target = 28) == 4
    assert candidate(nums = [5, 5, 5, 5, 5],target = 15) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],target = 9) == 2
    assert candidate(nums = [3, 3, 3, 3, 3],target = 9) == 3
    assert candidate(nums = [1, 2, 3],target = 6) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],target = 1) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7],target = 42) == 6
    assert candidate(nums = [5, 5, 5, 5],target = 15) == 3
    assert candidate(nums = [2, 4, 6, 8],target = 3) == -1
    assert candidate(nums = [1, 1, 1, 2, 3],target = 4) == 2
    assert candidate(nums = [1],target = 1) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],target = 15) == 5
    assert candidate(nums = [1, 2, 3, 4, 5],target = 30) == 10
    assert candidate(nums = [1, 3, 5, 7],target = 15) == 3
    assert candidate(nums = [1, 2, 3],target = 5) == 2
    assert candidate(nums = [5, 5, 5, 5],target = 20) == 4
    assert candidate(nums = [100000],target = 100000) == 1
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3],target = 21) == 10
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],target = 100) == 11
    assert candidate(nums = [7, 14, 28, 56, 112],target = 224) == 6
    assert candidate(nums = [10, 20, 30, 40, 50],target = 300) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 100) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 90) == 12
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],target = 90) == 10
    assert candidate(nums = [7, 11, 15, 19],target = 100) == -1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 55) == 10
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 110) == 10
    assert candidate(nums = [10, 20, 30, 40, 50],target = 100) == 3
    assert candidate(nums = [5, 5, 5, 5, 5],target = 25) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 100) == 100
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3],target = 27) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 100) == 100
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 550) == 10
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],target = 45) == 9
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 315) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17],target = 100) == -1
    assert candidate(nums = [7, 8, 9],target = 40) == 5
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],target = 10000) == 697
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 450) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1000) == 181
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],target = 39) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
    assert candidate(nums = [5, 10, 15, 20, 25, 30],target = 100) == 5
    assert candidate(nums = [1, 10, 100, 1000, 10000],target = 11111) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 50) == 50
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 50) == 10
    assert candidate(nums = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67],target = 300) == 6
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],target = 119) == 17
    assert candidate(nums = [1, 2, 4, 8, 16, 32],target = 127) == 13
    assert candidate(nums = [5, 5, 5, 5, 5],target = 75) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 50) == 50
    assert candidate(nums = [9, 7, 5, 3, 1],target = 20) == 4
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 27) == 9
    assert candidate(nums = [123456, 654321, 123456, 654321],target = 4508736) == -1
    assert candidate(nums = [2, 3, 6, 7, 9],target = 19) == -1
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],target = 90) == 4
    assert candidate(nums = [3, 3, 3],target = 27) == 9
    assert candidate(nums = [5, 5, 5, 5, 5],target = 125) == 25
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 10
    assert candidate(nums = [5, 7, 9, 11, 13],target = 100) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 120) == 15
    assert candidate(nums = [7, 14, 21, 28, 35],target = 98) == 4
    assert candidate(nums = [100000, 100000, 100000],target = 300000) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],target = 225) == 45
    assert candidate(nums = [100000],target = 500000) == 5
    assert candidate(nums = [10, 5, 15, 20, 25],target = 150) == 10
    assert candidate(nums = [23, 45, 67, 89, 12, 34, 56, 78],target = 500) == -1
    assert candidate(nums = [100000],target = 1000000000) == 10000
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 90) == 30
    assert candidate(nums = [5, 2, 7, 3, 9],target = 31) == 6
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 30) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 45) == 14
    assert candidate(nums = [10, 20, 30],target = 100) == 5
    assert candidate(nums = [10, 20, 30, 40, 50],target = 120) == 3
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17],target = 101) == 11
    assert candidate(nums = [123456, 654321, 135792, 246801, 357912, 468012, 579123],target = 10000000) == -1
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 27) == 9
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 30) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6],target = 15) == 3
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],target = 120) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 210) == 20
    assert candidate(nums = [1, 10, 100, 1000, 10000],target = 11111) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 100000) == 1816
    assert candidate(nums = [7, 8, 9],target = 60) == -1
    assert candidate(nums = [17, 19, 23, 29, 31],target = 150) == 6
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],target = 1000) == -1
    assert candidate(nums = [5, 2, 3, 1, 1, 1, 1, 1, 1, 1],target = 18) == 11
    assert candidate(nums = [100, 200, 300],target = 1000) == 5
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 40) == 20
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 2500) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 120) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 55) == 10
    assert candidate(nums = [7, 1, 5, 3],target = 31) == 7
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],target = 180) == 20
    assert candidate(nums = [9, 7, 5, 3, 1],target = 30) == 6
    assert candidate(nums = [5, 2, 7],target = 22) == -1
    assert candidate(nums = [100, 200, 300, 400, 500],target = 2500) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 550) == 10
    assert candidate(nums = [7, 14, 21, 28, 35],target = 105) == 5
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16],target = 100) == 12
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000],target = 1500000) == 5
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 90) == 30
    assert candidate(nums = [100000, 100000, 100000, 100000],target = 400000) == 4
    assert candidate(nums = [10, 20, 30, 40, 50],target = 120) == 3
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 25) == 5
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],target = 9000) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 275) == 50
    assert candidate(nums = [1],target = 100000) == 100000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 55) == 10
    assert candidate(nums = [1, 2, 3],target = 30) == 15
    assert candidate(nums = [123, 456, 789],target = 1518) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 210) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1000) == 181
    assert candidate(nums = [1],target = 1000000) == 1000000
