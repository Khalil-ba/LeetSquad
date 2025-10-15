def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 324: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 129744
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 129744: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 63504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 63504: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 256: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 28: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 324
    assert candidate(n = 3) == 3
    assert candidate(n = 11) == 129744
    assert candidate(n = 4) == 4
    assert candidate(n = 12) == 63504
    assert candidate(n = 9) == 3600
    assert candidate(n = 6) == 16
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 1
    assert candidate(n = 7) == 256
    assert candidate(n = 10) == 3600
    assert candidate(n = 5) == 28


