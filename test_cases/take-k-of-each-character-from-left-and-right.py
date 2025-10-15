def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abacbacbacb",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacb",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "baccbaccbacc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baccbaccbacc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaacc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaacc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccbbaaaa",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccbbaaaa",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbcabc",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbcabc",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccc",k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccc",k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaacaabc",k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaacaabc",k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccc",k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccc",k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccaaaabbb",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccaaaabbb",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccbbbaaa",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccbbbaaa",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacb",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacb",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccaaabbcc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccaaabbcc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbac",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbac",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "baacababacbacbacbacbacb",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baacababacbacbacbacbacb",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababcabcabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababcabcabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababababa",k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababababa",k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbcccc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbcccc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbaaaaaccccaaaabbbbccccaaaa",k = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbaaaaaccccaaaabbbbccccaaaa",k = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbccccaa",k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbccccaa",k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbacbacbac",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbacbacbac",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabbbcccaabbcccaabbccc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabbbcccaabbcccaabbccc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccaaa",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccaaa",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 6) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 6) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbbbaaaa",k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbbbaaaa",k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbcccccc",k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbcccccc",k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccaaaabbbccc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccaaaabbbccc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabcba",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabcba",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbcccccccc",k = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbcccccccc",k = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbacbacbacbacb",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbacbacbacbacb",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccbbbaaa",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccbbbaaa",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccaaaabbcc",k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccaaaabbcc",k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbbcccccc",k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbbcccccc",k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "baccbaabccba",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baccbaabccba",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccc",k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccc",k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccaabbbbbb",k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccaabbbbbb",k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabac",k = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabac",k = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabaacaba",k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabaacaba",k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccbbbcccaaa",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccbbbcccaaa",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcbaabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcbaabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccbbbbaaa",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccbbbbaaa",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccc",k = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccc",k = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaabbbccc",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaabbbccc",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbbcccaaaccc",k = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbbcccaaaccc",k = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccbbbbaaa",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccbbbbaaa",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccabcabcabcabcabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccabcabcabcabcabcabc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaacaabc",k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaacaabc",k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccbaabccbaabccba",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccbaabccbaabccba",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbbccccaaa",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbbccccaaa",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccaaa",k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccaaa",k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbaaabbbcccaaa",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbaaabbbcccaaa",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbacbac",k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbacbac",k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabccbbccaa",k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabccbbccaa",k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "bacbacbacbacbac",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bacbacbacbacbac",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccaaabbb",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccaaabbb",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbbacaabcbab",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbbacaabcbab",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababcabcabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababcabcabcabc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababab",k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababab",k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccbaabacabcabcabcabcabcabcabcabcabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccbaabacabcabcabcabcabcabcabcabcabcabc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbacbacbacbacbac",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbacbacbacbacbac",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccc",k = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccc",k = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccbaaaaabbccc",k = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccbaaaaabbccc",k = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababababababababababababa",k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababababababababababababa",k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcccaabbcccaabbccc",k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcccaabbcccaabbccc",k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccababacabac",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccababacabac",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbcc",k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbcc",k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccbacababacba",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccbacababacba",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaabbbcccaabbcccaabbccc",k = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaabbbcccaabbcccaabbccc",k = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccbaaaabbbccc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccbaaaabbbccc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaaccaabbbb",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaaccaabbbb",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbac",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbac",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "caacbbacabcabc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "caacbbacabcabc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccbaaabbccbaaabbcc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccbaaabbccbaaabbcc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccbcccccccccc",k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccbcccccccccc",k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "cabcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cabcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcaabcbaabcbaabcba",k = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcaabcbaabcbaabcba",k = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccbbbaaaaaaacccccccbbbaaaaaa",k = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccbbbaaaaaaacccccccbbbaaaaaa",k = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcccccccccccba",k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcccccccccccba",k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc",k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc",k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbc",k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbc",k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "bacbacbacbacbacbacbacbacbacbacbacbac",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bacbacbacbacbacbacbacbacbacbacbacbac",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccccccccccc",k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccccccccccc",k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccddd",k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccddd",k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccbaabccbaabccba",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccbaabccbaabccba",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababab",k = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababab",k = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccaaaabbbb",k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccaaaabbbb",k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbbbbaaaaccccbbaaaccccbbaa",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbbbbaaaaccccbbaaaccccbbaa",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaacaabc",k = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaacaabc",k = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbbaaaaaaaccccccc",k = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbbaaaaaaaccccccc",k = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "cacacacacacaca",k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cacacacacacaca",k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbacccbaaa",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbacccbaaa",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbaaacccbbbaaacccbbbaaacccbbbaaaccc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbaaacccbbbaaacccbbbaaacccbbbaaaccc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaaacaabcbbbccc",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaaacaabcbbbccc",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccccbaa",k = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccccbaa",k = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc",k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc",k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabad",k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabad",k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbbbaaa",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbbbaaa",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaa",k = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaa",k = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabacabacabacabacabacabacabacabac",k = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabacabacabacabacabacabacabacabac",k = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcaaacbbacabcabc",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcaaacbbacabcabc",k = 4) == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abacbacbacb",k = 2) == 6
    assert candidate(s = "baccbaccbacc",k = 2) == 6
    assert candidate(s = "abcabcabcabcabc",k = 3) == 9
    assert candidate(s = "aabbaacc",k = 2) == 6
    assert candidate(s = "",k = 0) == 0
    assert candidate(s = "abc",k = 0) == 0
    assert candidate(s = "abcabcabcabcabcabc",k = 3) == 9
    assert candidate(s = "cccbbaaaa",k = 2) == 7
    assert candidate(s = "abacbcabc",k = 0) == 0
    assert candidate(s = "ccccccc",k = 2) == -1
    assert candidate(s = "aabbbccc",k = 2) == 6
    assert candidate(s = "aaaabbbbcccc",k = 4) == 12
    assert candidate(s = "aabaaaacaabc",k = 2) == 8
    assert candidate(s = "abcabcabc",k = 1) == 3
    assert candidate(s = "abcabcabc",k = 3) == 9
    assert candidate(s = "ccccccc",k = 3) == -1
    assert candidate(s = "a",k = 1) == -1
    assert candidate(s = "cccaaaabbb",k = 2) == 7
    assert candidate(s = "aabbcc",k = 1) == 4
    assert candidate(s = "aaabbbccc",k = 3) == 9
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 4) == 12
    assert candidate(s = "ccccccbbbaaa",k = 3) == 9
    assert candidate(s = "abacbacbacb",k = 3) == 9
    assert candidate(s = "aabbccaaabbcc",k = 2) == 6
    assert candidate(s = "abacbacbacbac",k = 2) == 6
    assert candidate(s = "baacababacbacbacbacbacb",k = 3) == 9
    assert candidate(s = "ababababababcabcabc",k = 3) == 9
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15
    assert candidate(s = "bababababababa",k = 5) == -1
    assert candidate(s = "aaaabbbbccccaaaabbbbccccaaaabbbbcccc",k = 4) == 12
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc",k = 4) == 12
    assert candidate(s = "bbbbbaaaaaccccaaaabbbbccccaaaa",k = 5) == 18
    assert candidate(s = "aabbbbccccaa",k = 2) == 8
    assert candidate(s = "abacabacabc",k = 2) == 6
    assert candidate(s = "aabacbacbacbac",k = 3) == 9
    assert candidate(s = "aabaaaabbbcccaabbcccaabbccc",k = 3) == 9
    assert candidate(s = "aabbbcccaaa",k = 3) == 9
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 6) == 18
    assert candidate(s = "ccccbbbaaaa",k = 3) == 10
    assert candidate(s = "bbbbbcccccc",k = 2) == -1
    assert candidate(s = "cccaaaabbbccc",k = 3) == 9
    assert candidate(s = "abcbaabcbaabcba",k = 2) == 6
    assert candidate(s = "aaaaaaaaaabbbbbbbbcccccccc",k = 4) == 16
    assert candidate(s = "abacbacbacbacbacbacbacbacb",k = 3) == 9
    assert candidate(s = "ccbbbaaa",k = 2) == 6
    assert candidate(s = "aabbccaaaabbcc",k = 3) == 10
    assert candidate(s = "abccbaabccba",k = 2) == 6
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbbcccccc",k = 5) == 16
    assert candidate(s = "baccbaabccba",k = 2) == 6
    assert candidate(s = "abcabcabcabcabcabcabc",k = 3) == 9
    assert candidate(s = "abcabcabcabcabc",k = 2) == 6
    assert candidate(s = "cccccccccccccccccc",k = 5) == -1
    assert candidate(s = "cccccccccccaabbbbbb",k = 3) == -1
    assert candidate(s = "abacabacabac",k = 3) == 11
    assert candidate(s = "abacabaacaba",k = 3) == -1
    assert candidate(s = "aabbbcccbbbcccaaa",k = 3) == 9
    assert candidate(s = "abcabcabcabcabcabcabcabcabc",k = 4) == 12
    assert candidate(s = "abccbaabcbaabc",k = 3) == 9
    assert candidate(s = "ccccccbbbbaaa",k = 2) == 7
    assert candidate(s = "aaaaabbbbbcccc",k = 1) == 6
    assert candidate(s = "aaaaaaabbbccc",k = 2) == 7
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 5) == 15
    assert candidate(s = "aaabbbcccbbbcccaaaccc",k = 4) == 14
    assert candidate(s = "cccbbbbaaa",k = 2) == 7
    assert candidate(s = "aabbccabcabcabcabcabcabc",k = 4) == 12
    assert candidate(s = "aabaaaacaabc",k = 5) == -1
    assert candidate(s = "aabccbaabccbaabccba",k = 3) == 9
    assert candidate(s = "bbbbbbbccccaaa",k = 2) == 7
    assert candidate(s = "aaabbbcccaaa",k = 2) == 8
    assert candidate(s = "bbbaaabbbcccaaa",k = 2) == 7
    assert candidate(s = "abcabcabcabcabcabcabcabc",k = 3) == 9
    assert candidate(s = "abacbacbacbacbacbac",k = 5) == 15
    assert candidate(s = "aabaaabccbbccaa",k = 3) == 10
    assert candidate(s = "bacbacbacbacbac",k = 4) == 12
    assert candidate(s = "ccccaaabbb",k = 2) == 7
    assert candidate(s = "acbbacaabcbab",k = 2) == 6
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",k = 3) == 9
    assert candidate(s = "abababababababababcabcabcabc",k = 4) == 12
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",k = 3) == -1
    assert candidate(s = "abababababababababababababababababababababababab",k = 5) == -1
    assert candidate(s = "ccbaabacabcabcabcabcabcabcabcabcabcabc",k = 4) == 12
    assert candidate(s = "acbacbacbacbacbac",k = 2) == 6
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",k = 10) == 30
    assert candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccc",k = 15) == -1
    assert candidate(s = "cccbaaaaabbccc",k = 3) == 11
    assert candidate(s = "aababababababababababababa",k = 2) == -1
    assert candidate(s = "aabbcccaabbcccaabbccc",k = 5) == 16
    assert candidate(s = "ccababacabac",k = 2) == 6
    assert candidate(s = "aabbaabbaabbaabbcc",k = 4) == -1
    assert candidate(s = "ccbacababacba",k = 4) == 12
    assert candidate(s = "aabaaaabbbcccaabbcccaabbccc",k = 4) == 14
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15
    assert candidate(s = "cccccccccbaaaabbbccc",k = 3) == 9
    assert candidate(s = "bbaaccaabbbb",k = 2) == 6
    assert candidate(s = "abacbacbacbacbac",k = 4) == 12
    assert candidate(s = "caacbbacabcabc",k = 2) == 6
    assert candidate(s = "aabbccbaaabbccbaaabbcc",k = 2) == 6
    assert candidate(s = "cccccccccccbcccccccccc",k = 3) == -1
    assert candidate(s = "aabbcc",k = 0) == 0
    assert candidate(s = "cabcabcabcabcabcabcabcabcabcabcabc",k = 5) == 15
    assert candidate(s = "aabcaabcbaabcbaabcba",k = 4) == 16
    assert candidate(s = "ccccccbbbaaaaaaacccccccbbbaaaaaa",k = 4) == 16
    assert candidate(s = "abacabadabacaba",k = 3) == -1
    assert candidate(s = "bcccccccccccba",k = 3) == -1
    assert candidate(s = "aaabbbccc",k = 0) == 0
    assert candidate(s = "bcbcbcbcbcbc",k = 2) == -1
    assert candidate(s = "abcabcabcabcabcabc",k = 2) == 6
    assert candidate(s = "bacbacbacbacbacbacbacbacbacbacbacbac",k = 4) == 12
    assert candidate(s = "cccccccccccccccccccccccccc",k = 10) == -1
    assert candidate(s = "aabbbcccddd",k = 1) == 7
    assert candidate(s = "ccbaabccbaabccba",k = 3) == 9
    assert candidate(s = "ababababababababababababababababababababababababab",k = 6) == -1
    assert candidate(s = "ccccccaaaabbbb",k = 2) == 8
    assert candidate(s = "ccccbbbbaaaaccccbbaaaccccbbaa",k = 4) == 12
    assert candidate(s = "aabaaaacaabc",k = 3) == -1
    assert candidate(s = "bbbbbbbaaaaaaaccccccc",k = 3) == 13
    assert candidate(s = "cacacacacacaca",k = 2) == -1
    assert candidate(s = "bbacccbaaa",k = 2) == 6
    assert candidate(s = "bbbaaacccbbbaaacccbbbaaacccbbbaaaccc",k = 3) == 9
    assert candidate(s = "aabaaaacaabcbbbccc",k = 3) == 9
    assert candidate(s = "abcabcabcabcabcabcabc",k = 4) == 12
    assert candidate(s = "aabccccbaa",k = 1) == 4
    assert candidate(s = "aaaaabbbbbccccc",k = 2) == 9
    assert candidate(s = "abacabadabacabadabacabad",k = 4) == -1
    assert candidate(s = "ccccbbbaaa",k = 2) == 7
    assert candidate(s = "aaaaaaaaaaa",k = 1) == -1
    assert candidate(s = "abacabacabacabacabacabacabacabacabacabac",k = 5) == 19
    assert candidate(s = "aabbcc",k = 2) == 6
    assert candidate(s = "aabcaaacbbacabcabc",k = 4) == 12


