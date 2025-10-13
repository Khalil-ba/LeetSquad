# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(cardPoints = [5, 2, 1, 2, 5],k = 3) == 12
    assert candidate(cardPoints = [9, 7, 7, 9, 7, 7, 9],k = 7) == 55
    assert candidate(cardPoints = [1, 1000, 1],k = 1) == 1
    assert candidate(cardPoints = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 40
    assert candidate(cardPoints = [2, 2, 2],k = 2) == 4
    assert candidate(cardPoints = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 34
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 1],k = 3) == 12
    assert candidate(cardPoints = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 90
    assert candidate(cardPoints = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 5) == 5000
    assert candidate(cardPoints = [100, 400, 300, 100, 200, 500, 600, 300, 400],k = 4) == 1800
    assert candidate(cardPoints = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 10) == 1111111111
    assert candidate(cardPoints = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 300
    assert candidate(cardPoints = [5, 2, 1, 2, 5, 5, 5, 5, 5, 2, 1, 2, 5],k = 8) == 30
    assert candidate(cardPoints = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10) == 100000
    assert candidate(cardPoints = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 155
    assert candidate(cardPoints = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 50
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 195
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 19
    assert candidate(cardPoints = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 5) == 50000
    assert candidate(cardPoints = [3, 1, 2, 7, 4, 5, 6],k = 3) == 15
    assert candidate(cardPoints = [10, 1, 1, 10, 1, 1, 10, 1, 1],k = 3) == 12
    assert candidate(cardPoints = [5, 1, 1, 2, 4, 2, 2, 5, 5, 4],k = 5) == 21
    assert candidate(cardPoints = [8, 9, 10, 4, 10, 1, 1, 1, 5, 9],k = 4) == 36
    assert candidate(cardPoints = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 10) == 5000
    assert candidate(cardPoints = [5, 1, 1, 2, 4, 2, 2, 5, 5, 5],k = 3) == 15
    assert candidate(cardPoints = [5, 6, 4, 2, 7, 8, 3, 1, 9],k = 4) == 24
    assert candidate(cardPoints = [1000, 100, 10, 1, 10000, 1000, 100, 10],k = 4) == 11110
    assert candidate(cardPoints = [1, 2, 100, 3, 4, 100, 5, 6, 100, 7, 8, 100, 9, 10, 100, 11, 12, 100, 13, 14],k = 7) == 260
    assert candidate(cardPoints = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 34
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 90
    assert candidate(cardPoints = [5, 3, 8, 7, 6, 2, 9, 1, 4, 10],k = 4) == 26
    assert candidate(cardPoints = [10, 4, 5, 1, 7, 12, 3, 8, 6],k = 4) == 29
    assert candidate(cardPoints = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(cardPoints = [5, 9, 3, 4, 6, 7, 2, 8, 1, 0],k = 5) == 27
    assert candidate(cardPoints = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 10
    assert candidate(cardPoints = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],k = 6) == 39
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 195
    assert candidate(cardPoints = [5, 2, 1, 3, 4, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],k = 8) == 51
    assert candidate(cardPoints = [10000, 10000, 10000, 10000, 10000],k = 5) == 50000
    assert candidate(cardPoints = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
    assert candidate(cardPoints = [8, 9, 10, 4, 10, 4, 2, 2, 10, 10, 8, 6, 5, 1, 5, 9, 1, 6, 10, 8],k = 6) == 51
    assert candidate(cardPoints = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 5) == 15
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 49
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 57
    assert candidate(cardPoints = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 10) == 1550
    assert candidate(cardPoints = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],k = 10) == 20
    assert candidate(cardPoints = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 25
    assert candidate(cardPoints = [10000, 1, 10000, 1, 10000, 1],k = 3) == 20001
    assert candidate(cardPoints = [100, 40, 17, 9, 73, 75, 36, 21, 14, 92, 58],k = 5) == 307
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 34
    assert candidate(cardPoints = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 15) == 23
    assert candidate(cardPoints = [8, 9, 7, 6, 5, 4, 3, 2, 1],k = 3) == 24
    assert candidate(cardPoints = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 18) == 90
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 20) == 810
    assert candidate(cardPoints = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 6) == 84
    assert candidate(cardPoints = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991],k = 5) == 49990
    assert candidate(cardPoints = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41],k = 15) == 405
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 84
    assert candidate(cardPoints = [2, 3, 1, 2, 4, 3, 1, 5, 4],k = 5) == 17
    assert candidate(cardPoints = [5, 1, 1, 2, 4, 2, 2, 5, 5, 1],k = 3) == 11
    assert candidate(cardPoints = [5, 3, 1, 2, 6, 4, 8, 9, 10, 7, 2, 1, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 193
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 209
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 40
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 155
    assert candidate(cardPoints = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 400
    assert candidate(cardPoints = [3, 2, 6, 7, 5, 4, 8, 1, 9],k = 4) == 22
    assert candidate(cardPoints = [3, 2, 7, 4, 1],k = 2) == 5
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 345
    assert candidate(cardPoints = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 155
    assert candidate(cardPoints = [3, 1, 3, 100, 100, 100, 3, 1, 3],k = 5) == 207
    assert candidate(cardPoints = [3, 1, 5, 9, 2, 6, 5, 3, 5, 9],k = 5) == 28
    assert candidate(cardPoints = [5, 2, 1, 7, 3, 4, 6],k = 4) == 20
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 210
    assert candidate(cardPoints = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 3) == 270
    assert candidate(cardPoints = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 55
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 27
    assert candidate(cardPoints = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 15) == 3450
    assert candidate(cardPoints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 5) == 65
