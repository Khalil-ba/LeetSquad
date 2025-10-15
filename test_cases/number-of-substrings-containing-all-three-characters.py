def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcba") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "cba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbaacb") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbaacb") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbacbac") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbacbac") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccbaab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccbaab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcbc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcbc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaacc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaacc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabc") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabc") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccbaaabb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccbaaabb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "baccab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baccab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "bca") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bca") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaacb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaacb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbaab") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbaab") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcababc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcababc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbccc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbccc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbac") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbac") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcacbacbacbabc") == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcacbacbacbabc") == 89: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcacabcabc") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcacabcabc") == 59: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccabababc") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccabababc") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbabacbabacbab") == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbabacbabacbab") == 112: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccbabcbacbac") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccbabcbacbac") == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabccba") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabccba") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccbaa") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccbaa") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbbccc") == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbbccc") == 27: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbacbacbacbacb") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbacbacbacbacb") == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacb") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacb") == 44: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcbacbacbabc") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcbacbacbabc") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcabcabcabcabc") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcabcabcabcabc") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccabcabcabc") == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccabcabcabc") == 115: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbabcababcabc") == 271
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbabcababcabc") == 271: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbacbacbacb") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbacbacbacb") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbabc") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbabc") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccbbbaaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccbbbaaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "caabcbacbacb") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "caabcbacbacb") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbcccaabbbabc") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbcccaabbbabc") == 59: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbcabc") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbcabc") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbbaaa") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbbaaa") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "bacbacbacbacb") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bacbacbacbacb") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "cabcbacbacbabcb") == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cabcbacbacbabcb") == 88: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbcacab") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbcacab") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbcccaaa") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbcccaaa") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbccc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbccc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccbbbaaabbbccc") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccbbbaaabbbccc") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 406
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 406: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcab") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcab") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaccabcabcabc") == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaccabcabcabc") == 104: {e}')
    
    total += 1
    try:
        result = candidate(s = "bacbacbacbacbacba") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bacbacbacbacbacba") == 120: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbbbaaaaa") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbbbaaaaa") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbcabcabcab") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbcabcabcab") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "cacbacbacbac") == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cacbacbacbac") == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "cabbacbac") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cabbacbac") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaacccbaab") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaacccbaab") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 136: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbacbacbacbac") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbacbacbacbac") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccaaaabbbccc") == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccaaaabbbccc") == 86: {e}')
    
    total += 1
    try:
        result = candidate(s = "bacbacbacbacba") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bacbacbacbacba") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacababaac") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacababaac") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcababccbaabc") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcababccbaabc") == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababcabcab") == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababcabcab") == 57: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbb") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbb") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcababc") == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcababc") == 117: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaab") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaab") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "baccabaccabacc") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "baccabaccabacc") == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbcacbacb") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbcacbacb") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccbbaaaabbbccc") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccbbaaaabbbccc") == 68: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbcccaabbcccaab") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbcccaabbcccaab") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccccaaaabbbbccc") == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccccaaaabbbbccc") == 103: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbacbacbacbacbacbacbacbacbacbacb") == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbacbacbacbacbacbacbacbacbacbacb") == 465: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabc") == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabc") == 58: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcbabacabc") == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcbabacabc") == 49: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbacbacbac") == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbacbacbac") == 75: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaccbbacbbacaacabcbacbacbacbac") == 498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaccbbacbbacaacabcbacbacbacbac") == 498: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbabacbabac") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbabacbabac") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccaabbbabc") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccaabbbabc") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbccccabbbccc") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbccccabbbccc") == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccaaaabbbcccbbb") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccaaaabbbcccbbb") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbbaaaabc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbbaaaabc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbacbacbacbacbacbacbacbacbacbac") == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbacbacbacbacbacbacbacbacbacbac") == 465: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbbccaaa") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbbccaaa") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccaabbbaaacc") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccaabbbaaacc") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccccabbaabbcbbb") == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccccabbaabbcbbb") == 100: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccbababac") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccbababac") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccabcabcabc") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccabcabcabc") == 60: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacbababcabc") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacbababcabc") == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbbaaabbbc") == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbbaaabbbc") == 87: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccabccabccabc") == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccabccabccabc") == 85: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbacbacbacbaca") == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbacbacbacbaca") == 103: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabacbacb") == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabacbacb") == 119: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccabcabcabc") == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccabcabcabc") == 103: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbcabcabc") == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbcabcabc") == 53: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaccaabbcc") == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaccaabbcc") == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabacbcab") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabacbcab") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaacccbbcabab") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaacccbbcabab") == 77: {e}')
    
    total += 1
    try:
        result = candidate(s = "babababacacacacbcbbcbcbcbacbacbacb") == 441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babababacacacacbcbbcbcbcbacbacbacb") == 441: {e}')
    
    total += 1
    try:
        result = candidate(s = "cacbacbacbacbacbac") == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cacbacbacbacbacbac") == 135: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccbbaaaabacbacb") == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccbbaaaabacbacb") == 78: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbbbaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbbbaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabcabcabcabcabc") == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabcabcabcabcabc") == 208: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccccaaa") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccccaaa") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbac") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbac") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbaccccba") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbaccccba") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccbaabccababab") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccbaabccababab") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbaabccc") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbaabccc") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "bacabcabcabcabcabcabcabc") == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bacabcabcabcabcabcabcabc") == 252: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccaaaabbbccc") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccaaaabbbccc") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == 496: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbabcc") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbabcc") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacb") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacb") == 77: {e}')
    
    total += 1
    try:
        result = candidate(s = "bacbacbacbacbacbacbac") == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bacbacbacbacbacbacbac") == 190: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 91: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaacccaaaabbccba") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaacccaaaabbccba") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccabc") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccabc") == 34: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aaabbbccc") == 9
    assert candidate(s = "abcba") == 5
    assert candidate(s = "cba") == 1
    assert candidate(s = "cbaacb") == 8
    assert candidate(s = "bbbacbac") == 18
    assert candidate(s = "ccccabc") == 9
    assert candidate(s = "abcabcabc") == 28
    assert candidate(s = "abcabcabcabc") == 55
    assert candidate(s = "aabbc") == 2
    assert candidate(s = "cccbaab") == 9
    assert candidate(s = "aabbbc") == 2
    assert candidate(s = "aabcbc") == 6
    assert candidate(s = "abcabc") == 10
    assert candidate(s = "aabbaacc") == 8
    assert candidate(s = "abacbc") == 8
    assert candidate(s = "abacabacabc") == 41
    assert candidate(s = "aaaabbbbcccc") == 16
    assert candidate(s = "ccbaaabb") == 10
    assert candidate(s = "baccab") == 7
    assert candidate(s = "bca") == 1
    assert candidate(s = "abc") == 1
    assert candidate(s = "ccccbaaa") == 12
    assert candidate(s = "aaacb") == 3
    assert candidate(s = "ccccbaab") == 12
    assert candidate(s = "abcababc") == 18
    assert candidate(s = "aabbcc") == 4
    assert candidate(s = "aaaabbbccc") == 12
    assert candidate(s = "abacbac") == 14
    assert candidate(s = "abcacbacbacbabc") == 89
    assert candidate(s = "aabbcacabcabc") == 59
    assert candidate(s = "ccabababc") == 17
    assert candidate(s = "abacbabacbabacbab") == 112
    assert candidate(s = "aabccbabcbacbac") == 85
    assert candidate(s = "abcabcabccba") == 52
    assert candidate(s = "aabbccbaa") == 18
    assert candidate(s = "aaabbbcccbbbccc") == 27
    assert candidate(s = "acbacbacbacbacb") == 91
    assert candidate(s = "abacbacbacb") == 44
    assert candidate(s = "aabcbacbacbabc") == 75
    assert candidate(s = "bcabcabcabcabc") == 78
    assert candidate(s = "aaabbbcccabcabcabc") == 115
    assert candidate(s = "abacbacbacbacbabcababcabc") == 271
    assert candidate(s = "acbacbacbacb") == 55
    assert candidate(s = "abacbacbacbabc") == 76
    assert candidate(s = "cccbbbaaa") == 9
    assert candidate(s = "caabcbacbacb") == 52
    assert candidate(s = "abbbcccaabbbabc") == 59
    assert candidate(s = "abacbcabc") == 26
    assert candidate(s = "aaabbbcccbbbaaa") == 45
    assert candidate(s = "bacbacbacbacb") == 66
    assert candidate(s = "cabcbacbacbabcb") == 88
    assert candidate(s = "abacbcacab") == 31
    assert candidate(s = "bbbbbbcccaaa") == 18
    assert candidate(s = "aaaaaaaaaabbbccc") == 30
    assert candidate(s = "ccbbbaaabbbccc") == 36
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 406
    assert candidate(s = "abcabcabcab") == 45
    assert candidate(s = "aabbaaccabcabcabc") == 104
    assert candidate(s = "bacbacbacbacbacba") == 120
    assert candidate(s = "ccccbbbaaaaa") == 20
    assert candidate(s = "abababababababab") == 0
    assert candidate(s = "abacbcabcabcab") == 76
    assert candidate(s = "abababababab") == 0
    assert candidate(s = "cacbacbacbac") == 54
    assert candidate(s = "cabbacbac") == 25
    assert candidate(s = "aabbaacccbaab") == 45
    assert candidate(s = "abcabcabcabcabcabc") == 136
    assert candidate(s = "cbacbacbacbac") == 66
    assert candidate(s = "aabbbcccaaaabbbccc") == 86
    assert candidate(s = "bacbacbacbacba") == 78
    assert candidate(s = "aabacababaac") == 40
    assert candidate(s = "abcababccbaabc") == 69
    assert candidate(s = "ababababcabcab") == 57
    assert candidate(s = "aaabbbcccbbb") == 18
    assert candidate(s = "abcabcabcabcababc") == 117
    assert candidate(s = "abccbaabccbaab") == 66
    assert candidate(s = "baccabaccabacc") == 69
    assert candidate(s = "abacbcacbacb") == 52
    assert candidate(s = "cccccbbaaaabbbccc") == 68
    assert candidate(s = "bbcccaabbcccaab") == 65
    assert candidate(s = "aabbbccccaaaabbbbccc") == 103
    assert candidate(s = "abababab") == 0
    assert candidate(s = "cbacbacbacbacbacbacbacbacbacbacb") == 465
    assert candidate(s = "abcbaabcbaabc") == 58
    assert candidate(s = "aabcbabacabc") == 49
    assert candidate(s = "aabacbacbacbac") == 75
    assert candidate(s = "aabbaaccbbacbbacaacabcbacbacbacbac") == 498
    assert candidate(s = "abacbabacbabac") == 71
    assert candidate(s = "aabbbcccaabbbabc") == 70
    assert candidate(s = "aaaabbccccabbbccc") == 85
    assert candidate(s = "cccaaaabbbcccbbb") == 51
    assert candidate(s = "ccccbbaaaabc") == 30
    assert candidate(s = "acbacbacbacbacbacbacbacbacbacbac") == 465
    assert candidate(s = "abcbbccaaa") == 20
    assert candidate(s = "cccaabbbaaacc") == 34
    assert candidate(s = "ccccccccabbaabbcbbb") == 100
    assert candidate(s = "cccbababac") == 23
    assert candidate(s = "ccccabcabcabc") == 60
    assert candidate(s = "aabacbababcabc") == 69
    assert candidate(s = "aaabbbcccbbbaaabbbc") == 87
    assert candidate(s = "abccabccabccabc") == 85
    assert candidate(s = "abcbacbacbacbaca") == 103
    assert candidate(s = "abcabcabcabacbacb") == 119
    assert candidate(s = "aabbbcccabcabcabc") == 103
    assert candidate(s = "abacbcabcabc") == 53
    assert candidate(s = "aabbaaccaabbcc") == 52
    assert candidate(s = "abcabcabacbcab") == 76
    assert candidate(s = "aabbbccc") == 6
    assert candidate(s = "aabbaacccbbcabab") == 77
    assert candidate(s = "babababacacacacbcbbcbcbcbacbacbacb") == 441
    assert candidate(s = "cacbacbacbacbacbac") == 135
    assert candidate(s = "cccbbaaaabacbacb") == 78
    assert candidate(s = "ccccbbbaaa") == 12
    assert candidate(s = "aaaaaaaaaabcabcabcabcabc") == 208
    assert candidate(s = "aabbbccccaaa") == 23
    assert candidate(s = "abacbacbac") == 35
    assert candidate(s = "aabbbaccccba") == 36
    assert candidate(s = "ccbaabccababab") == 62
    assert candidate(s = "ccccbaabccc") == 33
    assert candidate(s = "ccccbaa") == 8
    assert candidate(s = "bacabcabcabcabcabcabcabc") == 252
    assert candidate(s = "ccccccaaaabbbccc") == 48
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabc") == 496
    assert candidate(s = "abacbabcc") == 25
    assert candidate(s = "abacbacbacbacb") == 77
    assert candidate(s = "bacbacbacbacbacbacbac") == 190
    assert candidate(s = "abcabcabcabcabc") == 91
    assert candidate(s = "bbaacccaaaabbccba") == 76
    assert candidate(s = "aaaaabbbbbccccc") == 25
    assert candidate(s = "aaabbbcccabc") == 34


