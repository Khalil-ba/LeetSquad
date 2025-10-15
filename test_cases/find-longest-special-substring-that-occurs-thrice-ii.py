def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzz") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzz") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabbbccc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabbbccc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbbcccaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbbcccaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdef") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdef") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacabadabacaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacabadabacaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcaba") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcaba") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbccccc") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbccccc") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbcc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbcc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaaaaaaa") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaaaaaaa") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaabbbbcccc") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaabbbbcccc") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababababa") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababababa") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdabcabcd") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdabcabcd") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeefff") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeefff") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgg") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgg") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaabaaa") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaabaaa") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaabbbbbaaaa") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaabbbbbaaaa") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "nnnhaaaannn") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "nnnhaaaannn") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaabbccddccddc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaabbccddccddc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zzzzzzzzz") == 7
    assert candidate(s = "aaabbbccc") == 1
    assert candidate(s = "aabbbcccaaa") == 2
    assert candidate(s = "abcdef") == -1
    assert candidate(s = "abacabadabacaba") == 1
    assert candidate(s = "abcabcabc") == 1
    assert candidate(s = "abcaba") == 1
    assert candidate(s = "aaaaabbbbccccc") == 3
    assert candidate(s = "aabbaabbcc") == 1
    assert candidate(s = "aaaaaaaaaa") == 8
    assert candidate(s = "aaaabbbbcccc") == 2
    assert candidate(s = "abababababa") == 1
    assert candidate(s = "abcdabcabcd") == 1
    assert candidate(s = "aabbccddeeefff") == 1
    assert candidate(s = "aabbccddeeffgg") == -1
    assert candidate(s = "aaaa") == 2
    assert candidate(s = "aaabaaa") == 2
    assert candidate(s = "aaaaabbbbbaaaa") == 4
    assert candidate(s = "nnnhaaaannn") == 2
    assert candidate(s = "zzzzz") == 3
    assert candidate(s = "aabbaabbccddccddc") == 1
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == -1


