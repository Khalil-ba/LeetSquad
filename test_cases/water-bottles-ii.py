def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(numBottles = 10,numExchange = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 10,numExchange = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 2,numExchange = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 2,numExchange = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 13,numExchange = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 13,numExchange = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 1) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 1) == 114: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 5,numExchange = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 5,numExchange = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 1,numExchange = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 1,numExchange = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 20,numExchange = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 20,numExchange = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 50,numExchange = 10) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 50,numExchange = 10) == 54: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 1,numExchange = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 1,numExchange = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 1,numExchange = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 1,numExchange = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 2) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 2) == 112: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 70,numExchange = 6) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 70,numExchange = 6) == 78: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 2) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 2) == 70: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 20) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 20) == 47: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 8) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 8) == 66: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 9) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 9) == 97: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 8) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 8) == 87: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 18) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 18) == 94: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 75,numExchange = 15) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 75,numExchange = 15) == 79: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 40,numExchange = 50) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 40,numExchange = 50) == 40: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 2) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 2) == 37: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 5) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 5) == 100: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 55,numExchange = 8) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 55,numExchange = 8) == 60: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 15,numExchange = 15) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 15,numExchange = 15) == 16: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 40,numExchange = 7) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 40,numExchange = 7) == 44: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 55,numExchange = 6) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 55,numExchange = 6) == 61: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 3) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 3) == 91: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 15) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 15) == 63: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 7) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 7) == 66: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 5) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 5) == 34: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 10) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 10) == 86: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 20) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 20) == 83: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 95,numExchange = 5) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 95,numExchange = 5) == 105: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 40,numExchange = 12) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 40,numExchange = 12) == 43: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 40,numExchange = 25) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 40,numExchange = 25) == 41: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 50,numExchange = 5) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 50,numExchange = 5) == 57: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 85,numExchange = 4) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 85,numExchange = 4) == 95: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 12) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 12) == 48: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 25,numExchange = 3) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 25,numExchange = 3) == 30: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 5) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 5) == 89: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 6) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 6) == 50: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 7) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 7) == 33: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 7,numExchange = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 7,numExchange = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 70,numExchange = 8) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 70,numExchange = 8) == 76: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 75,numExchange = 5) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 75,numExchange = 5) == 84: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 75,numExchange = 7) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 75,numExchange = 7) == 82: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 85,numExchange = 5) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 85,numExchange = 5) == 94: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 10) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 10) == 49: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 30) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 30) == 31: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 4) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 4) == 101: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 40,numExchange = 30) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 40,numExchange = 30) == 41: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 75,numExchange = 10) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 75,numExchange = 10) == 81: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 2) == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 2) == 113: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 35,numExchange = 18) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 35,numExchange = 18) == 36: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 55,numExchange = 12) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 55,numExchange = 12) == 59: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 50) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 50) == 102: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 8,numExchange = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 8,numExchange = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 15) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 15) == 84: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 20) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 20) == 62: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 3) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 3) == 111: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 20) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 20) == 103: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 20) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 20) == 104: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 3,numExchange = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 3,numExchange = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 50,numExchange = 1) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 50,numExchange = 1) == 60: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 70,numExchange = 25) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 70,numExchange = 25) == 72: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 6,numExchange = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 6,numExchange = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 65,numExchange = 12) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 65,numExchange = 12) == 69: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 55,numExchange = 20) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 55,numExchange = 20) == 57: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 25,numExchange = 2) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 25,numExchange = 2) == 31: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 95,numExchange = 7) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 95,numExchange = 7) == 104: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 2) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 2) == 53: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 25) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 25) == 93: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 95,numExchange = 15) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 95,numExchange = 15) == 100: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 4) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 4) == 52: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 9) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 9) == 107: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 25,numExchange = 7) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 25,numExchange = 7) == 28: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 3) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 3) == 36: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 5,numExchange = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 5,numExchange = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 3) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 3) == 69: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 3) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 3) == 53: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 25,numExchange = 9) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 25,numExchange = 9) == 27: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 6) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 6) == 99: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 10) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 10) == 97: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 70,numExchange = 7) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 70,numExchange = 7) == 77: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 15) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 15) == 95: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 50,numExchange = 2) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 50,numExchange = 2) == 59: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(numBottles = 10,numExchange = 3) == 13
    assert candidate(numBottles = 2,numExchange = 3) == 2
    assert candidate(numBottles = 13,numExchange = 6) == 15
    assert candidate(numBottles = 100,numExchange = 1) == 114
    assert candidate(numBottles = 5,numExchange = 5) == 6
    assert candidate(numBottles = 1,numExchange = 1) == 2
    assert candidate(numBottles = 20,numExchange = 4) == 24
    assert candidate(numBottles = 50,numExchange = 10) == 54
    assert candidate(numBottles = 1,numExchange = 100) == 1
    assert candidate(numBottles = 1,numExchange = 10) == 1
    assert candidate(numBottles = 99,numExchange = 2) == 112
    assert candidate(numBottles = 70,numExchange = 6) == 78
    assert candidate(numBottles = 60,numExchange = 2) == 70
    assert candidate(numBottles = 45,numExchange = 20) == 47
    assert candidate(numBottles = 60,numExchange = 8) == 66
    assert candidate(numBottles = 90,numExchange = 9) == 97
    assert candidate(numBottles = 80,numExchange = 8) == 87
    assert candidate(numBottles = 90,numExchange = 18) == 94
    assert candidate(numBottles = 75,numExchange = 15) == 79
    assert candidate(numBottles = 40,numExchange = 50) == 40
    assert candidate(numBottles = 30,numExchange = 2) == 37
    assert candidate(numBottles = 90,numExchange = 5) == 100
    assert candidate(numBottles = 55,numExchange = 8) == 60
    assert candidate(numBottles = 15,numExchange = 15) == 16
    assert candidate(numBottles = 40,numExchange = 7) == 44
    assert candidate(numBottles = 55,numExchange = 6) == 61
    assert candidate(numBottles = 80,numExchange = 3) == 91
    assert candidate(numBottles = 60,numExchange = 15) == 63
    assert candidate(numBottles = 60,numExchange = 7) == 66
    assert candidate(numBottles = 30,numExchange = 5) == 34
    assert candidate(numBottles = 80,numExchange = 10) == 86
    assert candidate(numBottles = 80,numExchange = 20) == 83
    assert candidate(numBottles = 95,numExchange = 5) == 105
    assert candidate(numBottles = 40,numExchange = 12) == 43
    assert candidate(numBottles = 40,numExchange = 25) == 41
    assert candidate(numBottles = 50,numExchange = 5) == 57
    assert candidate(numBottles = 85,numExchange = 4) == 95
    assert candidate(numBottles = 45,numExchange = 12) == 48
    assert candidate(numBottles = 25,numExchange = 3) == 30
    assert candidate(numBottles = 80,numExchange = 5) == 89
    assert candidate(numBottles = 45,numExchange = 6) == 50
    assert candidate(numBottles = 30,numExchange = 7) == 33
    assert candidate(numBottles = 7,numExchange = 8) == 7
    assert candidate(numBottles = 70,numExchange = 8) == 76
    assert candidate(numBottles = 75,numExchange = 5) == 84
    assert candidate(numBottles = 75,numExchange = 7) == 82
    assert candidate(numBottles = 85,numExchange = 5) == 94
    assert candidate(numBottles = 45,numExchange = 10) == 49
    assert candidate(numBottles = 30,numExchange = 30) == 31
    assert candidate(numBottles = 90,numExchange = 4) == 101
    assert candidate(numBottles = 40,numExchange = 30) == 41
    assert candidate(numBottles = 75,numExchange = 10) == 81
    assert candidate(numBottles = 100,numExchange = 2) == 113
    assert candidate(numBottles = 35,numExchange = 18) == 36
    assert candidate(numBottles = 55,numExchange = 12) == 59
    assert candidate(numBottles = 100,numExchange = 50) == 102
    assert candidate(numBottles = 8,numExchange = 4) == 10
    assert candidate(numBottles = 80,numExchange = 15) == 84
    assert candidate(numBottles = 60,numExchange = 20) == 62
    assert candidate(numBottles = 99,numExchange = 3) == 111
    assert candidate(numBottles = 99,numExchange = 20) == 103
    assert candidate(numBottles = 100,numExchange = 20) == 104
    assert candidate(numBottles = 3,numExchange = 3) == 4
    assert candidate(numBottles = 50,numExchange = 1) == 60
    assert candidate(numBottles = 70,numExchange = 25) == 72
    assert candidate(numBottles = 6,numExchange = 6) == 7
    assert candidate(numBottles = 65,numExchange = 12) == 69
    assert candidate(numBottles = 55,numExchange = 20) == 57
    assert candidate(numBottles = 25,numExchange = 2) == 31
    assert candidate(numBottles = 95,numExchange = 7) == 104
    assert candidate(numBottles = 45,numExchange = 2) == 53
    assert candidate(numBottles = 90,numExchange = 25) == 93
    assert candidate(numBottles = 95,numExchange = 15) == 100
    assert candidate(numBottles = 45,numExchange = 4) == 52
    assert candidate(numBottles = 99,numExchange = 9) == 107
    assert candidate(numBottles = 25,numExchange = 7) == 28
    assert candidate(numBottles = 30,numExchange = 3) == 36
    assert candidate(numBottles = 5,numExchange = 2) == 7
    assert candidate(numBottles = 60,numExchange = 3) == 69
    assert candidate(numBottles = 45,numExchange = 3) == 53
    assert candidate(numBottles = 25,numExchange = 9) == 27
    assert candidate(numBottles = 90,numExchange = 6) == 99
    assert candidate(numBottles = 90,numExchange = 10) == 97
    assert candidate(numBottles = 70,numExchange = 7) == 77
    assert candidate(numBottles = 90,numExchange = 15) == 95
    assert candidate(numBottles = 50,numExchange = 2) == 59


