# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 5
    assert candidate(n = 4) == 14
    assert candidate(n = 19) == 1767263190
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 16796
    assert candidate(n = 5) == 42
    assert candidate(n = 8) == 1430
    assert candidate(n = 15) == 9694845
    assert candidate(n = 12) == 208012
    assert candidate(n = 18) == 477638700
    assert candidate(n = 9) == 4862
    assert candidate(n = 6) == 132
    assert candidate(n = 2) == 2
    assert candidate(n = 7) == 429
