# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 0) == 1
    assert candidate(n = 8) == 2345851
    assert candidate(n = 3) == 739
    assert candidate(n = 4) == 5275
    assert candidate(n = 6) == 168571
    assert candidate(n = 2) == 91
    assert candidate(n = 1) == 10
    assert candidate(n = 7) == 712891
    assert candidate(n = 5) == 32491
    assert candidate(n = 9) == 5611771
    assert candidate(n = 10) == 8877691
