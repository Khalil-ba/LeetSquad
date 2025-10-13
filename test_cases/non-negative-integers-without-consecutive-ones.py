# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 100) == 34
    assert candidate(n = 15) == 8
    assert candidate(n = 1000000) == 17711
    assert candidate(n = 32) == 14
    assert candidate(n = 2) == 3
    assert candidate(n = 1) == 2
    assert candidate(n = 1000000000) == 2178309
    assert candidate(n = 1000) == 144
    assert candidate(n = 10) == 8
    assert candidate(n = 5) == 5
    assert candidate(n = 987654321) == 2178309
    assert candidate(n = 888888888) == 2178309
    assert candidate(n = 333333333) == 1149851
    assert candidate(n = 777777777) == 2178309
    assert candidate(n = 999999999) == 2178309
    assert candidate(n = 110011001) == 514229
    assert candidate(n = 314159265) == 1149851
    assert candidate(n = 500000000) == 1346269
    assert candidate(n = 2147483647) == 3524578
    assert candidate(n = 123456789) == 514229
    assert candidate(n = 555555555) == 1496319
    assert candidate(n = 101010101) == 514229
    assert candidate(n = 1000000001) == 2178309
    assert candidate(n = 100000000) == 514229
    assert candidate(n = 111111111) == 514229
    assert candidate(n = 800000000) == 2178309
