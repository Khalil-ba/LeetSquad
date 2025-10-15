def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == 66045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == 66045: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 10626
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 10626: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 316251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 316251: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 1001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 1001: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 126: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 211876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 211876: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 292825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 292825: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 1820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 1820: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 35960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 35960: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 46376
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 46376: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 135751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 135751: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 495: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == 14950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == 14950: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == 31465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == 31465: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == 82251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == 82251: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 3876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 3876: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 715
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 715: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 330: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 23751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 23751: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 35
    assert candidate(n = 4) == 70
    assert candidate(n = 33) == 66045
    assert candidate(n = 2) == 15
    assert candidate(n = 20) == 10626
    assert candidate(n = 1) == 5
    assert candidate(n = 50) == 316251
    assert candidate(n = 10) == 1001
    assert candidate(n = 5) == 126
    assert candidate(n = 45) == 211876
    assert candidate(n = 49) == 292825
    assert candidate(n = 12) == 1820
    assert candidate(n = 28) == 35960
    assert candidate(n = 30) == 46376
    assert candidate(n = 40) == 135751
    assert candidate(n = 8) == 495
    assert candidate(n = 22) == 14950
    assert candidate(n = 27) == 31465
    assert candidate(n = 35) == 82251
    assert candidate(n = 15) == 3876
    assert candidate(n = 9) == 715
    assert candidate(n = 6) == 210
    assert candidate(n = 7) == 330
    assert candidate(n = 25) == 23751


