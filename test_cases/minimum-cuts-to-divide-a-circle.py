# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 3
    assert candidate(n = 100) == 50
    assert candidate(n = 4) == 2
    assert candidate(n = 99) == 99
    assert candidate(n = 17) == 17
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 0
    assert candidate(n = 50) == 25
    assert candidate(n = 7) == 7
    assert candidate(n = 10) == 5
    assert candidate(n = 5) == 5
    assert candidate(n = 97) == 97
    assert candidate(n = 61) == 61
    assert candidate(n = 49) == 49
    assert candidate(n = 12) == 6
    assert candidate(n = 21) == 21
    assert candidate(n = 60) == 30
    assert candidate(n = 30) == 15
    assert candidate(n = 40) == 20
    assert candidate(n = 64) == 32
    assert candidate(n = 33) == 33
    assert candidate(n = 37) == 37
    assert candidate(n = 16) == 8
    assert candidate(n = 23) == 23
    assert candidate(n = 73) == 73
    assert candidate(n = 42) == 21
    assert candidate(n = 90) == 45
    assert candidate(n = 8) == 4
    assert candidate(n = 79) == 79
    assert candidate(n = 89) == 89
    assert candidate(n = 75) == 75
    assert candidate(n = 32) == 16
    assert candidate(n = 20) == 10
    assert candidate(n = 19) == 19
    assert candidate(n = 91) == 91
    assert candidate(n = 81) == 81
    assert candidate(n = 11) == 11
    assert candidate(n = 15) == 15
    assert candidate(n = 85) == 85
    assert candidate(n = 41) == 41
    assert candidate(n = 9) == 9
    assert candidate(n = 6) == 3
    assert candidate(n = 13) == 13
    assert candidate(n = 25) == 25
