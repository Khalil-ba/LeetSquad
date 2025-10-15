def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(cost = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(cost = [[15, 96], [36, 2]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [[15, 96], [36, 2]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(cost = [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(cost = [[10, 20], [30, 40], [50, 60]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [[10, 20], [30, 40], [50, 60]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(cost = [[5, 5, 5], [5, 5, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [[5, 5, 5], [5, 5, 5]]) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]) == 10
    assert candidate(cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]) == 4
    assert candidate(cost = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 16
    assert candidate(cost = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 13
    assert candidate(cost = [[15, 96], [36, 2]]) == 17
    assert candidate(cost = [[10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]]) == 40
    assert candidate(cost = [[10, 20], [30, 40], [50, 60]]) == 100
    assert candidate(cost = [[5, 5, 5], [5, 5, 5]]) == 15


