def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 1,t = 50) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1,t = 50) == 101: {e}')
    
    total += 1
    try:
        result = candidate(num = 10,t = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10,t = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(num = 50,t = 50) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 50,t = 50) == 150: {e}')
    
    total += 1
    try:
        result = candidate(num = 1,t = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1,t = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 25,t = 25) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 25,t = 25) == 75: {e}')
    
    total += 1
    try:
        result = candidate(num = 3,t = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3,t = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 4,t = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4,t = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num = 25,t = 10) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 25,t = 10) == 45: {e}')
    
    total += 1
    try:
        result = candidate(num = 2,t = 45) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2,t = 45) == 92: {e}')
    
    total += 1
    try:
        result = candidate(num = 28,t = 12) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 28,t = 12) == 52: {e}')
    
    total += 1
    try:
        result = candidate(num = 42,t = 15) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 42,t = 15) == 72: {e}')
    
    total += 1
    try:
        result = candidate(num = 45,t = 4) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45,t = 4) == 53: {e}')
    
    total += 1
    try:
        result = candidate(num = 35,t = 28) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 35,t = 28) == 91: {e}')
    
    total += 1
    try:
        result = candidate(num = 7,t = 20) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7,t = 20) == 47: {e}')
    
    total += 1
    try:
        result = candidate(num = 40,t = 1) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 40,t = 1) == 42: {e}')
    
    total += 1
    try:
        result = candidate(num = 27,t = 15) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 27,t = 15) == 57: {e}')
    
    total += 1
    try:
        result = candidate(num = 30,t = 15) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 30,t = 15) == 60: {e}')
    
    total += 1
    try:
        result = candidate(num = 28,t = 28) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 28,t = 28) == 84: {e}')
    
    total += 1
    try:
        result = candidate(num = 18,t = 49) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 18,t = 49) == 116: {e}')
    
    total += 1
    try:
        result = candidate(num = 29,t = 17) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 29,t = 17) == 63: {e}')
    
    total += 1
    try:
        result = candidate(num = 30,t = 29) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 30,t = 29) == 88: {e}')
    
    total += 1
    try:
        result = candidate(num = 35,t = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 35,t = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(num = 8,t = 8) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8,t = 8) == 24: {e}')
    
    total += 1
    try:
        result = candidate(num = 49,t = 50) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 49,t = 50) == 149: {e}')
    
    total += 1
    try:
        result = candidate(num = 30,t = 45) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 30,t = 45) == 120: {e}')
    
    total += 1
    try:
        result = candidate(num = 28,t = 30) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 28,t = 30) == 88: {e}')
    
    total += 1
    try:
        result = candidate(num = 20,t = 35) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20,t = 35) == 90: {e}')
    
    total += 1
    try:
        result = candidate(num = 5,t = 50) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5,t = 50) == 105: {e}')
    
    total += 1
    try:
        result = candidate(num = 10,t = 40) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10,t = 40) == 90: {e}')
    
    total += 1
    try:
        result = candidate(num = 29,t = 15) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 29,t = 15) == 59: {e}')
    
    total += 1
    try:
        result = candidate(num = 33,t = 18) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33,t = 18) == 69: {e}')
    
    total += 1
    try:
        result = candidate(num = 27,t = 30) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 27,t = 30) == 87: {e}')
    
    total += 1
    try:
        result = candidate(num = 40,t = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 40,t = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(num = 2,t = 25) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2,t = 25) == 52: {e}')
    
    total += 1
    try:
        result = candidate(num = 45,t = 15) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45,t = 15) == 75: {e}')
    
    total += 1
    try:
        result = candidate(num = 23,t = 48) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 23,t = 48) == 119: {e}')
    
    total += 1
    try:
        result = candidate(num = 49,t = 10) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 49,t = 10) == 69: {e}')
    
    total += 1
    try:
        result = candidate(num = 20,t = 45) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20,t = 45) == 110: {e}')
    
    total += 1
    try:
        result = candidate(num = 15,t = 45) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15,t = 45) == 105: {e}')
    
    total += 1
    try:
        result = candidate(num = 12,t = 10) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12,t = 10) == 32: {e}')
    
    total += 1
    try:
        result = candidate(num = 2,t = 30) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2,t = 30) == 62: {e}')
    
    total += 1
    try:
        result = candidate(num = 12,t = 40) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12,t = 40) == 92: {e}')
    
    total += 1
    try:
        result = candidate(num = 37,t = 30) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 37,t = 30) == 97: {e}')
    
    total += 1
    try:
        result = candidate(num = 7,t = 7) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7,t = 7) == 21: {e}')
    
    total += 1
    try:
        result = candidate(num = 1,t = 20) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1,t = 20) == 41: {e}')
    
    total += 1
    try:
        result = candidate(num = 7,t = 43) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7,t = 43) == 93: {e}')
    
    total += 1
    try:
        result = candidate(num = 20,t = 1) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20,t = 1) == 22: {e}')
    
    total += 1
    try:
        result = candidate(num = 10,t = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10,t = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(num = 42,t = 9) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 42,t = 9) == 60: {e}')
    
    total += 1
    try:
        result = candidate(num = 45,t = 20) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45,t = 20) == 85: {e}')
    
    total += 1
    try:
        result = candidate(num = 45,t = 45) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45,t = 45) == 135: {e}')
    
    total += 1
    try:
        result = candidate(num = 45,t = 10) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45,t = 10) == 65: {e}')
    
    total += 1
    try:
        result = candidate(num = 1,t = 25) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1,t = 25) == 51: {e}')
    
    total += 1
    try:
        result = candidate(num = 30,t = 25) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 30,t = 25) == 80: {e}')
    
    total += 1
    try:
        result = candidate(num = 5,t = 30) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5,t = 30) == 65: {e}')
    
    total += 1
    try:
        result = candidate(num = 45,t = 1) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45,t = 1) == 47: {e}')
    
    total += 1
    try:
        result = candidate(num = 12,t = 38) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 12,t = 38) == 88: {e}')
    
    total += 1
    try:
        result = candidate(num = 15,t = 20) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15,t = 20) == 55: {e}')
    
    total += 1
    try:
        result = candidate(num = 20,t = 30) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20,t = 30) == 80: {e}')
    
    total += 1
    try:
        result = candidate(num = 7,t = 35) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7,t = 35) == 77: {e}')
    
    total += 1
    try:
        result = candidate(num = 50,t = 2) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 50,t = 2) == 54: {e}')
    
    total += 1
    try:
        result = candidate(num = 40,t = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 40,t = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(num = 35,t = 15) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 35,t = 15) == 65: {e}')
    
    total += 1
    try:
        result = candidate(num = 27,t = 27) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 27,t = 27) == 81: {e}')
    
    total += 1
    try:
        result = candidate(num = 22,t = 35) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 22,t = 35) == 92: {e}')
    
    total += 1
    try:
        result = candidate(num = 50,t = 25) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 50,t = 25) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num = 49,t = 25) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 49,t = 25) == 99: {e}')
    
    total += 1
    try:
        result = candidate(num = 2,t = 40) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2,t = 40) == 82: {e}')
    
    total += 1
    try:
        result = candidate(num = 15,t = 30) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15,t = 30) == 75: {e}')
    
    total += 1
    try:
        result = candidate(num = 30,t = 30) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 30,t = 30) == 90: {e}')
    
    total += 1
    try:
        result = candidate(num = 33,t = 15) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33,t = 15) == 63: {e}')
    
    total += 1
    try:
        result = candidate(num = 35,t = 18) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 35,t = 18) == 71: {e}')
    
    total += 1
    try:
        result = candidate(num = 15,t = 40) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15,t = 40) == 95: {e}')
    
    total += 1
    try:
        result = candidate(num = 23,t = 3) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 23,t = 3) == 29: {e}')
    
    total += 1
    try:
        result = candidate(num = 40,t = 20) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 40,t = 20) == 80: {e}')
    
    total += 1
    try:
        result = candidate(num = 30,t = 20) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 30,t = 20) == 70: {e}')
    
    total += 1
    try:
        result = candidate(num = 33,t = 17) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33,t = 17) == 67: {e}')
    
    total += 1
    try:
        result = candidate(num = 7,t = 25) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7,t = 25) == 57: {e}')
    
    total += 1
    try:
        result = candidate(num = 47,t = 5) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 47,t = 5) == 57: {e}')
    
    total += 1
    try:
        result = candidate(num = 50,t = 1) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 50,t = 1) == 52: {e}')
    
    total += 1
    try:
        result = candidate(num = 29,t = 21) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 29,t = 21) == 71: {e}')
    
    total += 1
    try:
        result = candidate(num = 20,t = 25) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20,t = 25) == 70: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 1,t = 50) == 101
    assert candidate(num = 10,t = 5) == 20
    assert candidate(num = 50,t = 50) == 150
    assert candidate(num = 1,t = 1) == 3
    assert candidate(num = 25,t = 25) == 75
    assert candidate(num = 3,t = 2) == 7
    assert candidate(num = 4,t = 1) == 6
    assert candidate(num = 25,t = 10) == 45
    assert candidate(num = 2,t = 45) == 92
    assert candidate(num = 28,t = 12) == 52
    assert candidate(num = 42,t = 15) == 72
    assert candidate(num = 45,t = 4) == 53
    assert candidate(num = 35,t = 28) == 91
    assert candidate(num = 7,t = 20) == 47
    assert candidate(num = 40,t = 1) == 42
    assert candidate(num = 27,t = 15) == 57
    assert candidate(num = 30,t = 15) == 60
    assert candidate(num = 28,t = 28) == 84
    assert candidate(num = 18,t = 49) == 116
    assert candidate(num = 29,t = 17) == 63
    assert candidate(num = 30,t = 29) == 88
    assert candidate(num = 35,t = 10) == 55
    assert candidate(num = 8,t = 8) == 24
    assert candidate(num = 49,t = 50) == 149
    assert candidate(num = 30,t = 45) == 120
    assert candidate(num = 28,t = 30) == 88
    assert candidate(num = 20,t = 35) == 90
    assert candidate(num = 5,t = 50) == 105
    assert candidate(num = 10,t = 40) == 90
    assert candidate(num = 29,t = 15) == 59
    assert candidate(num = 33,t = 18) == 69
    assert candidate(num = 27,t = 30) == 87
    assert candidate(num = 40,t = 10) == 60
    assert candidate(num = 2,t = 25) == 52
    assert candidate(num = 45,t = 15) == 75
    assert candidate(num = 23,t = 48) == 119
    assert candidate(num = 49,t = 10) == 69
    assert candidate(num = 20,t = 45) == 110
    assert candidate(num = 15,t = 45) == 105
    assert candidate(num = 12,t = 10) == 32
    assert candidate(num = 2,t = 30) == 62
    assert candidate(num = 12,t = 40) == 92
    assert candidate(num = 37,t = 30) == 97
    assert candidate(num = 7,t = 7) == 21
    assert candidate(num = 1,t = 20) == 41
    assert candidate(num = 7,t = 43) == 93
    assert candidate(num = 20,t = 1) == 22
    assert candidate(num = 10,t = 1) == 12
    assert candidate(num = 42,t = 9) == 60
    assert candidate(num = 45,t = 20) == 85
    assert candidate(num = 45,t = 45) == 135
    assert candidate(num = 45,t = 10) == 65
    assert candidate(num = 1,t = 25) == 51
    assert candidate(num = 30,t = 25) == 80
    assert candidate(num = 5,t = 30) == 65
    assert candidate(num = 45,t = 1) == 47
    assert candidate(num = 12,t = 38) == 88
    assert candidate(num = 15,t = 20) == 55
    assert candidate(num = 20,t = 30) == 80
    assert candidate(num = 7,t = 35) == 77
    assert candidate(num = 50,t = 2) == 54
    assert candidate(num = 40,t = 5) == 50
    assert candidate(num = 35,t = 15) == 65
    assert candidate(num = 27,t = 27) == 81
    assert candidate(num = 22,t = 35) == 92
    assert candidate(num = 50,t = 25) == 100
    assert candidate(num = 49,t = 25) == 99
    assert candidate(num = 2,t = 40) == 82
    assert candidate(num = 15,t = 30) == 75
    assert candidate(num = 30,t = 30) == 90
    assert candidate(num = 33,t = 15) == 63
    assert candidate(num = 35,t = 18) == 71
    assert candidate(num = 15,t = 40) == 95
    assert candidate(num = 23,t = 3) == 29
    assert candidate(num = 40,t = 20) == 80
    assert candidate(num = 30,t = 20) == 70
    assert candidate(num = 33,t = 17) == 67
    assert candidate(num = 7,t = 25) == 57
    assert candidate(num = 47,t = 5) == 57
    assert candidate(num = 50,t = 1) == 52
    assert candidate(num = 29,t = 21) == 71
    assert candidate(num = 20,t = 25) == 70


