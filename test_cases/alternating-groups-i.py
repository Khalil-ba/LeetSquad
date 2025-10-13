# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(colors = [1, 1, 1, 0, 0, 0, 1, 1, 1]) == 0
    assert candidate(colors = [1, 0, 0, 0, 1, 1, 1, 0]) == 2
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0]) == 7
    assert candidate(colors = [0, 0, 1, 1, 0, 0, 1]) == 1
    assert candidate(colors = [0, 0, 1, 1, 0, 0, 1, 1, 0]) == 0
    assert candidate(colors = [0, 1, 1, 0, 0, 1]) == 2
    assert candidate(colors = [0, 1, 0, 1, 0]) == 3
    assert candidate(colors = [1, 1, 0, 1, 1, 0, 1]) == 2
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1]) == 5
    assert candidate(colors = [0, 1, 1, 0, 1, 1, 0, 1]) == 4
    assert candidate(colors = [1, 0, 0, 1, 1, 0]) == 2
    assert candidate(colors = [0, 1, 1, 0, 1, 1, 0, 1, 1]) == 3
    assert candidate(colors = [1, 1, 1]) == 0
    assert candidate(colors = [1, 1, 0, 1, 0, 1]) == 3
    assert candidate(colors = [0, 1, 0, 1, 1, 0, 1, 0, 1]) == 7
    assert candidate(colors = [1, 0, 0, 1, 0, 0, 1, 0, 0]) == 3
    assert candidate(colors = [0, 0, 0, 1, 1, 1, 0]) == 0
    assert candidate(colors = [0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [1, 1, 0, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [1, 0, 1, 0, 1]) == 3
    assert candidate(colors = [0, 1, 0, 0, 1]) == 3
    assert candidate(colors = [1, 0, 1, 0, 1, 0]) == 6
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1]) == 7
    assert candidate(colors = [0, 0, 0, 1, 1, 1, 0, 0, 0]) == 0
    assert candidate(colors = [1, 0, 0, 1, 0, 1, 1, 0, 1]) == 3
    assert candidate(colors = [1, 0, 0, 1, 0, 0, 1, 0]) == 4
    assert candidate(colors = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]) == 6
    assert candidate(colors = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]) == 0
    assert candidate(colors = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]) == 10
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 20
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 9
    assert candidate(colors = [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]) == 3
    assert candidate(colors = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 0
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 26
    assert candidate(colors = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 32
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 15
    assert candidate(colors = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 31
    assert candidate(colors = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]) == 6
    assert candidate(colors = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1]) == 8
    assert candidate(colors = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]) == 0
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 14
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0]) == 12
    assert candidate(colors = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == 0
    assert candidate(colors = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]) == 15
    assert candidate(colors = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]) == 11
    assert candidate(colors = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 12
    assert candidate(colors = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 20
    assert candidate(colors = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0]) == 0
    assert candidate(colors = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]) == 9
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 19
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 12
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 13
    assert candidate(colors = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 19
    assert candidate(colors = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]) == 1
    assert candidate(colors = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]) == 0
    assert candidate(colors = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 0
    assert candidate(colors = [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 27
    assert candidate(colors = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == 0
    assert candidate(colors = [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]) == 3
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 16
    assert candidate(colors = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == 6
    assert candidate(colors = [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]) == 9
    assert candidate(colors = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]) == 7
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 12
    assert candidate(colors = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]) == 13
    assert candidate(colors = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]) == 5
    assert candidate(colors = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 1
    assert candidate(colors = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 20
    assert candidate(colors = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0]) == 7
    assert candidate(colors = [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == 3
    assert candidate(colors = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1]) == 8
    assert candidate(colors = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]) == 0
    assert candidate(colors = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 1
    assert candidate(colors = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]) == 15
    assert candidate(colors = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]) == 9
    assert candidate(colors = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]) == 6
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 11
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 15
    assert candidate(colors = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]) == 0
    assert candidate(colors = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]) == 13
    assert candidate(colors = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]) == 9
    assert candidate(colors = [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 11
    assert candidate(colors = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1]) == 11
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 11
    assert candidate(colors = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]) == 9
    assert candidate(colors = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0]) == 13
    assert candidate(colors = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == 1
    assert candidate(colors = [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]) == 0
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 10
    assert candidate(colors = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 0
    assert candidate(colors = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]) == 0
    assert candidate(colors = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]) == 4
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 23
    assert candidate(colors = [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1]) == 9
    assert candidate(colors = [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == 1
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 20
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 12
    assert candidate(colors = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]) == 0
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 9
    assert candidate(colors = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 24
    assert candidate(colors = [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]) == 10
    assert candidate(colors = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]) == 4
    assert candidate(colors = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]) == 12
    assert candidate(colors = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]) == 0
    assert candidate(colors = [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]) == 4
    assert candidate(colors = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 0
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 15
    assert candidate(colors = [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 2
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 18
    assert candidate(colors = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]) == 13
    assert candidate(colors = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]) == 9
    assert candidate(colors = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 0
    assert candidate(colors = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 32
    assert candidate(colors = [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0]) == 0
    assert candidate(colors = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1]) == 6
    assert candidate(colors = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0]) == 7
    assert candidate(colors = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]) == 2
    assert candidate(colors = [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]) == 1
    assert candidate(colors = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]) == 1
    assert candidate(colors = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 1
    assert candidate(colors = [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1]) == 7
    assert candidate(colors = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(colors = [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]) == 9
