def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abac") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abac") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccabba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccabba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababbaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababbaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cabaabac") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cabaabac") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccbbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccbbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcccbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcccbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaccaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaccaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abca") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abca") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababababababababababababababababababababababababababab") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababababababababababababababababababababababababababab") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabacccbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabacccbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabacabacabacabacabacabacabacabacab") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabacabacabacabacabacabacabacabacab") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccbbbbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccbbbbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 66: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccabbbcccabbbcccabbbcc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccabbbcccabbbcccabbbcc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccbaabccba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccbaabccba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "acabacabacabacabacabacabacabacab") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acabacabacabacabacabacabacabacab") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccaaaaabbb") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccaaaaabbb") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccaaaabbbbcccc") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccaaaabbbbcccc") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbbbbbbccccccaaa") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbbbbbbccccccaaa") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbabcbabcb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbabcbabcb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 76: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbaaaaa") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbaaaaa") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaaabaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaaabaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbccccc") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbccccc") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiii") == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiii") == 56: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcbaabccba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcbaabccba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabaacaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabaacaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabbaaaabaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabbaaaabaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaabacaabaca") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaabacaabaca") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccccdddeeeccccbbbaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccccdddeeeccccbbbaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbacba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbacba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabaaaabaaaabaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabaaaabaaaabaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccccbbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccccbbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccbaaab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccbaaab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffeeddccbaabbaaabcabcabc") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffeeddccbaabbaaabcabcabc") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccbbaaaabbbcccbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccbbaaaabbbcccbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiii") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiii") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbbbaaaaabbbaaaaabbbb") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbbbaaaaabbbaaaaabbbb") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccaaaaabbbcccbaaabccbaaabccbaaabccbaa") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccaaaaabbbcccbaaabccbaaabccbaaabccbaa") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbaaaaabbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbaaaaabbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbbbccccccdddddd") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbbbccccccdddddd") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabaaaabaaa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabaaaabaaa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccbbbaaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccbbbaaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd") == 41: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbacba") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbacba") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaaabba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaaabba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddccccdddd") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddccccdddd") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabc") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabc") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccabbbccbbbbcabcabbbccabc") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccabbbccbbbbcabcabbbccabc") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccccccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccccccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 99: {e}')
    
    total += 1
    try:
        result = candidate(s = "acaacacaacac") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acaacacaacac") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabcbaabcbaabcbaabcbaabcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabcbaabcbaabcbaabcbaabcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabccbaabccba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabccbaabccba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 71: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccccaaaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccccaaaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbccccdddddeeecccbbbbaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbccccdddddeeecccbbbbaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababbababbababb") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababbababbababb") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccdddeeeeeeccccbbbaa") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccdddeeeeeeccccbbbaa") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeedccbbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeedccbbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "acaacaaca") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acaacaaca") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 93: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaabbbaaabbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaabbbaaabbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "accbabcbaccbacc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "accbabcbaccbacc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccbbccbbccaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccbbccbbccaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbcccbbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbcccbbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "cbbccbbcc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cbbccbbcc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbacbacbac") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbacbacbac") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabccccbaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabccccbaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeee") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeee") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiii") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiii") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccaaaabbbbaaaa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccaaaabbbbaaaa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccddddddddddeeeeeeeeeeeeeeefffffffff") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccddddddddddeeeeeeeeeeeeeeefffffffff") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbbbaaabbbcccbbbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbbbaaabbbcccbbbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababab") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababab") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccccaaaabbbb") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccccaaaabbbb") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabbbaaabbbaaabbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabbbaaabbbaaabbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccddddddddddeeeeeeeeeeeeeeefffffffffgggggggggghhhhhhhhhhhiiiiiiiiiii") == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccddddddddddeeeeeeeeeeeeeeefffffffffgggggggggghhhhhhhhhhhiiiiiiiiiii") == 97: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddeeffeeddccbaabbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddeeffeeddccbaabbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabccccbbbbaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabccccbbbbaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbbccccbbbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbbccccbbbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeedccbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeedccbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaabaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaabaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeeedddccbaabb") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeeedddccbaabb") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabccccbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabccccbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "acccba") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acccba") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacbacbacbacbaba") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacbacbacbacbaba") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbaaabbbbaaaabbbaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbaaabbbbaaaabbbaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabac") == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabac") == 96: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 90: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbbaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbbaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 82: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccbaaaabbbcccbaaaabbbccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccbaaaabbbcccbaaaabbbccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddccbbbaa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddccbbbaa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbaaabbbaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbaaabbbaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabb") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabb") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccdddddccccbbbaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccdddddccccbbbaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababaababa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababaababa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbaabcbaabcba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbaabcbaabcba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaccbbbaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaccbbbaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeeecccccbbbaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeeecccccbbbaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeecccbbbaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeecccbbbaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccbaabcba") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccbaabcba") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddccccddddeeeeffff") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddccccddddeeeeffff") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 61: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccaaaabbbbcccc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccaaaabbbbcccc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeedccbbaaabbccddeedccbbaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeedccbbaaabbccddeedccbbaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "babbacabacababb") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "babbacabacababb") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccabbbbbbbcc") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccabbbbbbbcc") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccbbccbbccaa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccbbccbbccaa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccbaabbbcccbaaabbb") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccbaabbbcccbaaabbb") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "acaabaaaca") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acaabaaaca") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccbbccbbccbbccaa") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccbbccbbccbbccaa") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccbaaaabbbcccbaaaabbbccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccbaaaabbbcccbaaaabbbccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbcccdddeeecccbbbbaaaa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbcccdddeeecccbbbbaaaa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 72: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccccccbbbbbbaaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccccccbbbbbbaaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccabbaacc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccabbaacc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiii") == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiii") == 51: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeedccbbaaacccccccccccbbbbaaa") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeedccbbaaacccccccccccbbbbaaa") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "acbacbacbacbacba") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acbacbacbacbacba") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "caabaccaabaaccaaa") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "caabaccaabaaccaaa") == 17: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abcba") == 1
    assert candidate(s = "ca") == 2
    assert candidate(s = "abac") == 4
    assert candidate(s = "aabccabba") == 3
    assert candidate(s = "aabbaa") == 0
    assert candidate(s = "aaaaa") == 0
    assert candidate(s = "aababbaa") == 1
    assert candidate(s = "cabaabac") == 0
    assert candidate(s = "aabbccbaa") == 0
    assert candidate(s = "aaa") == 0
    assert candidate(s = "abcabc") == 6
    assert candidate(s = "aabbbcccbbaa") == 0
    assert candidate(s = "aababa") == 1
    assert candidate(s = "aabcccbaa") == 0
    assert candidate(s = "abc") == 3
    assert candidate(s = "abbaccaa") == 5
    assert candidate(s = "aaaa") == 0
    assert candidate(s = "abccba") == 0
    assert candidate(s = "aaabaaa") == 1
    assert candidate(s = "aabbcc") == 6
    assert candidate(s = "abca") == 2
    assert candidate(s = "cccccc") == 0
    assert candidate(s = "abababababababababababababababababababababababababababababababababababababab") == 76
    assert candidate(s = "aabacccbaa") == 4
    assert candidate(s = "abacabacabacabacabacabacabacabacabacabacab") == 42
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiii") == 36
    assert candidate(s = "aabbbcccbbbbaa") == 0
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 66
    assert candidate(s = "ccabbbcccabbbcccabbbcc") == 18
    assert candidate(s = "abccbaabccbaabccbaabccba") == 0
    assert candidate(s = "acabacabacabacabacabacabacabacab") == 32
    assert candidate(s = "cccaaaaabbb") == 11
    assert candidate(s = "aaaabbbbccccaaaabbbbcccc") == 24
    assert candidate(s = "aaabbbbbbbbccccccaaa") == 14
    assert candidate(s = "cbabcbabcb") == 10
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 76
    assert candidate(s = "bbbbbbaaaaa") == 11
    assert candidate(s = "abcabcabc") == 9
    assert candidate(s = "aaaabaaaabaaa") == 0
    assert candidate(s = "abcabcabcabc") == 12
    assert candidate(s = "aaaaaaaaaabbbbbbbbbccccc") == 24
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiii") == 56
    assert candidate(s = "abccbaabcbaabccba") == 1
    assert candidate(s = "abacabacabaacaba") == 1
    assert candidate(s = "aaabaaaabbaaaabaa") == 0
    assert candidate(s = "abacaabacaabaca") == 13
    assert candidate(s = "aabbbccccdddeeeccccbbbaaa") == 6
    assert candidate(s = "abacbacbacbacbacba") == 14
    assert candidate(s = "aaaabaaaabaaaabaaa") == 1
    assert candidate(s = "aabccccbbaa") == 0
    assert candidate(s = "aaaabbbbcccc") == 12
    assert candidate(s = "aabccbaaab") == 10
    assert candidate(s = "aaabbbcccbbbbaaa") == 0
    assert candidate(s = "aabbccddeeffeeddccbaabbaaabcabcabc") == 34
    assert candidate(s = "aabbbcccbbaaaabbbcccbbaaa") == 0
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiii") == 41
    assert candidate(s = "abbbbaaaaabbbaaaaabbbb") == 22
    assert candidate(s = "cccaaaaabbbcccbaaabccbaaabccbaaabccbaa") == 38
    assert candidate(s = "bbbbaaaaabbbb") == 0
    assert candidate(s = "abccbaabccba") == 0
    assert candidate(s = "aaabaaaabbbaaa") == 0
    assert candidate(s = "aaaabbbbbbccccccdddddd") == 22
    assert candidate(s = "abacabacaba") == 1
    assert candidate(s = "aaabaaaabaaaabaaa") == 1
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabba") == 0
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabc") == 36
    assert candidate(s = "abacaba") == 1
    assert candidate(s = "cccbbbaaa") == 9
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccdddddddddd") == 41
    assert candidate(s = "abcbaabcbacba") == 7
    assert candidate(s = "aaabaaaabba") == 0
    assert candidate(s = "aabbaabbaabbaabb") == 16
    assert candidate(s = "aaaabbbbccccddddccccdddd") == 24
    assert candidate(s = "abcabcabcabcabcabcabc") == 21
    assert candidate(s = "ccabbbccbbbbcabcabbbccabc") == 22
    assert candidate(s = "cccccccccccccccccccccc") == 0
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 99
    assert candidate(s = "acaacacaacac") == 12
    assert candidate(s = "aaabbbcccbbbaaa") == 0
    assert candidate(s = "abcbaabcbaabcbaabcbaabcbaabcbaabcba") == 1
    assert candidate(s = "abccbaabccbaabccba") == 0
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 71
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc") == 30
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabb") == 32
    assert candidate(s = "aaaaabbbbbcccccaaaa") == 10
    assert candidate(s = "aabbbccccdddddeeecccbbbbaaa") == 8
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 48
    assert candidate(s = "ababbababbababb") == 15
    assert candidate(s = "aabbbcccdddeeeeeeccccbbbaa") == 9
    assert candidate(s = "aabbccddeedccbbaa") == 0
    assert candidate(s = "aabbbcccbaa") == 0
    assert candidate(s = "acaacaaca") == 1
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 93
    assert candidate(s = "aabbaaabbbaaabbbaaabbaa") == 0
    assert candidate(s = "accbabcbaccbacc") == 15
    assert candidate(s = "abcabcabcabcabcabc") == 18
    assert candidate(s = "abcbaabcba") == 0
    assert candidate(s = "aabbccbbccbbccaa") == 12
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(s = "aaaabbbcccbbbaaa") == 0
    assert candidate(s = "cbbccbbcc") == 0
    assert candidate(s = "abacbacbacbacbacbacbac") == 22
    assert candidate(s = "aaaaabccccbaaaa") == 0
    assert candidate(s = "aaaabbbbccccddddeee") == 19
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiii") == 45
    assert candidate(s = "ccccaaaabbbbaaaa") == 16
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccddddddddddeeeeeeeeeeeeeeefffffffff") == 65
    assert candidate(s = "aaabbbcccbbbbaaabbbcccbbbbaaa") == 0
    assert candidate(s = "ababababababababababab") == 22
    assert candidate(s = "aaaabbbbccccccaaaabbbb") == 22
    assert candidate(s = "aabbaaabbbaaabbbaaabbaaa") == 0
    assert candidate(s = "aaaaaaaaaabbbbbbbbbbbccccccccccddddddddddeeeeeeeeeeeeeeefffffffffgggggggggghhhhhhhhhhhiiiiiiiiiii") == 97
    assert candidate(s = "aabbaabbccddeeffeeddccbaabbaa") == 0
    assert candidate(s = "abababababababababab") == 20
    assert candidate(s = "aaaabccccbbbbaaaa") == 0
    assert candidate(s = "aabbbbccccbbbbaaa") == 0
    assert candidate(s = "aabbccddeedccbbaaa") == 0
    assert candidate(s = "abacabadabacaba") == 1
    assert candidate(s = "aabaaabaaa") == 0
    assert candidate(s = "aabbccddeeeedddccbaabb") == 22
    assert candidate(s = "aabccccbaa") == 0
    assert candidate(s = "acccba") == 4
    assert candidate(s = "abacbacbacbacbaba") == 11
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 42
    assert candidate(s = "aaaabbbaaabbbbaaaabbbaaaa") == 0
    assert candidate(s = "abacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabacabac") == 96
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc") == 90
    assert candidate(s = "aaabbbcccbbaaa") == 0
    assert candidate(s = "aabbccddeeffgg") == 14
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 82
    assert candidate(s = "ccbaaaabbbcccbaaaabbbccc") == 0
    assert candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 0
    assert candidate(s = "aabbaabbccddccbbbaa") == 10
    assert candidate(s = "cccccccccccccccccc") == 0
    assert candidate(s = "aaaabbaaabbbaaaa") == 0
    assert candidate(s = "aabbaabbaabbaabbaabb") == 20
    assert candidate(s = "aaaaabbbbbccccdddddccccbbbaaaaa") == 0
    assert candidate(s = "ababaababa") == 0
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaa") == 0
    assert candidate(s = "abcbaabcbaabcba") == 1
    assert candidate(s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb") == 0
    assert candidate(s = "aabbaaccbbbaa") == 4
    assert candidate(s = "ccccccc") == 0
    assert candidate(s = "aaabbbcccdddeeecccccbbbaaa") == 6
    assert candidate(s = "aabbccddeeecccbbbaa") == 5
    assert candidate(s = "abccbaabcba") == 0
    assert candidate(s = "ababababab") == 10
    assert candidate(s = "aaaabbbbccccddddccccddddeeeeffff") == 32
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiii") == 61
    assert candidate(s = "ccccaaaabbbbcccc") == 8
    assert candidate(s = "aabbccddeedccbbaaabbccddeedccbbaa") == 0
    assert candidate(s = "babbacabacababb") == 1
    assert candidate(s = "ccccccabbbbbbbcc") == 8
    assert candidate(s = "abcabcabcabcabcabcabcabc") == 24
    assert candidate(s = "aabbaabbccbbccbbccaa") == 16
    assert candidate(s = "aaabbbcccbaabbbcccbaaabbb") == 25
    assert candidate(s = "ababa") == 1
    assert candidate(s = "acaabaaaca") == 1
    assert candidate(s = "aabbccbbccbbccbbccaa") == 16
    assert candidate(s = "ccccbaaaabbbcccbaaaabbbccc") == 0
    assert candidate(s = "aaaabbbcccdddeeecccbbbbaaaa") == 6
    assert candidate(s = "aaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 72
    assert candidate(s = "aaaaabbbbbccccccccbbbbbbaaaaa") == 0
    assert candidate(s = "ccabbaacc") == 0
    assert candidate(s = "aaaabbbbccccddddeeeeffffgggghhhhiiiiiiiiiiiiiiiiiii") == 51
    assert candidate(s = "aabbccddeedccbbaaacccccccccccbbbbaaa") == 12
    assert candidate(s = "acbacbacbacbacba") == 14
    assert candidate(s = "abcabcabcabcabc") == 15
    assert candidate(s = "ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") == 0
    assert candidate(s = "caabaccaabaaccaaa") == 17


