# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(students = [0, 1, 0, 1],sandwiches = [1, 0, 1, 0]) == 0
    assert candidate(students = [1, 1, 1, 0, 0, 1],sandwiches = [1, 0, 0, 0, 1, 1]) == 3
    assert candidate(students = [0, 0, 1, 1],sandwiches = [1, 1, 0, 0]) == 0
    assert candidate(students = [1, 0, 1, 0],sandwiches = [0, 1, 0, 1]) == 0
    assert candidate(students = [0, 0, 0, 0],sandwiches = [0, 0, 0, 0]) == 0
    assert candidate(students = [0, 1, 0, 1],sandwiches = [0, 1, 0, 1]) == 0
    assert candidate(students = [1, 1, 0, 0],sandwiches = [0, 1, 0, 1]) == 0
    assert candidate(students = [1, 1, 1, 1],sandwiches = [1, 1, 1, 1]) == 0
    assert candidate(students = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 1, 1, 0, 0, 0, 0, 1, 1],sandwiches = [0, 0, 0, 1, 1, 1, 0, 1, 1]) == 0
    assert candidate(students = [1, 0, 0, 1, 1, 0, 0, 1],sandwiches = [1, 1, 1, 1, 0, 0, 0, 0]) == 0
    assert candidate(students = [1, 0, 0, 1, 0, 1, 1, 0],sandwiches = [1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(students = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],sandwiches = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(students = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 1, 0, 0, 1, 0, 1, 0],sandwiches = [0, 0, 1, 0, 1, 1, 0, 1]) == 0
    assert candidate(students = [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],sandwiches = [0, 1, 0, 1, 1, 1, 1, 0, 0, 0]) == 0
    assert candidate(students = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],sandwiches = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]) == 0
    assert candidate(students = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],sandwiches = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]) == 2
    assert candidate(students = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],sandwiches = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]) == 0
    assert candidate(students = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],sandwiches = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 0
    assert candidate(students = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],sandwiches = [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1]) == 0
    assert candidate(students = [1, 1, 1, 0, 0, 0, 0, 1, 1],sandwiches = [1, 0, 0, 0, 1, 0, 0, 1, 0]) == 3
    assert candidate(students = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],sandwiches = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0]) == 0
    assert candidate(students = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],sandwiches = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 2
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],sandwiches = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(students = [1, 1, 0, 0, 1, 1, 0, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],sandwiches = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]) == 0
    assert candidate(students = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],sandwiches = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],sandwiches = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 0
    assert candidate(students = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],sandwiches = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],sandwiches = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]) == 3
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(students = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],sandwiches = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]) == 0
    assert candidate(students = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sandwiches = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(students = [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(students = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],sandwiches = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 2
    assert candidate(students = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],sandwiches = [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1]) == 0
    assert candidate(students = [0, 1, 1, 0, 1, 0, 0, 1],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [1, 1, 0, 0, 1, 1, 0, 0, 0]) == 0
    assert candidate(students = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],sandwiches = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]) == 0
    assert candidate(students = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],sandwiches = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],sandwiches = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],sandwiches = [0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 0, 1, 1, 0, 0, 1, 1],sandwiches = [0, 0, 1, 1, 0, 0, 1, 1]) == 0
    assert candidate(students = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0],sandwiches = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 1
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],sandwiches = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]) == 4
    assert candidate(students = [1, 1, 0, 0, 0, 0, 1, 1],sandwiches = [1, 1, 0, 0, 0, 0, 1, 1]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],sandwiches = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 0
    assert candidate(students = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],sandwiches = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(students = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 0, 0, 1, 1, 0, 0, 1],sandwiches = [1, 0, 1, 0, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],sandwiches = [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0]) == 1
    assert candidate(students = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1],sandwiches = [0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(students = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],sandwiches = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(students = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],sandwiches = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0]) == 1
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [0, 0, 1, 1, 0, 0, 1, 1, 1]) == 0
    assert candidate(students = [0, 1, 1, 0, 1, 1, 0, 0, 1],sandwiches = [1, 1, 0, 0, 1, 1, 0, 0, 1]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 0, 1, 1, 0, 0, 0, 1],sandwiches = [0, 1, 1, 0, 0, 0, 1, 1]) == 0
    assert candidate(students = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],sandwiches = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(students = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],sandwiches = [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]) == 0
    assert candidate(students = [1, 1, 0, 0, 1, 1, 0, 0],sandwiches = [0, 0, 1, 1, 0, 0, 1, 1]) == 0
    assert candidate(students = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],sandwiches = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(students = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0],sandwiches = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],sandwiches = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == 0
    assert candidate(students = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sandwiches = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 69
    assert candidate(students = [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],sandwiches = [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1]) == 0
    assert candidate(students = [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(students = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],sandwiches = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 0
    assert candidate(students = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],sandwiches = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]) == 1
