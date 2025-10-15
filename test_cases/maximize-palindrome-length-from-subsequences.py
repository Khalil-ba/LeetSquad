def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word1 = "race",word2 = "car") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "race",word2 = "car") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "a") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "a") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabb",word2 = "bbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabb",word2 = "bbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "race",word2 = "care") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "race",word2 = "care") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcde",word2 = "edcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcde",word2 = "edcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "madam",word2 = "madam") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "madam",word2 = "madam") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabb",word2 = "bbaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabb",word2 = "bbaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "zyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "zyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "palindrome",word2 = "emordnilap") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "palindrome",word2 = "emordnilap") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabc",word2 = "cbacba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabc",word2 = "cbacba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aa",word2 = "bb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aa",word2 = "bb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "hello",word2 = "world") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "hello",word2 = "world") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdxyz",word2 = "zyxcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdxyz",word2 = "zyxcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "cacb",word2 = "cbba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "cacb",word2 = "cbba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnop",word2 = "pqrs") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnop",word2 = "pqrs") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "noon",word2 = "noon") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "noon",word2 = "noon") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "level",word2 = "deified") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "level",word2 = "deified") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "a",word2 = "b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "a",word2 = "b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "noon",word2 = "moon") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "noon",word2 = "moon") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcba",word2 = "abcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcba",word2 = "abcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "dcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "dcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "def") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "def") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ab",word2 = "ab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ab",word2 = "ab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzzxyzzxyzz",word2 = "zzzyzxzzzyzxzzzyx") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzzxyzzxyzz",word2 = "zzzyzxzzzyzxzzzyx") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacax",word2 = "xcabab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacax",word2 = "xcabab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "deeee",word2 = "eee") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "deeee",word2 = "eee") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "jihgfedcbajihgfedcba") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "jihgfedcbajihgfedcba") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "madam",word2 = "rotor") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "madam",word2 = "rotor") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeff",word2 = "ffeeddccbbaa") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeff",word2 = "ffeeddccbbaa") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "level",word2 = "leve") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "level",word2 = "leve") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "palindrome",word2 = "emordnilapracecar") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "palindrome",word2 = "emordnilapracecar") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "longestpalindrome",word2 = "emordnilapstgnol") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "longestpalindrome",word2 = "emordnilapstgnol") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "level") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "level") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "step on no pets",word2 = "step on no pets") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "step on no pets",word2 = "step on no pets") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbaa",word2 = "ccddeee") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbaa",word2 = "ccddeee") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abc",word2 = "cba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abc",word2 = "cba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzzyx",word2 = "zyxzyz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzzyx",word2 = "zyxzyz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdxyz",word2 = "zyxcdb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdxyz",word2 = "zyxcdb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyx",word2 = "xyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyx",word2 = "xyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "racecar") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "racecar") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "b",word2 = "b") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "b",word2 = "b") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefgh",word2 = "hgfedcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefgh",word2 = "hgfedcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "level",word2 = "level") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "level",word2 = "level") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgg",word2 = "ggffeeddccbbaa") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgg",word2 = "ggffeeddccbbaa") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabaaa",word2 = "aaabaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabaaa",word2 = "aaabaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacaxaba",word2 = "xyzzyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacaxaba",word2 = "xyzzyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "gfedcba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "gfedcba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "uniqueletters",word2 = "stretteleunik") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "uniqueletters",word2 = "stretteleunik") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaa",word2 = "bbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaa",word2 = "bbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcxyz",word2 = "zyxcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcxyz",word2 = "zyxcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacdfgdcaba",word2 = "abacdfgdcaba") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacdfgdcaba",word2 = "abacdfgdcaba") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbaa",word2 = "aaabba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbaa",word2 = "aaabba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccdd",word2 = "ddccbbaa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccdd",word2 = "ddccbbaa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaaa",word2 = "bbbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaaa",word2 = "bbbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ababababab",word2 = "bababababa") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ababababab",word2 = "bababababa") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "step",word2 = "onests") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "step",word2 = "onests") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "zyxw") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "zyxw") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ababab",word2 = "bababa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ababab",word2 = "bababa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacaba",word2 = "bcbcbcb") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacaba",word2 = "bcbcbcb") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "palindromeconstruction",word2 = "noitcitsnocemordnilap") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "palindromeconstruction",word2 = "noitcitsnocemordnilap") == 40: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcd",word2 = "dcbaabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcd",word2 = "dcbaabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "car") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "car") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "deified",word2 = "deified") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "deified",word2 = "deified") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefg",word2 = "hgfedcba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefg",word2 = "hgfedcba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "complexstring",word2 = "gnirtsxlpmoc") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "complexstring",word2 = "gnirtsxlpmoc") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "noonnoon",word2 = "noonnoon") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "noonnoon",word2 = "noonnoon") == 16: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisatest",word2 = "tsetasitisth") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisatest",word2 = "tsetasitisth") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdxyz",word2 = "zyxwvut") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdxyz",word2 = "zyxwvut") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnopqr",word2 = "rstuvw") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnopqr",word2 = "rstuvw") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "carrace") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "carrace") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccdd",word2 = "aabbccdd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccdd",word2 = "aabbccdd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abababa",word2 = "bababab") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abababa",word2 = "bababab") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbb",word2 = "bbbbbbaaaa") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbb",word2 = "bbbbbbaaaa") == 19: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzz",word2 = "zzxy") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzz",word2 = "zzxy") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabc",word2 = "cbacbacbacba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabc",word2 = "cbacbacbacba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ab",word2 = "bbaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ab",word2 = "bbaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "qwertyuiop",word2 = "poiuytrewq") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "qwertyuiop",word2 = "poiuytrewq") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaabbbbb",word2 = "bbbbbbaaaaa") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaabbbbb",word2 = "bbbbbbaaaaa") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zzzz",word2 = "zzzz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zzzz",word2 = "zzzz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyx",word2 = "yxy") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyx",word2 = "yxy") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "repaper",word2 = "repaper") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "repaper",word2 = "repaper") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "reviled",word2 = "devil") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "reviled",word2 = "devil") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "fedcbaxyz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "fedcbaxyz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mississippi",word2 = "ississippim") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mississippi",word2 = "ississippim") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabc",word2 = "cbadcbad") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabc",word2 = "cbadcbad") == 14: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "rotor",word2 = "rotor") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "rotor",word2 = "rotor") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdabc",word2 = "cbadacb") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdabc",word2 = "cbadacb") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zyxwvutsrqponmlkjihgfedcba",word2 = "abcdefghijklmnopqrstuvwxyz") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zyxwvutsrqponmlkjihgfedcba",word2 = "abcdefghijklmnopqrstuvwxyz") == 52: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgg",word2 = "ggffeeddccbaa") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgg",word2 = "ggffeeddccbaa") == 26: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xxyyzz",word2 = "zzxyyx") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xxyyzz",word2 = "zzxyyx") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzyx",word2 = "xzyyx") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzyx",word2 = "xzyyx") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbcc",word2 = "ccbbaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbcc",word2 = "ccbbaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "sinoconiovacolcosilicropicoviscounmoneup") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "sinoconiovacolcosilicropicoviscounmoneup") == 49: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaabbbb",word2 = "bbbbcccc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaabbbb",word2 = "bbbbcccc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pqrstu",word2 = "utsrqp") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pqrstu",word2 = "utsrqp") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mamad",word2 = "adam") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mamad",word2 = "adam") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabc",word2 = "cbacbacba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabc",word2 = "cbacbacba") == 18: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacabadabacaba",word2 = "abacabadabacaba") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacabadabacaba",word2 = "abacabadabacaba") == 30: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "refer",word2 = "refer") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "refer",word2 = "refer") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "redder",word2 = "redder") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "redder",word2 = "redder") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abacdfgdcaba",word2 = "gfdcbba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abacdfgdcaba",word2 = "gfdcbba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdefghijk",word2 = "kjihgfedcba") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdefghijk",word2 = "kjihgfedcba") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "mnopqr",word2 = "rqponm") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "mnopqr",word2 = "rqponm") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbaa",word2 = "bbccbb") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbaa",word2 = "bbccbb") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "thisisaverylongwordtoseetifthelongestpalindrome",word2 = "emordnilapelongethtofeesavaloydnevasiht") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "thisisaverylongwordtoseetifthelongestpalindrome",word2 = "emordnilapelongethtofeesavaloydnevasiht") == 58: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyzzxy",word2 = "zyxzyxzyx") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyzzxy",word2 = "zyxzyxzyx") == 13: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "overlappingword",word2 = "drowgnalppero") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "overlappingword",word2 = "drowgnalppero") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "ab",word2 = "ba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "ab",word2 = "ba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "zxcvbnmasdfghjkl",word2 = "lkjhgfdsamnbvcxz") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "zxcvbnmasdfghjkl",word2 = "lkjhgfdsamnbvcxz") == 32: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aaaaa",word2 = "bbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aaaaa",word2 = "bbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "racecar",word2 = "civic") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "racecar",word2 = "civic") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zz yy xx ww vv uu tt ss rr qq pp oo nn mm ll kk jj ii hh gg ff ee dd cc bb aa") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zz yy xx ww vv uu tt ss rr qq pp oo nn mm ll kk jj ii hh gg ff ee dd cc bb aa") == 104: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcdef",word2 = "fedcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcdef",word2 = "fedcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "pqr",word2 = "rstuv") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "pqr",word2 = "rstuv") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "xyz",word2 = "zyxcba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "xyz",word2 = "zyxcba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "c",word2 = "c") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "c",word2 = "c") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word1 = "abcabcabcabcabc",word2 = "cbacbacbacbacba") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word1 = "abcabcabcabcabc",word2 = "cbacbacbacbacba") == 30: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word1 = "race",word2 = "car") == 7
    assert candidate(word1 = "a",word2 = "a") == 2
    assert candidate(word1 = "aabb",word2 = "bbcc") == 4
    assert candidate(word1 = "race",word2 = "care") == 7
    assert candidate(word1 = "abcde",word2 = "edcba") == 10
    assert candidate(word1 = "madam",word2 = "madam") == 10
    assert candidate(word1 = "aabb",word2 = "bbaa") == 8
    assert candidate(word1 = "xyz",word2 = "zyx") == 6
    assert candidate(word1 = "palindrome",word2 = "emordnilap") == 20
    assert candidate(word1 = "abcabc",word2 = "cbacba") == 12
    assert candidate(word1 = "aa",word2 = "bb") == 0
    assert candidate(word1 = "hello",word2 = "world") == 5
    assert candidate(word1 = "abcdxyz",word2 = "zyxcba") == 12
    assert candidate(word1 = "cacb",word2 = "cbba") == 5
    assert candidate(word1 = "mnop",word2 = "pqrs") == 2
    assert candidate(word1 = "noon",word2 = "noon") == 8
    assert candidate(word1 = "level",word2 = "deified") == 5
    assert candidate(word1 = "a",word2 = "b") == 0
    assert candidate(word1 = "noon",word2 = "moon") == 7
    assert candidate(word1 = "abcba",word2 = "abcba") == 10
    assert candidate(word1 = "abcd",word2 = "dcba") == 8
    assert candidate(word1 = "abc",word2 = "def") == 0
    assert candidate(word1 = "ab",word2 = "ab") == 3
    assert candidate(word1 = "xyzzxyzzxyzz",word2 = "zzzyzxzzzyzxzzzyx") == 25
    assert candidate(word1 = "abcdefghijklmnopqrstuvwxyz",word2 = "zyxwvutsrqponmlkjihgfedcba") == 52
    assert candidate(word1 = "abacax",word2 = "xcabab") == 10
    assert candidate(word1 = "deeee",word2 = "eee") == 7
    assert candidate(word1 = "abcdefghij",word2 = "jihgfedcbajihgfedcba") == 21
    assert candidate(word1 = "madam",word2 = "rotor") == 0
    assert candidate(word1 = "aabbccddeeff",word2 = "ffeeddccbbaa") == 24
    assert candidate(word1 = "level",word2 = "leve") == 8
    assert candidate(word1 = "palindrome",word2 = "emordnilapracecar") == 20
    assert candidate(word1 = "longestpalindrome",word2 = "emordnilapstgnol") == 30
    assert candidate(word1 = "racecar",word2 = "level") == 3
    assert candidate(word1 = "step on no pets",word2 = "step on no pets") == 30
    assert candidate(word1 = "aabbaa",word2 = "ccddeee") == 0
    assert candidate(word1 = "abc",word2 = "cba") == 6
    assert candidate(word1 = "xyzzyx",word2 = "zyxzyz") == 7
    assert candidate(word1 = "abcdxyz",word2 = "zyxcdb") == 10
    assert candidate(word1 = "xyx",word2 = "xyx") == 6
    assert candidate(word1 = "abcdefghij",word2 = "jihgfedcba") == 20
    assert candidate(word1 = "racecar",word2 = "racecar") == 14
    assert candidate(word1 = "b",word2 = "b") == 2
    assert candidate(word1 = "abcdefgh",word2 = "hgfedcba") == 16
    assert candidate(word1 = "level",word2 = "level") == 10
    assert candidate(word1 = "aabbccddeeffgg",word2 = "ggffeeddccbbaa") == 28
    assert candidate(word1 = "aabaaa",word2 = "aaabaa") == 12
    assert candidate(word1 = "abacaxaba",word2 = "xyzzyx") == 6
    assert candidate(word1 = "abcdefg",word2 = "gfedcba") == 14
    assert candidate(word1 = "uniqueletters",word2 = "stretteleunik") == 20
    assert candidate(word1 = "aaa",word2 = "bbb") == 0
    assert candidate(word1 = "abcxyz",word2 = "zyxcba") == 12
    assert candidate(word1 = "abacdfgdcaba",word2 = "abacdfgdcaba") == 22
    assert candidate(word1 = "abcdabcdabcd",word2 = "dcbaabcdabcd") == 14
    assert candidate(word1 = "aabbaa",word2 = "aaabba") == 11
    assert candidate(word1 = "aabbccdd",word2 = "ddccbbaa") == 16
    assert candidate(word1 = "aaaaaa",word2 = "bbbbbb") == 0
    assert candidate(word1 = "ababababab",word2 = "bababababa") == 20
    assert candidate(word1 = "step",word2 = "onests") == 7
    assert candidate(word1 = "abcd",word2 = "zyxw") == 0
    assert candidate(word1 = "ababab",word2 = "bababa") == 12
    assert candidate(word1 = "abacaba",word2 = "bcbcbcb") == 9
    assert candidate(word1 = "palindromeconstruction",word2 = "noitcitsnocemordnilap") == 40
    assert candidate(word1 = "abcd",word2 = "dcbaabcd") == 8
    assert candidate(word1 = "racecar",word2 = "car") == 7
    assert candidate(word1 = "deified",word2 = "deified") == 14
    assert candidate(word1 = "abcdefg",word2 = "hgfedcba") == 15
    assert candidate(word1 = "complexstring",word2 = "gnirtsxlpmoc") == 24
    assert candidate(word1 = "noonnoon",word2 = "noonnoon") == 16
    assert candidate(word1 = "thisisatest",word2 = "tsetasitisth") == 18
    assert candidate(word1 = "abcdxyz",word2 = "zyxwvut") == 6
    assert candidate(word1 = "mnopqr",word2 = "rstuvw") == 2
    assert candidate(word1 = "racecar",word2 = "carrace") == 9
    assert candidate(word1 = "aabbccdd",word2 = "aabbccdd") == 6
    assert candidate(word1 = "abababa",word2 = "bababab") == 13
    assert candidate(word1 = "aaaaabbbbb",word2 = "bbbbbbaaaa") == 19
    assert candidate(word1 = "xyzz",word2 = "zzxy") == 6
    assert candidate(word1 = "abcabcabcabc",word2 = "cbacbacbacba") == 24
    assert candidate(word1 = "ab",word2 = "bbaa") == 5
    assert candidate(word1 = "qwertyuiop",word2 = "poiuytrewq") == 20
    assert candidate(word1 = "aaaaabbbbb",word2 = "bbbbbbaaaaa") == 21
    assert candidate(word1 = "zzzz",word2 = "zzzz") == 8
    assert candidate(word1 = "xyx",word2 = "yxy") == 5
    assert candidate(word1 = "repaper",word2 = "repaper") == 14
    assert candidate(word1 = "reviled",word2 = "devil") == 6
    assert candidate(word1 = "abcdef",word2 = "fedcbaxyz") == 12
    assert candidate(word1 = "mississippi",word2 = "ississippim") == 18
    assert candidate(word1 = "abcdabc",word2 = "cbadcbad") == 14
    assert candidate(word1 = "rotor",word2 = "rotor") == 10
    assert candidate(word1 = "abcdabc",word2 = "cbadacb") == 12
    assert candidate(word1 = "zyxwvutsrqponmlkjihgfedcba",word2 = "abcdefghijklmnopqrstuvwxyz") == 52
    assert candidate(word1 = "aabbccddeeffgg",word2 = "ggffeeddccbaa") == 26
    assert candidate(word1 = "xxyyzz",word2 = "zzxyyx") == 10
    assert candidate(word1 = "xyzyx",word2 = "xzyyx") == 8
    assert candidate(word1 = "aabbcc",word2 = "ccbbaa") == 12
    assert candidate(word1 = "pneumonoultramicroscopicsilicovolcanoconiosis",word2 = "sinoconiovacolcosilicropicoviscounmoneup") == 49
    assert candidate(word1 = "aaaabbbb",word2 = "bbbbcccc") == 8
    assert candidate(word1 = "pqrstu",word2 = "utsrqp") == 12
    assert candidate(word1 = "mamad",word2 = "adam") == 7
    assert candidate(word1 = "abcabcabc",word2 = "cbacbacba") == 18
    assert candidate(word1 = "abacabadabacaba",word2 = "abacabadabacaba") == 30
    assert candidate(word1 = "refer",word2 = "refer") == 10
    assert candidate(word1 = "redder",word2 = "redder") == 12
    assert candidate(word1 = "abacdfgdcaba",word2 = "gfdcbba") == 15
    assert candidate(word1 = "abcdefghijk",word2 = "kjihgfedcba") == 22
    assert candidate(word1 = "mnopqr",word2 = "rqponm") == 12
    assert candidate(word1 = "aabbaa",word2 = "bbccbb") == 6
    assert candidate(word1 = "thisisaverylongwordtoseetifthelongestpalindrome",word2 = "emordnilapelongethtofeesavaloydnevasiht") == 58
    assert candidate(word1 = "xyzzxy",word2 = "zyxzyxzyx") == 13
    assert candidate(word1 = "overlappingword",word2 = "drowgnalppero") == 20
    assert candidate(word1 = "ab",word2 = "ba") == 4
    assert candidate(word1 = "zxcvbnmasdfghjkl",word2 = "lkjhgfdsamnbvcxz") == 32
    assert candidate(word1 = "aaaaa",word2 = "bbbbb") == 0
    assert candidate(word1 = "racecar",word2 = "civic") == 5
    assert candidate(word1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word2 = "zz yy xx ww vv uu tt ss rr qq pp oo nn mm ll kk jj ii hh gg ff ee dd cc bb aa") == 104
    assert candidate(word1 = "abcdef",word2 = "fedcba") == 12
    assert candidate(word1 = "pqr",word2 = "rstuv") == 2
    assert candidate(word1 = "xyz",word2 = "zyxcba") == 6
    assert candidate(word1 = "c",word2 = "c") == 2
    assert candidate(word1 = "abcabcabcabcabc",word2 = "cbacbacbacbacba") == 30


