# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 3) == 27
    assert candidate(n = 100000) == 757631812
    assert candidate(n = 100) == 310828084
    assert candidate(n = 12) == 505379714
    assert candidate(n = 10000) == 356435599
    assert candidate(n = 20) == 632668867
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 499361981
    assert candidate(n = 10) == 462911642
    assert candidate(n = 5) == 1765
    assert candidate(n = 15000) == 760107204
    assert candidate(n = 99999) == 880407397
    assert candidate(n = 12345) == 836722104
    assert candidate(n = 67890) == 121883656
    assert candidate(n = 32767) == 351669993
    assert candidate(n = 90000) == 333354001
    assert candidate(n = 50000) == 305317209
    assert candidate(n = 60000) == 841047212
    assert candidate(n = 30000) == 789968936
    assert candidate(n = 80000) == 801174769
    assert candidate(n = 8192) == 853721666
    assert candidate(n = 65536) == 273282097
    assert candidate(n = 5000) == 754628255
    assert candidate(n = 75000) == 363627085
    assert candidate(n = 40000) == 162370743
    assert candidate(n = 65535) == 183542430
    assert candidate(n = 500) == 715412131
    assert candidate(n = 25000) == 110872861
