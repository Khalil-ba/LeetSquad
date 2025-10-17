def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 250) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == 330: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == 254
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == 254: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 104: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == 178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == 178: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 78: {e}')
    
    total += 1
    try:
        result = candidate(n = 230) == 302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 230) == 302: {e}')
    
    total += 1
    try:
        result = candidate(n = 125) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125) == 142: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 240) == 314
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 240) == 314: {e}')
    
    total += 1
    try:
        result = candidate(n = 199) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 199) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 120) == 132
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120) == 132: {e}')
    
    total += 1
    try:
        result = candidate(n = 225) == 296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225) == 296: {e}')
    
    total += 1
    try:
        result = candidate(n = 249) == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 249) == 324: {e}')
    
    total += 1
    try:
        result = candidate(n = 190) == 236
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 190) == 236: {e}')
    
    total += 1
    try:
        result = candidate(n = 175) == 214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 175) == 214: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == 218
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == 218: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 250) == 330
    assert candidate(n = 5) == 2
    assert candidate(n = 15) == 8
    assert candidate(n = 200) == 254
    assert candidate(n = 20) == 12
    assert candidate(n = 100) == 104
    assert candidate(n = 50) == 40
    assert candidate(n = 1) == 0
    assert candidate(n = 10) == 4
    assert candidate(n = 25) == 16
    assert candidate(n = 150) == 178
    assert candidate(n = 80) == 78
    assert candidate(n = 230) == 302
    assert candidate(n = 125) == 142
    assert candidate(n = 75) == 74
    assert candidate(n = 240) == 314
    assert candidate(n = 199) == 250
    assert candidate(n = 120) == 132
    assert candidate(n = 225) == 296
    assert candidate(n = 249) == 324
    assert candidate(n = 190) == 236
    assert candidate(n = 175) == 214
    assert candidate(n = 180) == 218


