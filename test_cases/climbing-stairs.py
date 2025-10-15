def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 1836311903
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 1836311903: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 10946
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 10946: {e}')
    
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
        result = candidate(n = 10) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 89: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 1346269
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 1346269: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 987
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 987: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 165580141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 165580141: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 233: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 14930352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 14930352: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 4181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 4181: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 121393
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 121393: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 3
    assert candidate(n = 45) == 1836311903
    assert candidate(n = 4) == 5
    assert candidate(n = 20) == 10946
    assert candidate(n = 2) == 2
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 89
    assert candidate(n = 5) == 8
    assert candidate(n = 30) == 1346269
    assert candidate(n = 15) == 987
    assert candidate(n = 40) == 165580141
    assert candidate(n = 12) == 233
    assert candidate(n = 35) == 14930352
    assert candidate(n = 18) == 4181
    assert candidate(n = 7) == 21
    assert candidate(n = 25) == 121393


