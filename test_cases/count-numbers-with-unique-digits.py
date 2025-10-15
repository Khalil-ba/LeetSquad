def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 2345851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 2345851: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 739
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 739: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 5275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 5275: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 168571
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 168571: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 91: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 712891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 712891: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 32491
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 32491: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 5611771
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 5611771: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 8877691
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 8877691: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 1
    assert candidate(n = 8) == 2345851
    assert candidate(n = 3) == 739
    assert candidate(n = 4) == 5275
    assert candidate(n = 6) == 168571
    assert candidate(n = 2) == 91
    assert candidate(n = 1) == 10
    assert candidate(n = 7) == 712891
    assert candidate(n = 5) == 32491
    assert candidate(n = 9) == 5611771
    assert candidate(n = 10) == 8877691


