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
        result = candidate(n = 30) == 832040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 832040: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 6765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 6765: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 514229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 514229: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 610: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 144: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 2584
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 2584: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 75025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 75025: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 317811
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 317811: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 3) == 2
    assert candidate(n = 30) == 832040
    assert candidate(n = 4) == 3
    assert candidate(n = 2) == 1
    assert candidate(n = 20) == 6765
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 55
    assert candidate(n = 5) == 5
    assert candidate(n = 8) == 21
    assert candidate(n = 29) == 514229
    assert candidate(n = 15) == 610
    assert candidate(n = 12) == 144
    assert candidate(n = 18) == 2584
    assert candidate(n = 6) == 8
    assert candidate(n = 25) == 75025
    assert candidate(n = 28) == 317811


