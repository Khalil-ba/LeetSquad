# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "pqrstu",p = "psu",removable = [5, 4, 3, 2, 1, 0]) == 0
    assert candidate(s = "abcdefghij",p = "acegi",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert candidate(s = "deeddeede",p = "dee",removable = [5, 3, 4, 6]) == 4
    assert candidate(s = "deeedbbcccbdaa",p = "ddccbb",removable = [8, 2, 3, 0, 7]) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "acegikmoqsuwy",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 13
    assert candidate(s = "zzzzzzzzzz",p = "zz",removable = [1, 3, 5, 7]) == 4
    assert candidate(s = "aaaabbbb",p = "ab",removable = [2, 3, 4, 5]) == 4
    assert candidate(s = "abcdef",p = "abc",removable = [5, 4, 3, 2, 1, 0]) == 3
    assert candidate(s = "aabcbcb",p = "abc",removable = [3, 1, 0, 4]) == 2
    assert candidate(s = "abcdxyz",p = "ad",removable = [0, 1, 2, 3, 4, 5, 6]) == 0
    assert candidate(s = "abcacb",p = "ab",removable = [3, 1, 0]) == 2
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "acegikmoqsuwy",removable = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 0
    assert candidate(s = "ababababab",p = "aaaa",removable = [0, 2, 4, 6, 8]) == 1
    assert candidate(s = "mississippi",p = "issi",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert candidate(s = "zpqom",p = "z",removable = [0, 1, 2, 3, 4]) == 0
    assert candidate(s = "abcab",p = "abc",removable = [0, 1, 2, 3, 4]) == 0
    assert candidate(s = "xyz",p = "xyz",removable = [0, 1, 2]) == 0
    assert candidate(s = "abcdef",p = "af",removable = [1, 2, 3, 4]) == 4
    assert candidate(s = "abcbddddd",p = "abcd",removable = [3, 2, 1, 4, 5, 6]) == 1
    assert candidate(s = "zazbzczdzezfzgzhzi",p = "abcdefg",removable = [0, 2, 4, 6, 8, 10, 12, 14, 16]) == 9
    assert candidate(s = "pythonprogramming",p = "ppn",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 0
    assert candidate(s = "thisisaverylongstringthatweneedtoremovesomecharactersfrom",p = "thisisalong",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0
    assert candidate(s = "mississippi",p = "miss",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(s = "onetwothreefourfivesixseveneightnine",p = "onefivesix",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == 0
    assert candidate(s = "abcdefghijklnmopqrstuvwxyz",p = "zyxwvutsrqponmlkjihgfedcba",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
    assert candidate(s = "abracadabra",p = "aca",removable = [1, 3, 5, 7, 9, 10]) == 5
    assert candidate(s = "leetcodeleetcodeleetcode",p = "leetcode",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]) == 16
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",p = "qwerty",removable = [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35]) == 0
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzz",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 30
    assert candidate(s = "abracadabra",p = "aa",removable = [0, 2, 4, 6, 8, 10]) == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzz",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 29
    assert candidate(s = "abacabadabacaba",p = "abc",removable = [2, 5, 8, 11, 14]) == 5
    assert candidate(s = "abcdefghijklm",p = "abc",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(s = "zzzzzzzzzz",p = "zz",removable = [1, 3, 5, 7, 9]) == 5
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog",p = "quickbrownfox",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 3
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "abcdefghijklmnopqrstuvwxyz",removable = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",p = "zzzzz",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 15
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "az",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 0
    assert candidate(s = "abcdeffedcba",p = "abcdef",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 0
    assert candidate(s = "mississippi",p = "issi",removable = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(s = "abcdefghijklmno",p = "def",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 3
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",p = "zzzz",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 16
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",p = "pus",removable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]) == 7
    assert candidate(s = "aaaaaaabbbbbbb",p = "aabbb",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 5
    assert candidate(s = "abcdefghijklmnop",p = "mnop",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 12
    assert candidate(s = "xyxzyzyzyxzyzyzyx",p = "xyz",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 9
    assert candidate(s = "banana",p = "ban",removable = [0, 2, 4]) == 0
    assert candidate(s = "aaaabbbbccccdddd",p = "abcd",removable = [3, 7, 11, 15]) == 4
    assert candidate(s = "abracadabra",p = "aca",removable = [1, 3, 5, 7, 9]) == 5
    assert candidate(s = "banana",p = "ban",removable = [0, 1, 2, 3, 4, 5]) == 0
    assert candidate(s = "abcdefffffghijklmnopqrstuvwxyz",p = "acegikmoqsuwy",removable = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) == 10
    assert candidate(s = "aabbccddeeffgghhii",p = "abcdefghi",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == 9
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "abcdefghijklmnopqrstuvwxzy",removable = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == 0
    assert candidate(s = "abcdabcdabcd",p = "abc",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 8
    assert candidate(s = "thisisateststring",p = "tst",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 21, 22, 23, 24]) == 5
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",p = "qz",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 0
    assert candidate(s = "abcabcabcabcabc",p = "abcabcabc",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == 4
    assert candidate(s = "xyzzxyzzxyzz",p = "xyz",removable = [0, 2, 4, 6, 8, 10]) == 4
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "abcdefghijklmnopqrstuvwxyz",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]) == 1
    assert candidate(s = "aaaaaaaaaaa",p = "aaaaa",removable = [1, 3, 5, 7, 9]) == 5
    assert candidate(s = "abcdabcdabcdabcdabcdabcd",p = "abcd",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 20
    assert candidate(s = "abababababababababab",p = "aabbaabb",removable = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == 4
    assert candidate(s = "hellohellohellohello",p = "heo",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]) == 15
    assert candidate(s = "xyzzxyzzxyzz",p = "xyz",removable = [1, 3, 5, 7, 9, 11]) == 4
    assert candidate(s = "mississippi",p = "issi",removable = [3, 1, 0, 4, 5, 2, 6, 7, 8, 9, 10]) == 3
    assert candidate(s = "abracadabra",p = "ac",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
    assert candidate(s = "bcaabcbabcabc",p = "abc",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",p = "zzz",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "bdfhjlnprtvxz",removable = [1, 5, 9, 13, 17, 21, 25]) == 0
    assert candidate(s = "abcdeffedcba",p = "abcdef",removable = [0, 2, 4, 6, 8, 10]) == 0
    assert candidate(s = "findinganagrams",p = "anag",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == 3
    assert candidate(s = "mississippi",p = "miss",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "adgjmpsvy",removable = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == 0
    assert candidate(s = "hellotherehowareyou",p = "heoy",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == 4
    assert candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "xyz",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 0
    assert candidate(s = "aaaaabbbbbcccc",p = "abc",removable = [5, 6, 7, 8, 9, 10]) == 4
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",p = "pneumo",removable = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54]) == 0
    assert candidate(s = "thisisaverylongstring",p = "tils",removable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 3
    assert candidate(s = "leetcodeleetcodeleetcodeleetcode",p = "leetcodelt",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]) == 16
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "acegikmoqsuwy",removable = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 12
    assert candidate(s = "abcdefghijabcdefghij",p = "acegik",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
    assert candidate(s = "nnnnoooooommmm",p = "nom",removable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 3
