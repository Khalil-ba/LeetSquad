def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "a",t = "b",maxCost = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "b",maxCost = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "a",maxCost = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "a",maxCost = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "krrgw",t = "grkwa",maxCost = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "krrgw",t = "grkwa",maxCost = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "abce",maxCost = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "abce",maxCost = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",t = "efghabcd",maxCost = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",t = "efghabcd",maxCost = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "krrgw",t = "zjxss",maxCost = 19) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "krrgw",t = "zjxss",maxCost = 19) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz",t = "bbbbb",maxCost = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz",t = "bbbbb",maxCost = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "cdef",maxCost = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "cdef",maxCost = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 26) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 26) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "pxezla",t = "sllerr",maxCost = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pxezla",t = "sllerr",maxCost = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "bcdef",maxCost = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "bcdef",maxCost = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "b",maxCost = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "b",maxCost = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "abcd",maxCost = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "abcd",maxCost = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 25) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 25) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",t = "dddddddddddd",maxCost = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",t = "dddddddddddd",maxCost = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "bcdf",maxCost = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "bcdf",maxCost = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "fghij",maxCost = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "fghij",maxCost = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "acde",maxCost = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "acde",maxCost = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",t = "aaaaaaaaaa",maxCost = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",t = "aaaaaaaaaa",maxCost = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc",t = "bbbbbccccdaaaaa",maxCost = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc",t = "bbbbbccccdaaaaa",maxCost = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",t = "z",maxCost = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",t = "z",maxCost = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstring",t = "thisisaverylongstring",maxCost = 50) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstring",t = "thisisaverylongstring",maxCost = 50) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",t = "fghij",maxCost = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",t = "fghij",maxCost = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzz",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaa",maxCost = 130) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzz",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaa",maxCost = 130) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",t = "abracadabra",maxCost = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",t = "abracadabra",maxCost = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaa",maxCost = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaa",maxCost = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophone",t = "pneumonia",maxCost = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophone",t = "pneumonia",maxCost = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabb",t = "bbaabbaabbab",maxCost = 20) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabb",t = "bbaabbaabbab",maxCost = 20) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosis",maxCost = 0) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosis",maxCost = 0) == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghij",maxCost = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghij",maxCost = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringthatweneedtocompare",t = "thisisaverylongstringthatweneedtoreplace",maxCost = 50) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringthatweneedtocompare",t = "thisisaverylongstringthatweneedtoreplace",maxCost = 50) == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzz",t = "zzyx",maxCost = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzz",t = "zzyx",maxCost = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",t = "dddddddddddddddddddddddddddddddd",maxCost = 200) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",t = "dddddddddddddddddddddddddddddddd",maxCost = 200) == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababab",t = "bababababababa",maxCost = 12) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababab",t = "bababababababa",maxCost = 12) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqr",t = "qrstuv",maxCost = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqr",t = "qrstuv",maxCost = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",t = "xyzxyzxyzxyzxyzxyzx",maxCost = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",t = "xyzxyzxyzxyzxyzxyzx",maxCost = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyz",maxCost = 0) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyz",maxCost = 0) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",maxCost = 1300) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",maxCost = 1300) == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",t = "ccccbbbbaaaa",maxCost = 16) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",t = "ccccbbbbaaaa",maxCost = 16) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",t = "bababababa",maxCost = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",t = "bababababa",maxCost = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",t = "abcabcabcabcabc",maxCost = 0) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",t = "abcabcabcabcabc",maxCost = 0) == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa",maxCost = 52) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa",maxCost = 52) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababababababab",t = "bababababababababababababababababababababababababa",maxCost = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababababababab",t = "bababababababababababababababababababababababababa",maxCost = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",t = "abababababa",maxCost = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",t = "abababababa",maxCost = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghja",maxCost = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghja",maxCost = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghkj",maxCost = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghkj",maxCost = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "acabababcababcaba",t = "bacbababcababcaba",maxCost = 25) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "acabababcababcaba",t = "bacbababcababcaba",maxCost = 25) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "oneonetwoonetwo",t = "twoonetwoonetwo",maxCost = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "oneonetwoonetwo",t = "twoonetwoonetwo",maxCost = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 200) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 200) == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzx",maxCost = 50) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzx",maxCost = 50) == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",maxCost = 0) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",maxCost = 0) == 52: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba",maxCost = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba",maxCost = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcd",t = "dddddddddddddddddddd",maxCost = 15) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcd",t = "dddddddddddddddddddd",maxCost = 15) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcdefghijklmnopqrstuvwxyza",maxCost = 51) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcdefghijklmnopqrstuvwxyza",maxCost = 51) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisateststring",t = "jajajajajajajajaj",maxCost = 50) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisateststring",t = "jajajajajajajajaj",maxCost = 50) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",maxCost = 100) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",maxCost = 100) == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",maxCost = 200) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",maxCost = 200) == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",t = "ccccbbbbaaaaffff",maxCost = 15) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",t = "ccccbbbbaaaaffff",maxCost = 15) == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghij",maxCost = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghij",maxCost = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 250) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 250) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabc",t = "bcbcbcbcbcbcbcbcbcbcbcbcbcbc",maxCost = 30) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabc",t = "bcbcbcbcbcbcbcbcbcbcbcbcbcbc",maxCost = 30) == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "bbbbbbbbbbbbbbbbbbbbbbbbbb",maxCost = 100) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "bbbbbbbbbbbbbbbbbbbbbbbbbb",maxCost = 100) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",t = "xyzxyzxyzxyzxyz",maxCost = 26) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",t = "xyzxyzxyzxyzxyz",maxCost = 26) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "samecharacters",t = "samecharacters",maxCost = 0) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "samecharacters",t = "samecharacters",maxCost = 0) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",maxCost = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",maxCost = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "abcdefghjk",maxCost = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "abcdefghjk",maxCost = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",t = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",maxCost = 500) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",t = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",maxCost = 500) == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",t = "zzeeffgghhii",maxCost = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",t = "zzeeffgghhii",maxCost = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcdefghijklmnopqrstuvwxyza",maxCost = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcdefghijklmnopqrstuvwxyza",maxCost = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 0) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 0) == 48: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "acde",maxCost = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "acde",maxCost = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabc",t = "defdefdefdefdefdef",maxCost = 18) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabc",t = "defdefdefdefdefdef",maxCost = 18) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "defdefdefdefdefdefdefdefdefdefdefdef",maxCost = 27) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "defdefdefdefdefdefdefdefdefdefdefdef",maxCost = 27) == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaa",t = "zzzzzaaaaazzzz",maxCost = 40) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaa",t = "zzzzzaaaaazzzz",maxCost = 40) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",t = "abcdbacdabca",maxCost = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",t = "abcdbacdabca",maxCost = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zabcdefghijklmnopqrstuvwxy",maxCost = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zabcdefghijklmnopqrstuvwxy",maxCost = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "ab",t = "ba",maxCost = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab",t = "ba",maxCost = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzyyyyxxxwwwwvvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaa",t = "aaabbbcccdddeeefffggghhiijjkkllmmnnoopppqqrrssttuuvvvwwwxxxxyyyyzzzz",maxCost = 200) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzyyyyxxxwwwwvvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaa",t = "aaabbbcccdddeeefffggghhiijjkkllmmnnoopppqqrrssttuuvvvwwwxxxxyyyyzzzz",maxCost = 200) == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",t = "zyxwzyxwzyxwzyx",maxCost = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",t = "zyxwzyxwzyxwzyx",maxCost = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",t = "xyzw",maxCost = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",t = "xyzw",maxCost = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbccccdddd",t = "ddddccccbbbbaaaa",maxCost = 20) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbccccdddd",t = "ddddccccbbbbaaaa",maxCost = 20) == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",t = "zyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxw",maxCost = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",t = "zyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxw",maxCost = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",t = "zzzzzzzzzz",maxCost = 250) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",t = "zzzzzzzzzz",maxCost = 250) == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 150) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 150) == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",t = "zzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyy",maxCost = 150) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",t = "zzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyy",maxCost = 150) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopasdfghjklzxcvbnm",maxCost = 0) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopasdfghjklzxcvbnm",maxCost = 0) == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "mnbvcxzlkjhgfdsapoiuytrewq",maxCost = 150) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "mnbvcxzlkjhgfdsapoiuytrewq",maxCost = 150) == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",t = "aaaaaaaaaa",maxCost = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",t = "aaaaaaaaaa",maxCost = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zabcdefghijklmnopqrstuvwxy",maxCost = 26) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zabcdefghijklmnopqrstuvwxy",maxCost = 26) == 25: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "a",t = "b",maxCost = 1) == 1
    assert candidate(s = "a",t = "a",maxCost = 0) == 1
    assert candidate(s = "krrgw",t = "grkwa",maxCost = 3) == 1
    assert candidate(s = "abcd",t = "abce",maxCost = 1) == 4
    assert candidate(s = "abcdefgh",t = "efghabcd",maxCost = 10) == 2
    assert candidate(s = "krrgw",t = "zjxss",maxCost = 19) == 2
    assert candidate(s = "zzzzz",t = "bbbbb",maxCost = 100) == 4
    assert candidate(s = "abcd",t = "cdef",maxCost = 3) == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 26) == 7
    assert candidate(s = "pxezla",t = "sllerr",maxCost = 5) == 1
    assert candidate(s = "abcde",t = "bcdef",maxCost = 5) == 5
    assert candidate(s = "a",t = "b",maxCost = 0) == 0
    assert candidate(s = "abcd",t = "abcd",maxCost = 10) == 4
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 25) == 7
    assert candidate(s = "abcdabcdabcd",t = "dddddddddddd",maxCost = 10) == 7
    assert candidate(s = "abcd",t = "bcdf",maxCost = 3) == 3
    assert candidate(s = "abcde",t = "fghij",maxCost = 10) == 2
    assert candidate(s = "abcd",t = "acde",maxCost = 0) == 1
    assert candidate(s = "zzzzzzzzzz",t = "aaaaaaaaaa",maxCost = 25) == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 100) == 14
    assert candidate(s = "aaaaabbbbbccccc",t = "bbbbbccccdaaaaa",maxCost = 15) == 12
    assert candidate(s = "a",t = "z",maxCost = 25) == 1
    assert candidate(s = "thisisaverylongstring",t = "thisisaverylongstring",maxCost = 50) == 21
    assert candidate(s = "abcde",t = "fghij",maxCost = 15) == 3
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzz",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaa",maxCost = 130) == 5
    assert candidate(s = "abracadabra",t = "abracadabra",maxCost = 5) == 11
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "aaaaaaaaaaaaaaaaaaaaaaaaaaa",maxCost = 100) == 4
    assert candidate(s = "xylophone",t = "pneumonia",maxCost = 20) == 5
    assert candidate(s = "aabbaabbaabb",t = "bbaabbaabbab",maxCost = 20) == 12
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",t = "pneumonoultramicroscopicsilicovolcanoconiosis",maxCost = 0) == 45
    assert candidate(s = "abcdefghij",t = "abcdefghij",maxCost = 50) == 10
    assert candidate(s = "thisisaverylongstringthatweneedtocompare",t = "thisisaverylongstringthatweneedtoreplace",maxCost = 50) == 40
    assert candidate(s = "xyzz",t = "zzyx",maxCost = 10) == 4
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcd",t = "dddddddddddddddddddddddddddddddd",maxCost = 200) == 32
    assert candidate(s = "ababababababab",t = "bababababababa",maxCost = 12) == 12
    assert candidate(s = "mnopqr",t = "qrstuv",maxCost = 12) == 3
    assert candidate(s = "abacabadabacaba",t = "xyzxyzxyzxyzxyzxyzx",maxCost = 30) == 1
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyz",maxCost = 0) == 26
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",maxCost = 1300) == 52
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 50) == 10
    assert candidate(s = "aaaabbbbcccc",t = "ccccbbbbaaaa",maxCost = 16) == 12
    assert candidate(s = "ababababab",t = "bababababa",maxCost = 15) == 10
    assert candidate(s = "abcabcabcabcabc",t = "abcabcabcabcabc",maxCost = 0) == 15
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggeeffddccbbaa",maxCost = 52) == 14
    assert candidate(s = "ababababababababababababababababababababababababab",t = "bababababababababababababababababababababababababa",maxCost = 25) == 25
    assert candidate(s = "mississippi",t = "abababababa",maxCost = 10) == 1
    assert candidate(s = "abcdefghij",t = "abcdefghja",maxCost = 9) == 9
    assert candidate(s = "abcdefghij",t = "abcdefghkj",maxCost = 2) == 10
    assert candidate(s = "acabababcababcaba",t = "bacbababcababcaba",maxCost = 25) == 17
    assert candidate(s = "oneonetwoonetwo",t = "twoonetwoonetwo",maxCost = 8) == 12
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 200) == 8
    assert candidate(s = "xyzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzx",maxCost = 50) == 29
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",maxCost = 0) == 52
    assert candidate(s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba",maxCost = 100) == 14
    assert candidate(s = "abcdabcdabcdabcdabcd",t = "dddddddddddddddddddd",maxCost = 15) == 11
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcdefghijklmnopqrstuvwxyza",maxCost = 51) == 26
    assert candidate(s = "thisisateststring",t = "jajajajajajajajaj",maxCost = 50) == 5
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",maxCost = 100) == 20
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",t = "zzyyxxwwvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbaa",maxCost = 200) == 28
    assert candidate(s = "aaaabbbbcccc",t = "ccccbbbbaaaaffff",maxCost = 15) == 11
    assert candidate(s = "abcdefghij",t = "abcdefghij",maxCost = 1) == 10
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 250) == 10
    assert candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 100) == 10
    assert candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 50) == 10
    assert candidate(s = "abcabcabcabcabcabcabcabc",t = "bcbcbcbcbcbcbcbcbcbcbcbcbcbc",maxCost = 30) == 24
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "bbbbbbbbbbbbbbbbbbbbbbbbbb",maxCost = 100) == 26
    assert candidate(s = "abacabadabacaba",t = "xyzxyzxyzxyzxyz",maxCost = 26) == 1
    assert candidate(s = "samecharacters",t = "samecharacters",maxCost = 0) == 14
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",maxCost = 30) == 1
    assert candidate(s = "abcdefghij",t = "abcdefghjk",maxCost = 1) == 9
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",t = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",maxCost = 500) == 21
    assert candidate(s = "aabbccddeeff",t = "zzeeffgghhii",maxCost = 15) == 5
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "bcdefghijklmnopqrstuvwxyza",maxCost = 25) == 25
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",t = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 0) == 48
    assert candidate(s = "abcd",t = "acde",maxCost = 2) == 3
    assert candidate(s = "abcabcabcabcabcabc",t = "defdefdefdefdefdef",maxCost = 18) == 6
    assert candidate(s = "abcabcabcabcabcabcabcabcabcabc",t = "defdefdefdefdefdefdefdefdefdefdefdef",maxCost = 27) == 9
    assert candidate(s = "aaaaabbbbbaaaa",t = "zzzzzaaaaazzzz",maxCost = 40) == 6
    assert candidate(s = "abcdabcdabcd",t = "abcdbacdabca",maxCost = 15) == 12
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zabcdefghijklmnopqrstuvwxy",maxCost = 25) == 25
    assert candidate(s = "ab",t = "ba",maxCost = 100) == 2
    assert candidate(s = "zzzzyyyyxxxwwwwvvvuuttssrrqqppoonnmmllkkjjiihhggffeeddccbbbaaa",t = "aaabbbcccdddeeefffggghhiijjkkllmmnnoopppqqrrssttuuvvvwwwxxxxyyyyzzzz",maxCost = 200) == 28
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaa",t = "zzzzzzzzzzzzzzzzzzzzzzzzzz",maxCost = 100) == 4
    assert candidate(s = "abacabadabacaba",t = "zyxwzyxwzyxwzyx",maxCost = 50) == 2
    assert candidate(s = "abcd",t = "xyzw",maxCost = 12) == 0
    assert candidate(s = "aaaabbbbccccdddd",t = "ddddccccbbbbaaaa",maxCost = 20) == 12
    assert candidate(s = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",t = "zyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxwzyxw",maxCost = 50) == 2
    assert candidate(s = "abcdefghij",t = "jihgfedcba",maxCost = 30) == 7
    assert candidate(s = "aaaaaaaaaa",t = "zzzzzzzzzz",maxCost = 250) == 10
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zyxwvutsrqponmlkjihgfedcba",maxCost = 150) == 17
    assert candidate(s = "aabbaabbaabbaabbaabbaabbaabbaabbaabbaabb",t = "zzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyyzzyy",maxCost = 150) == 6
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "qwertyuiopasdfghjklzxcvbnm",maxCost = 0) == 26
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnm",t = "mnbvcxzlkjhgfdsapoiuytrewq",maxCost = 150) == 25
    assert candidate(s = "zzzzzzzzzz",t = "aaaaaaaaaa",maxCost = 100) == 4
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",t = "zabcdefghijklmnopqrstuvwxy",maxCost = 26) == 25


