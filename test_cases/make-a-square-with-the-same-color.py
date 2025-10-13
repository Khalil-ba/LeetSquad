# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(grid = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']]) == False
    assert candidate(grid = [['B', 'B', 'W'], ['B', 'B', 'W'], ['B', 'B', 'W']]) == True
    assert candidate(grid = [['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'B']]) == True
    assert candidate(grid = [['B', 'B', 'B'], ['B', 'W', 'B'], ['B', 'B', 'B']]) == True
    assert candidate(grid = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']]) == True
    assert candidate(grid = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W']]) == True
    assert candidate(grid = [['B', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'B']]) == True
    assert candidate(grid = [['W', 'B', 'W'], ['B', 'W', 'B'], ['W', 'B', 'W']]) == False
    assert candidate(grid = [['B', 'W', 'B'], ['B', 'W', 'W'], ['B', 'W', 'W']]) == True
    assert candidate(grid = [['W', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'W']]) == True
