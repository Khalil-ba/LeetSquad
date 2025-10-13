# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 0) == 1
    assert candidate(n = 8) == 7
    assert candidate(n = 100) == 27
    assert candidate(n = 15) == 0
    assert candidate(n = 31) == 0
    assert candidate(n = 123456789) == 10760938
    assert candidate(n = 1) == 0
    assert candidate(n = 7) == 0
    assert candidate(n = 10) == 5
    assert candidate(n = 5) == 2
    assert candidate(n = 123) == 4
    assert candidate(n = 894567890) == 179173933
    assert candidate(n = 890123456) == 183618367
    assert candidate(n = 131071) == 0
    assert candidate(n = 897543210) == 176198613
    assert candidate(n = 67108863) == 0
    assert candidate(n = 2147483647) == 0
    assert candidate(n = 67890) == 63181
    assert candidate(n = 32767) == 0
    assert candidate(n = 4294967295) == 0
    assert candidate(n = 134217727) == 0
    assert candidate(n = 891011121) == 182730702
    assert candidate(n = 1073741823) == 0
    assert candidate(n = 1024) == 1023
    assert candidate(n = 16777215) == 0
    assert candidate(n = 2048) == 2047
    assert candidate(n = 255) == 0
    assert candidate(n = 1023) == 0
    assert candidate(n = 65535) == 0
    assert candidate(n = 1000000000) == 73741823
    assert candidate(n = 987654321) == 86087502
    assert candidate(n = 1048575) == 0
    assert candidate(n = 500000000) == 36870911
    assert candidate(n = 536870911) == 0
    assert candidate(n = 543210987) == 530530836
    assert candidate(n = 33554431) == 0
    assert candidate(n = 54321) == 11214
