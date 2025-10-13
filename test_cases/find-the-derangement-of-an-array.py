# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 2
    assert candidate(n = 100000) == 183389504
    assert candidate(n = 100) == 944828409
    assert candidate(n = 4) == 9
    assert candidate(n = 10000) == 381587473
    assert candidate(n = 1000000) == 102701088
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 0
    assert candidate(n = 1000) == 37043040
    assert candidate(n = 10) == 1334961
    assert candidate(n = 5) == 44
    assert candidate(n = 50000) == 429456667
    assert candidate(n = 50) == 77829876
    assert candidate(n = 8) == 14833
    assert candidate(n = 5000) == 22658429
    assert candidate(n = 20) == 927799753
    assert candidate(n = 15) == 66512367
    assert candidate(n = 500000) == 243851595
    assert candidate(n = 9) == 133496
    assert candidate(n = 6) == 265
    assert candidate(n = 999999) == 185559104
    assert candidate(n = 500) == 732014705
    assert candidate(n = 7) == 1854
    assert candidate(n = 25) == 63529464
