def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "abc",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababa",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababa",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcd",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcd",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnn",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnn",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abac",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abac",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdfgdcaba",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdfgdcaba",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "palindrome",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "palindrome",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccdd",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccdd",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "palindrome",k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "palindrome",k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 13) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 13) == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbaabbaabb",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbaabbaabb",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababab",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababab",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeff",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeff",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdcbaabcdcba",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdcbaabcdcba",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxy",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxy",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mamamamamama",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mamamamamama",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zxyxzyxzyxzyx",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zxyxzyxzyxzyx",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababababa",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababababa",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyxyxyxyxyxy",k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyxyxyxyxyxy",k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zazapapa",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zazapapa",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyxyxyxyx",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyxyxyxyx",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mnopqrstu",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mnopqrstu",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdedcba",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdedcba",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbcaabc",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbcaabc",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgabcdefg",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgabcdefg",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaaa",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaaa",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijk",k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijk",k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghh",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghh",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzzyxzyxzyxzyxzyxzyx",k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzzyxzyxzyxzyxzyxzyx",k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "levelmadammadam",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "levelmadammadam",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij",k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij",k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "banana",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "banana",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "noonnoonnoon",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noonnoonnoon",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecar",k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecar",k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacdefghijklmnopqrstuvwxyz",k = 26) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacdefghijklmnopqrstuvwxyz",k = 26) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyxzyzxzyx",k = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyxzyzxzyx",k = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabc",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabc",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaa",k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaa",k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccba",k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccba",k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcbabcba",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcbabcba",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh",k = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh",k = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzyzyzyzyzyz",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzyzyzyzyzyz",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabaaa",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabaaa",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefg",k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefg",k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababab",k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababab",k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabc",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabc",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz",k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz",k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccccba",k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccccba",k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi",k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi",k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababababababab",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababababababab",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "ababababa",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ababababa",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba",k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba",k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccccba",k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccccba",k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghi",k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghi",k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxaba",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxaba",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababbaab",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababbaab",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbcccccddddd",k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbcccccddddd",k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "racecarannakayak",k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "racecarannakayak",k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabba",k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabba",k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaxabac",k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaxabac",k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbb",k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbb",k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcdabcd",k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcdabcd",k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "abc",k = 2) == 1
    assert candidate(s = "abababa",k = 4) == 1
    assert candidate(s = "aaaa",k = 2) == 0
    assert candidate(s = "leetcode",k = 8) == 0
    assert candidate(s = "abcd",k = 2) == 1
    assert candidate(s = "racecar",k = 5) == 0
    assert candidate(s = "nnn",k = 1) == 0
    assert candidate(s = "abac",k = 3) == 1
    assert candidate(s = "racecar",k = 1) == 0
    assert candidate(s = "aabbc",k = 3) == 0
    assert candidate(s = "abacdfgdcaba",k = 3) == 1
    assert candidate(s = "palindrome",k = 2) == 4
    assert candidate(s = "aaaabbbbcccc",k = 3) == 0
    assert candidate(s = "aabbccdd",k = 4) == 0
    assert candidate(s = "zzzzzzzzzz",k = 1) == 0
    assert candidate(s = "palindrome",k = 4) == 3
    assert candidate(s = "mississippi",k = 4) == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 13) == 14
    assert candidate(s = "banana",k = 2) == 0
    assert candidate(s = "abcdefg",k = 7) == 0
    assert candidate(s = "aabbaabbaabbaabb",k = 4) == 0
    assert candidate(s = "ababababab",k = 5) == 1
    assert candidate(s = "abcdefg",k = 4) == 2
    assert candidate(s = "aabbccddeeff",k = 6) == 0
    assert candidate(s = "abcdcbaabcdcba",k = 4) == 0
    assert candidate(s = "xyxyxyxyxy",k = 5) == 1
    assert candidate(s = "mamamamamama",k = 5) == 1
    assert candidate(s = "zxyxzyxzyxzyx",k = 4) == 2
    assert candidate(s = "aababababa",k = 5) == 0
    assert candidate(s = "xyxyxyxyxyxyxyxyxy",k = 9) == 1
    assert candidate(s = "zazapapa",k = 3) == 1
    assert candidate(s = "xyxyxyxyx",k = 5) == 0
    assert candidate(s = "abababab",k = 5) == 1
    assert candidate(s = "abcde",k = 3) == 1
    assert candidate(s = "mnopqrstu",k = 5) == 2
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 50) == 0
    assert candidate(s = "abcdedcba",k = 3) == 0
    assert candidate(s = "abcbcaabc",k = 3) == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz",k = 26) == 0
    assert candidate(s = "abcdefgabcdefg",k = 2) == 6
    assert candidate(s = "aaaaaaaaaaa",k = 2) == 0
    assert candidate(s = "aabbaa",k = 3) == 0
    assert candidate(s = "racecar",k = 3) == 0
    assert candidate(s = "abcdefghijk",k = 3) == 4
    assert candidate(s = "aabbccddeeffgghh",k = 8) == 0
    assert candidate(s = "xyzzyxzyxzyxzyxzyxzyx",k = 5) == 4
    assert candidate(s = "levelmadammadam",k = 4) == 0
    assert candidate(s = "abcdefghij",k = 5) == 3
    assert candidate(s = "abcdabcdabcd",k = 3) == 3
    assert candidate(s = "noonnoonnoon",k = 6) == 0
    assert candidate(s = "aaaaaaaaaa",k = 5) == 0
    assert candidate(s = "banana",k = 3) == 1
    assert candidate(s = "noonnoonnoon",k = 4) == 0
    assert candidate(s = "racecar",k = 2) == 3
    assert candidate(s = "abacdefghijklmnopqrstuvwxyz",k = 26) == 1
    assert candidate(s = "xyzyxzyzxzyx",k = 6) == 0
    assert candidate(s = "abcbabc",k = 3) == 0
    assert candidate(s = "aabbaa",k = 2) == 1
    assert candidate(s = "aaaaabbbbb",k = 2) == 0
    assert candidate(s = "abccba",k = 1) == 0
    assert candidate(s = "abcbabcba",k = 4) == 1
    assert candidate(s = "abcdefghi",k = 3) == 3
    assert candidate(s = "abcdefgh",k = 8) == 0
    assert candidate(s = "abcdefghi",k = 9) == 0
    assert candidate(s = "xyzyzyzyzyzyz",k = 3) == 0
    assert candidate(s = "abcdefg",k = 3) == 2
    assert candidate(s = "aabaaa",k = 2) == 0
    assert candidate(s = "abcdefg",k = 1) == 3
    assert candidate(s = "ababab",k = 2) == 0
    assert candidate(s = "abcdabc",k = 3) == 1
    assert candidate(s = "xyzxyzxyz",k = 3) == 2
    assert candidate(s = "abccccba",k = 2) == 2
    assert candidate(s = "mississippi",k = 3) == 1
    assert candidate(s = "zzzzzzzzzz",k = 5) == 0
    assert candidate(s = "abababababababababab",k = 10) == 0
    assert candidate(s = "ababababa",k = 5) == 0
    assert candidate(s = "abacabadabacaba",k = 7) == 0
    assert candidate(s = "abccccba",k = 3) == 0
    assert candidate(s = "abcdefghi",k = 5) == 2
    assert candidate(s = "abacaxaba",k = 4) == 1
    assert candidate(s = "aababbaab",k = 4) == 0
    assert candidate(s = "aaaaabbbbbcccccddddd",k = 10) == 0
    assert candidate(s = "racecarannakayak",k = 4) == 1
    assert candidate(s = "abbaabba",k = 4) == 0
    assert candidate(s = "abacaxabac",k = 5) == 1
    assert candidate(s = "zzzzzzzzz",k = 5) == 0
    assert candidate(s = "aaaaabbbbb",k = 5) == 0
    assert candidate(s = "abcdabcdabcd",k = 4) == 2
    assert candidate(s = "zyxwvutsrqponmlkjihgfedcba",k = 26) == 0


