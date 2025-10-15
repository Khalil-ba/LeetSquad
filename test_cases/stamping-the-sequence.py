def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(stamp = "world",target = "worldworldworld") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "world",target = "worldworldworld") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abcababcbcababc") == [11, 9, 8, 6, 4, 2, 1, 10, 7, 3, 12, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abcababcbcababc") == [11, 9, 8, 6, 4, 2, 1, 10, 7, 3, 12, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcde",target = "abcdeabcde") == [4, 3, 2, 1, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcde",target = "abcdeabcde") == [4, 3, 2, 1, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abc????") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abc????") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "a",target = "aaaaaaaa") == [7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "a",target = "aaaaaaaa") == [7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcde",target = "abcdeabcdeabcde") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcde",target = "abcdeabcdeabcde") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "????abc???") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "????abc???") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abcabc????????") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abcabc????????") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "?????") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "?????") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "ab?bc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "ab?bc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "hello",target = "hellohellohello") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "hello",target = "hellohellohello") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abc????abc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abc????abc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "ab",target = "abababab") == [5, 3, 1, 6, 4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "ab",target = "abababab") == [5, 3, 1, 6, 4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcdef",target = "abcdefabcdef") == [5, 4, 3, 2, 1, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcdef",target = "abcdefabcdef") == [5, 4, 3, 2, 1, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "a",target = "aaaaaaaaa") == [8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "a",target = "aaaaaaaaa") == [8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abcabcabc") == [5, 4, 2, 1, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abcabcabc") == [5, 4, 2, 1, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abc????????abc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abc????????abc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abcabc") == [2, 1, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abcabc") == [2, 1, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "a",target = "aaaaaaaaaa") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "a",target = "aaaaaaaaaa") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "test",target = "testtesttest") == [7, 6, 5, 3, 2, 1, 8, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "test",target = "testtesttest") == [7, 6, 5, 3, 2, 1, 8, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "abcdabcd") == [3, 2, 1, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "abcdabcd") == [3, 2, 1, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abca",target = "aabcaca") == [2, 3, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abca",target = "aabcaca") == [2, 3, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "????abc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "????abc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "??abc??") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "??abc??") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "ababc") == [1, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "ababc") == [1, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyz",target = "xyzxyzxyz") == [5, 4, 2, 1, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyz",target = "xyzxyzxyz") == [5, 4, 2, 1, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "????????abcabc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "????????abcabc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abcabcabcabcabc") == [11, 10, 8, 7, 5, 4, 2, 1, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abcabcabcabcabc") == [11, 10, 8, 7, 5, 4, 2, 1, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcde",target = "abcde") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcde",target = "abcde") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "ababcbababcbababc") == [11, 9, 5, 3, 13, 10, 7, 4, 1, 12, 6, 0, 14, 8, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "ababcbababcbababc") == [11, 9, 5, 3, 13, 10, 7, 4, 1, 12, 6, 0, 14, 8, 2]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "mnopqr",target = "mnopqrmnopqrmnopqrmnopqrmnopqr") == [23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 24, 18, 12, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "mnopqr",target = "mnopqrmnopqrmnopqrmnopqrmnopqr") == [23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 24, 18, 12, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "efgh",target = "efghefghefghefghefghefghefgh") == [23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 24, 20, 16, 12, 8, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "efgh",target = "efghefghefghefghefghefghefgh") == [23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 24, 20, 16, 12, 8, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbcc") == [11, 10, 9, 8, 4, 3, 2, 1, 13, 12, 6, 5, 14, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbcc") == [11, 10, 9, 8, 4, 3, 2, 1, 13, 12, 6, 5, 14, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "ddddddddddddddddddddddddddddabcd") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "ddddddddddddddddddddddddddddabcd") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyz",target = "xyxyxyxyxyxyxyxyxyxy") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyz",target = "xyxyxyxyxyxyxyxyxyxy") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "zzz",target = "zzzzzzzzzzzzzzzzzzzz") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "zzz",target = "zzzzzzzzzzzzzzzzzzzz") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcdef",target = "abcdefabcdefabcdefabcdefabcdefabcdef") == [29, 28, 27, 26, 25, 23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 30, 24, 18, 12, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcdef",target = "abcdefabcdefabcdefabcdefabcdefabcdef") == [29, 28, 27, 26, 25, 23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 30, 24, 18, 12, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyz",target = "xyxyxyxyxyxyxyxyxyxyxyx") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyz",target = "xyxyxyxyxyxyxyxyxyxyxyx") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabcd") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabcd") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbccaaabbcc") == [18, 17, 16, 15, 11, 10, 9, 8, 4, 3, 2, 1, 20, 19, 13, 12, 6, 5, 21, 14, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbccaaabbcc") == [18, 17, 16, 15, 11, 10, 9, 8, 4, 3, 2, 1, 20, 19, 13, 12, 6, 5, 21, 14, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyz",target = "xyzxyzxyzxyzxyz") == [11, 10, 8, 7, 5, 4, 2, 1, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyz",target = "xyzxyzxyzxyzxyz") == [11, 10, 8, 7, 5, 4, 2, 1, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "abcdabcdeabcdabcd") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "abcdabcdeabcdabcd") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "aaaa",target = "aaaaaaaaaaaaaaaa") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "aaaa",target = "aaaaaaaaaaaaaaaa") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcdef") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcdef") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "xyzabcxyzabcxyz") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "xyzabcxyzabcxyz") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "abcdabcdabcdabcd") == [11, 10, 9, 7, 6, 5, 3, 2, 1, 12, 8, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "abcdabcdabcdabcd") == [11, 10, 9, 7, 6, 5, 3, 2, 1, 12, 8, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyz",target = "xyzxyzxyzxyz") == [8, 7, 5, 4, 2, 1, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyz",target = "xyzxyzxyzxyz") == [8, 7, 5, 4, 2, 1, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "qrstuv",target = "qrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuv") == [35, 34, 33, 32, 31, 29, 28, 27, 26, 25, 23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 36, 30, 24, 18, 12, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "qrstuv",target = "qrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuv") == [35, 34, 33, 32, 31, 29, 28, 27, 26, 25, 23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 36, 30, 24, 18, 12, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "aaa",target = "aaaaaaaaaaaaaaaaaaaa") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "aaa",target = "aaaaaaaaaaaaaaaaaaaa") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "a",target = "aaaaaaaaaaaaaaaaaaaa") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "a",target = "aaaaaaaaaaaaaaaaaaaa") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyzabc",target = "xyzabcxyzabcxyzabcxyzabc") == [17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 18, 12, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyzabc",target = "xyzabcxyzabcxyzabcxyzabc") == [17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 18, 12, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabc") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabc") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcde",target = "edcbaedcbaedcba") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcde",target = "edcbaedcbaedcba") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabcabc") == [17, 16, 14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 18, 15, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabcabc") == [17, 16, 14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 18, 15, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyz",target = "xyzxyzxyzxyzxyzxyz") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyz",target = "xyzxyzxyzxyzxyzxyz") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "qrst",target = "qrstqrstqrstqrstqrstqrstqrstqrst") == [27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 28, 24, 20, 16, 12, 8, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "qrst",target = "qrstqrstqrstqrstqrstqrstqrstqrst") == [27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 28, 24, 20, 16, 12, 8, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "mnop",target = "mnopmnopmnopmnopmnopmnopmnopmnop") == [27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 28, 24, 20, 16, 12, 8, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "mnop",target = "mnopmnopmnopmnopmnopmnopmnopmnop") == [27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 28, 24, 20, 16, 12, 8, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "abcabcabcabcabcabc") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "abcabcabcabcabcabc") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abac",target = "abacabacabacabacabac") == [15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 16, 12, 8, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abac",target = "abacabacabacabacabac") == [15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 16, 12, 8, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "aaaaaaaaaaabcabcaaaaaaaaaa") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "aaaaaaaaaaabcabcaaaaaaaaaa") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "ab",target = "abababababababababab") == [17, 15, 13, 11, 9, 7, 5, 3, 1, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "ab",target = "abababababababababab") == [17, 15, 13, 11, 9, 7, 5, 3, 1, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "stamp",target = "stampstampstamp") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "stamp",target = "stampstampstamp") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcdefg",target = "abcdefgabcdefgabcdefgabcdefg") == [20, 19, 18, 17, 16, 15, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 21, 14, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcdefg",target = "abcdefgabcdefgabcdefgabcdefg") == [20, 19, 18, 17, 16, 15, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 21, 14, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcdeabc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcdeabc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abab",target = "abababababababab") == [11, 9, 7, 5, 3, 1, 12, 10, 8, 6, 4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abab",target = "abababababababab") == [11, 9, 7, 5, 3, 1, 12, 10, 8, 6, 4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "ab",target = "abaabaabaab") == [7, 4, 1, 8, 5, 2, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "ab",target = "abaabaabaab") == [7, 4, 1, 8, 5, 2, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "hello",target = "hellohellohellohello") == [14, 13, 12, 11, 9, 8, 7, 6, 4, 3, 2, 1, 15, 10, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "hello",target = "hellohellohellohello") == [14, 13, 12, 11, 9, 8, 7, 6, 4, 3, 2, 1, 15, 10, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "mnopqr",target = "mnopqrnopqrmonpqrnonqrmpnoqrmnoprqmnopqr") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "mnopqr",target = "mnopqrnopqrmonpqrnonqrmpnoqrmnoprqmnopqr") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abc",target = "ababababababababc") == [1, 3, 0, 5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 12, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abc",target = "ababababababababc") == [1, 3, 0, 5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 12, 14]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyzxyz",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == [29, 28, 26, 25, 23, 22, 20, 19, 17, 16, 14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyzxyz",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == [29, 28, 26, 25, 23, 22, 20, 19, 17, 16, 14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "hello",target = "hellohellohellohelloh") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "hello",target = "hellohellohellohelloh") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "abcabcabcabc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "abcabcabcabc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "abcdeabcd") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "abcdeabcd") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "mnopqr",target = "mnopqrmnopqrmnopqr") == [11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 12, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "mnopqr",target = "mnopqrmnopqrmnopqr") == [11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 12, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbccabc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbccabc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcdef",target = "fedcbafedcbafedcba") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcdef",target = "fedcbafedcbafedcba") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcdef",target = "abcdefabcdefabcdefabcdef") == [17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 18, 12, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcdef",target = "abcdefabcdefabcdefabcdef") == [17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 18, 12, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "stamp",target = "stampstampstampstam") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "stamp",target = "stampstampstampstam") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcdefg",target = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == [34, 33, 32, 31, 30, 29, 27, 26, 25, 24, 23, 22, 20, 19, 18, 17, 16, 15, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 35, 28, 21, 14, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcdefg",target = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == [34, 33, 32, 31, 30, 29, 27, 26, 25, 24, 23, 22, 20, 19, 18, 17, 16, 15, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 35, 28, 21, 14, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "abcdabcdabcdabcdabcd") == [15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 16, 12, 8, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "abcdabcdabcdabcdabcd") == [15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 16, 12, 8, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "abcdabcabcd") == [6, 5, 3, 2, 1, 4, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "abcdabcabcd") == [6, 5, 3, 2, 1, 4, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "xyzyx",target = "xyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyx") == [67, 66, 65, 63, 62, 61, 59, 58, 57, 55, 54, 53, 51, 50, 49, 47, 46, 45, 43, 42, 41, 39, 38, 37, 35, 34, 33, 31, 30, 29, 27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "xyzyx",target = "xyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyx") == [67, 66, 65, 63, 62, 61, 59, 58, 57, 55, 54, 53, 51, 50, 49, 47, 46, 45, 43, 42, 41, 39, 38, 37, 35, 34, 33, 31, 30, 29, 27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "ab",target = "ababababababababababh") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "ab",target = "ababababababababababh") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcde") == [14, 13, 12, 11, 9, 8, 7, 6, 4, 3, 2, 1, 15, 10, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcde") == [14, 13, 12, 11, 9, 8, 7, 6, 4, 3, 2, 1, 15, 10, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcd",target = "dabcdabc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcd",target = "dabcdabc") == []: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "aabbcc",target = "aabbccaabbccaaabbccaaabbccaaabbccaaabbcc") == [31, 30, 29, 28, 24, 23, 22, 21, 17, 16, 15, 14, 10, 9, 8, 7, 33, 32, 26, 25, 19, 18, 12, 11, 5, 4, 3, 2, 1, 34, 27, 20, 13, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "aabbcc",target = "aabbccaabbccaaabbccaaabbccaaabbccaaabbcc") == [31, 30, 29, 28, 24, 23, 22, 21, 17, 16, 15, 14, 10, 9, 8, 7, 33, 32, 26, 25, 19, 18, 12, 11, 5, 4, 3, 2, 1, 34, 27, 20, 13, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "aabbcc",target = "aabbccaabbccaabbcc") == [11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 12, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "aabbcc",target = "aabbccaabbccaabbcc") == [11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 12, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(stamp = "abcdef",target = "fedcbafedcbafedcbafedcbafedcbafedcbafedcba") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stamp = "abcdef",target = "fedcbafedcbafedcbafedcbafedcbafedcbafedcba") == []: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(stamp = "world",target = "worldworldworld") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]
    assert candidate(stamp = "abc",target = "abcababcbcababc") == [11, 9, 8, 6, 4, 2, 1, 10, 7, 3, 12, 5, 0]
    assert candidate(stamp = "abcde",target = "abcdeabcde") == [4, 3, 2, 1, 5, 0]
    assert candidate(stamp = "abc",target = "abc????") == []
    assert candidate(stamp = "a",target = "aaaaaaaa") == [7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(stamp = "abcde",target = "abcdeabcdeabcde") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]
    assert candidate(stamp = "abc",target = "????abc???") == []
    assert candidate(stamp = "abc",target = "abcabc????????") == []
    assert candidate(stamp = "abc",target = "?????") == []
    assert candidate(stamp = "abc",target = "ab?bc") == []
    assert candidate(stamp = "hello",target = "hellohellohello") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]
    assert candidate(stamp = "abc",target = "abc????abc") == []
    assert candidate(stamp = "ab",target = "abababab") == [5, 3, 1, 6, 4, 2, 0]
    assert candidate(stamp = "abcdef",target = "abcdefabcdef") == [5, 4, 3, 2, 1, 6, 0]
    assert candidate(stamp = "a",target = "aaaaaaaaa") == [8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(stamp = "abc",target = "abcabcabc") == [5, 4, 2, 1, 6, 3, 0]
    assert candidate(stamp = "abc",target = "abc????????abc") == []
    assert candidate(stamp = "abc",target = "abcabc") == [2, 1, 3, 0]
    assert candidate(stamp = "a",target = "aaaaaaaaaa") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(stamp = "test",target = "testtesttest") == [7, 6, 5, 3, 2, 1, 8, 4, 0]
    assert candidate(stamp = "abcd",target = "abcdabcd") == [3, 2, 1, 4, 0]
    assert candidate(stamp = "abca",target = "aabcaca") == [2, 3, 0, 1]
    assert candidate(stamp = "abc",target = "????abc") == []
    assert candidate(stamp = "abc",target = "??abc??") == []
    assert candidate(stamp = "abc",target = "ababc") == [1, 0, 2]
    assert candidate(stamp = "xyz",target = "xyzxyzxyz") == [5, 4, 2, 1, 6, 3, 0]
    assert candidate(stamp = "abc",target = "????????abcabc") == []
    assert candidate(stamp = "abc",target = "abcabcabcabcabc") == [11, 10, 8, 7, 5, 4, 2, 1, 12, 9, 6, 3, 0]
    assert candidate(stamp = "abcde",target = "abcde") == [0]
    assert candidate(stamp = "abc",target = "ababcbababcbababc") == [11, 9, 5, 3, 13, 10, 7, 4, 1, 12, 6, 0, 14, 8, 2]
    assert candidate(stamp = "mnopqr",target = "mnopqrmnopqrmnopqrmnopqrmnopqr") == [23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 24, 18, 12, 6, 0]
    assert candidate(stamp = "efgh",target = "efghefghefghefghefghefghefgh") == [23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 24, 20, 16, 12, 8, 4, 0]
    assert candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbcc") == [11, 10, 9, 8, 4, 3, 2, 1, 13, 12, 6, 5, 14, 7, 0]
    assert candidate(stamp = "abcd",target = "ddddddddddddddddddddddddddddabcd") == []
    assert candidate(stamp = "xyz",target = "xyxyxyxyxyxyxyxyxyxy") == []
    assert candidate(stamp = "zzz",target = "zzzzzzzzzzzzzzzzzzzz") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(stamp = "abcdef",target = "abcdefabcdefabcdefabcdefabcdefabcdef") == [29, 28, 27, 26, 25, 23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 30, 24, 18, 12, 6, 0]
    assert candidate(stamp = "xyz",target = "xyxyxyxyxyxyxyxyxyxyxyx") == []
    assert candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabcd") == []
    assert candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbccaaabbcc") == [18, 17, 16, 15, 11, 10, 9, 8, 4, 3, 2, 1, 20, 19, 13, 12, 6, 5, 21, 14, 7, 0]
    assert candidate(stamp = "xyz",target = "xyzxyzxyzxyzxyz") == [11, 10, 8, 7, 5, 4, 2, 1, 12, 9, 6, 3, 0]
    assert candidate(stamp = "abcd",target = "abcdabcdeabcdabcd") == []
    assert candidate(stamp = "aaaa",target = "aaaaaaaaaaaaaaaa") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcdef") == []
    assert candidate(stamp = "abc",target = "xyzabcxyzabcxyz") == []
    assert candidate(stamp = "abcd",target = "abcdabcdabcdabcd") == [11, 10, 9, 7, 6, 5, 3, 2, 1, 12, 8, 4, 0]
    assert candidate(stamp = "xyz",target = "xyzxyzxyzxyz") == [8, 7, 5, 4, 2, 1, 9, 6, 3, 0]
    assert candidate(stamp = "qrstuv",target = "qrstuvqrstuvqrstuvqrstuvqrstuvqrstuvqrstuv") == [35, 34, 33, 32, 31, 29, 28, 27, 26, 25, 23, 22, 21, 20, 19, 17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 36, 30, 24, 18, 12, 6, 0]
    assert candidate(stamp = "aaa",target = "aaaaaaaaaaaaaaaaaaaa") == [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(stamp = "a",target = "aaaaaaaaaaaaaaaaaaaa") == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(stamp = "xyzabc",target = "xyzabcxyzabcxyzabcxyzabc") == [17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 18, 12, 6, 0]
    assert candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabc") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]
    assert candidate(stamp = "abcde",target = "edcbaedcbaedcba") == []
    assert candidate(stamp = "abcabc",target = "abcabcabcabcabcabcabcabc") == [17, 16, 14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 18, 15, 12, 9, 6, 3, 0]
    assert candidate(stamp = "xyz",target = "xyzxyzxyzxyzxyzxyz") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]
    assert candidate(stamp = "qrst",target = "qrstqrstqrstqrstqrstqrstqrstqrst") == [27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 28, 24, 20, 16, 12, 8, 4, 0]
    assert candidate(stamp = "mnop",target = "mnopmnopmnopmnopmnopmnopmnopmnop") == [27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 28, 24, 20, 16, 12, 8, 4, 0]
    assert candidate(stamp = "abc",target = "abcabcabcabcabcabc") == [14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 15, 12, 9, 6, 3, 0]
    assert candidate(stamp = "abac",target = "abacabacabacabacabac") == [15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 16, 12, 8, 4, 0]
    assert candidate(stamp = "abc",target = "aaaaaaaaaaabcabcaaaaaaaaaa") == []
    assert candidate(stamp = "ab",target = "abababababababababab") == [17, 15, 13, 11, 9, 7, 5, 3, 1, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
    assert candidate(stamp = "stamp",target = "stampstampstamp") == [9, 8, 7, 6, 4, 3, 2, 1, 10, 5, 0]
    assert candidate(stamp = "abcdefg",target = "abcdefgabcdefgabcdefgabcdefg") == [20, 19, 18, 17, 16, 15, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 21, 14, 7, 0]
    assert candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcdeabc") == []
    assert candidate(stamp = "abab",target = "abababababababab") == [11, 9, 7, 5, 3, 1, 12, 10, 8, 6, 4, 2, 0]
    assert candidate(stamp = "ab",target = "abaabaabaab") == [7, 4, 1, 8, 5, 2, 9, 6, 3, 0]
    assert candidate(stamp = "hello",target = "hellohellohellohello") == [14, 13, 12, 11, 9, 8, 7, 6, 4, 3, 2, 1, 15, 10, 5, 0]
    assert candidate(stamp = "mnopqr",target = "mnopqrnopqrmonpqrnonqrmpnoqrmnoprqmnopqr") == []
    assert candidate(stamp = "abc",target = "ababababababababc") == [1, 3, 0, 5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 12, 14]
    assert candidate(stamp = "xyzxyz",target = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz") == [29, 28, 26, 25, 23, 22, 20, 19, 17, 16, 14, 13, 11, 10, 8, 7, 5, 4, 2, 1, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
    assert candidate(stamp = "hello",target = "hellohellohellohelloh") == []
    assert candidate(stamp = "abcd",target = "abcabcabcabc") == []
    assert candidate(stamp = "abcd",target = "abcdeabcd") == []
    assert candidate(stamp = "mnopqr",target = "mnopqrmnopqrmnopqr") == [11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 12, 6, 0]
    assert candidate(stamp = "aabbcc",target = "aabbccaaabbccaaabbccabc") == []
    assert candidate(stamp = "abcdef",target = "fedcbafedcbafedcba") == []
    assert candidate(stamp = "abcdef",target = "abcdefabcdefabcdefabcdef") == [17, 16, 15, 14, 13, 11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 18, 12, 6, 0]
    assert candidate(stamp = "stamp",target = "stampstampstampstam") == []
    assert candidate(stamp = "abcdefg",target = "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg") == [34, 33, 32, 31, 30, 29, 27, 26, 25, 24, 23, 22, 20, 19, 18, 17, 16, 15, 13, 12, 11, 10, 9, 8, 6, 5, 4, 3, 2, 1, 35, 28, 21, 14, 7, 0]
    assert candidate(stamp = "abcd",target = "abcdabcdabcdabcdabcd") == [15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 16, 12, 8, 4, 0]
    assert candidate(stamp = "abcd",target = "abcdabcabcd") == [6, 5, 3, 2, 1, 4, 7, 0]
    assert candidate(stamp = "xyzyx",target = "xyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyxyzyx") == [67, 66, 65, 63, 62, 61, 59, 58, 57, 55, 54, 53, 51, 50, 49, 47, 46, 45, 43, 42, 41, 39, 38, 37, 35, 34, 33, 31, 30, 29, 27, 26, 25, 23, 22, 21, 19, 18, 17, 15, 14, 13, 11, 10, 9, 7, 6, 5, 3, 2, 1, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0]
    assert candidate(stamp = "ab",target = "ababababababababababh") == []
    assert candidate(stamp = "abcde",target = "abcdeabcdeabcdeabcde") == [14, 13, 12, 11, 9, 8, 7, 6, 4, 3, 2, 1, 15, 10, 5, 0]
    assert candidate(stamp = "abcd",target = "dabcdabc") == []
    assert candidate(stamp = "aabbcc",target = "aabbccaabbccaaabbccaaabbccaaabbccaaabbcc") == [31, 30, 29, 28, 24, 23, 22, 21, 17, 16, 15, 14, 10, 9, 8, 7, 33, 32, 26, 25, 19, 18, 12, 11, 5, 4, 3, 2, 1, 34, 27, 20, 13, 6, 0]
    assert candidate(stamp = "aabbcc",target = "aabbccaabbccaabbcc") == [11, 10, 9, 8, 7, 5, 4, 3, 2, 1, 12, 6, 0]
    assert candidate(stamp = "abcdef",target = "fedcbafedcbafedcbafedcbafedcbafedcbafedcba") == []


