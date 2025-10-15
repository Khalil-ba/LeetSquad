def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 987654321) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 987) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 521) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 521) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 24680) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24680) == -4: {e}')
    
    total += 1
    try:
        result = candidate(n = 886996) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 886996) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 111222333444555666777888999) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111222333444555666777888999) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321987654321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321987654321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10987654321) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10987654321) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456789) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456789) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 5432109876) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5432109876) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000001) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000001) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 909090909) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 909090909) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 202020202) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 202020202) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 135791357) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135791357) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 975318642) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 975318642) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 505050505) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 505050505) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 999888777) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999888777) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 135792468) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 135792468) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 99887766554433221100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99887766554433221100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 246802468) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 246802468) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 123321123321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123321123321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9753186420) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9753186420) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 121212121) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121212121) == -3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5040302010) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5040302010) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 808080808) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 808080808) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1212121212) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1212121212) == -5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321234) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321234) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8642086420) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8642086420) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 112233445566778899) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 112233445566778899) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7654321) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7654321) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1122334455) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1122334455) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 864208642) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 864208642) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321234321234) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321234321234) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1010101010) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1010101010) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222222222) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222222222) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 110011001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 110011001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123321) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123321) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 246813579) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 246813579) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123012301) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123012301) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210987654) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210987654) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1357924680) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1357924680) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 543210987) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 543210987) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 987654321) == 5
    assert candidate(n = 123) == 2
    assert candidate(n = 987) == 8
    assert candidate(n = 9) == 9
    assert candidate(n = 123456789) == 5
    assert candidate(n = 111) == 1
    assert candidate(n = 1) == 1
    assert candidate(n = 1000000000) == 1
    assert candidate(n = 521) == 4
    assert candidate(n = 100000000) == 1
    assert candidate(n = 24680) == -4
    assert candidate(n = 886996) == 0
    assert candidate(n = 222222222) == 2
    assert candidate(n = 111222333444555666777888999) == 5
    assert candidate(n = 999999999) == 9
    assert candidate(n = 987654321987654321) == 0
    assert candidate(n = 10987654321) == 6
    assert candidate(n = 1234567890123456789) == 10
    assert candidate(n = 5432109876) == 5
    assert candidate(n = 100000001) == 2
    assert candidate(n = 909090909) == 45
    assert candidate(n = 202020202) == 10
    assert candidate(n = 135791357) == 9
    assert candidate(n = 975318642) == 1
    assert candidate(n = 505050505) == 25
    assert candidate(n = 999888777) == 8
    assert candidate(n = 135792468) == 9
    assert candidate(n = 99887766554433221100) == 0
    assert candidate(n = 246802468) == 0
    assert candidate(n = 123321123321) == 0
    assert candidate(n = 9753186420) == 1
    assert candidate(n = 121212121) == -3
    assert candidate(n = 5040302010) == 15
    assert candidate(n = 808080808) == 40
    assert candidate(n = 101010101) == 5
    assert candidate(n = 1212121212) == -5
    assert candidate(n = 4321234) == 5
    assert candidate(n = 8642086420) == 0
    assert candidate(n = 9876543210) == 5
    assert candidate(n = 112233445566778899) == 0
    assert candidate(n = 7654321) == 4
    assert candidate(n = 1122334455) == 0
    assert candidate(n = 555555555) == 5
    assert candidate(n = 864208642) == 0
    assert candidate(n = 1000000001) == 0
    assert candidate(n = 4321234321234) == 6
    assert candidate(n = 111111111) == 1
    assert candidate(n = 1010101010) == 5
    assert candidate(n = 2222222222) == 0
    assert candidate(n = 110011001) == 1
    assert candidate(n = 123321) == 0
    assert candidate(n = 246813579) == 1
    assert candidate(n = 123012301) == 5
    assert candidate(n = 543210987654) == 6
    assert candidate(n = 1357924680) == 9
    assert candidate(n = 543210987) == 11
    assert candidate(n = 1111111111) == 0


