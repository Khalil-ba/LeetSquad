def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "7777777777777777") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "7777777777777777") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "666666666666666") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "666666666666666") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "111111") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "111111") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "999999999999999999") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "999999999999999999") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "55555555555555") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "55555555555555") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "00011111222") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00011111222") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "11") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "11") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "3333333333") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3333333333") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "011100022233") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "011100022233") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "000111000") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000111000") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "88888888888888888") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "88888888888888888") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "22222222") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "22222222") == True: {e}')
    
    total += 1
    try:
        result = candidate(s = "444444444444") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "444444444444") == False: {e}')
    
    total += 1
    try:
        result = candidate(s = "122111") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "122111") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "7777777777777777") == False
    assert candidate(s = "666666666666666") == False
    assert candidate(s = "111111") == False
    assert candidate(s = "999999999999999999") == False
    assert candidate(s = "55555555555555") == True
    assert candidate(s = "00011111222") == True
    assert candidate(s = "11") == True
    assert candidate(s = "3333333333") == False
    assert candidate(s = "011100022233") == False
    assert candidate(s = "000111000") == False
    assert candidate(s = "88888888888888888") == True
    assert candidate(s = "22222222") == True
    assert candidate(s = "444444444444") == False
    assert candidate(s = "122111") == False


