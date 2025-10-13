# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(mat = [[0, 0], [0, 1]]) == 3
    assert candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 5
    assert candidate(mat = [[1, 1], [1, 1]]) == 4
    assert candidate(mat = [[0]]) == 0
    assert candidate(mat = [[1, 1, 0], [0, 0, 0], [0, 0, 1]]) == 6
    assert candidate(mat = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]) == 4
    assert candidate(mat = [[1, 0, 0], [1, 0, 0]]) == -1
    assert candidate(mat = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]) == -1
    assert candidate(mat = [[1, 0, 1, 1], [0, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]) == -1
    assert candidate(mat = [[1, 1, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == -1
    assert candidate(mat = [[1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == -1
    assert candidate(mat = [[1, 0, 1, 1], [0, 1, 0, 0], [1, 0, 1, 1], [0, 0, 0, 1]]) == -1
    assert candidate(mat = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]) == 4
    assert candidate(mat = [[0, 1, 1], [1, 1, 0], [1, 0, 1]]) == 8
    assert candidate(mat = [[1, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0]]) == -1
    assert candidate(mat = [[1, 1, 0, 1], [0, 0, 0, 1], [1, 0, 1, 1], [0, 1, 1, 0]]) == -1
    assert candidate(mat = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0]]) == -1
    assert candidate(mat = [[1, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1]]) == -1
    assert candidate(mat = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]) == 4
    assert candidate(mat = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]) == 4
    assert candidate(mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0
    assert candidate(mat = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 6
    assert candidate(mat = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == -1
    assert candidate(mat = [[1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0]]) == 7
    assert candidate(mat = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 9
    assert candidate(mat = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]) == 3
    assert candidate(mat = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]) == 1
    assert candidate(mat = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]) == 2
    assert candidate(mat = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]) == 2
    assert candidate(mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 4
    assert candidate(mat = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]) == 5
    assert candidate(mat = [[1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 8
    assert candidate(mat = [[1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1]]) == 6
    assert candidate(mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 8
    assert candidate(mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0
    assert candidate(mat = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == -1
    assert candidate(mat = [[0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1]]) == 5
    assert candidate(mat = [[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]]) == -1
    assert candidate(mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]]) == 9
    assert candidate(mat = [[0, 0, 1, 1], [0, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 0]]) == -1
    assert candidate(mat = [[0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == -1
    assert candidate(mat = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]) == 5
    assert candidate(mat = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 7
    assert candidate(mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert candidate(mat = [[0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0]]) == -1
    assert candidate(mat = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == -1
    assert candidate(mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 5
    assert candidate(mat = [[1, 0, 1, 1], [0, 1, 0, 0], [1, 0, 1, 1], [0, 0, 0, 0]]) == -1
    assert candidate(mat = [[1, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == -1
    assert candidate(mat = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]) == 6
    assert candidate(mat = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]) == 2
    assert candidate(mat = [[1, 1, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]) == -1
    assert candidate(mat = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]) == 3
