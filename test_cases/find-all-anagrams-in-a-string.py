def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "hello",p = "billion") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",p = "billion") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa",p = "a") == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa",p = "a") == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaa",p = "ab") == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaa",p = "ab") == [1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abab",p = "ab") == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abab",p = "ab") == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbabc",p = "abc") == [1, 2, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbabc",p = "abc") == [1, 2, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",p = "a") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",p = "a") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaa",p = "aa") == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaa",p = "aa") == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbaebabacd",p = "abc") == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbaebabacd",p = "abc") == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyz",p = "zyx") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyz",p = "zyx") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",p = "aaa") == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",p = "aaa") == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",p = "issi") == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",p = "issi") == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",p = "abc") == [0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",p = "abc") == [0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",p = "abc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",p = "abc") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",p = "issip") == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",p = "issip") == [4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",p = "efgh") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",p = "efgh") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",p = "fgh") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",p = "fgh") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",p = "gfedcba") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",p = "gfedcba") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd",p = "abcd") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd",p = "abcd") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",p = "oll") == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",p = "oll") == [2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "p",p = "p") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "p",p = "p") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zdhfkahfewrfsad",p = "fes") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zdhfkahfewrfsad",p = "fes") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ananananan",p = "nana") == [0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ananananan",p = "nana") == [0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzz",p = "zzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzz",p = "zzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "anagramanagramanagram",p = "anagramanagram") == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anagramanagramanagram",p = "anagramanagram") == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzz",p = "xxyyzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzz",p = "xxyyzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aquickbrownfoxjumpsoverthelazydog",p = "quick") == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aquickbrownfoxjumpsoverthelazydog",p = "quick") == [1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzz",p = "xyz") == [0, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzz",p = "xyz") == [0, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "almostanagram",p = "anagram") == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "almostanagram",p = "anagram") == [6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",p = "abcdefghijklmnop") == [0, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",p = "abcdefghijklmnop") == [0, 26]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdeabcdabcdeabcdabcde",p = "abcde") == [4, 5, 6, 7, 8, 13, 14, 15, 16, 17, 22]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdeabcdabcdeabcdabcde",p = "abcde") == [4, 5, 6, 7, 8, 13, 14, 15, 16, 17, 22]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii",p = "abcdefghi") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii",p = "abcdefghi") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "aquickbrownfoxjumpsoverlazydog",p = "lazy") == [23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aquickbrownfoxjumpsoverlazydog",p = "lazy") == [23]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringtocheckanagrams",p = "strings") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringtocheckanagrams",p = "strings") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyx",p = "zyx") == [1, 2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyx",p = "zyx") == [1, 2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaaaab",p = "ab") == [1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaaaab",p = "ab") == [1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",p = "bbccbb") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",p = "bbccbb") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababababababababababababababababababab",p = "bab") == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababababababababababababababababababab",p = "bab") == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",p = "abcabc") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",p = "abcabc") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcd",p = "dcba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcd",p = "dcba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqrstuvwxyz") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqrstuvwxyz") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisanotherexample",p = "ample") == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisanotherexample",p = "ample") == [15]: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",p = "bcab") == [1, 2, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",p = "bcab") == [1, 2, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "zyxwvutsrqponmlkjihgfedcba") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "zyxwvutsrqponmlkjihgfedcba") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzyxyzzzzzyxyzzzzzy",p = "zzzzzyxy") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzyxyzzzzzyxyzzzzzy",p = "zzzzzyxy") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "repeatedpatternrepeatedpatternrepeated",p = "repeatedpattern") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "repeatedpatternrepeatedpatternrepeated",p = "repeatedpattern") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]: {e}')
    
    total += 1
    try:
        result = candidate(s = "eidbaooo",p = "ab") == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eidbaooo",p = "ab") == [3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "acdfgdcagdfgdsf",p = "gcd") == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acdfgdcagdfgdsf",p = "gcd") == [4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",p = "gfedcba") == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",p = "gfedcba") == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqrstuvwxzy") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqrstuvwxzy") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",p = "xyz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",p = "xyz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbc",p = "bccb") == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbc",p = "bccb") == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",p = "ihgfedcba") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",p = "ihgfedcba") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",p = "cba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",p = "cba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",p = "abc") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",p = "abc") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "zyxwvutsrqponmlkjihgfedcba") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "zyxwvutsrqponmlkjihgfedcba") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",p = "pneumonia") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",p = "pneumonia") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "counterexampletofindallanagramsinaverylargeinputstring",p = "example") == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "counterexampletofindallanagramsinaverylargeinputstring",p = "example") == [7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazazazazaz",p = "aaa") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazazazazaz",p = "aaa") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",p = "test") == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",p = "test") == [7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababa",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababa",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",p = "xyzzyx") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",p = "xyzzyx") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]: {e}')
    
    total += 1
    try:
        result = candidate(s = "anagramananagramanagramanagramanagram",p = "nagaram") == [0, 1, 2, 3, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anagramananagramanagramanagramanagram",p = "nagaram") == [0, 1, 2, 3, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcde",p = "cde") == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcde",p = "cde") == [6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbabcabcab",p = "abc") == [1, 2, 3, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbabcabcab",p = "abc") == [1, 2, 3, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(s = "anananananananananananananananananananananana",p = "nana") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anananananananananananananananananananananana",p = "nana") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaab",p = "ba") == [26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaab",p = "ba") == [26]: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbabcabcabcabcabcabcabcabcabcabc",p = "bac") == [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbabcabcabcabcabcabcabcabcabcabc",p = "bac") == [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaab",p = "aaaab") == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaab",p = "aaaab") == [8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ldfldjflsdkflsdkjfldsjkfldsjfldsjflsdkjfldskjflds",p = "sdkjf") == [13, 19, 35, 41]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ldfldjflsdkflsdkjfldsjkfldsjfldsjflsdkjfldskjflds",p = "sdkjf") == [13, 19, 35, 41]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",p = "abab") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",p = "abab") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeff",p = "abcdef") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeff",p = "abcdef") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",p = "zzz") == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",p = "zzz") == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyzzxyz",p = "xyz") == [0, 1, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyzzxyz",p = "xyz") == [0, 1, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisanexampleofaverylongstringwherefindinganagramsisnotthatstraightforward",p = "anagram") == [44]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisanexampleofaverylongstringwherefindinganagramsisnotthatstraightforward",p = "anagram") == [44]: {e}')
    
    total += 1
    try:
        result = candidate(s = "anagramananagramananagram",p = "anagram") == [0, 1, 2, 3, 9, 10, 11, 12, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anagramananagramananagram",p = "anagram") == [0, 1, 2, 3, 9, 10, 11, 12, 18]: {e}')
    
    total += 1
    try:
        result = candidate(s = "anananananananananananananananananana",p = "anana") == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anananananananananananananananananana",p = "anana") == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",p = "jihgfedcba") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",p = "jihgfedcba") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",p = "aaaaaa") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",p = "aaaaaa") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqr") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqr") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",p = "mnbvcxzlkjhgfdsapoiuytrewq") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",p = "mnbvcxzlkjhgfdsapoiuytrewq") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacb",p = "acbac") == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacb",p = "acbac") == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63]: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohellohellohellohellohellohellohello",p = "world") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohellohellohellohellohellohellohello",p = "world") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "anagramanagramanagram",p = "nagaram") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "anagramanagramanagram",p = "nagaram") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",p = "mnbvcxzlkjhgfdsapoiuytrewq") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",p = "mnbvcxzlkjhgfdsapoiuytrewq") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]: {e}')
    
    total += 1
    try:
        result = candidate(s = "layer",p = "relay") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "layer",p = "relay") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "quickbrownfoxjumpsoverthelazydog",p = "thequickbrownfoxjumpsover") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "quickbrownfoxjumpsoverthelazydog",p = "thequickbrownfoxjumpsover") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "llllllllllllllllllllllllllllllllllllll",p = "ll") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "llllllllllllllllllllllllllllllllllllll",p = "ll") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",p = "aab") == [62]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",p = "aab") == [62]: {e}')
    
    total += 1
    try:
        result = candidate(s = "qazwsxedcrfvtgbyhnujmikolp",p = "lopihgfytvremkluzxwqjncbv") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qazwsxedcrfvtgbyhnujmikolp",p = "lopihgfytvremkluzxwqjncbv") == []: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",p = "abacab") == [0, 1, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",p = "abacab") == [0, 1, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithseveralrepeatingcharacters",p = "characters") == [41]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithseveralrepeatingcharacters",p = "characters") == [41]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhii",p = "iihhggffeeddccbbaa") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhii",p = "iihhggffeeddccbbaa") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisanagram",p = "nagaram") == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisanagram",p = "nagaram") == [6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",p = "zyxwvutsrqponmlkjihgfedcba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",p = "zyxwvutsrqponmlkjihgfedcba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",p = "abcdef") == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",p = "abcdef") == []: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "hello",p = "billion") == []
    assert candidate(s = "aaaaa",p = "a") == [0, 1, 2, 3, 4]
    assert candidate(s = "bbaa",p = "ab") == [1]
    assert candidate(s = "abab",p = "ab") == [0, 1, 2]
    assert candidate(s = "abacbabc",p = "abc") == [1, 2, 3, 5]
    assert candidate(s = "a",p = "a") == [0]
    assert candidate(s = "aaaaaa",p = "aa") == [0, 1, 2, 3, 4]
    assert candidate(s = "cbaebabacd",p = "abc") == [0, 6]
    assert candidate(s = "xyz",p = "zyx") == [0]
    assert candidate(s = "aaaaaaaaaa",p = "aaa") == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "mississippi",p = "issi") == [1, 4]
    assert candidate(s = "abcabcabc",p = "abc") == [0, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "aabbcc",p = "abc") == []
    assert candidate(s = "mississippi",p = "issip") == [4]
    assert candidate(s = "abcd",p = "efgh") == []
    assert candidate(s = "abcde",p = "fgh") == []
    assert candidate(s = "abcdefg",p = "gfedcba") == [0]
    assert candidate(s = "aabbccdd",p = "abcd") == []
    assert candidate(s = "hello",p = "oll") == [2]
    assert candidate(s = "p",p = "p") == [0]
    assert candidate(s = "zdhfkahfewrfsad",p = "fes") == []
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
    assert candidate(s = "ananananan",p = "nana") == [0, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "ababababababababababababababababababababababababababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
    assert candidate(s = "zzzzzzzzzzzzzzzz",p = "zzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(s = "anagramanagramanagram",p = "anagramanagram") == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "xxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzzxxyyzz",p = "xxyyzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
    assert candidate(s = "aquickbrownfoxjumpsoverthelazydog",p = "quick") == [1]
    assert candidate(s = "xyzzxyzz",p = "xyz") == [0, 3, 4]
    assert candidate(s = "almostanagram",p = "anagram") == [6]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",p = "abcdefghijklmnop") == [0, 26]
    assert candidate(s = "abcdabcdeabcdabcdeabcdabcde",p = "abcde") == [4, 5, 6, 7, 8, 13, 14, 15, 16, 17, 22]
    assert candidate(s = "aabbccddeeffgghhii",p = "abcdefghi") == []
    assert candidate(s = "aquickbrownfoxjumpsoverlazydog",p = "lazy") == [23]
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzzzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    assert candidate(s = "thisisaverylongstringtocheckanagrams",p = "strings") == []
    assert candidate(s = "xyxzyzyx",p = "zyx") == [1, 2, 5]
    assert candidate(s = "bbaaaaab",p = "ab") == [1, 6]
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",p = "bbccbb") == []
    assert candidate(s = "abababababababababababababababababababababababababababababababababababababababababababab",p = "bab") == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85]
    assert candidate(s = "abcabcabcabcabcabc",p = "abcabc") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(s = "abcdabcdabcdabcd",p = "dcba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqrstuvwxyz") == []
    assert candidate(s = "thisisanotherexample",p = "ample") == [15]
    assert candidate(s = "acbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",p = "bcab") == [1, 2, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "zyxwvutsrqponmlkjihgfedcba") == []
    assert candidate(s = "xyzzzzzyxyzzzzzyxyzzzzzy",p = "zzzzzyxy") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert candidate(s = "repeatedpatternrepeatedpatternrepeated",p = "repeatedpattern") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    assert candidate(s = "eidbaooo",p = "ab") == [3]
    assert candidate(s = "acdfgdcagdfgdsf",p = "gcd") == [4]
    assert candidate(s = "abcdefgabcdefg",p = "gfedcba") == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqrstuvwxzy") == []
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",p = "xyz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
    assert candidate(s = "bcbcbcbcbcbc",p = "bccb") == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(s = "abcdefghij",p = "ihgfedcba") == [0]
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",p = "cba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzz") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbcccccccccc",p = "abc") == []
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",p = "zyxwvutsrqponmlkjihgfedcba") == [0]
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",p = "pneumonia") == []
    assert candidate(s = "counterexampletofindallanagramsinaverylargeinputstring",p = "example") == [7]
    assert candidate(s = "zazazazazaz",p = "aaa") == []
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",p = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == [0]
    assert candidate(s = "thisisateststring",p = "test") == [7]
    assert candidate(s = "ababababababababababababababababa",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",p = "xyzzyx") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    assert candidate(s = "anagramananagramanagramanagramanagram",p = "nagaram") == [0, 1, 2, 3, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    assert candidate(s = "abcdabcde",p = "cde") == [6]
    assert candidate(s = "abacbabcabcab",p = "abc") == [1, 2, 3, 5, 6, 7, 8, 9, 10]
    assert candidate(s = "anananananananananananananananananananananana",p = "nana") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaab",p = "ba") == [26]
    assert candidate(s = "acbabcabcabcabcabcabcabcabcabcabc",p = "bac") == [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    assert candidate(s = "aaaaaaaaaaaab",p = "aaaab") == [8]
    assert candidate(s = "ldfldjflsdkflsdkjfldsjkfldsjfldsjflsdkjfldskjflds",p = "sdkjf") == [13, 19, 35, 41]
    assert candidate(s = "abababababababababab",p = "abab") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert candidate(s = "aabbccddeeffaabbccddeeff",p = "abcdef") == []
    assert candidate(s = "zzzzzzzzzz",p = "zzz") == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "zxyzzxyz",p = "xyz") == [0, 1, 4, 5]
    assert candidate(s = "thisisanexampleofaverylongstringwherefindinganagramsisnotthatstraightforward",p = "anagram") == [44]
    assert candidate(s = "anagramananagramananagram",p = "anagram") == [0, 1, 2, 3, 9, 10, 11, 12, 18]
    assert candidate(s = "anananananananananananananananananana",p = "anana") == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
    assert candidate(s = "abcdefghij",p = "jihgfedcba") == [0]
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",p = "aaaaaa") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",p = "mnopqr") == []
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",p = "mnbvcxzlkjhgfdsapoiuytrewq") == [0]
    assert candidate(s = "acbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacbacb",p = "acbac") == [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63]
    assert candidate(s = "hellohellohellohellohellohellohellohellohellohello",p = "world") == []
    assert candidate(s = "anagramanagramanagram",p = "nagaram") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",p = "mnbvcxzlkjhgfdsapoiuytrewq") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    assert candidate(s = "layer",p = "relay") == [0]
    assert candidate(s = "quickbrownfoxjumpsoverthelazydog",p = "thequickbrownfoxjumpsover") == [0]
    assert candidate(s = "llllllllllllllllllllllllllllllllllllll",p = "ll") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    assert candidate(s = "abababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",p = "aab") == [62]
    assert candidate(s = "qazwsxedcrfvtgbyhnujmikolp",p = "lopihgfytvremkluzxwqjncbv") == []
    assert candidate(s = "abacabadabacaba",p = "abacab") == [0, 1, 8, 9]
    assert candidate(s = "thisisaverylongstringwithseveralrepeatingcharacters",p = "characters") == [41]
    assert candidate(s = "aabbccddeeffgghhii",p = "iihhggffeeddccbbaa") == [0]
    assert candidate(s = "thisisanagram",p = "nagaram") == [6]
    assert candidate(s = "ababababababababababababababababababababababababababab",p = "baba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",p = "zyxwvutsrqponmlkjihgfedcba") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    assert candidate(s = "aabbccddeeff",p = "abcdef") == []


