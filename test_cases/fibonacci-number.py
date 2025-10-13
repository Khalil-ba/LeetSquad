# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 3) == 2
    assert candidate(n = 30) == 832040
    assert candidate(n = 4) == 3
    assert candidate(n = 2) == 1
    assert candidate(n = 20) == 6765
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 55
    assert candidate(n = 5) == 5
    assert candidate(n = 8) == 21
    assert candidate(n = 29) == 514229
    assert candidate(n = 15) == 610
    assert candidate(n = 12) == 144
    assert candidate(n = 18) == 2584
    assert candidate(n = 6) == 8
    assert candidate(n = 25) == 75025
    assert candidate(n = 28) == 317811
