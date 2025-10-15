def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 101) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 300) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 123) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 169) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 169) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 150) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 180) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 180) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 101) == True
    assert candidate(n = 3) == True
    assert candidate(n = 100) == True
    assert candidate(n = 30) == True
    assert candidate(n = 5) == False
    assert candidate(n = 4) == True
    assert candidate(n = 200) == True
    assert candidate(n = 17) == False
    assert candidate(n = 2) == False
    assert candidate(n = 20) == False
    assert candidate(n = 1) == True
    assert candidate(n = 7) == False
    assert candidate(n = 10) == False
    assert candidate(n = 25) == True
    assert candidate(n = 50) == True
    assert candidate(n = 300) == True
    assert candidate(n = 123) == True
    assert candidate(n = 64) == True
    assert candidate(n = 16) == True
    assert candidate(n = 169) == True
    assert candidate(n = 81) == True
    assert candidate(n = 150) == False
    assert candidate(n = 55) == True
    assert candidate(n = 180) == False


