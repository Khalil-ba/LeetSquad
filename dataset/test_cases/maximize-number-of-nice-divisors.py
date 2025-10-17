def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(primeFactors = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeFactors = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(primeFactors = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeFactors = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(primeFactors = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeFactors = 2) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(primeFactors = 1) == 1
    assert candidate(primeFactors = 3) == 3
    assert candidate(primeFactors = 2) == 2


