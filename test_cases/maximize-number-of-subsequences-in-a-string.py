def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(text = "bbbb",pattern = "bb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbb",pattern = "bb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaa",pattern = "aa") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaa",pattern = "aa") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzz",pattern = "zz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzz",pattern = "zz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "abdcdbc",pattern = "ac") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abdcdbc",pattern = "ac") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "abc",pattern = "ca") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abc",pattern = "ca") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "babab",pattern = "ba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "babab",pattern = "ba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzz",pattern = "zz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzz",pattern = "zz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabc",pattern = "aa") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabc",pattern = "aa") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "a",pattern = "ab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "a",pattern = "ab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "ab",pattern = "ba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ab",pattern = "ba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabb",pattern = "ab") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabb",pattern = "ab") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaa",pattern = "aa") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaa",pattern = "aa") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "b",pattern = "ab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "b",pattern = "ab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaa",pattern = "aa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaa",pattern = "aa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzxyz",pattern = "yx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzxyz",pattern = "yx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabc",pattern = "ac") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabc",pattern = "ac") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyz",pattern = "xz") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyz",pattern = "xz") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "",pattern = "ab") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "",pattern = "ab") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "",pattern = "xy") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "",pattern = "xy") == 0: {e}')
    
    total += 1
    try:
        result = candidate(text = "abxyabxyabxy",pattern = "bx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abxyabxyabxy",pattern = "bx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "zxyzxyzxyz",pattern = "yz") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zxyzxyzxyz",pattern = "yz") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzyzyzyzyzx",pattern = "yx") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzyzyzyzyzx",pattern = "yx") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzz",pattern = "zz") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzz",pattern = "zz") == 66: {e}')
    
    total += 1
    try:
        result = candidate(text = "pqrsrstq",pattern = "pq") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "pqrsrstq",pattern = "pq") == 4: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbabbaaa",pattern = "ba") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbabbaaa",pattern = "ba") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababababab",pattern = "ba") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababababab",pattern = "ba") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaabbbbb",pattern = "ab") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaabbbbb",pattern = "ab") == 30: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaabbbccc",pattern = "ac") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaabbbccc",pattern = "ac") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabacaba",pattern = "ac") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabacaba",pattern = "ac") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefabcdef",pattern = "cf") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefabcdef",pattern = "cf") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbaabb",pattern = "ba") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbaabb",pattern = "ba") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "bcbcbcbcbb",pattern = "bc") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bcbcbcbcbb",pattern = "bc") == 16: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbaabaabaabbb",pattern = "ab") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbaabaabaabbb",pattern = "ab") == 31: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbbbba",pattern = "ba") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbbba",pattern = "ba") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "acbacbacba",pattern = "ac") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "acbacbacba",pattern = "ac") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "mnopqr",pattern = "pq") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mnopqr",pattern = "pq") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyxzyxzyxzyx",pattern = "yx") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyxzyxzyxzyx",pattern = "yx") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzyzxzyzxzy",pattern = "yz") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzyzxzyzxzy",pattern = "yz") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyyxxyyxxyy",pattern = "yx") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyyxxyyxxyy",pattern = "yx") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccdd",pattern = "ac") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccdd",pattern = "ac") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdabcd",pattern = "ac") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdabcd",pattern = "ac") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "mississippi",pattern = "is") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mississippi",pattern = "is") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzz",pattern = "zz") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzz",pattern = "zz") == 55: {e}')
    
    total += 1
    try:
        result = candidate(text = "ababababab",pattern = "ab") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ababababab",pattern = "ab") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabbaabbaabbaabbaabbaabbaabb",pattern = "bb") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabbaabbaabbaabbaabbaabbaabb",pattern = "bb") == 136: {e}')
    
    total += 1
    try:
        result = candidate(text = "qwertyuiop",pattern = "qp") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "qwertyuiop",pattern = "qp") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaa",pattern = "aa") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaa",pattern = "aa") == 28: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdabcd",pattern = "da") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdabcd",pattern = "da") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzz",pattern = "zz") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzz",pattern = "zz") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababab",pattern = "ba") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababab",pattern = "ba") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "abababababa",pattern = "ab") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abababababa",pattern = "ab") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabc",pattern = "ac") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabc",pattern = "ac") == 14: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbbcc",pattern = "ac") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbbcc",pattern = "ac") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabbaabbaabbaabb",pattern = "aa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabbaabbaabbaabb",pattern = "aa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(text = "babcbabcba",pattern = "bc") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "babcbabcba",pattern = "bc") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeff",pattern = "bf") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeff",pattern = "bf") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabc",pattern = "ab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabc",pattern = "ab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "bcbcbcbcbc",pattern = "bc") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bcbcbcbcbc",pattern = "bc") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyxxyxyxyx",pattern = "yx") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyxxyxyxyx",pattern = "yx") == 17: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabcabc",pattern = "ca") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabcabc",pattern = "ca") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "xzyxzyxzyz",pattern = "zy") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xzyxzyxzyz",pattern = "zy") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzz",pattern = "zz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzz",pattern = "zz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbbaaabbbb",pattern = "ab") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbbaaabbbb",pattern = "ab") == 33: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaabbb",pattern = "ab") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaabbb",pattern = "ab") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "nnaaaannaa",pattern = "an") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "nnaaaannaa",pattern = "an") == 14: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyxyxyxyxy",pattern = "yx") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyxyxyxyxy",pattern = "yx") == 15: {e}')
    
    total += 1
    try:
        result = candidate(text = "cccccc",pattern = "cc") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "cccccc",pattern = "cc") == 21: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacaba",pattern = "ba") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacaba",pattern = "ba") == 24: {e}')
    
    total += 1
    try:
        result = candidate(text = "bababababababababa",pattern = "bb") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bababababababababa",pattern = "bb") == 45: {e}')
    
    total += 1
    try:
        result = candidate(text = "dcbabcdabcba",pattern = "ab") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "dcbabcdabcba",pattern = "ab") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzzyxzyxzyxzyx",pattern = "zy") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzzyxzyxzyxzyx",pattern = "zy") == 19: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaabbbb",pattern = "ab") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaabbbb",pattern = "ab") == 30: {e}')
    
    total += 1
    try:
        result = candidate(text = "cccccccc",pattern = "cc") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "cccccccc",pattern = "cc") == 36: {e}')
    
    total += 1
    try:
        result = candidate(text = "babcbacbab",pattern = "bc") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "babcbacbab",pattern = "bc") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghijklmnopqrstuvwxyz",pattern = "zy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghijklmnopqrstuvwxyz",pattern = "zy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzyyy",pattern = "yz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzyyy",pattern = "yz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",pattern = "zz") == 406
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",pattern = "zz") == 406: {e}')
    
    total += 1
    try:
        result = candidate(text = "mnopqrqpomn",pattern = "mn") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mnopqrqpomn",pattern = "mn") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabb",pattern = "bb") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabb",pattern = "bb") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgg",pattern = "ag") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgg",pattern = "ag") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "ccbaaa",pattern = "ab") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ccbaaa",pattern = "ab") == 3: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzzyxzyzxzyxzyx",pattern = "yz") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzzyxzyzxzyxzyx",pattern = "yz") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaaaa",pattern = "aa") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaaaa",pattern = "aa") == 45: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabb",pattern = "ab") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabb",pattern = "ab") == 16: {e}')
    
    total += 1
    try:
        result = candidate(text = "bababababababa",pattern = "ba") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bababababababa",pattern = "ba") == 35: {e}')
    
    total += 1
    try:
        result = candidate(text = "bababababa",pattern = "ba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bababababa",pattern = "ba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "zyxwvutsrqponmlkjihgfedcba",pattern = "yz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zyxwvutsrqponmlkjihgfedcba",pattern = "yz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "qqqqqqqqqq",pattern = "qp") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "qqqqqqqqqq",pattern = "qp") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "qwertyuiopasdfghjklzxcvbnm",pattern = "mn") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "qwertyuiopasdfghjklzxcvbnm",pattern = "mn") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcdabc",pattern = "bc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcdabc",pattern = "bc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzyyyy",pattern = "zy") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzyyyy",pattern = "zy") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pattern = "xz") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pattern = "xz") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabacab",pattern = "ac") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabacab",pattern = "ac") == 11: {e}')
    
    total += 1
    try:
        result = candidate(text = "fedcba",pattern = "ab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "fedcba",pattern = "ab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "ccccbbbaaa",pattern = "ba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ccccbbbaaa",pattern = "ba") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "mmnnnmmnnm",pattern = "mn") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mmnnnmmnnm",pattern = "mn") == 19: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabc",pattern = "ba") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabc",pattern = "ba") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzxyzxyzxyz",pattern = "yx") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzxyzxyzxyz",pattern = "yx") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "qqqqqppppp",pattern = "pq") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "qqqqqppppp",pattern = "pq") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb",pattern = "ba") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb",pattern = "ba") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "abbaba",pattern = "ab") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abbaba",pattern = "ab") == 7: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzzzzzzz",pattern = "zz") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzzzzzzz",pattern = "zz") == 91: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzyzxzyzxzyz",pattern = "yz") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzyzxzyzxzyz",pattern = "yz") == 16: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabb",pattern = "aa") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabb",pattern = "aa") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabcabcabc",pattern = "ab") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabcabcabc",pattern = "ab") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "babbabababababababa",pattern = "ba") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "babbabababababababa",pattern = "ba") == 63: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaabbbcccddd",pattern = "ad") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaabbbcccddd",pattern = "ad") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdef",pattern = "fe") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdef",pattern = "fe") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbbbbbbbbb",pattern = "bb") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbbbbbbbb",pattern = "bb") == 55: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbbbbaaaaa",pattern = "ab") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbbbaaaaa",pattern = "ab") == 5: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcde",pattern = "ae") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcde",pattern = "ae") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abracadabra",pattern = "ra") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abracadabra",pattern = "ra") == 10: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghij",pattern = "ae") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghij",pattern = "ae") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaabbbccc",pattern = "ab") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaabbbccc",pattern = "ab") == 12: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghij",pattern = "aj") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghij",pattern = "aj") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzzyxzyxzyxzyxzyxzyxzyx",pattern = "zx") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzzyxzyxzyxzyxzyxzyxzyx",pattern = "zx") == 43: {e}')
    
    total += 1
    try:
        result = candidate(text = "mmnmmnmmn",pattern = "mn") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "mmnmmnmmn",pattern = "mn") == 18: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeff",pattern = "ef") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeff",pattern = "ef") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "zzzzzzzz",pattern = "zz") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "zzzzzzzz",pattern = "zz") == 36: {e}')
    
    total += 1
    try:
        result = candidate(text = "ccccccc",pattern = "cc") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "ccccccc",pattern = "cc") == 28: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabc",pattern = "bc") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabc",pattern = "bc") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pattern = "az") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pattern = "az") == 6: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghij",pattern = "af") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghij",pattern = "af") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "bbbbbaaaaa",pattern = "ba") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "bbbbbaaaaa",pattern = "ba") == 30: {e}')
    
    total += 1
    try:
        result = candidate(text = "xyzyxzyxzy",pattern = "yx") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "xyzyxzyxzy",pattern = "yx") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabccbaa",pattern = "ac") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabccbaa",pattern = "ac") == 8: {e}')
    
    total += 1
    try:
        result = candidate(text = "abacabadabacaba",pattern = "ab") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abacabadabacaba",pattern = "ab") == 24: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabccccdddd",pattern = "cd") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabccccdddd",pattern = "cd") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaaaaa",pattern = "aa") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaaaaa",pattern = "aa") == 55: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaabbbb",pattern = "ab") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaabbbb",pattern = "ab") == 20: {e}')
    
    total += 1
    try:
        result = candidate(text = "aaaaaaaaaaaabbbbbbbbbbbb",pattern = "ab") == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aaaaaaaaaaaabbbbbbbbbbbb",pattern = "ab") == 156: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdefghijklnmopqrstuvwxyz",pattern = "az") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdefghijklnmopqrstuvwxyz",pattern = "az") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcd",pattern = "da") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcd",pattern = "da") == 1: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcdabcdabcd",pattern = "ad") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcdabcdabcd",pattern = "ad") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "lkjqwpmr",pattern = "qw") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "lkjqwpmr",pattern = "qw") == 2: {e}')
    
    total += 1
    try:
        result = candidate(text = "aabbaabbcc",pattern = "ab") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "aabbaabbcc",pattern = "ab") == 16: {e}')
    
    total += 1
    try:
        result = candidate(text = "abcabcabc",pattern = "ac") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "abcabcabc",pattern = "ac") == 9: {e}')
    
    total += 1
    try:
        result = candidate(text = "baabbaab",pattern = "ba") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "baabbaab",pattern = "ba") == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(text = "bbbb",pattern = "bb") == 10
    assert candidate(text = "aaaaa",pattern = "aa") == 15
    assert candidate(text = "zzzz",pattern = "zz") == 10
    assert candidate(text = "abdcdbc",pattern = "ac") == 4
    assert candidate(text = "abc",pattern = "ca") == 1
    assert candidate(text = "babab",pattern = "ba") == 6
    assert candidate(text = "zzz",pattern = "zz") == 6
    assert candidate(text = "abcabc",pattern = "aa") == 3
    assert candidate(text = "a",pattern = "ab") == 1
    assert candidate(text = "ab",pattern = "ba") == 1
    assert candidate(text = "aabb",pattern = "ab") == 6
    assert candidate(text = "aaa",pattern = "aa") == 6
    assert candidate(text = "b",pattern = "ab") == 1
    assert candidate(text = "aaaa",pattern = "aa") == 10
    assert candidate(text = "xyzxyz",pattern = "yx") == 3
    assert candidate(text = "abcabc",pattern = "ac") == 5
    assert candidate(text = "xyz",pattern = "xz") == 2
    assert candidate(text = "",pattern = "ab") == 0
    assert candidate(text = "",pattern = "xy") == 0
    assert candidate(text = "abxyabxyabxy",pattern = "bx") == 9
    assert candidate(text = "zxyzxyzxyz",pattern = "yz") == 10
    assert candidate(text = "xyzyzyzyzyzx",pattern = "yx") == 10
    assert candidate(text = "zzzzzzzzzzz",pattern = "zz") == 66
    assert candidate(text = "pqrsrstq",pattern = "pq") == 4
    assert candidate(text = "bbabbaaa",pattern = "ba") == 18
    assert candidate(text = "ababababab",pattern = "ba") == 15
    assert candidate(text = "aaaaabbbbb",pattern = "ab") == 30
    assert candidate(text = "aaabbbccc",pattern = "ac") == 12
    assert candidate(text = "abacabacaba",pattern = "ac") == 12
    assert candidate(text = "abcdefabcdef",pattern = "cf") == 5
    assert candidate(text = "bbaabb",pattern = "ba") == 8
    assert candidate(text = "bcbcbcbcbb",pattern = "bc") == 16
    assert candidate(text = "bbaabaabaabbb",pattern = "ab") == 31
    assert candidate(text = "bbbbba",pattern = "ba") == 10
    assert candidate(text = "acbacbacba",pattern = "ac") == 10
    assert candidate(text = "mnopqr",pattern = "pq") == 2
    assert candidate(text = "xyxzyxzyxzyx",pattern = "yx") == 15
    assert candidate(text = "zzyzxzyzxzy",pattern = "yz") == 12
    assert candidate(text = "xyyxxyyxxyy",pattern = "yx") == 18
    assert candidate(text = "aabbccdd",pattern = "ac") == 6
    assert candidate(text = "abcdabcdabcd",pattern = "ac") == 9
    assert candidate(text = "mississippi",pattern = "is") == 10
    assert candidate(text = "zzzzzzzzzz",pattern = "zz") == 55
    assert candidate(text = "ababababab",pattern = "ab") == 20
    assert candidate(text = "aabbaabbaabbaabbaabbaabbaabbaabb",pattern = "bb") == 136
    assert candidate(text = "qwertyuiop",pattern = "qp") == 2
    assert candidate(text = "aaaaaaa",pattern = "aa") == 28
    assert candidate(text = "abcdabcdabcd",pattern = "da") == 6
    assert candidate(text = "zzzzz",pattern = "zz") == 15
    assert candidate(text = "abababababab",pattern = "ba") == 21
    assert candidate(text = "abababababa",pattern = "ab") == 21
    assert candidate(text = "abcabcabcabc",pattern = "ac") == 14
    assert candidate(text = "aabbbcc",pattern = "ac") == 6
    assert candidate(text = "aabbaabbaabbaabbaabb",pattern = "aa") == 55
    assert candidate(text = "babcbabcba",pattern = "bc") == 11
    assert candidate(text = "aabbccddeeff",pattern = "bf") == 6
    assert candidate(text = "abcabcabc",pattern = "ab") == 9
    assert candidate(text = "bcbcbcbcbc",pattern = "bc") == 20
    assert candidate(text = "xyxxyxyxyx",pattern = "yx") == 17
    assert candidate(text = "abcabcabcabcabcabc",pattern = "ca") == 21
    assert candidate(text = "xzyxzyxzyz",pattern = "zy") == 10
    assert candidate(text = "zzzzzz",pattern = "zz") == 21
    assert candidate(text = "aabbbaaabbbb",pattern = "ab") == 33
    assert candidate(text = "aaabbb",pattern = "ab") == 12
    assert candidate(text = "nnaaaannaa",pattern = "an") == 14
    assert candidate(text = "xyxyxyxyxy",pattern = "yx") == 15
    assert candidate(text = "cccccc",pattern = "cc") == 21
    assert candidate(text = "abacabadabacaba",pattern = "ba") == 24
    assert candidate(text = "bababababababababa",pattern = "bb") == 45
    assert candidate(text = "dcbabcdabcba",pattern = "ab") == 9
    assert candidate(text = "xyzzyxzyxzyxzyx",pattern = "zy") == 19
    assert candidate(text = "aaaaaabbbb",pattern = "ab") == 30
    assert candidate(text = "cccccccc",pattern = "cc") == 36
    assert candidate(text = "babcbacbab",pattern = "bc") == 10
    assert candidate(text = "abcdefghijklmnopqrstuvwxyz",pattern = "zy") == 1
    assert candidate(text = "zzzyyy",pattern = "yz") == 3
    assert candidate(text = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",pattern = "zz") == 406
    assert candidate(text = "mnopqrqpomn",pattern = "mn") == 5
    assert candidate(text = "aabbaabb",pattern = "bb") == 10
    assert candidate(text = "aabbccddeeffgg",pattern = "ag") == 6
    assert candidate(text = "ccbaaa",pattern = "ab") == 3
    assert candidate(text = "xyzzyxzyzxzyxzyx",pattern = "yz") == 20
    assert candidate(text = "aaaaaaaaa",pattern = "aa") == 45
    assert candidate(text = "aabbaabb",pattern = "ab") == 16
    assert candidate(text = "bababababababa",pattern = "ba") == 35
    assert candidate(text = "bababababa",pattern = "ba") == 20
    assert candidate(text = "zyxwvutsrqponmlkjihgfedcba",pattern = "yz") == 1
    assert candidate(text = "qqqqqqqqqq",pattern = "qp") == 10
    assert candidate(text = "qwertyuiopasdfghjklzxcvbnm",pattern = "mn") == 1
    assert candidate(text = "abcabcdabc",pattern = "bc") == 9
    assert candidate(text = "zzzzyyyy",pattern = "zy") == 20
    assert candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pattern = "xz") == 6
    assert candidate(text = "abacabacab",pattern = "ac") == 11
    assert candidate(text = "fedcba",pattern = "ab") == 1
    assert candidate(text = "ccccbbbaaa",pattern = "ba") == 12
    assert candidate(text = "mmnnnmmnnm",pattern = "mn") == 19
    assert candidate(text = "abcabcabc",pattern = "ba") == 6
    assert candidate(text = "xyzxyzxyzxyz",pattern = "yx") == 10
    assert candidate(text = "qqqqqppppp",pattern = "pq") == 5
    assert candidate(text = "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb",pattern = "ba") == 20
    assert candidate(text = "abbaba",pattern = "ab") == 7
    assert candidate(text = "zzzzzzzzzzzzz",pattern = "zz") == 91
    assert candidate(text = "zzyzxzyzxzyz",pattern = "yz") == 16
    assert candidate(text = "aabbaabb",pattern = "aa") == 10
    assert candidate(text = "abcabcabcabcabc",pattern = "ab") == 20
    assert candidate(text = "babbabababababababa",pattern = "ba") == 63
    assert candidate(text = "aaabbbcccddd",pattern = "ad") == 12
    assert candidate(text = "abcdef",pattern = "fe") == 1
    assert candidate(text = "bbbbbbbbbb",pattern = "bb") == 55
    assert candidate(text = "bbbbbaaaaa",pattern = "ab") == 5
    assert candidate(text = "abcde",pattern = "ae") == 2
    assert candidate(text = "abracadabra",pattern = "ra") == 10
    assert candidate(text = "abcdefghij",pattern = "ae") == 2
    assert candidate(text = "aaabbbccc",pattern = "ab") == 12
    assert candidate(text = "abcdefghij",pattern = "aj") == 2
    assert candidate(text = "xyzzyxzyxzyxzyxzyxzyxzyx",pattern = "zx") == 43
    assert candidate(text = "mmnmmnmmn",pattern = "mn") == 18
    assert candidate(text = "aabbccddeeff",pattern = "ef") == 6
    assert candidate(text = "zzzzzzzz",pattern = "zz") == 36
    assert candidate(text = "ccccccc",pattern = "cc") == 28
    assert candidate(text = "abcabcabc",pattern = "bc") == 9
    assert candidate(text = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",pattern = "az") == 6
    assert candidate(text = "abcdefghij",pattern = "af") == 2
    assert candidate(text = "bbbbbaaaaa",pattern = "ba") == 30
    assert candidate(text = "xyzyxzyxzy",pattern = "yx") == 9
    assert candidate(text = "aabccbaa",pattern = "ac") == 8
    assert candidate(text = "abacabadabacaba",pattern = "ab") == 24
    assert candidate(text = "aabccccdddd",pattern = "cd") == 20
    assert candidate(text = "aaaaaaaaaa",pattern = "aa") == 55
    assert candidate(text = "aaaabbbb",pattern = "ab") == 20
    assert candidate(text = "aaaaaaaaaaaabbbbbbbbbbbb",pattern = "ab") == 156
    assert candidate(text = "abcdefghijklnmopqrstuvwxyz",pattern = "az") == 2
    assert candidate(text = "abcd",pattern = "da") == 1
    assert candidate(text = "abcdabcdabcd",pattern = "ad") == 9
    assert candidate(text = "lkjqwpmr",pattern = "qw") == 2
    assert candidate(text = "aabbaabbcc",pattern = "ab") == 16
    assert candidate(text = "abcabcabc",pattern = "ac") == 9
    assert candidate(text = "baabbaab",pattern = "ba") == 12


