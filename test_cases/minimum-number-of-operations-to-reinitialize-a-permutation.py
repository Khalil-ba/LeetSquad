# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 8) == 3
    assert candidate(n = 4) == 2
    assert candidate(n = 12) == 10
    assert candidate(n = 14) == 12
    assert candidate(n = 16) == 4
    assert candidate(n = 18) == 8
    assert candidate(n = 6) == 4
    assert candidate(n = 2) == 1
    assert candidate(n = 20) == 18
    assert candidate(n = 100) == 30
    assert candidate(n = 500) == 166
    assert candidate(n = 1000) == 36
    assert candidate(n = 10) == 6
    assert candidate(n = 896) == 356
    assert candidate(n = 992) == 495
    assert candidate(n = 988) == 138
    assert candidate(n = 50) == 21
    assert candidate(n = 300) == 132
    assert candidate(n = 384) == 191
    assert candidate(n = 600) == 299
    assert candidate(n = 64) == 6
    assert candidate(n = 72) == 35
    assert candidate(n = 192) == 95
    assert candidate(n = 888) == 443
    assert candidate(n = 1024) == 10
    assert candidate(n = 128) == 7
    assert candidate(n = 22) == 6
    assert candidate(n = 46) == 12
    assert candidate(n = 256) == 8
    assert candidate(n = 768) == 348
    assert candidate(n = 32) == 5
    assert candidate(n = 48) == 23
    assert candidate(n = 800) == 184
    assert candidate(n = 200) == 99
    assert candidate(n = 400) == 18
    assert candidate(n = 512) == 9
    assert candidate(n = 750) == 318
    assert candidate(n = 998) == 332
