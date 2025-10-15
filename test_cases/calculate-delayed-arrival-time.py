def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arrivalTime = 5,delayedTime = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 5,delayedTime = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 8,delayedTime = 16) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 8,delayedTime = 16) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 13,delayedTime = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 13,delayedTime = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 15,delayedTime = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 15,delayedTime = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 1,delayedTime = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 1,delayedTime = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 12,delayedTime = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 12,delayedTime = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 1,delayedTime = 23) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 1,delayedTime = 23) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 0,delayedTime = 24) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 0,delayedTime = 24) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 23,delayedTime = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 23,delayedTime = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 5,delayedTime = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 5,delayedTime = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 19,delayedTime = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 19,delayedTime = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 18,delayedTime = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 18,delayedTime = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 2,delayedTime = 22) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 2,delayedTime = 22) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 20,delayedTime = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 20,delayedTime = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 3,delayedTime = 21) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 3,delayedTime = 21) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 20,delayedTime = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 20,delayedTime = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 6,delayedTime = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 6,delayedTime = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 9,delayedTime = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 9,delayedTime = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 17,delayedTime = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 17,delayedTime = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 7,delayedTime = 17) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 7,delayedTime = 17) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 20,delayedTime = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 20,delayedTime = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 7,delayedTime = 18) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 7,delayedTime = 18) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 18,delayedTime = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 18,delayedTime = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 15,delayedTime = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 15,delayedTime = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 10,delayedTime = 14) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 10,delayedTime = 14) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 19,delayedTime = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 19,delayedTime = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 20,delayedTime = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 20,delayedTime = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 16,delayedTime = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 16,delayedTime = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 11,delayedTime = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 11,delayedTime = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 17,delayedTime = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 17,delayedTime = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(arrivalTime = 14,delayedTime = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arrivalTime = 14,delayedTime = 10) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arrivalTime = 5,delayedTime = 19) == 0
    assert candidate(arrivalTime = 8,delayedTime = 16) == 0
    assert candidate(arrivalTime = 13,delayedTime = 11) == 0
    assert candidate(arrivalTime = 15,delayedTime = 5) == 20
    assert candidate(arrivalTime = 1,delayedTime = 1) == 2
    assert candidate(arrivalTime = 12,delayedTime = 12) == 0
    assert candidate(arrivalTime = 1,delayedTime = 23) == 0
    assert candidate(arrivalTime = 0,delayedTime = 24) == 0
    assert candidate(arrivalTime = 23,delayedTime = 2) == 1
    assert candidate(arrivalTime = 5,delayedTime = 20) == 1
    assert candidate(arrivalTime = 19,delayedTime = 5) == 0
    assert candidate(arrivalTime = 18,delayedTime = 6) == 0
    assert candidate(arrivalTime = 2,delayedTime = 22) == 0
    assert candidate(arrivalTime = 20,delayedTime = 4) == 0
    assert candidate(arrivalTime = 3,delayedTime = 21) == 0
    assert candidate(arrivalTime = 20,delayedTime = 5) == 1
    assert candidate(arrivalTime = 6,delayedTime = 18) == 0
    assert candidate(arrivalTime = 9,delayedTime = 15) == 0
    assert candidate(arrivalTime = 17,delayedTime = 8) == 1
    assert candidate(arrivalTime = 7,delayedTime = 17) == 0
    assert candidate(arrivalTime = 20,delayedTime = 8) == 4
    assert candidate(arrivalTime = 7,delayedTime = 18) == 1
    assert candidate(arrivalTime = 18,delayedTime = 7) == 1
    assert candidate(arrivalTime = 15,delayedTime = 9) == 0
    assert candidate(arrivalTime = 10,delayedTime = 14) == 0
    assert candidate(arrivalTime = 19,delayedTime = 6) == 1
    assert candidate(arrivalTime = 20,delayedTime = 6) == 2
    assert candidate(arrivalTime = 16,delayedTime = 8) == 0
    assert candidate(arrivalTime = 11,delayedTime = 14) == 1
    assert candidate(arrivalTime = 17,delayedTime = 7) == 0
    assert candidate(arrivalTime = 14,delayedTime = 10) == 0


