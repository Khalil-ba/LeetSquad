# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 100) == 400
    assert candidate(n = 15) == 30
    assert candidate(n = 200) == 952
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 0
    assert candidate(n = 10) == 16
    assert candidate(n = 5) == 6
    assert candidate(n = 150) == 692
    assert candidate(n = 3) == 2
    assert candidate(n = 130) == 585
    assert candidate(n = 125) == 560
    assert candidate(n = 12) == 21
    assert candidate(n = 110) == 460
    assert candidate(n = 50) == 172
    assert candidate(n = 60) == 214
    assert candidate(n = 155) == 718
    assert candidate(n = 30) == 79
    assert candidate(n = 40) == 119
    assert candidate(n = 4) == 4
    assert candidate(n = 80) == 295
    assert candidate(n = 75) == 274
    assert candidate(n = 140) == 635
    assert candidate(n = 18) == 42
    assert candidate(n = 120) == 529
    assert candidate(n = 160) == 743
    assert candidate(n = 199) == 946
    assert candidate(n = 180) == 843
    assert candidate(n = 90) == 345
