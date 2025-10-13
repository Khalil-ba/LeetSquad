# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(bulbs = [1, 2, 4, 3, 5, 6, 7],k = 2) == -1
    assert candidate(bulbs = [1, 4, 3, 2],k = 1) == 3
    assert candidate(bulbs = [6, 5, 8, 9, 7, 1, 4, 3, 2, 10],k = 2) == 7
    assert candidate(bulbs = [6, 5, 8, 9, 7, 1, 4, 2, 3, 10],k = 2) == 7
    assert candidate(bulbs = [3, 9, 2, 8, 1, 6, 10, 5, 4, 7],k = 3) == -1
    assert candidate(bulbs = [2, 1, 3],k = 1) == -1
    assert candidate(bulbs = [1, 3, 5, 7, 2, 6, 4, 8, 10, 9],k = 2) == -1
    assert candidate(bulbs = [6, 5, 8, 9, 7, 1, 10, 2, 3, 4],k = 2) == 8
    assert candidate(bulbs = [1, 2, 3],k = 1) == -1
    assert candidate(bulbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 2
    assert candidate(bulbs = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 2) == -1
    assert candidate(bulbs = [3, 9, 2, 8, 1, 6, 10, 5, 4, 7],k = 1) == 6
    assert candidate(bulbs = [1, 3, 2],k = 1) == 2
    assert candidate(bulbs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 0) == 2
    assert candidate(bulbs = [2, 1, 3, 5, 4],k = 1) == 4
    assert candidate(bulbs = [1, 6, 2, 5, 3, 4, 7, 8, 9, 10],k = 2) == 4
    assert candidate(bulbs = [20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 5) == 15
    assert candidate(bulbs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20],k = 1) == 2
    assert candidate(bulbs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == -1
    assert candidate(bulbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 0) == 2
    assert candidate(bulbs = [5, 3, 1, 2, 4],k = 1) == 2
    assert candidate(bulbs = [8, 6, 9, 7, 10, 3, 5, 1, 4, 2],k = 4) == -1
    assert candidate(bulbs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],k = 1) == 2
    assert candidate(bulbs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == -1
    assert candidate(bulbs = [15, 1, 13, 11, 14, 10, 9, 6, 12, 8, 7, 4, 5, 3, 2],k = 3) == -1
    assert candidate(bulbs = [3, 5, 4, 1, 2, 6, 8, 7],k = 1) == 2
    assert candidate(bulbs = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 1) == 2
    assert candidate(bulbs = [1, 4, 3, 5, 2],k = 1) == 3
    assert candidate(bulbs = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == -1
    assert candidate(bulbs = [7, 8, 4, 3, 6, 5, 2, 1, 9, 10],k = 2) == 3
    assert candidate(bulbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 3) == -1
    assert candidate(bulbs = [3, 1, 5, 4, 2],k = 2) == -1
    assert candidate(bulbs = [1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2],k = 1) == 15
    assert candidate(bulbs = [3, 1, 5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 15, 12, 17, 14, 19, 16, 20, 2],k = 3) == -1
    assert candidate(bulbs = [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],k = 10) == 5
    assert candidate(bulbs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 0) == 2
    assert candidate(bulbs = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9],k = 2) == -1
    assert candidate(bulbs = [15, 12, 10, 14, 7, 6, 13, 8, 9, 11, 4, 2, 3, 1, 5],k = 4) == -1
    assert candidate(bulbs = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 9) == -1
    assert candidate(bulbs = [3, 1, 2, 6, 5, 4, 10, 9, 8, 7],k = 2) == 4
    assert candidate(bulbs = [1, 6, 2, 5, 4, 3],k = 2) == 4
    assert candidate(bulbs = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 0) == 2
    assert candidate(bulbs = [1, 4, 7, 10, 13, 16, 19, 2, 5, 8, 11, 14, 17, 20, 3, 6, 9, 12, 15, 18],k = 6) == -1
    assert candidate(bulbs = [1, 10, 5, 3, 8, 6, 7, 2, 9, 4],k = 2) == 5
    assert candidate(bulbs = [7, 3, 5, 1, 9, 4, 8, 2, 6, 10],k = 3) == 2
    assert candidate(bulbs = [3, 1, 2, 5, 4, 8, 7, 10, 9, 6],k = 2) == 6
    assert candidate(bulbs = [3, 1, 2, 5, 4, 6, 8, 7, 10, 9],k = 2) == -1
    assert candidate(bulbs = [12, 1, 14, 10, 15, 13, 3, 2, 9, 11, 5, 7, 8, 4, 6],k = 3) == 11
    assert candidate(bulbs = [4, 3, 2, 5, 1, 7, 6, 8, 9, 10],k = 3) == -1
    assert candidate(bulbs = [5, 1, 4, 3, 2],k = 1) == 4
    assert candidate(bulbs = [6, 10, 1, 3, 8, 5, 2, 7, 9, 4],k = 2) == 4
    assert candidate(bulbs = [5, 3, 8, 6, 2, 7, 4, 1, 10, 9],k = 2) == 3
    assert candidate(bulbs = [3, 1, 2, 5, 4, 6, 8, 7, 9, 11, 10, 12, 14, 13, 15],k = 1) == 2
    assert candidate(bulbs = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2],k = 4) == 6
    assert candidate(bulbs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == -1
    assert candidate(bulbs = [8, 1, 4, 3, 7, 10, 9, 2, 6, 5],k = 2) == 3
    assert candidate(bulbs = [1, 6, 3, 4, 7, 2, 5, 8, 9, 10],k = 2) == 3
    assert candidate(bulbs = [7, 5, 6, 8, 1, 3, 4, 2, 10, 9],k = 2) == -1
    assert candidate(bulbs = [3, 1, 2, 5, 6, 4, 7, 10, 8, 9],k = 2) == 8
    assert candidate(bulbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 9) == -1
    assert candidate(bulbs = [1, 4, 6, 2, 7, 5, 3, 8, 10, 9],k = 3) == -1
    assert candidate(bulbs = [10, 5, 1, 9, 4, 2, 8, 7, 3, 6],k = 4) == 2
    assert candidate(bulbs = [5, 1, 2, 4, 3, 6],k = 1) == 4
    assert candidate(bulbs = [2, 3, 5, 4, 1, 6, 7, 8, 10, 9],k = 3) == -1
    assert candidate(bulbs = [16, 14, 2, 1, 3, 5, 15, 6, 7, 9, 4, 8, 10, 12, 13, 11],k = 5) == -1
    assert candidate(bulbs = [7, 5, 3, 1, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14, 16],k = 2) == -1
    assert candidate(bulbs = [1, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 15],k = 5) == 9
    assert candidate(bulbs = [1, 4, 2, 3, 6, 5, 8, 7, 10, 9],k = 3) == -1
    assert candidate(bulbs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == -1
    assert candidate(bulbs = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == -1
    assert candidate(bulbs = [3, 9, 2, 8, 1, 6, 10, 5, 4, 7],k = 2) == 6
    assert candidate(bulbs = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 2) == -1
    assert candidate(bulbs = [3, 1, 9, 7, 5, 4, 8, 6, 10, 2],k = 4) == -1
    assert candidate(bulbs = [1, 2, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 1) == 3
    assert candidate(bulbs = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],k = 4) == -1
    assert candidate(bulbs = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 0) == 2
    assert candidate(bulbs = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2],k = 2) == -1
    assert candidate(bulbs = [1, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12],k = 4) == -1
    assert candidate(bulbs = [5, 2, 1, 3, 4],k = 0) == 3
    assert candidate(bulbs = [6, 2, 3, 4, 5, 1],k = 4) == -1
    assert candidate(bulbs = [1, 4, 2, 3, 6, 5],k = 1) == 3
    assert candidate(bulbs = [2, 6, 1, 7, 3, 5, 4, 8],k = 2) == 5
    assert candidate(bulbs = [1, 5, 9, 4, 6, 2, 8, 3, 7, 10],k = 3) == 2
    assert candidate(bulbs = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],k = 4) == 6
    assert candidate(bulbs = [5, 4, 3, 2, 1],k = 3) == -1
    assert candidate(bulbs = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10],k = 3) == -1
    assert candidate(bulbs = [1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10],k = 1) == 2
    assert candidate(bulbs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 0) == 2
    assert candidate(bulbs = [6, 2, 5, 1, 3, 4],k = 2) == 3
    assert candidate(bulbs = [7, 4, 6, 8, 2, 1, 3, 5],k = 3) == -1
    assert candidate(bulbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == -1
    assert candidate(bulbs = [4, 3, 1, 5, 2],k = 2) == -1
    assert candidate(bulbs = [1, 5, 4, 3, 2, 10, 9, 8, 7, 6],k = 4) == 6
    assert candidate(bulbs = [2, 1, 4, 3, 6, 5],k = 2) == -1
    assert candidate(bulbs = [5, 3, 1, 2, 4, 6, 8, 7, 9, 10],k = 1) == 2
    assert candidate(bulbs = [3, 5, 4, 1, 6, 2],k = 1) == 2
    assert candidate(bulbs = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1],k = 1) == 2
    assert candidate(bulbs = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10],k = 4) == 2
    assert candidate(bulbs = [8, 7, 6, 5, 4, 3, 2, 1],k = 3) == -1
    assert candidate(bulbs = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 2) == 8
    assert candidate(bulbs = [14, 4, 13, 2, 6, 3, 10, 1, 7, 5, 12, 9, 11, 8],k = 4) == -1
    assert candidate(bulbs = [3, 9, 2, 8, 1, 6, 5, 4, 7, 10],k = 3) == -1
    assert candidate(bulbs = [1, 5, 3, 4, 2, 8, 7, 6, 10, 9, 13, 12, 11, 15, 14, 18, 17, 16, 20, 19],k = 2) == 6
    assert candidate(bulbs = [3, 1, 5, 4, 2],k = 1) == 2
    assert candidate(bulbs = [4, 5, 6, 1, 7, 3, 2, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == -1
    assert candidate(bulbs = [1, 5, 3, 7, 9, 2, 4, 6, 8, 10],k = 3) == 2
    assert candidate(bulbs = [12, 1, 13, 2, 14, 3, 15, 4, 5, 6, 7, 8, 9, 10, 11],k = 4) == 11
    assert candidate(bulbs = [16, 20, 23, 11, 12, 24, 2, 13, 10, 17, 5, 9, 25, 3, 7, 18, 19, 1, 14, 15, 6, 4, 8, 21, 22],k = 5) == -1
    assert candidate(bulbs = [5, 4, 3, 2, 1],k = 0) == 2
    assert candidate(bulbs = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10],k = 6) == 14
    assert candidate(bulbs = [15, 8, 2, 11, 4, 13, 7, 6, 3, 1, 5, 12, 10, 9, 14],k = 5) == 3
    assert candidate(bulbs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 3) == -1
    assert candidate(bulbs = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 1) == 3
    assert candidate(bulbs = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 8) == -1
    assert candidate(bulbs = [15, 1, 14, 10, 4, 2, 11, 5, 3, 8, 6, 7, 13, 12, 9],k = 5) == 5
