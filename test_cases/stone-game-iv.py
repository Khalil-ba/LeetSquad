# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 101) == True
    assert candidate(n = 3) == True
    assert candidate(n = 100) == True
    assert candidate(n = 30) == True
    assert candidate(n = 5) == False
    assert candidate(n = 4) == True
    assert candidate(n = 200) == True
    assert candidate(n = 17) == False
    assert candidate(n = 2) == False
    assert candidate(n = 20) == False
    assert candidate(n = 1) == True
    assert candidate(n = 7) == False
    assert candidate(n = 10) == False
    assert candidate(n = 25) == True
    assert candidate(n = 50) == True
    assert candidate(n = 300) == True
    assert candidate(n = 123) == True
    assert candidate(n = 64) == True
    assert candidate(n = 16) == True
    assert candidate(n = 169) == True
    assert candidate(n = 81) == True
    assert candidate(n = 150) == False
    assert candidate(n = 55) == True
    assert candidate(n = 180) == False
