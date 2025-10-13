# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [4, 1],cost1 = 5,cost2 = 2) == 15
    assert candidate(nums = [1, 3, 5, 7, 9],cost1 = 2,cost2 = 4) == 40
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost1 = 1,cost2 = 2) == 0
    assert candidate(nums = [10, 10, 10, 10],cost1 = 100,cost2 = 50) == 0
    assert candidate(nums = [2, 3, 3, 3, 5],cost1 = 2,cost2 = 1) == 6
    assert candidate(nums = [1, 2, 3, 4, 5],cost1 = 1,cost2 = 2) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost1 = 7,cost2 = 3) == 0
    assert candidate(nums = [10, 10, 10, 10, 10],cost1 = 100,cost2 = 50) == 0
    assert candidate(nums = [1, 1, 1, 1],cost1 = 10,cost2 = 5) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],cost1 = 3,cost2 = 2) == 10
    assert candidate(nums = [1, 2, 3, 4, 5],cost1 = 10,cost2 = 5) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost1 = 1000000,cost2 = 500000) == 0
    assert candidate(nums = [1, 1000000],cost1 = 1,cost2 = 1000000) == 999999
    assert candidate(nums = [1, 1000000],cost1 = 1,cost2 = 1) == 999999
    assert candidate(nums = [1, 1000000],cost1 = 1,cost2 = 2) == 999999
    assert candidate(nums = [1000000, 1000000, 1000000],cost1 = 1000000,cost2 = 500000) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost1 = 5,cost2 = 2) == 49
    assert candidate(nums = [5, 5, 5, 5, 5],cost1 = 1,cost2 = 1) == 0
    assert candidate(nums = [1, 2],cost1 = 2,cost2 = 1) == 2
    assert candidate(nums = [100000, 100000, 100000],cost1 = 1,cost2 = 1) == 0
    assert candidate(nums = [3, 5, 3],cost1 = 1,cost2 = 3) == 4
    assert candidate(nums = [1, 2, 3],cost1 = 3,cost2 = 2) == 5
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],cost1 = 3,cost2 = 2) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],cost1 = 100000,cost2 = 50000) == 10950000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],cost1 = 1,cost2 = 3) == 9
    assert candidate(nums = [1, 3, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15],cost1 = 1,cost2 = 1) == 55
    assert candidate(nums = [100000, 100000, 100000, 100000, 100000],cost1 = 1,cost2 = 1) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],cost1 = 1,cost2 = 2) == 72
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],cost1 = 7,cost2 = 10) == 527
    assert candidate(nums = [1, 3, 5, 7, 9],cost1 = 3,cost2 = 5) == 50
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, 999989, 999988, 999987, 999986, 999985],cost1 = 1000,cost2 = 500) == 27000
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],cost1 = 123456,cost2 = 654321) == 18675295
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost1 = 10,cost2 = 5) == 1125
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost1 = 7,cost2 = 3) == 135
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost1 = 1,cost2 = 2) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],cost1 = 3,cost2 = 5) == 50
    assert candidate(nums = [1, 3, 5, 7, 9],cost1 = 2,cost2 = 3) == 30
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost1 = 1000000,cost2 = 500000) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost1 = 100000,cost2 = 50000) == 1200000
    assert candidate(nums = [1, 5, 9, 13, 17],cost1 = 3,cost2 = 5) == 100
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5],cost1 = 1,cost2 = 3) == 40
    assert candidate(nums = [100, 200, 300, 400, 500],cost1 = 10,cost2 = 7) == 3500
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost1 = 2,cost2 = 3) == 135
    assert candidate(nums = [5, 2, 3, 7, 1],cost1 = 3,cost2 = 5) == 43
    assert candidate(nums = [500000, 500001, 500002, 500003, 500004, 500005, 500006, 500007, 500008, 500009],cost1 = 1000000,cost2 = 2000000) == 45000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost1 = 1000,cost2 = 500) == 12000
    assert candidate(nums = [1, 3, 5, 7, 9],cost1 = 7,cost2 = 3) == 30
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],cost1 = 1000000,cost2 = 500000) == 0
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996],cost1 = 1,cost2 = 1) == 5
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],cost1 = 10,cost2 = 5) == 1170
    assert candidate(nums = [100, 200, 300, 400, 500],cost1 = 10,cost2 = 20) == 10000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],cost1 = 2,cost2 = 4) == 210
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost1 = 5,cost2 = 3) == 285
    assert candidate(nums = [5, 4, 3, 2, 1],cost1 = 5,cost2 = 10) == 50
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],cost1 = 50,cost2 = 20) == 45000
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost1 = 100,cost2 = 50) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost1 = 100,cost2 = 200) == 4500
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625],cost1 = 2,cost2 = 4) == 10031250
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],cost1 = 1000,cost2 = 500) == 12000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost1 = 20,cost2 = 10) == 950
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],cost1 = 7,cost2 = 11) == 110
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost1 = 1000000,cost2 = 500000) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],cost1 = 5,cost2 = 10) == 5250
    assert candidate(nums = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6],cost1 = 5,cost2 = 2) == 32
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost1 = 10,cost2 = 20) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],cost1 = 500000,cost2 = 1000000) == 52500000
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],cost1 = 2,cost2 = 1) == 105
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],cost1 = 2,cost2 = 1) == 10
    assert candidate(nums = [5, 3, 1, 2, 4],cost1 = 7,cost2 = 3) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost1 = 10,cost2 = 20) == 1900
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost1 = 3,cost2 = 5) == 113
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],cost1 = 4,cost2 = 8) == 64
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],cost1 = 1,cost2 = 2) == 90
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],cost1 = 50,cost2 = 25) == 600
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996],cost1 = 1000,cost2 = 500) == 2500
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],cost1 = 2,cost2 = 4) == 20
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],cost1 = 1,cost2 = 1) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost1 = 10,cost2 = 5) == 120
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost1 = 1,cost2 = 2) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost1 = 50,cost2 = 25) == 5625
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],cost1 = 3,cost2 = 5) == 180
    assert candidate(nums = [1, 3, 5, 7, 9],cost1 = 2,cost2 = 4) == 40
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost1 = 1000,cost2 = 500) == 112500
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],cost1 = 1,cost2 = 2) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost1 = 1,cost2 = 2) == 0
    assert candidate(nums = [100, 200, 300, 400, 500],cost1 = 1000,cost2 = 500) == 250000
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],cost1 = 1000000,cost2 = 500000) == 12000000
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],cost1 = 4,cost2 = 8) == 760
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost1 = 1,cost2 = 1) == 225
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990],cost1 = 10,cost2 = 5) == 120
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],cost1 = 7,cost2 = 6) == 60
    assert candidate(nums = [1, 1000000, 1, 1000000, 1, 1000000],cost1 = 500000,cost2 = 250000) == 999997382
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5],cost1 = 7,cost2 = 3) == 45
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost1 = 1,cost2 = 2) == 0
    assert candidate(nums = [100, 200, 300, 400, 500],cost1 = 10,cost2 = 15) == 7500
    assert candidate(nums = [1, 3, 5, 7, 9],cost1 = 1000000,cost2 = 500000) == 5000000
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],cost1 = 1000,cost2 = 500) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost1 = 1000,cost2 = 500) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],cost1 = 10,cost2 = 3) == 30
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],cost1 = 5,cost2 = 2) == 450
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],cost1 = 1,cost2 = 1) == 105
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],cost1 = 1,cost2 = 1) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],cost1 = 10,cost2 = 20) == 300
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],cost1 = 1,cost2 = 2) == 45
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],cost1 = 100,cost2 = 50) == 30700
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],cost1 = 2,cost2 = 1) == 525
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],cost1 = 10,cost2 = 5) == 50
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991],cost1 = 1,cost2 = 2) == 45
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],cost1 = 5,cost2 = 2) == 49
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],cost1 = 1000000,cost2 = 500000) == 27000000
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],cost1 = 6,cost2 = 3) == 207
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost1 = 1,cost2 = 2) == 0
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5],cost1 = 3,cost2 = 5) == 100
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],cost1 = 2,cost2 = 4) == 0
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000],cost1 = 10000,cost2 = 5000) == 499999986
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],cost1 = 100,cost2 = 50) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],cost1 = 1,cost2 = 1) == 83
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],cost1 = 10,cost2 = 5) == 2625
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],cost1 = 1000,cost2 = 500) == 4500
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],cost1 = 1,cost2 = 2) == 0
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],cost1 = 100,cost2 = 50) == 112500000
    assert candidate(nums = [7, 7, 8, 8, 8, 9, 9, 9, 9, 9],cost1 = 5,cost2 = 3) == 14
