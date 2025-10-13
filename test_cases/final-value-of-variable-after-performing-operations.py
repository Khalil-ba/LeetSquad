# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(operations = ['X++', '++X', '--X', 'X--']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++']) == 5
    assert candidate(operations = ['--X', '--X', 'X--', 'X--']) == -4
    assert candidate(operations = ['++X', '++X', '++X', '++X']) == 4
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++']) == 4
    assert candidate(operations = ['--X', 'X++', 'X++']) == 1
    assert candidate(operations = ['--X', '--X', '--X', '--X']) == -4
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X']) == -5
    assert candidate(operations = ['--X', '--X', 'X++', '++X']) == 0
    assert candidate(operations = ['++X', '++X', 'X++']) == 3
    assert candidate(operations = ['--X', '--X', 'X++', '++X', '--X']) == -1
    assert candidate(operations = ['++X', 'X--', '--X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X--', '++X', '--X']) == 0
    assert candidate(operations = ['++X', '++X', '++X', '++X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -12
    assert candidate(operations = ['X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', 'X++', 'X++', 'X++']) == 1
    assert candidate(operations = ['--X', '--X', 'X++', 'X++', 'X--', 'X--', 'X++', '++X', '--X', 'X++', '--X', '++X', 'X--', '--X', 'X++', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == 0
    assert candidate(operations = ['++X', '++X', '++X', '++X', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--', 'X--']) == -6
    assert candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
    assert candidate(operations = ['X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X', 'X--', '--X']) == -16
    assert candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X']) == 0
    assert candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--']) == 0
    assert candidate(operations = ['X--', '--X', 'X++', '++X', '--X', 'X--', '--X', '++X', 'X++']) == -1
    assert candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', '--X', 'X++', 'X++', '--X', '--X', 'X++', '--X', 'X++', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X']) == 1
    assert candidate(operations = ['--X', '--X', 'X--', 'X++', '++X', '++X', 'X--', '--X', '++X', '--X']) == -2
    assert candidate(operations = ['++X', 'X--', '--X', 'X++', 'X--', '++X', 'X--', '--X', 'X++', '++X']) == 0
    assert candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++']) == 2
    assert candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', '--X', 'X++']) == 1
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X', '++X']) == -5
    assert candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X']) == 0
    assert candidate(operations = ['++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X', '--X', '--X', '++X', '++X']) == 2
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -12
    assert candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
    assert candidate(operations = ['++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X', '--X']) == 0
    assert candidate(operations = ['X++', '--X', '++X', 'X--', '++X', 'X++', '--X', '--X', '++X', 'X++']) == 2
    assert candidate(operations = ['++X', '++X', '++X', '++X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
    assert candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
    assert candidate(operations = ['--X', 'X++', '++X', '--X', 'X++', '--X', 'X--', 'X++', '--X', '++X']) == 0
    assert candidate(operations = ['++X', '++X', '++X', '--X', '--X', '--X', '++X', 'X++', '--X']) == 1
    assert candidate(operations = ['++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == -1
    assert candidate(operations = ['--X', '--X', 'X++', 'X--', 'X--', 'X--', 'X--', 'X--', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 0
    assert candidate(operations = ['++X', '--X', 'X++', '++X', '--X', 'X--', '++X', 'X++']) == 2
    assert candidate(operations = ['--X', 'X--', '--X', 'X--', '--X', 'X--', '++X', 'X++', '++X', 'X++', '++X', 'X++', '++X', 'X++']) == 2
    assert candidate(operations = ['X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X']) == 0
    assert candidate(operations = ['--X', '++X', '--X', '++X', '--X', '++X', '--X', '++X']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X--', 'X--', 'X--', 'X--', 'X++', 'X++', 'X--', 'X--']) == 0
    assert candidate(operations = ['X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X', 'X++', '--X', 'X--', 'X++', '--X']) == -5
    assert candidate(operations = ['X++', 'X++', '--X', '--X', '++X', 'X--', '++X', '--X', '++X', '--X']) == 0
    assert candidate(operations = ['X++', 'X++', '++X', '--X', 'X--', 'X--', '--X', '++X', 'X--', '--X']) == -2
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 12
    assert candidate(operations = ['--X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', '--X', 'X++', '--X', '++X', 'X--', '--X', 'X++']) == -2
    assert candidate(operations = ['--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 4
    assert candidate(operations = ['--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == -1
    assert candidate(operations = ['X--', '--X', '++X', 'X++', 'X--', '--X', '++X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', '++X', 'X++', '--X', '--X', '++X', 'X++']) == 2
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', '++X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 8
    assert candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 57
    assert candidate(operations = ['X++', '--X', '++X', 'X--', '++X', '--X', 'X++', '++X', '--X', 'X--']) == 0
    assert candidate(operations = ['--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 37
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++']) == 2
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X']) == 0
    assert candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X']) == 0
    assert candidate(operations = ['--X', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', 'X--', 'X--', '++X', '++X']) == 0
    assert candidate(operations = ['X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X', 'X++', 'X--', '++X', '--X']) == 0
    assert candidate(operations = ['X++', 'X--', '++X', '--X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X']) == 0
    assert candidate(operations = ['X++', '--X', '++X', '--X', 'X++', '--X', 'X--']) == -1
    assert candidate(operations = ['--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++']) == 2
    assert candidate(operations = ['X--', 'X--', '--X', '--X', 'X++', 'X++', '++X']) == -1
    assert candidate(operations = ['X++', 'X++', 'X++', '--X', '--X', '--X', 'X++', 'X++', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X']) == 1
    assert candidate(operations = ['++X', '++X', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++']) == 2
    assert candidate(operations = ['--X', '--X', '--X', '--X', '--X', '++X', '++X', '++X', '++X', '++X', 'X++', 'X++', 'X++']) == 3
    assert candidate(operations = ['++X', 'X++', '--X', 'X--', '++X', '--X', 'X++', '++X']) == 2
    assert candidate(operations = ['X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X', 'X--', '--X', 'X++', '++X']) == 2
    assert candidate(operations = ['X++', '++X', 'X++', '++X', '--X', '--X', 'X--', '--X', 'X++', '++X', '--X', 'X--', '++X', 'X++']) == 2
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == -4
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X++', 'X++', '--X', '--X', '--X']) == 0
    assert candidate(operations = ['X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', 'X++', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X', '--X']) == 0
    assert candidate(operations = ['X--', '--X', 'X++', '++X', 'X--', 'X--', '--X', '++X', 'X--', 'X--', 'X++', '++X']) == -2
    assert candidate(operations = ['X++', 'X++', '--X', '--X', 'X++', 'X--', 'X++', '--X', 'X++', 'X--', '++X', '--X']) == 0
    assert candidate(operations = ['++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--', '++X', 'X--']) == 0
    assert candidate(operations = ['X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X', 'X++', '--X']) == 0
    assert candidate(operations = ['--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++', '--X', 'X--', '++X', 'X++']) == 0
    assert candidate(operations = ['++X', '++X', '++X', '--X', 'X--', '--X', 'X--', '--X', '++X', '--X']) == -2
