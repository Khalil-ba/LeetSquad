def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(numBottles = 10,numExchange = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 10,numExchange = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 20,numExchange = 6) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 20,numExchange = 6) == 23: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 10) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 10) == 111: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 5,numExchange = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 5,numExchange = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 15,numExchange = 4) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 15,numExchange = 4) == 19: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 2) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 2) == 199: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 9,numExchange = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 9,numExchange = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 2) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 2) == 197: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 98,numExchange = 14) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 98,numExchange = 14) == 105: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 75,numExchange = 9) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 75,numExchange = 9) == 84: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 10) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 10) == 88: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 10) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 10) == 66: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 15) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 15) == 32: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 8) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 8) == 68: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 85,numExchange = 3) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 85,numExchange = 3) == 127: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 33,numExchange = 33) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 33,numExchange = 33) == 34: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 7) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 7) == 93: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 50,numExchange = 5) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 50,numExchange = 5) == 62: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 77,numExchange = 14) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 77,numExchange = 14) == 82: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 55,numExchange = 9) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 55,numExchange = 9) == 61: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 12) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 12) == 87: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 12) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 12) == 49: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 72,numExchange = 8) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 72,numExchange = 8) == 82: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 25,numExchange = 11) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 25,numExchange = 11) == 27: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 55,numExchange = 13) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 55,numExchange = 13) == 59: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 9) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 9) == 112: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 5) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 5) == 99: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 25,numExchange = 3) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 25,numExchange = 3) == 37: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 65,numExchange = 9) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 65,numExchange = 9) == 73: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 5,numExchange = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 5,numExchange = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 4) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 4) == 79: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 9) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 9) == 50: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 7) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 7) == 34: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 75,numExchange = 8) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 75,numExchange = 8) == 85: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 50,numExchange = 3) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 50,numExchange = 3) == 74: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 55,numExchange = 11) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 55,numExchange = 11) == 60: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 25,numExchange = 6) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 25,numExchange = 6) == 29: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 1,numExchange = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 1,numExchange = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 70,numExchange = 8) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 70,numExchange = 8) == 79: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 4) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 4) == 39: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 4) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 4) == 59: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 64,numExchange = 8) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 64,numExchange = 8) == 73: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 40,numExchange = 8) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 40,numExchange = 8) == 45: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 50,numExchange = 7) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 50,numExchange = 7) == 58: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 75,numExchange = 6) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 75,numExchange = 6) == 89: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 9) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 9) == 111: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 70,numExchange = 9) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 70,numExchange = 9) == 78: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 7) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 7) == 115: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 85,numExchange = 5) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 85,numExchange = 5) == 106: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 81,numExchange = 9) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 81,numExchange = 9) == 91: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 10) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 10) == 109: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 88,numExchange = 11) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 88,numExchange = 11) == 96: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 11) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 11) == 65: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 60,numExchange = 12) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 60,numExchange = 12) == 65: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 77,numExchange = 13) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 77,numExchange = 13) == 83: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 7) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 7) == 52: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 3) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 3) == 148: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 65,numExchange = 15) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 65,numExchange = 15) == 69: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 33,numExchange = 11) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 33,numExchange = 11) == 36: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 45,numExchange = 3) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 45,numExchange = 3) == 67: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 40,numExchange = 13) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 40,numExchange = 13) == 43: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 99,numExchange = 5) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 99,numExchange = 5) == 123: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 11) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 11) == 109: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 6) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 6) == 107: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 75,numExchange = 12) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 75,numExchange = 12) == 81: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 30,numExchange = 6) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 30,numExchange = 6) == 35: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 100,numExchange = 5) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 100,numExchange = 5) == 124: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 40,numExchange = 15) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 40,numExchange = 15) == 42: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 65,numExchange = 13) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 65,numExchange = 13) == 70: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 90,numExchange = 4) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 90,numExchange = 4) == 119: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 50,numExchange = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 50,numExchange = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(numBottles = 80,numExchange = 4) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numBottles = 80,numExchange = 4) == 106: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(numBottles = 10,numExchange = 2) == 19
    assert candidate(numBottles = 20,numExchange = 6) == 23
    assert candidate(numBottles = 100,numExchange = 10) == 111
    assert candidate(numBottles = 5,numExchange = 5) == 6
    assert candidate(numBottles = 15,numExchange = 4) == 19
    assert candidate(numBottles = 100,numExchange = 2) == 199
    assert candidate(numBottles = 9,numExchange = 3) == 13
    assert candidate(numBottles = 99,numExchange = 2) == 197
    assert candidate(numBottles = 98,numExchange = 14) == 105
    assert candidate(numBottles = 75,numExchange = 9) == 84
    assert candidate(numBottles = 80,numExchange = 10) == 88
    assert candidate(numBottles = 60,numExchange = 10) == 66
    assert candidate(numBottles = 30,numExchange = 15) == 32
    assert candidate(numBottles = 60,numExchange = 8) == 68
    assert candidate(numBottles = 85,numExchange = 3) == 127
    assert candidate(numBottles = 33,numExchange = 33) == 34
    assert candidate(numBottles = 80,numExchange = 7) == 93
    assert candidate(numBottles = 50,numExchange = 5) == 62
    assert candidate(numBottles = 77,numExchange = 14) == 82
    assert candidate(numBottles = 55,numExchange = 9) == 61
    assert candidate(numBottles = 80,numExchange = 12) == 87
    assert candidate(numBottles = 45,numExchange = 12) == 49
    assert candidate(numBottles = 72,numExchange = 8) == 82
    assert candidate(numBottles = 100,numExchange = 100) == 101
    assert candidate(numBottles = 25,numExchange = 11) == 27
    assert candidate(numBottles = 55,numExchange = 13) == 59
    assert candidate(numBottles = 100,numExchange = 9) == 112
    assert candidate(numBottles = 80,numExchange = 5) == 99
    assert candidate(numBottles = 25,numExchange = 3) == 37
    assert candidate(numBottles = 65,numExchange = 9) == 73
    assert candidate(numBottles = 5,numExchange = 6) == 5
    assert candidate(numBottles = 60,numExchange = 4) == 79
    assert candidate(numBottles = 45,numExchange = 9) == 50
    assert candidate(numBottles = 30,numExchange = 7) == 34
    assert candidate(numBottles = 75,numExchange = 8) == 85
    assert candidate(numBottles = 50,numExchange = 3) == 74
    assert candidate(numBottles = 55,numExchange = 11) == 60
    assert candidate(numBottles = 25,numExchange = 6) == 29
    assert candidate(numBottles = 1,numExchange = 2) == 1
    assert candidate(numBottles = 70,numExchange = 8) == 79
    assert candidate(numBottles = 30,numExchange = 4) == 39
    assert candidate(numBottles = 45,numExchange = 4) == 59
    assert candidate(numBottles = 64,numExchange = 8) == 73
    assert candidate(numBottles = 40,numExchange = 8) == 45
    assert candidate(numBottles = 50,numExchange = 7) == 58
    assert candidate(numBottles = 75,numExchange = 6) == 89
    assert candidate(numBottles = 99,numExchange = 9) == 111
    assert candidate(numBottles = 70,numExchange = 9) == 78
    assert candidate(numBottles = 99,numExchange = 7) == 115
    assert candidate(numBottles = 85,numExchange = 5) == 106
    assert candidate(numBottles = 81,numExchange = 9) == 91
    assert candidate(numBottles = 99,numExchange = 10) == 109
    assert candidate(numBottles = 88,numExchange = 11) == 96
    assert candidate(numBottles = 60,numExchange = 11) == 65
    assert candidate(numBottles = 60,numExchange = 12) == 65
    assert candidate(numBottles = 77,numExchange = 13) == 83
    assert candidate(numBottles = 45,numExchange = 7) == 52
    assert candidate(numBottles = 99,numExchange = 3) == 148
    assert candidate(numBottles = 65,numExchange = 15) == 69
    assert candidate(numBottles = 33,numExchange = 11) == 36
    assert candidate(numBottles = 45,numExchange = 3) == 67
    assert candidate(numBottles = 40,numExchange = 13) == 43
    assert candidate(numBottles = 99,numExchange = 5) == 123
    assert candidate(numBottles = 100,numExchange = 11) == 109
    assert candidate(numBottles = 90,numExchange = 6) == 107
    assert candidate(numBottles = 75,numExchange = 12) == 81
    assert candidate(numBottles = 30,numExchange = 6) == 35
    assert candidate(numBottles = 100,numExchange = 5) == 124
    assert candidate(numBottles = 40,numExchange = 15) == 42
    assert candidate(numBottles = 65,numExchange = 13) == 70
    assert candidate(numBottles = 90,numExchange = 4) == 119
    assert candidate(numBottles = 50,numExchange = 10) == 55
    assert candidate(numBottles = 80,numExchange = 4) == 106


