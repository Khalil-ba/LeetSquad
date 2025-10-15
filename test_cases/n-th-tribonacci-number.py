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
        result = candidate(n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 2082876103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 2082876103: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 1389537
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 1389537: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 29249425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 29249425: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 3136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 3136: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 223317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 223317: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 504: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 615693474
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 615693474: {e}')
    
    total += 1
    try:
        result = candidate(n = 26) == 2555757
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26) == 2555757: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == 4700770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == 4700770: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 19513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 19513: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 66012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 66012: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 149: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 0) == 0
    assert candidate(n = 3) == 2
    assert candidate(n = 4) == 4
    assert candidate(n = 37) == 2082876103
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 1
    assert candidate(n = 25) == 1389537
    assert candidate(n = 30) == 29249425
    assert candidate(n = 15) == 3136
    assert candidate(n = 22) == 223317
    assert candidate(n = 12) == 504
    assert candidate(n = 35) == 615693474
    assert candidate(n = 26) == 2555757
    assert candidate(n = 27) == 4700770
    assert candidate(n = 18) == 19513
    assert candidate(n = 20) == 66012
    assert candidate(n = 10) == 149
    assert candidate(n = 5) == 7


