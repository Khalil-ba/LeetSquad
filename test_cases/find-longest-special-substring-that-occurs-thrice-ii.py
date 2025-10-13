# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "zzzzzzzzz") == 7
    assert candidate(s = "aaabbbccc") == 1
    assert candidate(s = "aabbbcccaaa") == 2
    assert candidate(s = "abcdef") == -1
    assert candidate(s = "abacabadabacaba") == 1
    assert candidate(s = "abcabcabc") == 1
    assert candidate(s = "abcaba") == 1
    assert candidate(s = "aaaaabbbbccccc") == 3
    assert candidate(s = "aabbaabbcc") == 1
    assert candidate(s = "aaaaaaaaaa") == 8
    assert candidate(s = "aaaabbbbcccc") == 2
    assert candidate(s = "abababababa") == 1
    assert candidate(s = "abcdabcabcd") == 1
    assert candidate(s = "aabbccddeeefff") == 1
    assert candidate(s = "aabbccddeeffgg") == -1
    assert candidate(s = "aaaa") == 2
    assert candidate(s = "aaabaaa") == 2
    assert candidate(s = "aaaaabbbbbaaaa") == 4
    assert candidate(s = "nnnhaaaannn") == 2
    assert candidate(s = "zzzzz") == 3
    assert candidate(s = "aabbaabbccddccddc") == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1
