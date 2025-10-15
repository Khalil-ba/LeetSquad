def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "zzzzzzy") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzy") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "zyzzyzyzy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zyzzyzyzy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abbaabbaabba") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abbaabbaabba") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "abababab") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abababab") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aaaaa") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aaaaa") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzyzxzyzyzxzyzxzyzxzyzxzyzxzyzxzyz") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzyzxzyzyzxzyzxzyzxzyzxzyzxzyzxzyz") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcabcabcabc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcabcabcabc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcde") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcde") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "leetcode") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "leetcode") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "xyzxyzxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "xyzxyzxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "abccccccc") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abccccccc") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzzzzzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzzzzzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "zzzzzyyyyxxxxwwwwvvvvuuuuttttssssrrrrqqqqppppllllkkkkjjjjiiiihhhhggggffffffeee ddcccbbbbaaaa") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "zzzzzyyyyxxxxwwwwvvvvuuuuttttssssrrrrqqqqppppllllkkkkjjjjiiiihhhhggggffffffeee ddcccbbbbaaaa") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbcc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbcc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "mississippi") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "mississippi") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbccddeeffgghhiijj") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbccddeeffgghhiijj") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "aabbaaabb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aabbaaabb") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "abacaba") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abacaba") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "aababbb") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "aababbb") == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "zzzzzzy") == 5
    assert candidate(s = "zyzzyzyzy") == 2
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(s = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "abbaabbaabba") == 2
    assert candidate(s = "abababab") == 1
    assert candidate(s = "aaaaa") == 0
    assert candidate(s = "a") == 0
    assert candidate(s = "abcabcabc") == 1
    assert candidate(s = "zzyzxzyzyzxzyzxzyzxzyzxzyzxzyzxzyz") == 11
    assert candidate(s = "abcabcabcabc") == 1
    assert candidate(s = "abcde") == 0
    assert candidate(s = "leetcode") == 2
    assert candidate(s = "xyzxyzxyz") == 1
    assert candidate(s = "abccccccc") == 6
    assert candidate(s = "zzzzzzzzzz") == 0
    assert candidate(s = "zzzzzyyyyxxxxwwwwvvvvuuuuttttssssrrrrqqqqppppllllkkkkjjjjiiiihhhhggggffffffeee ddcccbbbbaaaa") == 5
    assert candidate(s = "aabbcc") == 1
    assert candidate(s = "mississippi") == 3
    assert candidate(s = "abcdefghij") == 0
    assert candidate(s = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 1
    assert candidate(s = "aabbccddeeffgghhiijj") == 1
    assert candidate(s = "aabbaaabb") == 3
    assert candidate(s = "abacaba") == 3
    assert candidate(s = "aababbb") == 3


