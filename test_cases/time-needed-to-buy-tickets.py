# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(tickets = [5, 1, 1, 1],k = 0) == 8
    assert candidate(tickets = [4, 3, 2, 1],k = 1) == 9
    assert candidate(tickets = [100, 100, 100],k = 1) == 299
    assert candidate(tickets = [1],k = 0) == 1
    assert candidate(tickets = [10, 10, 10],k = 2) == 30
    assert candidate(tickets = [10, 10, 10],k = 0) == 28
    assert candidate(tickets = [10, 10, 10],k = 1) == 29
    assert candidate(tickets = [1, 2, 3, 4, 5],k = 4) == 15
    assert candidate(tickets = [2, 3, 2],k = 2) == 6
    assert candidate(tickets = [100, 100, 100],k = 2) == 300
    assert candidate(tickets = [1, 1, 1, 1],k = 2) == 3
    assert candidate(tickets = [1, 1, 1, 1],k = 1) == 2
    assert candidate(tickets = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 19) == 110
    assert candidate(tickets = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 10) == 59
    assert candidate(tickets = [9, 3, 5, 7, 1, 2, 6],k = 4) == 5
    assert candidate(tickets = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 91
    assert candidate(tickets = [7, 2, 9, 1, 8, 3, 6, 4, 5],k = 6) == 39
    assert candidate(tickets = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],k = 15) == 86
    assert candidate(tickets = [1, 2, 3, 4, 5, 4, 3, 2, 1],k = 8) == 9
    assert candidate(tickets = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 15) == 76
    assert candidate(tickets = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 91
    assert candidate(tickets = [25, 30, 15, 20, 10],k = 3) == 85
    assert candidate(tickets = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 5) == 44
    assert candidate(tickets = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 4) == 25
    assert candidate(tickets = [5, 2, 3, 1, 4],k = 2) == 11
    assert candidate(tickets = [5, 1, 2, 3, 4],k = 0) == 15
    assert candidate(tickets = [3, 1, 5, 4, 2],k = 3) == 14
    assert candidate(tickets = [7, 8, 9, 10, 11, 12, 13, 14, 15],k = 8) == 99
    assert candidate(tickets = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 10
    assert candidate(tickets = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 8) == 29
    assert candidate(tickets = [9, 3, 8, 4, 6, 7, 5, 2, 1],k = 1) == 19
    assert candidate(tickets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 19) == 20
    assert candidate(tickets = [1, 5, 3, 4, 2, 6, 7, 8],k = 5) == 31
    assert candidate(tickets = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 15) == 28
    assert candidate(tickets = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2],k = 10) == 192
    assert candidate(tickets = [5, 4, 3, 2, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1],k = 19) == 20
    assert candidate(tickets = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 81
    assert candidate(tickets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 4) == 395
    assert candidate(tickets = [1, 2, 3, 4, 3, 2, 1],k = 5) == 12
    assert candidate(tickets = [5, 3, 5, 2, 4, 1, 3],k = 3) == 11
    assert candidate(tickets = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4],k = 10) == 43
    assert candidate(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 85
    assert candidate(tickets = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == 16
    assert candidate(tickets = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 4) == 45
    assert candidate(tickets = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 9) == 90
    assert candidate(tickets = [1, 2, 3, 4, 5, 4, 3, 2, 1],k = 4) == 25
    assert candidate(tickets = [2, 6, 3, 4, 5, 1],k = 2) == 13
    assert candidate(tickets = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 9) == 10
    assert candidate(tickets = [20, 1, 20, 1, 20],k = 2) == 61
    assert candidate(tickets = [25, 30, 5, 10, 15],k = 1) == 85
    assert candidate(tickets = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],k = 8) == 9
    assert candidate(tickets = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 4) == 35
    assert candidate(tickets = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 40
    assert candidate(tickets = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 0) == 45
    assert candidate(tickets = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],k = 0) == 1
    assert candidate(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 156
    assert candidate(tickets = [5, 4, 3, 2, 1],k = 0) == 15
    assert candidate(tickets = [4, 2, 3, 3, 1, 4, 2, 3],k = 5) == 22
    assert candidate(tickets = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 50) == 104
    assert candidate(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 19) == 210
    assert candidate(tickets = [5, 6, 7, 8, 9],k = 2) == 30
    assert candidate(tickets = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 49) == 162
    assert candidate(tickets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 6
    assert candidate(tickets = [10, 15, 5, 20, 25, 30, 5],k = 4) == 104
    assert candidate(tickets = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 0) == 55
    assert candidate(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 35
    assert candidate(tickets = [1, 5, 2, 3, 4, 5],k = 5) == 20
    assert candidate(tickets = [3, 1, 5, 2, 4, 6],k = 3) == 9
    assert candidate(tickets = [20, 15, 10, 5, 1],k = 0) == 51
    assert candidate(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 1
    assert candidate(tickets = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],k = 19) == 20
    assert candidate(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 41
    assert candidate(tickets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 11
    assert candidate(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 156
    assert candidate(tickets = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 9) == 30
    assert candidate(tickets = [10, 1, 10, 1, 10, 1, 10],k = 3) == 4
    assert candidate(tickets = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 0) == 163
    assert candidate(tickets = [10, 5, 4, 6, 3, 8, 2],k = 4) == 19
    assert candidate(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 55
    assert candidate(tickets = [2, 5, 3, 4, 1, 2],k = 2) == 13
    assert candidate(tickets = [10, 20, 30, 40, 50],k = 2) == 118
    assert candidate(tickets = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],k = 0) == 393
    assert candidate(tickets = [3, 2, 1, 4, 5, 6],k = 5) == 21
    assert candidate(tickets = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 238
    assert candidate(tickets = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 5) == 36
    assert candidate(tickets = [20, 15, 10, 5, 1],k = 1) == 46
    assert candidate(tickets = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 9) == 10
    assert candidate(tickets = [3, 3, 3, 3, 3],k = 2) == 13
    assert candidate(tickets = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 96
    assert candidate(tickets = [50, 50, 50, 50, 50],k = 2) == 248
    assert candidate(tickets = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 7) == 38
    assert candidate(tickets = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],k = 9) == 110
    assert candidate(tickets = [7, 8, 9, 10, 11, 12, 13, 14],k = 5) == 79
    assert candidate(tickets = [3, 5, 2, 4, 1],k = 2) == 8
    assert candidate(tickets = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 3) == 24
    assert candidate(tickets = [1, 1, 1, 2, 2, 2, 3, 3, 3],k = 6) == 16
    assert candidate(tickets = [5, 4, 3, 2, 1],k = 2) == 12
    assert candidate(tickets = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 8) == 29
    assert candidate(tickets = [50, 30, 20, 10, 90, 80, 70, 60],k = 4) == 410
