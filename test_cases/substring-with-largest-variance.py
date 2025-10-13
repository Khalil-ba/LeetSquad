# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "zzzzzzy") == 5
    assert candidate(s = "zyzzyzyzy") == 2
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(s = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "abbaabbaabba") == 2
    assert candidate(s = "abababab") == 1
    assert candidate(s = "aaaaa") == 0
    assert candidate(s = "a") == 0
    assert candidate(s = "abcabcabc") == 1
    assert candidate(s = "zzyzxzyzyzxzyzxzyzxzyzxzyzxzyzxzyz") == 11
    assert candidate(s = "abcabcabcabc") == 1
    assert candidate(s = "abcde") == 0
    assert candidate(s = "leetcode") == 2
    assert candidate(s = "xyzxyzxyz") == 1
    assert candidate(s = "abccccccc") == 6
    assert candidate(s = "zzzzzzzzzz") == 0
    assert candidate(s = "zzzzzyyyyxxxxwwwwvvvvuuuuttttssssrrrrqqqqppppllllkkkkjjjjiiiihhhhggggffffffeee ddcccbbbbaaaa") == 5
    assert candidate(s = "aabbcc") == 1
    assert candidate(s = "mississippi") == 3
    assert candidate(s = "abcdefghij") == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "aabbccddeeffgghhiijj") == 1
    assert candidate(s = "aabbaaabb") == 3
    assert candidate(s = "abacaba") == 3
    assert candidate(s = "aababbb") == 3
