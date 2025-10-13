# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(m = 4,n = 4) == 1624
    assert candidate(m = 7,n = 7) == 72912
    assert candidate(m = 7,n = 8) == 213616
    assert candidate(m = 2,n = 2) == 56
    assert candidate(m = 4,n = 5) == 8776
    assert candidate(m = 5,n = 9) == 387488
    assert candidate(m = 1,n = 2) == 65
    assert candidate(m = 5,n = 5) == 7152
    assert candidate(m = 6,n = 6) == 26016
    assert candidate(m = 8,n = 9) == 281408
    assert candidate(m = 9,n = 9) == 140704
    assert candidate(m = 1,n = 1) == 9
    assert candidate(m = 2,n = 9) == 389488
    assert candidate(m = 8,n = 8) == 140704
    assert candidate(m = 3,n = 3) == 320
    assert candidate(m = 1,n = 9) == 389497
    assert candidate(m = 2,n = 3) == 376
    assert candidate(m = 5,n = 7) == 106080
    assert candidate(m = 6,n = 9) == 380336
    assert candidate(m = 1,n = 5) == 9161
    assert candidate(m = 5,n = 6) == 33168
    assert candidate(m = 6,n = 7) == 98928
    assert candidate(m = 3,n = 5) == 9096
    assert candidate(m = 3,n = 9) == 389432
    assert candidate(m = 7,n = 9) == 354320
    assert candidate(m = 3,n = 7) == 108024
    assert candidate(m = 5,n = 8) == 246784
    assert candidate(m = 4,n = 6) == 34792
    assert candidate(m = 2,n = 4) == 2000
    assert candidate(m = 2,n = 5) == 9152
    assert candidate(m = 4,n = 9) == 389112
    assert candidate(m = 3,n = 8) == 248728
    assert candidate(m = 2,n = 7) == 108080
    assert candidate(m = 1,n = 3) == 385
    assert candidate(m = 1,n = 8) == 248793
    assert candidate(m = 2,n = 8) == 248784
    assert candidate(m = 1,n = 4) == 2009
    assert candidate(m = 6,n = 8) == 239632
