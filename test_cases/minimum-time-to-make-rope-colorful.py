# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(colors = "abcabc",neededTime = [1, 2, 3, 1, 2, 3]) == 0
    assert candidate(colors = "aaaaa",neededTime = [5, 4, 3, 2, 1]) == 10
    assert candidate(colors = "abacabadabacaba",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 0
    assert candidate(colors = "aabaa",neededTime = [1, 2, 3, 4, 1]) == 2
    assert candidate(colors = "zzzz",neededTime = [1, 1, 1, 1]) == 3
    assert candidate(colors = "aaaa",neededTime = [10, 5, 4, 2]) == 11
    assert candidate(colors = "abcdef",neededTime = [1, 1, 1, 1, 1, 1]) == 0
    assert candidate(colors = "abaac",neededTime = [1, 2, 3, 4, 5]) == 3
    assert candidate(colors = "abc",neededTime = [1, 2, 3]) == 0
    assert candidate(colors = "abcdefg",neededTime = [1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(colors = "aaabbb",neededTime = [1, 2, 3, 4, 5, 6]) == 12
    assert candidate(colors = "aabbcc",neededTime = [1, 2, 3, 1, 2, 3]) == 4
    assert candidate(colors = "abcd",neededTime = [4, 3, 2, 1]) == 0
    assert candidate(colors = "bbbaaa",neededTime = [4, 9, 3, 8, 8, 9]) == 23
    assert candidate(colors = "ababab",neededTime = [1, 2, 3, 4, 5, 6]) == 0
    assert candidate(colors = "a",neededTime = [5]) == 0
    assert candidate(colors = "aabab",neededTime = [3, 5, 10, 7, 5]) == 3
    assert candidate(colors = "aaabbb",neededTime = [3, 5, 10, 7, 5, 3]) == 16
    assert candidate(colors = "a",neededTime = [1]) == 0
    assert candidate(colors = "zzzz",neededTime = [10, 1, 1, 100]) == 12
    assert candidate(colors = "abcabcabcabc",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 0
    assert candidate(colors = "ababababab",neededTime = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == 0
    assert candidate(colors = "aaaaaaaaaabbbbbbbbbb",neededTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 18
    assert candidate(colors = "aaabbbcccdddeee",neededTime = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 30
    assert candidate(colors = "aaabaaaabaaaaaaaabaa",neededTime = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 28
    assert candidate(colors = "ababaababaaba",neededTime = [1, 3, 5, 2, 4, 6, 3, 5, 7, 4, 6, 8, 5]) == 8
    assert candidate(colors = "aabbaa",neededTime = [1, 2, 3, 4, 5, 6]) == 9
    assert candidate(colors = "aaaabbbbccccdddd",neededTime = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 30
    assert candidate(colors = "abacabadabacabadabacabadabacabadabacabad",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 0
    assert candidate(colors = "aabaaabbaaaabaaa",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 76
    assert candidate(colors = "aaaabbbbcccc",neededTime = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 18
    assert candidate(colors = "abababababab",neededTime = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4]) == 0
    assert candidate(colors = "aabbccddeeff",neededTime = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 9
    assert candidate(colors = "aabccbaa",neededTime = [3, 5, 10, 7, 5, 3, 5, 3]) == 11
    assert candidate(colors = "aabbccddeeffgg",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 49
    assert candidate(colors = "aaaaaaaaaa",neededTime = [1, 10, 100, 1000, 10000, 1, 10, 100, 1000, 10000]) == 12222
    assert candidate(colors = "zzzzzzzzzz",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(colors = "bbbaaabbb",neededTime = [10, 1, 1, 1, 10, 10, 1, 1, 10]) == 15
    assert candidate(colors = "xyzzzyx",neededTime = [1, 2, 3, 4, 5, 6, 7]) == 7
    assert candidate(colors = "aaaaaaaaaaaa",neededTime = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989]) == 109934
    assert candidate(colors = "aabbbaaabbbaaa",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 65
    assert candidate(colors = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",neededTime = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 0
    assert candidate(colors = "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 180
    assert candidate(colors = "abccbaabccba",neededTime = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]) == 7
    assert candidate(colors = "aabbaa",neededTime = [10, 5, 1, 1, 5, 10]) == 11
    assert candidate(colors = "abcabcabc",neededTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(colors = "abcdefghij",neededTime = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 0
    assert candidate(colors = "aabbccddeeffgghhiijjkk",neededTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(colors = "abcabcabcabc",neededTime = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 0
    assert candidate(colors = "aaabbbcccddd",neededTime = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 20
    assert candidate(colors = "aaaabbbb",neededTime = [1, 2, 3, 4, 5, 6, 7, 8]) == 24
    assert candidate(colors = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 676
    assert candidate(colors = "abababababababababab",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 0
    assert candidate(colors = "aabccbaabccbaabc",neededTime = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]) == 13
    assert candidate(colors = "abcabcabcabcabcabcabc",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 0
    assert candidate(colors = "abababababababababab",neededTime = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 4, 6, 3, 7, 2, 8, 1, 9, 1, 9]) == 0
    assert candidate(colors = "aabaaaaba",neededTime = [1, 2, 1, 1, 1, 1, 1, 2, 1]) == 4
    assert candidate(colors = "ababababab",neededTime = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4]) == 0
    assert candidate(colors = "aabbaa",neededTime = [10, 1, 10, 2, 10, 3]) == 6
    assert candidate(colors = "abcabcabcabc",neededTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3]) == 0
    assert candidate(colors = "ababaababa",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert candidate(colors = "abcabcabcabcabcabc",neededTime = [6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(colors = "aaaabbbbccccdddd",neededTime = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 24
    assert candidate(colors = "aabbccddeeffgg",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 49
    assert candidate(colors = "aabbccddeeffgg",neededTime = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 33
    assert candidate(colors = "aaaaaaaaaabbbbbbbbbb",neededTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 18
    assert candidate(colors = "aabbaabbcc",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(colors = "aaabaaaaba",neededTime = [5, 5, 5, 1, 1, 5, 5, 1, 1, 5]) == 17
    assert candidate(colors = "zzzzzzzzz",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 36
    assert candidate(colors = "abcdabcde",neededTime = [1, 2, 3, 4, 1, 2, 3, 4, 5]) == 0
    assert candidate(colors = "abcdefghijklmnopqrstuvwxyz",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 0
    assert candidate(colors = "aaabaaaabaaab",neededTime = [3, 2, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 11
    assert candidate(colors = "abcdeffedcba",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]) == 6
    assert candidate(colors = "aabbaaabbbaaa",neededTime = [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1]) == 9
    assert candidate(colors = "zzzzzzzzzz",neededTime = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(colors = "abcabcabcabc",neededTime = [10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]) == 0
    assert candidate(colors = "ababababab",neededTime = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 0
    assert candidate(colors = "abababababab",neededTime = [1, 9, 2, 8, 3, 7, 4, 6, 5, 10, 6, 1]) == 0
    assert candidate(colors = "abcabcabcabcabcabcabcabcabcabc",neededTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(colors = "aabbbcccaabbcc",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 54
    assert candidate(colors = "aabbaabbaabb",neededTime = [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]) == 120
    assert candidate(colors = "aabbccddeeff",neededTime = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(colors = "abcabcabcabc",neededTime = [2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 0
    assert candidate(colors = "zzzzz",neededTime = [1, 2, 3, 4, 5]) == 10
    assert candidate(colors = "aabbccddeeffgg",neededTime = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(colors = "zzzzzzzzzz",neededTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 45
    assert candidate(colors = "aabacbacba",neededTime = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 1
    assert candidate(colors = "abcdabcda",neededTime = [1, 2, 3, 4, 1, 2, 3, 4, 1]) == 0
    assert candidate(colors = "aabbccddeeff",neededTime = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 6
    assert candidate(colors = "aaaabbbb",neededTime = [1, 2, 3, 4, 1, 2, 3, 4]) == 12
    assert candidate(colors = "abcdefghij",neededTime = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
