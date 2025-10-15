def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "bb",k = 2,letter = "b",repetition = 2) == "bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bb",k = 2,letter = "b",repetition = 2) == "bb": {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode",k = 4,letter = "e",repetition = 2) == "ecde"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode",k = 4,letter = "e",repetition = 2) == "ecde": {e}')
    
    total += 1
    try:
        result = candidate(s = "leet",k = 3,letter = "e",repetition = 1) == "eet"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leet",k = 3,letter = "e",repetition = 1) == "eet": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc",k = 3,letter = "a",repetition = 1) == "aab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc",k = 3,letter = "a",repetition = 1) == "aab": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabad",k = 4,letter = "a",repetition = 2) == "aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabad",k = 4,letter = "a",repetition = 2) == "aaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",k = 3,letter = "z",repetition = 3) == "zzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",k = 3,letter = "z",repetition = 3) == "zzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba",k = 5,letter = "d",repetition = 1) == "abcda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba",k = 5,letter = "d",repetition = 1) == "abcda": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzaaaaa",k = 5,letter = "a",repetition = 3) == "aaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzaaaaa",k = 5,letter = "a",repetition = 3) == "aaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "apple",k = 3,letter = "p",repetition = 1) == "ape"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "apple",k = 3,letter = "p",repetition = 1) == "ape": {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 7,letter = "a",repetition = 3) == "aaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 7,letter = "a",repetition = 3) == "aaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "azbzczdz",k = 4,letter = "z",repetition = 2) == "abzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "azbzczdz",k = 4,letter = "z",repetition = 2) == "abzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba",k = 5,letter = "c",repetition = 1) == "abcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba",k = 5,letter = "c",repetition = 1) == "abcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",k = 5,letter = "z",repetition = 2) == "xxyzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",k = 5,letter = "z",repetition = 2) == "xxyzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba",k = 5,letter = "c",repetition = 2) == "abcca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba",k = 5,letter = "c",repetition = 2) == "abcca": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",k = 2,letter = "z",repetition = 2) == "zz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",k = 2,letter = "z",repetition = 2) == "zz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 6,letter = "a",repetition = 2) == "aababc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 6,letter = "a",repetition = 2) == "aababc": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 9,letter = "b",repetition = 3) == "ababcabcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 9,letter = "b",repetition = 3) == "ababcabcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "elephant",k = 4,letter = "e",repetition = 1) == "eant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "elephant",k = 4,letter = "e",repetition = 1) == "eant": {e}')
    
    total += 1
    try:
        result = candidate(s = "zazbzazbzazb",k = 8,letter = "z",repetition = 4) == "abzazbzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazbzazbzazb",k = 8,letter = "z",repetition = 4) == "abzazbzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "babcbabcbabc",k = 5,letter = "b",repetition = 3) == "aabbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babcbabcbabc",k = 5,letter = "b",repetition = 3) == "aabbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcbaabcdedcbaabcdedcba",k = 15,letter = "c",repetition = 3) == "aaabcaabcdedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcbaabcdedcbaabcdedcba",k = 15,letter = "c",repetition = 3) == "aaabcaabcdedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 20,letter = "c",repetition = 4) == "aaaaaaaaaaaabbbbcccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 20,letter = "c",repetition = 4) == "aaaaaaaaaaaabbbbcccc": {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbbcccccc",k = 12,letter = "b",repetition = 4) == "aaaaaabbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbbcccccc",k = 12,letter = "b",repetition = 4) == "aaaaaabbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 26,letter = "z",repetition = 1) == "aabcdefghijklmnopqrstuvwxz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 26,letter = "z",repetition = 1) == "aabcdefghijklmnopqrstuvwxz": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 13,letter = "m",repetition = 1) == "abcdefghijklm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 13,letter = "m",repetition = 1) == "abcdefghijklm": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 5,letter = "i",repetition = 2) == "iiipi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 5,letter = "i",repetition = 2) == "iiipi": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba",k = 26,letter = "a",repetition = 2) == "ayxwvutsrqponmlkjihgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba",k = 26,letter = "a",repetition = 2) == "ayxwvutsrqponmlkjihgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababab",k = 10,letter = "a",repetition = 3) == "aaaaaaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababab",k = 10,letter = "a",repetition = 3) == "aaaaaaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxyzyxyzyxyzyzyzyxyzyzyzyzyzyxyzyxyzyzyzyzyzy",k = 15,letter = "x",repetition = 3) == "xxxxxxxyyyyzyzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxyzyxyzyxyzyzyzyxyzyzyzyzyzyxyzyxyzyzyzyzyzy",k = 15,letter = "x",repetition = 3) == "xxxxxxxyyyyzyzy": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 8,letter = "c",repetition = 3) == "aabbccd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 8,letter = "c",repetition = 3) == "aabbccd": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzaaaaabbbb",k = 10,letter = "a",repetition = 4) == "zaaaaabbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzaaaaabbbb",k = 10,letter = "a",repetition = 4) == "zaaaaabbbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 4,letter = "i",repetition = 2) == "iiii"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 4,letter = "i",repetition = 2) == "iiii": {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 6,letter = "i",repetition = 2) == "iiippi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 6,letter = "i",repetition = 2) == "iiippi": {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50,letter = "z",repetition = 10) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50,letter = "z",repetition = 10) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz": {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20,letter = "a",repetition = 2) == "aabbccddeeffgghhiijj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20,letter = "a",repetition = 2) == "aabbccddeeffgghhiijj": {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",k = 4,letter = "a",repetition = 2) == "aana"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",k = 4,letter = "a",repetition = 2) == "aana": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 8,letter = "b",repetition = 3) == "abababcd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 8,letter = "b",repetition = 3) == "abababcd": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10,letter = "m",repetition = 2) == "abcdefghm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10,letter = "m",repetition = 2) == "abcdefghm": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",k = 7,letter = "a",repetition = 3) == "aaaabra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",k = 7,letter = "a",repetition = 3) == "aaaabra": {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxzyxzyx",k = 5,letter = "x",repetition = 2) == "xxzyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxzyxzyx",k = 5,letter = "x",repetition = 2) == "xxzyx": {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra",k = 12,letter = "a",repetition = 4) == "aaaaaaaaabra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra",k = 12,letter = "a",repetition = 4) == "aaaaaaaaabra": {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 5,letter = "e",repetition = 1) == "acear"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 5,letter = "e",repetition = 1) == "acear": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcabc",k = 9,letter = "c",repetition = 3) == "aabcabcac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcabc",k = 9,letter = "c",repetition = 3) == "aabcabcac": {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwerty",k = 12,letter = "r",repetition = 2) == "erabnmqwerty"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwerty",k = 12,letter = "r",repetition = 2) == "erabnmqwerty": {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyx",k = 7,letter = "y",repetition = 3) == "xyyyyyx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyx",k = 7,letter = "y",repetition = 3) == "xyyyyyx": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "bb",k = 2,letter = "b",repetition = 2) == "bb"
    assert candidate(s = "leetcode",k = 4,letter = "e",repetition = 2) == "ecde"
    assert candidate(s = "leet",k = 3,letter = "e",repetition = 1) == "eet"
    assert candidate(s = "aabbc",k = 3,letter = "a",repetition = 1) == "aab"
    assert candidate(s = "abacabad",k = 4,letter = "a",repetition = 2) == "aaaa"
    assert candidate(s = "zzzzz",k = 3,letter = "z",repetition = 3) == "zzz"
    assert candidate(s = "abcdedcba",k = 5,letter = "d",repetition = 1) == "abcda"
    assert candidate(s = "zzzzzaaaaa",k = 5,letter = "a",repetition = 3) == "aaaaa"
    assert candidate(s = "apple",k = 3,letter = "p",repetition = 1) == "ape"
    assert candidate(s = "abacabadabacaba",k = 7,letter = "a",repetition = 3) == "aaaaaaa"
    assert candidate(s = "azbzczdz",k = 4,letter = "z",repetition = 2) == "abzz"
    assert candidate(s = "abcdedcba",k = 5,letter = "c",repetition = 1) == "abcba"
    assert candidate(s = "xyzxyzxyz",k = 5,letter = "z",repetition = 2) == "xxyzz"
    assert candidate(s = "abcdedcba",k = 5,letter = "c",repetition = 2) == "abcca"
    assert candidate(s = "zzzz",k = 2,letter = "z",repetition = 2) == "zz"
    assert candidate(s = "abcabcabc",k = 6,letter = "a",repetition = 2) == "aababc"
    assert candidate(s = "abcdabcdabcd",k = 9,letter = "b",repetition = 3) == "ababcabcd"
    assert candidate(s = "elephant",k = 4,letter = "e",repetition = 1) == "eant"
    assert candidate(s = "zazbzazbzazb",k = 8,letter = "z",repetition = 4) == "abzazbzz"
    assert candidate(s = "babcbabcbabc",k = 5,letter = "b",repetition = 3) == "aabbb"
    assert candidate(s = "abcdedcbaabcdedcbaabcdedcba",k = 15,letter = "c",repetition = 3) == "aaabcaabcdedcba"
    assert candidate(s = "aaaaaaaaaaaabbbbbbbbbbccccccccccdddddddddd",k = 20,letter = "c",repetition = 4) == "aaaaaaaaaaaabbbbcccc"
    assert candidate(s = "aaaaaabbbbbbcccccc",k = 12,letter = "b",repetition = 4) == "aaaaaabbbbbb"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",k = 26,letter = "z",repetition = 1) == "aabcdefghijklmnopqrstuvwxz"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 13,letter = "m",repetition = 1) == "abcdefghijklm"
    assert candidate(s = "mississippi",k = 5,letter = "i",repetition = 2) == "iiipi"
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba",k = 26,letter = "a",repetition = 2) == "ayxwvutsrqponmlkjihgfedcba"
    assert candidate(s = "ababababababababababababababababababababababab",k = 10,letter = "a",repetition = 3) == "aaaaaaaaaa"
    assert candidate(s = "xyzyxyzyxyzyxyzyzyzyxyzyzyzyzyzyxyzyxyzyzyzyzyzy",k = 15,letter = "x",repetition = 3) == "xxxxxxxyyyyzyzy"
    assert candidate(s = "aabbccddeeff",k = 8,letter = "c",repetition = 3) == "aabbccd"
    assert candidate(s = "zzzzzaaaaabbbb",k = 10,letter = "a",repetition = 4) == "zaaaaabbbb"
    assert candidate(s = "mississippi",k = 4,letter = "i",repetition = 2) == "iiii"
    assert candidate(s = "mississippi",k = 6,letter = "i",repetition = 2) == "iiippi"
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50,letter = "z",repetition = 10) == "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 20,letter = "a",repetition = 2) == "aabbccddeeffgghhiijj"
    assert candidate(s = "banana",k = 4,letter = "a",repetition = 2) == "aana"
    assert candidate(s = "abcdabcdabcd",k = 8,letter = "b",repetition = 3) == "abababcd"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 10,letter = "m",repetition = 2) == "abcdefghm"
    assert candidate(s = "abracadabra",k = 7,letter = "a",repetition = 3) == "aaaabra"
    assert candidate(s = "zyxzyxzyx",k = 5,letter = "x",repetition = 2) == "xxzyx"
    assert candidate(s = "abracadabraabracadabra",k = 12,letter = "a",repetition = 4) == "aaaaaaaaabra"
    assert candidate(s = "racecar",k = 5,letter = "e",repetition = 1) == "acear"
    assert candidate(s = "abcdabcabcabc",k = 9,letter = "c",repetition = 3) == "aabcabcac"
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwerty",k = 12,letter = "r",repetition = 2) == "erabnmqwerty"
    assert candidate(s = "xyzyzyzyzyx",k = 7,letter = "y",repetition = 3) == "xyyyyyx"


