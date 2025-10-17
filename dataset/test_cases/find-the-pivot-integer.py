def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 625) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 576) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 576) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 729) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 144) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 900) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 324) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 324) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 841) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 841) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 289) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 289) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 550) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 484) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 484) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 225) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 784) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 784) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 250) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 169) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 169) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 256) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 529) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 529) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 676) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 676) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 48) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 325) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 325) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 441) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 441) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 961) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 961) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 400) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 196) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 196) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 121) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 361) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 361) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 700) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8) == 6
    assert candidate(n = 3) == -1
    assert candidate(n = 4) == -1
    assert candidate(n = 1) == 1
    assert candidate(n = 1000) == -1
    assert candidate(n = 10) == -1
    assert candidate(n = 625) == -1
    assert candidate(n = 576) == -1
    assert candidate(n = 729) == -1
    assert candidate(n = 144) == -1
    assert candidate(n = 49) == 35
    assert candidate(n = 12) == -1
    assert candidate(n = 900) == -1
    assert candidate(n = 324) == -1
    assert candidate(n = 100) == -1
    assert candidate(n = 50) == -1
    assert candidate(n = 5) == -1
    assert candidate(n = 841) == -1
    assert candidate(n = 289) == -1
    assert candidate(n = 550) == -1
    assert candidate(n = 99) == -1
    assert candidate(n = 64) == -1
    assert candidate(n = 17) == -1
    assert candidate(n = 484) == -1
    assert candidate(n = 2) == -1
    assert candidate(n = 225) == -1
    assert candidate(n = 784) == -1
    assert candidate(n = 250) == -1
    assert candidate(n = 999) == -1
    assert candidate(n = 35) == -1
    assert candidate(n = 169) == -1
    assert candidate(n = 75) == -1
    assert candidate(n = 256) == -1
    assert candidate(n = 36) == -1
    assert candidate(n = 529) == -1
    assert candidate(n = 20) == -1
    assert candidate(n = 676) == -1
    assert candidate(n = 81) == -1
    assert candidate(n = 48) == -1
    assert candidate(n = 325) == -1
    assert candidate(n = 15) == -1
    assert candidate(n = 441) == -1
    assert candidate(n = 961) == -1
    assert candidate(n = 400) == -1
    assert candidate(n = 196) == -1
    assert candidate(n = 9) == -1
    assert candidate(n = 121) == -1
    assert candidate(n = 361) == -1
    assert candidate(n = 700) == -1
    assert candidate(n = 500) == -1
    assert candidate(n = 7) == -1
    assert candidate(n = 25) == -1


