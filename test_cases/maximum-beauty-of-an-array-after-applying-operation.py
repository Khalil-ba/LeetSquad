# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],k = 3) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 3
    assert candidate(nums = [10, 20, 30, 40, 50],k = 15) == 4
    assert candidate(nums = [5, 15, 25, 35],k = 5) == 2
    assert candidate(nums = [100, 100, 100],k = 5) == 3
    assert candidate(nums = [100, 200, 300, 400, 500],k = 0) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 10
    assert candidate(nums = [3, 3, 3, 3, 3],k = 1) == 5
    assert candidate(nums = [1, 2, 3, 4, 5],k = 2) == 5
    assert candidate(nums = [100000, 0, 50000, 25000, 75000],k = 50000) == 5
    assert candidate(nums = [10, 20, 30, 40, 50],k = 5) == 2
    assert candidate(nums = [8, 8, 8, 8, 8, 8],k = 0) == 6
    assert candidate(nums = [1, 3, 5, 7, 9],k = 1) == 2
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 2) == 9
    assert candidate(nums = [5, 3, 9, 8, 7],k = 1) == 3
    assert candidate(nums = [2, 4, 6, 8, 10],k = 2) == 3
    assert candidate(nums = [3, 3, 3, 3, 3],k = 5) == 5
    assert candidate(nums = [4, 6, 1, 2],k = 2) == 3
    assert candidate(nums = [10, 20, 30, 40, 50],k = 0) == 1
    assert candidate(nums = [5, 5, 5, 5, 5],k = 0) == 5
    assert candidate(nums = [1, 2, 3, 4, 5],k = 0) == 1
    assert candidate(nums = [1, 100000],k = 50000) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 9
    assert candidate(nums = [5, 3, 15, 8, 10],k = 5) == 4
    assert candidate(nums = [100000, 100000, 100000],k = 0) == 3
    assert candidate(nums = [5, 3, 15, 8, 1],k = 3) == 3
    assert candidate(nums = [1, 1, 1, 1],k = 10) == 4
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 100) == 3
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 50) == 10
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 5) == 10
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6],k = 1) == 18
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3) == 4
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 1) == 12
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 0) == 5
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57],k = 4) == 3
    assert candidate(nums = [2, 5, 9, 14, 20, 27, 35, 44, 54, 65],k = 10) == 5
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],k = 1) == 9
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],k = 1) == 9
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],k = 4) == 3
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 3
    assert candidate(nums = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996],k = 50000) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 1) == 6
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],k = 50) == 11
    assert candidate(nums = [100, 100, 200, 200, 300, 300, 400, 400],k = 50) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 4
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],k = 10000) == 10
    assert candidate(nums = [10, 20, 20, 30, 30, 30, 40, 40, 40, 40],k = 10) == 9
    assert candidate(nums = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 3) == 4
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 13, 14, 15],k = 3) == 10
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 10) == 3
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 20) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 3
    assert candidate(nums = [5, 8, 12, 15, 17, 20, 23, 25, 28, 30],k = 5) == 5
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4],k = 1) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 7
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11],k = 2) == 5
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50],k = 5) == 3
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981],k = 50000) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 3
    assert candidate(nums = [5, 8, 11, 14, 17, 20, 23, 26, 29, 32],k = 5) == 4
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 20
    assert candidate(nums = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10],k = 1) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 15
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 32
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 11
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 150) == 4
    assert candidate(nums = [5, 8, 8, 10, 12, 15, 15, 20, 22, 25],k = 3) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 20
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 2
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],k = 50) == 11
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == 19
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500],k = 50) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == 19
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 1) == 6
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700],k = 100) == 3
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],k = 3) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10000) == 15
    assert candidate(nums = [100000, 1, 2, 3, 100000, 100000, 4, 5, 6, 7, 8, 9],k = 100000) == 12
    assert candidate(nums = [90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],k = 25000) == 6
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40],k = 7) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 3
    assert candidate(nums = [2, 4, 4, 4, 6, 8, 8, 8, 10, 12, 12, 14, 16, 18],k = 2) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 11
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 15) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 5
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 45) == 10
    assert candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],k = 10) == 3
    assert candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 10) == 5
    assert candidate(nums = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190],k = 15) == 4
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000],k = 15000) == 4
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],k = 5) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 1) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 0) == 2
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],k = 2) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 8) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100000) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 5
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],k = 2) == 15
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6],k = 1) == 14
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 3
    assert candidate(nums = [2, 5, 8, 11, 14, 17, 20],k = 3) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 8) == 9
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145],k = 25) == 6
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],k = 20) == 11
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000],k = 25000) == 6
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 4
    assert candidate(nums = [100, 100, 100, 200, 200, 200, 300, 300, 300, 400, 400, 400, 500, 500, 500],k = 100) == 9
    assert candidate(nums = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23],k = 3) == 4
    assert candidate(nums = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],k = 45) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 1
    assert candidate(nums = [5, 15, 25, 35, 45, 55],k = 10) == 3
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6],k = 1) == 15
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 12) == 25
