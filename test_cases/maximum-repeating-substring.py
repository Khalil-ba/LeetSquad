def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(sequence = "ababc",word = "ac") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababc",word = "ac") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "banana",word = "ana") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "banana",word = "ana") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabc",word = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabc",word = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaa",word = "aa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaa",word = "aa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abc",word = "d") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abc",word = "d") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababc",word = "ab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababc",word = "ab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "mississippi",word = "issi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "mississippi",word = "issi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaabaaa",word = "aa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaabaaa",word = "aa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababc",word = "ba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababc",word = "ba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "a",word = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "a",word = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabc",word = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabc",word = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "hellohellohello",word = "llohe") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "hellohellohello",word = "llohe") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababababab",word = "abab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababababab",word = "abab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababababababab",word = "ababab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababababababab",word = "ababab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aabbccddeeff",word = "aabbcc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aabbccddeeff",word = "aabbcc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababab",word = "ababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababab",word = "ababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyxxyxyxyxyxyxyxyxyxyx",word = "xyxxy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyxxyxyxyxyxyxyxyxyxyx",word = "xyxxy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabc",word = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabc",word = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababab",word = "ab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababab",word = "ab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "abcd") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "abcd") == 8: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abacabadabacaba",word = "dab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abacabadabacaba",word = "dab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabcabc",word = "abcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabcabc",word = "abcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababababababababab",word = "ababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababababababababab",word = "ababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "banana",word = "ban") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "banana",word = "ban") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabc",word = "cab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabc",word = "cab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abacabadabacaba",word = "cab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abacabadabacaba",word = "cab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "hellohellohellohello",word = "hello") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "hellohellohellohello",word = "hello") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "banana",word = "na") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "banana",word = "na") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababababab",word = "baba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababababab",word = "baba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababababababab",word = "ababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababababababab",word = "ababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabc",word = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabc",word = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzyzyzyzyzyzyzy",word = "zyzyzyzyzyzyzyzy") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzyzyzyzyzyzyzy",word = "zyzyzyzyzyzyzyzy") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzxxzzzxxzzzxx",word = "zzzxx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzxxzzzxxzzzxx",word = "zzzxx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aabbccddeeffgghhiijj",word = "ccdd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aabbccddeeffgghhiijj",word = "ccdd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzxyzxyzxyz",word = "zyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzxyzxyzxyz",word = "zyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabc",word = "cab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabc",word = "cab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababababababab",word = "bab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababababababab",word = "bab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "bananaananabana",word = "ana") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "bananaananabana",word = "ana") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaabaaa",word = "aaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaabaaa",word = "aaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abacabadabacaba",word = "bac") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abacabadabacaba",word = "bac") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaabbbbbcccc",word = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaabbbbbcccc",word = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaaa",word = "aaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaaa",word = "aaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzzzzzzzzzz",word = "zzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzzzzzzzzzz",word = "zzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababa",word = "aba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababa",word = "aba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababcabababc",word = "ababc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababcabababc",word = "ababc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababababababababababababab",word = "abab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababababababababababababab",word = "abab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaabaaaabaaaab",word = "aaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaabaaaabaaaab",word = "aaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababababababab",word = "baba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababababababab",word = "baba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzyzyzyzyzyzyzy",word = "zyzy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzyzyzyzyzyzyzy",word = "zyzy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabc",word = "abcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabc",word = "abcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaabaaaabaaaabaaaab",word = "aaaab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaabaaaabaaaabaaaab",word = "aaaab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabc",word = "cab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabc",word = "cab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababababababababab",word = "abab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababababababababab",word = "abab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abacabadabacaba",word = "abaca") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abacabadabacaba",word = "abaca") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaaa",word = "a") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaaa",word = "a") == 7: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aabbccddeeff",word = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aabbccddeeff",word = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabcabcabc",word = "abca") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabcabcabc",word = "abca") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabc",word = "abcabcab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabc",word = "abcabcab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdefabcdefabcdef",word = "defabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdefabcdefabcdef",word = "defabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word = "aabbccddeeffgghhiijjkkll") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word = "aabbccddeeffgghhiijjkkll") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdefabcdefabcdef",word = "abcdef") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdefabcdefabcdef",word = "abcdef") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzxyzxyzxyzxyz",word = "xyzxyzxyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzxyzxyzxyzxyz",word = "xyzxyzxyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababab",word = "ab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababab",word = "ab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abacabacabacabacabac",word = "abac") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abacabacabacabacabac",word = "abac") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaab",word = "aaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaab",word = "aaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaaa",word = "aaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaaa",word = "aaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababababababababab",word = "babab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababababababababab",word = "babab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababab",word = "aba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababab",word = "aba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaabaaa",word = "aaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaabaaa",word = "aaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaabaaaa",word = "aaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaabaaaa",word = "aaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababab",word = "aba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababab",word = "aba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "hellohellohellohellohello",word = "hellohello") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "hellohellohellohellohello",word = "hellohello") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabcabcabcabcabcabc",word = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabcabcabcabcabcabc",word = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aabbccddeeefffggghhh",word = "eefffggg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aabbccddeeefffggghhh",word = "eefffggg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "mississippi",word = "iss") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "mississippi",word = "iss") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abacabacabac",word = "abac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abacabacabac",word = "abac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxyxyxyxyxyxy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxyxyxyxyxyxy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabcabcabcabc",word = "abcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabcabcabcabc",word = "abcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aabbccddeeffgghhiijj",word = "aabbcc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aabbccddeeffgghhiijj",word = "aabbcc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyxyxyxyxyxyxyxyxyxy",word = "xyxy") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyxyxyxyxyxyxyxyxyxy",word = "xyxy") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyxyxyxyxyxyxy",word = "xyxy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyxyxyxyxyxyxy",word = "xyxy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "mississippi",word = "miss") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "mississippi",word = "miss") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababababababab",word = "ab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababababababab",word = "ab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "hellohellohellohello",word = "hellohello") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "hellohellohellohello",word = "hellohello") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "banana",word = "nan") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "banana",word = "nan") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababaaba",word = "aba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababaaba",word = "aba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "hellohellohello",word = "lohel") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "hellohellohello",word = "lohel") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "qqqqqqqqqqqq",word = "qqqq") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "qqqqqqqqqqqq",word = "qqqq") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyxxyxyxyxyxyx",word = "xyxyx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyxxyxyxyxyxyx",word = "xyxyx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdabcdabcdabcd",word = "abcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdabcdabcdabcd",word = "abcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "sequencewordsequenceword",word = "word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "sequencewordsequenceword",word = "word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababa",word = "aba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababa",word = "aba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxy") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxy") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdefgabcdefgabcdefg",word = "abcdefg") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdefgabcdefgabcdefg",word = "abcdefg") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababababababababababab",word = "abababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababababababababababab",word = "abababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaabaaaabaaaabaaaab",word = "aaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaabaaaabaaaabaaaab",word = "aaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababababababab",word = "abab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababababababab",word = "abab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdefghijabcdefghij",word = "cde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdefghijabcdefghij",word = "cde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "mamamamamamama",word = "mama") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "mamamamamamama",word = "mama") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababababab",word = "abab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababababab",word = "abab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "hellohellohello",word = "hello") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "hellohellohello",word = "hello") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabc",word = "abcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabc",word = "abcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzxyzxyz",word = "xyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzxyzxyz",word = "xyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabcabc",word = "bcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabcabc",word = "bcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abababababababab",word = "abab") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abababababababab",word = "abab") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "dabc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "dabc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "mississippiissippi",word = "issi") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "mississippiissippi",word = "issi") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzxyz",word = "xy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzxyz",word = "xy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabcabcabc",word = "abcabcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabcabcabc",word = "abcabcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",word = "zzzz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",word = "zzzz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabcabc",word = "abcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabcabc",word = "abcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "dcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "dcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "qwertyqwertyqwerty",word = "qwerty") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "qwertyqwertyqwerty",word = "qwerty") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "acacacacacac",word = "acac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "acacacacacac",word = "acac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababa",word = "bab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababa",word = "bab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababcabcababc",word = "abcab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababcabcababc",word = "abcab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaaaaaa",word = "aaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaaaaaa",word = "aaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaaaaaa",word = "aaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaaaaaa",word = "aaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "mississippi",word = "sip") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "mississippi",word = "sip") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaaa",word = "aa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaaa",word = "aa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaabaaaaa",word = "aaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaabaaaaa",word = "aaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzxyzxyz",word = "xyzxyz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzxyzxyz",word = "xyzxyz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababc",word = "aba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababc",word = "aba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabcabc",word = "cab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabcabc",word = "cab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abacabacabacabac",word = "abacabac") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abacabacabacabac",word = "abacabac") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabc",word = "abcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabc",word = "abcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcabcabcabcabc",word = "abcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcabcabcabcabc",word = "abcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzyzyzxzyzyzxzyzyz",word = "zyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzyzyzxzyzyzxzyzyz",word = "zyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzxyzxyz",word = "zyxzyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzxyzxyz",word = "zyxzyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzxyzxyz",word = "xyzxyzxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzxyzxyz",word = "xyzxyzxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aaaaaa",word = "aa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aaaaaa",word = "aa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "abcdabcdabcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "abcdabcdabcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdabcdabcdabcd",word = "cdab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdabcdabcdabcd",word = "cdab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzzzzzz",word = "zzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzzzzzz",word = "zzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdefgabcdefgabcdefg",word = "efg") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdefgabcdefgabcdefg",word = "efg") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdefgabcdefg",word = "abcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdefgabcdefg",word = "abcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "bananaananabananananabanananananana",word = "anana") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "bananaananabananananabanananananana",word = "anana") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "qwertyqwertyqwerty",word = "erty") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "qwertyqwertyqwerty",word = "erty") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "pqrspqrspqrspqrspqr",word = "pqrs") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "pqrspqrspqrspqrspqr",word = "pqrs") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababababa",word = "bab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababababa",word = "bab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcbabcabcbabcabc",word = "abcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcbabcabcbabcabc",word = "abcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "qwertyqwertyqwerty",word = "qwertyqwerty") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "qwertyqwertyqwerty",word = "qwertyqwerty") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzzzzzzzzzz",word = "zzz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzzzzzzzzzz",word = "zzz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "zzzzzzzzzzzzzzz",word = "zzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "zzzzzzzzzzzzzzz",word = "zzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyzxyzxyz",word = "xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyzxyzxyz",word = "xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aabbccddeeff",word = "eeff") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aabbccddeeff",word = "eeff") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word = "mmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word = "mmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "ababababab",word = "abab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "ababababab",word = "abab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxyxyxyxyxyxyxy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxyxyxyxyxyxyxy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "abcdabcdabcdabcdabcdabcd",word = "abcdabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "abcdabcdabcdabcdabcdabcd",word = "abcdabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sequence = "qwertyqwertyqwertyqwerty",word = "qwertyqwerty") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sequence = "qwertyqwertyqwertyqwerty",word = "qwertyqwerty") == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(sequence = "ababc",word = "ac") == 0
    assert candidate(sequence = "banana",word = "ana") == 1
    assert candidate(sequence = "abcabcabc",word = "abc") == 3
    assert candidate(sequence = "aaaa",word = "aa") == 2
    assert candidate(sequence = "abc",word = "d") == 0
    assert candidate(sequence = "ababc",word = "ab") == 2
    assert candidate(sequence = "mississippi",word = "issi") == 1
    assert candidate(sequence = "aaaabaaa",word = "aa") == 2
    assert candidate(sequence = "ababc",word = "ba") == 1
    assert candidate(sequence = "a",word = "a") == 1
    assert candidate(sequence = "abcabcabc",word = "abcd") == 0
    assert candidate(sequence = "hellohellohello",word = "llohe") == 2
    assert candidate(sequence = "abababababab",word = "abab") == 3
    assert candidate(sequence = "abababababababab",word = "ababab") == 2
    assert candidate(sequence = "aabbccddeeff",word = "aabbcc") == 1
    assert candidate(sequence = "ababababab",word = "ababab") == 1
    assert candidate(sequence = "xyxxyxyxyxyxyxyxyxyxyx",word = "xyxxy") == 1
    assert candidate(sequence = "abcabcabcabc",word = "abcd") == 0
    assert candidate(sequence = "ababababab",word = "ab") == 5
    assert candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "abcd") == 8
    assert candidate(sequence = "abacabadabacaba",word = "dab") == 1
    assert candidate(sequence = "abcabcabcabcabcabc",word = "abcabcabc") == 2
    assert candidate(sequence = "abababababababababab",word = "ababab") == 3
    assert candidate(sequence = "banana",word = "ban") == 1
    assert candidate(sequence = "abcabcabcabcabc",word = "cab") == 4
    assert candidate(sequence = "abacabadabacaba",word = "cab") == 1
    assert candidate(sequence = "hellohellohellohello",word = "hello") == 4
    assert candidate(sequence = "banana",word = "na") == 2
    assert candidate(sequence = "abababababab",word = "baba") == 2
    assert candidate(sequence = "ababababababababab",word = "ababab") == 3
    assert candidate(sequence = "abcabcabcabcabc",word = "abcd") == 0
    assert candidate(sequence = "xyzyzyzyzyzyzyzy",word = "zyzyzyzyzyzyzyzy") == 0
    assert candidate(sequence = "zzzxxzzzxxzzzxx",word = "zzzxx") == 3
    assert candidate(sequence = "aabbccddeeffgghhiijj",word = "ccdd") == 1
    assert candidate(sequence = "xyzxyzxyzxyzxyz",word = "zyx") == 0
    assert candidate(sequence = "abcabcabcabc",word = "cab") == 3
    assert candidate(sequence = "ababababababababab",word = "bab") == 1
    assert candidate(sequence = "bananaananabana",word = "ana") == 2
    assert candidate(sequence = "aaaaabaaa",word = "aaaa") == 1
    assert candidate(sequence = "abacabadabacaba",word = "bac") == 1
    assert candidate(sequence = "aaaaabbbbbcccc",word = "abc") == 0
    assert candidate(sequence = "aaaaaaa",word = "aaa") == 2
    assert candidate(sequence = "zzzzzzzzzzzz",word = "zzzz") == 3
    assert candidate(sequence = "ababababa",word = "aba") == 1
    assert candidate(sequence = "abababcabababc",word = "ababc") == 1
    assert candidate(sequence = "ababababababababababababababab",word = "abab") == 7
    assert candidate(sequence = "aaaabaaaabaaaab",word = "aaab") == 1
    assert candidate(sequence = "abababababababab",word = "baba") == 3
    assert candidate(sequence = "xyzyzyzyzyzyzyzy",word = "zyzy") == 3
    assert candidate(sequence = "abcabcabcabc",word = "abcabc") == 2
    assert candidate(sequence = "aaaabaaaabaaaabaaaab",word = "aaaab") == 4
    assert candidate(sequence = "abcabcabc",word = "cab") == 2
    assert candidate(sequence = "abababababababababab",word = "abab") == 5
    assert candidate(sequence = "abacabadabacaba",word = "abaca") == 1
    assert candidate(sequence = "aaaaaaa",word = "a") == 7
    assert candidate(sequence = "aabbccddeeff",word = "abc") == 0
    assert candidate(sequence = "abcabcabcabcabcabcabc",word = "abca") == 1
    assert candidate(sequence = "abcabcabcabcabc",word = "abcabcab") == 1
    assert candidate(sequence = "abcdefabcdefabcdef",word = "defabc") == 2
    assert candidate(sequence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word = "aabbccddeeffgghhiijjkkll") == 1
    assert candidate(sequence = "abcdefabcdefabcdef",word = "abcdef") == 3
    assert candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzzzz") == 3
    assert candidate(sequence = "xyzxyzxyzxyzxyzxyz",word = "xyzxyzxyz") == 2
    assert candidate(sequence = "abababab",word = "ab") == 4
    assert candidate(sequence = "abacabacabacabacabac",word = "abac") == 5
    assert candidate(sequence = "aaaaab",word = "aaa") == 1
    assert candidate(sequence = "aaaaaaa",word = "aaaa") == 1
    assert candidate(sequence = "ababababababababababab",word = "babab") == 1
    assert candidate(sequence = "abababab",word = "aba") == 1
    assert candidate(sequence = "aaaaaabaaa",word = "aaa") == 2
    assert candidate(sequence = "aaaaabaaaa",word = "aaa") == 1
    assert candidate(sequence = "ababababab",word = "aba") == 1
    assert candidate(sequence = "hellohellohellohellohello",word = "hellohello") == 2
    assert candidate(sequence = "abcabcabcabcabcabcabcabcabcabc",word = "abcabcabc") == 3
    assert candidate(sequence = "aabbccddeeefffggghhh",word = "eefffggg") == 1
    assert candidate(sequence = "mississippi",word = "iss") == 2
    assert candidate(sequence = "abacabacabac",word = "abac") == 3
    assert candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxyxyxyxyxyxy") == 1
    assert candidate(sequence = "abcabcabcabcabcabcabcabc",word = "abcabcabc") == 2
    assert candidate(sequence = "aabbccddeeffgghhiijj",word = "aabbcc") == 1
    assert candidate(sequence = "xyxyxyxyxyxyxyxyxyxy",word = "xyxy") == 5
    assert candidate(sequence = "xyxyxyxyxyxyxy",word = "xyxy") == 3
    assert candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzz") == 5
    assert candidate(sequence = "mississippi",word = "miss") == 1
    assert candidate(sequence = "ababababababababab",word = "ab") == 9
    assert candidate(sequence = "hellohellohellohello",word = "hellohello") == 2
    assert candidate(sequence = "banana",word = "nan") == 1
    assert candidate(sequence = "abababaaba",word = "aba") == 2
    assert candidate(sequence = "hellohellohello",word = "lohel") == 2
    assert candidate(sequence = "qqqqqqqqqqqq",word = "qqqq") == 3
    assert candidate(sequence = "xyxxyxyxyxyxyx",word = "xyxyx") == 1
    assert candidate(sequence = "abcdabcdabcdabcd",word = "abcdabcd") == 2
    assert candidate(sequence = "sequencewordsequenceword",word = "word") == 1
    assert candidate(sequence = "abababa",word = "aba") == 1
    assert candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxy") == 4
    assert candidate(sequence = "abcdefgabcdefgabcdefg",word = "abcdefg") == 3
    assert candidate(sequence = "abababababababababababab",word = "abababab") == 3
    assert candidate(sequence = "aaaabaaaabaaaabaaaab",word = "aaab") == 1
    assert candidate(sequence = "ababababababababab",word = "abab") == 4
    assert candidate(sequence = "abcdefghijabcdefghij",word = "cde") == 1
    assert candidate(sequence = "mamamamamamama",word = "mama") == 3
    assert candidate(sequence = "ababababababab",word = "abab") == 3
    assert candidate(sequence = "hellohellohello",word = "hello") == 3
    assert candidate(sequence = "abcabcabcabcabc",word = "abcabcabcabc") == 1
    assert candidate(sequence = "xyzxyzxyzxyz",word = "xyz") == 4
    assert candidate(sequence = "abcabcabcabcabcabc",word = "bcabc") == 1
    assert candidate(sequence = "abababababababab",word = "abab") == 4
    assert candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "dabc") == 7
    assert candidate(sequence = "mississippiissippi",word = "issi") == 1
    assert candidate(sequence = "xyzxyzxyz",word = "xy") == 1
    assert candidate(sequence = "abcabcabcabcabcabcabc",word = "abcabcabcabcabc") == 1
    assert candidate(sequence = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",word = "zzzz") == 7
    assert candidate(sequence = "abcabcabcabcabcabc",word = "abcabc") == 3
    assert candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "dcba") == 0
    assert candidate(sequence = "qwertyqwertyqwerty",word = "qwerty") == 3
    assert candidate(sequence = "acacacacacac",word = "acac") == 3
    assert candidate(sequence = "ababababa",word = "bab") == 1
    assert candidate(sequence = "ababcabcababc",word = "abcab") == 1
    assert candidate(sequence = "aaaaaaaaaa",word = "aaa") == 3
    assert candidate(sequence = "aaaaaaaaaa",word = "aaaa") == 2
    assert candidate(sequence = "mississippi",word = "sip") == 1
    assert candidate(sequence = "aaaaaaa",word = "aa") == 3
    assert candidate(sequence = "aaaaaabaaaaa",word = "aaaaa") == 1
    assert candidate(sequence = "xyzxyzxyzxyz",word = "xyzxyz") == 2
    assert candidate(sequence = "ababababc",word = "aba") == 1
    assert candidate(sequence = "abcabcabcabcabcabc",word = "cab") == 5
    assert candidate(sequence = "abacabacabacabac",word = "abacabac") == 2
    assert candidate(sequence = "abcabcabcabcabc",word = "abcabcabc") == 1
    assert candidate(sequence = "abcabcabcabcabc",word = "abcabc") == 2
    assert candidate(sequence = "xyzxyzyzyzxzyzyzxzyzyz",word = "zyz") == 1
    assert candidate(sequence = "xyzxyzxyzxyz",word = "zyxzyx") == 0
    assert candidate(sequence = "xyzxyzxyzxyz",word = "xyzxyzxyz") == 1
    assert candidate(sequence = "aaaaaa",word = "aa") == 3
    assert candidate(sequence = "abcdabcdabcdabcdabcdabcdabcdabcd",word = "abcdabcdabcdabcd") == 2
    assert candidate(sequence = "abcdabcdabcdabcd",word = "cdab") == 3
    assert candidate(sequence = "zzzzzzzz",word = "zzzz") == 2
    assert candidate(sequence = "abcdefgabcdefgabcdefg",word = "efg") == 1
    assert candidate(sequence = "zzzzzzzzzzzzzzzzzzzz",word = "zzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(sequence = "abcdefgabcdefg",word = "abcdefg") == 2
    assert candidate(sequence = "bananaananabananananabanananananana",word = "anana") == 2
    assert candidate(sequence = "qwertyqwertyqwerty",word = "erty") == 1
    assert candidate(sequence = "pqrspqrspqrspqrspqr",word = "pqrs") == 4
    assert candidate(sequence = "ababababababa",word = "bab") == 1
    assert candidate(sequence = "abcbabcabcbabcabc",word = "abcabc") == 1
    assert candidate(sequence = "qwertyqwertyqwerty",word = "qwertyqwerty") == 1
    assert candidate(sequence = "zzzzzzzzzzzz",word = "zzz") == 4
    assert candidate(sequence = "zzzzzzzzzzzzzzz",word = "zzzz") == 3
    assert candidate(sequence = "xyzxyzxyz",word = "xyz") == 3
    assert candidate(sequence = "aabbccddeeff",word = "eeff") == 1
    assert candidate(sequence = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",word = "mmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(sequence = "ababababab",word = "abab") == 2
    assert candidate(sequence = "xyxyxyxyxyxyxyxy",word = "xyxyxyxyxyxyxyxy") == 1
    assert candidate(sequence = "abcdabcdabcdabcdabcdabcd",word = "abcdabcd") == 3
    assert candidate(sequence = "qwertyqwertyqwertyqwerty",word = "qwertyqwerty") == 2


