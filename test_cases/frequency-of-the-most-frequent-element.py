# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 2, 4],k = 5) == 3
    assert candidate(nums = [100000, 100000, 100000],k = 300000) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 25) == 7
    assert candidate(nums = [1, 1, 1, 1],k = 0) == 4
    assert candidate(nums = [5, 5, 5, 5, 5],k = 10) == 5
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4],k = 7) == 6
    assert candidate(nums = [1, 1, 1, 1, 1],k = 10) == 5
    assert candidate(nums = [3, 9, 6],k = 2) == 1
    assert candidate(nums = [1, 1, 1, 1, 1],k = 5) == 5
    assert candidate(nums = [1, 1, 1],k = 0) == 3
    assert candidate(nums = [1, 100000],k = 100000) == 2
    assert candidate(nums = [1, 2, 2, 4],k = 6) == 3
    assert candidate(nums = [1, 4, 8, 13],k = 5) == 2
    assert candidate(nums = [1, 100000],k = 99999) == 2
    assert candidate(nums = [5, 5, 5, 5, 5],k = 0) == 5
    assert candidate(nums = [100000, 100000, 100000],k = 100000) == 3
    assert candidate(nums = [5, 9, 11, 13, 15],k = 10) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],k = 10) == 5
    assert candidate(nums = [1, 2, 2, 3, 3, 3],k = 6) == 6
    assert candidate(nums = [1, 2, 2, 4],k = 3) == 3
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 10) == 10
    assert candidate(nums = [1, 1, 1, 1],k = 10) == 4
    assert candidate(nums = [1, 2, 3, 4, 5],k = 15) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],k = 50) == 20
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 200) == 9
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 150) == 8
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 50) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 45) == 10
    assert candidate(nums = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],k = 150) == 21
    assert candidate(nums = [5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9],k = 50) == 15
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 15) == 10
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],k = 75) == 20
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],k = 40) == 19
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 1000) == 14
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 55) == 7
    assert candidate(nums = [1, 3, 6, 10, 15],k = 25) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 6
    assert candidate(nums = [5, 7, 7, 8, 8, 10, 10, 10, 10],k = 30) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 50) == 10
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 100) == 20
    assert candidate(nums = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],k = 500000) == 10
    assert candidate(nums = [5, 7, 7, 8, 8, 10, 10, 10, 12, 12, 12, 12],k = 30) == 11
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 10) == 7
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],k = 100) == 20
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000],k = 199999) == 19
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000],k = 500000) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 150) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 50) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5],k = 10) == 10
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9],k = 30) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 60) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 20
    assert candidate(nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1000) == 10
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],k = 60) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 100) == 10
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],k = 30) == 17
    assert candidate(nums = [10, 20, 30, 40, 50],k = 100) == 5
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000],k = 100000) == 5
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 0) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == 10
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 50) == 10
    assert candidate(nums = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50],k = 100) == 7
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],k = 200) == 14
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 50) == 18
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 100) == 20
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 1500) == 17
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4],k = 50) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 200) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 100) == 10
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101],k = 500) == 16
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 200) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 15
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 20) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3000) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1000) == 20
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 100) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 50) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 100) == 10
    assert candidate(nums = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 100) == 40
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 300) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 14
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 150) == 17
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50],k = 100) == 6
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],k = 100) == 21
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],k = 200) == 30
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4],k = 20) == 14
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 50000) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20],k = 200) == 29
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 15) == 13
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 250) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 100) == 14
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 500) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100) == 14
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000],k = 500000) == 5
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],k = 50) == 20
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 12
