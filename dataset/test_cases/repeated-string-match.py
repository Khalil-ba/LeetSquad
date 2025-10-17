def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = "abab",b = "abababab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abab",b = "abababab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "aba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "aba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "def") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "def") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "abcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "abcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaaaaaaaaaaaaaaaaaaaab",b = "ba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaaaaaaaaaaaaaaaaaaaab",b = "ba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "cdabcdab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "cdabcdab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "ac") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "ac") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "abcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "abcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "xyzxyzxyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "xyzxyzxyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "bca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "bca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "cab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "cab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "aa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "aa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "acbac") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "acbac") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaa",b = "aa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaa",b = "aa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dddd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dddd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "hello",b = "ohell") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "hello",b = "ohell") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "cabd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "cabd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dabcabcdabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dabcabcdabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "b") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "b") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "xyzyzyzx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "xyzyzyzx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "cabcabca") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "cabcabca") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dabcdabcdabcdabc") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dabcdabcdabcdabc") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "qrstuv",b = "uvqrstuvqrstuv") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "qrstuv",b = "uvqrstuvqrstuv") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "abcabcabcabcabcabcabcabcabcabc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "abcabcabcabcabcabcabcabcabcabc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dcba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dcba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "sequence",b = "encesequ") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "sequence",b = "encesequ") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "hello",b = "lohellohel") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "hello",b = "lohellohel") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabc",b = "cababcabcab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabc",b = "cababcabcab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "hello",b = "lohelohello") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "hello",b = "lohelohello") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "cdabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "cdabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "repeat",b = "peatreprea") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "repeat",b = "peatreprea") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "babababababab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "babababababab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "efgabcdefgabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "efgabcdefgabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "cdeabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "cdeabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabb",b = "bbaabbaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabb",b = "bbaabbaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 11: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "efgabcdefgabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "efgabcdefgabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "babababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "babababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "cdeabcdeabcde") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "cdeabcdeabcde") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "abcdabcdabcdabcdabcdab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "abcdabcdabcdabcdabcdab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabc",b = "bcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabc",b = "bcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "algorithm",b = "rithmalgorith") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "algorithm",b = "rithmalgorith") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "unique",b = "queuniqueuni") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "unique",b = "queuniqueuni") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "xyzxyzxyzxyzxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "xyzxyzxyzxyzxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dabcdabcdabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dabcdabcdabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzz",b = "zzzzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzz",b = "zzzzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "yzxyzxyzyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "yzxyzxyzyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaa",b = "aaaaaaaaaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaa",b = "aaaaaaaaaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "defgabcdefgab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "defgabcdefgab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaab",b = "babaaabaaaab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaab",b = "babaaabaaaab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "fgabcdefgabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "fgabcdefgabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "repeat",b = "atrepeatrepeatrep") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "repeat",b = "atrepeatrepeatrep") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "cdeabcdea") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "cdeabcdea") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "uvwxy",b = "xyuvwxyuvwx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "uvwxy",b = "xyuvwxyuvwx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaa",b = "aaaaaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaa",b = "aaaaaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "babababababababab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "babababababababab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(a = "repeat",b = "atrepeatrep") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "repeat",b = "atrepeatrep") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabbcc",b = "ccccaabbaabbcccc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabbcc",b = "ccccaabbaabbcccc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "test",b = "sttestte") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "test",b = "sttestte") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "bababababa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "bababababa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdef",b = "defabcdeabcf") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdef",b = "defabcdeabcf") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "zyxwv",b = "wvzyxwvzyxwv") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zyxwv",b = "wvzyxwvzyxwv") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abac",b = "acabacaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abac",b = "acabacaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdef",b = "defabcdefabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdef",b = "defabcdefabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "ababab",b = "babababababab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ababab",b = "babababababab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabb",b = "bbaabbbaab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabb",b = "bbaabbbaab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "zzz",b = "zzzzzzzzzzzzzzzzzzzz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "zzz",b = "zzzzzzzzzzzzzzzzzzzz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = "complex",b = "lexcomplexc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "complex",b = "lexcomplexc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "eabcdeabcdeabcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "eabcdeabcdeabcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "abcdabcdabcdabcdabcd") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "abcdabcdabcdabcdabcd") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "fgabcdefgabcde") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "fgabcdefgabcde") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "cdecdecdec") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "cdecdecdec") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "pattern",b = "ternpatternpat") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pattern",b = "ternpatternpat") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabc",b = "cabcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabc",b = "cabcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "babababa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "babababa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "zzzzxyzzz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "zzzzxyzzz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "ddddddddddddddddddd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "ddddddddddddddddddd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "aabb",b = "bbaabbbaabb") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aabb",b = "bbaabbbaabb") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abac",b = "cabacaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abac",b = "cabacaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "zyxzyxzyxzyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "zyxzyxzyxzyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "pattern",b = "ternpatte") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pattern",b = "ternpatte") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "test",b = "sttesttest") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "test",b = "sttesttest") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "cdabcdabcdabcdab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "cdabcdabcdabcdab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabc",b = "cabcabcabcabcab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabc",b = "cabcabcabcabcab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "xyzxyzxyzxyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "xyzxyzxyzxyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dddddddd") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dddddddd") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "cdabcda") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "cdabcda") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "bcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "bcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "ace",b = "aceaceaceace") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ace",b = "aceaceaceace") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzxyz",b = "zyxzyxzyxzyxzyxzyxzyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzxyz",b = "zyxzyxzyxzyxzyxzyxzyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "cababc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "cababc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefgh",b = "habcdefghabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefgh",b = "habcdefghabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 40: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabc",b = "cccc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabc",b = "cccc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dabcdabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dabcdabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnopqr",b = "qrmonpqrmon") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnopqr",b = "qrmonpqrmon") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzabc",b = "bcxyzabcxy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzabc",b = "bcxyzabcxy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "pattern",b = "ternpattern") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pattern",b = "ternpattern") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabc",b = "cabcabcab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabc",b = "cabcabcab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "unique",b = "niqueuniq") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "unique",b = "niqueuniq") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "substring",b = "stringsubstr") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "substring",b = "stringsubstr") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "mnop",b = "onmnoponmnop") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "mnop",b = "onmnoponmnop") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefg",b = "efgabcdefgabcdefgabcdefg") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefg",b = "efgabcdefgabcdefgabcdefg") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcd",b = "cdabcdabcdabcd") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcd",b = "cdabcdabcdabcd") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "bababababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "bababababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabc",b = "cabcabcabca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabc",b = "cabcabcabca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcd",b = "dcbaabcdabcda") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcd",b = "dcbaabcdabcda") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "ababababab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "ababababab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdabcdabcd",b = "dabcdabcdabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdabcdabcd",b = "dabcdabcdabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzyzyz",b = "zyzyzyzyzyzy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzyzyz",b = "zyzyzyzyzyzy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "eabcdeabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "eabcdeabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 32: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "abababababababab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "abababababababab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "deabcdeabcdeabcdeabcd") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "deabcdeabcdeabcdeabcd") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaaa",b = "aaaaaaaaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaaa",b = "aaaaaaaaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "pattern",b = "ernpatternpatt") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "pattern",b = "ernpatternpatt") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdef",b = "defabcdeabc") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdef",b = "defabcdeabc") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefabcdef",b = "defabcdefabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefabcdef",b = "defabcdefabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefgh",b = "fghabcdefgha") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefgh",b = "fghabcdefgha") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "a",b = "aaaaaaaaaaaaa") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "a",b = "aaaaaaaaaaaaa") == 13: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdef",b = "defabcde") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdef",b = "defabcde") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "xy",b = "yxyxyxyxyxyxyx") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xy",b = "yxyxyxyxyxyxyx") == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdeabcde",b = "cdecdecdecdec") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdeabcde",b = "cdecdecdecdec") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdefgabcdefg",b = "fgabcdefgabcdefgabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdefgabcdefg",b = "fgabcdefgabcdefgabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "ababab",b = "bababa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ababab",b = "bababa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabc",b = "bcabcabcabcabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabc",b = "bcabcabcabcabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "eabcdeabcdeabc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "eabcdeabcdeabc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcdef",b = "fedcbafedcba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcdef",b = "fedcbafedcba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "aaa",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "aaa",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 19: {e}')
    
    total += 1
    try:
        result = candidate(a = "abababa",b = "babababababab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abababa",b = "babababababab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "ab",b = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "ab",b = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "cba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "cba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcde",b = "deabcdeabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcde",b = "deabcdeabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abab",b = "babbababbababbababbababbababbaba") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abab",b = "babbababbababbababbababbababbaba") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyzxyz",b = "zyxzyxzyxzyxzyxzyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyzxyz",b = "zyxzyxzyxzyxzyxzyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "abcabcabc",b = "abcabcabcabcabcabcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abcabcabc",b = "abcabcabcabcabcabcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "xy",b = "yxyxyxyx") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xy",b = "yxyxyxyx") == 5: {e}')
    
    total += 1
    try:
        result = candidate(a = "repeat",b = "peatrepeatre") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "repeat",b = "peatrepeatre") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "hello",b = "hellohellohello") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "hello",b = "hellohellohello") == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "cabcabcabcabcab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "cabcabcabcabcab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = "abc",b = "cbaabcab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "abc",b = "cbaabcab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(a = "xyz",b = "zyxzyxzyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = "xyz",b = "zyxzyxzyx") == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = "abab",b = "abababab") == 2
    assert candidate(a = "ab",b = "aba") == 2
    assert candidate(a = "abc",b = "def") == -1
    assert candidate(a = "abc",b = "abcabc") == 2
    assert candidate(a = "aaaaaaaaaaaaaaaaaaaaaab",b = "ba") == 2
    assert candidate(a = "abcd",b = "cdabcdab") == 3
    assert candidate(a = "abc",b = "ac") == -1
    assert candidate(a = "abcd",b = "abcdabcd") == 2
    assert candidate(a = "xyz",b = "xyzxyzxyz") == 3
    assert candidate(a = "abc",b = "abcabcabc") == 3
    assert candidate(a = "abc",b = "bca") == 2
    assert candidate(a = "abc",b = "cab") == 2
    assert candidate(a = "a",b = "a") == 1
    assert candidate(a = "a",b = "aa") == 2
    assert candidate(a = "abc",b = "acbac") == -1
    assert candidate(a = "aaaa",b = "aa") == 1
    assert candidate(a = "abcd",b = "dddd") == -1
    assert candidate(a = "hello",b = "ohell") == 2
    assert candidate(a = "abcd",b = "cabd") == -1
    assert candidate(a = "abcd",b = "dabcabcdabc") == -1
    assert candidate(a = "a",b = "b") == -1
    assert candidate(a = "xyz",b = "xyzyzyzx") == -1
    assert candidate(a = "abc",b = "cabcabca") == 4
    assert candidate(a = "abcd",b = "dabcdabcdabcdabc") == 5
    assert candidate(a = "qrstuv",b = "uvqrstuvqrstuv") == 3
    assert candidate(a = "abc",b = "abcabcabcabcabcabcabcabcabcabc") == 10
    assert candidate(a = "abcd",b = "dcba") == -1
    assert candidate(a = "sequence",b = "encesequ") == 2
    assert candidate(a = "hello",b = "lohellohel") == 3
    assert candidate(a = "abcabcabc",b = "cababcabcab") == -1
    assert candidate(a = "hello",b = "lohelohello") == -1
    assert candidate(a = "abcd",b = "cdabc") == 2
    assert candidate(a = "repeat",b = "peatreprea") == -1
    assert candidate(a = "ab",b = "babababababab") == 7
    assert candidate(a = "abcdefg",b = "efgabcdefgabc") == 3
    assert candidate(a = "abcde",b = "cdeabcd") == 2
    assert candidate(a = "aabb",b = "bbaabbaa") == 3
    assert candidate(a = "zzzz",b = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == 11
    assert candidate(a = "abcdefg",b = "efgabcdefgabcd") == 3
    assert candidate(a = "ab",b = "babababab") == 5
    assert candidate(a = "abcde",b = "cdeabcdeabcde") == 3
    assert candidate(a = "abcd",b = "abcdabcdabcdabcdabcdab") == 6
    assert candidate(a = "abcabc",b = "bcabcabc") == 2
    assert candidate(a = "algorithm",b = "rithmalgorith") == 2
    assert candidate(a = "unique",b = "queuniqueuni") == 3
    assert candidate(a = "xyz",b = "xyzxyzxyzxyzxyz") == 5
    assert candidate(a = "abcd",b = "dabcdabcdabc") == 4
    assert candidate(a = "zzz",b = "zzzzzzzz") == 3
    assert candidate(a = "xyz",b = "yzxyzxyzyx") == -1
    assert candidate(a = "aaa",b = "aaaaaaaaaaaa") == 4
    assert candidate(a = "abcdefg",b = "defgabcdefgab") == 3
    assert candidate(a = "aaaab",b = "babaaabaaaab") == -1
    assert candidate(a = "abcdefg",b = "fgabcdefgabc") == 3
    assert candidate(a = "repeat",b = "atrepeatrepeatrep") == 4
    assert candidate(a = "abcde",b = "cdeabcdea") == 3
    assert candidate(a = "uvwxy",b = "xyuvwxyuvwx") == 3
    assert candidate(a = "aaaa",b = "aaaaaaaaa") == 3
    assert candidate(a = "ab",b = "babababababababab") == 9
    assert candidate(a = "repeat",b = "atrepeatrep") == 3
    assert candidate(a = "aabbcc",b = "ccccaabbaabbcccc") == -1
    assert candidate(a = "test",b = "sttestte") == 3
    assert candidate(a = "ab",b = "bababababa") == 6
    assert candidate(a = "abcdef",b = "defabcdeabcf") == -1
    assert candidate(a = "zyxwv",b = "wvzyxwvzyxwv") == 3
    assert candidate(a = "abac",b = "acabacaba") == 3
    assert candidate(a = "abcdef",b = "defabcdefabc") == 3
    assert candidate(a = "ababab",b = "babababababab") == 3
    assert candidate(a = "aabb",b = "bbaabbbaab") == -1
    assert candidate(a = "zzz",b = "zzzzzzzzzzzzzzzzzzzz") == 7
    assert candidate(a = "complex",b = "lexcomplexc") == 3
    assert candidate(a = "abcde",b = "eabcdeabcdeabcd") == 4
    assert candidate(a = "abcd",b = "abcdabcdabcdabcdabcd") == 5
    assert candidate(a = "abcdefg",b = "fgabcdefgabcde") == 3
    assert candidate(a = "abcde",b = "cdecdecdec") == -1
    assert candidate(a = "pattern",b = "ternpatternpat") == 3
    assert candidate(a = "abcabc",b = "cabcabcabc") == 2
    assert candidate(a = "ab",b = "babababa") == 5
    assert candidate(a = "xyz",b = "zzzzxyzzz") == -1
    assert candidate(a = "abcd",b = "ddddddddddddddddddd") == -1
    assert candidate(a = "aabb",b = "bbaabbbaabb") == -1
    assert candidate(a = "abac",b = "cabacaba") == 3
    assert candidate(a = "xyz",b = "zyxzyxzyxzyx") == -1
    assert candidate(a = "pattern",b = "ternpatte") == 2
    assert candidate(a = "test",b = "sttesttest") == 3
    assert candidate(a = "abcd",b = "cdabcdabcdabcdab") == 5
    assert candidate(a = "abcabc",b = "cabcabcabcabcab") == 3
    assert candidate(a = "xyz",b = "xyzxyzxyzxyz") == 4
    assert candidate(a = "abcd",b = "dddddddd") == -1
    assert candidate(a = "abcd",b = "cdabcda") == 3
    assert candidate(a = "abc",b = "bcabcabc") == 3
    assert candidate(a = "ace",b = "aceaceaceace") == 4
    assert candidate(a = "xyzxyz",b = "zyxzyxzyxzyxzyxzyxzyx") == -1
    assert candidate(a = "abc",b = "cababc") == -1
    assert candidate(a = "abcdefgh",b = "habcdefghabc") == 3
    assert candidate(a = "a",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 40
    assert candidate(a = "abcabcabc",b = "cccc") == -1
    assert candidate(a = "abcd",b = "dabcdabc") == 3
    assert candidate(a = "mnopqr",b = "qrmonpqrmon") == -1
    assert candidate(a = "xyzabc",b = "bcxyzabcxy") == 3
    assert candidate(a = "pattern",b = "ternpattern") == 2
    assert candidate(a = "abcabc",b = "cabcabcab") == 2
    assert candidate(a = "unique",b = "niqueuniq") == 2
    assert candidate(a = "substring",b = "stringsubstr") == 2
    assert candidate(a = "mnop",b = "onmnoponmnop") == -1
    assert candidate(a = "abcdefg",b = "efgabcdefgabcdefgabcdefg") == 4
    assert candidate(a = "abcdabcd",b = "cdabcdabcdabcd") == 2
    assert candidate(a = "ab",b = "bababababab") == 6
    assert candidate(a = "abcabc",b = "cabcabcabca") == 3
    assert candidate(a = "abcd",b = "dcbaabcdabcda") == -1
    assert candidate(a = "ab",b = "ababababab") == 5
    assert candidate(a = "abcdabcdabcd",b = "dabcdabcdabc") == 2
    assert candidate(a = "xyzyzyz",b = "zyzyzyzyzyzy") == -1
    assert candidate(a = "abcde",b = "eabcdeabcd") == 3
    assert candidate(a = "a",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 32
    assert candidate(a = "a",b = "abababababababab") == -1
    assert candidate(a = "abcde",b = "deabcdeabcdeabcdeabcd") == 5
    assert candidate(a = "aaaa",b = "aaaaaaaaaa") == 3
    assert candidate(a = "pattern",b = "ernpatternpatt") == 3
    assert candidate(a = "abcdef",b = "defabcdeabc") == -1
    assert candidate(a = "abcdefabcdef",b = "defabcdefabc") == 2
    assert candidate(a = "abcdefgh",b = "fghabcdefgha") == 3
    assert candidate(a = "a",b = "aaaaaaaaaaaaa") == 13
    assert candidate(a = "abcdef",b = "defabcde") == 2
    assert candidate(a = "xy",b = "yxyxyxyxyxyxyx") == 8
    assert candidate(a = "abcdeabcde",b = "cdecdecdecdec") == -1
    assert candidate(a = "abcdefgabcdefg",b = "fgabcdefgabcdefgabc") == 2
    assert candidate(a = "ababab",b = "bababa") == 2
    assert candidate(a = "abcabcabc",b = "bcabcabcabcabc") == 2
    assert candidate(a = "abcde",b = "eabcdeabcdeabc") == 4
    assert candidate(a = "abcdef",b = "fedcbafedcba") == -1
    assert candidate(a = "aaa",b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 19
    assert candidate(a = "abababa",b = "babababababab") == -1
    assert candidate(a = "ab",b = "") == 0
    assert candidate(a = "abc",b = "cba") == -1
    assert candidate(a = "abcde",b = "deabcdeabc") == 3
    assert candidate(a = "abab",b = "babbababbababbababbababbababbaba") == -1
    assert candidate(a = "xyzxyz",b = "zyxzyxzyxzyxzyxzyx") == -1
    assert candidate(a = "abcabcabc",b = "abcabcabcabcabcabcabcabc") == 3
    assert candidate(a = "xy",b = "yxyxyxyx") == 5
    assert candidate(a = "repeat",b = "peatrepeatre") == 3
    assert candidate(a = "hello",b = "hellohellohello") == 3
    assert candidate(a = "abc",b = "cabcabcabcabcab") == 6
    assert candidate(a = "abc",b = "cbaabcab") == -1
    assert candidate(a = "xyz",b = "zyxzyxzyx") == -1


