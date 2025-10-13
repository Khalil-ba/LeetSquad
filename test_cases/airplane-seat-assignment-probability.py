# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 0.5
    assert candidate(n = 100000) == 0.5
    assert candidate(n = 100) == 0.5
    assert candidate(n = 10000) == 0.5
    assert candidate(n = 2) == 0.5
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 0.5
    assert candidate(n = 10) == 0.5
    assert candidate(n = 99999) == 0.5
    assert candidate(n = 2000) == 0.5
    assert candidate(n = 50000) == 0.5
    assert candidate(n = 50) == 0.5
    assert candidate(n = 5) == 0.5
    assert candidate(n = 10001) == 0.5
    assert candidate(n = 250000) == 0.5
    assert candidate(n = 4) == 0.5
    assert candidate(n = 750000) == 0.5
    assert candidate(n = 1001) == 0.5
    assert candidate(n = 200000) == 0.5
    assert candidate(n = 101) == 0.5
    assert candidate(n = 20000) == 0.5
    assert candidate(n = 5000) == 0.5
    assert candidate(n = 20) == 0.5
    assert candidate(n = 9999) == 0.5
    assert candidate(n = 50001) == 0.5
    assert candidate(n = 2500) == 0.5
    assert candidate(n = 500000) == 0.5
    assert candidate(n = 200) == 0.5
    assert candidate(n = 99998) == 0.5
    assert candidate(n = 1000000) == 0.5
    assert candidate(n = 100001) == 0.5
    assert candidate(n = 500) == 0.5
