def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 700) == 1660140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700) == 1660140: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 3353149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 3353149: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 41334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 41334: {e}')
    
    total += 1
    try:
        result = candidate(n = 600) == 772866
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600) == 772866: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 1478
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 1478: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 41334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 41334: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 601470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 601470: {e}')
    
    total += 1
    try:
        result = candidate(n = 900) == 3353149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900) == 3353149: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 82: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 182: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 772866
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 772866: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 10804657
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 10804657: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 182: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 184768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 184768: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 3503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 3503: {e}')
    
    total += 1
    try:
        result = candidate(n = 625) == 772866
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == 772866: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 9804657
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 9804657: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 2154349
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 2154349: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 41334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 41334: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 700) == 1660140
    assert candidate(n = 800) == 3353149
    assert candidate(n = 100) == 41334
    assert candidate(n = 600) == 772866
    assert candidate(n = 37) == 1478
    assert candidate(n = 200) == 41334
    assert candidate(n = 400) == 601470
    assert candidate(n = 900) == 3353149
    assert candidate(n = 9) == 82
    assert candidate(n = 2) == 1
    assert candidate(n = 25) == 182
    assert candidate(n = 1) == 1
    assert candidate(n = 500) == 772866
    assert candidate(n = 1000) == 10804657
    assert candidate(n = 10) == 182
    assert candidate(n = 300) == 184768
    assert candidate(n = 50) == 3503
    assert candidate(n = 625) == 772866
    assert candidate(n = 999) == 9804657
    assert candidate(n = 750) == 2154349
    assert candidate(n = 150) == 41334


