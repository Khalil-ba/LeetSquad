def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 88) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 3) == 2
    assert candidate(n = 100) == 21
    assert candidate(n = 99) == 21
    assert candidate(n = 2) == 1
    assert candidate(n = 20) == 7
    assert candidate(n = 1) == 1
    assert candidate(n = 50) == 13
    assert candidate(n = 7) == 3
    assert candidate(n = 10) == 4
    assert candidate(n = 88) == 21
    assert candidate(n = 97) == 21
    assert candidate(n = 63) == 13
    assert candidate(n = 45) == 13
    assert candidate(n = 49) == 13
    assert candidate(n = 47) == 13
    assert candidate(n = 60) == 13
    assert candidate(n = 64) == 13
    assert candidate(n = 37) == 11
    assert candidate(n = 17) == 5
    assert candidate(n = 42) == 11
    assert candidate(n = 90) == 21
    assert candidate(n = 22) == 8
    assert candidate(n = 89) == 21
    assert candidate(n = 75) == 18
    assert candidate(n = 81) == 18
    assert candidate(n = 24) == 8
    assert candidate(n = 11) == 5
    assert candidate(n = 15) == 5
    assert candidate(n = 31) == 8
    assert candidate(n = 25) == 8


