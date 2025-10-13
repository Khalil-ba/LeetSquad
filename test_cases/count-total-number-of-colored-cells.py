# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 13
    assert candidate(n = 100000) == 19999800001
    assert candidate(n = 100) == 19801
    assert candidate(n = 10000) == 199980001
    assert candidate(n = 2) == 5
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 1998001
    assert candidate(n = 10) == 181
    assert candidate(n = 15000) == 449970001
    assert candidate(n = 99999) == 19999400005
    assert candidate(n = 12345) == 304773361
    assert candidate(n = 7500) == 112485001
    assert candidate(n = 2000) == 7996001
    assert candidate(n = 50000) == 4999900001
    assert candidate(n = 50) == 4901
    assert candidate(n = 5) == 41
    assert candidate(n = 30) == 1741
    assert candidate(n = 60000) == 7199880001
    assert candidate(n = 1500) == 4497001
    assert candidate(n = 4) == 25
    assert candidate(n = 30000) == 1799940001
    assert candidate(n = 1001) == 2002001
    assert candidate(n = 85000) == 14449830001
    assert candidate(n = 80000) == 12799840001
    assert candidate(n = 20000) == 799960001
    assert candidate(n = 5000) == 49990001
    assert candidate(n = 75000) == 11249850001
    assert candidate(n = 20) == 761
    assert candidate(n = 40000) == 3199920001
    assert candidate(n = 15) == 421
    assert candidate(n = 2500) == 12495001
    assert candidate(n = 9000) == 161982001
    assert candidate(n = 200) == 79601
    assert candidate(n = 99998) == 19999000013
    assert candidate(n = 500) == 499001
    assert candidate(n = 25) == 1201
    assert candidate(n = 25000) == 1249950001
