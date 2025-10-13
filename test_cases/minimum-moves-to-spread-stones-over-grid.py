# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(grid = [[2, 2, 1], [1, 1, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[0, 0, 9], [0, 0, 0], [0, 0, 0]]) == 18
    assert candidate(grid = [[2, 2, 1], [1, 1, 1], [1, 1, 2]]) == 0
    assert candidate(grid = [[1, 3, 0], [1, 0, 0], [1, 0, 3]]) == 4
    assert candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]) == 0
    assert candidate(grid = [[1, 1, 1], [1, 2, 2], [2, 2, 1]]) == 0
    assert candidate(grid = [[1, 2, 2], [2, 1, 1], [2, 1, 1]]) == 0
    assert candidate(grid = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]) == 8
    assert candidate(grid = [[1, 1, 0], [1, 1, 1], [1, 2, 1]]) == 3
    assert candidate(grid = [[0, 0, 0], [0, 9, 0], [0, 0, 0]]) == 12
    assert candidate(grid = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[3, 1, 1], [0, 0, 0], [1, 1, 3]]) == 4
    assert candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 9]]) == 18
    assert candidate(grid = [[1, 0, 0], [0, 0, 0], [0, 0, 8]]) == 14
    assert candidate(grid = [[2, 2, 0], [1, 0, 2], [0, 1, 1]]) == 4
    assert candidate(grid = [[0, 1, 0], [1, 0, 0], [0, 0, 7]]) == 12
    assert candidate(grid = [[0, 1, 2], [3, 0, 0], [0, 0, 3]]) == 6
    assert candidate(grid = [[0, 0, 0], [0, 0, 2], [0, 0, 7]]) == 16
    assert candidate(grid = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]) == 4
    assert candidate(grid = [[2, 1, 0], [1, 1, 1], [0, 1, 2]]) == 4
    assert candidate(grid = [[2, 0, 1], [1, 0, 3], [0, 3, 0]]) == 4
    assert candidate(grid = [[4, 0, 1], [0, 0, 0], [1, 0, 3]]) == 6
    assert candidate(grid = [[1, 0, 2], [2, 0, 0], [0, 1, 3]]) == 5
    assert candidate(grid = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]) == 4
    assert candidate(grid = [[0, 2, 0], [3, 0, 0], [0, 1, 3]]) == 6
    assert candidate(grid = [[3, 0, 0], [0, 0, 3], [0, 3, 0]]) == 6
    assert candidate(grid = [[0, 0, 1], [1, 7, 0], [0, 0, 1]]) == 7
    assert candidate(grid = [[2, 2, 2], [1, 1, 1], [0, 0, 0]]) == 6
    assert candidate(grid = [[1, 1, 0], [0, 0, 0], [0, 0, 7]]) == 11
    assert candidate(grid = [[1, 2, 0], [0, 1, 2], [2, 0, 1]]) == 4
    assert candidate(grid = [[0, 2, 0], [1, 0, 3], [0, 4, 0]]) == 5
    assert candidate(grid = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]) == 6
    assert candidate(grid = [[0, 0, 0], [0, 8, 1], [0, 0, 0]]) == 11
    assert candidate(grid = [[0, 1, 0], [0, 7, 0], [0, 1, 0]]) == 10
    assert candidate(grid = [[1, 2, 0], [2, 0, 1], [0, 3, 0]]) == 4
    assert candidate(grid = [[1, 2, 2], [2, 1, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[2, 2, 0], [1, 1, 0], [0, 0, 3]]) == 5
    assert candidate(grid = [[2, 2, 1], [1, 0, 1], [1, 1, 2]]) == 1
