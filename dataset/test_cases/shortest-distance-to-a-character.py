def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abba",c = "a") == [0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba",c = "a") == [0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "loveleetcode",c = "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "loveleetcode",c = "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",c = "e") == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",c = "e") == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc",c = "b") == [1, 0, 1, 1, 0, 1, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc",c = "b") == [1, 0, 1, 1, 0, 1, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcde",c = "c") == [2, 1, 0, 1, 2, 1, 0, 1, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcde",c = "c") == [2, 1, 0, 1, 2, 1, 0, 1, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "eccdccccdcccdcced",c = "e") == [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "eccdccccdcccdcced",c = "e") == [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabc",c = "a") == [0, 1, 2, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabc",c = "a") == [0, 1, 2, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc",c = "b") == [2, 1, 0, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc",c = "b") == [2, 1, 0, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzz",c = "z") == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzz",c = "z") == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaacc",c = "c") == [4, 3, 2, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaacc",c = "c") == [4, 3, 2, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab",c = "a") == [0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab",c = "a") == [0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",c = "d") == [6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",c = "d") == [6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",c = "a") == [0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",c = "a") == [0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaabaaa",c = "b") == [2, 1, 0, 1, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaabaaa",c = "b") == [2, 1, 0, 1, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaab",c = "b") == [3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaab",c = "b") == [3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",c = "a") == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",c = "a") == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",c = "i") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",c = "i") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",c = "g") == [6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",c = "g") == [6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abba",c = "b") == [1, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abba",c = "b") == [1, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",c = "a") == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",c = "a") == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbccccc",c = "b") == [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbccccc",c = "b") == [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "a",c = "a") == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a",c = "a") == [0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyz",c = "z") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyz",c = "z") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "m") == [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "m") == [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohello",c = "h") == [0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohello",c = "h") == [0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabraabracadabraabracadabra",c = "a") == [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabraabracadabraabracadabra",c = "a") == [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzxxxyyyzzz",c = "y") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzxxxyyyzzz",c = "y") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "o") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "o") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghij",c = "f") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghij",c = "f") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeleetcodeleetcode",c = "e") == [1, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeleetcodeleetcode",c = "e") == [1, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "allaboutthatbass",c = "a") == [0, 1, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "allaboutthatbass",c = "a") == [0, 1, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "alibabaibabaibabaibabaibabaibabaibabaibaba",c = "b") == [3, 2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "alibabaibabaibabaibabaibabaibabaibabaibaba",c = "b") == [3, 2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabbaabbaabbaabbaa",c = "b") == [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabbaabbaabbaabbaa",c = "b") == [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyxzyxzyzyx",c = "z") == [3, 2, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyxzyxzyzyx",c = "z") == [3, 2, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",c = "n") == [2, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",c = "n") == [2, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "antidisestablishmentarianism",c = "a") == [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 1, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "antidisestablishmentarianism",c = "a") == [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 1, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",c = "b") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",c = "b") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",c = "a") == [1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",c = "a") == [1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababa",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababa",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",c = "x") == [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",c = "x") == [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaabaaaaaaaa",c = "b") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaabaaaaaaaa",c = "b") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaabbbaaaa",c = "b") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaabbbaaaa",c = "b") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "helloworld",c = "o") == [4, 3, 2, 1, 0, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "helloworld",c = "o") == [4, 3, 2, 1, 0, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzxyzxxzyzxzzzxzyzxzyzxzyzxzyz",c = "x") == [3, 2, 1, 0, 1, 1, 0, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzxyzxxzyzxzzzxzyzxzyzxzyzxzyz",c = "x") == [3, 2, 1, 0, 1, 1, 0, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzzzzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzzzzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",c = "a") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",c = "a") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababa",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababa",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",c = "c") == [2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",c = "c") == [2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababababababababababababababababababab",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababababababababababababababababababab",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "honorificabilitudinitatibus",c = "i") == [5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "honorificabilitudinitatibus",c = "i") == [5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",c = "y") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",c = "y") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeleetcodeleetcode",c = "o") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeleetcodeleetcode",c = "o") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",c = "p") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",c = "p") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bababababababababababababababababababababa",c = "b") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bababababababababababababababababababababa",c = "b") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "m") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "m") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",c = "c") == [2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",c = "c") == [2, 1, 0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "longstringwithvariouscharacters",c = "r") == [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longstringwithvariouscharacters",c = "r") == [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbbbbbaaaabbbbbbaaaabbbbbbaaaabbbbbb",c = "a") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbbbbbaaaabbbbbbaaaabbbbbbaaaabbbbbb",c = "a") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",c = "h") == [7, 6, 5, 4, 3, 2, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",c = "h") == [7, 6, 5, 4, 3, 2, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "a") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "a") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",c = "d") == [3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",c = "d") == [3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxzyzyzxzyzxzyzx",c = "z") == [3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxzyzyzxzyzxzyzx",c = "z") == [3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbcccdddeee",c = "c") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbcccdddeee",c = "c") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "q") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "q") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",c = "j") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",c = "j") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",c = "o") == [5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 1, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",c = "o") == [5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 1, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrownfoxjumpsoverthelazydog",c = "o") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrownfoxjumpsoverthelazydog",c = "o") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",c = "a") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",c = "a") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyxzyxzyxz",c = "y") == [2, 1, 0, 1, 1, 0, 1, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyxzyxzyxz",c = "y") == [2, 1, 0, 1, 1, 0, 1, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "z") == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "z") == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "longwordwithmanyletters",c = "w") == [4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "longwordwithmanyletters",c = "w") == [4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",c = "e") == [3, 2, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",c = "e") == [3, 2, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",c = "c") == [3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",c = "c") == [3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "programming",c = "m") == [6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "programming",c = "m") == [6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabcabc",c = "b") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabcabc",c = "b") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",c = "b") == [1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",c = "b") == [1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabaaaabaaaaabaaa",c = "b") == [5, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabaaaabaaaaabaaa",c = "b") == [5, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijabcdefghijabcdefghij",c = "f") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijabcdefghijabcdefghij",c = "f") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "pppppppppp",c = "p") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "pppppppppp",c = "p") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xxyyzzxxxyyzz",c = "z") == [4, 3, 2, 1, 0, 0, 1, 2, 3, 2, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xxyyzzxxxyyzz",c = "z") == [4, 3, 2, 1, 0, 0, 1, 2, 3, 2, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaaaaaaab",c = "b") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaaaaaaab",c = "b") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "bbaabbaabbaa",c = "a") == [2, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "bbaabbaabbaa",c = "a") == [2, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "p") == [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "p") == [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(s = "civicciviccivic",c = "v") == [2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "civicciviccivic",c = "v") == [2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",c = "z") == [2, 1, 0, 1, 1, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",c = "z") == [2, 1, 0, 1, 1, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",c = "d") == [3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",c = "d") == [3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "c") == [4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "c") == [4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thequickbrownfoxjumpsoverthelazydog",c = "q") == [3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thequickbrownfoxjumpsoverthelazydog",c = "q") == [3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",c = "n") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",c = "n") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "xylophone",c = "o") == [3, 2, 1, 0, 1, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xylophone",c = "o") == [3, 2, 1, 0, 1, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",c = "a") == [1, 0, 1, 2, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",c = "a") == [1, 0, 1, 2, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbaaa",c = "b") == [3, 2, 1, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbaaa",c = "b") == [3, 2, 1, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "floccinaucinihilipilification",c = "f") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "floccinaucinihilipilification",c = "f") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "elephantelephant",c = "e") == [0, 1, 0, 1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "elephantelephant",c = "e") == [0, 1, 0, 1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithsomerepeatedcharacters",c = "s") == [3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithsomerepeatedcharacters",c = "s") == [3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",c = "d") == [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",c = "d") == [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaabbbbcccc",c = "b") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaabbbbcccc",c = "b") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "m") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "m") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abracadabra",c = "a") == [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abracadabra",c = "a") == [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcodeisnice",c = "e") == [1, 0, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcodeisnice",c = "e") == [1, 0, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefgabcdefg",c = "g") == [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefgabcdefg",c = "g") == [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababa",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababa",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "lkhfjldshgflsjghljsfgljsdgfljsgdfjlsghsflkghsflkl",c = "l") == [0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lkhfjldshgflsjghljsfgljsdgfljsgdfjlsghsflkghsflkl",c = "l") == [0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "supercalifragilisticexpialidocious",c = "i") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 0, 1, 2, 2, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "supercalifragilisticexpialidocious",c = "i") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 0, 1, 2, 2, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(s = "hellohellohellohello",c = "l") == [2, 1, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hellohellohellohello",c = "l") == [2, 1, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(s = "elephant",c = "e") == [0, 1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "elephant",c = "e") == [0, 1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(s = "thisisaverylongstringwithmultiplescharacters",c = "s") == [3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "thisisaverylongstringwithmultiplescharacters",c = "s") == [3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "llllllllllllllllllllllllllllllllllllllllllllllllllllll",c = "l") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "llllllllllllllllllllllllllllllllllllllllllllllllllllll",c = "l") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(s = "supercalifragilisticexpialidocious",c = "x") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "supercalifragilisticexpialidocious",c = "x") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abba",c = "a") == [0, 1, 1, 0]
    assert candidate(s = "loveleetcode",c = "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    assert candidate(s = "abcde",c = "e") == [4, 3, 2, 1, 0]
    assert candidate(s = "abcabcabc",c = "b") == [1, 0, 1, 1, 0, 1, 1, 0, 1]
    assert candidate(s = "abcdabcabcde",c = "c") == [2, 1, 0, 1, 2, 1, 0, 1, 1, 0, 1, 2]
    assert candidate(s = "eccdccccdcccdcced",c = "e") == [0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 0, 1]
    assert candidate(s = "abcdabc",c = "a") == [0, 1, 2, 1, 0, 1, 2]
    assert candidate(s = "aabbcc",c = "b") == [2, 1, 0, 0, 1, 2]
    assert candidate(s = "zzzz",c = "z") == [0, 0, 0, 0]
    assert candidate(s = "bbaacc",c = "c") == [4, 3, 2, 1, 0, 0]
    assert candidate(s = "ababab",c = "a") == [0, 1, 0, 1, 0, 1]
    assert candidate(s = "aabbccddeeff",c = "d") == [6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4]
    assert candidate(s = "abcdefg",c = "a") == [0, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "aabaabaaa",c = "b") == [2, 1, 0, 1, 1, 0, 1, 2, 3]
    assert candidate(s = "aaab",c = "b") == [3, 2, 1, 0]
    assert candidate(s = "abcde",c = "a") == [0, 1, 2, 3, 4]
    assert candidate(s = "mississippi",c = "i") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
    assert candidate(s = "abcdefg",c = "g") == [6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "abba",c = "b") == [1, 0, 0, 1]
    assert candidate(s = "aaaa",c = "a") == [0, 0, 0, 0]
    assert candidate(s = "aaaaabbbbbccccc",c = "b") == [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(s = "a",c = "a") == [0]
    assert candidate(s = "mnopqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyzmnpqrstuvwxyz",c = "z") == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "m") == [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    assert candidate(s = "hellohellohello",c = "h") == [0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 4]
    assert candidate(s = "abracadabraabracadabraabracadabra",c = "a") == [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    assert candidate(s = "zzzxxxyyyzzz",c = "y") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3]
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "o") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]
    assert candidate(s = "abcdefghijabcdefghij",c = "f") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    assert candidate(s = "leetcodeleetcodeleetcode",c = "e") == [1, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    assert candidate(s = "zzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "allaboutthatbass",c = "a") == [0, 1, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 1, 0, 1, 2]
    assert candidate(s = "alibabaibabaibabaibabaibabaibabaibabaibaba",c = "b") == [3, 2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "bbaabbaabbaabbaabbaa",c = "b") == [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 2]
    assert candidate(s = "xyxzyzyxzyxzyzyx",c = "z") == [3, 2, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 2]
    assert candidate(s = "banana",c = "n") == [2, 1, 0, 1, 0, 1]
    assert candidate(s = "antidisestablishmentarianism",c = "a") == [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 1, 0, 1, 2, 3, 4]
    assert candidate(s = "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc",c = "b") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(s = "banana",c = "a") == [1, 0, 1, 0, 1, 0]
    assert candidate(s = "ababababababababababa",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(s = "xyxxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx",c = "x") == [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(s = "aaaaaaaabaaaaaaaa",c = "b") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(s = "aaaaaabbbaaaa",c = "b") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4]
    assert candidate(s = "helloworld",c = "o") == [4, 3, 2, 1, 0, 1, 0, 1, 2, 3]
    assert candidate(s = "abababababababababab",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(s = "zzzxyzxxzyzxzzzxzyzxzyzxzyzxzyz",c = "x") == [3, 2, 1, 0, 1, 1, 0, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3]
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "ababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(s = "abcdefghij",c = "a") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(s = "ababababababababababababababababababababa",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(s = "abcdefgabcdefg",c = "c") == [2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4]
    assert candidate(s = "ababababababababababababababababababababab",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(s = "honorificabilitudinitatibus",c = "i") == [5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 3]
    assert candidate(s = "xyzxyzxyzxyzxyzxyzxyzxyzxyzxyz",c = "y") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
    assert candidate(s = "leetcodeleetcodeleetcode",c = "o") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2]
    assert candidate(s = "mississippi",c = "p") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1]
    assert candidate(s = "bababababababababababababababababababababa",c = "b") == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "m") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert candidate(s = "abcdefghij",c = "c") == [2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "longstringwithvariouscharacters",c = "r") == [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1]
    assert candidate(s = "bbbbbbaaaabbbbbbaaaabbbbbbaaaabbbbbb",c = "a") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "abcdefghij",c = "h") == [7, 6, 5, 4, 3, 2, 1, 0, 1, 2]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "a") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",c = "d") == [3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "xyxzyzyzxzyzxzyzx",c = "z") == [3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert candidate(s = "aaabbbcccdddeee",c = "c") == [6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5, 6]
    assert candidate(s = "qwertyuiopasdfghjklzxcvbnmqwertyuiop",c = "q") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(s = "abcdefghij",c = "j") == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "pneumonoultramicroscopicsilicovolcanoconiosis",c = "o") == [5, 4, 3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 1, 0, 1, 2, 3, 4, 4, 3, 2, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 0, 1, 2, 3]
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog",c = "o") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1]
    assert candidate(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",c = "a") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "zxyxzyxzyxz",c = "y") == [2, 1, 0, 1, 1, 0, 1, 1, 0, 1, 2]
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",c = "z") == [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "zzzzzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "longwordwithmanyletters",c = "w") == [4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(s = "racecar",c = "e") == [3, 2, 1, 0, 1, 2, 3]
    assert candidate(s = "abacabadabacaba",c = "c") == [3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3]
    assert candidate(s = "programming",c = "m") == [6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3]
    assert candidate(s = "abcabcabcabcabc",c = "b") == [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
    assert candidate(s = "abacabadabacaba",c = "b") == [1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
    assert candidate(s = "aaaaabaaaabaaaaabaaa",c = "b") == [5, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3]
    assert candidate(s = "abcdefghijabcdefghijabcdefghij",c = "f") == [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    assert candidate(s = "pppppppppp",c = "p") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "xxyyzzxxxyyzz",c = "z") == [4, 3, 2, 1, 0, 0, 1, 2, 3, 2, 1, 0, 0]
    assert candidate(s = "aaaaaaaaaaaaaaaab",c = "b") == [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "bbaabbaabbaa",c = "a") == [2, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "p") == [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert candidate(s = "civicciviccivic",c = "v") == [2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2]
    assert candidate(s = "xyzxyzxyz",c = "z") == [2, 1, 0, 1, 1, 0, 1, 1, 0]
    assert candidate(s = "zzzzzzz",c = "z") == [0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "abababababababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(s = "abcdefgabcdefg",c = "d") == [3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3]
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",c = "c") == [4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
    assert candidate(s = "thequickbrownfoxjumpsoverthelazydog",c = "q") == [3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    assert candidate(s = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",c = "n") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "abcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(s = "xylophone",c = "o") == [3, 2, 1, 0, 1, 1, 0, 1, 2]
    assert candidate(s = "abababababababababababababab",c = "b") == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(s = "racecar",c = "a") == [1, 0, 1, 2, 1, 0, 1]
    assert candidate(s = "aaabbaaa",c = "b") == [3, 2, 1, 0, 0, 1, 2, 3]
    assert candidate(s = "floccinaucinihilipilification",c = "f") == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "elephantelephant",c = "e") == [0, 1, 0, 1, 2, 3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5]
    assert candidate(s = "thisisaverylongstringwithsomerepeatedcharacters",c = "s") == [3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "abacabadabacaba",c = "d") == [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(s = "aaaaaaaaaabbbbcccc",c = "b") == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4]
    assert candidate(s = "abcdefghigklmnopqrstuvwxyz",c = "m") == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert candidate(s = "abracadabra",c = "a") == [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    assert candidate(s = "leetcodeisnice",c = "e") == [1, 0, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0]
    assert candidate(s = "abcdefgabcdefgabcdefg",c = "g") == [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0]
    assert candidate(s = "ababababa",c = "a") == [0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(s = "lkhfjldshgflsjghljsfgljsdgfljsgdfjlsghsflkghsflkl",c = "l") == [0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 0]
    assert candidate(s = "supercalifragilisticexpialidocious",c = "i") == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 1, 0, 1, 2, 2, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 3]
    assert candidate(s = "hellohellohellohello",c = "l") == [2, 1, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0, 0, 1]
    assert candidate(s = "elephant",c = "e") == [0, 1, 0, 1, 2, 3, 4, 5]
    assert candidate(s = "thisisaverylongstringwithmultiplescharacters",c = "s") == [3, 2, 1, 0, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    assert candidate(s = "llllllllllllllllllllllllllllllllllllllllllllllllllllll",c = "l") == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(s = "supercalifragilisticexpialidocious",c = "x") == [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


