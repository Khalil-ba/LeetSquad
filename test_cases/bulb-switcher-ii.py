def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1,presses = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,presses = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,presses = 1000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,presses = 1000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,presses = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,presses = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,presses = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,presses = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,presses = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,presses = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,presses = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,presses = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,presses = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,presses = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,presses = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,presses = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,presses = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,presses = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,presses = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,presses = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,presses = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,presses = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,presses = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,presses = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,presses = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,presses = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,presses = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,presses = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,presses = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,presses = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,presses = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,presses = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 65,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,presses = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,presses = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,presses = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,presses = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,presses = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,presses = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,presses = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,presses = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,presses = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,presses = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 90,presses = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 90,presses = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,presses = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,presses = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,presses = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,presses = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,presses = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,presses = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,presses = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,presses = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,presses = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,presses = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,presses = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,presses = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,presses = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,presses = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,presses = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,presses = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,presses = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,presses = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,presses = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,presses = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,presses = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,presses = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,presses = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,presses = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,presses = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,presses = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,presses = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,presses = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,presses = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,presses = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,presses = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,presses = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,presses = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,presses = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,presses = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,presses = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,presses = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,presses = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,presses = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,presses = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,presses = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,presses = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,presses = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,presses = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,presses = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,presses = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,presses = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,presses = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,presses = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,presses = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,presses = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 70,presses = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70,presses = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,presses = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,presses = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,presses = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,presses = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,presses = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,presses = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,presses = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,presses = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,presses = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,presses = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,presses = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,presses = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,presses = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,presses = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,presses = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,presses = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,presses = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,presses = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,presses = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,presses = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,presses = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,presses = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,presses = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,presses = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,presses = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,presses = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,presses = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,presses = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,presses = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,presses = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,presses = 0) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1,presses = 1) == 2
    assert candidate(n = 5,presses = 3) == 8
    assert candidate(n = 1000,presses = 1000) == 8
    assert candidate(n = 4,presses = 2) == 7
    assert candidate(n = 2,presses = 1) == 3
    assert candidate(n = 10,presses = 4) == 8
    assert candidate(n = 4,presses = 3) == 8
    assert candidate(n = 100,presses = 0) == 1
    assert candidate(n = 3,presses = 3) == 8
    assert candidate(n = 3,presses = 1) == 4
    assert candidate(n = 4,presses = 1) == 4
    assert candidate(n = 5,presses = 0) == 1
    assert candidate(n = 3,presses = 2) == 7
    assert candidate(n = 10,presses = 5) == 8
    assert candidate(n = 1000,presses = 0) == 1
    assert candidate(n = 2,presses = 2) == 4
    assert candidate(n = 10,presses = 6) == 8
    assert candidate(n = 15,presses = 5) == 8
    assert candidate(n = 100,presses = 10) == 8
    assert candidate(n = 2,presses = 0) == 1
    assert candidate(n = 5,presses = 1) == 4
    assert candidate(n = 15,presses = 6) == 8
    assert candidate(n = 6,presses = 6) == 8
    assert candidate(n = 65,presses = 5) == 8
    assert candidate(n = 10,presses = 2) == 7
    assert candidate(n = 1000,presses = 100) == 8
    assert candidate(n = 8,presses = 3) == 8
    assert candidate(n = 8,presses = 8) == 8
    assert candidate(n = 7,presses = 3) == 8
    assert candidate(n = 100,presses = 5) == 8
    assert candidate(n = 9,presses = 3) == 8
    assert candidate(n = 9,presses = 1) == 4
    assert candidate(n = 60,presses = 8) == 8
    assert candidate(n = 90,presses = 6) == 8
    assert candidate(n = 12,presses = 5) == 8
    assert candidate(n = 10,presses = 3) == 8
    assert candidate(n = 3,presses = 10) == 8
    assert candidate(n = 45,presses = 6) == 8
    assert candidate(n = 1,presses = 10) == 2
    assert candidate(n = 9,presses = 8) == 8
    assert candidate(n = 8,presses = 2) == 7
    assert candidate(n = 3,presses = 5) == 8
    assert candidate(n = 20,presses = 3) == 8
    assert candidate(n = 20,presses = 7) == 8
    assert candidate(n = 6,presses = 2) == 7
    assert candidate(n = 10,presses = 1) == 4
    assert candidate(n = 5,presses = 4) == 8
    assert candidate(n = 4,presses = 4) == 8
    assert candidate(n = 15,presses = 3) == 8
    assert candidate(n = 14,presses = 3) == 8
    assert candidate(n = 60,presses = 6) == 8
    assert candidate(n = 2,presses = 5) == 4
    assert candidate(n = 500,presses = 15) == 8
    assert candidate(n = 1,presses = 0) == 1
    assert candidate(n = 100,presses = 7) == 8
    assert candidate(n = 20,presses = 6) == 8
    assert candidate(n = 6,presses = 1) == 4
    assert candidate(n = 50,presses = 4) == 8
    assert candidate(n = 15,presses = 7) == 8
    assert candidate(n = 25,presses = 10) == 8
    assert candidate(n = 15,presses = 4) == 8
    assert candidate(n = 8,presses = 5) == 8
    assert candidate(n = 5,presses = 5) == 8
    assert candidate(n = 8,presses = 7) == 8
    assert candidate(n = 7,presses = 0) == 1
    assert candidate(n = 20,presses = 0) == 1
    assert candidate(n = 1,presses = 2) == 2
    assert candidate(n = 12,presses = 1) == 4
    assert candidate(n = 7,presses = 6) == 8
    assert candidate(n = 70,presses = 9) == 8
    assert candidate(n = 80,presses = 10) == 8
    assert candidate(n = 7,presses = 5) == 8
    assert candidate(n = 35,presses = 7) == 8
    assert candidate(n = 30,presses = 3) == 8
    assert candidate(n = 50,presses = 5) == 8
    assert candidate(n = 4,presses = 0) == 1
    assert candidate(n = 500,presses = 10) == 8
    assert candidate(n = 7,presses = 2) == 7
    assert candidate(n = 30,presses = 5) == 8
    assert candidate(n = 2,presses = 10) == 4
    assert candidate(n = 40,presses = 3) == 8
    assert candidate(n = 40,presses = 4) == 8
    assert candidate(n = 15,presses = 2) == 7
    assert candidate(n = 12,presses = 9) == 8
    assert candidate(n = 6,presses = 3) == 8
    assert candidate(n = 1000,presses = 1) == 4
    assert candidate(n = 7,presses = 4) == 8
    assert candidate(n = 20,presses = 2) == 7
    assert candidate(n = 20,presses = 4) == 8
    assert candidate(n = 3,presses = 0) == 1


