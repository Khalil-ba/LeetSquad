def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10001) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10001) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 250000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 101) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 50001) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50001) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 99998) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99998) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100001) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100001) == 0.5: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 0.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 0.5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 0.5
    assert candidate(n = 100000) == 0.5
    assert candidate(n = 100) == 0.5
    assert candidate(n = 10000) == 0.5
    assert candidate(n = 2) == 0.5
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 0.5
    assert candidate(n = 10) == 0.5
    assert candidate(n = 99999) == 0.5
    assert candidate(n = 2000) == 0.5
    assert candidate(n = 50000) == 0.5
    assert candidate(n = 50) == 0.5
    assert candidate(n = 5) == 0.5
    assert candidate(n = 10001) == 0.5
    assert candidate(n = 250000) == 0.5
    assert candidate(n = 4) == 0.5
    assert candidate(n = 750000) == 0.5
    assert candidate(n = 1001) == 0.5
    assert candidate(n = 200000) == 0.5
    assert candidate(n = 101) == 0.5
    assert candidate(n = 20000) == 0.5
    assert candidate(n = 5000) == 0.5
    assert candidate(n = 20) == 0.5
    assert candidate(n = 9999) == 0.5
    assert candidate(n = 50001) == 0.5
    assert candidate(n = 2500) == 0.5
    assert candidate(n = 500000) == 0.5
    assert candidate(n = 200) == 0.5
    assert candidate(n = 99998) == 0.5
    assert candidate(n = 1000000) == 0.5
    assert candidate(n = 100001) == 0.5
    assert candidate(n = 500) == 0.5


