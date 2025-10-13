# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(n = 5,s1 = "apple",s2 = "zebra",evil = "app") == 11220078
    assert candidate(n = 5,s1 = "apple",s2 = "appla",evil = "appl") == 0
    assert candidate(n = 3,s1 = "aaa",s2 = "zzz",evil = "abc") == 17575
    assert candidate(n = 5,s1 = "aaaaa",s2 = "zzzzz",evil = "abc") == 11879348
    assert candidate(n = 10,s1 = "abcdefghij",s2 = "abcdefghij",evil = "ghij") == 0
    assert candidate(n = 5,s1 = "apple",s2 = "zebra",evil = "dog") == 11219789
    assert candidate(n = 2,s1 = "gx",s2 = "gz",evil = "x") == 2
    assert candidate(n = 3,s1 = "abc",s2 = "xyz",evil = "def") == 16169
    assert candidate(n = 8,s1 = "leetcode",s2 = "leetgoes",evil = "leet") == 0
    assert candidate(n = 3,s1 = "aaa",s2 = "zzz",evil = "xyz") == 17575
    assert candidate(n = 2,s1 = "aa",s2 = "da",evil = "b") == 51
    assert candidate(n = 3,s1 = "abc",s2 = "xyz",evil = "de") == 16120
    assert candidate(n = 10,s1 = "aaaaaaaaaa",s2 = "zzzzzzzzzz",evil = "mnop") == 932258852
    assert candidate(n = 10,s1 = "abcdefghij",s2 = "zzzzzzzzzz",evil = "mnop") == 67339166
    assert candidate(n = 25,s1 = "abcdefghijklmnopqrstuvwxyz",s2 = "abcdefghijklmnopqrstuvwxyz",evil = "abcde") == 0
    assert candidate(n = 45,s1 = "abcdefghijklmnopqrstuvwxyzabcdefghij",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",evil = "mnopqr") == 720631236
    assert candidate(n = 6,s1 = "aaaaaa",s2 = "zzzzzz",evil = "ab") == 306634951
    assert candidate(n = 20,s1 = "aaabaaabaaabaaabaa",s2 = "zzzzzzzzzzzzzzzzzzzz",evil = "aaa") == 357553640
    assert candidate(n = 35,s1 = "applepieapplepieapplepieapplepie",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",evil = "apple") == 695022504
    assert candidate(n = 7,s1 = "aaaaaaa",s2 = "zzzzzzz",evil = "abc") == 29525318
    assert candidate(n = 20,s1 = "abcdabcdabcdabcdabcd",s2 = "zzzzzzzzzzzzzzzzzzzz",evil = "zabcd") == 426896930
    assert candidate(n = 10,s1 = "abcdefghij",s2 = "abcdefghiz",evil = "ghi") == 0
    assert candidate(n = 15,s1 = "abcdefghijklnmop",s2 = "abcdefghijklnmopqrstuvwxyz",evil = "mnop") == 1
    assert candidate(n = 30,s1 = "abcdefghijklmnopqrstuvwxyzabcde",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",evil = "vwxyz") == 858527385
    assert candidate(n = 50,s1 = "leetcodeleetcodeleetcodeleetcodeleetcode",s2 = "leetgoesleetgoesleetgoesleetgoesleetgoes",evil = "leet") == 0
    assert candidate(n = 40,s1 = "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyzzz",s2 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",evil = "mnopqr") == 438601268
    assert candidate(n = 10,s1 = "abcdefghij",s2 = "zjklmnopqr",evil = "mnop") == 922212598
    assert candidate(n = 40,s1 = "abcdefghijabcdefghijabcdefghijabcdefghij",s2 = "zjklmnopqrzjklmnopqrzjklmnopqrzjklmnopqr",evil = "mnopqr") == 54391096
    assert candidate(n = 5,s1 = "aaaaa",s2 = "zzzzz",evil = "b") == 9765625
