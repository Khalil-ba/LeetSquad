# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(picture = [['B', 'W'], ['W', 'B']],target = 1) == 2
    assert candidate(picture = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']],target = 1) == 0
    assert candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']],target = 3) == 6
    assert candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 3) == 9
    assert candidate(picture = [['W', 'B', 'W'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 1) == 0
    assert candidate(picture = [['B', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'B']],target = 1) == 3
    assert candidate(picture = [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 0) == 0
    assert candidate(picture = [['B', 'W', 'B'], ['B', 'W', 'B'], ['B', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B', 'W']],target = 3) == 6
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],target = 0) == 0
    assert candidate(picture = [['B', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'B']],target = 1) == 1
    assert candidate(picture = [['W', 'B'], ['B', 'W']],target = 1) == 2
    assert candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 3) == 9
    assert candidate(picture = [['B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'B'], ['W', 'W', 'W', 'B', 'B']],target = 3) == 9
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['B', 'W', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'W', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['B', 'B', 'B', 'B', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B'], ['B', 'B', 'B', 'B', 'B']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'B', 'B'], ['W', 'B', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'W', 'B', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['B', 'B', 'W', 'W'], ['B', 'B', 'W', 'W'], ['W', 'W', 'B', 'B'], ['W', 'W', 'B', 'B']],target = 2) == 8
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'W', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']],target = 2) == 0
    assert candidate(picture = [['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']],target = 4) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 2) == 4
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 5) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'B'], ['W', 'B', 'B', 'B', 'W']],target = 2) == 2
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W']],target = 3) == 9
    assert candidate(picture = [['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W']],target = 2) == 8
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 5) == 0
    assert candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'B']],target = 3) == 9
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'B', 'W', 'B'], ['B', 'B', 'W', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['B', 'B', 'W', 'W', 'B'], ['B', 'B', 'W', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'B', 'B', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W']],target = 4) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'B', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'B', 'B'], ['B', 'W', 'W', 'B', 'B'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'W', 'W', 'B'], ['W', 'B', 'B', 'W', 'W'], ['W', 'B', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'W', 'B']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'W', 'W', 'B'], ['B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'B'], ['W', 'B', 'B', 'B', 'W'], ['B', 'W', 'W', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'W', 'B', 'B', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B'], ['W', 'W', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 2) == 0
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'B', 'W', 'B']],target = 3) == 9
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'B', 'B', 'W'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'B', 'B', 'W']],target = 2) == 8
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B']],target = 5) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W'], ['W', 'B', 'W'], ['W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'W'], ['B', 'W', 'W', 'W', 'B', 'W'], ['W', 'W', 'B', 'W', 'W', 'B']],target = 2) == 4
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W'], ['W', 'W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['B', 'W', 'B', 'B'], ['W', 'W', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'W', 'B', 'B']],target = 3) == 6
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W'], ['W', 'W', 'W', 'B', 'W', 'W']],target = 4) == 0
    assert candidate(picture = [['B', 'B', 'W', 'W', 'B'], ['B', 'B', 'W', 'W', 'B'], ['W', 'W', 'B', 'B', 'W'], ['W', 'W', 'B', 'B', 'W'], ['B', 'B', 'W', 'W', 'B']],target = 3) == 9
    assert candidate(picture = [['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B']],target = 5) == 0
    assert candidate(picture = [['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B']],target = 6) == 36
    assert candidate(picture = [['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W'], ['B', 'W', 'W', 'B', 'W']],target = 4) == 0
    assert candidate(picture = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']],target = 4) == 16
    assert candidate(picture = [['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'W'], ['W', 'B', 'B', 'W', 'W'], ['B', 'B', 'B', 'B', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W'], ['W', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 2) == 4
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'B', 'B', 'B'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'W'], ['W', 'B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W', 'W']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W'], ['B', 'B', 'B', 'B'], ['W', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],target = 4) == 0
    assert candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'W', 'B', 'B'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['B', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W'], ['W', 'B', 'W', 'W', 'W']],target = 2) == 0
    assert candidate(picture = [['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'W', 'W', 'W']],target = 3) == 9
    assert candidate(picture = [['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'W', 'B'], ['W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B'], ['W', 'W', 'W', 'B']],target = 3) == 0
    assert candidate(picture = [['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'B', 'B', 'B', 'W', 'W'], ['W', 'W', 'B', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W']],target = 1) == 0
    assert candidate(picture = [['W', 'W', 'B', 'W'], ['W', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['W', 'B', 'B', 'W'], ['W', 'W', 'B', 'W']],target = 2) == 0
