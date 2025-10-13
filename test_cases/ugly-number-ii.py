# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 15) == 24
    assert candidate(n = 200) == 16200
    assert candidate(n = 1690) == 2123366400
    assert candidate(n = 1) == 1
    assert candidate(n = 50) == 243
    assert candidate(n = 10) == 12
    assert candidate(n = 5) == 5
    assert candidate(n = 1400) == 516560652
    assert candidate(n = 3) == 3
    assert candidate(n = 1575) == 1230187500
    assert candidate(n = 1600) == 1399680000
    assert candidate(n = 1685) == 2066242608
    assert candidate(n = 900) == 26244000
    assert candidate(n = 1688) == 2099520000
    assert candidate(n = 100) == 1536
    assert candidate(n = 1000) == 51200000
    assert candidate(n = 300) == 82944
    assert candidate(n = 550) == 1555200
    assert candidate(n = 1200) == 174960000
    assert candidate(n = 600) == 2460375
    assert candidate(n = 4) == 4
    assert candidate(n = 1675) == 1990656000
    assert candidate(n = 1650) == 1769472000
    assert candidate(n = 1550) == 1093500000
    assert candidate(n = 1300) == 306110016
    assert candidate(n = 2) == 2
    assert candidate(n = 1024) == 60466176
    assert candidate(n = 8) == 9
    assert candidate(n = 1689) == 2109375000
    assert candidate(n = 800) == 12754584
    assert candidate(n = 400) == 311040
    assert candidate(n = 9) == 10
    assert candidate(n = 750) == 8748000
    assert candidate(n = 6) == 6
    assert candidate(n = 500) == 937500
    assert candidate(n = 7) == 8
    assert candidate(n = 1680) == 2025000000
    assert candidate(n = 1500) == 859963392
