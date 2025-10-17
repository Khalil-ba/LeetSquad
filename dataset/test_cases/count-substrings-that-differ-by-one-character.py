def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abc",t = "abcd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",t = "abcd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "bcdef") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "bcdef") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",t = "bbbb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",t = "bbbb") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",t = "xya") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",t = "xya") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "python",t = "typhon") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",t = "typhon") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",t = "xyy") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",t = "xyy") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzz",t = "zzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzz",t = "zzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "same",t = "same") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "same",t = "same") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "abcf") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "abcf") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "fghij") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "fghij") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc",t = "abcabc") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc",t = "abcabc") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",t = "aaab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",t = "aaab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "misissippi") == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "misissippi") == 126: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",t = "xyw") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",t = "xyw") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "dcba") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "dcba") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",t = "def") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",t = "def") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "b") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "b") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "test",t = "tast") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "test",t = "tast") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aba",t = "baba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aba",t = "baba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa",t = "aaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa",t = "aaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "test",t = "text") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "test",t = "text") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "abce") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "abce") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",t = "hallo") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",t = "hallo") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "code",t = "cide") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "code",t = "cide") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab",t = "bb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab",t = "bb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "same",t = "sane") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "same",t = "sane") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abcdxyz") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abcdxyz") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaab",t = "aaaaaac") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaab",t = "aaaaaac") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiop",t = "qwertuiopq") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiop",t = "qwertuiopq") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",t = "banane") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",t = "banane") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "asdfghjkl",t = "asdfghjkl") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "asdfghjkl",t = "asdfghjkl") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "substring",t = "substrung") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "substring",t = "substrung") == 94: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",t = "bbbbbbaaaa") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",t = "bbbbbbaaaa") == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",t = "anana") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",t = "anana") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",t = "algorihm") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",t = "algorihm") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",t = "racecdr") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",t = "racecdr") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",t = "abacabb") == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",t = "abacabb") == 50: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",t = "aabbcz") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",t = "aabbcz") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "gfedcba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "gfedcba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",t = "aaabccddeeff") == 177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",t = "aaabccddeeff") == 177: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohello",t = "hellohelll") == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohello",t = "hellohelll") == 101: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd",t = "bbccddaa") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd",t = "bbccddaa") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",t = "racecars") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",t = "racecars") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",t = "zyxzyxzyx") == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",t = "zyxzyxzyx") == 96: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "programminh") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "programminh") == 125: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",t = "bandana") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",t = "bandana") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abcdefgh") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abcdefgh") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwert",t = "qwqrt") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwert",t = "qwqrt") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abcdeff") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abcdeff") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghjk") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghjk") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",t = "abcabcabd") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",t = "abcabcabd") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",t = "aaaabbbbbb") == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",t = "aaaabbbbbb") == 123: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghib") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghib") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",t = "abcfghi") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",t = "abcfghi") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohello",t = "hallohallo") == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohello",t = "hallohallo") == 134: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "abcdefgha") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "abcdefgha") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwert",t = "qwera") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwert",t = "qwera") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "progrcmming") == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "progrcmming") == 150: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",t = "banama") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",t = "banama") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosus") == 2250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosus") == 2250: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",t = "abceabcd") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",t = "abceabcd") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghix") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghix") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "example",t = "exampel") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "example",t = "exampel") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "abxdefgh") == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "abxdefgh") == 74: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",t = "defdefdef") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",t = "defdefdef") == 81: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "prognamming") == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "prognamming") == 149: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "jihgfedcba") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "jihgfedcba") == 106: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosi") == 2118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosi") == 2118: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",t = "fedcba") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",t = "fedcba") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",t = "dcbaabcd") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",t = "dcbaabcd") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "fedcbagh") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "fedcbagh") == 68: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "abcdexyz") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "abcdexyz") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "fghijkl") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "fghijkl") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abcdefh") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abcdefh") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghia") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghia") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",t = "abcxef") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",t = "abcxef") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcde",t = "abcdeabcda") == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcde",t = "abcdeabcda") == 94: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyx",t = "zyxzyx") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyx",t = "zyxzyx") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxcvbnm",t = "zxsvbnm") == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxcvbnm",t = "zxsvbnm") == 57: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",t = "abxdabcd") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",t = "abxdabcd") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "misssissippi") == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "misssissippi") == 155: {e}')
    
    total += 1
    try:
        result = candidate(s = "longerstring",t = "longerstirng") == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longerstring",t = "longerstirng") == 148: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrstuvw",t = "pqrsvwxy") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrstuvw",t = "pqrsvwxy") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",t = "zzzzzzzzza") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",t = "zzzzzzzzza") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abcdefi") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abcdefi") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "substring",t = "substrang") == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "substring",t = "substrang") == 93: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",t = "abaxaba") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",t = "abaxaba") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",t = "abcabcab") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",t = "abcabcab") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "abcefgih") == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "abcefgih") == 67: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",t = "abcdefgabcdeff") == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",t = "abcdefgabcdeff") == 189: {e}')
    
    total += 1
    try:
        result = candidate(s = "python",t = "pythpn") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "python",t = "pythpn") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",t = "abcddcba") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",t = "abcddcba") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abcdefj") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abcdefj") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "testtest",t = "tasttest") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "testtest",t = "tasttest") == 68: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",t = "algorithr") == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",t = "algorithr") == 81: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaab",t = "aaaabb") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaab",t = "aaaabb") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "programming") == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "programming") == 114: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",t = "bananas") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",t = "bananas") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "testcase",t = "tastcase") == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "testcase",t = "tastcase") == 73: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",t = "aabbbcc") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",t = "aabbbcc") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiop",t = "qwertuiop") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiop",t = "qwertuiop") == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "programmimg") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "programmimg") == 136: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",t = "aabbccddeegg") == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",t = "aabbccddeegg") == 160: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abcdefa") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abcdefa") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",t = "abcababc") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",t = "abcababc") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",t = "abcabcbca") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",t = "abcabcbca") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghja") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghja") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "testtest",t = "settsett") == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "testtest",t = "settsett") == 83: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "efghabcd") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "efghabcd") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",t = "abacaba") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",t = "abacaba") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdxyz",t = "xyzabcd") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdxyz",t = "xyzabcd") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzz",t = "zzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzz",t = "zzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrstuv",t = "qrsuvwp") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrstuv",t = "qrsuvwp") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",t = "ababcabc") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",t = "ababcabc") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",t = "abcdefghijx") == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",t = "abcdefghijx") == 121: {e}')
    
    total += 1
    try:
        result = candidate(s = "algorithm",t = "algorihtm") == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "algorithm",t = "algorihtm") == 83: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcd",t = "abacabad") == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcd",t = "abacabad") == 74: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",t = "zzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",t = "zzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzz",t = "xyyz") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzz",t = "xyyz") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",t = "bananna") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",t = "bananna") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "progrMming") == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "progrMming") == 118: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbb",t = "aaaabbbbb") == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbb",t = "aaaabbbbb") == 98: {e}')
    
    total += 1
    try:
        result = candidate(s = "pattern",t = "patterr") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pattern",t = "patterr") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacax",t = "abacay") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacax",t = "abacay") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "mississippa") == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "mississippa") == 141: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "progranning") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "progranning") == 125: {e}')
    
    total += 1
    try:
        result = candidate(s = "substrings",t = "substraings") == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "substrings",t = "substraings") == 108: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "abcdefga") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "abcdefga") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "mississipp") == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "mississipp") == 119: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",t = "zzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",t = "zzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcegijhif") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcegijhif") == 104: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",t = "bbbbbbbbbb") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",t = "bbbbbbbbbb") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "programminq") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "programminq") == 125: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyx",t = "zyxzyz") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyx",t = "zyxzyz") == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",t = "bbaacc") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",t = "bbaacc") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",t = "abababababab") == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",t = "abababababab") == 166: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",t = "mnopqs") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",t = "mnopqs") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",t = "abacabadabacaba") == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",t = "abacabadabacaba") == 272: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",t = "racecer") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",t = "racecer") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",t = "babcaba") == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",t = "babcaba") == 47: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "abcdefgi") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "abcdefgi") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababa",t = "bababab") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababa",t = "bababab") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "abdc") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "abdc") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwerty",t = "qwertyuiop") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwerty",t = "qwertyuiop") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "interview",t = "interviww") == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "interview",t = "interviww") == 89: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "mississipxy") == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "mississipxy") == 140: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiop",t = "poiuytrewq") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiop",t = "poiuytrewq") == 106: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abacdef") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abacdef") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "abcxefg") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "abcxefg") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",t = "aaaabbbbba") == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",t = "aaaabbbbba") == 128: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaab",t = "aaabaa") == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaab",t = "aaabaa") == 39: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaab",t = "aaaaaaax") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaab",t = "aaaaaaax") == 64: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "hgfedcba") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "hgfedcba") == 68: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab",t = "babababa") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab",t = "babababa") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",t = "abcdeg") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",t = "abcdeg") == 36: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abc",t = "abcd") == 9
    assert candidate(s = "abcde",t = "bcdef") == 21
    assert candidate(s = "aaaa",t = "bbbb") == 16
    assert candidate(s = "xyz",t = "xya") == 9
    assert candidate(s = "python",t = "typhon") == 40
    assert candidate(s = "xyz",t = "xyy") == 9
    assert candidate(s = "zzz",t = "zzz") == 0
    assert candidate(s = "same",t = "same") == 12
    assert candidate(s = "abcd",t = "abcf") == 16
    assert candidate(s = "abcde",t = "fghij") == 25
    assert candidate(s = "abcabc",t = "abcabc") == 24
    assert candidate(s = "aaaa",t = "aaab") == 10
    assert candidate(s = "mississippi",t = "misissippi") == 126
    assert candidate(s = "xyz",t = "xyw") == 9
    assert candidate(s = "a",t = "a") == 0
    assert candidate(s = "abcd",t = "dcba") == 16
    assert candidate(s = "abc",t = "def") == 9
    assert candidate(s = "a",t = "b") == 1
    assert candidate(s = "test",t = "tast") == 16
    assert candidate(s = "aba",t = "baba") == 6
    assert candidate(s = "aaa",t = "aaa") == 0
    assert candidate(s = "test",t = "text") == 16
    assert candidate(s = "abcd",t = "abce") == 16
    assert candidate(s = "hello",t = "hallo") == 30
    assert candidate(s = "code",t = "cide") == 18
    assert candidate(s = "ab",t = "bb") == 3
    assert candidate(s = "same",t = "sane") == 18
    assert candidate(s = "abcdefg",t = "abcdxyz") == 49
    assert candidate(s = "aaaaaab",t = "aaaaaac") == 49
    assert candidate(s = "qwertyuiop",t = "qwertuiopq") == 99
    assert candidate(s = "banana",t = "banane") == 38
    assert candidate(s = "asdfghjkl",t = "asdfghjkl") == 72
    assert candidate(s = "substring",t = "substrung") == 94
    assert candidate(s = "aaaaabbbbb",t = "bbbbbbaaaa") == 91
    assert candidate(s = "banana",t = "anana") == 21
    assert candidate(s = "algorithm",t = "algorihm") == 72
    assert candidate(s = "racecar",t = "racecdr") == 55
    assert candidate(s = "abacaba",t = "abacabb") == 50
    assert candidate(s = "aabbcc",t = "aabbcz") == 41
    assert candidate(s = "abcdefg",t = "gfedcba") == 52
    assert candidate(s = "aabbccddeeff",t = "aaabccddeeff") == 177
    assert candidate(s = "hellohello",t = "hellohelll") == 101
    assert candidate(s = "aabbccdd",t = "bbccddaa") == 64
    assert candidate(s = "racecar",t = "racecars") == 52
    assert candidate(s = "xyzxyzxyz",t = "zyxzyxzyx") == 96
    assert candidate(s = "programming",t = "programminh") == 125
    assert candidate(s = "banana",t = "bandana") == 44
    assert candidate(s = "abcdefg",t = "abcdefgh") == 49
    assert candidate(s = "qwert",t = "qwqrt") == 29
    assert candidate(s = "abcdefg",t = "abcdeff") == 49
    assert candidate(s = "abcdefghij",t = "abcdefghjk") == 100
    assert candidate(s = "abcabcabc",t = "abcabcabd") == 72
    assert candidate(s = "aaaaabbbbb",t = "aaaabbbbbb") == 123
    assert candidate(s = "abcdefghij",t = "abcdefghib") == 100
    assert candidate(s = "abcdefghi",t = "abcfghi") == 63
    assert candidate(s = "hellohello",t = "hallohallo") == 134
    assert candidate(s = "abcdefgh",t = "abcdefgha") == 63
    assert candidate(s = "qwert",t = "qwera") == 25
    assert candidate(s = "programming",t = "progrcmming") == 150
    assert candidate(s = "banana",t = "banama") == 42
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosus") == 2250
    assert candidate(s = "abcdabcd",t = "abceabcd") == 72
    assert candidate(s = "abcdefghij",t = "abcdefghix") == 100
    assert candidate(s = "example",t = "exampel") == 48
    assert candidate(s = "abcdefgh",t = "abxdefgh") == 74
    assert candidate(s = "abcabcabc",t = "defdefdef") == 81
    assert candidate(s = "programming",t = "prognamming") == 149
    assert candidate(s = "abcdefghij",t = "jihgfedcba") == 106
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosi") == 2118
    assert candidate(s = "abcdef",t = "fedcba") == 38
    assert candidate(s = "abcdabcd",t = "dcbaabcd") == 66
    assert candidate(s = "abcdefgh",t = "fedcbagh") == 68
    assert candidate(s = "abcdefgh",t = "abcdexyz") == 64
    assert candidate(s = "abcdefg",t = "fghijkl") == 47
    assert candidate(s = "abcdefg",t = "abcdefh") == 49
    assert candidate(s = "abcdefghij",t = "abcdefghia") == 99
    assert candidate(s = "abcdef",t = "abcxef") == 42
    assert candidate(s = "abcdeabcde",t = "abcdeabcda") == 94
    assert candidate(s = "xyzzyx",t = "zyxzyx") == 38
    assert candidate(s = "zxcvbnm",t = "zxsvbnm") == 57
    assert candidate(s = "abcdabcd",t = "abxdabcd") == 72
    assert candidate(s = "mississippi",t = "misssissippi") == 155
    assert candidate(s = "longerstring",t = "longerstirng") == 148
    assert candidate(s = "pqrstuvw",t = "pqrsvwxy") == 64
    assert candidate(s = "zzzzzzzzzz",t = "zzzzzzzzza") == 55
    assert candidate(s = "abcdefg",t = "abcdefi") == 49
    assert candidate(s = "substring",t = "substrang") == 93
    assert candidate(s = "abacaba",t = "abaxaba") == 56
    assert candidate(s = "abcabcabc",t = "abcabcab") == 48
    assert candidate(s = "abcdefgh",t = "abcefgih") == 67
    assert candidate(s = "abcdefgabcdefg",t = "abcdefgabcdeff") == 189
    assert candidate(s = "python",t = "pythpn") == 40
    assert candidate(s = "abcdabcd",t = "abcddcba") == 66
    assert candidate(s = "abcdefg",t = "abcdefj") == 49
    assert candidate(s = "testtest",t = "tasttest") == 68
    assert candidate(s = "algorithm",t = "algorithr") == 81
    assert candidate(s = "aaaaab",t = "aaaabb") == 35
    assert candidate(s = "programming",t = "programming") == 114
    assert candidate(s = "banana",t = "bananas") == 40
    assert candidate(s = "testcase",t = "tastcase") == 73
    assert candidate(s = "aabbcc",t = "aabbbcc") == 54
    assert candidate(s = "qwertyuiop",t = "qwertuiop") == 90
    assert candidate(s = "programming",t = "programmimg") == 136
    assert candidate(s = "aabbccddeeff",t = "aabbccddeegg") == 160
    assert candidate(s = "abcdefg",t = "abcdefa") == 48
    assert candidate(s = "abcabcabc",t = "abcababc") == 66
    assert candidate(s = "abcabcabc",t = "abcabcbca") == 71
    assert candidate(s = "abcdefghij",t = "abcdefghja") == 99
    assert candidate(s = "testtest",t = "settsett") == 83
    assert candidate(s = "abcdefgh",t = "efghabcd") == 56
    assert candidate(s = "abacaba",t = "abacaba") == 40
    assert candidate(s = "abcdxyz",t = "xyzabcd") == 42
    assert candidate(s = "zzzzzz",t = "zzzzzz") == 0
    assert candidate(s = "pqrstuv",t = "qrsuvwp") == 48
    assert candidate(s = "abcabcabc",t = "ababcabc") == 63
    assert candidate(s = "abcdefghijk",t = "abcdefghijx") == 121
    assert candidate(s = "algorithm",t = "algorihtm") == 83
    assert candidate(s = "abcdabcd",t = "abacabad") == 74
    assert candidate(s = "zzzzz",t = "zzzzz") == 0
    assert candidate(s = "xyzz",t = "xyyz") == 18
    assert candidate(s = "banana",t = "bananna") == 44
    assert candidate(s = "programming",t = "progrMming") == 118
    assert candidate(s = "aaaaabbbb",t = "aaaabbbbb") == 98
    assert candidate(s = "pattern",t = "patterr") == 51
    assert candidate(s = "abacax",t = "abacay") == 40
    assert candidate(s = "mississippi",t = "mississippa") == 141
    assert candidate(s = "programming",t = "progranning") == 125
    assert candidate(s = "substrings",t = "substraings") == 108
    assert candidate(s = "abcdefgh",t = "abcdefga") == 63
    assert candidate(s = "mississippi",t = "mississipp") == 119
    assert candidate(s = "zzzzzzzzzz",t = "zzzzzzzzzz") == 0
    assert candidate(s = "abcdefghij",t = "abcegijhif") == 104
    assert candidate(s = "aaaaaaaaaa",t = "bbbbbbbbbb") == 100
    assert candidate(s = "programming",t = "programminq") == 125
    assert candidate(s = "xyzzyx",t = "zyxzyz") == 39
    assert candidate(s = "aabbcc",t = "bbaacc") == 38
    assert candidate(s = "abcabcabcabc",t = "abababababab") == 166
    assert candidate(s = "mnopqr",t = "mnopqs") == 36
    assert candidate(s = "abacabadabacaba",t = "abacabadabacaba") == 272
    assert candidate(s = "racecar",t = "racecer") == 56
    assert candidate(s = "abacaba",t = "babcaba") == 47
    assert candidate(s = "abcdefgh",t = "abcdefgi") == 64
    assert candidate(s = "abababa",t = "bababab") == 25
    assert candidate(s = "abcd",t = "abdc") == 16
    assert candidate(s = "qwerty",t = "qwertyuiop") == 54
    assert candidate(s = "interview",t = "interviww") == 89
    assert candidate(s = "mississippi",t = "mississipxy") == 140
    assert candidate(s = "qwertyuiop",t = "poiuytrewq") == 106
    assert candidate(s = "abcdefg",t = "abacdef") == 49
    assert candidate(s = "abcdefg",t = "abcxefg") == 58
    assert candidate(s = "aaaaabbbbb",t = "aaaabbbbba") == 128
    assert candidate(s = "aaaaab",t = "aaabaa") == 39
    assert candidate(s = "aaaaaaab",t = "aaaaaaax") == 64
    assert candidate(s = "abcdefgh",t = "hgfedcba") == 68
    assert candidate(s = "abababab",t = "babababa") == 32
    assert candidate(s = "abcdef",t = "abcdeg") == 36


