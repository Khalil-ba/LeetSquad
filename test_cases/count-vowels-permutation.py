# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 1000) == 89945857
    assert candidate(n = 100) == 173981881
    assert candidate(n = 20000) == 759959057
    assert candidate(n = 200) == 670333618
    assert candidate(n = 10000) == 76428576
    assert candidate(n = 5000) == 598627501
    assert candidate(n = 2000) == 793084836
    assert candidate(n = 2) == 10
    assert candidate(n = 20) == 1151090
    assert candidate(n = 1) == 5
    assert candidate(n = 500) == 518032023
    assert candidate(n = 50) == 227130014
    assert candidate(n = 10) == 1739
    assert candidate(n = 5) == 68
    assert candidate(n = 15000) == 381635004
    assert candidate(n = 3) == 19
    assert candidate(n = 12345) == 480007966
    assert candidate(n = 4) == 35
    assert candidate(n = 30000) == 770607143
    assert candidate(n = 75) == 467397509
    assert candidate(n = 150) == 965179800
    assert candidate(n = 6) == 129
    assert candidate(n = 19999) == 706457669
    assert candidate(n = 19000) == 70562691
    assert candidate(n = 18000) == 596349393
    assert candidate(n = 25) == 29599477
