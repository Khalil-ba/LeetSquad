# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [10, 20, 30],start = 100,goal = 50) == 2
    assert candidate(nums = [1, 2, 3],start = 5,goal = 5) == 2
    assert candidate(nums = [5, 15, 25],start = 10,goal = 30) == 2
    assert candidate(nums = [10, 20, 30],start = 100,goal = 300) == 7
    assert candidate(nums = [500, 500, 500],start = 1,goal = 1001) == 2
    assert candidate(nums = [1, 3, 5, 7, 9],start = 0,goal = 10) == 2
    assert candidate(nums = [1, 3, 5, 7, 9],start = 1000,goal = 0) == 112
    assert candidate(nums = [10, 20, 30, 40, 50],start = 100,goal = 0) == 2
    assert candidate(nums = [10, 20, 30],start = 100,goal = 200) == 4
    assert candidate(nums = [500, 501, 502],start = 500,goal = 505) == 4
    assert candidate(nums = [1000, -1000, 500],start = 0,goal = 1000) == 1
    assert candidate(nums = [-1000, 1000],start = 0,goal = 0) == 2
    assert candidate(nums = [7, 14, 28],start = 1,goal = 28) == 4
    assert candidate(nums = [100, 200, 300],start = 100,goal = 1000) == 3
    assert candidate(nums = [100, 200, 300],start = 500,goal = 1000) == 2
    assert candidate(nums = [1],start = 0,goal = 1000) == 1000
    assert candidate(nums = [500, 500],start = 500,goal = 1000) == 1
    assert candidate(nums = [7, 14, 21],start = 7,goal = 0) == 1
    assert candidate(nums = [1000],start = 1000,goal = 0) == 1
    assert candidate(nums = [2, 4, 12],start = 2,goal = 12) == 2
    assert candidate(nums = [1, 1000],start = 0,goal = 1001) == 2
    assert candidate(nums = [1, 3, 5, 7, 9],start = 500,goal = 500) == 2
    assert candidate(nums = [-1, -2, -3],start = 5,goal = -5) == 1
    assert candidate(nums = [100, 200, 300],start = 500,goal = 100) == 2
    assert candidate(nums = [1, 1000],start = 500,goal = 1500) == 1
    assert candidate(nums = [3, 5, 7],start = 0,goal = -4) == 2
    assert candidate(nums = [1, 2, 3],start = 1000,goal = 0) == 334
    assert candidate(nums = [500, 500, 500],start = 100,goal = 500) == -1
    assert candidate(nums = [10, 20, 30],start = 50,goal = 110) == 2
    assert candidate(nums = [2, 8, 16],start = 0,goal = 1) == -1
    assert candidate(nums = [1000, 500, 250],start = 1,goal = 1000) == -1
    assert candidate(nums = [1, 2, 3, 4, 5],start = 1,goal = 5) == 1
    assert candidate(nums = [1, 2, 3, 4, 5],start = 5,goal = 0) == 1
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],start = 50,goal = 1000) == 10
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],start = 1,goal = 1000) == 3
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],start = 1000,goal = 0) == 22
    assert candidate(nums = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],start = 500,goal = 1000) == -1
    assert candidate(nums = [256, 512, 768, 1024],start = 0,goal = 1024) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 500,goal = 1) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 10,goal = 1000) == 10
    assert candidate(nums = [10, 20, 30, 40, 50],start = 1000,goal = 0) == 20
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],start = 500,goal = 1000) == 6
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113],start = 0,goal = 999) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 10,goal = 500) == 490
    assert candidate(nums = [13, 21, 34, 55, 89, 144, 233, 377, 610, 987],start = 500,goal = 1000) == 3
    assert candidate(nums = [256, 128, 64, 32, 16, 8, 4, 2, 1],start = 500,goal = 999) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],start = 1000,goal = 0) == 18
    assert candidate(nums = [999, 1, 2, 3, 4, 5],start = 0,goal = 999) == 1
    assert candidate(nums = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],start = 512,goal = 0) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],start = 5,goal = 100) == 10
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],start = 50,goal = 999) == 10
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],start = 1,goal = 98) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],start = 100,goal = 1000) == 48
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],start = 50,goal = 1000) == 106
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],start = 500,goal = 1000) == 17
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],start = 100,goal = 256) == 3
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],start = 25,goal = 1000) == 20
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],start = 1,goal = 999) == 36
    assert candidate(nums = [10, 20, 30, 40, 50],start = 500,goal = -100) == -1
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29],start = 1,goal = 999) == 36
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],start = 50,goal = 999) == 21
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 500,goal = 0) == 5
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],start = 1,goal = 1000) == 33
    assert candidate(nums = [13, 19, 23, 29, 31, 37, 41, 43, 47, 53],start = 200,goal = 300) == 2
    assert candidate(nums = [1, 10, 100, 1000],start = 1,goal = 1000) == 2
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],start = 500,goal = 0) == 3
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],start = 100,goal = 1000) == 10
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41],start = 100,goal = 999) == 23
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110],start = 10,goal = 1000) == 9
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],start = 1,goal = 1000) == 5
    assert candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],start = 0,goal = 1000) == 2
    assert candidate(nums = [333, 667, 999],start = 1,goal = 999) == 2
    assert candidate(nums = [999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],start = 1,goal = 1000) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],start = 0,goal = 1000) == 4
    assert candidate(nums = [64, 128, 256, 512],start = 100,goal = 1024) == -1
    assert candidate(nums = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144],start = 10,goal = 200) == 3
    assert candidate(nums = [123, 456, 789],start = 321,goal = 654) == 2
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],start = 1000,goal = 0) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290],start = 50,goal = 1000) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 500,goal = 1000) == 500
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],start = 100,goal = 0) == 3
    assert candidate(nums = [999, 1000, 1001, 1002, 1003],start = 500,goal = 1500) == 1
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91, 104, 117, 130],start = 100,goal = 200) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 0,goal = 500) == 5
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],start = 500,goal = 1000) == 1
    assert candidate(nums = [100, 200, 300, 400, 500],start = 10,goal = 999) == -1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],start = 100,goal = 999) == 31
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 500,goal = 1000) == 500
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],start = 1024,goal = 1) == 2
    assert candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],start = 100,goal = 1000) == 9
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1000],start = 500,goal = 1500) == 1
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],start = 100,goal = 2048) == -1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],start = 100,goal = 511) == 5
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 100,goal = 99) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 50,goal = 1000) == 10
    assert candidate(nums = [123, 456, 789],start = 100,goal = 900) == 6
    assert candidate(nums = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67],start = 5,goal = 1000) == 15
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],start = 50,goal = 500) == 6
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],start = 1,goal = 1000000000) == 2
    assert candidate(nums = [333, 667, 999],start = 500,goal = 1000) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],start = 500,goal = 400) == 6
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99],start = 500,goal = 200) == 4
    assert candidate(nums = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39],start = 200,goal = 500) == 8
    assert candidate(nums = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26],start = 500,goal = 550) == 2
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],start = 1,goal = 1000) == 11
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 50,goal = 990) == 10
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],start = 100,goal = -100) == -1
    assert candidate(nums = [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],start = 500,goal = 999) == 7
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],start = 0,goal = 500) == 10
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],start = 100,goal = 1000) == 10
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],start = 50,goal = 999) == 11
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],start = 500,goal = 1024) == 3
    assert candidate(nums = [100, 200, 300, 400, 500],start = 999,goal = 1) == -1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],start = 512,goal = 1000) == 3
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],start = 50,goal = 150) == 1
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],start = 50,goal = 987) == 3
    assert candidate(nums = [23, 45, 67, 89, 101],start = 100,goal = 1) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],start = 1,goal = 1000) == 200
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],start = 500,goal = 1024) == 3
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],start = 1,goal = 999) == 54
    assert candidate(nums = [100, 200, 300, 400, 500],start = 100,goal = 500) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],start = 500,goal = 1005) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],start = 1,goal = 1001) == 100
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],start = 1,goal = 999) == 1
    assert candidate(nums = [100, 200, 300, 400, 500],start = 50,goal = 500) == -1
    assert candidate(nums = [-1, 1, -2, 2, -4, 4, -8, 8, -16, 16],start = 500,goal = 1) == 33
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 1,goal = 1000) == 999
    assert candidate(nums = [666, 333, 111, 777, 888, 999, 222, 444, 555],start = 111,goal = 777) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],start = 0,goal = 1000) == 1000
    assert candidate(nums = [-100, -50, -25, 0, 25, 50, 100],start = 50,goal = 250) == 2
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],start = 1,goal = 1000) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],start = 1000,goal = 1) == 50
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],start = 10,goal = 99) == 4
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],start = 500,goal = 999) == 4
