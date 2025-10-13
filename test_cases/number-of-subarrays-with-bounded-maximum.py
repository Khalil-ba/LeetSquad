# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [5, 2, 1],left = 1,right = 5) == 6
    assert candidate(nums = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52],left = 32,right = 69) == 22
    assert candidate(nums = [2, 1, 4, 3],left = 2,right = 3) == 3
    assert candidate(nums = [8, 2, 4, 4, 4, 6, 7, 7, 7, 8],left = 4,right = 6) == 14
    assert candidate(nums = [10, 20, 30, 40, 50],left = 15,right = 45) == 9
    assert candidate(nums = [5, 2, 4, 5, 5, 5, 6, 5, 5, 5],left = 4,right = 5) == 26
    assert candidate(nums = [2, 9, 2, 5, 6],left = 2,right = 8) == 7
    assert candidate(nums = [5, 5, 5, 5, 5],left = 5,right = 5) == 15
    assert candidate(nums = [10, 20, 30],left = 25,right = 25) == 0
    assert candidate(nums = [1, 2, 3],left = 1,right = 3) == 6
    assert candidate(nums = [10, 20, 30, 40, 50],left = 20,right = 40) == 9
    assert candidate(nums = [1, 2, 3, 4, 5],left = 2,right = 4) == 9
    assert candidate(nums = [5, 5, 5, 5, 5],left = 5,right = 5) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50],left = 30,right = 80) == 43
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 9, 3, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5],left = 5,right = 10) == 2028
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],left = 10,right = 20) == 0
    assert candidate(nums = [10, 5, 3, 15, 7, 9, 20, 1],left = 5,right = 10) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],left = 1,right = 10) == 55
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],left = 0,right = 2) == 210
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],left = 5,right = 15) == 33
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],left = 4,right = 12) == 18
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13],left = 4,right = 10) == 12
    assert candidate(nums = [8, 1, 6, 3, 5, 7, 2, 9, 4, 10],left = 3,right = 7) == 20
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],left = 3,right = 6) == 49
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],left = 3,right = 7) == 25
    assert candidate(nums = [2, 3, 2, 1, 2, 3, 4, 3, 2, 1],left = 2,right = 3) == 25
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],left = 50,right = 950) == 45
    assert candidate(nums = [3, 2, 1, 4, 3, 5, 4, 3, 2, 1],left = 2,right = 4) == 23
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],left = 4,right = 8) == 35
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],left = 1,right = 2) == 55
    assert candidate(nums = [100, 200, 300, 400, 500],left = 150,right = 350) == 5
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],left = 2,right = 2) == 53
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],left = 3,right = 8) == 21
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],left = 1,right = 5) == 120
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],left = 7,right = 7) == 55
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],left = 10,right = 100) == 55
    assert candidate(nums = [7, 4, 7, 2, 5, 3, 6],left = 4,right = 6) == 9
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],left = 6,right = 12) == 15
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],left = 5,right = 5) == 0
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],left = 6,right = 14) == 25
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],left = 1,right = 3) == 27
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],left = 25,right = 75) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],left = 1,right = 1) == 55
    assert candidate(nums = [5, 4, 3, 2, 1],left = 2,right = 4) == 9
    assert candidate(nums = [3, 7, 2, 5, 4, 6, 1, 8, 9],left = 4,right = 7) == 25
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],left = 0,right = 0) == 55
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],left = 4,right = 8) == 30
    assert candidate(nums = [4, 2, 7, 3, 6, 5, 8, 1, 9, 0],left = 3,right = 7) == 20
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],left = 400,right = 800) == 30
    assert candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10],left = 5,right = 10) == 36
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],left = 5,right = 10) == 12
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5],left = 5,right = 15) == 66
    assert candidate(nums = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],left = 10,right = 15) == 27
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],left = 1,right = 3) == 55
    assert candidate(nums = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10],left = 3,right = 8) == 33
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],left = 10,right = 20) == 165
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1],left = 3,right = 6) == 18
    assert candidate(nums = [3, 2, 1, 2, 3, 2, 1, 2, 3],left = 2,right = 3) == 43
    assert candidate(nums = [7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],left = 5,right = 9) == 45
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],left = 4,right = 8) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],left = 5,right = 15) == 110
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],left = 5,right = 10) == 45
    assert candidate(nums = [1, 4, 2, 3, 5, 6, 7, 8, 9, 10],left = 3,right = 8) == 34
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],left = 1,right = 4) == 44
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],left = 5,right = 10) == 210
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6],left = 3,right = 5) == 39
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],left = 2,right = 8) == 42
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],left = 8,right = 8) == 55
    assert candidate(nums = [1, 3, 5, 2, 4, 6, 8, 7],left = 2,right = 6) == 20
    assert candidate(nums = [3, 4, 2, 2, 2, 2, 2, 4, 3, 1],left = 2,right = 3) == 18
    assert candidate(nums = [1000000000, 999999999, 1000000000, 999999999, 1000000000],left = 500000000,right = 1500000000) == 15
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],left = 200,right = 800) == 35
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],left = 1,right = 1) == 120
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],left = 15,right = 95) == 44
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],left = 5,right = 9) == 55
    assert candidate(nums = [100, 200, 300, 400, 500],left = 150,right = 450) == 9
    assert candidate(nums = [5, 4, 3, 2, 1],left = 1,right = 3) == 6
    assert candidate(nums = [5, 1, 4, 3, 2, 5, 6, 7, 8, 5],left = 3,right = 6) == 27
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],left = 250,right = 750) == 25
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],left = 3,right = 7) == 25
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],left = 2,right = 4) == 55
    assert candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],left = 10,right = 15) == 39
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],left = 2,right = 4) == 33
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],left = 4,right = 7) == 22
    assert candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5],left = 5,right = 5) == 50
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],left = 3,right = 7) == 25
    assert candidate(nums = [3, 7, 2, 5, 9, 1, 6],left = 3,right = 7) == 11
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],left = 100,right = 1000) == 55
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],left = 5,right = 10) == 55
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],left = 5,right = 5) == 210
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],left = 4,right = 10) == 12
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13],left = 2,right = 10) == 14
    assert candidate(nums = [10, 12, 8, 7, 5, 4, 3, 11, 6, 10],left = 5,right = 10) == 16
    assert candidate(nums = [7, 1, 8, 2, 3, 8, 4, 5, 6, 8, 7, 1, 2],left = 3,right = 7) == 13
    assert candidate(nums = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],left = 50,right = 150) == 50
    assert candidate(nums = [5, 8, 1, 4, 9, 7, 6, 3, 2, 10],left = 4,right = 7) == 10
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],left = 5,right = 10) == 45
    assert candidate(nums = [10, 20, 30, 40, 50],left = 25,right = 45) == 7
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],left = 6,right = 8) == 55
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],left = 2,right = 2) == 8
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],left = 0,right = 1) == 120
