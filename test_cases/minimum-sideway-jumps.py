# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(obstacles = [0, 1, 0, 0, 2, 0, 0, 3, 0, 0]) == 1
    assert candidate(obstacles = [0, 0, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 3, 2, 1, 0, 3, 2, 1, 0]) == 4
    assert candidate(obstacles = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0]) == 1
    assert candidate(obstacles = [0, 1, 3, 2, 3, 1, 0, 0, 0, 0]) == 2
    assert candidate(obstacles = [0, 3, 0, 0, 2, 0, 0, 1, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 0, 0]) == 5
    assert candidate(obstacles = [0, 2, 1, 0, 3, 0]) == 2
    assert candidate(obstacles = [0, 1, 2, 0, 2, 1, 0, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 2, 0, 0, 0, 3, 0, 0, 1, 0]) == 2
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 0]) == 1
    assert candidate(obstacles = [0, 1, 1, 3, 3, 0]) == 0
    assert candidate(obstacles = [0, 3, 2, 1, 3, 0]) == 3
    assert candidate(obstacles = [0, 0, 1, 2, 3, 0]) == 2
    assert candidate(obstacles = [0, 3, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 2, 0, 2, 0, 2, 0]) == 1
    assert candidate(obstacles = [0, 3, 0, 3, 0, 3, 0]) == 0
    assert candidate(obstacles = [0, 1, 2, 3, 0]) == 2
    assert candidate(obstacles = [0, 1, 0, 0, 2, 0]) == 1
    assert candidate(obstacles = [0, 2, 3, 2, 1, 2, 3, 0]) == 3
    assert candidate(obstacles = [0, 3, 2, 1, 0, 0]) == 2
    assert candidate(obstacles = [0, 1, 2, 0, 3, 0]) == 2
    assert candidate(obstacles = [0, 2, 3, 1, 0, 0]) == 2
    assert candidate(obstacles = [0, 2, 2, 2, 2, 0]) == 1
    assert candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 0]) == 5
    assert candidate(obstacles = [0, 3, 0, 1, 2, 0, 0, 0, 0, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 16
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 11
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 12
    assert candidate(obstacles = [0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 2
    assert candidate(obstacles = [0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0]) == 10
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 8
    assert candidate(obstacles = [0, 1, 1, 1, 1, 0, 2, 2, 2, 2, 0, 3, 3, 3, 3, 0, 1, 1, 1, 1, 0]) == 2
    assert candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 2
    assert candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 20
    assert candidate(obstacles = [0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 2, 0]) == 7
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 4
    assert candidate(obstacles = [0, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 0]) == 5
    assert candidate(obstacles = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0]) == 10
    assert candidate(obstacles = [0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 2
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 3
    assert candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 1
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 10
    assert candidate(obstacles = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]) == 0
    assert candidate(obstacles = [0, 3, 2, 0, 1, 0, 3, 2, 0, 1, 0, 3, 0]) == 4
    assert candidate(obstacles = [0, 1, 0, 0, 2, 0, 3, 0, 0, 1, 0, 0, 0, 3, 0, 2, 0]) == 3
    assert candidate(obstacles = [0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 2
    assert candidate(obstacles = [0, 3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 0]) == 5
    assert candidate(obstacles = [0, 1, 3, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 10
    assert candidate(obstacles = [0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0]) == 10
    assert candidate(obstacles = [0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0]) == 4
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 18
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 13
    assert candidate(obstacles = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 0]) == 0
    assert candidate(obstacles = [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 12
    assert candidate(obstacles = [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 1
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0]) == 7
    assert candidate(obstacles = [0, 3, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 1]) == 2
    assert candidate(obstacles = [0, 3, 2, 1, 0, 2, 1, 0, 3, 2, 1, 0, 2, 1, 3, 0]) == 5
    assert candidate(obstacles = [0, 1, 3, 2, 3, 1, 2, 3, 0, 1, 2, 3, 0]) == 6
    assert candidate(obstacles = [0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 3, 0, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 3
    assert candidate(obstacles = [0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 30
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 27
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 3, 2, 1]) == 8
    assert candidate(obstacles = [0, 2, 1, 3, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 26
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1]) == 5
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 11
    assert candidate(obstacles = [0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 25
    assert candidate(obstacles = [0, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 26
    assert candidate(obstacles = [0, 2, 2, 0, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1, 0]) == 5
    assert candidate(obstacles = [0, 3, 0, 2, 3, 1, 0, 2, 3, 1, 0, 2, 3, 1, 0]) == 6
    assert candidate(obstacles = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 0]) == 7
    assert candidate(obstacles = [0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0]) == 8
    assert candidate(obstacles = [0, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 8
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 6
    assert candidate(obstacles = [0, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 18
    assert candidate(obstacles = [0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0]) == 1
    assert candidate(obstacles = [0, 1, 2, 0, 3, 0, 1, 2, 0, 3, 0, 1, 0]) == 4
    assert candidate(obstacles = [0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]) == 2
    assert candidate(obstacles = [0, 3, 2, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0]) == 6
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 19
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 31
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 3, 2, 1, 0, 2, 1, 3, 2, 1, 0]) == 11
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 2, 3, 2, 1, 0]) == 5
    assert candidate(obstacles = [0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 23
    assert candidate(obstacles = [0, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 0]) == 1
    assert candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0]) == 3
    assert candidate(obstacles = [0, 3, 2, 1, 2, 3, 1, 2, 3, 1, 0]) == 7
    assert candidate(obstacles = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]) == 1
    assert candidate(obstacles = [0, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 17
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0]) == 3
    assert candidate(obstacles = [0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 1
    assert candidate(obstacles = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
    assert candidate(obstacles = [0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 3
    assert candidate(obstacles = [0, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 3, 0]) == 12
    assert candidate(obstacles = [0, 1, 0, 3, 0, 2, 0, 1, 0, 3, 0, 2, 0, 1, 0]) == 3
    assert candidate(obstacles = [0, 1, 2, 3, 0, 2, 1, 3, 0, 1, 2, 3, 0]) == 6
    assert candidate(obstacles = [0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3]) == 0
    assert candidate(obstacles = [0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 11
    assert candidate(obstacles = [0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 17
    assert candidate(obstacles = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(obstacles = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
    assert candidate(obstacles = [0, 0, 0, 2, 3, 1, 0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3]) == 6
    assert candidate(obstacles = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0]) == 7
    assert candidate(obstacles = [0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0]) == 0
    assert candidate(obstacles = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0]) == 3
    assert candidate(obstacles = [0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1, 0]) == 2
    assert candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 17
    assert candidate(obstacles = [0, 1, 3, 1, 2, 3, 1, 2, 3, 1, 0]) == 6
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 2
    assert candidate(obstacles = [0, 2, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 7
    assert candidate(obstacles = [0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0, 3, 0, 1, 0, 2, 0]) == 4
    assert candidate(obstacles = [0, 3, 2, 3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 9
    assert candidate(obstacles = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 0]) == 9
    assert candidate(obstacles = [0, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0]) == 2
    assert candidate(obstacles = [0, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]) == 1
    assert candidate(obstacles = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(obstacles = [0, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 0]) == 11
    assert candidate(obstacles = [0, 1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 0]) == 9
    assert candidate(obstacles = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]) == 0
    assert candidate(obstacles = [0, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 11
