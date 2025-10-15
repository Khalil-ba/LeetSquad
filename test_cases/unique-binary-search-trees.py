def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 1767263190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 1767263190: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 16796
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 16796: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 1430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 1430: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 9694845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 9694845: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 208012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 208012: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 477638700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 477638700: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 4862
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 4862: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 132: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 429: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 5
    assert candidate(n = 4) == 14
    assert candidate(n = 19) == 1767263190
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 16796
    assert candidate(n = 5) == 42
    assert candidate(n = 8) == 1430
    assert candidate(n = 15) == 9694845
    assert candidate(n = 12) == 208012
    assert candidate(n = 18) == 477638700
    assert candidate(n = 9) == 4862
    assert candidate(n = 6) == 132
    assert candidate(n = 2) == 2
    assert candidate(n = 7) == 429


