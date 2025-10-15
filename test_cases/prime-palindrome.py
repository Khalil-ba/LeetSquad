def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 101) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 101: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000000) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000000) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 10007) == 10301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10007) == 10301: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 10301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 10301: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 999983) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999983) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 9989900) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9989900) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 100030001) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100030001) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 10301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 10301: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000000) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000000) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 101: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345678) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345678) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 789789789) == 789868987
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789789789) == 789868987: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999999) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999999) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 66666666) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 66666666) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000001) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000001) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 12321) == 12421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12321) == 12421: {e}')
    
    total += 1
    try:
        result = candidate(n = 10111011101) == 10111311101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10111011101) == 10111311101: {e}')
    
    total += 1
    try:
        result = candidate(n = 80000000) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80000000) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 8999998) == 9002009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8999998) == 9002009: {e}')
    
    total += 1
    try:
        result = candidate(n = 75000000) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75000000) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 1003001) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1003001) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 899989) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 899989) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000000) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000000) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 100003) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100003) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 98765432) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98765432) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 55555555) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55555555) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 10301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 10301: {e}')
    
    total += 1
    try:
        result = candidate(n = 90000000) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90000000) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 111181111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 111181111: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 987757789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 987757789: {e}')
    
    total += 1
    try:
        result = candidate(n = 9988999) == 9989899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9988999) == 9989899: {e}')
    
    total += 1
    try:
        result = candidate(n = 998899) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 998899) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 150000000) == 150070051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150000000) == 150070051: {e}')
    
    total += 1
    try:
        result = candidate(n = 11111111) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11111111) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 88888888) == 100030001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88888888) == 100030001: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 123484321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 123484321: {e}')
    
    total += 1
    try:
        result = candidate(n = 989) == 10301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 989) == 10301: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000001) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000001) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567) == 1235321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567) == 1235321: {e}')
    
    total += 1
    try:
        result = candidate(n = 100001) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100001) == 1003001: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000003) == 1003001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000003) == 1003001: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 101) == 101
    assert candidate(n = 8) == 11
    assert candidate(n = 10000000) == 100030001
    assert candidate(n = 10007) == 10301
    assert candidate(n = 999) == 10301
    assert candidate(n = 6) == 7
    assert candidate(n = 999983) == 1003001
    assert candidate(n = 2) == 2
    assert candidate(n = 100000000) == 100030001
    assert candidate(n = 9989900) == 100030001
    assert candidate(n = 100030001) == 100030001
    assert candidate(n = 100) == 101
    assert candidate(n = 10) == 11
    assert candidate(n = 1000) == 10301
    assert candidate(n = 20000000) == 100030001
    assert candidate(n = 1) == 2
    assert candidate(n = 13) == 101
    assert candidate(n = 12345678) == 100030001
    assert candidate(n = 99999) == 1003001
    assert candidate(n = 789789789) == 789868987
    assert candidate(n = 9999999) == 100030001
    assert candidate(n = 66666666) == 100030001
    assert candidate(n = 100000001) == 100030001
    assert candidate(n = 12321) == 12421
    assert candidate(n = 10111011101) == 10111311101
    assert candidate(n = 80000000) == 100030001
    assert candidate(n = 8999998) == 9002009
    assert candidate(n = 75000000) == 100030001
    assert candidate(n = 1003001) == 1003001
    assert candidate(n = 899989) == 1003001
    assert candidate(n = 50000000) == 100030001
    assert candidate(n = 100003) == 1003001
    assert candidate(n = 98765432) == 100030001
    assert candidate(n = 99999999) == 100030001
    assert candidate(n = 55555555) == 100030001
    assert candidate(n = 9999) == 10301
    assert candidate(n = 90000000) == 100030001
    assert candidate(n = 111111111) == 111181111
    assert candidate(n = 987654321) == 987757789
    assert candidate(n = 9988999) == 9989899
    assert candidate(n = 998899) == 1003001
    assert candidate(n = 150000000) == 150070051
    assert candidate(n = 11111111) == 100030001
    assert candidate(n = 1000000) == 1003001
    assert candidate(n = 88888888) == 100030001
    assert candidate(n = 123456789) == 123484321
    assert candidate(n = 989) == 10301
    assert candidate(n = 1000001) == 1003001
    assert candidate(n = 999999) == 1003001
    assert candidate(n = 1234567) == 1235321
    assert candidate(n = 100001) == 1003001
    assert candidate(n = 1000003) == 1003001


