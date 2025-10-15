def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(red = 100,blue = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 100,blue = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(red = 3,blue = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 3,blue = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(red = 50,blue = 50) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 50,blue = 50) == 13: {e}')
    
    total += 1
    try:
        result = candidate(red = 5,blue = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 5,blue = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(red = 1,blue = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 1,blue = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(red = 10,blue = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 10,blue = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(red = 1,blue = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 1,blue = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(red = 2,blue = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 2,blue = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(red = 2,blue = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 2,blue = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(red = 100,blue = 100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 100,blue = 100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(red = 15,blue = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 15,blue = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 20,blue = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 20,blue = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(red = 30,blue = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 30,blue = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(red = 25,blue = 25) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 25,blue = 25) == 9: {e}')
    
    total += 1
    try:
        result = candidate(red = 8,blue = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 8,blue = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(red = 15,blue = 14) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 15,blue = 14) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 30,blue = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 30,blue = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 33,blue = 66) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 33,blue = 66) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 7,blue = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 7,blue = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(red = 40,blue = 40) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 40,blue = 40) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 15,blue = 85) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 15,blue = 85) == 7: {e}')
    
    total += 1
    try:
        result = candidate(red = 10,blue = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 10,blue = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 70,blue = 30) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 70,blue = 30) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 30,blue = 70) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 30,blue = 70) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 50,blue = 30) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 50,blue = 30) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 40,blue = 39) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 40,blue = 39) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 49,blue = 49) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 49,blue = 49) == 13: {e}')
    
    total += 1
    try:
        result = candidate(red = 10,blue = 90) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 10,blue = 90) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 3,blue = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 3,blue = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(red = 42,blue = 42) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 42,blue = 42) == 12: {e}')
    
    total += 1
    try:
        result = candidate(red = 7,blue = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 7,blue = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(red = 7,blue = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 7,blue = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(red = 15,blue = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 15,blue = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 30,blue = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 30,blue = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(red = 55,blue = 45) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 55,blue = 45) == 13: {e}')
    
    total += 1
    try:
        result = candidate(red = 40,blue = 60) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 40,blue = 60) == 12: {e}')
    
    total += 1
    try:
        result = candidate(red = 12,blue = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 12,blue = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 50,blue = 60) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 50,blue = 60) == 14: {e}')
    
    total += 1
    try:
        result = candidate(red = 30,blue = 40) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 30,blue = 40) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 20,blue = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 20,blue = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(red = 10,blue = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 10,blue = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 99,blue = 99) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 99,blue = 99) == 18: {e}')
    
    total += 1
    try:
        result = candidate(red = 3,blue = 97) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 3,blue = 97) == 3: {e}')
    
    total += 1
    try:
        result = candidate(red = 99,blue = 100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 99,blue = 100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(red = 90,blue = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 90,blue = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 99,blue = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 99,blue = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(red = 45,blue = 55) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 45,blue = 55) == 13: {e}')
    
    total += 1
    try:
        result = candidate(red = 99,blue = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 99,blue = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(red = 35,blue = 65) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 35,blue = 65) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 60,blue = 40) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 60,blue = 40) == 12: {e}')
    
    total += 1
    try:
        result = candidate(red = 25,blue = 75) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 25,blue = 75) == 10: {e}')
    
    total += 1
    try:
        result = candidate(red = 2,blue = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 2,blue = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(red = 50,blue = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 50,blue = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(red = 1,blue = 99) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 1,blue = 99) == 2: {e}')
    
    total += 1
    try:
        result = candidate(red = 20,blue = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 20,blue = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(red = 100,blue = 50) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 100,blue = 50) == 14: {e}')
    
    total += 1
    try:
        result = candidate(red = 8,blue = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 8,blue = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(red = 50,blue = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 50,blue = 25) == 10: {e}')
    
    total += 1
    try:
        result = candidate(red = 10,blue = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 10,blue = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(red = 15,blue = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 15,blue = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(red = 75,blue = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 75,blue = 25) == 10: {e}')
    
    total += 1
    try:
        result = candidate(red = 5,blue = 95) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 5,blue = 95) == 4: {e}')
    
    total += 1
    try:
        result = candidate(red = 80,blue = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 80,blue = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(red = 20,blue = 80) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 20,blue = 80) == 9: {e}')
    
    total += 1
    try:
        result = candidate(red = 30,blue = 50) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 30,blue = 50) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 33,blue = 67) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 33,blue = 67) == 11: {e}')
    
    total += 1
    try:
        result = candidate(red = 100,blue = 99) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(red = 100,blue = 99) == 19: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(red = 100,blue = 1) == 2
    assert candidate(red = 3,blue = 7) == 3
    assert candidate(red = 50,blue = 50) == 13
    assert candidate(red = 5,blue = 5) == 3
    assert candidate(red = 1,blue = 1) == 1
    assert candidate(red = 10,blue = 1) == 2
    assert candidate(red = 1,blue = 100) == 2
    assert candidate(red = 2,blue = 1) == 2
    assert candidate(red = 2,blue = 4) == 3
    assert candidate(red = 100,blue = 100) == 19
    assert candidate(red = 15,blue = 10) == 6
    assert candidate(red = 20,blue = 15) == 7
    assert candidate(red = 30,blue = 30) == 10
    assert candidate(red = 25,blue = 25) == 9
    assert candidate(red = 8,blue = 8) == 4
    assert candidate(red = 15,blue = 14) == 6
    assert candidate(red = 30,blue = 10) == 6
    assert candidate(red = 33,blue = 66) == 11
    assert candidate(red = 7,blue = 12) == 5
    assert candidate(red = 40,blue = 40) == 11
    assert candidate(red = 15,blue = 85) == 7
    assert candidate(red = 10,blue = 15) == 6
    assert candidate(red = 70,blue = 30) == 11
    assert candidate(red = 30,blue = 70) == 11
    assert candidate(red = 50,blue = 30) == 11
    assert candidate(red = 40,blue = 39) == 11
    assert candidate(red = 49,blue = 49) == 13
    assert candidate(red = 10,blue = 90) == 6
    assert candidate(red = 3,blue = 5) == 3
    assert candidate(red = 42,blue = 42) == 12
    assert candidate(red = 7,blue = 9) == 5
    assert candidate(red = 7,blue = 3) == 3
    assert candidate(red = 15,blue = 15) == 6
    assert candidate(red = 30,blue = 20) == 9
    assert candidate(red = 55,blue = 45) == 13
    assert candidate(red = 40,blue = 60) == 12
    assert candidate(red = 12,blue = 12) == 6
    assert candidate(red = 50,blue = 60) == 14
    assert candidate(red = 30,blue = 40) == 11
    assert candidate(red = 20,blue = 20) == 8
    assert candidate(red = 10,blue = 20) == 6
    assert candidate(red = 99,blue = 99) == 18
    assert candidate(red = 3,blue = 97) == 3
    assert candidate(red = 99,blue = 100) == 19
    assert candidate(red = 90,blue = 10) == 6
    assert candidate(red = 99,blue = 2) == 3
    assert candidate(red = 45,blue = 55) == 13
    assert candidate(red = 99,blue = 1) == 2
    assert candidate(red = 35,blue = 65) == 11
    assert candidate(red = 60,blue = 40) == 12
    assert candidate(red = 25,blue = 75) == 10
    assert candidate(red = 2,blue = 2) == 2
    assert candidate(red = 50,blue = 100) == 14
    assert candidate(red = 1,blue = 99) == 2
    assert candidate(red = 20,blue = 10) == 6
    assert candidate(red = 100,blue = 50) == 14
    assert candidate(red = 8,blue = 7) == 4
    assert candidate(red = 50,blue = 25) == 10
    assert candidate(red = 10,blue = 10) == 5
    assert candidate(red = 15,blue = 20) == 7
    assert candidate(red = 75,blue = 25) == 10
    assert candidate(red = 5,blue = 95) == 4
    assert candidate(red = 80,blue = 20) == 9
    assert candidate(red = 20,blue = 80) == 9
    assert candidate(red = 30,blue = 50) == 11
    assert candidate(red = 33,blue = 67) == 11
    assert candidate(red = 100,blue = 99) == 19


