# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 8) == 132
    assert candidate(n = 3) == 3
    assert candidate(n = 11) == 750
    assert candidate(n = 15) == 24679
    assert candidate(n = 4) == 8
    assert candidate(n = 12) == 4010
    assert candidate(n = 14) == 10680
    assert candidate(n = 9) == 250
    assert candidate(n = 13) == 4237
    assert candidate(n = 6) == 36
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 7) == 41
    assert candidate(n = 10) == 700
    assert candidate(n = 5) == 10
