def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 44) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 97: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 104) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 841) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 841) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1009) == 1009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1009) == 1009: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 6857) == 6857
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6857) == 6857: {e}')
    
    total += 1
    try:
        result = candidate(n = 72) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 13195) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13195) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 225) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 720) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 720) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 789) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 2048) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2048) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 2310) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2310) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 65536) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65536) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 169) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 169) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 104729) == 104729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104729) == 104729: {e}')
    
    total += 1
    try:
        result = candidate(n = 97531) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97531) == 67: {e}')
    
    total += 1
    try:
        result = candidate(n = 99998) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99998) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 619
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 619: {e}')
    
    total += 1
    try:
        result = candidate(n = 3125) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3125) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8898) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8898) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 510510) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 510510) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 121) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 1237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 1237: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 600851475143) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600851475143) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 84) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 3
    assert candidate(n = 15) == 5
    assert candidate(n = 100) == 5
    assert candidate(n = 44) == 5
    assert candidate(n = 28) == 11
    assert candidate(n = 97) == 97
    assert candidate(n = 99999) == 31
    assert candidate(n = 729) == 5
    assert candidate(n = 12345) == 5
    assert candidate(n = 49) == 5
    assert candidate(n = 104) == 19
    assert candidate(n = 841) == 31
    assert candidate(n = 987654) == 5
    assert candidate(n = 1009) == 1009
    assert candidate(n = 60) == 7
    assert candidate(n = 6857) == 6857
    assert candidate(n = 72) == 7
    assert candidate(n = 13195) == 11
    assert candidate(n = 225) == 5
    assert candidate(n = 720) == 19
    assert candidate(n = 128) == 5
    assert candidate(n = 1024) == 5
    assert candidate(n = 100000) == 7
    assert candidate(n = 789) == 11
    assert candidate(n = 2048) == 13
    assert candidate(n = 999) == 7
    assert candidate(n = 2310) == 11
    assert candidate(n = 65536) == 7
    assert candidate(n = 169) == 5
    assert candidate(n = 256) == 5
    assert candidate(n = 77) == 5
    assert candidate(n = 81) == 7
    assert candidate(n = 104729) == 104729
    assert candidate(n = 97531) == 67
    assert candidate(n = 99998) == 5
    assert candidate(n = 1234) == 619
    assert candidate(n = 3125) == 7
    assert candidate(n = 8898) == 7
    assert candidate(n = 510510) == 31
    assert candidate(n = 121) == 13
    assert candidate(n = 1234567) == 1237
    assert candidate(n = 500) == 19
    assert candidate(n = 54321) == 5
    assert candidate(n = 600851475143) == 13
    assert candidate(n = 84) == 5


