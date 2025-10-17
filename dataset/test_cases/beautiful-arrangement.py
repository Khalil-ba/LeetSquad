def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 132: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 750: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 24679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 24679: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 4010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 4010: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 10680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 10680: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 4237
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 4237: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 700: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 132
    assert candidate(n = 3) == 3
    assert candidate(n = 11) == 750
    assert candidate(n = 15) == 24679
    assert candidate(n = 4) == 8
    assert candidate(n = 12) == 4010
    assert candidate(n = 14) == 10680
    assert candidate(n = 9) == 250
    assert candidate(n = 13) == 4237
    assert candidate(n = 6) == 36
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 7) == 41
    assert candidate(n = 10) == 700
    assert candidate(n = 5) == 10


