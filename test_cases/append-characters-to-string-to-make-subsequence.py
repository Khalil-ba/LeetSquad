def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "ghijkl") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "ghijkl") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab",t = "bbba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab",t = "bbba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "xyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "xyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",t = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",t = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "dbca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "dbca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",t = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",t = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa",t = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa",t = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab",t = "bbbb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab",t = "bbbb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab",t = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab",t = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "efghij") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "efghij") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",t = "oleh") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",t = "oleh") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "abdc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "abdc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "z",t = "abcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "z",t = "abcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "",t = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",t = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc",t = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc",t = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",t = "ole") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",t = "ole") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "efgh") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "efgh") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "b") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "b") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "coaching",t = "coding") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "coaching",t = "coding") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",t = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",t = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",t = "xyza") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",t = "xyza") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",t = "xyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",t = "xyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "",t = "abcd") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",t = "abcd") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "efgh") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "efgh") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",t = "aa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",t = "aa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "complex",t = "cmpx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "complex",t = "cmpx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",t = "abcabcabcabcabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",t = "abcabcabcabcabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstring",t = "thisstring") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstring",t = "thisstring") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellothere",t = "lohere") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellothere",t = "lohere") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",t = "bababa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",t = "bababa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyz",t = "xyzyzyzyzyzyzyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyz",t = "xyzyzyzyzyzyzyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",t = "dcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",t = "dcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",t = "abacaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",t = "abacaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thefastbrownfoxjumpsoverthelazydog",t = "quickbrownfox") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thefastbrownfoxjumpsoverthelazydog",t = "quickbrownfox") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",t = "acegik") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",t = "acegik") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "cbad") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "cbad") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",t = "bracadabr") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",t = "bracadabr") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwithvariouscharacters",t = "string") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwithvariouscharacters",t = "string") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "sequence",t = "subsequence") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sequence",t = "subsequence") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",t = "cccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",t = "cccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "longerstring",t = "string") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longerstring",t = "string") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",t = "abcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",t = "abcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",t = "fghijk") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",t = "fghijk") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",t = "defghijk") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",t = "defghijk") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdexyz",t = "dezy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdexyz",t = "dezy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",t = "zyxzyxzyx") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",t = "zyxzyxzyx") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",t = "abab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",t = "abab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "kglvkyeavnnrdq",t = "lky") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "kglvkyeavnnrdq",t = "lky") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",t = "abcdabcdabcd") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",t = "abcdabcdabcd") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "hijjiklmn") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "hijjiklmn") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "overlaplaplap",t = "laplaplaplap") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlaplaplap",t = "laplaplaplap") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxy",t = "xyyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxy",t = "xyyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",t = "heoo") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",t = "heoo") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "edcba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "edcba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "randomstring",t = "stringrandom") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "randomstring",t = "stringrandom") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "",t = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",t = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "pis") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "pis") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",t = "abcabcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",t = "abcabcabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "sequencealignment",t = "seqaln") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sequencealignment",t = "seqaln") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "testtesttest",t = "testset") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "testtesttest",t = "testset") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "pippi") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "pippi") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "issip") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "issip") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "sequencealignment",t = "quencal") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sequencealignment",t = "quencal") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "",t = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",t = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "jihgfedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "jihgfedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "gram") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "gram") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef",t = "fedcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef",t = "fedcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "xyzuvw") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "xyzuvw") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",t = "abcd") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",t = "abcd") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "issi") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "issi") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccccdddddeeeee",t = "abcde") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccccdddddeeeee",t = "abcde") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwithrandomcharacters",t = "lgrmc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwithrandomcharacters",t = "lgrmc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",t = "abcdefghij") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",t = "abcdefghij") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "patternmatching",t = "ternat") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "patternmatching",t = "ternat") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeff",t = "abcdeff") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeff",t = "abcdeff") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "abcdeabcde") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "abcdeabcde") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "uniquecharacters",t = "charactersunique") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "uniquecharacters",t = "charactersunique") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "progmin") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "progmin") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "subsequence",t = "subs") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "subsequence",t = "subs") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellothere",t = "othertimes") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellothere",t = "othertimes") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",t = "aabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",t = "aabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "efghij") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "efghij") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "isip") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "isip") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdef",t = "fedcbafedcba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdef",t = "fedcbafedcba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "longerstringwithcharacters",t = "stringcharacters") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longerstringwithcharacters",t = "stringcharacters") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zyxwvutsrqponmlkjihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zyxwvutsrqponmlkjihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "short",t = "longerstring") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "short",t = "longerstring") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",t = "abcabcabc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",t = "abcabcabc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",t = "zzzzyyyyxxxxwwwwvvvvuuuuttttrrrrqqqqpppplllloooonnnnmmmkkkkjjjjiiiihhhhhggggggfffffeeeeeddddccccbbbbbaaaa") == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",t = "zzzzyyyyxxxxwwwwvvvvuuuuttttrrrrqqqqpppplllloooonnnnmmmkkkkjjjjiiiihhhhhggggggfffffeeeeeddddccccbbbbbaaaa") == 105: {e}')
    
    total += 1
    try:
        result = candidate(s = "overlappingcharacters",t = "lap") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlappingcharacters",t = "lap") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "sequence",t = "quen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sequence",t = "quen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "zzzzzzzzzz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "zzzzzzzzzz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",t = "abababab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",t = "abababab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "ihgfedcba") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "ihgfedcba") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstring",t = "isaverylong") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstring",t = "isaverylong") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",t = "gramming") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",t = "gramming") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "longeststring",t = "tiny") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longeststring",t = "tiny") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",t = "zyxzyxzyx") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",t = "zyxzyxzyx") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdeabcdeabcde",t = "abcdee") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdeabcdeabcde",t = "abcdee") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",t = "acadabra") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",t = "acadabra") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "ppip") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "ppip") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "onetwothreefourfive",t = "owhfv") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "onetwothreefourfive",t = "owhfv") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",t = "bbbbb") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",t = "bbbbb") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzzyyxwwvvuutsrrqppoonnmlkkjjiihhggffeeddccbbaa") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzzyyxwwvvuutsrrqppoonnmlkkjjiihhggffeeddccbbaa") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "hijjiklm") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "hijjiklm") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "example",t = "ample") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "example",t = "ample") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",t = "lelo") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",t = "lelo") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",t = "abcabcabcabcabcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",t = "abcabcabcabcabcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "characters",t = "char") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "characters",t = "char") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",t = "abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",t = "abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",t = "aaaabbbbcccc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",t = "aaaabbbbcccc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzuvw",t = "abcdefghijklmnopqrstuvwxyz") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzuvw",t = "abcdefghijklmnopqrstuvwxyz") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",t = "wxyzyxwxyzyx") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",t = "wxyzyxwxyzyx") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",t = "abcbcabcbcabcbca") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",t = "abcbcabcbcabcbca") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "randomstring",t = "random") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "randomstring",t = "random") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghiklmnopqrstuvwxyz",t = "mnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghiklmnopqrstuvwxyz",t = "mnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacadaea",t = "abcde") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacadaea",t = "abcde") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",t = "aaaaaab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",t = "aaaaaab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "sequence",t = "seq") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "sequence",t = "seq") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedcharactersrepeatedcharacters",t = "characterscharacterscharacters") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedcharactersrepeatedcharacters",t = "characterscharacterscharacters") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "hijjijk") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "hijjijk") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",t = "abcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",t = "abcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzabc",t = "uvwabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzabc",t = "uvwabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "alibabacloud",t = "aliloud") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alibabacloud",t = "aliloud") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",t = "bbcccaaa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",t = "bbcccaaa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccc",t = "abcabc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccc",t = "abcabc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",t = "olelh") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",t = "olelh") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",t = "agh") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",t = "agh") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijkllkjihgfedcba",t = "abcdefghijkllkjihgfedcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijkllkjihgfedcba",t = "abcdefghijkllkjihgfedcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "overlappingoverlapping",t = "lapover") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "overlappingoverlapping",t = "lapover") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",t = "aabbaabbaabbaabb") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",t = "aabbaabbaabbaabb") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyz",t = "xyzxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyz",t = "xyzxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellotherehellothere",t = "helloothere") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellotherehellothere",t = "helloothere") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "hijjikl") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "hijjikl") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",t = "badaba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",t = "badaba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyzzz",t = "zzzyyxxwwvvuuuttrrssqqppoonnmmlkkjjiihhgggfffeeeddccbbaaa") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyzzz",t = "zzzyyxxwwvvuuuttrrssqqppoonnmmlkkjjiihhgggfffeeeddccbbaaa") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvut") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvut") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "hijjik") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "hijjik") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",t = "abcdefg") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",t = "abcdefg") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "acegik") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "acegik") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",t = "racecar") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",t = "racecar") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",t = "abcde") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",t = "abcde") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghij") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghij") == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcdefgh",t = "ghijkl") == 4
    assert candidate(s = "ababab",t = "bbba") == 1
    assert candidate(s = "abcd",t = "xyz") == 3
    assert candidate(s = "aaaa",t = "a") == 0
    assert candidate(s = "abcd",t = "dbca") == 3
    assert candidate(s = "aabbcc",t = "abc") == 0
    assert candidate(s = "aaaaa",t = "a") == 0
    assert candidate(s = "abcd",t = "abcde") == 1
    assert candidate(s = "ababab",t = "bbbb") == 1
    assert candidate(s = "ab",t = "abc") == 1
    assert candidate(s = "abcdefgh",t = "efghij") == 2
    assert candidate(s = "hello",t = "oleh") == 3
    assert candidate(s = "abcd",t = "") == 0
    assert candidate(s = "abcde",t = "a") == 0
    assert candidate(s = "abcd",t = "abdc") == 1
    assert candidate(s = "abcd",t = "abcd") == 0
    assert candidate(s = "z",t = "abcde") == 5
    assert candidate(s = "",t = "abc") == 3
    assert candidate(s = "abcabc",t = "abc") == 0
    assert candidate(s = "hello",t = "ole") == 2
    assert candidate(s = "abcdefgh",t = "efgh") == 0
    assert candidate(s = "a",t = "b") == 1
    assert candidate(s = "coaching",t = "coding") == 4
    assert candidate(s = "abc",t = "") == 0
    assert candidate(s = "xyz",t = "xyza") == 1
    assert candidate(s = "xyz",t = "xyz") == 0
    assert candidate(s = "",t = "abcd") == 4
    assert candidate(s = "abcd",t = "efgh") == 4
    assert candidate(s = "aaaa",t = "aa") == 0
    assert candidate(s = "complex",t = "cmpx") == 0
    assert candidate(s = "abcabcabcabcabcabc",t = "abcabcabcabcabcd") == 1
    assert candidate(s = "thisisaverylongstring",t = "thisstring") == 0
    assert candidate(s = "hellothere",t = "lohere") == 0
    assert candidate(s = "ababababab",t = "bababa") == 0
    assert candidate(s = "xyzxyzxyzxyzxyz",t = "xyzyzyzyzyzyzyz") == 4
    assert candidate(s = "abcdabcdabcd",t = "dcba") == 1
    assert candidate(s = "abcabcabcabc",t = "abacaba") == 0
    assert candidate(s = "thefastbrownfoxjumpsoverthelazydog",t = "quickbrownfox") == 13
    assert candidate(s = "abcdefghijk",t = "acegik") == 0
    assert candidate(s = "abcde",t = "cbad") == 3
    assert candidate(s = "abracadabra",t = "bracadabr") == 0
    assert candidate(s = "longstringwithvariouscharacters",t = "string") == 0
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 24
    assert candidate(s = "sequence",t = "subsequence") == 9
    assert candidate(s = "abcabcabcabc",t = "cccc") == 0
    assert candidate(s = "longerstring",t = "string") == 0
    assert candidate(s = "aaaabbbbcccc",t = "abcabc") == 3
    assert candidate(s = "abcdef",t = "fghijk") == 5
    assert candidate(s = "abcdef",t = "defghijk") == 5
    assert candidate(s = "abcdexyz",t = "dezy") == 1
    assert candidate(s = "xyzxyzxyz",t = "zyxzyxzyx") == 5
    assert candidate(s = "abababababababab",t = "abab") == 0
    assert candidate(s = "kglvkyeavnnrdq",t = "lky") == 0
    assert candidate(s = "abcabcabcabc",t = "abcdabcdabcd") == 9
    assert candidate(s = "abcdefghij",t = "hijjiklmn") == 6
    assert candidate(s = "overlaplaplap",t = "laplaplaplap") == 3
    assert candidate(s = "xyxyxyxyxy",t = "xyyx") == 0
    assert candidate(s = "hello",t = "heoo") == 1
    assert candidate(s = "abcde",t = "edcba") == 4
    assert candidate(s = "randomstring",t = "stringrandom") == 6
    assert candidate(s = "",t = "a") == 1
    assert candidate(s = "mississippi",t = "pis") == 1
    assert candidate(s = "abcdabcdabcd",t = "abcabcabc") == 0
    assert candidate(s = "sequencealignment",t = "seqaln") == 0
    assert candidate(s = "testtesttest",t = "testset") == 0
    assert candidate(s = "mississippi",t = "pippi") == 3
    assert candidate(s = "mississippi",t = "issip") == 0
    assert candidate(s = "sequencealignment",t = "quencal") == 0
    assert candidate(s = "",t = "") == 0
    assert candidate(s = "abcdefghij",t = "jihgfedcba") == 9
    assert candidate(s = "programming",t = "gram") == 0
    assert candidate(s = "abcdef",t = "fedcba") == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "xyzuvw") == 3
    assert candidate(s = "abacabadabacaba",t = "abcd") == 0
    assert candidate(s = "mississippi",t = "issi") == 0
    assert candidate(s = "aaaaabbbbbcccccdddddeeeee",t = "abcde") == 0
    assert candidate(s = "longstringwithrandomcharacters",t = "lgrmc") == 0
    assert candidate(s = "zzzzzzzzzz",t = "abcdefghij") == 10
    assert candidate(s = "patternmatching",t = "ternat") == 0
    assert candidate(s = "aabbaabbccddeeff",t = "abcdeff") == 0
    assert candidate(s = "abcde",t = "abcdeabcde") == 5
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(s = "uniquecharacters",t = "charactersunique") == 6
    assert candidate(s = "programming",t = "progmin") == 0
    assert candidate(s = "subsequence",t = "subs") == 0
    assert candidate(s = "hellothere",t = "othertimes") == 5
    assert candidate(s = "aaaaaa",t = "aabbcc") == 4
    assert candidate(s = "abcde",t = "efghij") == 5
    assert candidate(s = "mississippi",t = "isip") == 0
    assert candidate(s = "abcdefabcdef",t = "fedcbafedcba") == 10
    assert candidate(s = "longerstringwithcharacters",t = "stringcharacters") == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(s = "short",t = "longerstring") == 12
    assert candidate(s = "abcabcabcabcabc",t = "abcabcabc") == 0
    assert candidate(s = "abababababababab",t = "zzzzyyyyxxxxwwwwvvvvuuuuttttrrrrqqqqpppplllloooonnnnmmmkkkkjjjjiiiihhhhhggggggfffffeeeeeddddccccbbbbbaaaa") == 105
    assert candidate(s = "overlappingcharacters",t = "lap") == 0
    assert candidate(s = "sequence",t = "quen") == 0
    assert candidate(s = "abcdefghij",t = "zzzzzzzzzz") == 10
    assert candidate(s = "aaaaabbbbb",t = "abababab") == 6
    assert candidate(s = "abcdefgh",t = "ihgfedcba") == 9
    assert candidate(s = "thisisaverylongstring",t = "isaverylong") == 0
    assert candidate(s = "programming",t = "gramming") == 0
    assert candidate(s = "longeststring",t = "tiny") == 1
    assert candidate(s = "xyz",t = "zyxzyxzyx") == 8
    assert candidate(s = "abcdeabcdeabcde",t = "abcdee") == 0
    assert candidate(s = "abracadabra",t = "acadabra") == 0
    assert candidate(s = "mississippi",t = "ppip") == 1
    assert candidate(s = "onetwothreefourfive",t = "owhfv") == 0
    assert candidate(s = "aaaaaa",t = "bbbbb") == 5
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzzyyxwwvvuutsrrqppoonnmlkkjjiihhggffeeddccbbaa") == 45
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaab") == 1
    assert candidate(s = "abcdefghij",t = "hijjiklm") == 5
    assert candidate(s = "example",t = "ample") == 0
    assert candidate(s = "hello",t = "lelo") == 3
    assert candidate(s = "abcabcabcabc",t = "abcabcabcabcabcabc") == 6
    assert candidate(s = "characters",t = "char") == 0
    assert candidate(s = "aaaabbbbcccc",t = "abc") == 0
    assert candidate(s = "aaaaaaaaaa",t = "aaaabbbbcccc") == 8
    assert candidate(s = "xyzuvw",t = "abcdefghijklmnopqrstuvwxyz") == 26
    assert candidate(s = "xyz",t = "wxyzyxwxyzyx") == 12
    assert candidate(s = "abcabcabcabcabc",t = "abcbcabcbcabcbca") == 3
    assert candidate(s = "randomstring",t = "random") == 0
    assert candidate(s = "abcdefghiklmnopqrstuvwxyz",t = "mnopqrstuvwxyz") == 0
    assert candidate(s = "aabacadaea",t = "abcde") == 0
    assert candidate(s = "aaaaaa",t = "aaaaaab") == 1
    assert candidate(s = "sequence",t = "seq") == 0
    assert candidate(s = "repeatedcharactersrepeatedcharacters",t = "characterscharacterscharacters") == 10
    assert candidate(s = "abcdefghij",t = "hijjijk") == 4
    assert candidate(s = "abacabadabacaba",t = "abcabcabc") == 1
    assert candidate(s = "xyzabc",t = "uvwabc") == 6
    assert candidate(s = "alibabacloud",t = "aliloud") == 0
    assert candidate(s = "aaaabbbbcccc",t = "bbcccaaa") == 3
    assert candidate(s = "aaaaabbbbbcccc",t = "abcabc") == 3
    assert candidate(s = "hello",t = "olelh") == 4
    assert candidate(s = "abcdefg",t = "agh") == 1
    assert candidate(s = "abcdefghijkllkjihgfedcba",t = "abcdefghijkllkjihgfedcba") == 0
    assert candidate(s = "overlappingoverlapping",t = "lapover") == 0
    assert candidate(s = "a",t = "") == 0
    assert candidate(s = "abcabcabcabcabc",t = "aabbaabbaabbaabb") == 9
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba") == 25
    assert candidate(s = "xyzzyxzyxzyz",t = "xyzxyz") == 0
    assert candidate(s = "hellotherehellothere",t = "helloothere") == 0
    assert candidate(s = "abcdefghij",t = "hijjikl") == 4
    assert candidate(s = "abacabadabacaba",t = "badaba") == 0
    assert candidate(s = "aaabbbcccdddeeefffggghhhiiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxxyyyzzz",t = "zzzyyxxwwvvuuuttrrssqqppoonnmmlkkjjiihhgggfffeeeddccbbaaa") == 54
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvut") == 6
    assert candidate(s = "abcdefghij",t = "hijjik") == 3
    assert candidate(s = "aabbccddeeffgg",t = "abcdefg") == 0
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopasdfghjklzxcvbnmqwertyuiop") == 10
    assert candidate(s = "abcdefghij",t = "acegik") == 1
    assert candidate(s = "racecar",t = "racecar") == 0
    assert candidate(s = "abracadabra",t = "abcde") == 1
    assert candidate(s = "abcdefghij",t = "abcdefghij") == 0


