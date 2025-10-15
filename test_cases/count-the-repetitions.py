def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "acb",n1 = 1,s2 = "acb",n2 = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "acb",n1 = 1,s2 = "acb",n2 = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaa",n1 = 3,s2 = "a",n2 = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaa",n1 = 3,s2 = "a",n2 = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabaacaabaab",n1 = 8,s2 = "aab",n2 = 1) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabaacaabaab",n1 = 8,s2 = "aab",n2 = 1) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "acb",n1 = 4,s2 = "ab",n2 = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "acb",n1 = 4,s2 = "ab",n2 = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",n1 = 2,s2 = "ace",n2 = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",n1 = 2,s2 = "ace",n2 = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "banana",n1 = 10,s2 = "nan",n2 = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "banana",n1 = 10,s2 = "nan",n2 = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",n1 = 5,s2 = "abc",n2 = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",n1 = 5,s2 = "abc",n2 = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",n1 = 5,s2 = "abcdef",n2 = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",n1 = 5,s2 = "abcdef",n2 = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzz",n1 = 1000,s2 = "zz",n2 = 100) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzz",n1 = 1000,s2 = "zz",n2 = 100) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",n1 = 1000,s2 = "abcabcabcabcabcabcabcabc",n2 = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",n1 = 1000,s2 = "abcabcabcabcabcabcabcabc",n2 = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",n1 = 500,s2 = "aceg",n2 = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",n1 = 500,s2 = "aceg",n2 = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccdd",n1 = 25,s2 = "abcdabcd",n2 = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccdd",n1 = 25,s2 = "abcdabcd",n2 = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",n1 = 20,s2 = "lohel",n2 = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",n1 = 20,s2 = "lohel",n2 = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "pqrs",n1 = 100,s2 = "rqpqsr",n2 = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "pqrs",n1 = 100,s2 = "rqpqsr",n2 = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",n1 = 100,s2 = "aceg",n2 = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",n1 = 100,s2 = "aceg",n2 = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzz",n1 = 1000000,s2 = "z",n2 = 1) == 5000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzz",n1 = 1000000,s2 = "z",n2 = 1) == 5000000: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",n1 = 100,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",n1 = 100,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zabzabczb",n1 = 10,s2 = "abc",n2 = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zabzabczb",n1 = 10,s2 = "abc",n2 = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyzxyz",n1 = 5,s2 = "xyz",n2 = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyzxyz",n1 = 5,s2 = "xyz",n2 = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 100,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 100,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",n1 = 100000,s2 = "dabc",n2 = 1000) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",n1 = 100000,s2 = "dabc",n2 = 1000) == 99: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",n1 = 20,s2 = "fedcba",n2 = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",n1 = 20,s2 = "fedcba",n2 = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyz",n1 = 3,s2 = "xyzxyzxyz",n2 = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyz",n1 = 3,s2 = "xyzxyzxyz",n2 = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hellohello",n1 = 10,s2 = "lohe",n2 = 1) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hellohello",n1 = 10,s2 = "lohe",n2 = 1) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefgh",n1 = 10,s2 = "aceg",n2 = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefgh",n1 = 10,s2 = "aceg",n2 = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyzxyz",n1 = 100,s2 = "xyzxyzxyz",n2 = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyzxyz",n1 = 100,s2 = "xyzxyzxyz",n2 = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",n1 = 50000,s2 = "xzy",n2 = 10000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",n1 = 50000,s2 = "xzy",n2 = 10000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",n1 = 15,s2 = "defabc",n2 = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",n1 = 15,s2 = "defabc",n2 = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabcabcabcabcabc",n1 = 10,s2 = "abcabcabcabcabcabcabcabc",n2 = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabcabcabcabcabc",n1 = 10,s2 = "abcabcabcabcabcabcabcabc",n2 = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "acb",n1 = 10,s2 = "acbacb",n2 = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "acb",n1 = 10,s2 = "acbacb",n2 = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefg",n1 = 10,s2 = "xyz",n2 = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefg",n1 = 10,s2 = "xyz",n2 = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababababab",n1 = 20,s2 = "abab",n2 = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababababab",n1 = 20,s2 = "abab",n2 = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabcabc",n1 = 999,s2 = "abab",n2 = 125) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabcabc",n1 = 999,s2 = "abab",n2 = 125) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaa",n1 = 10,s2 = "aa",n2 = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaa",n1 = 10,s2 = "aa",n2 = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",n1 = 100,s2 = "issi",n2 = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",n1 = 100,s2 = "issi",n2 = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgg",n1 = 20,s2 = "abcdefg",n2 = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgg",n1 = 20,s2 = "abcdefg",n2 = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzz",n1 = 1000,s2 = "zz",n2 = 100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzz",n1 = 1000,s2 = "zz",n2 = 100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertyuiop",n1 = 50,s2 = "qrp",n2 = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertyuiop",n1 = 50,s2 = "qrp",n2 = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzxyzxyz",n1 = 15,s2 = "zyxzyx",n2 = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzxyzxyz",n1 = 15,s2 = "zyxzyx",n2 = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",n1 = 500,s2 = "cab",n2 = 250) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",n1 = 500,s2 = "cab",n2 = 250) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",n1 = 5,s2 = "xz",n2 = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",n1 = 5,s2 = "xz",n2 = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabcabcabcabcabc",n1 = 10,s2 = "abc",n2 = 1) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabcabcabcabcabc",n1 = 10,s2 = "abc",n2 = 1) == 80: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",n1 = 1000000,s2 = "xyzz",n2 = 1000) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",n1 = 1000000,s2 = "xyzz",n2 = 1000) == 500: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "hello",n1 = 10,s2 = "heo",n2 = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "hello",n1 = 10,s2 = "heo",n2 = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",n1 = 12,s2 = "abcabc",n2 = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",n1 = 12,s2 = "abcabc",n2 = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadabacaba",n1 = 200,s2 = "abad",n2 = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadabacaba",n1 = 200,s2 = "abad",n2 = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyz",n1 = 10,s2 = "yxz",n2 = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyz",n1 = 10,s2 = "yxz",n2 = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabadaba",n1 = 1000,s2 = "abad",n2 = 250) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabadaba",n1 = 1000,s2 = "abad",n2 = 250) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababa",n1 = 10,s2 = "aba",n2 = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababa",n1 = 10,s2 = "aba",n2 = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",n1 = 50,s2 = "bd",n2 = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",n1 = 50,s2 = "bd",n2 = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcde",n1 = 1,s2 = "edcba",n2 = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcde",n1 = 1,s2 = "edcba",n2 = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zabzabczabc",n1 = 10,s2 = "abc",n2 = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zabzabczabc",n1 = 10,s2 = "abc",n2 = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaaab",n1 = 1000,s2 = "aab",n2 = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaaab",n1 = 1000,s2 = "aab",n2 = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",n1 = 6,s2 = "fed",n2 = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",n1 = 6,s2 = "fed",n2 = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",n1 = 10,s2 = "abc",n2 = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",n1 = 10,s2 = "abc",n2 = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababcabc",n1 = 10,s2 = "abc",n2 = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababcabc",n1 = 10,s2 = "abc",n2 = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaa",n1 = 1000000,s2 = "aa",n2 = 100000) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaa",n1 = 1000000,s2 = "aa",n2 = 100000) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdef",n1 = 999999,s2 = "fabcde",n2 = 100000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdef",n1 = 999999,s2 = "fabcde",n2 = 100000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaa",n1 = 100000,s2 = "aa",n2 = 10000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaa",n1 = 100000,s2 = "aa",n2 = 10000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abccbaabccba",n1 = 20,s2 = "abc",n2 = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abccbaabccba",n1 = 20,s2 = "abc",n2 = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababababababababababab",n1 = 100,s2 = "baba",n2 = 25) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababababababababababab",n1 = 100,s2 = "baba",n2 = 25) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aeiou",n1 = 10000,s2 = "aeiouaeiou",n2 = 500) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aeiou",n1 = 10000,s2 = "aeiouaeiou",n2 = 500) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",n1 = 3,s2 = "issi",n2 = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",n1 = 3,s2 = "issi",n2 = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",n1 = 3,s2 = "abcd",n2 = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",n1 = 3,s2 = "abcd",n2 = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "qwertyuiop",n1 = 50,s2 = "qo",n2 = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "qwertyuiop",n1 = 50,s2 = "qo",n2 = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 1000,s2 = "abcdefghijklmnopqrstuvwxyz",n2 = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 1000,s2 = "abcdefghijklmnopqrstuvwxyz",n2 = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcdabcd",n1 = 20,s2 = "abc",n2 = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcdabcd",n1 = 20,s2 = "abc",n2 = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",n1 = 100,s2 = "dabc",n2 = 50) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",n1 = 100,s2 = "dabc",n2 = 50) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababa",n1 = 1000,s2 = "aba",n2 = 10) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababa",n1 = 1000,s2 = "aba",n2 = 10) == 200: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "banana",n1 = 20,s2 = "ban",n2 = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "banana",n1 = 20,s2 = "ban",n2 = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzabc",n1 = 5,s2 = "cab",n2 = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzabc",n1 = 5,s2 = "cab",n2 = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaa",n1 = 500,s2 = "a",n2 = 100) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaa",n1 = 500,s2 = "a",n2 = 100) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxzyxyxyxy",n1 = 2,s2 = "xyz",n2 = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxzyxyxyxy",n1 = 2,s2 = "xyz",n2 = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",n1 = 1000000,s2 = "zzz",n2 = 100000) == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",n1 = 1000000,s2 = "zzz",n2 = 100000) == 113: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababab",n1 = 5,s2 = "ab",n2 = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababab",n1 = 5,s2 = "ab",n2 = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",n1 = 10,s2 = "abcdefghijklmnopqrstuvwxyz",n2 = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",n1 = 10,s2 = "abcdefghijklmnopqrstuvwxyz",n2 = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbcc",n1 = 3,s2 = "abc",n2 = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbcc",n1 = 3,s2 = "abc",n2 = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ababcabcabc",n1 = 6,s2 = "abcabc",n2 = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ababcabcabc",n1 = 6,s2 = "abcabc",n2 = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcd",n1 = 500,s2 = "abcd",n2 = 125) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcd",n1 = 500,s2 = "abcd",n2 = 125) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aabbccddeeff",n1 = 1000,s2 = "abcdef",n2 = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aabbccddeeff",n1 = 1000,s2 = "abcdef",n2 = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",n1 = 10,s2 = "abcabc",n2 = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",n1 = 10,s2 = "abcabc",n2 = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabbbbcccc",n1 = 10,s2 = "abccba",n2 = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabbbbcccc",n1 = 10,s2 = "abccba",n2 = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababab",n1 = 100,s2 = "aba",n2 = 15) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababab",n1 = 100,s2 = "aba",n2 = 15) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghij",n1 = 50,s2 = "adgj",n2 = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghij",n1 = 50,s2 = "adgj",n2 = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mississippi",n1 = 10,s2 = "issi",n2 = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mississippi",n1 = 10,s2 = "issi",n2 = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaa",n1 = 1000000,s2 = "aa",n2 = 100000) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaa",n1 = 1000000,s2 = "aa",n2 = 100000) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcd",n1 = 10000,s2 = "dcba",n2 = 1000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcd",n1 = 10000,s2 = "dcba",n2 = 1000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaaaaaa",n1 = 100000,s2 = "aa",n2 = 10000) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaaaaaa",n1 = 100000,s2 = "aa",n2 = 10000) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "ab",n1 = 1000000,s2 = "a",n2 = 500000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "ab",n1 = 1000000,s2 = "a",n2 = 500000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaaabaabaabaaaaaa",n1 = 5,s2 = "aab",n2 = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaaabaabaabaaaaaa",n1 = 5,s2 = "aab",n2 = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyzabc",n1 = 5,s2 = "xz",n2 = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyzabc",n1 = 5,s2 = "xz",n2 = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abababa",n1 = 7,s2 = "baab",n2 = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abababa",n1 = 7,s2 = "baab",n2 = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "banana",n1 = 10,s2 = "an",n2 = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "banana",n1 = 10,s2 = "an",n2 = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",n1 = 500,s2 = "bcab",n2 = 125) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",n1 = 500,s2 = "bcab",n2 = 125) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcd",n1 = 100,s2 = "cdab",n2 = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcd",n1 = 100,s2 = "cdab",n2 = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",n1 = 1000,s2 = "abcabc",n2 = 200) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",n1 = 1000,s2 = "abcabc",n2 = 200) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabc",n1 = 1000,s2 = "abc",n2 = 100) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabc",n1 = 1000,s2 = "abc",n2 = 100) == 30: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "aaa",n1 = 1000000,s2 = "a",n2 = 1) == 3000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "aaa",n1 = 1000000,s2 = "a",n2 = 1) == 3000000: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 10000,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 10000,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "zzzzzzzzzz",n1 = 1000,s2 = "z",n2 = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "zzzzzzzzzz",n1 = 1000,s2 = "z",n2 = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 1000,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 1000,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "mnopqrstuvwxyz",n1 = 10000,s2 = "mnop",n2 = 2000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "mnopqrstuvwxyz",n1 = 10000,s2 = "mnop",n2 = 2000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcdabcdabcdabcd",n1 = 500,s2 = "dcbadcbadcbadcba",n2 = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcdabcdabcdabcd",n1 = 500,s2 = "dcbadcbadcbadcba",n2 = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abcabcabcabc",n1 = 100,s2 = "abcabc",n2 = 5) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abcabcabcabc",n1 = 100,s2 = "abcabc",n2 = 5) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abab",n1 = 3,s2 = "ab",n2 = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abab",n1 = 3,s2 = "ab",n2 = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "abacabacabacabac",n1 = 1000,s2 = "acabacabacabacab",n2 = 250) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "abacabacabacabac",n1 = 1000,s2 = "acabacabacabacab",n2 = 250) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "baba",n1 = 20,s2 = "ab",n2 = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "baba",n1 = 20,s2 = "ab",n2 = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "babccbababcabbbabcbbabbbbabcbbb",n1 = 100,s2 = "babccbabab",n2 = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "babccbababcabbbabcbbabbbbabcbbb",n1 = 100,s2 = "babccbabab",n2 = 10) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "acb",n1 = 1,s2 = "acb",n2 = 1) == 1
    assert candidate(s1 = "aaa",n1 = 3,s2 = "a",n2 = 1) == 9
    assert candidate(s1 = "aabaacaabaab",n1 = 8,s2 = "aab",n2 = 1) == 24
    assert candidate(s1 = "acb",n1 = 4,s2 = "ab",n2 = 2) == 2
    assert candidate(s1 = "abcde",n1 = 2,s2 = "ace",n2 = 1) == 2
    assert candidate(s1 = "banana",n1 = 10,s2 = "nan",n2 = 1) == 10
    assert candidate(s1 = "abcdabcd",n1 = 5,s2 = "abc",n2 = 2) == 5
    assert candidate(s1 = "aabbccddeeff",n1 = 5,s2 = "abcdef",n2 = 1) == 5
    assert candidate(s1 = "zzzzzzzz",n1 = 1000,s2 = "zz",n2 = 100) == 40
    assert candidate(s1 = "aabbcc",n1 = 1000,s2 = "abcabcabcabcabcabcabcabc",n2 = 50) == 2
    assert candidate(s1 = "abcdefg",n1 = 500,s2 = "aceg",n2 = 100) == 5
    assert candidate(s1 = "aabbccdd",n1 = 25,s2 = "abcdabcd",n2 = 2) == 6
    assert candidate(s1 = "hello",n1 = 20,s2 = "lohel",n2 = 4) == 4
    assert candidate(s1 = "pqrs",n1 = 100,s2 = "rqpqsr",n2 = 5) == 5
    assert candidate(s1 = "abcdefg",n1 = 100,s2 = "aceg",n2 = 5) == 20
    assert candidate(s1 = "zzzzz",n1 = 1000000,s2 = "z",n2 = 1) == 5000000
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",n1 = 100,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 1) == 3
    assert candidate(s1 = "zabzabczb",n1 = 10,s2 = "abc",n2 = 2) == 5
    assert candidate(s1 = "xyzxyzxyz",n1 = 5,s2 = "xyz",n2 = 1) == 15
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 100,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 50) == 0
    assert candidate(s1 = "abcd",n1 = 100000,s2 = "dabc",n2 = 1000) == 99
    assert candidate(s1 = "abcdef",n1 = 20,s2 = "fedcba",n2 = 1) == 3
    assert candidate(s1 = "xyzxyz",n1 = 3,s2 = "xyzxyzxyz",n2 = 1) == 2
    assert candidate(s1 = "hellohello",n1 = 10,s2 = "lohe",n2 = 1) == 19
    assert candidate(s1 = "abcdefgh",n1 = 10,s2 = "aceg",n2 = 1) == 10
    assert candidate(s1 = "xyzxyzxyz",n1 = 100,s2 = "xyzxyzxyz",n2 = 20) == 5
    assert candidate(s1 = "xyz",n1 = 50000,s2 = "xzy",n2 = 10000) == 2
    assert candidate(s1 = "abcdef",n1 = 15,s2 = "defabc",n2 = 3) == 4
    assert candidate(s1 = "abcabcabcabcabcabcabcabc",n1 = 10,s2 = "abcabcabcabcabcabcabcabc",n2 = 1) == 10
    assert candidate(s1 = "acb",n1 = 10,s2 = "acbacb",n2 = 1) == 5
    assert candidate(s1 = "abcdefg",n1 = 10,s2 = "xyz",n2 = 1) == 0
    assert candidate(s1 = "ababababab",n1 = 20,s2 = "abab",n2 = 5) == 10
    assert candidate(s1 = "abcabcabcabcabc",n1 = 999,s2 = "abab",n2 = 125) == 19
    assert candidate(s1 = "aaa",n1 = 10,s2 = "aa",n2 = 2) == 7
    assert candidate(s1 = "mississippi",n1 = 100,s2 = "issi",n2 = 5) == 20
    assert candidate(s1 = "aabbccddeeffgg",n1 = 20,s2 = "abcdefg",n2 = 2) == 10
    assert candidate(s1 = "zzzzzzzzzz",n1 = 1000,s2 = "zz",n2 = 100) == 50
    assert candidate(s1 = "qwertyuiop",n1 = 50,s2 = "qrp",n2 = 10) == 5
    assert candidate(s1 = "xyzxyzxyz",n1 = 15,s2 = "zyxzyx",n2 = 1) == 11
    assert candidate(s1 = "abcabcabc",n1 = 500,s2 = "cab",n2 = 250) == 5
    assert candidate(s1 = "xyz",n1 = 5,s2 = "xz",n2 = 1) == 5
    assert candidate(s1 = "abcabcabcabcabcabcabcabc",n1 = 10,s2 = "abc",n2 = 1) == 80
    assert candidate(s1 = "xyz",n1 = 1000000,s2 = "xyzz",n2 = 1000) == 500
    assert candidate(s1 = "hello",n1 = 10,s2 = "heo",n2 = 1) == 10
    assert candidate(s1 = "abcabcabcabc",n1 = 12,s2 = "abcabc",n2 = 2) == 12
    assert candidate(s1 = "abacabadabacaba",n1 = 200,s2 = "abad",n2 = 10) == 20
    assert candidate(s1 = "xyz",n1 = 10,s2 = "yxz",n2 = 1) == 5
    assert candidate(s1 = "abacabadaba",n1 = 1000,s2 = "abad",n2 = 250) == 4
    assert candidate(s1 = "abababa",n1 = 10,s2 = "aba",n2 = 2) == 10
    assert candidate(s1 = "abcd",n1 = 50,s2 = "bd",n2 = 10) == 5
    assert candidate(s1 = "abcde",n1 = 1,s2 = "edcba",n2 = 1) == 0
    assert candidate(s1 = "zabzabczabc",n1 = 10,s2 = "abc",n2 = 3) == 6
    assert candidate(s1 = "aaaaaaab",n1 = 1000,s2 = "aab",n2 = 100) == 10
    assert candidate(s1 = "abcdef",n1 = 6,s2 = "fed",n2 = 1) == 2
    assert candidate(s1 = "aabbcc",n1 = 10,s2 = "abc",n2 = 2) == 5
    assert candidate(s1 = "ababcabc",n1 = 10,s2 = "abc",n2 = 2) == 10
    assert candidate(s1 = "aaaa",n1 = 1000000,s2 = "aa",n2 = 100000) == 20
    assert candidate(s1 = "abcdef",n1 = 999999,s2 = "fabcde",n2 = 100000) == 9
    assert candidate(s1 = "aaaaa",n1 = 100000,s2 = "aa",n2 = 10000) == 25
    assert candidate(s1 = "abccbaabccba",n1 = 20,s2 = "abc",n2 = 4) == 10
    assert candidate(s1 = "ababababababababababab",n1 = 100,s2 = "baba",n2 = 25) == 21
    assert candidate(s1 = "aeiou",n1 = 10000,s2 = "aeiouaeiou",n2 = 500) == 10
    assert candidate(s1 = "mississippi",n1 = 3,s2 = "issi",n2 = 1) == 3
    assert candidate(s1 = "abcdabcdabcd",n1 = 3,s2 = "abcd",n2 = 1) == 9
    assert candidate(s1 = "qwertyuiop",n1 = 50,s2 = "qo",n2 = 10) == 5
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 1000,s2 = "abcdefghijklmnopqrstuvwxyz",n2 = 10) == 100
    assert candidate(s1 = "abcdabcdabcdabcd",n1 = 20,s2 = "abc",n2 = 5) == 16
    assert candidate(s1 = "abcd",n1 = 100,s2 = "dabc",n2 = 50) == 1
    assert candidate(s1 = "abababa",n1 = 1000,s2 = "aba",n2 = 10) == 200
    assert candidate(s1 = "banana",n1 = 20,s2 = "ban",n2 = 5) == 4
    assert candidate(s1 = "xyzabc",n1 = 5,s2 = "cab",n2 = 2) == 2
    assert candidate(s1 = "aaa",n1 = 500,s2 = "a",n2 = 100) == 15
    assert candidate(s1 = "xyxzyxyxyxy",n1 = 2,s2 = "xyz",n2 = 1) == 2
    assert candidate(s1 = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",n1 = 1000000,s2 = "zzz",n2 = 100000) == 113
    assert candidate(s1 = "ababab",n1 = 5,s2 = "ab",n2 = 2) == 7
    assert candidate(s1 = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",n1 = 10,s2 = "abcdefghijklmnopqrstuvwxyz",n2 = 1) == 10
    assert candidate(s1 = "aabbcc",n1 = 3,s2 = "abc",n2 = 1) == 3
    assert candidate(s1 = "ababcabcabc",n1 = 6,s2 = "abcabc",n2 = 1) == 9
    assert candidate(s1 = "abcdabcdabcd",n1 = 500,s2 = "abcd",n2 = 125) == 12
    assert candidate(s1 = "aabbccddeeff",n1 = 1000,s2 = "abcdef",n2 = 10) == 100
    assert candidate(s1 = "abcabcabcabc",n1 = 10,s2 = "abcabc",n2 = 1) == 20
    assert candidate(s1 = "aaaabbbbcccc",n1 = 10,s2 = "abccba",n2 = 2) == 2
    assert candidate(s1 = "abababab",n1 = 100,s2 = "aba",n2 = 15) == 13
    assert candidate(s1 = "abcdefghij",n1 = 50,s2 = "adgj",n2 = 5) == 10
    assert candidate(s1 = "mississippi",n1 = 10,s2 = "issi",n2 = 1) == 10
    assert candidate(s1 = "aaaaaa",n1 = 1000000,s2 = "aa",n2 = 100000) == 30
    assert candidate(s1 = "abcd",n1 = 10000,s2 = "dcba",n2 = 1000) == 3
    assert candidate(s1 = "aaaaaaaa",n1 = 100000,s2 = "aa",n2 = 10000) == 40
    assert candidate(s1 = "ab",n1 = 1000000,s2 = "a",n2 = 500000) == 2
    assert candidate(s1 = "aaaabaabaabaaaaaa",n1 = 5,s2 = "aab",n2 = 1) == 15
    assert candidate(s1 = "xyzabc",n1 = 5,s2 = "xz",n2 = 1) == 5
    assert candidate(s1 = "abababa",n1 = 7,s2 = "baab",n2 = 1) == 7
    assert candidate(s1 = "banana",n1 = 10,s2 = "an",n2 = 2) == 10
    assert candidate(s1 = "abcabcabcabc",n1 = 500,s2 = "bcab",n2 = 125) == 8
    assert candidate(s1 = "abcdabcd",n1 = 100,s2 = "cdab",n2 = 10) == 19
    assert candidate(s1 = "abcabcabc",n1 = 1000,s2 = "abcabc",n2 = 200) == 7
    assert candidate(s1 = "abcabcabc",n1 = 1000,s2 = "abc",n2 = 100) == 30
    assert candidate(s1 = "aaa",n1 = 1000000,s2 = "a",n2 = 1) == 3000000
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 10000,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 5000) == 0
    assert candidate(s1 = "zzzzzzzzzz",n1 = 1000,s2 = "z",n2 = 100) == 100
    assert candidate(s1 = "abcdefghijklmnopqrstuvwxyz",n1 = 1000,s2 = "zyxwvutsrqponmlkjihgfedcba",n2 = 10) == 3
    assert candidate(s1 = "mnopqrstuvwxyz",n1 = 10000,s2 = "mnop",n2 = 2000) == 5
    assert candidate(s1 = "abcdabcdabcdabcd",n1 = 500,s2 = "dcbadcbadcbadcba",n2 = 100) == 1
    assert candidate(s1 = "abcabcabcabc",n1 = 100,s2 = "abcabc",n2 = 5) == 40
    assert candidate(s1 = "abab",n1 = 3,s2 = "ab",n2 = 2) == 3
    assert candidate(s1 = "abacabacabacabac",n1 = 1000,s2 = "acabacabacabacab",n2 = 250) == 3
    assert candidate(s1 = "baba",n1 = 20,s2 = "ab",n2 = 5) == 7
    assert candidate(s1 = "babccbababcabbbabcbbabbbbabcbbb",n1 = 100,s2 = "babccbabab",n2 = 10) == 10


