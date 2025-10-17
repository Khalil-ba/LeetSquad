def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 10,limit = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,limit = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,limit = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,limit = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,limit = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,limit = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,limit = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,limit = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,limit = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,limit = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,limit = 4) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,limit = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,limit = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,limit = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,limit = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,limit = 10) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,limit = 10) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,limit = 15) == 186
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,limit = 15) == 186: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 50) == 1326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 50) == 1326: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,limit = 10) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,limit = 10) == 91: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,limit = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,limit = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,limit = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,limit = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,limit = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,limit = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,limit = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 31,limit = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31,limit = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 42,limit = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42,limit = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,limit = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,limit = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,limit = 15) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,limit = 15) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 32,limit = 11) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32,limit = 11) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 32,limit = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32,limit = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,limit = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,limit = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 20) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 20) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,limit = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,limit = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,limit = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,limit = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,limit = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,limit = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,limit = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,limit = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 33,limit = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33,limit = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,limit = 7) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,limit = 7) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 25) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 25) == 351: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,limit = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,limit = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 37,limit = 18) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37,limit = 18) == 171: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,limit = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,limit = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,limit = 17) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,limit = 17) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,limit = 20) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,limit = 20) == 231: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,limit = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 38,limit = 19) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 38,limit = 19) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 33,limit = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33,limit = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,limit = 25) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,limit = 25) == 375: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,limit = 12) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,limit = 12) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,limit = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,limit = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 42,limit = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42,limit = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,limit = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,limit = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,limit = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,limit = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,limit = 16) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,limit = 16) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,limit = 20) == 331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,limit = 20) == 331: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,limit = 20) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,limit = 20) == 136: {e}')
    
    total += 1
    try:
        result = candidate(n = 48,limit = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48,limit = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,limit = 14) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,limit = 14) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,limit = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,limit = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,limit = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,limit = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,limit = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,limit = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,limit = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,limit = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,limit = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,limit = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,limit = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,limit = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 33,limit = 11) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33,limit = 11) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,limit = 18) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,limit = 18) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,limit = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,limit = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,limit = 20) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 20) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,limit = 11) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,limit = 11) == 78: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,limit = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,limit = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,limit = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,limit = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,limit = 10) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,limit = 10) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 42,limit = 21) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42,limit = 21) == 253: {e}')
    
    total += 1
    try:
        result = candidate(n = 42,limit = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42,limit = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,limit = 20) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,limit = 20) == 78: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,limit = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,limit = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,limit = 20) == 306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,limit = 20) == 306: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 10,limit = 5) == 21
    assert candidate(n = 3,limit = 3) == 10
    assert candidate(n = 5,limit = 2) == 3
    assert candidate(n = 4,limit = 2) == 6
    assert candidate(n = 7,limit = 3) == 6
    assert candidate(n = 4,limit = 4) == 15
    assert candidate(n = 25,limit = 10) == 21
    assert candidate(n = 1,limit = 1) == 3
    assert candidate(n = 20,limit = 10) == 66
    assert candidate(n = 20,limit = 15) == 186
    assert candidate(n = 50,limit = 50) == 1326
    assert candidate(n = 15,limit = 10) == 91
    assert candidate(n = 10,limit = 1) == 0
    assert candidate(n = 35,limit = 12) == 3
    assert candidate(n = 50,limit = 1) == 0
    assert candidate(n = 18,limit = 6) == 1
    assert candidate(n = 28,limit = 8) == 0
    assert candidate(n = 31,limit = 9) == 0
    assert candidate(n = 42,limit = 3) == 0
    assert candidate(n = 30,limit = 3) == 0
    assert candidate(n = 40,limit = 15) == 21
    assert candidate(n = 32,limit = 11) == 3
    assert candidate(n = 32,limit = 8) == 0
    assert candidate(n = 15,limit = 3) == 0
    assert candidate(n = 50,limit = 20) == 66
    assert candidate(n = 27,limit = 9) == 1
    assert candidate(n = 45,limit = 15) == 1
    assert candidate(n = 28,limit = 7) == 0
    assert candidate(n = 30,limit = 5) == 0
    assert candidate(n = 33,limit = 8) == 0
    assert candidate(n = 15,limit = 7) == 28
    assert candidate(n = 50,limit = 25) == 351
    assert candidate(n = 22,limit = 7) == 0
    assert candidate(n = 37,limit = 18) == 171
    assert candidate(n = 30,limit = 8) == 0
    assert candidate(n = 49,limit = 17) == 6
    assert candidate(n = 40,limit = 20) == 231
    assert candidate(n = 10,limit = 2) == 0
    assert candidate(n = 38,limit = 19) == 210
    assert candidate(n = 33,limit = 6) == 0
    assert candidate(n = 49,limit = 25) == 375
    assert candidate(n = 30,limit = 12) == 28
    assert candidate(n = 35,limit = 8) == 0
    assert candidate(n = 42,limit = 12) == 0
    assert candidate(n = 30,limit = 10) == 1
    assert candidate(n = 50,limit = 10) == 0
    assert candidate(n = 49,limit = 16) == 0
    assert candidate(n = 30,limit = 20) == 331
    assert candidate(n = 45,limit = 20) == 136
    assert candidate(n = 48,limit = 16) == 1
    assert candidate(n = 49,limit = 14) == 0
    assert candidate(n = 10,limit = 3) == 0
    assert candidate(n = 28,limit = 10) == 6
    assert candidate(n = 15,limit = 5) == 1
    assert candidate(n = 40,limit = 5) == 0
    assert candidate(n = 15,limit = 4) == 0
    assert candidate(n = 35,limit = 10) == 0
    assert candidate(n = 10,limit = 4) == 6
    assert candidate(n = 33,limit = 11) == 1
    assert candidate(n = 49,limit = 18) == 21
    assert candidate(n = 27,limit = 10) == 10
    assert candidate(n = 10,limit = 20) == 66
    assert candidate(n = 22,limit = 11) == 78
    assert candidate(n = 27,limit = 8) == 0
    assert candidate(n = 35,limit = 7) == 0
    assert candidate(n = 10,limit = 10) == 66
    assert candidate(n = 42,limit = 21) == 253
    assert candidate(n = 42,limit = 9) == 0
    assert candidate(n = 49,limit = 20) == 78
    assert candidate(n = 20,limit = 2) == 0
    assert candidate(n = 35,limit = 20) == 306


