def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == 99: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == 97: {e}')
    
    total += 1
    try:
        result = candidate(n = 61) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61) == 61: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 73) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73) == 73: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 79) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 79) == 79: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == 89: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 91) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91) == 91: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == 81: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == 85: {e}')
    
    total += 1
    try:
        result = candidate(n = 41) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == 25: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == 3
    assert candidate(n = 100) == 50
    assert candidate(n = 4) == 2
    assert candidate(n = 99) == 99
    assert candidate(n = 17) == 17
    assert candidate(n = 2) == 1
    assert candidate(n = 1) == 0
    assert candidate(n = 50) == 25
    assert candidate(n = 7) == 7
    assert candidate(n = 10) == 5
    assert candidate(n = 5) == 5
    assert candidate(n = 97) == 97
    assert candidate(n = 61) == 61
    assert candidate(n = 49) == 49
    assert candidate(n = 12) == 6
    assert candidate(n = 21) == 21
    assert candidate(n = 60) == 30
    assert candidate(n = 30) == 15
    assert candidate(n = 40) == 20
    assert candidate(n = 64) == 32
    assert candidate(n = 33) == 33
    assert candidate(n = 37) == 37
    assert candidate(n = 16) == 8
    assert candidate(n = 23) == 23
    assert candidate(n = 73) == 73
    assert candidate(n = 42) == 21
    assert candidate(n = 90) == 45
    assert candidate(n = 8) == 4
    assert candidate(n = 79) == 79
    assert candidate(n = 89) == 89
    assert candidate(n = 75) == 75
    assert candidate(n = 32) == 16
    assert candidate(n = 20) == 10
    assert candidate(n = 19) == 19
    assert candidate(n = 91) == 91
    assert candidate(n = 81) == 81
    assert candidate(n = 11) == 11
    assert candidate(n = 15) == 15
    assert candidate(n = 85) == 85
    assert candidate(n = 41) == 41
    assert candidate(n = 9) == 9
    assert candidate(n = 6) == 3
    assert candidate(n = 13) == 13
    assert candidate(n = 25) == 25


