# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(num = 31) == 0
    assert candidate(num = 10) == 5
    assert candidate(num = 32) == 31
    assert candidate(num = 5) == 2
    assert candidate(num = 1023) == 0
    assert candidate(num = 1) == 0
    assert candidate(num = 100) == 27
    assert candidate(num = 2147483647) == 0
    assert candidate(num = 15) == 0
    assert candidate(num = 8191) == 0
    assert candidate(num = 4294967295) == 0
    assert candidate(num = 33) == 30
    assert candidate(num = 4095) == 0
    assert candidate(num = 1048575) == 0
    assert candidate(num = 123456789) == 10760938
    assert candidate(num = 65535) == 0
    assert candidate(num = 500) == 11
    assert candidate(num = 2097151) == 0
    assert candidate(num = 131071) == 0
    assert candidate(num = 16777215) == 0
    assert candidate(num = 2147483646) == 1
    assert candidate(num = 134217728) == 134217727
    assert candidate(num = 4194303) == 0
    assert candidate(num = 2047) == 0
    assert candidate(num = 987654321) == 86087502
    assert candidate(num = 89123456) == 45094271
    assert candidate(num = 255) == 0
    assert candidate(num = 8388607) == 0
    assert candidate(num = 1024) == 1023
    assert candidate(num = 100000) == 31071
    assert candidate(num = 1073741823) == 0
    assert candidate(num = 262143) == 0
    assert candidate(num = 268435455) == 0
    assert candidate(num = 123456) == 7615
    assert candidate(num = 1000000) == 48575
    assert candidate(num = 8) == 7
    assert candidate(num = 32767) == 0
    assert candidate(num = 524287) == 0
    assert candidate(num = 134217727) == 0
    assert candidate(num = 4294967294) == 1
    assert candidate(num = 33554431) == 0
    assert candidate(num = 536870911) == 0
    assert candidate(num = 67108863) == 0
    assert candidate(num = 1073741824) == 1073741823
