def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 985598218
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 985598218: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 3536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 3536: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 94: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 100469819
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 100469819: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 921822362
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 921822362: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 43: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 2947811
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 2947811: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 110821862
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 110821862: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 19
    assert candidate(n = 100) == 985598218
    assert candidate(n = 2) == 8
    assert candidate(n = 1) == 3
    assert candidate(n = 10) == 3536
    assert candidate(n = 5) == 94
    assert candidate(n = 50) == 100469819
    assert candidate(n = 300) == 921822362
    assert candidate(n = 4) == 43
    assert candidate(n = 20) == 2947811
    assert candidate(n = 200) == 110821862


