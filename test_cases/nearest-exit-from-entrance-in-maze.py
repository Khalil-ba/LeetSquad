# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(maze = [['.', '+']],entrance = [0, 0]) == -1
    assert candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [0, 1]) == 1
    assert candidate(maze = [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [0, 0]) == 1
    assert candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [2, 2]) == 1
    assert candidate(maze = [['+)', '+)', '+'], ['.', '.', '.'], ['+)', '+)', '+']],entrance = [1, 0]) == 2
    assert candidate(maze = [['+)', '+)', '.'], ['.', '.', '.', '+'], ['+)', '+)', '+)', '.']],entrance = [1, 2]) == 1
    assert candidate(maze = [['+', '.', '+'], ['.', '.', '.'], ['+', '.', '+']],entrance = [1, 1]) == 1
    assert candidate(maze = [['.', '.', '+', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [0, 3]) == 1
    assert candidate(maze = [['.', '.', '.', '.'], ['.', '+', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']],entrance = [1, 1]) == 1
    assert candidate(maze = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']],entrance = [1, 1]) == 1
