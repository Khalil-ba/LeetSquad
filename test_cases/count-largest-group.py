def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 200) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 104) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2345) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2345) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4096) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4096) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4567) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4567) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8888) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8888) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 333) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 888) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8192) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8192) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5555) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5555) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6543) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6543) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7865) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7865) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7777) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7777) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4999) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4999) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 200) == 2
    assert candidate(n = 10000) == 1
    assert candidate(n = 9) == 9
    assert candidate(n = 104) == 1
    assert candidate(n = 9999) == 1
    assert candidate(n = 2) == 2
    assert candidate(n = 100) == 1
    assert candidate(n = 1000) == 2
    assert candidate(n = 13) == 4
    assert candidate(n = 25) == 6
    assert candidate(n = 4000) == 1
    assert candidate(n = 2345) == 1
    assert candidate(n = 1111) == 1
    assert candidate(n = 7000) == 2
    assert candidate(n = 4096) == 1
    assert candidate(n = 7500) == 1
    assert candidate(n = 4567) == 1
    assert candidate(n = 2000) == 1
    assert candidate(n = 111) == 1
    assert candidate(n = 8888) == 1
    assert candidate(n = 300) == 1
    assert candidate(n = 333) == 2
    assert candidate(n = 3000) == 2
    assert candidate(n = 99) == 1
    assert candidate(n = 888) == 1
    assert candidate(n = 1024) == 2
    assert candidate(n = 8192) == 1
    assert candidate(n = 999) == 2
    assert candidate(n = 5555) == 1
    assert candidate(n = 8000) == 1
    assert candidate(n = 5000) == 2
    assert candidate(n = 6543) == 1
    assert candidate(n = 7865) == 1
    assert candidate(n = 7777) == 1
    assert candidate(n = 2222) == 1
    assert candidate(n = 2500) == 1
    assert candidate(n = 9000) == 2
    assert candidate(n = 4999) == 2
    assert candidate(n = 3999) == 1
    assert candidate(n = 1234) == 1
    assert candidate(n = 6000) == 1
    assert candidate(n = 1) == 1
    assert candidate(n = 500) == 1
    assert candidate(n = 10) == 1
    assert candidate(n = 1500) == 1


