def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8,m = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,m = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,m = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 14) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 14) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 9) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 9) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,m = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,m = 13) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 13) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 13) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 12) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 12) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 11) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 11) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,m = 13) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,m = 13) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,m = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,m = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,m = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,m = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,m = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,m = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 12) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 12) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 14) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 14) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 13) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,m = 14) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,m = 14) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,m = 13) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,m = 13) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 13) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,m = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,m = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,m = 12) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,m = 12) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,m = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,m = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 14) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 14) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 13) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 13) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 11) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 11) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,m = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,m = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,m = 14) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,m = 14) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,m = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,m = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,m = 9) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,m = 9) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,m = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,m = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,m = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,m = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,m = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,m = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,m = 13) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,m = 13) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,m = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,m = 10) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8,m = 8) == 1
    assert candidate(n = 1,m = 1) == 1
    assert candidate(n = 10,m = 14) == 5
    assert candidate(n = 7,m = 7) == 1
    assert candidate(n = 9,m = 10) == 6
    assert candidate(n = 7,m = 8) == 7
    assert candidate(n = 6,m = 7) == 5
    assert candidate(n = 6,m = 10) == 4
    assert candidate(n = 8,m = 9) == 7
    assert candidate(n = 3,m = 3) == 1
    assert candidate(n = 4,m = 10) == 4
    assert candidate(n = 11,m = 13) == 6
    assert candidate(n = 5,m = 8) == 5
    assert candidate(n = 12,m = 13) == 7
    assert candidate(n = 4,m = 6) == 3
    assert candidate(n = 10,m = 11) == 6
    assert candidate(n = 9,m = 12) == 4
    assert candidate(n = 9,m = 11) == 7
    assert candidate(n = 13,m = 13) == 1
    assert candidate(n = 3,m = 5) == 4
    assert candidate(n = 2,m = 3) == 3
    assert candidate(n = 10,m = 10) == 1
    assert candidate(n = 6,m = 6) == 1
    assert candidate(n = 7,m = 12) == 6
    assert candidate(n = 3,m = 11) == 6
    assert candidate(n = 11,m = 10) == 6
    assert candidate(n = 13,m = 5) == 6
    assert candidate(n = 12,m = 7) == 6
    assert candidate(n = 13,m = 7) == 6
    assert candidate(n = 5,m = 11) == 6
    assert candidate(n = 5,m = 12) == 6
    assert candidate(n = 3,m = 14) == 7
    assert candidate(n = 8,m = 15) == 8
    assert candidate(n = 7,m = 13) == 6
    assert candidate(n = 9,m = 9) == 1
    assert candidate(n = 3,m = 7) == 5
    assert candidate(n = 4,m = 15) == 7
    assert candidate(n = 6,m = 11) == 6
    assert candidate(n = 14,m = 14) == 1
    assert candidate(n = 2,m = 13) == 8
    assert candidate(n = 6,m = 13) == 6
    assert candidate(n = 6,m = 9) == 3
    assert candidate(n = 4,m = 9) == 6
    assert candidate(n = 8,m = 12) == 3
    assert candidate(n = 4,m = 11) == 6
    assert candidate(n = 13,m = 12) == 7
    assert candidate(n = 10,m = 5) == 2
    assert candidate(n = 4,m = 7) == 5
    assert candidate(n = 7,m = 10) == 6
    assert candidate(n = 12,m = 5) == 6
    assert candidate(n = 12,m = 14) == 5
    assert candidate(n = 9,m = 7) == 6
    assert candidate(n = 10,m = 12) == 5
    assert candidate(n = 8,m = 13) == 6
    assert candidate(n = 12,m = 11) == 7
    assert candidate(n = 10,m = 15) == 3
    assert candidate(n = 9,m = 14) == 7
    assert candidate(n = 8,m = 10) == 5
    assert candidate(n = 3,m = 10) == 6
    assert candidate(n = 11,m = 9) == 7
    assert candidate(n = 8,m = 11) == 6
    assert candidate(n = 13,m = 6) == 6
    assert candidate(n = 5,m = 9) == 6
    assert candidate(n = 4,m = 13) == 7
    assert candidate(n = 12,m = 15) == 5
    assert candidate(n = 12,m = 10) == 5


