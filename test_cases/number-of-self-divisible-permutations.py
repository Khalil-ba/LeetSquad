# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 8) == 324
    assert candidate(n = 3) == 3
    assert candidate(n = 11) == 129744
    assert candidate(n = 4) == 4
    assert candidate(n = 12) == 63504
    assert candidate(n = 9) == 3600
    assert candidate(n = 6) == 16
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 1
    assert candidate(n = 7) == 256
    assert candidate(n = 10) == 3600
    assert candidate(n = 5) == 28
