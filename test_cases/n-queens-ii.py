def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 92: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 352: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 40: {e}')
    
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
    assert candidate(n = 8) == 92
    assert candidate(n = 3) == 0
    assert candidate(n = 4) == 2
    assert candidate(n = 9) == 352
    assert candidate(n = 6) == 4
    assert candidate(n = 2) == 0
    assert candidate(n = 1) == 1
    assert candidate(n = 7) == 40
    assert candidate(n = 5) == 10


