# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 8) == 9
    assert candidate(n = 3) == 6
    assert candidate(n = 100) == 101
    assert candidate(n = 4) == 7
    assert candidate(n = 10000) == 10001
    assert candidate(n = 9) == 11
    assert candidate(n = 5000) == 5001
    assert candidate(n = 6) == 8
    assert candidate(n = 2) == 2
    assert candidate(n = 9999) == 9998
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 1001
    assert candidate(n = 7) == 6
    assert candidate(n = 10) == 12
    assert candidate(n = 5) == 7
    assert candidate(n = 12) == 13
    assert candidate(n = 21) == 23
    assert candidate(n = 2000) == 2001
    assert candidate(n = 7500) == 7501
    assert candidate(n = 104) == 105
    assert candidate(n = 50) == 52
    assert candidate(n = 300) == 301
    assert candidate(n = 28) == 29
    assert candidate(n = 30) == 32
    assert candidate(n = 99) == 98
    assert candidate(n = 6666) == 6668
    assert candidate(n = 17) == 19
    assert candidate(n = 999) == 998
    assert candidate(n = 18) == 20
    assert candidate(n = 20) == 21
    assert candidate(n = 24) == 25
    assert candidate(n = 7777) == 7779
    assert candidate(n = 11) == 10
    assert candidate(n = 15) == 14
    assert candidate(n = 14) == 16
    assert candidate(n = 31) == 30
    assert candidate(n = 500) == 501
    assert candidate(n = 25) == 27
