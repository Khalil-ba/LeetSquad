# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 250) == 330
    assert candidate(n = 5) == 2
    assert candidate(n = 15) == 8
    assert candidate(n = 200) == 254
    assert candidate(n = 20) == 12
    assert candidate(n = 100) == 104
    assert candidate(n = 50) == 40
    assert candidate(n = 1) == 0
    assert candidate(n = 10) == 4
    assert candidate(n = 25) == 16
    assert candidate(n = 150) == 178
    assert candidate(n = 80) == 78
    assert candidate(n = 230) == 302
    assert candidate(n = 125) == 142
    assert candidate(n = 75) == 74
    assert candidate(n = 240) == 314
    assert candidate(n = 199) == 250
    assert candidate(n = 120) == 132
    assert candidate(n = 225) == 296
    assert candidate(n = 249) == 324
    assert candidate(n = 190) == 236
    assert candidate(n = 175) == 214
    assert candidate(n = 180) == 218
