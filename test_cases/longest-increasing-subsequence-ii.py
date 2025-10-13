# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18],k = 10) == 3
    assert candidate(nums = [5, 4, 3, 2, 1],k = 2) == 1
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18],k = 5) == 3
    assert candidate(nums = [7, 4, 5, 1, 8, 12, 4, 7],k = 5) == 4
    assert candidate(nums = [5, 4, 3, 2, 1],k = 1) == 1
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18],k = 2) == 2
    assert candidate(nums = [10, 9, 2, 5, 3, 7, 101, 18],k = 4) == 3
    assert candidate(nums = [9, 7, 5, 3, 1],k = 2) == 1
    assert candidate(nums = [1, 3, 5, 7, 9],k = 2) == 5
    assert candidate(nums = [4, 2, 1, 4, 3, 4, 5, 8, 15],k = 3) == 5
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 5
    assert candidate(nums = [1, 5],k = 1) == 1
    assert candidate(nums = [5, 8, 7, 1, 9, 1, 5, 10, 4, 3, 2, 1],k = 2) == 4
    assert candidate(nums = [3, 1, 2, 4, 6, 5, 9, 7, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20],k = 3) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 4) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 20
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 9) == 2
    assert candidate(nums = [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 10
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 9) == 1
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 11
    assert candidate(nums = [100, 200, 300, 400, 500, 401, 402, 403, 501, 502, 503, 504],k = 10) == 5
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 1) == 2
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 15) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 1) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 10
    assert candidate(nums = [5, 8, 7, 1, 9, 12, 10, 13, 14, 15],k = 4) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 20
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],k = 4) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 10
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 10
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9],k = 2) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 10
    assert candidate(nums = [1, 4, 3, 5, 6, 2, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 4) == 11
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 20
    assert candidate(nums = [9, 1, 4, 7, 3, 2, 5, 8, 6],k = 3) == 4
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 1
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2],k = 1) == 3
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 9) == 1
    assert candidate(nums = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 10
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 3) == 30
    assert candidate(nums = [1, 6, 7, 8, 4, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10, 11, 12],k = 3) == 10
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7, 8],k = 2) == 8
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996],k = 99999) == 6
    assert candidate(nums = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],k = 1) == 3
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 9) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 2) == 15
    assert candidate(nums = [2, 3, 1, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 5) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 14) == 15
    assert candidate(nums = [3, 1, 5, 2, 6, 4, 7],k = 3) == 4
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == 16
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6],k = 3) == 6
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 10) == 1
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],k = 4) == 2
    assert candidate(nums = [3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 10
    assert candidate(nums = [3, 1, 2, 5, 4, 8, 7, 6, 10, 9],k = 3) == 5
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 10) == 1
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 1) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 0) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 1
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],k = 10) == 1
    assert candidate(nums = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985],k = 5) == 1
    assert candidate(nums = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, 92, 83, 74, 65, 56, 47, 38, 29],k = 9) == 12
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 10
    assert candidate(nums = [3, 1, 5, 4, 7, 6, 9, 8, 11, 10],k = 2) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 2) == 20
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 1) == 2
    assert candidate(nums = [3, 10, 2, 1, 20, 15, 25, 28, 30, 100],k = 10) == 6
    assert candidate(nums = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5],k = 10) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 10
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],k = 5) == 1
    assert candidate(nums = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 4) == 1
    assert candidate(nums = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],k = 0) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],k = 2) == 40
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 90) == 10
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 16
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 0) == 1
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93],k = 90) == 9
    assert candidate(nums = [5, 3, 4, 8, 9, 10, 20, 30, 15, 25, 35, 45, 55, 65, 75],k = 20) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 10
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6],k = 2) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 6, 7, 8, 9, 10],k = 3) == 10
    assert candidate(nums = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58],k = 2) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 20
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5],k = 3) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 10
    assert candidate(nums = [4, 3, 5, 4, 7, 6, 8, 9, 10, 11, 12],k = 3) == 8
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == 1
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 100) == 1
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 1
    assert candidate(nums = [4, 3, 2, 1, 100, 101, 102, 103, 104],k = 3) == 5
    assert candidate(nums = [3, 10, 2, 1, 20, 1, 15, 5, 17, 6, 8, 9, 11, 13, 14],k = 4) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5],k = 5) == 20
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],k = 3) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 50) == 15
