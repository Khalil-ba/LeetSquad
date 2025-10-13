# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(bits = [1, 1, 1, 0]) == False
    assert candidate(bits = [0, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0]) == True
    assert candidate(bits = [0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 0, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 1, 1, 0]) == False
    assert candidate(bits = [0, 0, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 0]) == True
    assert candidate(bits = [0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 1, 0, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]) == True
    assert candidate(bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(bits = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 0, 1, 1, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1]) == True
    assert candidate(bits = [0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 1, 1, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 0, 0, 0, 0]) == True
    assert candidate(bits = [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [0, 0, 0, 0, 0, 0, 0, 0]) == True
    assert candidate(bits = [0, 1, 1, 0, 1, 1, 0]) == True
    assert candidate(bits = [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == True
    assert candidate(bits = [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0]) == True
    assert candidate(bits = [0, 1, 0, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]) == False
    assert candidate(bits = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [0, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True
    assert candidate(bits = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == True
