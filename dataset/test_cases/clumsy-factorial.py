def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == 10001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == 10001: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000) == 5001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000) == 5001: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999) == 9998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999) == 9998: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000) == 2001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000) == 2001: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500) == 7501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500) == 7501: {e}')
    
    total += 1
    try:
        result = candidate(n = 104) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 104) == 105: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 52: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == 301: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 98: {e}')
    
    total += 1
    try:
        result = candidate(n = 6666) == 6668
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6666) == 6668: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == 998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == 998: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 7777) == 7779
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7777) == 7779: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == 501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == 501: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 27: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 9
    assert candidate(n = 3) == 6
    assert candidate(n = 100) == 101
    assert candidate(n = 4) == 7
    assert candidate(n = 10000) == 10001
    assert candidate(n = 9) == 11
    assert candidate(n = 5000) == 5001
    assert candidate(n = 6) == 8
    assert candidate(n = 2) == 2
    assert candidate(n = 9999) == 9998
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == 1001
    assert candidate(n = 7) == 6
    assert candidate(n = 10) == 12
    assert candidate(n = 5) == 7
    assert candidate(n = 12) == 13
    assert candidate(n = 21) == 23
    assert candidate(n = 2000) == 2001
    assert candidate(n = 7500) == 7501
    assert candidate(n = 104) == 105
    assert candidate(n = 50) == 52
    assert candidate(n = 300) == 301
    assert candidate(n = 28) == 29
    assert candidate(n = 30) == 32
    assert candidate(n = 99) == 98
    assert candidate(n = 6666) == 6668
    assert candidate(n = 17) == 19
    assert candidate(n = 999) == 998
    assert candidate(n = 18) == 20
    assert candidate(n = 20) == 21
    assert candidate(n = 24) == 25
    assert candidate(n = 7777) == 7779
    assert candidate(n = 11) == 10
    assert candidate(n = 15) == 14
    assert candidate(n = 14) == 16
    assert candidate(n = 31) == 30
    assert candidate(n = 500) == 501
    assert candidate(n = 25) == 27


