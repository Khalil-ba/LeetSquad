# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 3
    assert candidate(n = 45) == 1836311903
    assert candidate(n = 4) == 5
    assert candidate(n = 20) == 10946
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 89
    assert candidate(n = 5) == 8
    assert candidate(n = 30) == 1346269
    assert candidate(n = 15) == 987
    assert candidate(n = 40) == 165580141
    assert candidate(n = 12) == 233
    assert candidate(n = 35) == 14930352
    assert candidate(n = 18) == 4181
    assert candidate(n = 7) == 21
    assert candidate(n = 25) == 121393
