def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbebebe",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbebebe",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "eceba",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eceba",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabb",k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabb",k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abaccc",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abaccc",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbb",k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbb",k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aa",k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aa",k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacaba",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacaba",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacadaeaefaefaeg",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacadaeaefaefaeg",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 4) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 4) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "asjsadowsadjsa",k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "asjsadowsadjsa",k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 13) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 13) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzz",k = 1) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzz",k = 1) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "pwwkew",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pwwkew",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefg",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefg",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcaaacccbbb",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcaaacccbbb",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabbbbbbbbbbbbbbccccccccccccccccccdddddddddddddddddddd",k = 4) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabbbbbbbbbbbbbbccccccccccccccccccdddddddddddddddddddd",k = 4) == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaaaccccc",k = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaaaccccc",k = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcabcabcabcabc",k = 4) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcabcabcabcabc",k = 4) == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabad",k = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabad",k = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "eceba",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eceba",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkll",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkll",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklllllllllmmmmmmmmmno",k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklllllllllmmmmmmmmmno",k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkk",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkk",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaa",k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaa",k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccc",k = 3) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccc",k = 3) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj",k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj",k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyz",k = 3) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyz",k = 3) == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "longestsubstringwithatmostkdistinctcharacters",k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longestsubstringwithatmostkdistinctcharacters",k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccdddd",k = 4) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccdddd",k = 4) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii",k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii",k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababab",k = 2) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababab",k = 2) == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "anviaj",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anviaj",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabbbbbbccccc",k = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabbbbbbccccc",k = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcdabcdabcd",k = 4) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcdabcdabcd",k = 4) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc",k = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc",k = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcd",k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcd",k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcddeeeeabc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcddeeeeabc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii",k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii",k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzxyzzzxyzz",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzxyzzzxyzz",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcadbcacdabc",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcadbcacdabc",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaabbbaaabbaaabbbaaabbaa",k = 2) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaabbbaaabbaaabbbaaabbaa",k = 2) == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbebebe",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbebebe",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbebebe",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbebebe",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii",k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii",k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab",k = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab",k = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazazazazazazaza",k = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazazazazazazaza",k = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzyzzzz",k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzyzzzz",k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "dvdf",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dvdf",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbbbc",k = 2) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbbbc",k = 2) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbcccccccc",k = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbcccccccc",k = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababcabcdeffefefefefefefefefefefe",k = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababcabcdeffefefefefefefefefefefe",k = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyz",k = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyz",k = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcabcabcabcabcabcabcabcabcabcabc",k = 4) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcabcabcabcabcabcabcabcabcabcabc",k = 4) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "ecebaacbebebe",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ecebaacbebebe",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaacaaccaaaabbbb",k = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaacaaccaaaabbbb",k = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "dvdf",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "dvdf",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",k = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",k = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccddd",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccddd",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",k = 3) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",k = 3) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcd",k = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcd",k = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcdabcd",k = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcdabcd",k = 4) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdefgh",k = 5) == 5
    assert candidate(s = "aabacbebebe",k = 3) == 7
    assert candidate(s = "",k = 0) == 0
    assert candidate(s = "eceba",k = 2) == 3
    assert candidate(s = "",k = 1) == 0
    assert candidate(s = "aabbcc",k = 2) == 4
    assert candidate(s = "aabb",k = 1) == 2
    assert candidate(s = "abaccc",k = 2) == 4
    assert candidate(s = "xyzxyzxyz",k = 2) == 2
    assert candidate(s = "aaaaaaa",k = 2) == 7
    assert candidate(s = "a",k = 0) == 0
    assert candidate(s = "abcdefg",k = 3) == 3
    assert candidate(s = "aaaabbbb",k = 1) == 4
    assert candidate(s = "abcabcabc",k = 3) == 9
    assert candidate(s = "aa",k = 1) == 2
    assert candidate(s = "a",k = 1) == 1
    assert candidate(s = "aabbcc",k = 1) == 2
    assert candidate(s = "abcd",k = 4) == 4
    assert candidate(s = "abcabcabc",k = 2) == 2
    assert candidate(s = "abcdef",k = 6) == 6
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 50) == 52
    assert candidate(s = "abcdefg",k = 0) == 0
    assert candidate(s = "abcdefgabcdefgabcdefg",k = 3) == 3
    assert candidate(s = "abacabadabacabadabacaba",k = 3) == 7
    assert candidate(s = "abacadaeaefaefaeg",k = 4) == 12
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",k = 4) == 40
    assert candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff",k = 3) == 6
    assert candidate(s = "abacabadabacabadabacabad",k = 3) == 7
    assert candidate(s = "asjsadowsadjsa",k = 4) == 6
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 13) == 26
    assert candidate(s = "zzzzzzzzzzzzzz",k = 1) == 14
    assert candidate(s = "pwwkew",k = 2) == 3
    assert candidate(s = "abcdefgabcdefgabcdefgabcdefgabcdefg",k = 5) == 5
    assert candidate(s = "abcaaacccbbb",k = 2) == 7
    assert candidate(s = "aaaaaaaabbbbbbbbbbbbbbccccccccccccccccccdddddddddddddddddddd",k = 4) == 60
    assert candidate(s = "abcdefg",k = 7) == 7
    assert candidate(s = "aaaaabbbbbaaaaaccccc",k = 2) == 15
    assert candidate(s = "abcdabcabcabcabcabcabc",k = 4) == 22
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabad",k = 5) == 40
    assert candidate(s = "eceba",k = 3) == 4
    assert candidate(s = "abcdefghij",k = 10) == 10
    assert candidate(s = "aabbccddeeffgghhiijjkkll",k = 10) == 20
    assert candidate(s = "abcdefghijklllllllllmmmmmmmmmno",k = 4) == 20
    assert candidate(s = "abcd",k = 0) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkk",k = 10) == 20
    assert candidate(s = "abcdefgabcdefgabcdefg",k = 5) == 5
    assert candidate(s = "aaaaaaa",k = 1) == 7
    assert candidate(s = "mississippi",k = 2) == 7
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 5) == 10
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbccccccccc",k = 3) == 29
    assert candidate(s = "aabbccddeeffgghhiijj",k = 5) == 10
    assert candidate(s = "abcabcabcabc",k = 4) == 12
    assert candidate(s = "zzzzz",k = 1) == 5
    assert candidate(s = "aabbccddeeff",k = 3) == 6
    assert candidate(s = "xyzzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyzxzyz",k = 3) == 62
    assert candidate(s = "longestsubstringwithatmostkdistinctcharacters",k = 5) == 9
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 52
    assert candidate(s = "aaaaabbbbbccccdddd",k = 4) == 18
    assert candidate(s = "abcdefgh",k = 7) == 7
    assert candidate(s = "aabbc",k = 2) == 4
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 50
    assert candidate(s = "abcdabcdabcd",k = 1) == 1
    assert candidate(s = "aabbccddeeffgghhii",k = 1) == 2
    assert candidate(s = "ababababababababababababababababababababab",k = 2) == 42
    assert candidate(s = "abcdef",k = 0) == 0
    assert candidate(s = "abacabadabacaba",k = 2) == 3
    assert candidate(s = "anviaj",k = 1) == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 48
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 5) == 5
    assert candidate(s = "abcdefghij",k = 5) == 5
    assert candidate(s = "aaaaaaabbbbbbccccc",k = 3) == 18
    assert candidate(s = "abcdabcabcdabcdabcd",k = 4) == 19
    assert candidate(s = "abcabcabcabcabcabcabcabc",k = 3) == 24
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 10) == 20
    assert candidate(s = "abacaba",k = 3) == 7
    assert candidate(s = "xyzxyzxyzxyz",k = 2) == 2
    assert candidate(s = "abcdabcdeabcd",k = 4) == 8
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",k = 1) == 20
    assert candidate(s = "abcddeeeeabc",k = 2) == 6
    assert candidate(s = "aabbccddeeffgghhii",k = 4) == 8
    assert candidate(s = "xyzzzzxyzzzxyzz",k = 2) == 5
    assert candidate(s = "abcadbcacdabc",k = 3) == 5
    assert candidate(s = "abcdefgh",k = 8) == 8
    assert candidate(s = "aaaabbbbccccdddd",k = 2) == 8
    assert candidate(s = "aabbccddeeffgg",k = 4) == 8
    assert candidate(s = "aabbaaabbbaaabbbaaabbaaabbbaaabbaa",k = 2) == 34
    assert candidate(s = "aabacbebebe",k = 0) == 0
    assert candidate(s = "aabbccddeeff",k = 5) == 10
    assert candidate(s = "abacabadabacaba",k = 1) == 1
    assert candidate(s = "aabbcc",k = 0) == 0
    assert candidate(s = "aabacbebebe",k = 2) == 6
    assert candidate(s = "aabbccddeeffgghhii",k = 5) == 10
    assert candidate(s = "abababababab",k = 2) == 12
    assert candidate(s = "zazazazazazazaza",k = 2) == 16
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",k = 10) == 10
    assert candidate(s = "abccba",k = 2) == 4
    assert candidate(s = "mississippi",k = 3) == 10
    assert candidate(s = "zzzzzzyzzzz",k = 2) == 11
    assert candidate(s = "abacabadabacaba",k = 3) == 7
    assert candidate(s = "dvdf",k = 1) == 1
    assert candidate(s = "aaaaaabbbbbc",k = 2) == 11
    assert candidate(s = "aaaaaaaaaabbbbbbcccccccc",k = 3) == 24
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",k = 1) == 30
    assert candidate(s = "aababcabcdeffefefefefefefefefefefe",k = 3) == 25
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 3) == 42
    assert candidate(s = "mnbvcxzlkjhgfdsapoiuytrewq",k = 15) == 15
    assert candidate(s = "xyzxyzxyzxyzxyzxyz",k = 3) == 18
    assert candidate(s = "abcdabcabcabcabcabcabcabcabcabcabcabcabc",k = 4) == 40
    assert candidate(s = "ecebaacbebebe",k = 2) == 6
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",k = 26) == 26
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 0) == 0
    assert candidate(s = "aabaaaacaaccaaaabbbb",k = 2) == 13
    assert candidate(s = "dvdf",k = 2) == 3
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",k = 10) == 30
    assert candidate(s = "aabbbcccddd",k = 3) == 9
    assert candidate(s = "xyzxyzxyzxyz",k = 3) == 12
    assert candidate(s = "abcdabcdabcdabcdabcdabcd",k = 4) == 24
    assert candidate(s = "abcdabcabcdabcd",k = 4) == 15


