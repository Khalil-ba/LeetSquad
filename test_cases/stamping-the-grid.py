# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],stampHeight = 2,stampWidth = 2) == True
    assert candidate(grid = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],stampHeight = 1,stampWidth = 1) == True
    assert candidate(grid = [[0, 0], [0, 0]],stampHeight = 1,stampWidth = 1) == True
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == True
    assert candidate(grid = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],stampHeight = 4,stampWidth = 3) == True
    assert candidate(grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],stampHeight = 2,stampWidth = 2) == True
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 2) == False
    assert candidate(grid = [[0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == True
    assert candidate(grid = [[1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]],stampHeight = 3,stampWidth = 3) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],stampHeight = 5,stampWidth = 5) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 5) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 2,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 5,stampWidth = 5) == True
    assert candidate(grid = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == True
    assert candidate(grid = [[1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1]],stampHeight = 2,stampWidth = 3) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 5) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == True
    assert candidate(grid = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]],stampHeight = 2,stampWidth = 3) == False
    assert candidate(grid = [[1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 4) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == False
    assert candidate(grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1]],stampHeight = 2,stampWidth = 2) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == False
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == False
    assert candidate(grid = [[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]],stampHeight = 2,stampWidth = 2) == True
    assert candidate(grid = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]],stampHeight = 2,stampWidth = 2) == True
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]],stampHeight = 2,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 5,stampWidth = 10) == True
    assert candidate(grid = [[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 1, 0]],stampHeight = 3,stampWidth = 2) == False
    assert candidate(grid = [[0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]],stampHeight = 2,stampWidth = 2) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 5,stampWidth = 4) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]],stampHeight = 2,stampWidth = 4) == False
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]],stampHeight = 2,stampWidth = 3) == False
    assert candidate(grid = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == False
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 5) == True
    assert candidate(grid = [[0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 2) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 5) == True
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]],stampHeight = 2,stampWidth = 3) == False
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]],stampHeight = 2,stampWidth = 3) == True
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]],stampHeight = 2,stampWidth = 3) == False
    assert candidate(grid = [[0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],stampHeight = 3,stampWidth = 4) == True
    assert candidate(grid = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1]],stampHeight = 3,stampWidth = 2) == False
    assert candidate(grid = [[1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1]],stampHeight = 1,stampWidth = 1) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 5) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == False
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 4) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == False
    assert candidate(grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],stampHeight = 5,stampWidth = 4) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 5,stampWidth = 5) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]],stampHeight = 4,stampWidth = 4) == False
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]],stampHeight = 2,stampWidth = 3) == False
    assert candidate(grid = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]],stampHeight = 2,stampWidth = 2) == True
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 3) == True
    assert candidate(grid = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0]],stampHeight = 2,stampWidth = 2) == False
    assert candidate(grid = [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],stampHeight = 3,stampWidth = 2) == False
