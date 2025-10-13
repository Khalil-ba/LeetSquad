# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(arr = [2, 1, 3, 5, 4, 6, 7],k = 2) == 5
    assert candidate(arr = [7, 10, 5, 3, 8],k = 3) == 10
    assert candidate(arr = [5, 4, 3, 2, 1],k = 1) == 5
    assert candidate(arr = [3, 2, 1],k = 10) == 3
    assert candidate(arr = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 4) == 100
    assert candidate(arr = [5, 1, 4, 2, 3],k = 4) == 5
    assert candidate(arr = [1, 2, 3, 4, 5],k = 1) == 2
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 10
    assert candidate(arr = [1, 2, 3, 4, 5],k = 3) == 5
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1],k = 3) == 7
    assert candidate(arr = [7, 6, 5, 8, 4, 3, 2, 1],k = 4) == 8
    assert candidate(arr = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10],k = 7) == 10
    assert candidate(arr = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],k = 7) == 999999
    assert candidate(arr = [5, 1, 9, 3, 7, 2, 8, 4, 6],k = 4) == 9
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 6) == 19
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10],k = 2) == 7
    assert candidate(arr = [500000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 10) == 500000
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 10
    assert candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 1) == 3
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 50) == 100
    assert candidate(arr = [2, 1, 3, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 20
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 3) == 20
    assert candidate(arr = [7, 14, 28, 8, 16, 32, 4, 2, 1],k = 6) == 32
    assert candidate(arr = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 1000000
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1000000) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 2
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 200
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 1) == 3
    assert candidate(arr = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 10
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 4) == 19
    assert candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 3) == 20
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 10) == 10
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 7) == 20
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 10
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 8) == 20
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 15) == 20
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 5) == 19
    assert candidate(arr = [5, 8, 4, 9, 3, 2, 1, 6, 7, 10],k = 6) == 9
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 100
    assert candidate(arr = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 100
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 100
    assert candidate(arr = [1000000, 999999, 999998, 999997, 999996, 999995, 999994],k = 6) == 1000000
    assert candidate(arr = [4, 8, 6, 2, 7, 3, 9, 1, 5, 10],k = 6) == 10
    assert candidate(arr = [50, 20, 30, 10, 40],k = 3) == 50
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 3) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 500000],k = 10) == 500000
    assert candidate(arr = [5, 1, 4, 3, 2],k = 4) == 5
    assert candidate(arr = [5, 2, 9, 1, 7, 8, 3, 6, 4],k = 5) == 9
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10],k = 7) == 9
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 7) == 10
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 30
    assert candidate(arr = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5],k = 3) == 50
    assert candidate(arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],k = 7) == 30
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 10) == 20
    assert candidate(arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],k = 4) == 10
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 10
    assert candidate(arr = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],k = 10) == 1000000
    assert candidate(arr = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],k = 5) == 1000000
    assert candidate(arr = [9, 3, 5, 2, 8, 1, 7, 6, 4, 10],k = 2) == 9
    assert candidate(arr = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 3) == 5
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 20
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 20
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 19
    assert candidate(arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 2) == 9
    assert candidate(arr = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989],k = 10) == 100000
    assert candidate(arr = [5, 1, 4, 2, 3],k = 4) == 5
    assert candidate(arr = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],k = 4) == 5
    assert candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 15],k = 8) == 15
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 30
    assert candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 20) == 30
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 10
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10],k = 4) == 7
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 3) == 100
    assert candidate(arr = [5, 3, 8, 6, 7, 2, 4, 9, 1],k = 4) == 8
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10],k = 1) == 9
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 3) == 10
    assert candidate(arr = [7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8],k = 5) == 7
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97],k = 3) == 100
    assert candidate(arr = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11],k = 5) == 89
    assert candidate(arr = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],k = 3) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 2
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],k = 5) == 20
    assert candidate(arr = [1, 25, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 25
    assert candidate(arr = [7, 14, 4, 14, 13, 2, 6, 13],k = 3) == 14
    assert candidate(arr = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],k = 2) == 2
    assert candidate(arr = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10],k = 3) == 5
    assert candidate(arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 5) == 10
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3) == 1000
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 25) == 100
    assert candidate(arr = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5],k = 10) == 99
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 15
    assert candidate(arr = [23, 11, 45, 78, 90, 67, 34, 21, 56, 89],k = 4) == 90
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 9) == 1000
    assert candidate(arr = [7, 10, 4, 3, 20, 15, 6, 1, 2, 8, 5, 9],k = 4) == 20
    assert candidate(arr = [100, 200, 50, 150, 250, 500, 400, 300, 600, 700],k = 7) == 700
    assert candidate(arr = [7, 8, 9, 10, 11, 5, 6, 1, 2, 3, 4],k = 3) == 11
    assert candidate(arr = [500, 400, 300, 200, 100, 101, 102, 103, 104, 105],k = 3) == 500
    assert candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 10) == 20
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 1) == 10
    assert candidate(arr = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10],k = 2) == 3
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 9
    assert candidate(arr = [1, 3, 2, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 15, 14, 16, 17, 19, 18, 20],k = 5) == 20
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],k = 4) == 100
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 10
    assert candidate(arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],k = 12) == 75
