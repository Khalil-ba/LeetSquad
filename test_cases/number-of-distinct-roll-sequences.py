# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 66
    assert candidate(n = 100) == 534856607
    assert candidate(n = 4) == 184
    assert candidate(n = 10000) == 874574246
    assert candidate(n = 2) == 22
    assert candidate(n = 1) == 6
    assert candidate(n = 1000) == 497171723
    assert candidate(n = 10) == 93120
    assert candidate(n = 2000) == 784558903
    assert candidate(n = 104) == 920649565
    assert candidate(n = 5) == 516
    assert candidate(n = 20000) == 846205927
    assert candidate(n = 8000) == 366597434
    assert candidate(n = 5000) == 798977852
    assert candidate(n = 9999) == 455330915
    assert candidate(n = 20) == 996985946
    assert candidate(n = 15) == 16706688
    assert candidate(n = 6) == 1472
    assert candidate(n = 750) == 498714087
    assert candidate(n = 500) == 353640467
    assert candidate(n = 7) == 4136
