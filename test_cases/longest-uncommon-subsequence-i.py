def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = "aaa",b = "bbb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaa",b = "bbb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "same",b = "same") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "same",b = "same") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "test",b = "testing") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "test",b = "testing") == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "b") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "b") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "fghij") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "fghij") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "a") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "a") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abab",b = "baba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abab",b = "baba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabc",b = "abc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabc",b = "abc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "ab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "ab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaa",b = "aaa") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaa",b = "aaa") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "aba",b = "cdc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aba",b = "cdc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaa",b = "aa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaa",b = "aa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "zyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "zyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "hello",b = "world") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "hello",b = "world") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "",b = "") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "",b = "") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "def") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "def") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "samecharacters",b = "samecharacters") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "samecharacters",b = "samecharacters") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhii",b = "abcabcabcabcabcabcabcabcabcabc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhii",b = "abcabcabcabcabcabcabcabcabcabc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(a = "sameple",b = "sample") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "sameple",b = "sample") == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaabbbb",b = "bbbbbaaaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaabbbb",b = "bbbbbaaaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "pqrstuvwxyz",b = "mnopqrstuvwxyz") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pqrstuvwxyz",b = "mnopqrstuvwxyz") == 14: {e}')
    
    total += 1
    try:
        result = candidate(a = "mississippi",b = "mississippiiss") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mississippi",b = "mississippiiss") == 14: {e}')
    
    total += 1
    try:
        result = candidate(a = "xylophone",b = "polymorph") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xylophone",b = "polymorph") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbcc",b = "bbccaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbcc",b = "bbccaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "pqr",b = "pqrstu") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pqr",b = "pqrstu") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcdabcd",b = "dcba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcdabcd",b = "dcba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefgh",b = "abcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefgh",b = "abcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "thisisatest",b = "thisisatesting") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "thisisatest",b = "thisisatesting") == 14: {e}')
    
    total += 1
    try:
        result = candidate(a = "uniquecharacters",b = "differentcharacters") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "uniquecharacters",b = "differentcharacters") == 19: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "defg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "defg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaabbbb",b = "bbbbbcccc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaabbbb",b = "bbbbbcccc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "abracadabra",b = "avadakedavra") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abracadabra",b = "avadakedavra") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "mississippi",b = "ississippi") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mississippi",b = "ississippi") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "patternmatching",b = "ternmpahcinoat") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "patternmatching",b = "ternmpahcinoat") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaaab",b = "bbbbbbbba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaaab",b = "bbbbbbbba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "uniquecharacters",b = "distinctcharacters") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "uniquecharacters",b = "distinctcharacters") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabc",b = "defdefdefdef") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabc",b = "defdefdefdef") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaa",b = "aaaaaaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaa",b = "aaaaaaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeff",b = "ffeeddccbaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeff",b = "ffeeddccbaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacaba",b = "abcabcabcabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacaba",b = "abcabcabcabc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhii",b = "jklmnopqrstuvwxyzz") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhii",b = "jklmnopqrstuvwxyzz") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijk",b = "mnopqrstuvw") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijk",b = "mnopqrstuvw") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacaba",b = "abacabadabacab") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacaba",b = "abacabadabacab") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabc",b = "bcabcabca") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabc",b = "bcabcabca") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgg",b = "ffggeeccddbbbaaa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgg",b = "ffggeeccddbbbaaa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaaaaa",b = "bbbbbbbbbb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaaaaa",b = "bbbbbbbbbb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabc",b = "abcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabc",b = "abcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhii",b = "aabbccddeeffgghhii") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhii",b = "aabbccddeeffgghhii") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabc",b = "abcabcabc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabc",b = "abcabcabc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "",b = "abcdef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "",b = "abcdef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "defdefdefdefdefdefdefdefdefdef") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "defdefdefdefdefdefdefdefdefdef") == 30: {e}')
    
    total += 1
    try:
        result = candidate(a = "abababab",b = "babababa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abababab",b = "babababa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzabc",b = "xyzdef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzabc",b = "xyzdef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabc",b = "defdefdef") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabc",b = "defdefdef") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "repeatedrepeated",b = "repeatedrepeatt") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "repeatedrepeated",b = "repeatedrepeatt") == 16: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabc",b = "abc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabc",b = "abc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyxyxyxyxy",b = "yxyxyxyxyx") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyxyxyxyxy",b = "yxyxyxyxyx") == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = "",b = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "",b = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "longestuncommonsubsequence",b = "short") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "longestuncommonsubsequence",b = "short") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcba") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcba") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "mississippi",b = "mississipp") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mississippi",b = "mississipp") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacax",b = "bacxab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacax",b = "bacxab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abracadabra",b = "cabracadabr") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abracadabra",b = "cabracadabr") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "pneumonoultramicroscopicsilicovolcanoconiosis",b = "antidisestablishmentarianism") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pneumonoultramicroscopicsilicovolcanoconiosis",b = "antidisestablishmentarianism") == 45: {e}')
    
    total += 1
    try:
        result = candidate(a = "thisisatest",b = "isatestthis") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "thisisatest",b = "isatestthis") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeff",b = "aabbccddeeffgghh") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeff",b = "aabbccddeeffgghh") == 16: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzxyz",b = "zyxzyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzxyz",b = "zyxzyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdexyz",b = "abcdexyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdexyz",b = "abcdexyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52: {e}')
    
    total += 1
    try:
        result = candidate(a = "differentstrings",b = "different") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "differentstrings",b = "different") == 16: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacaba",b = "bacabadabacabaa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacaba",b = "bacabadabacabaa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "repeatedrepeated",b = "repeated") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "repeatedrepeated",b = "repeated") == 16: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaabbbbcccc",b = "ccccbbbbaaaaaa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaabbbbcccc",b = "ccccbbbbaaaaaa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabc",b = "abcabc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabc",b = "abcabc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "differentstring",b = "differentstringxyz") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "differentstring",b = "differentstringxyz") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "abcdabcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "abcdabcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "abracadabra",b = "abracadabrac") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abracadabra",b = "abracadabrac") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaa",b = "baaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaa",b = "baaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "repeatedsubstringrepeatedsubstring",b = "substring") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "repeatedsubstringrepeatedsubstring",b = "substring") == 34: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaabbbcccdddeee",b = "eeeedddcccbbbbaaa") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaabbbcccdddeee",b = "eeeedddcccbbbbaaa") == 17: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefghijabcdefghij",b = "jihgfedcbajihgfedcba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefghijabcdefghij",b = "jihgfedcbajihgfedcba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "ghijklm") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "ghijklm") == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaabbbbcccc",b = "ccccbbbbaaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaabbbbcccc",b = "ccccbbbbaaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdeabcdeabcde",b = "deabcdeabcdeabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdeabcdeabcde",b = "deabcdeabcdeabc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaa",b = "aaaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaa",b = "aaaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcdabcd",b = "dcbaabdc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcdabcd",b = "dcbaabdc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaab",b = "aaaaaaac") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaab",b = "aaaaaaac") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "samestring",b = "samestring") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "samestring",b = "samestring") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "edcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "edcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaabaaa",b = "aaabaaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaabaaa",b = "aaabaaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdef",b = "ghijkl") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdef",b = "ghijkl") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abacabadabacaba",b = "babacabadabacab") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abacabadabacaba",b = "babacabadabacab") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "unique",b = "distinct") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "unique",b = "distinct") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "abababababababab",b = "babababababababa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abababababababab",b = "babababababababa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeff",b = "ffeeddccbbaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeff",b = "ffeeddccbbaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaabbbbbbbbbbcccccc",b = "ccccccdddddeeeeeeffffff") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaabbbbbbbbbbcccccc",b = "ccccccdddddeeeeeeffffff") == 23: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaaab",b = "aaaaaaaac") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaaab",b = "aaaaaaaac") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "longestuncommonsubsequence",b = "subsequencelongestuncom") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "longestuncommonsubsequence",b = "subsequencelongestuncom") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "banana",b = "bananab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "banana",b = "bananab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhiijj",b = "bbccddeeffgghhiijjkk") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhiijj",b = "bbccddeeffgghhiijjkk") == 20: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbcc",b = "ccbbaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbcc",b = "ccbbaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaabaaaaabaaaaab",b = "baaaaabaaaaabaaaaa") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaabaaaaabaaaaab",b = "baaaaabaaaaabaaaaa") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaabbbbb",b = "bbbbbaaaaaa") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaabbbbb",b = "bbbbbaaaaaa") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "longestuncommonsubsequence",b = "longestcommonsubsequence") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "longestuncommonsubsequence",b = "longestcommonsubsequence") == 26: {e}')
    
    total += 1
    try:
        result = candidate(a = "longerstringexample",b = "short") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "longerstringexample",b = "short") == 19: {e}')
    
    total += 1
    try:
        result = candidate(a = "thisisatest",b = "testthisis") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "thisisatest",b = "testthisis") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcdabcd",b = "dcbaabcdabcd") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcdabcd",b = "dcbaabcdabcd") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "uniqueuncommonstring",b = "stringuncommonunique") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "uniqueuncommonstring",b = "stringuncommonunique") == 20: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaabbbbb",b = "bbbbbccccc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaabbbbb",b = "bbbbbccccc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = "overlappingcharactersoverlap",b = "overlapoverlappingcharacters") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "overlappingcharactersoverlap",b = "overlapoverlappingcharacters") == 28: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabcabc",b = "abcabcabcabcabcabc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabcabc",b = "abcabcabcabcabcabc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhii",b = "aabbccddeeffgg") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhii",b = "aabbccddeeffgg") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbcc",b = "abbccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbcc",b = "abbccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaa",b = "aaaaaab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaa",b = "aaaaaab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcd",b = "dcba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcd",b = "dcba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "identicalstrings",b = "identicalstrings") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "identicalstrings",b = "identicalstrings") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcdabcd",b = "cdabcdabcdab") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcdabcd",b = "cdabcdabcdab") == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaa",b = "bbbbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaa",b = "bbbbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgg",b = "ggffeeeeddccbaaabb") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgg",b = "ggffeeeeddccbaaabb") == 18: {e}')
    
    total += 1
    try:
        result = candidate(a = "longerstring",b = "longerstringabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "longerstring",b = "longerstringabc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzabc",b = "abcxyz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzabc",b = "abcxyz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbccddeeffgghhii",b = "zzzzzzzzzzzzzzzzzzzzzzzz") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbccddeeffgghhii",b = "zzzzzzzzzzzzzzzzzzzzzzzz") == 24: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = "aaa",b = "bbb") == 3
    assert candidate(a = "same",b = "same") == -1
    assert candidate(a = "test",b = "testing") == 7
    assert candidate(a = "a",b = "b") == 1
    assert candidate(a = "abcde",b = "fghij") == 5
    assert candidate(a = "abc",b = "abcde") == 5
    assert candidate(a = "a",b = "a") == -1
    assert candidate(a = "abab",b = "baba") == 4
    assert candidate(a = "abcabc",b = "abc") == 6
    assert candidate(a = "abcd",b = "ab") == 4
    assert candidate(a = "aaa",b = "aaa") == -1
    assert candidate(a = "aba",b = "cdc") == 3
    assert candidate(a = "aaaa",b = "aa") == 4
    assert candidate(a = "abcd",b = "dcba") == 4
    assert candidate(a = "xyz",b = "zyx") == 3
    assert candidate(a = "hello",b = "world") == 5
    assert candidate(a = "",b = "") == -1
    assert candidate(a = "abc",b = "def") == 3
    assert candidate(a = "samecharacters",b = "samecharacters") == -1
    assert candidate(a = "aabbccddeeffgghhii",b = "abcabcabcabcabcabcabcabcabcabc") == 30
    assert candidate(a = "sameple",b = "sample") == 7
    assert candidate(a = "aaaaabbbb",b = "bbbbbaaaa") == 9
    assert candidate(a = "pqrstuvwxyz",b = "mnopqrstuvwxyz") == 14
    assert candidate(a = "mississippi",b = "mississippiiss") == 14
    assert candidate(a = "xylophone",b = "polymorph") == 9
    assert candidate(a = "aabbcc",b = "bbccaa") == 6
    assert candidate(a = "pqr",b = "pqrstu") == 6
    assert candidate(a = "abcdabcdabcd",b = "dcba") == 12
    assert candidate(a = "abcdefgh",b = "abcd") == 8
    assert candidate(a = "thisisatest",b = "thisisatesting") == 14
    assert candidate(a = "uniquecharacters",b = "differentcharacters") == 19
    assert candidate(a = "abc",b = "defg") == 4
    assert candidate(a = "aaaaabbbb",b = "bbbbbcccc") == 9
    assert candidate(a = "abracadabra",b = "avadakedavra") == 12
    assert candidate(a = "mississippi",b = "ississippi") == 11
    assert candidate(a = "patternmatching",b = "ternmpahcinoat") == 15
    assert candidate(a = "aaaaaaaab",b = "bbbbbbbba") == 9
    assert candidate(a = "uniquecharacters",b = "distinctcharacters") == 18
    assert candidate(a = "abcabcabcabc",b = "defdefdefdef") == 12
    assert candidate(a = "aaaaaaa",b = "aaaaaaaa") == 8
    assert candidate(a = "aabbccddeeff",b = "ffeeddccbaa") == 12
    assert candidate(a = "abacabadabacaba",b = "abcabcabcabc") == 15
    assert candidate(a = "aabbccddeeffgghhii",b = "jklmnopqrstuvwxyzz") == 18
    assert candidate(a = "abcdefghijk",b = "mnopqrstuvw") == 11
    assert candidate(a = "abacabadabacaba",b = "abacabadabacab") == 15
    assert candidate(a = "abcabcabc",b = "bcabcabca") == 9
    assert candidate(a = "aabbccddeeffgg",b = "ffggeeccddbbbaaa") == 16
    assert candidate(a = "aaaaaaaaaa",b = "bbbbbbbbbb") == 10
    assert candidate(a = "abcabcabc",b = "abcabc") == 9
    assert candidate(a = "aabbccddeeffgghhii",b = "aabbccddeeffgghhii") == -1
    assert candidate(a = "abcabcabcabc",b = "abcabcabc") == 12
    assert candidate(a = "",b = "abcdef") == 6
    assert candidate(a = "abcabcabcabcabcabcabcabcabcabc",b = "defdefdefdefdefdefdefdefdefdef") == 30
    assert candidate(a = "abababab",b = "babababa") == 8
    assert candidate(a = "xyzabc",b = "xyzdef") == 6
    assert candidate(a = "abcabcabc",b = "defdefdef") == 9
    assert candidate(a = "repeatedrepeated",b = "repeatedrepeatt") == 16
    assert candidate(a = "abcabcabc",b = "abc") == 9
    assert candidate(a = "xyxyxyxyxy",b = "yxyxyxyxyx") == 10
    assert candidate(a = "",b = "a") == 1
    assert candidate(a = "longestuncommonsubsequence",b = "short") == 26
    assert candidate(a = "abcdefghijklmnopqrstuvwxyz",b = "zyxwvutsrqponmlkjihgfedcba") == 26
    assert candidate(a = "mississippi",b = "mississipp") == 11
    assert candidate(a = "abacax",b = "bacxab") == 6
    assert candidate(a = "abracadabra",b = "cabracadabr") == 11
    assert candidate(a = "pneumonoultramicroscopicsilicovolcanoconiosis",b = "antidisestablishmentarianism") == 45
    assert candidate(a = "thisisatest",b = "isatestthis") == 11
    assert candidate(a = "aabbccddeeff",b = "aabbccddeeffgghh") == 16
    assert candidate(a = "xyzxyz",b = "zyxzyx") == 6
    assert candidate(a = "abcdexyz",b = "abcdexyz") == -1
    assert candidate(a = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",b = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa") == 52
    assert candidate(a = "differentstrings",b = "different") == 16
    assert candidate(a = "abacabadabacaba",b = "bacabadabacabaa") == 15
    assert candidate(a = "repeatedrepeated",b = "repeated") == 16
    assert candidate(a = "aaaaaaabbbbcccc",b = "ccccbbbbaaaaaa") == 15
    assert candidate(a = "abcabcabcabc",b = "abcabc") == 12
    assert candidate(a = "differentstring",b = "differentstringxyz") == 18
    assert candidate(a = "abcd",b = "abcdabcd") == 8
    assert candidate(a = "abracadabra",b = "abracadabrac") == 12
    assert candidate(a = "aaaaa",b = "baaaa") == 5
    assert candidate(a = "repeatedsubstringrepeatedsubstring",b = "substring") == 34
    assert candidate(a = "aaabbbcccdddeee",b = "eeeedddcccbbbbaaa") == 17
    assert candidate(a = "abcdefghijabcdefghij",b = "jihgfedcbajihgfedcba") == 20
    assert candidate(a = "abcdefg",b = "ghijklm") == 7
    assert candidate(a = "aaaabbbbcccc",b = "ccccbbbbaaaa") == 12
    assert candidate(a = "abcdeabcdeabcde",b = "deabcdeabcdeabc") == 15
    assert candidate(a = "aaaaaa",b = "aaaaa") == 6
    assert candidate(a = "abcdabcdabcd",b = "dcbaabdc") == 12
    assert candidate(a = "aaaaaaab",b = "aaaaaaac") == 8
    assert candidate(a = "samestring",b = "samestring") == -1
    assert candidate(a = "abcde",b = "edcba") == 5
    assert candidate(a = "aaaabaaa",b = "aaabaaaa") == 8
    assert candidate(a = "abcdef",b = "ghijkl") == 6
    assert candidate(a = "abacabadabacaba",b = "babacabadabacab") == 15
    assert candidate(a = "unique",b = "distinct") == 8
    assert candidate(a = "abababababababab",b = "babababababababa") == 16
    assert candidate(a = "aabbccddeeff",b = "ffeeddccbbaa") == 12
    assert candidate(a = "aaaaaabbbbbbbbbbcccccc",b = "ccccccdddddeeeeeeffffff") == 23
    assert candidate(a = "aaaaaaaab",b = "aaaaaaaac") == 9
    assert candidate(a = "longestuncommonsubsequence",b = "subsequencelongestuncom") == 26
    assert candidate(a = "a",b = "") == 1
    assert candidate(a = "banana",b = "bananab") == 7
    assert candidate(a = "aabbccddeeffgghhiijj",b = "bbccddeeffgghhiijjkk") == 20
    assert candidate(a = "aabbcc",b = "ccbbaa") == 6
    assert candidate(a = "aaaaabaaaaabaaaaab",b = "baaaaabaaaaabaaaaa") == 18
    assert candidate(a = "aaaaaabbbbb",b = "bbbbbaaaaaa") == 11
    assert candidate(a = "longestuncommonsubsequence",b = "longestcommonsubsequence") == 26
    assert candidate(a = "longerstringexample",b = "short") == 19
    assert candidate(a = "thisisatest",b = "testthisis") == 11
    assert candidate(a = "abcdabcdabcd",b = "dcbaabcdabcd") == 12
    assert candidate(a = "uniqueuncommonstring",b = "stringuncommonunique") == 20
    assert candidate(a = "aaaaabbbbb",b = "bbbbbccccc") == 10
    assert candidate(a = "overlappingcharactersoverlap",b = "overlapoverlappingcharacters") == 28
    assert candidate(a = "abcabcabcabc",b = "abcabcabcabcabcabc") == 18
    assert candidate(a = "aabbccddeeffgghhii",b = "aabbccddeeffgg") == 18
    assert candidate(a = "aabbcc",b = "abbccc") == 6
    assert candidate(a = "aaaaaaa",b = "aaaaaab") == 7
    assert candidate(a = "abcdabcd",b = "dcba") == 8
    assert candidate(a = "identicalstrings",b = "identicalstrings") == -1
    assert candidate(a = "abcdabcdabcd",b = "cdabcdabcdab") == 12
    assert candidate(a = "aaaaa",b = "bbbbb") == 5
    assert candidate(a = "aabbccddeeffgg",b = "ggffeeeeddccbaaabb") == 18
    assert candidate(a = "longerstring",b = "longerstringabc") == 15
    assert candidate(a = "xyzabc",b = "abcxyz") == 6
    assert candidate(a = "aabbccddeeffgghhii",b = "zzzzzzzzzzzzzzzzzzzzzzzz") == 24


