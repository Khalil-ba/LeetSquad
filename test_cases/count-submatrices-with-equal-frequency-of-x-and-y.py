# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(grid = [['X', 'Y', 'X'], ['Y', 'X', 'Y'], ['X', 'Y', 'X']]) == 5
    assert candidate(grid = [['.', '.'], ['.', '.']]) == 0
    assert candidate(grid = [['X', 'X'], ['X', 'Y']]) == 0
    assert candidate(grid = [['X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X']]) == 5
    assert candidate(grid = [['X', 'X', 'X', 'X'], ['X', 'Y', 'Y', 'X'], ['X', 'Y', 'Y', 'X'], ['X', 'X', 'X', 'X']]) == 0
    assert candidate(grid = [['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y']]) == 8
    assert candidate(grid = [['X', '.', 'Y'], ['.', 'X', 'Y'], ['Y', '.', 'X']]) == 4
    assert candidate(grid = [['X'], ['Y'], ['X']]) == 1
    assert candidate(grid = [['X', 'Y', '.'], ['Y', '.', '.']]) == 3
    assert candidate(grid = [['X', 'Y'], ['X', 'Y'], ['X', 'Y']]) == 3
    assert candidate(grid = [['X', 'X', 'Y'], ['Y', 'Y', 'X'], ['X', 'Y', 'X']]) == 4
    assert candidate(grid = [['X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y']]) == 6
    assert candidate(grid = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]) == 0
    assert candidate(grid = [['X', 'Y'], ['Y', 'X']]) == 3
    assert candidate(grid = [['X', 'X', 'X'], ['Y', 'Y', 'Y'], ['.', '.', '.']]) == 6
    assert candidate(grid = [['X', '.', 'Y'], ['.', 'X', '.'], ['Y', '.', 'X']]) == 2
    assert candidate(grid = [['X', 'Y', '.'], ['.', 'X', 'Y'], ['Y', 'X', '.']]) == 5
    assert candidate(grid = [['X', 'Y', 'X'], ['X', 'Y', 'X'], ['X', 'Y', 'X']]) == 3
    assert candidate(grid = [['X', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'Y']]) == 19
    assert candidate(grid = [['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y']]) == 0
    assert candidate(grid = [['X', 'Y', 'X'], ['Y', '.', 'X'], ['X', 'Y', '.']]) == 2
    assert candidate(grid = [['.', '.', '.', 'X', 'Y'], ['.', 'X', 'Y', '.', '.'], ['.', 'Y', 'X', '.', '.'], ['X', '.', '.', 'Y', '.'], ['Y', '.', '.', '.', 'X']]) == 12
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X']]) == 15
    assert candidate(grid = [['X', 'X', 'X'], ['Y', 'Y', 'Y'], ['X', 'Y', 'X'], ['Y', 'X', 'Y']]) == 7
    assert candidate(grid = [['X', 'Y', 'X', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'X', 'Y'], ['X', 'X', 'Y', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y']]) == 6
    assert candidate(grid = [['X', 'Y', 'Y', 'X'], ['Y', 'X', 'X', 'Y'], ['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X']]) == 12
    assert candidate(grid = [['X', '.', 'X', 'Y'], ['Y', 'X', 'Y', '.'], ['.', 'Y', 'X', 'X'], ['X', 'Y', '.', 'Y']]) == 6
    assert candidate(grid = [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 0
    assert candidate(grid = [['.', '.', 'X', 'Y', '.'], ['X', 'Y', '.', 'X', 'Y'], ['Y', 'X', 'X', 'Y', 'X'], ['.', 'Y', 'X', '.', 'Y'], ['X', '.', 'Y', 'X', '.']]) == 9
    assert candidate(grid = [['X', 'X', 'X', 'Y'], ['Y', 'Y', 'X', 'X'], ['X', 'Y', 'X', 'X'], ['Y', 'X', 'Y', 'Y']]) == 5
    assert candidate(grid = [['X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'Y'], ['X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'Y']]) == 8
    assert candidate(grid = [['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X']]) == 12
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 13
    assert candidate(grid = [['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']]) == 6
    assert candidate(grid = [['X', '.', '.', 'Y', '.', '.', 'X', '.', 'Y', '.'], ['.', 'X', '.', '.', 'Y', '.', '.', 'X', '.', 'Y'], ['.', '.', 'X', '.', '.', 'Y', '.', '.', 'X', '.'], ['Y', '.', '.', 'X', '.', '.', 'Y', '.', '.', 'X']]) == 12
    assert candidate(grid = [['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y']]) == 12
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X']]) == 16
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 16
    assert candidate(grid = [['X', 'Y', '.', 'X'], ['Y', 'X', '.', 'Y'], ['.', '.', '.', '.'], ['X', 'Y', 'X', 'Y']]) == 12
    assert candidate(grid = [['X', 'Y', 'Y', 'Y'], ['X', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y'], ['X', 'X', 'X', 'X']]) == 5
    assert candidate(grid = [['.', '.', 'X'], ['Y', 'X', 'Y'], ['X', 'Y', 'X'], ['Y', '.', 'Y']]) == 4
    assert candidate(grid = [['X', '.', 'Y', 'X'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', '.'], ['.', 'X', 'Y', 'X']]) == 4
    assert candidate(grid = [['.', '.', '.', '.'], ['.', 'X', 'Y', '.'], ['.', 'Y', 'X', '.'], ['.', '.', '.', '.']]) == 8
    assert candidate(grid = [['.', '.', 'X', 'Y', '.'], ['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['.', 'X', 'Y', 'X', 'Y']]) == 10
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 10
