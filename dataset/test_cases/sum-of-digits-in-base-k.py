def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 64,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 42,k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42,k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 99,k = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99,k = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 81,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 34,k = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34,k = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 81,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 72,k = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72,k = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 91,k = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 91,k = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 73,k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73,k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 85,k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85,k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 63,k = 9) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63,k = 9) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 63,k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63,k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 37,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 95,k = 9) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95,k = 9) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 63,k = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 63,k = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 55,k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55,k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 31,k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31,k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 32,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 42,k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42,k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 19,k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19,k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 55,k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55,k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 84,k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84,k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 31,k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31,k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 97,k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97,k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 67,k = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67,k = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 37,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 67,k = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67,k = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 72,k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72,k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 37,k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37,k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 85,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 88,k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88,k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 95,k = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 95,k = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 67,k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67,k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 81,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 55,k = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55,k = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 98,k = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98,k = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 58,k = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 58,k = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 48,k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48,k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 31,k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 31,k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 81,k = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81,k = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 42,k = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42,k = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 77,k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77,k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 97,k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97,k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 77,k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77,k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 55,k = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 55,k = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 41,k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41,k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 98,k = 6) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 98,k = 6) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 85,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 73,k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 73,k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 77,k = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 77,k = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 85,k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 85,k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 99,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,k = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,k = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 72,k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72,k = 6) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 64,k = 2) == 1
    assert candidate(n = 7,k = 3) == 3
    assert candidate(n = 42,k = 5) == 6
    assert candidate(n = 50,k = 4) == 5
    assert candidate(n = 100,k = 3) == 4
    assert candidate(n = 10,k = 10) == 1
    assert candidate(n = 50,k = 7) == 2
    assert candidate(n = 99,k = 9) == 3
    assert candidate(n = 81,k = 9) == 1
    assert candidate(n = 34,k = 6) == 9
    assert candidate(n = 8,k = 2) == 1
    assert candidate(n = 45,k = 3) == 3
    assert candidate(n = 25,k = 2) == 3
    assert candidate(n = 81,k = 3) == 1
    assert candidate(n = 64,k = 10) == 10
    assert candidate(n = 27,k = 5) == 3
    assert candidate(n = 100,k = 2) == 3
    assert candidate(n = 1,k = 2) == 1
    assert candidate(n = 100,k = 4) == 4
    assert candidate(n = 72,k = 8) == 2
    assert candidate(n = 50,k = 5) == 2
    assert candidate(n = 17,k = 8) == 3
    assert candidate(n = 91,k = 8) == 7
    assert candidate(n = 73,k = 4) == 4
    assert candidate(n = 85,k = 7) == 7
    assert candidate(n = 63,k = 9) == 7
    assert candidate(n = 100,k = 7) == 4
    assert candidate(n = 63,k = 5) == 7
    assert candidate(n = 37,k = 5) == 5
    assert candidate(n = 95,k = 9) == 7
    assert candidate(n = 63,k = 7) == 3
    assert candidate(n = 55,k = 7) == 7
    assert candidate(n = 31,k = 5) == 3
    assert candidate(n = 32,k = 2) == 1
    assert candidate(n = 42,k = 4) == 6
    assert candidate(n = 19,k = 4) == 4
    assert candidate(n = 55,k = 6) == 5
    assert candidate(n = 100,k = 5) == 4
    assert candidate(n = 15,k = 6) == 5
    assert candidate(n = 45,k = 7) == 9
    assert candidate(n = 84,k = 4) == 3
    assert candidate(n = 31,k = 10) == 4
    assert candidate(n = 45,k = 6) == 5
    assert candidate(n = 97,k = 5) == 9
    assert candidate(n = 45,k = 10) == 9
    assert candidate(n = 50,k = 8) == 8
    assert candidate(n = 67,k = 5) == 7
    assert candidate(n = 37,k = 2) == 3
    assert candidate(n = 67,k = 7) == 7
    assert candidate(n = 29,k = 3) == 3
    assert candidate(n = 50,k = 6) == 5
    assert candidate(n = 72,k = 5) == 8
    assert candidate(n = 37,k = 6) == 2
    assert candidate(n = 85,k = 3) == 3
    assert candidate(n = 88,k = 3) == 4
    assert candidate(n = 64,k = 3) == 4
    assert candidate(n = 64,k = 4) == 1
    assert candidate(n = 95,k = 6) == 10
    assert candidate(n = 67,k = 3) == 5
    assert candidate(n = 100,k = 10) == 1
    assert candidate(n = 81,k = 5) == 5
    assert candidate(n = 55,k = 5) == 3
    assert candidate(n = 98,k = 2) == 3
    assert candidate(n = 58,k = 7) == 4
    assert candidate(n = 48,k = 4) == 3
    assert candidate(n = 31,k = 2) == 5
    assert candidate(n = 81,k = 8) == 4
    assert candidate(n = 42,k = 7) == 6
    assert candidate(n = 27,k = 9) == 3
    assert candidate(n = 77,k = 7) == 5
    assert candidate(n = 29,k = 8) == 8
    assert candidate(n = 97,k = 10) == 16
    assert candidate(n = 77,k = 4) == 5
    assert candidate(n = 13,k = 6) == 3
    assert candidate(n = 49,k = 9) == 9
    assert candidate(n = 55,k = 10) == 10
    assert candidate(n = 41,k = 4) == 5
    assert candidate(n = 98,k = 6) == 8
    assert candidate(n = 50,k = 3) == 6
    assert candidate(n = 85,k = 5) == 5
    assert candidate(n = 73,k = 8) == 3
    assert candidate(n = 100,k = 9) == 4
    assert candidate(n = 77,k = 8) == 7
    assert candidate(n = 85,k = 4) == 4
    assert candidate(n = 99,k = 3) == 3
    assert candidate(n = 29,k = 4) == 5
    assert candidate(n = 72,k = 6) == 2


