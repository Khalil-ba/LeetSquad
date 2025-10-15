def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 15,desiredTotal = 50) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 15,desiredTotal = 50) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 8,desiredTotal = 25) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 8,desiredTotal = 25) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 40) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 40) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 21) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 21) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 5,desiredTotal = 50) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 5,desiredTotal = 50) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 100) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 100) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 28) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 28) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 15,desiredTotal = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 15,desiredTotal = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 12,desiredTotal = 30) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 12,desiredTotal = 30) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 7,desiredTotal = 15) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 7,desiredTotal = 15) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 6,desiredTotal = 16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 6,desiredTotal = 16) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 3,desiredTotal = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 3,desiredTotal = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 300) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 300) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 11) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 11) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 16,desiredTotal = 80) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 16,desiredTotal = 80) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 18,desiredTotal = 150) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 18,desiredTotal = 150) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 15,desiredTotal = 70) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 15,desiredTotal = 70) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 8,desiredTotal = 30) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 8,desiredTotal = 30) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 199) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 199) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 9,desiredTotal = 36) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 9,desiredTotal = 36) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 16,desiredTotal = 85) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 16,desiredTotal = 85) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 200) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 200) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 18,desiredTotal = 120) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 18,desiredTotal = 120) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 11,desiredTotal = 33) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 11,desiredTotal = 33) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 13,desiredTotal = 45) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 13,desiredTotal = 45) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 99) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 99) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 16,desiredTotal = 90) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 16,desiredTotal = 90) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 14,desiredTotal = 49) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 14,desiredTotal = 49) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 13,desiredTotal = 30) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 13,desiredTotal = 30) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 180) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 180) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 14,desiredTotal = 60) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 14,desiredTotal = 60) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 13,desiredTotal = 80) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 13,desiredTotal = 80) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 14,desiredTotal = 80) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 14,desiredTotal = 80) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 16,desiredTotal = 60) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 16,desiredTotal = 60) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 12,desiredTotal = 80) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 12,desiredTotal = 80) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 55) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 55) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 19,desiredTotal = 135) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 19,desiredTotal = 135) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 14,desiredTotal = 99) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 14,desiredTotal = 99) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 19,desiredTotal = 110) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 19,desiredTotal = 110) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 12,desiredTotal = 75) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 12,desiredTotal = 75) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 5,desiredTotal = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 5,desiredTotal = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 14,desiredTotal = 95) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 14,desiredTotal = 95) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 7,desiredTotal = 28) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 7,desiredTotal = 28) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 14,desiredTotal = 50) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 14,desiredTotal = 50) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 250) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 250) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 17,desiredTotal = 140) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 17,desiredTotal = 140) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 19,desiredTotal = 180) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 19,desiredTotal = 180) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 16,desiredTotal = 110) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 16,desiredTotal = 110) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 13,desiredTotal = 60) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 13,desiredTotal = 60) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 9,desiredTotal = 45) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 9,desiredTotal = 45) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 12,desiredTotal = 35) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 12,desiredTotal = 35) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 17,desiredTotal = 85) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 17,desiredTotal = 85) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 150) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 150) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 15,desiredTotal = 80) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 15,desiredTotal = 80) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 8,desiredTotal = 28) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 8,desiredTotal = 28) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 7,desiredTotal = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 7,desiredTotal = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 18,desiredTotal = 130) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 18,desiredTotal = 130) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 11,desiredTotal = 55) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 11,desiredTotal = 55) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 17,desiredTotal = 90) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 17,desiredTotal = 90) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 17,desiredTotal = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 17,desiredTotal = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 16,desiredTotal = 120) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 16,desiredTotal = 120) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 20,desiredTotal = 130) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 20,desiredTotal = 130) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 19,desiredTotal = 120) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 19,desiredTotal = 120) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 16,desiredTotal = 130) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 16,desiredTotal = 130) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 7,desiredTotal = 20) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 7,desiredTotal = 20) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 18,desiredTotal = 180) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 18,desiredTotal = 180) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 18,desiredTotal = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 18,desiredTotal = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 12,desiredTotal = 60) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 12,desiredTotal = 60) == False: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 15,desiredTotal = 120) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 15,desiredTotal = 120) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 14,desiredTotal = 70) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 14,desiredTotal = 70) == True: {e}')
    
    total += 1
    try:
        result = candidate(maxChoosableInteger = 10,desiredTotal = 50) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(maxChoosableInteger = 10,desiredTotal = 50) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(maxChoosableInteger = 15,desiredTotal = 50) == True
    assert candidate(maxChoosableInteger = 10,desiredTotal = 0) == True
    assert candidate(maxChoosableInteger = 10,desiredTotal = 15) == True
    assert candidate(maxChoosableInteger = 8,desiredTotal = 25) == False
    assert candidate(maxChoosableInteger = 10,desiredTotal = 40) == False
    assert candidate(maxChoosableInteger = 10,desiredTotal = 25) == True
    assert candidate(maxChoosableInteger = 20,desiredTotal = 21) == False
    assert candidate(maxChoosableInteger = 5,desiredTotal = 50) == False
    assert candidate(maxChoosableInteger = 10,desiredTotal = 100) == False
    assert candidate(maxChoosableInteger = 20,desiredTotal = 28) == True
    assert candidate(maxChoosableInteger = 15,desiredTotal = 100) == True
    assert candidate(maxChoosableInteger = 12,desiredTotal = 30) == False
    assert candidate(maxChoosableInteger = 7,desiredTotal = 15) == False
    assert candidate(maxChoosableInteger = 6,desiredTotal = 16) == True
    assert candidate(maxChoosableInteger = 10,desiredTotal = 1) == True
    assert candidate(maxChoosableInteger = 3,desiredTotal = 8) == False
    assert candidate(maxChoosableInteger = 20,desiredTotal = 300) == False
    assert candidate(maxChoosableInteger = 10,desiredTotal = 11) == False
    assert candidate(maxChoosableInteger = 16,desiredTotal = 80) == True
    assert candidate(maxChoosableInteger = 18,desiredTotal = 150) == False
    assert candidate(maxChoosableInteger = 15,desiredTotal = 70) == False
    assert candidate(maxChoosableInteger = 8,desiredTotal = 30) == True
    assert candidate(maxChoosableInteger = 20,desiredTotal = 199) == False
    assert candidate(maxChoosableInteger = 9,desiredTotal = 36) == True
    assert candidate(maxChoosableInteger = 16,desiredTotal = 85) == False
    assert candidate(maxChoosableInteger = 20,desiredTotal = 200) == False
    assert candidate(maxChoosableInteger = 18,desiredTotal = 120) == False
    assert candidate(maxChoosableInteger = 11,desiredTotal = 33) == True
    assert candidate(maxChoosableInteger = 13,desiredTotal = 45) == True
    assert candidate(maxChoosableInteger = 10,desiredTotal = 99) == False
    assert candidate(maxChoosableInteger = 16,desiredTotal = 90) == False
    assert candidate(maxChoosableInteger = 14,desiredTotal = 49) == True
    assert candidate(maxChoosableInteger = 13,desiredTotal = 30) == True
    assert candidate(maxChoosableInteger = 20,desiredTotal = 180) == False
    assert candidate(maxChoosableInteger = 14,desiredTotal = 60) == False
    assert candidate(maxChoosableInteger = 13,desiredTotal = 80) == True
    assert candidate(maxChoosableInteger = 14,desiredTotal = 80) == True
    assert candidate(maxChoosableInteger = 16,desiredTotal = 60) == True
    assert candidate(maxChoosableInteger = 12,desiredTotal = 80) == False
    assert candidate(maxChoosableInteger = 10,desiredTotal = 55) == False
    assert candidate(maxChoosableInteger = 19,desiredTotal = 135) == True
    assert candidate(maxChoosableInteger = 14,desiredTotal = 99) == False
    assert candidate(maxChoosableInteger = 19,desiredTotal = 110) == True
    assert candidate(maxChoosableInteger = 12,desiredTotal = 75) == False
    assert candidate(maxChoosableInteger = 5,desiredTotal = 15) == True
    assert candidate(maxChoosableInteger = 14,desiredTotal = 95) == False
    assert candidate(maxChoosableInteger = 7,desiredTotal = 28) == True
    assert candidate(maxChoosableInteger = 14,desiredTotal = 50) == True
    assert candidate(maxChoosableInteger = 20,desiredTotal = 250) == False
    assert candidate(maxChoosableInteger = 17,desiredTotal = 140) == True
    assert candidate(maxChoosableInteger = 19,desiredTotal = 180) == True
    assert candidate(maxChoosableInteger = 16,desiredTotal = 110) == False
    assert candidate(maxChoosableInteger = 13,desiredTotal = 60) == True
    assert candidate(maxChoosableInteger = 9,desiredTotal = 45) == True
    assert candidate(maxChoosableInteger = 12,desiredTotal = 35) == True
    assert candidate(maxChoosableInteger = 17,desiredTotal = 85) == True
    assert candidate(maxChoosableInteger = 20,desiredTotal = 150) == False
    assert candidate(maxChoosableInteger = 15,desiredTotal = 80) == True
    assert candidate(maxChoosableInteger = 8,desiredTotal = 28) == True
    assert candidate(maxChoosableInteger = 7,desiredTotal = 25) == True
    assert candidate(maxChoosableInteger = 18,desiredTotal = 130) == True
    assert candidate(maxChoosableInteger = 11,desiredTotal = 55) == True
    assert candidate(maxChoosableInteger = 17,desiredTotal = 90) == True
    assert candidate(maxChoosableInteger = 17,desiredTotal = 100) == True
    assert candidate(maxChoosableInteger = 16,desiredTotal = 120) == True
    assert candidate(maxChoosableInteger = 20,desiredTotal = 130) == False
    assert candidate(maxChoosableInteger = 19,desiredTotal = 120) == True
    assert candidate(maxChoosableInteger = 16,desiredTotal = 130) == False
    assert candidate(maxChoosableInteger = 7,desiredTotal = 20) == True
    assert candidate(maxChoosableInteger = 18,desiredTotal = 180) == False
    assert candidate(maxChoosableInteger = 18,desiredTotal = 100) == True
    assert candidate(maxChoosableInteger = 12,desiredTotal = 60) == False
    assert candidate(maxChoosableInteger = 15,desiredTotal = 120) == True
    assert candidate(maxChoosableInteger = 14,desiredTotal = 70) == True
    assert candidate(maxChoosableInteger = 10,desiredTotal = 50) == False


