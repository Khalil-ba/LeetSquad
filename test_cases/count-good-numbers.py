def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 400: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 564908303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 564908303: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1) == 5
    assert candidate(n = 4) == 400
    assert candidate(n = 50) == 564908303


