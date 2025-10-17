def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 98: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 99: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 96: {e}')
    
    total += 1
    try:
        result = candidate(n = 88) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88) == 87: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == 28: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 61) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61) == 60: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 48: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == 46: {e}')
    
    total += 1
    try:
        result = candidate(n = 82) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82) == 81: {e}')
    
    total += 1
    try:
        result = candidate(n = 70) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70) == 69: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 34) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 59: {e}')
    
    total += 1
    try:
        result = candidate(n = 87) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87) == 86: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 95) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95) == 94: {e}')
    
    total += 1
    try:
        result = candidate(n = 67) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 39: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 63: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 98) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98) == 97: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 73) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73) == 72: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == 79: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 88: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 71) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 71) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 91) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 80: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == 84: {e}')
    
    total += 1
    try:
        result = candidate(n = 41) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 83) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 83) == 82: {e}')
    
    total += 1
    try:
        result = candidate(n = 65) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == 89: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 24: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 2
    assert candidate(n = 99) == 98
    assert candidate(n = 20) == 19
    assert candidate(n = 100) == 99
    assert candidate(n = 1) == 1
    assert candidate(n = 10) == 9
    assert candidate(n = 5) == 4
    assert candidate(n = 97) == 96
    assert candidate(n = 88) == 87
    assert candidate(n = 29) == 28
    assert candidate(n = 45) == 44
    assert candidate(n = 61) == 60
    assert candidate(n = 49) == 48
    assert candidate(n = 47) == 46
    assert candidate(n = 82) == 81
    assert candidate(n = 70) == 69
    assert candidate(n = 50) == 49
    assert candidate(n = 34) == 33
    assert candidate(n = 28) == 27
    assert candidate(n = 60) == 59
    assert candidate(n = 87) == 86
    assert candidate(n = 30) == 29
    assert candidate(n = 95) == 94
    assert candidate(n = 67) == 66
    assert candidate(n = 40) == 39
    assert candidate(n = 37) == 36
    assert candidate(n = 64) == 63
    assert candidate(n = 17) == 16
    assert candidate(n = 98) == 97
    assert candidate(n = 2) == 1
    assert candidate(n = 23) == 22
    assert candidate(n = 73) == 72
    assert candidate(n = 80) == 79
    assert candidate(n = 89) == 88
    assert candidate(n = 75) == 74
    assert candidate(n = 71) == 70
    assert candidate(n = 91) == 90
    assert candidate(n = 77) == 76
    assert candidate(n = 81) == 80
    assert candidate(n = 13) == 12
    assert candidate(n = 11) == 10
    assert candidate(n = 85) == 84
    assert candidate(n = 41) == 40
    assert candidate(n = 31) == 30
    assert candidate(n = 83) == 82
    assert candidate(n = 65) == 64
    assert candidate(n = 55) == 54
    assert candidate(n = 7) == 6
    assert candidate(n = 90) == 89
    assert candidate(n = 25) == 24


