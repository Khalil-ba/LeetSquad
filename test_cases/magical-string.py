# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 100000) == 49972
    assert candidate(n = 100) == 49
    assert candidate(n = 15) == 7
    assert candidate(n = 10000) == 4996
    assert candidate(n = 6) == 3
    assert candidate(n = 20) == 10
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 502
    assert candidate(n = 10) == 5
    assert candidate(n = 32000) == 15996
    assert candidate(n = 99999) == 49972
    assert candidate(n = 15000) == 7501
    assert candidate(n = 3) == 1
    assert candidate(n = 12345) == 6172
    assert candidate(n = 7500) == 3747
    assert candidate(n = 90000) == 44975
    assert candidate(n = 50000) == 24985
    assert candidate(n = 50) == 25
    assert candidate(n = 5) == 3
    assert candidate(n = 300) == 150
    assert candidate(n = 30) == 15
    assert candidate(n = 60000) == 29976
    assert candidate(n = 40) == 20
    assert candidate(n = 4) == 2
    assert candidate(n = 30000) == 14993
    assert candidate(n = 2) == 1
    assert candidate(n = 45000) == 22491
    assert candidate(n = 85000) == 42478
    assert candidate(n = 80000) == 39982
    assert candidate(n = 8) == 4
    assert candidate(n = 20000) == 9996
    assert candidate(n = 5000) == 2500
    assert candidate(n = 75000) == 37487
    assert candidate(n = 9999) == 4995
    assert candidate(n = 50001) == 24986
    assert candidate(n = 200) == 100
    assert candidate(n = 400) == 199
    assert candidate(n = 9) == 4
    assert candidate(n = 500) == 249
    assert candidate(n = 7) == 4
    assert candidate(n = 25000) == 12495
