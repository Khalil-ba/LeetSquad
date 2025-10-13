# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(team = [0],dist = 1) == 0
    assert candidate(team = [0, 0, 1, 1, 0, 0, 1, 0],dist = 2) == 3
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 1],dist = 2) == 1
    assert candidate(team = [0, 0, 1, 1, 0, 0, 1],dist = 2) == 3
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1],dist = 4) == 4
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0],dist = 2) == 1
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
    assert candidate(team = [0, 0, 1, 1, 0, 0],dist = 2) == 2
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 4
    assert candidate(team = [1, 1, 1, 1, 0, 0, 0, 0],dist = 4) == 4
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
    assert candidate(team = [0, 1, 0, 1, 0],dist = 3) == 2
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0],dist = 2) == 3
    assert candidate(team = [1, 1, 1, 1, 0, 0, 0, 0],dist = 2) == 2
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 5
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1],dist = 3) == 4
    assert candidate(team = [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 2) == 5
    assert candidate(team = [1],dist = 1) == 0
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 6
    assert candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],dist = 3) == 6
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 7) == 2
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 20) == 2
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 20) == 10
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 3) == 3
    assert candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],dist = 2) == 6
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 15
    assert candidate(team = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],dist = 6) == 5
    assert candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],dist = 2) == 6
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],dist = 3) == 8
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 0
    assert candidate(team = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 8
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 10
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 5
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 10) == 2
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 2) == 9
    assert candidate(team = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],dist = 4) == 4
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 1) == 17
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 1) == 5
    assert candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],dist = 3) == 8
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 8) == 8
    assert candidate(team = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],dist = 5) == 5
    assert candidate(team = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],dist = 3) == 18
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 12
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 19
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 6
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 10
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 7
    assert candidate(team = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 3) == 6
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 4
    assert candidate(team = [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],dist = 6) == 3
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 4) == 14
    assert candidate(team = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],dist = 2) == 6
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [0, 1, 0, 0, 1, 1, 0, 0, 1, 0],dist = 2) == 4
    assert candidate(team = [0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 7
    assert candidate(team = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],dist = 2) == 4
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 12
    assert candidate(team = [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 5) == 6
    assert candidate(team = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],dist = 2) == 6
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 10
    assert candidate(team = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],dist = 5) == 5
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 17
    assert candidate(team = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],dist = 4) == 6
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 10) == 12
    assert candidate(team = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 3) == 10
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 5
    assert candidate(team = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],dist = 3) == 6
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 4) == 4
    assert candidate(team = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 6) == 6
    assert candidate(team = [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],dist = 2) == 6
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 13
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 1) == 1
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 3) == 10
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 7
    assert candidate(team = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],dist = 3) == 3
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 5) == 11
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 2) == 10
    assert candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],dist = 5) == 5
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 5) == 12
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 1) == 5
    assert candidate(team = [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],dist = 3) == 8
    assert candidate(team = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 3) == 9
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 7) == 7
    assert candidate(team = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],dist = 4) == 7
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 4) == 6
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 12) == 2
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],dist = 3) == 12
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 3) == 6
    assert candidate(team = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],dist = 4) == 6
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 5) == 2
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 4
    assert candidate(team = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],dist = 5) == 15
    assert candidate(team = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],dist = 3) == 4
    assert candidate(team = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],dist = 3) == 5
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 17
    assert candidate(team = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],dist = 3) == 11
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],dist = 4) == 3
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],dist = 4) == 4
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 32
    assert candidate(team = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],dist = 4) == 8
    assert candidate(team = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 6) == 8
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 10) == 10
    assert candidate(team = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dist = 10) == 10
    assert candidate(team = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],dist = 2) == 4
    assert candidate(team = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],dist = 20) == 2
    assert candidate(team = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],dist = 2) == 13
    assert candidate(team = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],dist = 5) == 5
    assert candidate(team = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],dist = 3) == 5
