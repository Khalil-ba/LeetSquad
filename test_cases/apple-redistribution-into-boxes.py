# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(apple = [10, 20, 30],capacity = [15, 10, 25]) == None
    assert candidate(apple = [10, 20, 30, 40],capacity = [10, 10, 10, 10, 10, 10, 10]) == None
    assert candidate(apple = [45, 5],capacity = [50]) == 1
    assert candidate(apple = [1, 1, 1, 1, 1],capacity = [1, 1, 1, 1, 1, 1]) == 5
    assert candidate(apple = [10, 20, 30],capacity = [5, 15, 10, 20]) == None
    assert candidate(apple = [2, 2, 2, 2],capacity = [1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(apple = [1, 1, 1, 1],capacity = [1, 1, 1, 1, 1]) == 4
    assert candidate(apple = [2, 2, 2, 2, 2],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(apple = [1, 1, 1, 1, 1],capacity = [1, 1, 1, 1, 1]) == 5
    assert candidate(apple = [40, 10, 10],capacity = [20, 20, 20]) == 3
    assert candidate(apple = [25, 25],capacity = [30, 20]) == 2
    assert candidate(apple = [1, 1, 1, 1],capacity = [1, 1, 1, 1, 1, 1]) == 4
    assert candidate(apple = [5, 5, 5],capacity = [2, 4, 2, 7]) == 4
    assert candidate(apple = [45, 3, 2],capacity = [50, 1, 1, 1]) == 1
    assert candidate(apple = [15, 15, 15],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9
    assert candidate(apple = [3, 5, 7, 9],capacity = [2, 4, 6, 8, 10]) == 3
    assert candidate(apple = [10, 20, 30],capacity = [5, 10, 15, 25]) == None
    assert candidate(apple = [1, 3, 2],capacity = [4, 3, 1, 5, 2]) == 2
    assert candidate(apple = [50],capacity = [50]) == 1
    assert candidate(apple = [10, 20, 30],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == None
    assert candidate(apple = [25, 25, 25, 25, 25],capacity = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == None
    assert candidate(apple = [48, 48, 48],capacity = [16, 16, 16, 16, 16, 16]) == None
    assert candidate(apple = [25, 25, 25],capacity = [10, 10, 10, 10, 10, 10, 10]) == None
    assert candidate(apple = [49, 1, 1],capacity = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]) == 3
    assert candidate(apple = [15, 20, 5],capacity = [12, 18, 9, 7]) == 4
    assert candidate(apple = [1, 2, 3, 4, 5],capacity = [2, 3, 4, 5, 6]) == 3
    assert candidate(apple = [25, 25, 25, 25, 25],capacity = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 13
    assert candidate(apple = [50, 40, 30, 20, 10],capacity = [10, 20, 30, 40, 50]) == 5
    assert candidate(apple = [48, 1, 1],capacity = [24, 24, 1, 1, 1]) == 4
    assert candidate(apple = [25, 25, 25, 25],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == None
    assert candidate(apple = [40, 30, 20, 10],capacity = [50, 20, 10, 10, 10]) == 5
    assert candidate(apple = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 1
    assert candidate(apple = [15, 25, 35],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == None
    assert candidate(apple = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(apple = [15, 25, 35, 45],capacity = [10, 20, 30, 40, 50]) == 3
    assert candidate(apple = [30, 20, 10, 40],capacity = [10, 15, 5, 25, 30, 5]) == None
    assert candidate(apple = [50, 50, 50],capacity = [16, 17, 18, 19, 20]) == None
    assert candidate(apple = [1, 2, 3, 4, 5],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 15
    assert candidate(apple = [2, 3, 5, 7, 11, 13],capacity = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 2
    assert candidate(apple = [10, 20, 30, 40],capacity = [10, 20, 30, 40, 50]) == 3
    assert candidate(apple = [30, 10, 5],capacity = [15, 10, 10, 5, 5]) == 5
    assert candidate(apple = [3, 6, 9, 12],capacity = [2, 4, 6, 8, 10, 12, 14]) == 3
    assert candidate(apple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacity = [5, 10, 15, 20, 25]) == 3
    assert candidate(apple = [25, 25, 25],capacity = [20, 15, 30, 10, 25]) == 3
    assert candidate(apple = [45, 35, 25],capacity = [20, 15, 10, 5, 5, 5]) == None
    assert candidate(apple = [49, 49, 49],capacity = [50, 50, 50, 50, 50, 50]) == 3
    assert candidate(apple = [30, 30, 30],capacity = [25, 25, 25, 25]) == 4
    assert candidate(apple = [10, 20, 30, 40],capacity = [15, 25, 35, 5, 5, 5]) == None
    assert candidate(apple = [10, 20, 30, 40, 50],capacity = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == None
    assert candidate(apple = [10, 20, 30],capacity = [5, 15, 10, 25]) == None
    assert candidate(apple = [45, 45, 5],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == None
    assert candidate(apple = [40, 30, 20, 10],capacity = [15, 15, 15, 15, 15, 15]) == None
    assert candidate(apple = [30, 20, 10],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == None
    assert candidate(apple = [25, 25, 25],capacity = [10, 10, 10, 10, 10, 10, 10, 10]) == 8
    assert candidate(apple = [15, 15, 15, 15],capacity = [10, 10, 10, 10, 10]) == None
    assert candidate(apple = [49, 1, 1],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 51
    assert candidate(apple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == None
    assert candidate(apple = [50, 40, 30, 20, 10],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == None
    assert candidate(apple = [3, 6, 9, 12, 15],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6
    assert candidate(apple = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],capacity = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 4
    assert candidate(apple = [2, 3, 5, 7, 11],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(apple = [45, 5, 3, 7],capacity = [12, 8, 15, 10, 2]) == None
    assert candidate(apple = [49, 1],capacity = [50]) == 1
    assert candidate(apple = [5, 5, 5, 5, 5, 5, 5],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 35
    assert candidate(apple = [10, 10, 10],capacity = [5, 5, 5, 5, 5, 5]) == 6
    assert candidate(apple = [50, 45, 40],capacity = [10, 20, 15, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == None
    assert candidate(apple = [1, 1, 2, 2, 3, 3, 4, 4],capacity = [1, 2, 3, 4, 5, 6, 7, 8]) == 3
    assert candidate(apple = [1, 2, 3, 4, 5, 6],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(apple = [7, 8, 9],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3
    assert candidate(apple = [49, 49, 49, 49, 49],capacity = [50, 50, 50, 50, 50]) == 5
    assert candidate(apple = [10, 20, 30, 40, 50],capacity = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 4
    assert candidate(apple = [9, 11, 13, 17],capacity = [8, 15, 7, 10, 6, 12]) == 5
    assert candidate(apple = [48, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 18
    assert candidate(apple = [49, 1],capacity = [25, 24, 1]) == 3
    assert candidate(apple = [40, 30, 20],capacity = [10, 10, 10, 10, 10, 10, 10, 10]) == None
    assert candidate(apple = [20, 20, 10, 10],capacity = [15, 15, 15, 15, 15]) == 4
    assert candidate(apple = [25, 25, 25],capacity = [50, 50]) == 2
    assert candidate(apple = [45, 2, 3],capacity = [10, 10, 10, 10, 10]) == 5
    assert candidate(apple = [10, 20, 30],capacity = [5, 15, 25, 10]) == None
    assert candidate(apple = [10, 20, 30],capacity = [5, 15, 20, 10]) == None
    assert candidate(apple = [3, 7, 2, 8],capacity = [5, 10, 3, 6, 1]) == 3
    assert candidate(apple = [25, 25, 25, 25],capacity = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(apple = [8, 16, 32, 64],capacity = [32, 32, 32, 32, 32, 32]) == 4
    assert candidate(apple = [40, 40, 40, 40],capacity = [20, 20, 20, 20, 20, 20, 20, 20]) == 8
    assert candidate(apple = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 49
    assert candidate(apple = [10, 20, 30, 40],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(apple = [49, 49, 49],capacity = [16, 16, 16, 16, 16, 16]) == None
    assert candidate(apple = [50, 50, 50, 50, 50],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 6
    assert candidate(apple = [15, 25, 10, 5],capacity = [10, 20, 5, 5, 5, 5]) == None
    assert candidate(apple = [23, 17, 15, 12],capacity = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 7
    assert candidate(apple = [5, 10, 15, 20, 25],capacity = [30, 20, 10, 5, 1, 1, 1, 1]) == None
    assert candidate(apple = [4, 4, 4, 4, 4],capacity = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 7
    assert candidate(apple = [45, 3, 2, 1],capacity = [40, 5, 3, 2, 1, 1, 1, 1, 1]) == 5
    assert candidate(apple = [45, 5, 5],capacity = [25, 20, 5, 5, 5, 5]) == 4
    assert candidate(apple = [10, 10, 10, 10, 10],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 10
    assert candidate(apple = [1, 2, 3, 4, 5],capacity = [15, 10, 5]) == 1
    assert candidate(apple = [3, 3, 3, 3, 3, 3],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 18
    assert candidate(apple = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == None
    assert candidate(apple = [10, 20, 30, 40],capacity = [20, 20, 20, 20, 20]) == 5
    assert candidate(apple = [1, 2, 3, 4, 5],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == None
    assert candidate(apple = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 20
    assert candidate(apple = [45, 3, 2],capacity = [50, 25, 10, 5]) == 1
    assert candidate(apple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacity = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 11
    assert candidate(apple = [45, 45, 45],capacity = [15, 15, 15, 15, 15, 15]) == None
    assert candidate(apple = [10, 20, 30],capacity = [5, 15, 10, 20, 25]) == 3
    assert candidate(apple = [50, 50, 50],capacity = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == None
    assert candidate(apple = [45, 30, 10, 5],capacity = [20, 15, 10, 5, 1]) == None
    assert candidate(apple = [10, 20, 30],capacity = [5, 15, 25, 35]) == 2
    assert candidate(apple = [8, 16, 24, 32],capacity = [4, 8, 12, 16, 20, 24, 28, 32]) == 3
    assert candidate(apple = [45, 30, 15],capacity = [10, 10, 10, 10, 10, 10]) == None
    assert candidate(apple = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],capacity = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 30
    assert candidate(apple = [40, 10, 10],capacity = [20, 20, 20, 20, 20, 20]) == 3
    assert candidate(apple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],capacity = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(apple = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(apple = [10, 20, 30, 40],capacity = [5, 10, 15, 20, 25, 30]) == 5
