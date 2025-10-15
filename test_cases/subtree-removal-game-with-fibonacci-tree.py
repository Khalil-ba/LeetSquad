def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 45) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 53) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 53) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 70) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 43) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 43) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 68) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 68) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 37) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 73) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 27) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 35) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 36) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 77) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 24) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 24) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 94) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 94) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 55) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 65) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 88) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 97) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 29) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 21) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 82) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 86) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 86) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 44) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 87) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 87) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 17) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 98) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 42) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 80) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 74) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 74) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 46) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 46) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 75) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 71) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 71) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 81) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 41) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 83) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 83) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 52) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 52) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 92) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 92) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 79) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 79) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 84) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 90) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 63) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 61) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 61) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 47) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 93) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 93) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 57) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 57) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 34) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 60) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 30) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 95) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 72) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 33) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 76) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 76) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 51) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 51) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 18) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 32) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 48) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 14) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 26) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 26) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 13) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 69) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 69) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 12) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 50) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 58) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 58) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 56) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 59) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 59) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 40) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 67) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 99) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 64) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 66) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 66) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 54) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 22) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 96) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 96) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 39) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 39) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 91) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 62) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 62) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 78) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 78) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 85) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 31) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 38) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 38) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 25) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 3) == True
    assert candidate(n = 45) == True
    assert candidate(n = 53) == True
    assert candidate(n = 70) == True
    assert candidate(n = 43) == False
    assert candidate(n = 68) == True
    assert candidate(n = 5) == True
    assert candidate(n = 37) == False
    assert candidate(n = 23) == True
    assert candidate(n = 73) == False
    assert candidate(n = 8) == True
    assert candidate(n = 27) == True
    assert candidate(n = 35) == True
    assert candidate(n = 36) == True
    assert candidate(n = 77) == True
    assert candidate(n = 24) == True
    assert candidate(n = 11) == True
    assert candidate(n = 94) == True
    assert candidate(n = 1) == False
    assert candidate(n = 55) == False
    assert candidate(n = 65) == True
    assert candidate(n = 88) == True
    assert candidate(n = 97) == False
    assert candidate(n = 29) == True
    assert candidate(n = 21) == True
    assert candidate(n = 82) == True
    assert candidate(n = 86) == True
    assert candidate(n = 44) == True
    assert candidate(n = 28) == True
    assert candidate(n = 87) == True
    assert candidate(n = 4) == True
    assert candidate(n = 17) == True
    assert candidate(n = 98) == True
    assert candidate(n = 42) == True
    assert candidate(n = 80) == True
    assert candidate(n = 89) == True
    assert candidate(n = 74) == True
    assert candidate(n = 46) == True
    assert candidate(n = 75) == True
    assert candidate(n = 20) == True
    assert candidate(n = 71) == True
    assert candidate(n = 81) == True
    assert candidate(n = 41) == True
    assert candidate(n = 9) == True
    assert candidate(n = 83) == True
    assert candidate(n = 6) == True
    assert candidate(n = 52) == True
    assert candidate(n = 92) == True
    assert candidate(n = 10) == True
    assert candidate(n = 79) == False
    assert candidate(n = 84) == True
    assert candidate(n = 90) == True
    assert candidate(n = 63) == True
    assert candidate(n = 61) == False
    assert candidate(n = 49) == False
    assert candidate(n = 47) == True
    assert candidate(n = 93) == True
    assert candidate(n = 57) == True
    assert candidate(n = 34) == True
    assert candidate(n = 60) == True
    assert candidate(n = 30) == True
    assert candidate(n = 95) == True
    assert candidate(n = 72) == True
    assert candidate(n = 16) == True
    assert candidate(n = 33) == True
    assert candidate(n = 2) == True
    assert candidate(n = 76) == True
    assert candidate(n = 51) == True
    assert candidate(n = 18) == True
    assert candidate(n = 32) == True
    assert candidate(n = 48) == True
    assert candidate(n = 15) == True
    assert candidate(n = 14) == True
    assert candidate(n = 26) == True
    assert candidate(n = 13) == False
    assert candidate(n = 69) == True
    assert candidate(n = 12) == True
    assert candidate(n = 100) == True
    assert candidate(n = 50) == True
    assert candidate(n = 58) == True
    assert candidate(n = 56) == True
    assert candidate(n = 59) == True
    assert candidate(n = 40) == True
    assert candidate(n = 67) == False
    assert candidate(n = 99) == True
    assert candidate(n = 64) == True
    assert candidate(n = 66) == True
    assert candidate(n = 54) == True
    assert candidate(n = 22) == True
    assert candidate(n = 96) == True
    assert candidate(n = 19) == False
    assert candidate(n = 39) == True
    assert candidate(n = 91) == False
    assert candidate(n = 62) == True
    assert candidate(n = 78) == True
    assert candidate(n = 85) == False
    assert candidate(n = 31) == False
    assert candidate(n = 38) == True
    assert candidate(n = 7) == False
    assert candidate(n = 25) == False


