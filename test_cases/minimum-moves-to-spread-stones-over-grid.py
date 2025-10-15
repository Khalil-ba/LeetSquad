def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [[2, 2, 1], [1, 1, 1], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 2, 1], [1, 1, 1], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 9], [0, 0, 0], [0, 0, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 9], [0, 0, 0], [0, 0, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 2, 1], [1, 1, 1], [1, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 2, 1], [1, 1, 1], [1, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 3, 0], [1, 0, 0], [1, 0, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 3, 0], [1, 0, 0], [1, 0, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1], [1, 2, 2], [2, 2, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1], [1, 2, 2], [2, 2, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 2], [2, 1, 1], [2, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 2], [2, 1, 1], [2, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 0], [1, 1, 1], [1, 2, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 0], [1, 1, 1], [1, 2, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [0, 9, 0], [0, 0, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [0, 9, 0], [0, 0, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 1, 1], [0, 0, 0], [1, 1, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 1, 1], [0, 0, 0], [1, 1, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 9]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 9]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0], [0, 0, 0], [0, 0, 8]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0], [0, 0, 0], [0, 0, 8]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 2, 0], [1, 0, 2], [0, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 2, 0], [1, 0, 2], [0, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 0], [1, 0, 0], [0, 0, 7]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 0], [1, 0, 0], [0, 0, 7]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2], [3, 0, 0], [0, 0, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2], [3, 0, 0], [0, 0, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [0, 0, 2], [0, 0, 7]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [0, 0, 2], [0, 0, 7]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 1, 0], [1, 1, 1], [0, 1, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 1, 0], [1, 1, 1], [0, 1, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 0, 1], [1, 0, 3], [0, 3, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 0, 1], [1, 0, 3], [0, 3, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 0, 1], [0, 0, 0], [1, 0, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 0, 1], [0, 0, 0], [1, 0, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 2], [2, 0, 0], [0, 1, 3]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 2], [2, 0, 0], [0, 1, 3]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 2, 0], [3, 0, 0], [0, 1, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 2, 0], [3, 0, 0], [0, 1, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 0], [0, 0, 3], [0, 3, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 0], [0, 0, 3], [0, 3, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 1], [1, 7, 0], [0, 0, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 1], [1, 7, 0], [0, 0, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 2, 2], [1, 1, 1], [0, 0, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 2, 2], [1, 1, 1], [0, 0, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 0], [0, 0, 0], [0, 0, 7]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 0], [0, 0, 0], [0, 0, 7]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 0], [0, 1, 2], [2, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 0], [0, 1, 2], [2, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 2, 0], [1, 0, 3], [0, 4, 0]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 2, 0], [1, 0, 3], [0, 4, 0]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [0, 8, 1], [0, 0, 0]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [0, 8, 1], [0, 0, 0]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 0], [0, 7, 0], [0, 1, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 0], [0, 7, 0], [0, 1, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 0], [2, 0, 1], [0, 3, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 0], [2, 0, 1], [0, 3, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 2], [2, 1, 1], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 2], [2, 1, 1], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 2, 0], [1, 1, 0], [0, 0, 3]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 2, 0], [1, 1, 0], [0, 0, 3]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 2, 1], [1, 0, 1], [1, 1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 2, 1], [1, 0, 1], [1, 1, 2]]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [[2, 2, 1], [1, 1, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[0, 0, 9], [0, 0, 0], [0, 0, 0]]) == 18
    assert candidate(grid = [[2, 2, 1], [1, 1, 1], [1, 1, 2]]) == 0
    assert candidate(grid = [[1, 3, 0], [1, 0, 0], [1, 0, 3]]) == 4
    assert candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]) == 0
    assert candidate(grid = [[1, 1, 1], [1, 2, 2], [2, 2, 1]]) == 0
    assert candidate(grid = [[1, 2, 2], [2, 1, 1], [2, 1, 1]]) == 0
    assert candidate(grid = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]) == 8
    assert candidate(grid = [[1, 1, 0], [1, 1, 1], [1, 2, 1]]) == 3
    assert candidate(grid = [[0, 0, 0], [0, 9, 0], [0, 0, 0]]) == 12
    assert candidate(grid = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[3, 1, 1], [0, 0, 0], [1, 1, 3]]) == 4
    assert candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 9]]) == 18
    assert candidate(grid = [[1, 0, 0], [0, 0, 0], [0, 0, 8]]) == 14
    assert candidate(grid = [[2, 2, 0], [1, 0, 2], [0, 1, 1]]) == 4
    assert candidate(grid = [[0, 1, 0], [1, 0, 0], [0, 0, 7]]) == 12
    assert candidate(grid = [[0, 1, 2], [3, 0, 0], [0, 0, 3]]) == 6
    assert candidate(grid = [[0, 0, 0], [0, 0, 2], [0, 0, 7]]) == 16
    assert candidate(grid = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]) == 4
    assert candidate(grid = [[2, 1, 0], [1, 1, 1], [0, 1, 2]]) == 4
    assert candidate(grid = [[2, 0, 1], [1, 0, 3], [0, 3, 0]]) == 4
    assert candidate(grid = [[4, 0, 1], [0, 0, 0], [1, 0, 3]]) == 6
    assert candidate(grid = [[1, 0, 2], [2, 0, 0], [0, 1, 3]]) == 5
    assert candidate(grid = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]) == 4
    assert candidate(grid = [[0, 2, 0], [3, 0, 0], [0, 1, 3]]) == 6
    assert candidate(grid = [[3, 0, 0], [0, 0, 3], [0, 3, 0]]) == 6
    assert candidate(grid = [[0, 0, 1], [1, 7, 0], [0, 0, 1]]) == 7
    assert candidate(grid = [[2, 2, 2], [1, 1, 1], [0, 0, 0]]) == 6
    assert candidate(grid = [[1, 1, 0], [0, 0, 0], [0, 0, 7]]) == 11
    assert candidate(grid = [[1, 2, 0], [0, 1, 2], [2, 0, 1]]) == 4
    assert candidate(grid = [[0, 2, 0], [1, 0, 3], [0, 4, 0]]) == 5
    assert candidate(grid = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]) == 6
    assert candidate(grid = [[0, 0, 0], [0, 8, 1], [0, 0, 0]]) == 11
    assert candidate(grid = [[0, 1, 0], [0, 7, 0], [0, 1, 0]]) == 10
    assert candidate(grid = [[1, 2, 0], [2, 0, 1], [0, 3, 0]]) == 4
    assert candidate(grid = [[1, 2, 2], [2, 1, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[2, 2, 0], [1, 1, 0], [0, 0, 3]]) == 5
    assert candidate(grid = [[2, 2, 1], [1, 0, 1], [1, 1, 2]]) == 1


