# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 11) == 54
    assert candidate(n = 30) == 59049
    assert candidate(n = 20) == 1458
    assert candidate(n = 2) == 1
    assert candidate(n = 10) == 36
    assert candidate(n = 58) == 1549681956
    assert candidate(n = 29) == 39366
    assert candidate(n = 45) == 14348907
    assert candidate(n = 49) == 57395628
    assert candidate(n = 12) == 81
    assert candidate(n = 47) == 28697814
    assert candidate(n = 53) == 258280326
    assert candidate(n = 57) == 1162261467
    assert candidate(n = 50) == 86093442
    assert candidate(n = 28) == 26244
    assert candidate(n = 56) == 774840978
    assert candidate(n = 40) == 2125764
    assert candidate(n = 37) == 708588
    assert candidate(n = 42) == 4782969
    assert candidate(n = 35) == 354294
    assert candidate(n = 18) == 729
    assert candidate(n = 32) == 118098
    assert candidate(n = 36) == 531441
    assert candidate(n = 19) == 972
    assert candidate(n = 48) == 43046721
    assert candidate(n = 15) == 243
    assert candidate(n = 6) == 9
    assert candidate(n = 55) == 516560652
    assert candidate(n = 13) == 108
    assert candidate(n = 25) == 8748
