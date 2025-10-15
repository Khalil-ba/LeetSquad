def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(purchaseAmount = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 85) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 85) == 10: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 15) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 15) == 80: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 10) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 10) == 90: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 45) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 45) == 50: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 51) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 51) == 50: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 34) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 34) == 70: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 0) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 0) == 100: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 60) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 60) == 40: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 25) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 25) == 70: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 9) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 9) == 90: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 75) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 75) == 20: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 55) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 55) == 40: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 99) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 99) == 0: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 31) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 31) == 70: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 27) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 27) == 70: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 22) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 22) == 80: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 35) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 35) == 60: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 7) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 7) == 90: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 49) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 49) == 50: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 28) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 28) == 70: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 11) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 11) == 90: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 26) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 26) == 70: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 65) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 65) == 30: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 90) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 90) == 10: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 69) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 69) == 30: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 84) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 84) == 20: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 91) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 91) == 10: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 29) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 29) == 70: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 67) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 67) == 30: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 23) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 23) == 80: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 59) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 59) == 40: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 63) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 63) == 40: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 4) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 4) == 100: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 38) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 38) == 60: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 6) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 6) == 90: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 5) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 5) == 90: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 79) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 79) == 20: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 74) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 74) == 30: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 47) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 47) == 50: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 77) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 77) == 20: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 39) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 39) == 60: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 2) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 2) == 100: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 8) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 8) == 90: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 95) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 95) == 0: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 14) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 14) == 90: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 94) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 94) == 10: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 30) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 30) == 70: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 89) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 89) == 10: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 3) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 3) == 100: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 19) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 19) == 80: {e}')
    
    total += 1
    try:
        result = candidate(purchaseAmount = 82) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(purchaseAmount = 82) == 20: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(purchaseAmount = 100) == 0
    assert candidate(purchaseAmount = 85) == 10
    assert candidate(purchaseAmount = 15) == 80
    assert candidate(purchaseAmount = 10) == 90
    assert candidate(purchaseAmount = 45) == 50
    assert candidate(purchaseAmount = 51) == 50
    assert candidate(purchaseAmount = 34) == 70
    assert candidate(purchaseAmount = 0) == 100
    assert candidate(purchaseAmount = 60) == 40
    assert candidate(purchaseAmount = 25) == 70
    assert candidate(purchaseAmount = 9) == 90
    assert candidate(purchaseAmount = 75) == 20
    assert candidate(purchaseAmount = 50) == 50
    assert candidate(purchaseAmount = 55) == 40
    assert candidate(purchaseAmount = 99) == 0
    assert candidate(purchaseAmount = 31) == 70
    assert candidate(purchaseAmount = 27) == 70
    assert candidate(purchaseAmount = 22) == 80
    assert candidate(purchaseAmount = 35) == 60
    assert candidate(purchaseAmount = 1) == 100
    assert candidate(purchaseAmount = 7) == 90
    assert candidate(purchaseAmount = 49) == 50
    assert candidate(purchaseAmount = 28) == 70
    assert candidate(purchaseAmount = 11) == 90
    assert candidate(purchaseAmount = 26) == 70
    assert candidate(purchaseAmount = 65) == 30
    assert candidate(purchaseAmount = 90) == 10
    assert candidate(purchaseAmount = 69) == 30
    assert candidate(purchaseAmount = 84) == 20
    assert candidate(purchaseAmount = 91) == 10
    assert candidate(purchaseAmount = 29) == 70
    assert candidate(purchaseAmount = 67) == 30
    assert candidate(purchaseAmount = 23) == 80
    assert candidate(purchaseAmount = 59) == 40
    assert candidate(purchaseAmount = 63) == 40
    assert candidate(purchaseAmount = 4) == 100
    assert candidate(purchaseAmount = 38) == 60
    assert candidate(purchaseAmount = 6) == 90
    assert candidate(purchaseAmount = 5) == 90
    assert candidate(purchaseAmount = 79) == 20
    assert candidate(purchaseAmount = 74) == 30
    assert candidate(purchaseAmount = 47) == 50
    assert candidate(purchaseAmount = 77) == 20
    assert candidate(purchaseAmount = 39) == 60
    assert candidate(purchaseAmount = 2) == 100
    assert candidate(purchaseAmount = 8) == 90
    assert candidate(purchaseAmount = 95) == 0
    assert candidate(purchaseAmount = 14) == 90
    assert candidate(purchaseAmount = 94) == 10
    assert candidate(purchaseAmount = 30) == 70
    assert candidate(purchaseAmount = 89) == 10
    assert candidate(purchaseAmount = 3) == 100
    assert candidate(purchaseAmount = 19) == 80
    assert candidate(purchaseAmount = 82) == 20


