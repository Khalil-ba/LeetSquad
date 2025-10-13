# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 3) == 2
    assert candidate(n = 100) == 21
    assert candidate(n = 99) == 21
    assert candidate(n = 2) == 1
    assert candidate(n = 20) == 7
    assert candidate(n = 1) == 1
    assert candidate(n = 50) == 13
    assert candidate(n = 7) == 3
    assert candidate(n = 10) == 4
    assert candidate(n = 88) == 21
    assert candidate(n = 97) == 21
    assert candidate(n = 63) == 13
    assert candidate(n = 45) == 13
    assert candidate(n = 49) == 13
    assert candidate(n = 47) == 13
    assert candidate(n = 60) == 13
    assert candidate(n = 64) == 13
    assert candidate(n = 37) == 11
    assert candidate(n = 17) == 5
    assert candidate(n = 42) == 11
    assert candidate(n = 90) == 21
    assert candidate(n = 22) == 8
    assert candidate(n = 89) == 21
    assert candidate(n = 75) == 18
    assert candidate(n = 81) == 18
    assert candidate(n = 24) == 8
    assert candidate(n = 11) == 5
    assert candidate(n = 15) == 5
    assert candidate(n = 31) == 8
    assert candidate(n = 25) == 8
