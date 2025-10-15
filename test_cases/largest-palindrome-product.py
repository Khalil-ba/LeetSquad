def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 475: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 123: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 597
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 597: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 1218
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 1218: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 987
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 987: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 877
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 877: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 677
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 677: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 475
    assert candidate(n = 3) == 123
    assert candidate(n = 4) == 597
    assert candidate(n = 6) == 1218
    assert candidate(n = 2) == 987
    assert candidate(n = 1) == 9
    assert candidate(n = 7) == 877
    assert candidate(n = 5) == 677


