# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 8) == 3
    assert candidate(n = 15) == 5
    assert candidate(n = 4) == 2
    assert candidate(n = 2147483647) == 32
    assert candidate(n = 1) == 0
    assert candidate(n = 1000000000) == 38
    assert candidate(n = 7) == 4
    assert candidate(n = 317) == 11
    assert candidate(n = 63) == 7
    assert candidate(n = 21) == 6
    assert candidate(n = 32767) == 16
    assert candidate(n = 50000) == 20
    assert candidate(n = 2047) == 12
    assert candidate(n = 16383) == 15
    assert candidate(n = 5) == 3
    assert candidate(n = 123) == 9
    assert candidate(n = 134217727) == 28
    assert candidate(n = 64) == 6
    assert candidate(n = 99) == 9
    assert candidate(n = 1073741823) == 31
    assert candidate(n = 23) == 6
    assert candidate(n = 51) == 8
    assert candidate(n = 16777215) == 25
    assert candidate(n = 101) == 9
    assert candidate(n = 99999999) == 32
    assert candidate(n = 2048) == 11
    assert candidate(n = 999) == 13
    assert candidate(n = 27) == 7
    assert candidate(n = 8191) == 14
    assert candidate(n = 1023) == 11
    assert candidate(n = 19) == 6
    assert candidate(n = 65535) == 17
    assert candidate(n = 513) == 10
    assert candidate(n = 127) == 8
    assert candidate(n = 1048575) == 21
    assert candidate(n = 31) == 6
    assert candidate(n = 1000000) == 24
