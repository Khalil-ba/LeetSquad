def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 17711
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 17711: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == 2178309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == 2178309: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 144: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == 2178309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == 2178309: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888) == 2178309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888) == 2178309: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333) == 1149851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333) == 1149851: {e}')
    
    total += 1
    try:
        result = candidate(n = 777777777) == 2178309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 777777777) == 2178309: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999) == 2178309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999) == 2178309: {e}')
    
    total += 1
    try:
        result = candidate(n = 110011001) == 514229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 110011001) == 514229: {e}')
    
    total += 1
    try:
        result = candidate(n = 314159265) == 1149851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 314159265) == 1149851: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000) == 1346269
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000) == 1346269: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == 3524578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == 3524578: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == 514229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == 514229: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555) == 1496319
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555) == 1496319: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101) == 514229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101) == 514229: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000001) == 2178309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000001) == 2178309: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == 514229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == 514229: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == 514229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == 514229: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000) == 2178309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000) == 2178309: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100) == 34
    assert candidate(n = 15) == 8
    assert candidate(n = 1000000) == 17711
    assert candidate(n = 32) == 14
    assert candidate(n = 2) == 3
    assert candidate(n = 1) == 2
    assert candidate(n = 1000000000) == 2178309
    assert candidate(n = 1000) == 144
    assert candidate(n = 10) == 8
    assert candidate(n = 5) == 5
    assert candidate(n = 987654321) == 2178309
    assert candidate(n = 888888888) == 2178309
    assert candidate(n = 333333333) == 1149851
    assert candidate(n = 777777777) == 2178309
    assert candidate(n = 999999999) == 2178309
    assert candidate(n = 110011001) == 514229
    assert candidate(n = 314159265) == 1149851
    assert candidate(n = 500000000) == 1346269
    assert candidate(n = 2147483647) == 3524578
    assert candidate(n = 123456789) == 514229
    assert candidate(n = 555555555) == 1496319
    assert candidate(n = 101010101) == 514229
    assert candidate(n = 1000000001) == 2178309
    assert candidate(n = 100000000) == 514229
    assert candidate(n = 111111111) == 514229
    assert candidate(n = 800000000) == 2178309


