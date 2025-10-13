# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 35
    assert candidate(n = 4) == 70
    assert candidate(n = 33) == 66045
    assert candidate(n = 2) == 15
    assert candidate(n = 20) == 10626
    assert candidate(n = 1) == 5
    assert candidate(n = 50) == 316251
    assert candidate(n = 10) == 1001
    assert candidate(n = 5) == 126
    assert candidate(n = 45) == 211876
    assert candidate(n = 49) == 292825
    assert candidate(n = 12) == 1820
    assert candidate(n = 28) == 35960
    assert candidate(n = 30) == 46376
    assert candidate(n = 40) == 135751
    assert candidate(n = 8) == 495
    assert candidate(n = 22) == 14950
    assert candidate(n = 27) == 31465
    assert candidate(n = 35) == 82251
    assert candidate(n = 15) == 3876
    assert candidate(n = 9) == 715
    assert candidate(n = 6) == 210
    assert candidate(n = 7) == 330
    assert candidate(n = 25) == 23751
