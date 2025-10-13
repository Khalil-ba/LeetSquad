# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 5000000) == 348513
    assert candidate(n = 1000) == 168
    assert candidate(n = 100) == 25
    assert candidate(n = 30) == 10
    assert candidate(n = 1500000) == 114155
    assert candidate(n = 1000000) == 78498
    assert candidate(n = 20) == 8
    assert candidate(n = 2) == 0
    assert candidate(n = 1) == 0
    assert candidate(n = 50) == 15
    assert candidate(n = 10) == 4
    assert candidate(n = 5) == 2
    assert candidate(n = 3) == 1
    assert candidate(n = 4999999) == 348512
    assert candidate(n = 10000) == 1229
    assert candidate(n = 17) == 6
    assert candidate(n = 7890123) == 532888
    assert candidate(n = 2000000) == 148933
    assert candidate(n = 4000000) == 283146
    assert candidate(n = 3141592) == 226277
    assert candidate(n = 499979) == 41537
    assert candidate(n = 10000000) == 664579
    assert candidate(n = 5000001) == 348513
    assert candidate(n = 18) == 7
    assert candidate(n = 5000) == 669
    assert candidate(n = 999983) == 78497
    assert candidate(n = 3000000) == 216816
    assert candidate(n = 789654) == 63183
    assert candidate(n = 31337) == 3378
    assert candidate(n = 104729) == 9999
    assert candidate(n = 500000) == 41538
    assert candidate(n = 1234567) == 95360
