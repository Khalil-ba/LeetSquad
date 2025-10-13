# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 700) == 1660140
    assert candidate(n = 800) == 3353149
    assert candidate(n = 100) == 41334
    assert candidate(n = 600) == 772866
    assert candidate(n = 37) == 1478
    assert candidate(n = 200) == 41334
    assert candidate(n = 400) == 601470
    assert candidate(n = 900) == 3353149
    assert candidate(n = 9) == 82
    assert candidate(n = 2) == 1
    assert candidate(n = 25) == 182
    assert candidate(n = 1) == 1
    assert candidate(n = 500) == 772866
    assert candidate(n = 1000) == 10804657
    assert candidate(n = 10) == 182
    assert candidate(n = 300) == 184768
    assert candidate(n = 50) == 3503
    assert candidate(n = 625) == 772866
    assert candidate(n = 999) == 9804657
    assert candidate(n = 750) == 2154349
    assert candidate(n = 150) == 41334
