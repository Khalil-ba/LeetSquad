def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 99999) == 59004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 59004: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111) == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111) == -4: {e}')
    
    total += 1
    try:
        result = candidate(n = 789) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789) == 480: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111) == -3: {e}')
    
    total += 1
    try:
        result = candidate(n = 234) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 234) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345) == 105: {e}')
    
    total += 1
    try:
        result = candidate(n = 456) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 456) == 105: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 6525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 6525: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 105) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 105) == -6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4421) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4421) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 33333) == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33333) == 228: {e}')
    
    total += 1
    try:
        result = candidate(n = 199999) == 59003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199999) == 59003: {e}')
    
    total += 1
    try:
        result = candidate(n = 55555) == 3100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55555) == 3100: {e}')
    
    total += 1
    try:
        result = candidate(n = 10987) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10987) == -25: {e}')
    
    total += 1
    try:
        result = candidate(n = 77777) == 16772
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77777) == 16772: {e}')
    
    total += 1
    try:
        result = candidate(n = 67890) == -30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67890) == -30: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111) == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111) == -5: {e}')
    
    total += 1
    try:
        result = candidate(n = 86420) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 86420) == -20: {e}')
    
    total += 1
    try:
        result = candidate(n = 56789) == 15085
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789) == 15085: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888) == 262096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888) == 262096: {e}')
    
    total += 1
    try:
        result = candidate(n = 24680) == -20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24680) == -20: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654) == 60441
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654) == 60441: {e}')
    
    total += 1
    try:
        result = candidate(n = 59382) == 2133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59382) == 2133: {e}')
    
    total += 1
    try:
        result = candidate(n = 80808) == -24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80808) == -24: {e}')
    
    total += 1
    try:
        result = candidate(n = 50400) == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50400) == -9: {e}')
    
    total += 1
    try:
        result = candidate(n = 234567) == 5013
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 234567) == 5013: {e}')
    
    total += 1
    try:
        result = candidate(n = 44444) == 1004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44444) == 1004: {e}')
    
    total += 1
    try:
        result = candidate(n = 102030405) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 102030405) == -15: {e}')
    
    total += 1
    try:
        result = candidate(n = 59876) == 15085
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59876) == 15085: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10401) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10401) == -6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10101) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10101) == -3: {e}')
    
    total += 1
    try:
        result = candidate(n = 7654321) == 5012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7654321) == 5012: {e}')
    
    total += 1
    try:
        result = candidate(n = 29999) == 13084
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29999) == 13084: {e}')
    
    total += 1
    try:
        result = candidate(n = 22222) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22222) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 362835
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 362835: {e}')
    
    total += 1
    try:
        result = candidate(n = 13579) == 920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13579) == 920: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010) == -3: {e}')
    
    total += 1
    try:
        result = candidate(n = 90909) == -27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90909) == -27: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765) == 15085
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765) == 15085: {e}')
    
    total += 1
    try:
        result = candidate(n = 43210) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43210) == -10: {e}')
    
    total += 1
    try:
        result = candidate(n = 95135) == 652
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95135) == 652: {e}')
    
    total += 1
    try:
        result = candidate(n = 91123) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91123) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 314159) == 517
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 314159) == 517: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 531387
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 531387: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456) == 699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456) == 699: {e}')
    
    total += 1
    try:
        result = candidate(n = 10010) == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10010) == -2: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321) == 105: {e}')
    
    total += 1
    try:
        result = candidate(n = 505050) == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 505050) == -15: {e}')
    
    total += 1
    try:
        result = candidate(n = 76543) == 2495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 76543) == 2495: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 99999) == 59004
    assert candidate(n = 11111) == -4
    assert candidate(n = 789) == 480
    assert candidate(n = 1111) == -3
    assert candidate(n = 234) == 15
    assert candidate(n = 12345) == 105
    assert candidate(n = 456) == 105
    assert candidate(n = 10000) == -1
    assert candidate(n = 9999) == 6525
    assert candidate(n = 100) == -1
    assert candidate(n = 105) == -6
    assert candidate(n = 1000) == -1
    assert candidate(n = 4421) == 21
    assert candidate(n = 4321) == 14
    assert candidate(n = 123) == 0
    assert candidate(n = 33333) == 228
    assert candidate(n = 199999) == 59003
    assert candidate(n = 55555) == 3100
    assert candidate(n = 10987) == -25
    assert candidate(n = 77777) == 16772
    assert candidate(n = 67890) == -30
    assert candidate(n = 111111) == -5
    assert candidate(n = 86420) == -20
    assert candidate(n = 56789) == 15085
    assert candidate(n = 888888) == 262096
    assert candidate(n = 24680) == -20
    assert candidate(n = 987654) == 60441
    assert candidate(n = 59382) == 2133
    assert candidate(n = 80808) == -24
    assert candidate(n = 50400) == -9
    assert candidate(n = 234567) == 5013
    assert candidate(n = 44444) == 1004
    assert candidate(n = 102030405) == -15
    assert candidate(n = 59876) == 15085
    assert candidate(n = 100000) == -1
    assert candidate(n = 10401) == -6
    assert candidate(n = 10101) == -3
    assert candidate(n = 7654321) == 5012
    assert candidate(n = 29999) == 13084
    assert candidate(n = 22222) == 22
    assert candidate(n = 987654321) == 362835
    assert candidate(n = 13579) == 920
    assert candidate(n = 101010) == -3
    assert candidate(n = 90909) == -27
    assert candidate(n = 98765) == 15085
    assert candidate(n = 43210) == -10
    assert candidate(n = 95135) == 652
    assert candidate(n = 91123) == 38
    assert candidate(n = 314159) == 517
    assert candidate(n = 999999) == 531387
    assert candidate(n = 123456) == 699
    assert candidate(n = 10010) == -2
    assert candidate(n = 54321) == 105
    assert candidate(n = 505050) == -15
    assert candidate(n = 76543) == 2495


