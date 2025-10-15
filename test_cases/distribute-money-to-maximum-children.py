def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(money = 150,children = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 150,children = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(money = 100,children = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 100,children = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(money = 15,children = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 15,children = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(money = 31,children = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 31,children = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(money = 7,children = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 7,children = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 25,children = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 25,children = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(money = 8,children = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 8,children = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 50,children = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 50,children = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(money = 28,children = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 28,children = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(money = 25,children = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 25,children = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(money = 150,children = 20) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 150,children = 20) == 18: {e}')
    
    total += 1
    try:
        result = candidate(money = 199,children = 25) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 199,children = 25) == 24: {e}')
    
    total += 1
    try:
        result = candidate(money = 100,children = 12) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 100,children = 12) == 11: {e}')
    
    total += 1
    try:
        result = candidate(money = 7,children = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 7,children = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 16,children = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 16,children = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(money = 40,children = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 40,children = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(money = 30,children = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 30,children = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(money = 300,children = 30) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 300,children = 30) == 29: {e}')
    
    total += 1
    try:
        result = candidate(money = 3,children = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 3,children = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 4,children = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 4,children = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 30,children = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 30,children = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(money = 31,children = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 31,children = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(money = 8,children = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 8,children = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 20,children = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 20,children = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(money = 200,children = 30) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 200,children = 30) == 24: {e}')
    
    total += 1
    try:
        result = candidate(money = 72,children = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 72,children = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(money = 300,children = 25) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 300,children = 25) == 24: {e}')
    
    total += 1
    try:
        result = candidate(money = 28,children = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 28,children = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(money = 7,children = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 7,children = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 32,children = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 32,children = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(money = 12,children = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 12,children = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 25,children = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 25,children = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(money = 6,children = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 6,children = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 4,children = 1) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 4,children = 1) == -1: {e}')
    
    total += 1
    try:
        result = candidate(money = 1,children = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 1,children = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(money = 200,children = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 200,children = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(money = 8,children = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 8,children = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(money = 10,children = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 10,children = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(money = 30,children = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 30,children = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(money = 50,children = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 50,children = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(money = 100,children = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 100,children = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(money = 1,children = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 1,children = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 15,children = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 15,children = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(money = 56,children = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 56,children = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(money = 24,children = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 24,children = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(money = 5,children = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 5,children = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(money = 50,children = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(money = 50,children = 5) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(money = 150,children = 15) == 14
    assert candidate(money = 100,children = 5) == 4
    assert candidate(money = 15,children = 3) == 1
    assert candidate(money = 31,children = 3) == 2
    assert candidate(money = 7,children = 2) == 0
    assert candidate(money = 25,children = 4) == 3
    assert candidate(money = 8,children = 8) == 0
    assert candidate(money = 50,children = 6) == 5
    assert candidate(money = 28,children = 3) == 2
    assert candidate(money = 25,children = 5) == 2
    assert candidate(money = 150,children = 20) == 18
    assert candidate(money = 199,children = 25) == 24
    assert candidate(money = 100,children = 12) == 11
    assert candidate(money = 7,children = 3) == 0
    assert candidate(money = 16,children = 2) == 2
    assert candidate(money = 40,children = 5) == 5
    assert candidate(money = 30,children = 4) == 3
    assert candidate(money = 300,children = 30) == 29
    assert candidate(money = 3,children = 2) == 0
    assert candidate(money = 4,children = 2) == 0
    assert candidate(money = 30,children = 3) == 2
    assert candidate(money = 31,children = 4) == 3
    assert candidate(money = 8,children = 2) == 0
    assert candidate(money = 20,children = 3) == 1
    assert candidate(money = 200,children = 30) == 24
    assert candidate(money = 72,children = 9) == 9
    assert candidate(money = 300,children = 25) == 24
    assert candidate(money = 28,children = 4) == 2
    assert candidate(money = 7,children = 1) == 0
    assert candidate(money = 32,children = 4) == 4
    assert candidate(money = 12,children = 2) == 0
    assert candidate(money = 25,children = 3) == 2
    assert candidate(money = 6,children = 2) == 0
    assert candidate(money = 4,children = 1) == -1
    assert candidate(money = 1,children = 2) == -1
    assert candidate(money = 200,children = 25) == 25
    assert candidate(money = 8,children = 1) == 1
    assert candidate(money = 10,children = 2) == 1
    assert candidate(money = 30,children = 5) == 3
    assert candidate(money = 50,children = 7) == 6
    assert candidate(money = 100,children = 10) == 9
    assert candidate(money = 1,children = 1) == 0
    assert candidate(money = 15,children = 2) == 1
    assert candidate(money = 56,children = 7) == 7
    assert candidate(money = 24,children = 3) == 3
    assert candidate(money = 5,children = 2) == 0
    assert candidate(money = 50,children = 5) == 4


