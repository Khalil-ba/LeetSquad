# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 8) == 92
    assert candidate(n = 3) == 0
    assert candidate(n = 4) == 2
    assert candidate(n = 9) == 352
    assert candidate(n = 6) == 4
    assert candidate(n = 2) == 0
    assert candidate(n = 1) == 1
    assert candidate(n = 7) == 40
    assert candidate(n = 5) == 10
