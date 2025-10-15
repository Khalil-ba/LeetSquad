def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X'], ['Y', 'X', 'Y'], ['X', 'Y', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X'], ['Y', 'X', 'Y'], ['X', 'Y', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['.', '.'], ['.', '.']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['.', '.'], ['.', '.']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X'], ['X', 'Y']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X'], ['X', 'Y']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'X', 'X'], ['X', 'Y', 'Y', 'X'], ['X', 'Y', 'Y', 'X'], ['X', 'X', 'X', 'X']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'X', 'X'], ['X', 'Y', 'Y', 'X'], ['X', 'Y', 'Y', 'X'], ['X', 'X', 'X', 'X']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', '.', 'Y'], ['.', 'X', 'Y'], ['Y', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', '.', 'Y'], ['.', 'X', 'Y'], ['Y', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X'], ['Y'], ['X']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X'], ['Y'], ['X']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', '.'], ['Y', '.', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', '.'], ['Y', '.', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y'], ['X', 'Y'], ['X', 'Y']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y'], ['X', 'Y'], ['X', 'Y']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'Y'], ['Y', 'Y', 'X'], ['X', 'Y', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'Y'], ['Y', 'Y', 'X'], ['X', 'Y', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y'], ['Y', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y'], ['Y', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'X'], ['Y', 'Y', 'Y'], ['.', '.', '.']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'X'], ['Y', 'Y', 'Y'], ['.', '.', '.']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', '.', 'Y'], ['.', 'X', '.'], ['Y', '.', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', '.', 'Y'], ['.', 'X', '.'], ['Y', '.', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', '.'], ['.', 'X', 'Y'], ['Y', 'X', '.']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', '.'], ['.', 'X', 'Y'], ['Y', 'X', '.']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X'], ['X', 'Y', 'X'], ['X', 'Y', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X'], ['X', 'Y', 'X'], ['X', 'Y', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'Y']]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'Y']]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X'], ['Y', '.', 'X'], ['X', 'Y', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X'], ['Y', '.', 'X'], ['X', 'Y', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['.', '.', '.', 'X', 'Y'], ['.', 'X', 'Y', '.', '.'], ['.', 'Y', 'X', '.', '.'], ['X', '.', '.', 'Y', '.'], ['Y', '.', '.', '.', 'X']]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['.', '.', '.', 'X', 'Y'], ['.', 'X', 'Y', '.', '.'], ['.', 'Y', 'X', '.', '.'], ['X', '.', '.', 'Y', '.'], ['Y', '.', '.', '.', 'X']]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X']]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X']]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'X'], ['Y', 'Y', 'Y'], ['X', 'Y', 'X'], ['Y', 'X', 'Y']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'X'], ['Y', 'Y', 'Y'], ['X', 'Y', 'X'], ['Y', 'X', 'Y']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'X', 'Y'], ['X', 'X', 'Y', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'X', 'Y'], ['X', 'X', 'Y', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'Y', 'X'], ['Y', 'X', 'X', 'Y'], ['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X']]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'Y', 'X'], ['Y', 'X', 'X', 'Y'], ['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X']]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', '.', 'X', 'Y'], ['Y', 'X', 'Y', '.'], ['.', 'Y', 'X', 'X'], ['X', 'Y', '.', 'Y']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', '.', 'X', 'Y'], ['Y', 'X', 'Y', '.'], ['.', 'Y', 'X', 'X'], ['X', 'Y', '.', 'Y']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['.', '.', 'X', 'Y', '.'], ['X', 'Y', '.', 'X', 'Y'], ['Y', 'X', 'X', 'Y', 'X'], ['.', 'Y', 'X', '.', 'Y'], ['X', '.', 'Y', 'X', '.']]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['.', '.', 'X', 'Y', '.'], ['X', 'Y', '.', 'X', 'Y'], ['Y', 'X', 'X', 'Y', 'X'], ['.', 'Y', 'X', '.', 'Y'], ['X', '.', 'Y', 'X', '.']]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'X', 'Y'], ['Y', 'Y', 'X', 'X'], ['X', 'Y', 'X', 'X'], ['Y', 'X', 'Y', 'Y']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'X', 'Y'], ['Y', 'Y', 'X', 'X'], ['X', 'Y', 'X', 'X'], ['Y', 'X', 'Y', 'Y']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'Y'], ['X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'Y']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'Y'], ['X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'Y']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X']]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X']]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', '.', '.', 'Y', '.', '.', 'X', '.', 'Y', '.'], ['.', 'X', '.', '.', 'Y', '.', '.', 'X', '.', 'Y'], ['.', '.', 'X', '.', '.', 'Y', '.', '.', 'X', '.'], ['Y', '.', '.', 'X', '.', '.', 'Y', '.', '.', 'X']]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', '.', '.', 'Y', '.', '.', 'X', '.', 'Y', '.'], ['.', 'X', '.', '.', 'Y', '.', '.', 'X', '.', 'Y'], ['.', '.', 'X', '.', '.', 'Y', '.', '.', 'X', '.'], ['Y', '.', '.', 'X', '.', '.', 'Y', '.', '.', 'X']]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y']]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y']]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X']]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X']]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', '.', 'X'], ['Y', 'X', '.', 'Y'], ['.', '.', '.', '.'], ['X', 'Y', 'X', 'Y']]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', '.', 'X'], ['Y', 'X', '.', 'Y'], ['.', '.', '.', '.'], ['X', 'Y', 'X', 'Y']]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'Y', 'Y'], ['X', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y'], ['X', 'X', 'X', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'Y', 'Y'], ['X', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y'], ['X', 'X', 'X', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['.', '.', 'X'], ['Y', 'X', 'Y'], ['X', 'Y', 'X'], ['Y', '.', 'Y']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['.', '.', 'X'], ['Y', 'X', 'Y'], ['X', 'Y', 'X'], ['Y', '.', 'Y']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', '.', 'Y', 'X'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', '.'], ['.', 'X', 'Y', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', '.', 'Y', 'X'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', '.'], ['.', 'X', 'Y', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['.', '.', '.', '.'], ['.', 'X', 'Y', '.'], ['.', 'Y', 'X', '.'], ['.', '.', '.', '.']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['.', '.', '.', '.'], ['.', 'X', 'Y', '.'], ['.', 'Y', 'X', '.'], ['.', '.', '.', '.']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['.', '.', 'X', 'Y', '.'], ['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['.', 'X', 'Y', 'X', 'Y']]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['.', '.', 'X', 'Y', '.'], ['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['.', 'X', 'Y', 'X', 'Y']]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [['X', 'Y', 'X'], ['Y', 'X', 'Y'], ['X', 'Y', 'X']]) == 5
    assert candidate(grid = [['.', '.'], ['.', '.']]) == 0
    assert candidate(grid = [['X', 'X'], ['X', 'Y']]) == 0
    assert candidate(grid = [['X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X']]) == 5
    assert candidate(grid = [['X', 'X', 'X', 'X'], ['X', 'Y', 'Y', 'X'], ['X', 'Y', 'Y', 'X'], ['X', 'X', 'X', 'X']]) == 0
    assert candidate(grid = [['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y']]) == 8
    assert candidate(grid = [['X', '.', 'Y'], ['.', 'X', 'Y'], ['Y', '.', 'X']]) == 4
    assert candidate(grid = [['X'], ['Y'], ['X']]) == 1
    assert candidate(grid = [['X', 'Y', '.'], ['Y', '.', '.']]) == 3
    assert candidate(grid = [['X', 'Y'], ['X', 'Y'], ['X', 'Y']]) == 3
    assert candidate(grid = [['X', 'X', 'Y'], ['Y', 'Y', 'X'], ['X', 'Y', 'X']]) == 4
    assert candidate(grid = [['X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y']]) == 6
    assert candidate(grid = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]) == 0
    assert candidate(grid = [['X', 'Y'], ['Y', 'X']]) == 3
    assert candidate(grid = [['X', 'X', 'X'], ['Y', 'Y', 'Y'], ['.', '.', '.']]) == 6
    assert candidate(grid = [['X', '.', 'Y'], ['.', 'X', '.'], ['Y', '.', 'X']]) == 2
    assert candidate(grid = [['X', 'Y', '.'], ['.', 'X', 'Y'], ['Y', 'X', '.']]) == 5
    assert candidate(grid = [['X', 'Y', 'X'], ['X', 'Y', 'X'], ['X', 'Y', 'X']]) == 3
    assert candidate(grid = [['X', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'Y']]) == 19
    assert candidate(grid = [['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y']]) == 0
    assert candidate(grid = [['X', 'Y', 'X'], ['Y', '.', 'X'], ['X', 'Y', '.']]) == 2
    assert candidate(grid = [['.', '.', '.', 'X', 'Y'], ['.', 'X', 'Y', '.', '.'], ['.', 'Y', 'X', '.', '.'], ['X', '.', '.', 'Y', '.'], ['Y', '.', '.', '.', 'X']]) == 12
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X']]) == 15
    assert candidate(grid = [['X', 'X', 'X'], ['Y', 'Y', 'Y'], ['X', 'Y', 'X'], ['Y', 'X', 'Y']]) == 7
    assert candidate(grid = [['X', 'Y', 'X', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'X', 'Y'], ['X', 'X', 'Y', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y']]) == 6
    assert candidate(grid = [['X', 'Y', 'Y', 'X'], ['Y', 'X', 'X', 'Y'], ['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X']]) == 12
    assert candidate(grid = [['X', '.', 'X', 'Y'], ['Y', 'X', 'Y', '.'], ['.', 'Y', 'X', 'X'], ['X', 'Y', '.', 'Y']]) == 6
    assert candidate(grid = [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 0
    assert candidate(grid = [['.', '.', 'X', 'Y', '.'], ['X', 'Y', '.', 'X', 'Y'], ['Y', 'X', 'X', 'Y', 'X'], ['.', 'Y', 'X', '.', 'Y'], ['X', '.', 'Y', 'X', '.']]) == 9
    assert candidate(grid = [['X', 'X', 'X', 'Y'], ['Y', 'Y', 'X', 'X'], ['X', 'Y', 'X', 'X'], ['Y', 'X', 'Y', 'Y']]) == 5
    assert candidate(grid = [['X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'Y'], ['X', 'X', 'Y', 'X'], ['Y', 'Y', 'X', 'Y']]) == 8
    assert candidate(grid = [['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X']]) == 12
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 13
    assert candidate(grid = [['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['Y', 'Y', 'Y', 'Y', 'Y', 'Y'], ['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']]) == 6
    assert candidate(grid = [['X', '.', '.', 'Y', '.', '.', 'X', '.', 'Y', '.'], ['.', 'X', '.', '.', 'Y', '.', '.', 'X', '.', 'Y'], ['.', '.', 'X', '.', '.', 'Y', '.', '.', 'X', '.'], ['Y', '.', '.', 'X', '.', '.', 'Y', '.', '.', 'X']]) == 12
    assert candidate(grid = [['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y'], ['Y', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y']]) == 12
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['X', 'Y', 'X', 'Y', 'X']]) == 16
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], ['Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 16
    assert candidate(grid = [['X', 'Y', '.', 'X'], ['Y', 'X', '.', 'Y'], ['.', '.', '.', '.'], ['X', 'Y', 'X', 'Y']]) == 12
    assert candidate(grid = [['X', 'Y', 'Y', 'Y'], ['X', 'Y', 'X', 'X'], ['X', 'X', 'Y', 'Y'], ['X', 'X', 'X', 'X']]) == 5
    assert candidate(grid = [['.', '.', 'X'], ['Y', 'X', 'Y'], ['X', 'Y', 'X'], ['Y', '.', 'Y']]) == 4
    assert candidate(grid = [['X', '.', 'Y', 'X'], ['Y', 'X', 'Y', 'X'], ['X', 'Y', 'X', '.'], ['.', 'X', 'Y', 'X']]) == 4
    assert candidate(grid = [['.', '.', '.', '.'], ['.', 'X', 'Y', '.'], ['.', 'Y', 'X', '.'], ['.', '.', '.', '.']]) == 8
    assert candidate(grid = [['.', '.', 'X', 'Y', '.'], ['X', 'Y', 'X', 'Y', 'X'], ['Y', 'X', 'Y', 'X', 'Y'], ['.', 'X', 'Y', 'X', 'Y']]) == 10
    assert candidate(grid = [['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y']]) == 10


