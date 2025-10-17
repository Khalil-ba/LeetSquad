def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num1 = 100,num2 = -100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100,num2 = -100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -10,num2 = 4) == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -10,num2 = 4) == -6: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 25,num2 = 25) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 25,num2 = 25) == 50: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -50,num2 = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -50,num2 = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 99,num2 = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 99,num2 = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -50,num2 = 25) == -25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -50,num2 = 25) == -25: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -30,num2 = -70) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -30,num2 = -70) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100,num2 = 100) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100,num2 = 100) == 200: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 12,num2 = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 12,num2 = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 0,num2 = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 0,num2 = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -100,num2 = -100) == -200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -100,num2 = -100) == -200: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -99,num2 = -1) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -99,num2 = -1) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 50,num2 = -50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 50,num2 = -50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -45,num2 = -55) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -45,num2 = -55) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -73,num2 = -27) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -73,num2 = -27) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 80,num2 = -30) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 80,num2 = -30) == 50: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 23,num2 = -23) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 23,num2 = -23) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -75,num2 = 20) == -55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -75,num2 = 20) == -55: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100,num2 = 0) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100,num2 = 0) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 0,num2 = -100) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 0,num2 = -100) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -1,num2 = -99) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -1,num2 = -99) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -45,num2 = 65) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -45,num2 = 65) == 20: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 22,num2 = 78) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 22,num2 = 78) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 98,num2 = 2) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 98,num2 = 2) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 45,num2 = -55) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 45,num2 = -55) == -10: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -75,num2 = 25) == -50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -75,num2 = 25) == -50: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -88,num2 = 12) == -76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -88,num2 = 12) == -76: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -75,num2 = -25) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -75,num2 = -25) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 99) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 99) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -100,num2 = 0) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -100,num2 = 0) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 42,num2 = -42) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 42,num2 = -42) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -49,num2 = 51) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -49,num2 = 51) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -99,num2 = 1) == -98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -99,num2 = 1) == -98: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 0,num2 = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 0,num2 = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 45,num2 = -45) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 45,num2 = -45) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 50,num2 = -60) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 50,num2 = -60) == -10: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 88,num2 = 12) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 88,num2 = 12) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -45,num2 = 55) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -45,num2 = 55) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 67,num2 = -33) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 67,num2 = -33) == 34: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -33,num2 = -67) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -33,num2 = -67) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -30,num2 = 70) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -30,num2 = 70) == 40: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -67,num2 = 33) == -34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -67,num2 = 33) == -34: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 99,num2 = -1) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 99,num2 = -1) == 98: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 73,num2 = 27) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 73,num2 = 27) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 75,num2 = -25) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 75,num2 = -25) == 50: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -45,num2 = 45) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -45,num2 = 45) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -100,num2 = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -100,num2 = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -23,num2 = 23) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -23,num2 = 23) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 67,num2 = 33) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 67,num2 = 33) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 50,num2 = 50) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 50,num2 = 50) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -50,num2 = -50) == -100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -50,num2 = -50) == -100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 28,num2 = -28) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 28,num2 = -28) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 45,num2 = 55) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 45,num2 = 55) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 33,num2 = 67) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 33,num2 = 67) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 75,num2 = 25) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 75,num2 = 25) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 49,num2 = 51) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 49,num2 = 51) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = -23,num2 = 77) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = -23,num2 = 77) == 54: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 37,num2 = 63) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 37,num2 = 63) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 29,num2 = 71) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 29,num2 = 71) == 100: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num1 = 100,num2 = -100) == 0
    assert candidate(num1 = -10,num2 = 4) == -6
    assert candidate(num1 = 25,num2 = 25) == 50
    assert candidate(num1 = -50,num2 = 50) == 0
    assert candidate(num1 = 99,num2 = 1) == 100
    assert candidate(num1 = -50,num2 = 25) == -25
    assert candidate(num1 = -30,num2 = -70) == -100
    assert candidate(num1 = 100,num2 = 100) == 200
    assert candidate(num1 = 12,num2 = 5) == 17
    assert candidate(num1 = 0,num2 = 0) == 0
    assert candidate(num1 = -100,num2 = -100) == -200
    assert candidate(num1 = -99,num2 = -1) == -100
    assert candidate(num1 = 50,num2 = -50) == 0
    assert candidate(num1 = -45,num2 = -55) == -100
    assert candidate(num1 = -73,num2 = -27) == -100
    assert candidate(num1 = 80,num2 = -30) == 50
    assert candidate(num1 = 23,num2 = -23) == 0
    assert candidate(num1 = -75,num2 = 20) == -55
    assert candidate(num1 = 100,num2 = 0) == 100
    assert candidate(num1 = 0,num2 = -100) == -100
    assert candidate(num1 = -1,num2 = -99) == -100
    assert candidate(num1 = -45,num2 = 65) == 20
    assert candidate(num1 = 22,num2 = 78) == 100
    assert candidate(num1 = 98,num2 = 2) == 100
    assert candidate(num1 = 45,num2 = -55) == -10
    assert candidate(num1 = -75,num2 = 25) == -50
    assert candidate(num1 = -88,num2 = 12) == -76
    assert candidate(num1 = -75,num2 = -25) == -100
    assert candidate(num1 = 1,num2 = 99) == 100
    assert candidate(num1 = -100,num2 = 0) == -100
    assert candidate(num1 = 42,num2 = -42) == 0
    assert candidate(num1 = -49,num2 = 51) == 2
    assert candidate(num1 = -99,num2 = 1) == -98
    assert candidate(num1 = 0,num2 = 100) == 100
    assert candidate(num1 = 45,num2 = -45) == 0
    assert candidate(num1 = 50,num2 = -60) == -10
    assert candidate(num1 = 88,num2 = 12) == 100
    assert candidate(num1 = -45,num2 = 55) == 10
    assert candidate(num1 = 67,num2 = -33) == 34
    assert candidate(num1 = -33,num2 = -67) == -100
    assert candidate(num1 = -30,num2 = 70) == 40
    assert candidate(num1 = -67,num2 = 33) == -34
    assert candidate(num1 = 99,num2 = -1) == 98
    assert candidate(num1 = 73,num2 = 27) == 100
    assert candidate(num1 = 75,num2 = -25) == 50
    assert candidate(num1 = -45,num2 = 45) == 0
    assert candidate(num1 = -100,num2 = 100) == 0
    assert candidate(num1 = -23,num2 = 23) == 0
    assert candidate(num1 = 67,num2 = 33) == 100
    assert candidate(num1 = 50,num2 = 50) == 100
    assert candidate(num1 = -50,num2 = -50) == -100
    assert candidate(num1 = 28,num2 = -28) == 0
    assert candidate(num1 = 45,num2 = 55) == 100
    assert candidate(num1 = 33,num2 = 67) == 100
    assert candidate(num1 = 75,num2 = 25) == 100
    assert candidate(num1 = 49,num2 = 51) == 100
    assert candidate(num1 = -23,num2 = 77) == 54
    assert candidate(num1 = 37,num2 = 63) == 100
    assert candidate(num1 = 29,num2 = 71) == 100


