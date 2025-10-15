def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = 7,b = 1,c = 0) == "aabaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 1,c = 0) == "aabaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 100,c = 100) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 100,c = 100) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 33,b = 33,c = 34) == "cabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33,b = 33,c = 34) == "cabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 2,c = 2) == "abcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 2,c = 2) == "abcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 5,c = 5) == "abcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 5,c = 5) == "abcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 3,c = 2) == "aabaabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 3,c = 2) == "aabaabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 50,c = 0) == "abababababababababababababababababababababababababababababababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 50,c = 0) == "abababababababababababababababababababababababababababababababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 30,c = 20) == "aabaabaabaabaabaabaabaabaabaabaabaacaabaacaabaacaabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 30,c = 20) == "aabaabaabaabaabaabaabaabaabaabaabaacaabaacaabaacaabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 7) == "ccaccbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 7) == "ccaccbcc": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 0,c = 1) == "c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 0,c = 1) == "c": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 0,c = 0) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 0,c = 0) == "": {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 0,c = 0) == "aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 0,c = 0) == "aa": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 0,c = 3) == "cc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 0,c = 3) == "cc": {e}')
    
    total += 1
    try:
        result = candidate(a = 40,b = 30,c = 30) == "aabaacaabaacaabaacaabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 40,b = 30,c = 30) == "aabaacaabaacaabaacaabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 10,c = 10) == "bcbcbcbcbcbcbcbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 10,c = 10) == "bcbcbcbcbcbcbcbcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 10,c = 1) == "ababababababababababc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 10,c = 1) == "ababababababababababc": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 10,c = 15) == "aacaacaacaacaacabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 10,c = 15) == "aacaacaacaacaacabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 20,c = 10) == "bbabbabbabbabababcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 20,c = 10) == "bbabbabbabbabababcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 45,b = 10,c = 45) == "acacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 45,b = 10,c = 45) == "acacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 6,c = 6) == "abcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 6,c = 6) == "abcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 3,c = 3) == "abcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 3,c = 3) == "abcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 40,b = 20,c = 40) == "acacacacacacacacacacacacacacacacacacacacabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 40,b = 20,c = 40) == "acacacacacacacacacacacacacacacacacacacacabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 15,c = 15) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 15,c = 15) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 33,b = 34,c = 33) == "babcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33,b = 34,c = 33) == "babcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 5,c = 4) == "ababcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 5,c = 4) == "ababcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 10,c = 20) == "ccaccbccaccbccaccbcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 10,c = 20) == "ccaccbccaccbccaccbcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 60,b = 40,c = 5) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabababababababababababababababababcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 60,b = 40,c = 5) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabababababababababababababababababcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 4,b = 4,c = 3) == "ababcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4,b = 4,c = 3) == "ababcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 15,c = 5) == "abababababababababababcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 15,c = 5) == "abababababababababababcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 4,c = 4) == "aabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 4,c = 4) == "aabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 5,c = 0) == "ababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 5,c = 0) == "ababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 10,c = 5) == "ababababababcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 10,c = 5) == "ababababababcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 0,c = 5) == "acacacacac"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 0,c = 5) == "acacacacac": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 20,c = 10) == "abababababababababababcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 20,c = 10) == "abababababababababababcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 34,b = 33,c = 33) == "aabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 34,b = 33,c = 33) == "aabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 0,c = 100) == "cc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 0,c = 100) == "cc": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 20,c = 10) == "bbabbcbbabbcbbabbcbabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 20,c = 10) == "bbabbcbbabbcbbabbcbabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 20,c = 10) == "aabaabaabaabaabaabaabaabaabaababcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 20,c = 10) == "aabaabaabaabaabaabaabaabaabaababcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 30,c = 20) == "abababababababababababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 30,c = 20) == "abababababababababababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 25,c = 20) == "bbabbcbbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 25,c = 20) == "bbabbcbbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 50,c = 50) == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 50,c = 50) == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(a = 90,b = 5,c = 5) == "aabaacaabaacaabaacaabaacaabaacaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 90,b = 5,c = 5) == "aabaacaabaacaabaacaabaacaabaacaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 19,c = 18) == "aababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 19,c = 18) == "aababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 6,b = 7,c = 8) == "cbcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 6,b = 7,c = 8) == "cbcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 5) == "ccaccbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 5) == "ccaccbc": {e}')
    
    total += 1
    try:
        result = candidate(a = 4,b = 4,c = 5) == "cabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4,b = 4,c = 5) == "cabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 1,c = 1) == "aabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 1,c = 1) == "aabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 50,c = 50) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 50,c = 50) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 99,b = 1,c = 0) == "aabaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99,b = 1,c = 0) == "aabaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 34,b = 34,c = 32) == "abababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 34,b = 34,c = 32) == "abababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 45,c = 45) == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 45,c = 45) == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 3,c = 5) == "ccbcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 3,c = 5) == "ccbcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 5,c = 10) == "aacaacaacaacaacabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 5,c = 10) == "aacaacaacaacaacabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 2) == "cabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 2) == "cabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 8,c = 9) == "cbcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 8,c = 9) == "cbcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 8,c = 8) == "abcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 8,c = 8) == "abcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 33,b = 33,c = 33) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33,b = 33,c = 33) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 25,c = 24) == "ababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 25,c = 24) == "ababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 50,c = 50) == "aabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabacabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 50,c = 50) == "aabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabacabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 2,c = 2) == "aabaacabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 2,c = 2) == "aabaacabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 25,c = 25) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 25,c = 25) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 99,b = 99,c = 99) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99,b = 99,c = 99) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 15,c = 10) == "ababababababcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 15,c = 10) == "ababababababcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 3,c = 9) == "ccaccbccacbcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 3,c = 9) == "ccaccbccacbcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 15,c = 1) == "abababababababababababababababc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 15,c = 1) == "abababababababababababababababc": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 10,c = 10) == "abcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 10,c = 10) == "abcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 9,b = 8,c = 7) == "aababcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 9,b = 8,c = 7) == "aababcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 3,c = 4) == "cabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 3,c = 4) == "cabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2,c = 1) == "babc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2,c = 1) == "babc": {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 2,c = 1) == "aababc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 2,c = 1) == "aababc": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 1,c = 1) == "aabaacaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 1,c = 1) == "aabaacaa": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 5,c = 15) == "ccaccaccaccacacabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 5,c = 15) == "ccaccaccaccacacabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 1) == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 1) == "abc": {e}')
    
    total += 1
    try:
        result = candidate(a = 49,b = 50,c = 51) == "cbcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 49,b = 50,c = 51) == "cbcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 10,c = 10) == "aabaacaabaacaabaacaabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 10,c = 10) == "aabaacaabaacaabaacaabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 51,b = 50,c = 49) == "aababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 51,b = 50,c = 49) == "aababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 30,c = 20) == "bbabbcbbabbcbbabbcbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 30,c = 20) == "bbabbcbbabbcbbabbcbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 100,c = 1) == "bbabbcbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 100,c = 1) == "bbabbcbb": {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 5,c = 10) == "ccaccbccabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 5,c = 10) == "ccaccbccabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 50,c = 1) == "ababababababababababababababababababababababababababababababababababababababababababababababababababc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 50,c = 1) == "ababababababababababababababababababababababababababababababababababababababababababababababababababc": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 100,c = 0) == "bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 100,c = 0) == "bb": {e}')
    
    total += 1
    try:
        result = candidate(a = 24,b = 25,c = 25) == "bcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 24,b = 25,c = 25) == "bcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 10,c = 15) == "ccaccbccabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 10,c = 15) == "ccaccbccabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 100) == "ccaccbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 100) == "ccaccbcc": {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2,c = 3) == "cbcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2,c = 3) == "cbcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 20,c = 19) == "ababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 20,c = 19) == "ababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 45,b = 45,c = 10) == "ababababababababababababababababababababababababababababababababababababcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 45,b = 45,c = 10) == "ababababababababababababababababababababababababababababababababababababcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 0,b = 5,c = 5) == "bcbcbcbcbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 0,b = 5,c = 5) == "bcbcbcbcbc": {e}')
    
    total += 1
    try:
        result = candidate(a = 60,b = 40,c = 0) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaababababababababababababababababababababab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 60,b = 40,c = 0) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaababababababababababababababababababababab": {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 7,c = 5) == "bbcbbcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 7,c = 5) == "bbcbbcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 30,c = 30) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 30,c = 30) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 25,c = 45) == "ccaccaccaccaccaccaccbccaccbccaccbcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 25,c = 45) == "ccaccaccaccaccaccaccbccaccbccaccbcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = 7,b = 1,c = 0) == "aabaa"
    assert candidate(a = 100,b = 100,c = 100) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 33,b = 33,c = 34) == "cabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 2,b = 2,c = 2) == "abcabc"
    assert candidate(a = 5,b = 5,c = 5) == "abcabcabcabcabc"
    assert candidate(a = 5,b = 3,c = 2) == "aabaabcabc"
    assert candidate(a = 50,b = 50,c = 0) == "abababababababababababababababababababababababababababababababababababababababababababababababababab"
    assert candidate(a = 50,b = 30,c = 20) == "aabaabaabaabaabaabaabaabaabaabaabaacaabaacaabaacaabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 1,b = 1,c = 7) == "ccaccbcc"
    assert candidate(a = 0,b = 0,c = 1) == "c"
    assert candidate(a = 0,b = 0,c = 0) == ""
    assert candidate(a = 100,b = 0,c = 0) == "aa"
    assert candidate(a = 0,b = 0,c = 3) == "cc"
    assert candidate(a = 40,b = 30,c = 30) == "aabaacaabaacaabaacaabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 0,b = 10,c = 10) == "bcbcbcbcbcbcbcbcbcbc"
    assert candidate(a = 10,b = 10,c = 1) == "ababababababababababc"
    assert candidate(a = 20,b = 10,c = 15) == "aacaacaacaacaacabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 15,b = 20,c = 10) == "bbabbabbabbabababcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 45,b = 10,c = 45) == "acacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacacabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 6,b = 6,c = 6) == "abcabcabcabcabcabc"
    assert candidate(a = 3,b = 3,c = 3) == "abcabcabc"
    assert candidate(a = 40,b = 20,c = 40) == "acacacacacacacacacacacacacacacacacacacacabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 15,b = 15,c = 15) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 33,b = 34,c = 33) == "babcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 5,b = 5,c = 4) == "ababcabcabcabc"
    assert candidate(a = 10,b = 10,c = 20) == "ccaccbccaccbccaccbcabcabcabcabcabcabcabc"
    assert candidate(a = 60,b = 40,c = 5) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabababababababababababababababababcabcabcabcabc"
    assert candidate(a = 4,b = 4,c = 3) == "ababcabcabc"
    assert candidate(a = 15,b = 15,c = 5) == "abababababababababababcabcabcabcabc"
    assert candidate(a = 5,b = 4,c = 4) == "aabcabcabcabc"
    assert candidate(a = 5,b = 5,c = 0) == "ababababab"
    assert candidate(a = 10,b = 10,c = 5) == "ababababababcabcabcabcabc"
    assert candidate(a = 5,b = 0,c = 5) == "acacacacac"
    assert candidate(a = 20,b = 20,c = 10) == "abababababababababababcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 34,b = 33,c = 33) == "aabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 0,b = 0,c = 100) == "cc"
    assert candidate(a = 10,b = 20,c = 10) == "bbabbcbbabbcbbabbcbabcabcabcabcabcabcabc"
    assert candidate(a = 30,b = 20,c = 10) == "aabaabaabaabaabaabaabaabaabaababcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 30,b = 30,c = 20) == "abababababababababababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 20,b = 25,c = 20) == "bbabbcbbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 0,b = 50,c = 50) == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc"
    assert candidate(a = 90,b = 5,c = 5) == "aabaacaabaacaabaacaabaacaabaacaa"
    assert candidate(a = 20,b = 19,c = 18) == "aababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 6,b = 7,c = 8) == "cbcabcabcabcabcabcabc"
    assert candidate(a = 1,b = 1,c = 5) == "ccaccbc"
    assert candidate(a = 4,b = 4,c = 5) == "cabcabcabcabc"
    assert candidate(a = 2,b = 1,c = 1) == "aabc"
    assert candidate(a = 50,b = 50,c = 50) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 99,b = 1,c = 0) == "aabaa"
    assert candidate(a = 34,b = 34,c = 32) == "abababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 10,b = 45,c = 45) == "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 2,b = 3,c = 5) == "ccbcabcabc"
    assert candidate(a = 15,b = 5,c = 10) == "aacaacaacaacaacabcabcabcabcabc"
    assert candidate(a = 1,b = 1,c = 2) == "cabc"
    assert candidate(a = 7,b = 8,c = 9) == "cbcabcabcabcabcabcabcabc"
    assert candidate(a = 8,b = 8,c = 8) == "abcabcabcabcabcabcabcabc"
    assert candidate(a = 33,b = 33,c = 33) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 25,b = 25,c = 24) == "ababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 100,b = 50,c = 50) == "aabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabaacaabacabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 5,b = 2,c = 2) == "aabaacabc"
    assert candidate(a = 25,b = 25,c = 25) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 99,b = 99,c = 99) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 15,b = 15,c = 10) == "ababababababcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 3,b = 3,c = 9) == "ccaccbccacbcabc"
    assert candidate(a = 15,b = 15,c = 1) == "abababababababababababababababc"
    assert candidate(a = 10,b = 10,c = 10) == "abcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 9,b = 8,c = 7) == "aababcabcabcabcabcabcabc"
    assert candidate(a = 3,b = 3,c = 4) == "cabcabcabc"
    assert candidate(a = 1,b = 2,c = 1) == "babc"
    assert candidate(a = 3,b = 2,c = 1) == "aababc"
    assert candidate(a = 10,b = 1,c = 1) == "aabaacaa"
    assert candidate(a = 10,b = 5,c = 15) == "ccaccaccaccacacabcabcabcabcabc"
    assert candidate(a = 1,b = 1,c = 1) == "abc"
    assert candidate(a = 49,b = 50,c = 51) == "cbcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 20,b = 10,c = 10) == "aabaacaabaacaabaacaabcabcabcabcabcabcabc"
    assert candidate(a = 51,b = 50,c = 49) == "aababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 20,b = 30,c = 20) == "bbabbcbbabbcbbabbcbabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 1,b = 100,c = 1) == "bbabbcbb"
    assert candidate(a = 5,b = 5,c = 10) == "ccaccbccabcabcabcabc"
    assert candidate(a = 50,b = 50,c = 1) == "ababababababababababababababababababababababababababababababababababababababababababababababababababc"
    assert candidate(a = 0,b = 100,c = 0) == "bb"
    assert candidate(a = 24,b = 25,c = 25) == "bcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 10,b = 10,c = 15) == "ccaccbccabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 1,b = 1,c = 100) == "ccaccbcc"
    assert candidate(a = 1,b = 2,c = 3) == "cbcabc"
    assert candidate(a = 20,b = 20,c = 19) == "ababcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 45,b = 45,c = 10) == "ababababababababababababababababababababababababababababababababababababcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 0,b = 5,c = 5) == "bcbcbcbcbc"
    assert candidate(a = 60,b = 40,c = 0) == "aabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaabaababababababababababababababababababababab"
    assert candidate(a = 3,b = 7,c = 5) == "bbcbbcabcabcabc"
    assert candidate(a = 30,b = 30,c = 30) == "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"
    assert candidate(a = 30,b = 25,c = 45) == "ccaccaccaccaccaccaccbccaccbccaccbcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc"


