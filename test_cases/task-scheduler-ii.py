# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 10) == 10
    assert candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],space = 1) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5],space = 5) == 5
    assert candidate(tasks = [1, 1, 1, 1, 1],space = 1) == 9
    assert candidate(tasks = [1, 1, 1, 1],space = 2) == 10
    assert candidate(tasks = [1, 1, 1, 1, 1],space = 5) == 25
    assert candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],space = 5) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5],space = 1) == 5
    assert candidate(tasks = [1, 1, 1, 1],space = 1) == 7
    assert candidate(tasks = [1, 2, 1, 2, 3, 1],space = 3) == 9
    assert candidate(tasks = [5, 8, 8, 5],space = 2) == 6
    assert candidate(tasks = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],space = 10) == 10
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 1) == 10
    assert candidate(tasks = [1000000000, 999999999, 1000000000, 999999999, 1000000000],space = 3) == 9
    assert candidate(tasks = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],space = 100000000) == 400000005
    assert candidate(tasks = [1, 3, 2, 3, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],space = 4) == 34
    assert candidate(tasks = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],space = 1) == 36
    assert candidate(tasks = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],space = 2) == 12
    assert candidate(tasks = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],space = 100000) == 400005
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 10) == 21
    assert candidate(tasks = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10],space = 3) == 34
    assert candidate(tasks = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],space = 20) == 191
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],space = 100) == 6869
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],space = 1) == 39
    assert candidate(tasks = [1, 2, 2, 1, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9, 10, 9, 10],space = 5) == 41
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 0) == 20
    assert candidate(tasks = [1000000000, 1, 2, 1000000000, 3, 4, 1000000000, 5],space = 2) == 8
    assert candidate(tasks = [5, 1, 2, 5, 1, 2, 5, 1, 2],space = 3) == 11
    assert candidate(tasks = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],space = 3) == 38
    assert candidate(tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],space = 5) == 29
    assert candidate(tasks = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2],space = 2) == 64
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],space = 1) == 19
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],space = 15) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 4) == 20
    assert candidate(tasks = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],space = 9) == 91
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 15) == 30
    assert candidate(tasks = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],space = 1) == 20
    assert candidate(tasks = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6],space = 3) == 66
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],space = 10) == 188
    assert candidate(tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],space = 5) == 17
    assert candidate(tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],space = 2) == 10
    assert candidate(tasks = [5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],space = 5) == 25
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5],space = 4) == 25
    assert candidate(tasks = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],space = 1) == 20
    assert candidate(tasks = [1000000000, 999999999, 1000000000, 999999999, 1000000000],space = 2) == 7
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],space = 10) == 100
    assert candidate(tasks = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],space = 2) == 20
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],space = 10) == 210
    assert candidate(tasks = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 1000000000],space = 5) == 11
    assert candidate(tasks = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],space = 1) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 20) == 52
    assert candidate(tasks = [100, 200, 300, 400, 500, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500],space = 50) == 107
    assert candidate(tasks = [999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990, 999999989, 999999988, 999999987, 999999986, 999999985],space = 10) == 15
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],space = 5) == 70
    assert candidate(tasks = [1, 2, 3, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1],space = 2) == 20
    assert candidate(tasks = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],space = 3) == 18
    assert candidate(tasks = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3],space = 3) == 38
    assert candidate(tasks = [1, 3, 5, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9],space = 5) == 20
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],space = 3) == 77
    assert candidate(tasks = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],space = 10) == 113
    assert candidate(tasks = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50],space = 15) == 53
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 10) == 32
    assert candidate(tasks = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],space = 1) == 12
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],space = 19) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 5) == 20
    assert candidate(tasks = [1, 2, 2, 1, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],space = 2) == 34
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],space = 5) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],space = 2) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 5) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],space = 3) == 18
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],space = 5) == 140
    assert candidate(tasks = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],space = 9) == 91
    assert candidate(tasks = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1],space = 3) == 31
    assert candidate(tasks = [1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999],space = 5) == 14
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],space = 2) == 40
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],space = 3) == 75
    assert candidate(tasks = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],space = 3) == 35
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],space = 3) == 20
    assert candidate(tasks = [1, 2, 3, 2, 1, 2, 1, 2, 1],space = 2) == 12
    assert candidate(tasks = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5],space = 4) == 105
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],space = 0) == 20
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],space = 2) == 40
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 100) == 111
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],space = 3) == 74
    assert candidate(tasks = [1, 3, 2, 3, 1, 4, 2, 3, 1, 2, 4, 3, 1, 2, 3, 4, 1, 2, 3, 4],space = 4) == 28
    assert candidate(tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],space = 4) == 15
    assert candidate(tasks = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8],space = 2) == 20
    assert candidate(tasks = [1, 2, 1, 3, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1],space = 3) == 18
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 1) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5],space = 4) == 14
    assert candidate(tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],space = 5) == 265
    assert candidate(tasks = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],space = 0) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 10) == 30
    assert candidate(tasks = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],space = 1) == 21
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],space = 4) == 18
    assert candidate(tasks = [1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3],space = 2) == 36
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],space = 1) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],space = 20) == 20
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 1) == 30
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],space = 15) == 46
    assert candidate(tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],space = 1) == 20
    assert candidate(tasks = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],space = 4) == 47
