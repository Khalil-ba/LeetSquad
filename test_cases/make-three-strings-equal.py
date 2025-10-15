def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "abb",s3 = "ab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "abb",s3 = "ab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "abcdf",s3 = "abcde") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "abcdf",s3 = "abcde") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abcf",s3 = "abcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abcf",s3 = "abcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abce",s3 = "abcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abce",s3 = "abcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "xyw",s3 = "xyv") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "xyw",s3 = "xyv") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "abcde",s3 = "abcdef") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "abcde",s3 = "abcdef") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",s2 = "abfde",s3 = "abcde") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",s2 = "abfde",s3 = "abcde") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcghi",s3 = "abcjkl") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcghi",s3 = "abcjkl") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaa",s2 = "aaa",s3 = "aaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaa",s2 = "aaa",s3 = "aaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abc",s2 = "abc",s3 = "abcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abc",s2 = "abc",s3 = "abcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "a",s3 = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "a",s3 = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "xyw",s3 = "xy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "xyw",s3 = "xy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "dac",s2 = "bac",s3 = "cac") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "dac",s2 = "bac",s3 = "cac") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",s2 = "xyw",s3 = "xyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",s2 = "xyw",s3 = "xyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaa",s2 = "aaaaab",s3 = "aaaaac") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaa",s2 = "aaaaab",s3 = "aaaaac") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdegh",s3 = "abcdexh") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdegh",s3 = "abcdexh") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzz",s2 = "zzzzzzz",s3 = "zzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzz",s2 = "zzzzzzz",s3 = "zzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "same",s2 = "same",s3 = "same") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "same",s2 = "same",s3 = "same") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcdabcd",s2 = "abcdabcdabcdabcd",s3 = "abcdabcdabcdabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcdabcd",s2 = "abcdabcdabcdabcd",s3 = "abcdabcdabcdabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "different",s2 = "differences",s3 = "differentl") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "different",s2 = "differences",s3 = "differentl") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghik",s3 = "abcdefghi") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghik",s3 = "abcdefghi") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "ghijklm",s3 = "nopqrst") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "ghijklm",s3 = "nopqrst") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbaabb",s2 = "aabbaacc",s3 = "aabbaadd") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbaabb",s2 = "aabbaacc",s3 = "aabbaadd") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrstu",s2 = "pqrstv",s3 = "pqrstu") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrstu",s2 = "pqrstv",s3 = "pqrstu") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdeabcde",s2 = "abcdeabcdf",s3 = "abcdeabcde") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdeabcde",s2 = "abcdeabcdf",s3 = "abcdeabcde") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwerty",s2 = "qwerty",s3 = "qwertyu") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwerty",s2 = "qwerty",s3 = "qwertyu") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdeghi",s3 = "abcdefgj") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdeghi",s3 = "abcdefgj") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aabbc",s3 = "aabcc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aabbc",s3 = "aabcc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabcabcabc",s2 = "abcabcabcabcabcabc",s3 = "abcabcabcabcabcab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabcabcabc",s2 = "abcabcabcabcabcabc",s3 = "abcabcabcabcabcab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",s2 = "mississipp",s3 = "mississipp") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",s2 = "mississipp",s3 = "mississipp") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdefga",s3 = "abcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdefga",s3 = "abcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "hell",s3 = "helo") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "hell",s3 = "helo") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcde",s3 = "abcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcde",s3 = "abcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aabbc",s3 = "aab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aabbc",s3 = "aab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "testcase",s2 = "testcase",s3 = "testcases") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "testcase",s2 = "testcase",s3 = "testcases") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz",s3 = "zzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz",s3 = "zzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccdd",s2 = "aabbccdd",s3 = "aabbcddd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccdd",s2 = "aabbccdd",s3 = "aabbcddd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdefgh",s3 = "abcdefgh") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdefgh",s3 = "abcdefgh") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcxyz",s3 = "abcuvw") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcxyz",s3 = "abcuvw") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "xyyz",s3 = "xyzz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "xyyz",s3 = "xyzz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzz",s2 = "zzzzzzzz",s3 = "zzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzz",s2 = "zzzzzzzz",s3 = "zzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdef") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdef") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcdef",s3 = "ghijkl") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcdef",s3 = "ghijkl") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abracadabra",s2 = "abracadabr",s3 = "abracadaba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abracadabra",s2 = "abracadabr",s3 = "abracadaba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "abcdabc",s3 = "abcdab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "abcdabc",s3 = "abcdab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaabbbb",s2 = "aaaaacccc",s3 = "aaaaadddd") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaabbbb",s2 = "aaaaacccc",s3 = "aaaaadddd") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdefgj",s3 = "abcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdefgj",s3 = "abcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaa",s2 = "aaaaaa",s3 = "aaaaaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaa",s2 = "aaaaaa",s3 = "aaaaaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcdeg",s3 = "abcdef") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcdeg",s3 = "abcdef") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "fedcba",s3 = "abcdef") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "fedcba",s3 = "abcdef") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qrstuv",s2 = "qrstuw",s3 = "qrstvv") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qrstuv",s2 = "qrstuw",s3 = "qrstvv") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnop",s2 = "mnoq",s3 = "mnop") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnop",s2 = "mnoq",s3 = "mnop") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "longerstring",s2 = "longeststring",s3 = "longerstrings") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "longerstring",s2 = "longeststring",s3 = "longerstrings") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgxyz",s2 = "abcdefgxyw",s3 = "abcdefgxy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgxyz",s2 = "abcdefgxyw",s3 = "abcdefgxy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xylophone",s2 = "xylophon",s3 = "xylopho") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xylophone",s2 = "xylophon",s3 = "xylopho") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdehi",s3 = "abcdejk") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdehi",s3 = "abcdejk") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "python",s2 = "pythpn",s3 = "pythpn") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "python",s2 = "pythpn",s3 = "pythpn") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "abcdabce",s3 = "abcdabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "abcdabce",s3 = "abcdabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",s2 = "abcdabcdabcd",s3 = "abcdabcdabc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",s2 = "abcdabcdabcd",s3 = "abcdabcdabc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghij",s3 = "abcdefghijk") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghij",s3 = "abcdefghijk") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabbbb",s2 = "aaaabbbb",s3 = "aaaabbb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabbbb",s2 = "aaaabbbb",s3 = "aaaabbb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccdd",s2 = "aabbccde",s3 = "aabbccdf") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccdd",s2 = "aabbccde",s3 = "aabbccdf") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabc",s2 = "abcabc",s3 = "abcabd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabc",s2 = "abcabc",s3 = "abcabd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "a",s2 = "a",s3 = "b") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "a",s2 = "a",s3 = "b") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "ghijkl",s3 = "mnopqr") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "ghijkl",s3 = "mnopqr") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbaabb",s2 = "aabbaabb",s3 = "aabbaab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbaabb",s2 = "aabbaabb",s3 = "aabbaab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "matching",s2 = "match",s3 = "matchi") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "matching",s2 = "match",s3 = "matchi") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "unique",s2 = "uniquely",s3 = "uniquer") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "unique",s2 = "uniquely",s3 = "uniquer") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefh") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefh") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdxyz",s2 = "abcdwxy",s3 = "abcdvwx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdxyz",s2 = "abcdwxy",s3 = "abcdvwx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "programming",s2 = "programmer",s3 = "programing") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "programming",s2 = "programmer",s3 = "programing") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aabbbc",s3 = "aabbbcc") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aabbbc",s3 = "aabbbcc") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdefgg",s3 = "abcdefg") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdefgg",s3 = "abcdefg") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "abcdefghij",s3 = "abcdefgh") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "abcdefghij",s3 = "abcdefgh") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqr",s2 = "mnopqs",s3 = "mnopqt") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqr",s2 = "mnopqs",s3 = "mnopqt") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aabccc",s3 = "aabccx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aabccc",s3 = "aabccx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcxyz",s2 = "abcxyw",s3 = "abcxy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcxyz",s2 = "abcxyw",s3 = "abcxy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "abcdabcde",s3 = "abcdabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "abcdabcde",s3 = "abcdabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zxy",s2 = "zyx",s3 = "xyz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zxy",s2 = "zyx",s3 = "xyz") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzz",s2 = "zzzzz",s3 = "zzzz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzz",s2 = "zzzzz",s3 = "zzzz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aabbcd",s3 = "aabbbc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aabbcd",s3 = "aabbbc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",s2 = "abcdefh",s3 = "abcdefi") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",s2 = "abcdefh",s3 = "abcdefi") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",s2 = "abcabcabcabc",s3 = "abcabcabcab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",s2 = "abcabcabcabc",s3 = "abcabcabcab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaa",s2 = "aaaaa",s3 = "aaaab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaa",s2 = "aaaaa",s3 = "aaaab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyz",s2 = "xyzxyw",s3 = "xyzxy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyz",s2 = "xyzxyw",s3 = "xyzxy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaab",s2 = "aaaabb",s3 = "aaaaab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaab",s2 = "aaaabb",s3 = "aaaaab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "abcabcabcd",s3 = "abcabcabcde") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "abcabcabcd",s3 = "abcabcabcde") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcdfe",s3 = "abcdee") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcdfe",s3 = "abcdee") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",s2 = "abcde",s3 = "abcdf") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",s2 = "abcde",s3 = "abcdf") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyzxyz",s2 = "xyzxyzxy",s3 = "xyzxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyzxyz",s2 = "xyzxyzxy",s3 = "xyzxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "abcdbcd",s3 = "abcdabcd") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "abcdbcd",s3 = "abcdabcd") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "programming",s2 = "prognmming",s3 = "progrmming") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "programming",s2 = "prognmming",s3 = "progrmming") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "",s2 = "",s3 = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "",s2 = "",s3 = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijk",s2 = "abcdefghijl",s3 = "abcdefghijk") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijk",s2 = "abcdefghijl",s3 = "abcdefghijk") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",s2 = "abcdeabc",s3 = "abcdabcd") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",s2 = "abcdeabc",s3 = "abcdabcd") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",s2 = "abcdabcdabca",s3 = "abcdabcdabcd") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",s2 = "abcdabcdabca",s3 = "abcdabcdabcd") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabcabc",s2 = "abcabcabcabcabc",s3 = "abcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabcabc",s2 = "abcabcabcabcabc",s3 = "abcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdegh",s3 = "abcdefg") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdegh",s3 = "abcdefg") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzz",s2 = "zzzzz",s3 = "zzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzz",s2 = "zzzzz",s3 = "zzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "abcabcaba",s3 = "abcabcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "abcabcaba",s3 = "abcabcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaaaa",s2 = "aaaaaaab",s3 = "aaaaaaac") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaaaa",s2 = "aaaaaaab",s3 = "aaaaaaac") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccdd",s2 = "aabbccdee",s3 = "aabbccdde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccdd",s2 = "aabbccdee",s3 = "aabbccdde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxzyxzy",s2 = "xyxzyxzz",s3 = "xyxzyxzq") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxzyxzy",s2 = "xyxzyxzz",s3 = "xyxzyxzq") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcab") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcab") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzz",s2 = "zzzzzzz",s3 = "zzzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzz",s2 = "zzzzzzz",s3 = "zzzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdeabcde",s2 = "abcdeabced",s3 = "abcdeabcde") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdeabcde",s2 = "abcdeabced",s3 = "abcdeabcde") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",s2 = "aabbccddeeffg",s3 = "aabbccddeeffh") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",s2 = "aabbccddeeffg",s3 = "aabbccddeeffh") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",s2 = "hallo",s3 = "hella") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",s2 = "hallo",s3 = "hella") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbaabb",s2 = "aabbaaba",s3 = "aabbaabb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbaabb",s2 = "aabbaaba",s3 = "aabbaabb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "sameprefix",s2 = "sameprefixa",s3 = "sameprefixb") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "sameprefix",s2 = "sameprefixa",s3 = "sameprefixb") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",s2 = "abcdefghik",s3 = "abcdefghil") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",s2 = "abcdefghik",s3 = "abcdefghil") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgg",s2 = "aabbccddeeffgg",s3 = "aabbccddeeffgghh") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgg",s2 = "aabbccddeeffgg",s3 = "aabbccddeeffgghh") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabad",s2 = "abacabae",s3 = "abacabad") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabad",s2 = "abacabae",s3 = "abacabad") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyzxyz",s2 = "xyzxyzxyw",s3 = "xyzxyzxyv") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyzxyz",s2 = "xyzxyzxyw",s3 = "xyzxyzxyv") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzz",s2 = "xyzz",s3 = "xyzy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzz",s2 = "xyzz",s3 = "xyzy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",s2 = "abcdexyz",s3 = "abcdefyz") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",s2 = "abcdexyz",s3 = "abcdefyz") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababab",s2 = "babababa",s3 = "abababab") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababab",s2 = "babababa",s3 = "abababab") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",s2 = "abcdef",s3 = "abc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",s2 = "abcdef",s3 = "abc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyz",s2 = "xyzxyz",s3 = "xyzxyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyz",s2 = "xyzxyz",s3 = "xyzxyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",s2 = "aabbbcc",s3 = "aabcccc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",s2 = "aabbbcc",s3 = "aabcccc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzz",s2 = "zzzzzz",s3 = "zzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzz",s2 = "zzzzzz",s3 = "zzzzzz") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "abc",s2 = "abb",s3 = "ab") == 2
    assert candidate(s1 = "abcde",s2 = "abcdf",s3 = "abcde") == 3
    assert candidate(s1 = "abcd",s2 = "abcf",s3 = "abcd") == 3
    assert candidate(s1 = "abcd",s2 = "abce",s3 = "abcd") == 3
    assert candidate(s1 = "xyz",s2 = "xyw",s3 = "xyv") == 3
    assert candidate(s1 = "abcde",s2 = "abcde",s3 = "abcdef") == 1
    assert candidate(s1 = "abcde",s2 = "abfde",s3 = "abcde") == 9
    assert candidate(s1 = "abcdef",s2 = "abcghi",s3 = "abcjkl") == 9
    assert candidate(s1 = "aaa",s2 = "aaa",s3 = "aaa") == 0
    assert candidate(s1 = "abc",s2 = "abc",s3 = "abcd") == 1
    assert candidate(s1 = "a",s2 = "a",s3 = "a") == 0
    assert candidate(s1 = "xyz",s2 = "xyw",s3 = "xy") == 2
    assert candidate(s1 = "dac",s2 = "bac",s3 = "cac") == -1
    assert candidate(s1 = "xyz",s2 = "xyw",s3 = "xyx") == 3
    assert candidate(s1 = "aaaaa",s2 = "aaaaab",s3 = "aaaaac") == 2
    assert candidate(s1 = "abcdefgh",s2 = "abcdegh",s3 = "abcdexh") == 7
    assert candidate(s1 = "zzzzzzz",s2 = "zzzzzzz",s3 = "zzzzzzz") == 0
    assert candidate(s1 = "same",s2 = "same",s3 = "same") == 0
    assert candidate(s1 = "abcdabcdabcdabcd",s2 = "abcdabcdabcdabcd",s3 = "abcdabcdabcdabc") == 2
    assert candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefg") == 0
    assert candidate(s1 = "different",s2 = "differences",s3 = "differentl") == 6
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghik",s3 = "abcdefghi") == 2
    assert candidate(s1 = "abcdefg",s2 = "ghijklm",s3 = "nopqrst") == -1
    assert candidate(s1 = "aabbaabb",s2 = "aabbaacc",s3 = "aabbaadd") == 6
    assert candidate(s1 = "pqrstu",s2 = "pqrstv",s3 = "pqrstu") == 3
    assert candidate(s1 = "abcdeabcde",s2 = "abcdeabcdf",s3 = "abcdeabcde") == 3
    assert candidate(s1 = "qwerty",s2 = "qwerty",s3 = "qwertyu") == 1
    assert candidate(s1 = "abcdefgh",s2 = "abcdeghi",s3 = "abcdefgj") == 9
    assert candidate(s1 = "aabbcc",s2 = "aabbc",s3 = "aabcc") == 7
    assert candidate(s1 = "abcabcabcabcabcabc",s2 = "abcabcabcabcabcabc",s3 = "abcabcabcabcabcab") == 2
    assert candidate(s1 = "mississippi",s2 = "mississipp",s3 = "mississipp") == 1
    assert candidate(s1 = "abcdefgh",s2 = "abcdefga",s3 = "abcdefg") == 2
    assert candidate(s1 = "hello",s2 = "hell",s3 = "helo") == 4
    assert candidate(s1 = "abcdef",s2 = "abcde",s3 = "abcd") == 3
    assert candidate(s1 = "aabbcc",s2 = "aabbc",s3 = "aab") == 5
    assert candidate(s1 = "testcase",s2 = "testcase",s3 = "testcases") == 1
    assert candidate(s1 = "zzzzzzzzzz",s2 = "zzzzzzzzzz",s3 = "zzzzzzzzzzz") == 1
    assert candidate(s1 = "aabbccdd",s2 = "aabbccdd",s3 = "aabbcddd") == 9
    assert candidate(s1 = "abcdefgh",s2 = "abcdefgh",s3 = "abcdefgh") == 0
    assert candidate(s1 = "abcdef",s2 = "abcxyz",s3 = "abcuvw") == 9
    assert candidate(s1 = "xyzz",s2 = "xyyz",s3 = "xyzz") == 6
    assert candidate(s1 = "zzzzzzzz",s2 = "zzzzzzzz",s3 = "zzzzzzzz") == 0
    assert candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdef") == 2
    assert candidate(s1 = "abcdef",s2 = "abcdef",s3 = "ghijkl") == -1
    assert candidate(s1 = "abracadabra",s2 = "abracadabr",s3 = "abracadaba") == 4
    assert candidate(s1 = "abcdabcd",s2 = "abcdabc",s3 = "abcdab") == 3
    assert candidate(s1 = "aaaaabbbb",s2 = "aaaaacccc",s3 = "aaaaadddd") == 12
    assert candidate(s1 = "abcdefgh",s2 = "abcdefgj",s3 = "abcdefg") == 2
    assert candidate(s1 = "aaaaaa",s2 = "aaaaaa",s3 = "aaaaaaa") == 1
    assert candidate(s1 = "abcdef",s2 = "abcdeg",s3 = "abcdef") == 3
    assert candidate(s1 = "abcdef",s2 = "fedcba",s3 = "abcdef") == -1
    assert candidate(s1 = "qrstuv",s2 = "qrstuw",s3 = "qrstvv") == 6
    assert candidate(s1 = "mnop",s2 = "mnoq",s3 = "mnop") == 3
    assert candidate(s1 = "longerstring",s2 = "longeststring",s3 = "longerstrings") == 23
    assert candidate(s1 = "abcdefgxyz",s2 = "abcdefgxyw",s3 = "abcdefgxy") == 2
    assert candidate(s1 = "xylophone",s2 = "xylophon",s3 = "xylopho") == 3
    assert candidate(s1 = "abcdefg",s2 = "abcdehi",s3 = "abcdejk") == 6
    assert candidate(s1 = "python",s2 = "pythpn",s3 = "pythpn") == 6
    assert candidate(s1 = "abcdabcd",s2 = "abcdabce",s3 = "abcdabcd") == 3
    assert candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefx") == 3
    assert candidate(s1 = "abcdabcdabcd",s2 = "abcdabcdabcd",s3 = "abcdabcdabc") == 2
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghij",s3 = "abcdefghijk") == 1
    assert candidate(s1 = "aaaabbbb",s2 = "aaaabbbb",s3 = "aaaabbb") == 2
    assert candidate(s1 = "aabbccdd",s2 = "aabbccde",s3 = "aabbccdf") == 3
    assert candidate(s1 = "abcabc",s2 = "abcabc",s3 = "abcabd") == 3
    assert candidate(s1 = "a",s2 = "a",s3 = "b") == -1
    assert candidate(s1 = "abcdef",s2 = "ghijkl",s3 = "mnopqr") == -1
    assert candidate(s1 = "aabbaabb",s2 = "aabbaabb",s3 = "aabbaab") == 2
    assert candidate(s1 = "matching",s2 = "match",s3 = "matchi") == 4
    assert candidate(s1 = "unique",s2 = "uniquely",s3 = "uniquer") == 3
    assert candidate(s1 = "abcdefg",s2 = "abcdefg",s3 = "abcdefh") == 3
    assert candidate(s1 = "abcdxyz",s2 = "abcdwxy",s3 = "abcdvwx") == 9
    assert candidate(s1 = "programming",s2 = "programmer",s3 = "programing") == 10
    assert candidate(s1 = "aabbcc",s2 = "aabbbc",s3 = "aabbbcc") == 7
    assert candidate(s1 = "abcdefgh",s2 = "abcdefgg",s3 = "abcdefg") == 2
    assert candidate(s1 = "abcdefghijk",s2 = "abcdefghij",s3 = "abcdefgh") == 5
    assert candidate(s1 = "mnopqr",s2 = "mnopqs",s3 = "mnopqt") == 3
    assert candidate(s1 = "aabbcc",s2 = "aabccc",s3 = "aabccx") == 9
    assert candidate(s1 = "abcxyz",s2 = "abcxyw",s3 = "abcxy") == 2
    assert candidate(s1 = "abcdabcd",s2 = "abcdabcde",s3 = "abcdabcd") == 1
    assert candidate(s1 = "zxy",s2 = "zyx",s3 = "xyz") == -1
    assert candidate(s1 = "zzzzz",s2 = "zzzzz",s3 = "zzzz") == 2
    assert candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabd") == 3
    assert candidate(s1 = "aabbcc",s2 = "aabbcd",s3 = "aabbbc") == 6
    assert candidate(s1 = "abcdefg",s2 = "abcdefh",s3 = "abcdefi") == 3
    assert candidate(s1 = "abcabcabcabc",s2 = "abcabcabcabc",s3 = "abcabcabcab") == 2
    assert candidate(s1 = "aaaaa",s2 = "aaaaa",s3 = "aaaab") == 3
    assert candidate(s1 = "xyzxyz",s2 = "xyzxyw",s3 = "xyzxy") == 2
    assert candidate(s1 = "aaaaab",s2 = "aaaabb",s3 = "aaaaab") == 6
    assert candidate(s1 = "abcabcabc",s2 = "abcabcabcd",s3 = "abcabcabcde") == 3
    assert candidate(s1 = "abcdef",s2 = "abcdfe",s3 = "abcdee") == 6
    assert candidate(s1 = "abcd",s2 = "abcde",s3 = "abcdf") == 2
    assert candidate(s1 = "xyzxyzxyz",s2 = "xyzxyzxy",s3 = "xyzxyz") == 5
    assert candidate(s1 = "abcdabcd",s2 = "abcdbcd",s3 = "abcdabcd") == 11
    assert candidate(s1 = "programming",s2 = "prognmming",s3 = "progrmming") == 19
    assert candidate(s1 = "",s2 = "",s3 = "") == 0
    assert candidate(s1 = "abcdefghijk",s2 = "abcdefghijl",s3 = "abcdefghijk") == 3
    assert candidate(s1 = "abcdabcd",s2 = "abcdeabc",s3 = "abcdabcd") == 12
    assert candidate(s1 = "abcdabcdabcd",s2 = "abcdabcdabca",s3 = "abcdabcdabcd") == 3
    assert candidate(s1 = "abcabcabcabcabc",s2 = "abcabcabcabcabc",s3 = "abcabcabcabc") == 6
    assert candidate(s1 = "abcdefgh",s2 = "abcdegh",s3 = "abcdefg") == 7
    assert candidate(s1 = "zzzzzz",s2 = "zzzzz",s3 = "zzzz") == 3
    assert candidate(s1 = "abcabcabc",s2 = "abcabcaba",s3 = "abcabcabc") == 3
    assert candidate(s1 = "aaaaaaaa",s2 = "aaaaaaab",s3 = "aaaaaaac") == 3
    assert candidate(s1 = "aabbccdd",s2 = "aabbccdee",s3 = "aabbccdde") == 5
    assert candidate(s1 = "xyxzyxzy",s2 = "xyxzyxzz",s3 = "xyxzyxzq") == 3
    assert candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcab") == 2
    assert candidate(s1 = "zzzzzzzz",s2 = "zzzzzzz",s3 = "zzzzzz") == 3
    assert candidate(s1 = "abcdeabcde",s2 = "abcdeabced",s3 = "abcdeabcde") == 6
    assert candidate(s1 = "aabbccddeeff",s2 = "aabbccddeeffg",s3 = "aabbccddeeffh") == 2
    assert candidate(s1 = "hello",s2 = "hallo",s3 = "hella") == 12
    assert candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabcd") == 1
    assert candidate(s1 = "aabbaabb",s2 = "aabbaaba",s3 = "aabbaabb") == 3
    assert candidate(s1 = "sameprefix",s2 = "sameprefixa",s3 = "sameprefixb") == 2
    assert candidate(s1 = "abcdefghij",s2 = "abcdefghik",s3 = "abcdefghil") == 3
    assert candidate(s1 = "aabbccddeeffgg",s2 = "aabbccddeeffgg",s3 = "aabbccddeeffgghh") == 2
    assert candidate(s1 = "abcabcabc",s2 = "abcabcabc",s3 = "abcabcabx") == 3
    assert candidate(s1 = "abacabad",s2 = "abacabae",s3 = "abacabad") == 3
    assert candidate(s1 = "xyzxyzxyz",s2 = "xyzxyzxyw",s3 = "xyzxyzxyv") == 3
    assert candidate(s1 = "xyzz",s2 = "xyzz",s3 = "xyzy") == 3
    assert candidate(s1 = "abcdefgh",s2 = "abcdexyz",s3 = "abcdefyz") == 9
    assert candidate(s1 = "abababab",s2 = "babababa",s3 = "abababab") == -1
    assert candidate(s1 = "abcdef",s2 = "abcdef",s3 = "abc") == 6
    assert candidate(s1 = "xyzxyz",s2 = "xyzxyz",s3 = "xyzxyzz") == 1
    assert candidate(s1 = "aabbcc",s2 = "aabbbcc",s3 = "aabcccc") == 11
    assert candidate(s1 = "zzzzzz",s2 = "zzzzzz",s3 = "zzzzzz") == 0


