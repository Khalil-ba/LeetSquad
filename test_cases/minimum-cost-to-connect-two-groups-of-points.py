# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]) == 10
    assert candidate(cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]) == 4
    assert candidate(cost = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 16
    assert candidate(cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 13
    assert candidate(cost = [[15, 96], [36, 2]]) == 17
    assert candidate(cost = [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]) == 40
    assert candidate(cost = [[10, 20], [30, 40], [50, 60]]) == 100
    assert candidate(cost = [[5, 5, 5], [5, 5, 5]]) == 15
