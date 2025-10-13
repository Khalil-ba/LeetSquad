# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1, 4, 4, 1, 3, 5, 5, 3],pattern = [1, 0, -1]) == 2
    assert candidate(nums = [1, 3, 2, 3, 1, 2],pattern = [1, -1, 1, -1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6],pattern = [1, 1]) == 4
    assert candidate(nums = [1, 1, 1, 1, 1],pattern = [0, 0, 0]) == 2
    assert candidate(nums = [5, 4, 3, 2, 1],pattern = [-1, -1, -1]) == 2
    assert candidate(nums = [1, 2, 2, 3, 4, 3, 5],pattern = [1, 0, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 2, 3, 4],pattern = [1, -1, 1]) == 1
    assert candidate(nums = [1, 2, 2, 3, 4, 4, 5],pattern = [1, 0, 1, 0]) == 0
    assert candidate(nums = [3, 5, 2, 8, 6, 4, 7],pattern = [1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17],pattern = [1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, 1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],pattern = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 4
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5],pattern = [-1, -1, -1, -1, 1, 1, 1]) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [2, 1, 3, 1, 4, 1, 5, 1, 6],pattern = [-1, 1, -1, 1, -1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],pattern = [1, 1, -1, -1, 1, 1]) == 0
    assert candidate(nums = [100, 200, 150, 150, 200, 250, 300, 200, 100, 100, 200, 300, 400, 500, 600],pattern = [1, -1, 0, 1, 1, -1, 1, 0, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],pattern = [1, -1, 1, -1, 1, -1, 1]) == 2
    assert candidate(nums = [1, 3, 5, 3, 1, 3, 5, 3, 1],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 0
    assert candidate(nums = [10, 20, 15, 15, 20, 25, 30, 20, 10],pattern = [1, -1, 0, 1, 1, -1]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5],pattern = [0, 0, 0, 0, 0, 0, 0]) == 2
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],pattern = [0, 0, 1, 0, 0, 1, 0, 0, 1]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0]) == 3
    assert candidate(nums = [1, 3, 2, 2, 4, 3, 3, 5, 4, 4],pattern = [1, -1, 0, 1, -1, 0, 1, -1]) == 1
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],pattern = [-1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10],pattern = [0, 0, 0, 0, 0, 0]) == 2
    assert candidate(nums = [10, 10, 10, 10, 10, 10],pattern = [0, 0, 0]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0]) == 7
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1, 0]) == 2
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8],pattern = [1, -1, 1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5],pattern = [1, -1, 1, -1, 1, 1]) == 0
    assert candidate(nums = [2, 1, 3, 4, 3, 5, 6, 5, 7, 8],pattern = [-1, 1, 1, -1, 1, 1, -1, 1]) == 1
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 7, 8],pattern = [1, -1, 1, 1, 0]) == 0
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],pattern = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],pattern = [0, 0, 0, 0, 0, 0, 0]) == 3
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 4, 3, 5, 7],pattern = [1, -1, 1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 4, 3, 2, 1, 2, 3, 4],pattern = [1, -1, 1, 0, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 3, 4, 5, 6, 5, 4],pattern = [1, 1, -1, 1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7],pattern = [1, -1, 1, 0, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],pattern = [1, -1, 1, 1, -1, 1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6],pattern = [1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(nums = [10, 10, 10, 10, 10],pattern = [0, 0, 0]) == 2
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [10, 20, 15, 10, 15, 25, 30, 20],pattern = [1, -1, 1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],pattern = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 2
    assert candidate(nums = [1, 2, 2, 1, 1, 2, 2, 1, 1],pattern = [1, 0, -1, 0, 1, 0, -1]) == 1
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],pattern = [0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(nums = [10, 20, 15, 15, 25, 30, 20, 10, 5],pattern = [1, -1, 0, 1, -1, -1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 5, 4, 3, 2, 1],pattern = [1, -1, 1, 1, -1, 1, -1, -1]) == 0
    assert candidate(nums = [10, 20, 30, 20, 10, 5, 15, 25, 35, 25, 15],pattern = [1, 1, -1, -1, 1, 1, 1, -1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],pattern = [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],pattern = [1, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],pattern = [1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7],pattern = [1, 0, 1, 0, 1, 0, 1, 0, 1]) == 2
    assert candidate(nums = [5, 3, 8, 6, 7, 4, 9, 10, 11, 10, 9],pattern = [-1, 1, 1, -1, 1, 1, -1, -1]) == 0
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1],pattern = [1, -1, 1, -1, 1, -1, 1]) == 1
    assert candidate(nums = [100, 200, 150, 100, 50, 100, 150, 200, 250, 300],pattern = [1, -1, 1, 1, 1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],pattern = [0, 0, 0, 0, 0]) == 5
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],pattern = [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6],pattern = [1, 1, -1, -1, 1, 1, 1]) == 0
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],pattern = [1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 3, 2, 3, 4, 5, 4, 3, 2],pattern = [1, -1, 1, 1, -1, -1, 1]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],pattern = [-1, -1, -1, -1, -1, -1, -1]) == 3
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1],pattern = [0, 1, 0, -1, 0, 1, 0, -1]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],pattern = [0, 1, 0, 1, 0, 1, 0]) == 2
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 2
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 3, 4, 5, 6, 5, 6],pattern = [1, 1, -1, 1, 1, -1, 1]) == 0
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],pattern = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 4
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5],pattern = [1, 1, 1, -1, -1, -1, -1, -1, -1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 8],pattern = [1, -1, 1, 1, 0]) == 0
    assert candidate(nums = [9, 8, 7, 8, 7, 8, 7, 8, 7, 8],pattern = [-1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1]) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 4, 5, 6, 7, 5, 6, 7, 8, 9, 7, 8, 9, 10, 11],pattern = [1, -1, 1, 1, 0, -1, 1, 1, 0, -1, 1, 1, 0, -1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, 2, 2, 3, 3],pattern = [1, 0, 1, 0, -1, 0, -1, 0, 1]) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9],pattern = [1, 0, 1, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1, -1]) == 2
    assert candidate(nums = [10, 10, 10, 10, 10],pattern = [0, 0, 0, 0]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],pattern = [1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],pattern = [1, 1, -1, -1, 1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7],pattern = [1, -1, 1, 1, 1, 1, 0]) == 0
    assert candidate(nums = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3],pattern = [1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 5],pattern = [1, 0, 1, 0, 1]) == 1
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7],pattern = [0, 0, 0, 0, 0, 0, 0]) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],pattern = [-1, -1, -1, -1, -1, -1, -1]) == 3
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],pattern = [-1, -1, -1, -1, -1, -1, -1]) == 3
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5],pattern = [1, -1, 1, 0, -1, 1, 0, 1]) == 0
    assert candidate(nums = [3, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1],pattern = [0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1]) == 0
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],pattern = [1, -1, 1, -1, 1, -1]) == 2
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20],pattern = [1, -1, 1, -1, 1]) == 2
    assert candidate(nums = [1, 3, 1, 5, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1, 17, 1, 19],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, 3, 2, 3, 1, 3, 2, 3, 1, 3, 2, 3],pattern = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, 2, 3, 2, 3, 4, 5, 4],pattern = [1, -1, 1, 1]) == 1
