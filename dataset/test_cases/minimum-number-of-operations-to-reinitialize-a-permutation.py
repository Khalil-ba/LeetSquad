def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 166: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 896) == 356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 896) == 356: {e}')
    
    total += 1
    try:
        result = candidate(n = 992) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 992) == 495: {e}')
    
    total += 1
    try:
        result = candidate(n = 988) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 988) == 138: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 132: {e}')
    
    total += 1
    try:
        result = candidate(n = 384) == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 384) == 191: {e}')
    
    total += 1
    try:
        result = candidate(n = 600) == 299
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600) == 299: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 72) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 192) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 192) == 95: {e}')
    
    total += 1
    try:
        result = candidate(n = 888) == 443
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888) == 443: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 128) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 46) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 768) == 348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 768) == 348: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 48) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 800) == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800) == 184: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 99: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 512) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 512) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 750) == 318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750) == 318: {e}')
    
    total += 1
    try:
        result = candidate(n = 998) == 332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 998) == 332: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 3
    assert candidate(n = 4) == 2
    assert candidate(n = 12) == 10
    assert candidate(n = 14) == 12
    assert candidate(n = 16) == 4
    assert candidate(n = 18) == 8
    assert candidate(n = 6) == 4
    assert candidate(n = 2) == 1
    assert candidate(n = 20) == 18
    assert candidate(n = 100) == 30
    assert candidate(n = 500) == 166
    assert candidate(n = 1000) == 36
    assert candidate(n = 10) == 6
    assert candidate(n = 896) == 356
    assert candidate(n = 992) == 495
    assert candidate(n = 988) == 138
    assert candidate(n = 50) == 21
    assert candidate(n = 300) == 132
    assert candidate(n = 384) == 191
    assert candidate(n = 600) == 299
    assert candidate(n = 64) == 6
    assert candidate(n = 72) == 35
    assert candidate(n = 192) == 95
    assert candidate(n = 888) == 443
    assert candidate(n = 1024) == 10
    assert candidate(n = 128) == 7
    assert candidate(n = 22) == 6
    assert candidate(n = 46) == 12
    assert candidate(n = 256) == 8
    assert candidate(n = 768) == 348
    assert candidate(n = 32) == 5
    assert candidate(n = 48) == 23
    assert candidate(n = 800) == 184
    assert candidate(n = 200) == 99
    assert candidate(n = 400) == 18
    assert candidate(n = 512) == 9
    assert candidate(n = 750) == 318
    assert candidate(n = 998) == 332


