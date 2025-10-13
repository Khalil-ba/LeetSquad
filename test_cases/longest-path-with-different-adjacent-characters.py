# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(parent = [-1, 0, 0, 2, 2, 2],s = "abbccc") == 4
    assert candidate(parent = [-1, 0, 0, 0],s = "aabc") == 3
    assert candidate(parent = [-1, 0, 0, 1, 1, 2],s = "abacbe") == 3
    assert candidate(parent = [-1, 0, 1, 2, 3, 4, 5],s = "abcdefg") == 7
    assert candidate(parent = [-1, 0, 0, 0, 0, 0, 0],s = "abcdefg") == 3
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "aabbaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 5
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],s = "abcdefghijklmnopqrstuvwxyz") == 8
    assert candidate(parent = [-1, 0, 1, 2, 3, 0, 6, 7, 8, 2, 10, 11, 12, 1, 14, 15, 16, 0, 18, 19, 20, 3, 22, 23, 24, 4, 26, 27, 28, 5, 30, 31, 32, 6, 34, 35, 36, 7, 38, 39, 40, 8, 42, 43, 44, 9, 46, 47, 48, 10, 50, 51, 52, 11, 54, 55, 56, 12, 58, 59, 60],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 8
    assert candidate(parent = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],s = "abcdefghijklmnopqrstuvwxyz") == 21
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],s = "aabbccddeeffgghhiiiijjjjkkkkllllmmmmnnnnoooppqqrrssttuuvvwwxxyyzz") == 7
    assert candidate(parent = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],s = "abcdefghijklmno") == 14
    assert candidate(parent = [-1, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],s = "abcdefghijklmnopqrstuvwxyz") == 7
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 10
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21],s = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba") == 10
    assert candidate(parent = [-1, 0, 0, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13],s = "abcdefghijklmnopqrstuvwxyzabcdefghijk") == 8
    assert candidate(parent = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],s = "aabbaaccddcceeddffgeee") == 5
    assert candidate(parent = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],s = "abcabcabcabcabcabc") == 5
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba") == 9
    assert candidate(parent = [-1, 0, 0, 0, 1, 1, 1, 2, 2, 3],s = "abacabadaba") == 5
    assert candidate(parent = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "abacabadacadaeafagahaiajakalalamanaoapaqara") == 7
    assert candidate(parent = [-1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5],s = "ababababababababababababababababababababababababababababababababababababababababababa") == 5
    assert candidate(parent = [-1, 0, 0, 0, 1, 1, 2, 2, 3, 4],s = "abcdefghij") == 6
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 4, 5, 6],s = "aabbccddeee") == 5
    assert candidate(parent = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 21, 22, 23, 24, 25, 26, 27, 28, 29],s = "zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29],s = "abcdefghijklmnopqrstuvabcdefghijklmnopqrstuvabcdefghijklmnopqrstuvabcdefghijklmnopqrstuv") == 11
    assert candidate(parent = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],s = "abacabadabacabadabacabadabacabadabacabadabacaba") == 32
    assert candidate(parent = [-1, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21],s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1
    assert candidate(parent = [-1, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],s = "abcdefghijklmnopqrstuvwx") == 7
    assert candidate(parent = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],s = "abcdefghijklmnopqrstuvwxypq") == 21
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 0, 37, 38, 39, 40, 41, 42, 43, 44, 45],s = "abcdefghijklmnopqrstuvwxypqabcdefghijklmnopqrstuvwxypq") == 13
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnop") == 9
    assert candidate(parent = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],s = "abcdefghijklmnopqrstuvwxyz") == 16
    assert candidate(parent = [-1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],s = "aaaaabbbbbcccccddeeeeffffgghhhhiijjjj") == 3
    assert candidate(parent = [-1, 0, 0, 0, 1, 1, 2, 2, 3, 3],s = "aababbccdd") == 3
    assert candidate(parent = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 31
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4],s = "abcdefghij") == 6
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 8
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "abacabadacadaeafagahaiajakalalamanaoapaqara") == 7
    assert candidate(parent = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],s = "abcdefghijklmnopqrstuvwxyz") == 5
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4],s = "aaabbbcccdd") == 5
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],s = "abacabadabacaba") == 5
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 8
    assert candidate(parent = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19, 0, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 11
    assert candidate(parent = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == 10
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "abcdefghijklmnopqrstuvwxyzzzzzzzzzzzzzzzzzzzz") == 9
    assert candidate(parent = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 9
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14],s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 7
    assert candidate(parent = [-1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],s = "abcdeabcdeabcde") == 5
    assert candidate(parent = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49],s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 13
