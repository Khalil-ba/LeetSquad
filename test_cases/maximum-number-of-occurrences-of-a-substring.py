def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "aaaa",maxLetters = 1,minSize = 3,maxSize = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",maxLetters = 1,minSize = 3,maxSize = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",maxLetters = 3,minSize = 3,maxSize = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",maxLetters = 3,minSize = 3,maxSize = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 3,maxSize = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 3,maxSize = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba",maxLetters = 2,minSize = 2,maxSize = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba",maxLetters = 2,minSize = 2,maxSize = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabcabcabc",maxLetters = 2,minSize = 2,maxSize = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabcabcabc",maxLetters = 2,minSize = 2,maxSize = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyz",maxLetters = 3,minSize = 2,maxSize = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyz",maxLetters = 3,minSize = 2,maxSize = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",maxLetters = 3,minSize = 2,maxSize = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",maxLetters = 3,minSize = 2,maxSize = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 1,maxSize = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 1,maxSize = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",maxLetters = 3,minSize = 2,maxSize = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",maxLetters = 3,minSize = 2,maxSize = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",maxLetters = 5,minSize = 1,maxSize = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",maxLetters = 5,minSize = 1,maxSize = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",maxLetters = 2,minSize = 2,maxSize = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",maxLetters = 2,minSize = 2,maxSize = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadaba",maxLetters = 2,minSize = 2,maxSize = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadaba",maxLetters = 2,minSize = 2,maxSize = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababcaab",maxLetters = 2,minSize = 3,maxSize = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababcaab",maxLetters = 2,minSize = 3,maxSize = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",maxLetters = 3,minSize = 3,maxSize = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",maxLetters = 3,minSize = 3,maxSize = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopq",maxLetters = 5,minSize = 10,maxSize = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopq",maxLetters = 5,minSize = 10,maxSize = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisjustatest",maxLetters = 4,minSize = 4,maxSize = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisjustatest",maxLetters = 4,minSize = 4,maxSize = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef",maxLetters = 3,minSize = 5,maxSize = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef",maxLetters = 3,minSize = 5,maxSize = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 15,minSize = 7,maxSize = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 15,minSize = 7,maxSize = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef",maxLetters = 3,minSize = 3,maxSize = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef",maxLetters = 3,minSize = 3,maxSize = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 3,minSize = 3,maxSize = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 3,minSize = 3,maxSize = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzz",maxLetters = 3,minSize = 4,maxSize = 8) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzz",maxLetters = 3,minSize = 4,maxSize = 8) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",maxLetters = 2,minSize = 1,maxSize = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",maxLetters = 2,minSize = 1,maxSize = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg",maxLetters = 3,minSize = 2,maxSize = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg",maxLetters = 3,minSize = 2,maxSize = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxy",maxLetters = 2,minSize = 3,maxSize = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxy",maxLetters = 2,minSize = 3,maxSize = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopmnopmnop",maxLetters = 4,minSize = 5,maxSize = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopmnopmnop",maxLetters = 4,minSize = 5,maxSize = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",maxLetters = 2,minSize = 3,maxSize = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",maxLetters = 2,minSize = 3,maxSize = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",maxLetters = 5,minSize = 3,maxSize = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",maxLetters = 5,minSize = 3,maxSize = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 10,minSize = 5,maxSize = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 10,minSize = 5,maxSize = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiissi",maxLetters = 3,minSize = 2,maxSize = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiissi",maxLetters = 3,minSize = 2,maxSize = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",maxLetters = 2,minSize = 4,maxSize = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",maxLetters = 2,minSize = 4,maxSize = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",maxLetters = 10,minSize = 10,maxSize = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",maxLetters = 10,minSize = 10,maxSize = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeaabbccddeeaabb",maxLetters = 3,minSize = 4,maxSize = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeaabbccddeeaabb",maxLetters = 3,minSize = 4,maxSize = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuv",maxLetters = 10,minSize = 10,maxSize = 15) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuv",maxLetters = 10,minSize = 10,maxSize = 15) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacaba",maxLetters = 3,minSize = 5,maxSize = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacaba",maxLetters = 3,minSize = 5,maxSize = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",maxLetters = 2,minSize = 4,maxSize = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",maxLetters = 2,minSize = 4,maxSize = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacaba",maxLetters = 3,minSize = 3,maxSize = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacaba",maxLetters = 3,minSize = 3,maxSize = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",maxLetters = 1,minSize = 1,maxSize = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",maxLetters = 1,minSize = 1,maxSize = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 1,maxSize = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 1,maxSize = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrstuvwpqrstu",maxLetters = 7,minSize = 5,maxSize = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrstuvwpqrstu",maxLetters = 7,minSize = 5,maxSize = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 8,maxSize = 12) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 8,maxSize = 12) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 6,maxSize = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 6,maxSize = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 5,minSize = 5,maxSize = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 5,minSize = 5,maxSize = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra",maxLetters = 4,minSize = 5,maxSize = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra",maxLetters = 4,minSize = 5,maxSize = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",maxLetters = 6,minSize = 1,maxSize = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",maxLetters = 6,minSize = 1,maxSize = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",maxLetters = 2,minSize = 3,maxSize = 4) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",maxLetters = 2,minSize = 3,maxSize = 4) == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyz",maxLetters = 2,minSize = 3,maxSize = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyz",maxLetters = 2,minSize = 3,maxSize = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 4,maxSize = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 4,maxSize = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppppppppppppppppppppppppppppppppppppppp",maxLetters = 1,minSize = 50,maxSize = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppppppppppppppppppppppppppppppppppppp",maxLetters = 1,minSize = 50,maxSize = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab",maxLetters = 2,minSize = 4,maxSize = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab",maxLetters = 2,minSize = 4,maxSize = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 2,maxSize = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 2,maxSize = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 8) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 8) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff",maxLetters = 3,minSize = 6,maxSize = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff",maxLetters = 3,minSize = 6,maxSize = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 26,minSize = 1,maxSize = 26) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 26,minSize = 1,maxSize = 26) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 15,maxSize = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 15,maxSize = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyxzyxzyxzyxzyxzyxz",maxLetters = 3,minSize = 3,maxSize = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyxzyxzyxzyxzyxzyxz",maxLetters = 3,minSize = 3,maxSize = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 10,minSize = 10,maxSize = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 10,minSize = 10,maxSize = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",maxLetters = 4,minSize = 3,maxSize = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",maxLetters = 4,minSize = 3,maxSize = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "bananaananabanananaanananana",maxLetters = 3,minSize = 3,maxSize = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bananaananabanananaanananana",maxLetters = 3,minSize = 3,maxSize = 6) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",maxLetters = 1,minSize = 25000,maxSize = 25000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",maxLetters = 1,minSize = 25000,maxSize = 25000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatwilltestthelimits",maxLetters = 10,minSize = 5,maxSize = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatwilltestthelimits",maxLetters = 10,minSize = 5,maxSize = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyz",maxLetters = 3,minSize = 4,maxSize = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyz",maxLetters = 3,minSize = 4,maxSize = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",maxLetters = 5,minSize = 10,maxSize = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",maxLetters = 5,minSize = 10,maxSize = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababababababab",maxLetters = 2,minSize = 4,maxSize = 8) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababababababab",maxLetters = 2,minSize = 4,maxSize = 8) == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 1,maxSize = 26) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 1,maxSize = 26) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 6,maxSize = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 6,maxSize = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "tuvwxyzuvwxy",maxLetters = 10,minSize = 4,maxSize = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "tuvwxyzuvwxy",maxLetters = 10,minSize = 4,maxSize = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad",maxLetters = 4,minSize = 4,maxSize = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad",maxLetters = 4,minSize = 4,maxSize = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrsmnopqr",maxLetters = 7,minSize = 5,maxSize = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrsmnopqr",maxLetters = 7,minSize = 5,maxSize = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyxxxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",maxLetters = 2,minSize = 5,maxSize = 10) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyxxxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",maxLetters = 2,minSize = 5,maxSize = 10) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 3,maxSize = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 3,maxSize = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 54: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmn",maxLetters = 10,minSize = 5,maxSize = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmn",maxLetters = 10,minSize = 5,maxSize = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 6,maxSize = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 6,maxSize = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 3,maxSize = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 3,maxSize = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippiississippiississi",maxLetters = 4,minSize = 5,maxSize = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippiississippiississi",maxLetters = 4,minSize = 5,maxSize = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefabcdef",maxLetters = 6,minSize = 3,maxSize = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefabcdef",maxLetters = 6,minSize = 3,maxSize = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabra",maxLetters = 5,minSize = 5,maxSize = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabra",maxLetters = 5,minSize = 5,maxSize = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyx",maxLetters = 2,minSize = 1,maxSize = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyx",maxLetters = 2,minSize = 1,maxSize = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 10,minSize = 5,maxSize = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 10,minSize = 5,maxSize = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababababababababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababababababababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababab",maxLetters = 2,minSize = 4,maxSize = 8) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababab",maxLetters = 2,minSize = 4,maxSize = 8) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababab",maxLetters = 2,minSize = 2,maxSize = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababab",maxLetters = 2,minSize = 2,maxSize = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "llllllllllllll",maxLetters = 1,minSize = 6,maxSize = 8) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "llllllllllllll",maxLetters = 1,minSize = 6,maxSize = 8) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 10,maxSize = 20) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 10,maxSize = 20) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 3,maxSize = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 3,maxSize = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababab",maxLetters = 2,minSize = 2,maxSize = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababab",maxLetters = 2,minSize = 2,maxSize = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad",maxLetters = 4,minSize = 5,maxSize = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad",maxLetters = 4,minSize = 5,maxSize = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",maxLetters = 2,minSize = 4,maxSize = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",maxLetters = 2,minSize = 4,maxSize = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 10,maxSize = 15) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 10,maxSize = 15) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",maxLetters = 10,minSize = 5,maxSize = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",maxLetters = 10,minSize = 5,maxSize = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "pqrspqrspqrspqrs",maxLetters = 4,minSize = 5,maxSize = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pqrspqrspqrspqrs",maxLetters = 4,minSize = 5,maxSize = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 1,maxSize = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 1,maxSize = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",maxLetters = 10,minSize = 5,maxSize = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",maxLetters = 10,minSize = 5,maxSize = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 4,maxSize = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 4,maxSize = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeee",maxLetters = 2,minSize = 2,maxSize = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeee",maxLetters = 2,minSize = 2,maxSize = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 2,maxSize = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 2,maxSize = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 50000,maxSize = 50000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 50000,maxSize = 50000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababab",maxLetters = 2,minSize = 3,maxSize = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababab",maxLetters = 2,minSize = 3,maxSize = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 5,minSize = 10,maxSize = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 5,minSize = 10,maxSize = 15) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "aaaa",maxLetters = 1,minSize = 3,maxSize = 3) == 2
    assert candidate(s = "abacabadabacaba",maxLetters = 3,minSize = 3,maxSize = 5) == 4
    assert candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 3,maxSize = 3) == 3
    assert candidate(s = "abacaba",maxLetters = 2,minSize = 2,maxSize = 5) == 2
    assert candidate(s = "aabcabcabc",maxLetters = 2,minSize = 2,maxSize = 3) == 3
    assert candidate(s = "xyzxyz",maxLetters = 3,minSize = 2,maxSize = 4) == 2
    assert candidate(s = "abcde",maxLetters = 3,minSize = 2,maxSize = 3) == 1
    assert candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 1,maxSize = 2) == 3
    assert candidate(s = "abcde",maxLetters = 3,minSize = 2,maxSize = 4) == 1
    assert candidate(s = "abcde",maxLetters = 5,minSize = 1,maxSize = 5) == 1
    assert candidate(s = "abacabadabacaba",maxLetters = 2,minSize = 2,maxSize = 3) == 4
    assert candidate(s = "abacabadaba",maxLetters = 2,minSize = 2,maxSize = 3) == 3
    assert candidate(s = "aababcaab",maxLetters = 2,minSize = 3,maxSize = 4) == 2
    assert candidate(s = "abcabcabc",maxLetters = 3,minSize = 3,maxSize = 9) == 3
    assert candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopq",maxLetters = 5,minSize = 10,maxSize = 15) == 0
    assert candidate(s = "thisisjustatest",maxLetters = 4,minSize = 4,maxSize = 5) == 1
    assert candidate(s = "abababababababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 12
    assert candidate(s = "abcdefabcdefabcdef",maxLetters = 3,minSize = 5,maxSize = 6) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 15,minSize = 7,maxSize = 14) == 1
    assert candidate(s = "zzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 7) == 8
    assert candidate(s = "abcdefabcdefabcdef",maxLetters = 3,minSize = 3,maxSize = 3) == 3
    assert candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 9) == 4
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 3,minSize = 3,maxSize = 5) == 1
    assert candidate(s = "xyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzzxyzz",maxLetters = 3,minSize = 4,maxSize = 8) == 17
    assert candidate(s = "xyzxyzxyzxyz",maxLetters = 2,minSize = 1,maxSize = 3) == 4
    assert candidate(s = "abcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 6
    assert candidate(s = "aabbccddeeffgg",maxLetters = 3,minSize = 2,maxSize = 4) == 1
    assert candidate(s = "xyxyxyxyxyxyxy",maxLetters = 2,minSize = 3,maxSize = 6) == 6
    assert candidate(s = "mnopmnopmnop",maxLetters = 4,minSize = 5,maxSize = 7) == 2
    assert candidate(s = "abababababababab",maxLetters = 2,minSize = 3,maxSize = 6) == 7
    assert candidate(s = "abcdefghij",maxLetters = 5,minSize = 3,maxSize = 4) == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 10,minSize = 5,maxSize = 10) == 1
    assert candidate(s = "abcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 4) == 3
    assert candidate(s = "mississippiissi",maxLetters = 3,minSize = 2,maxSize = 5) == 3
    assert candidate(s = "abcdefgabcdefg",maxLetters = 2,minSize = 4,maxSize = 5) == 0
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",maxLetters = 10,minSize = 10,maxSize = 20) == 1
    assert candidate(s = "aabbccddeeaabbccddeeaabb",maxLetters = 3,minSize = 4,maxSize = 5) == 3
    assert candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuvmnopqrstuv",maxLetters = 10,minSize = 10,maxSize = 15) == 9
    assert candidate(s = "abacabadabacabadabacabadabacaba",maxLetters = 3,minSize = 5,maxSize = 7) == 4
    assert candidate(s = "abacabadabacaba",maxLetters = 2,minSize = 4,maxSize = 4) == 0
    assert candidate(s = "abacabadabacabadabacaba",maxLetters = 3,minSize = 3,maxSize = 7) == 6
    assert candidate(s = "abcabcabcabc",maxLetters = 1,minSize = 1,maxSize = 1) == 4
    assert candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 5) == 4
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 1,maxSize = 10) == 2
    assert candidate(s = "pqrstuvwpqrstu",maxLetters = 7,minSize = 5,maxSize = 8) == 2
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 8,maxSize = 12) == 13
    assert candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 6,maxSize = 6) == 3
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 8) == 8
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 5,minSize = 5,maxSize = 10) == 1
    assert candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 4) == 4
    assert candidate(s = "abracadabraabracadabra",maxLetters = 4,minSize = 5,maxSize = 7) == 2
    assert candidate(s = "mnopqr",maxLetters = 6,minSize = 1,maxSize = 6) == 1
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",maxLetters = 2,minSize = 3,maxSize = 4) == 18
    assert candidate(s = "xyzyzyzyzyz",maxLetters = 2,minSize = 3,maxSize = 4) == 4
    assert candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 4,maxSize = 6) == 3
    assert candidate(s = "pppppppppppppppppppppppppppppppppppppppppp",maxLetters = 1,minSize = 50,maxSize = 100) == 0
    assert candidate(s = "zzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 10
    assert candidate(s = "ababababababab",maxLetters = 2,minSize = 4,maxSize = 6) == 6
    assert candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 2,maxSize = 5) == 3
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 4,maxSize = 8) == 29
    assert candidate(s = "aabbccddeeffaabbccddeeffaabbccddeeff",maxLetters = 3,minSize = 6,maxSize = 12) == 3
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 26,minSize = 1,maxSize = 26) == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 15,maxSize = 20) == 1
    assert candidate(s = "xyxzyxzyxzyxzyxzyxzyxz",maxLetters = 3,minSize = 3,maxSize = 4) == 7
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 10,minSize = 10,maxSize = 20) == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 16
    assert candidate(s = "abcdabcdabcd",maxLetters = 4,minSize = 3,maxSize = 3) == 3
    assert candidate(s = "bananaananabanananaanananana",maxLetters = 3,minSize = 3,maxSize = 6) == 11
    assert candidate(s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",maxLetters = 1,minSize = 25000,maxSize = 25000) == 0
    assert candidate(s = "thisisaverylongstringthatwilltestthelimits",maxLetters = 10,minSize = 5,maxSize = 15) == 1
    assert candidate(s = "xyzxyzxyzxyz",maxLetters = 3,minSize = 4,maxSize = 6) == 3
    assert candidate(s = "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij",maxLetters = 5,minSize = 10,maxSize = 15) == 0
    assert candidate(s = "ababababababababababababababababababababababababababababababababababab",maxLetters = 2,minSize = 4,maxSize = 8) == 34
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 26,minSize = 1,maxSize = 26) == 2
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 31
    assert candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 6,maxSize = 12) == 3
    assert candidate(s = "tuvwxyzuvwxy",maxLetters = 10,minSize = 4,maxSize = 7) == 2
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad",maxLetters = 4,minSize = 4,maxSize = 8) == 8
    assert candidate(s = "mnopqrsmnopqr",maxLetters = 7,minSize = 5,maxSize = 8) == 2
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 6) == 10
    assert candidate(s = "xxyxxxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",maxLetters = 2,minSize = 5,maxSize = 10) == 13
    assert candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 3,maxSize = 5) == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 54
    assert candidate(s = "mnopqrstuvmnopqrstuvmnopqrstuvmn",maxLetters = 10,minSize = 5,maxSize = 15) == 3
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",maxLetters = 4,minSize = 6,maxSize = 8) == 7
    assert candidate(s = "abcdefabcdefabcdef",maxLetters = 6,minSize = 3,maxSize = 6) == 3
    assert candidate(s = "mississippiississippiississi",maxLetters = 4,minSize = 5,maxSize = 8) == 3
    assert candidate(s = "abcdefabcdef",maxLetters = 6,minSize = 3,maxSize = 6) == 2
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 20
    assert candidate(s = "abracadabraabracadabra",maxLetters = 5,minSize = 5,maxSize = 10) == 2
    assert candidate(s = "xyxxyxyxyx",maxLetters = 2,minSize = 1,maxSize = 3) == 6
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",maxLetters = 10,minSize = 5,maxSize = 8) == 1
    assert candidate(s = "ababababababababababababababababababababababababababababababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 35
    assert candidate(s = "ababababababababababababababab",maxLetters = 2,minSize = 4,maxSize = 8) == 14
    assert candidate(s = "abababababab",maxLetters = 2,minSize = 2,maxSize = 3) == 6
    assert candidate(s = "llllllllllllll",maxLetters = 1,minSize = 6,maxSize = 8) == 9
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 10,maxSize = 20) == 21
    assert candidate(s = "xyzxyzxyz",maxLetters = 3,minSize = 3,maxSize = 6) == 3
    assert candidate(s = "ababababababababababababababab",maxLetters = 2,minSize = 2,maxSize = 2) == 15
    assert candidate(s = "abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad",maxLetters = 4,minSize = 5,maxSize = 10) == 8
    assert candidate(s = "abababababababababab",maxLetters = 2,minSize = 4,maxSize = 6) == 9
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 10,maxSize = 15) == 11
    assert candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 3,maxSize = 4) == 4
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",maxLetters = 10,minSize = 5,maxSize = 10) == 1
    assert candidate(s = "abababababababab",maxLetters = 2,minSize = 2,maxSize = 4) == 8
    assert candidate(s = "pqrspqrspqrspqrs",maxLetters = 4,minSize = 5,maxSize = 8) == 3
    assert candidate(s = "abcabcabcabc",maxLetters = 3,minSize = 1,maxSize = 10) == 4
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm",maxLetters = 10,minSize = 5,maxSize = 10) == 2
    assert candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 4,maxSize = 6) == 1
    assert candidate(s = "aaabbbcccdddeee",maxLetters = 2,minSize = 2,maxSize = 3) == 2
    assert candidate(s = "abcabcabcabcabcabc",maxLetters = 3,minSize = 2,maxSize = 4) == 6
    assert candidate(s = "aabbccddeeff",maxLetters = 3,minSize = 2,maxSize = 6) == 1
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 10) == 22
    assert candidate(s = "zzzzzzzzzzzz",maxLetters = 1,minSize = 5,maxSize = 6) == 8
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzz",maxLetters = 1,minSize = 50000,maxSize = 50000) == 0
    assert candidate(s = "abababababababababababababab",maxLetters = 2,minSize = 3,maxSize = 5) == 13
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",maxLetters = 5,minSize = 10,maxSize = 15) == 0


