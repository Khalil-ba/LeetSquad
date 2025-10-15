def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(board = [[4, 1, 2], [0, 5, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 1, 2], [0, 5, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 2, 4], [1, 5, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 2, 4], [1, 5, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[0, 1, 2], [4, 5, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[0, 1, 2], [4, 5, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 2, 3], [4, 0, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 2, 3], [4, 0, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 2, 0], [3, 4, 5]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 2, 0], [3, 4, 5]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 0, 2], [4, 5, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 0, 2], [4, 5, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 2, 3], [5, 4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 2, 3], [5, 4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[0, 1, 2], [3, 4, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[0, 1, 2], [3, 4, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 0, 3], [4, 2, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 0, 3], [4, 2, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 2, 3], [0, 4, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 2, 3], [0, 4, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 1, 2], [5, 0, 3]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 1, 2], [5, 0, 3]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 4, 2], [0, 1, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 4, 2], [0, 1, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 0, 3], [1, 5, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 0, 3], [1, 5, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 5, 3], [0, 4, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 5, 3], [0, 4, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 3, 0], [4, 2, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 3, 0], [4, 2, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 3, 1], [4, 0, 5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 3, 1], [4, 0, 5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 1, 0], [2, 5, 3]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 1, 0], [2, 5, 3]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 3, 0], [4, 1, 2]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 3, 0], [4, 1, 2]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 3, 5], [2, 4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 3, 5], [2, 4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 3, 4], [1, 0, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 3, 4], [1, 0, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 3, 4], [1, 2, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 3, 4], [1, 2, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 2, 5], [0, 4, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 2, 5], [0, 4, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 3, 2], [1, 5, 0]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 3, 2], [1, 5, 0]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 5, 4], [0, 2, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 5, 4], [0, 2, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 1, 3], [4, 0, 2]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 1, 3], [4, 0, 2]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 3, 0], [1, 5, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 3, 0], [1, 5, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 2, 0], [5, 4, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 2, 0], [5, 4, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 4, 2], [3, 5, 0]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 4, 2], [3, 5, 0]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 3, 4], [5, 0, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 3, 4], [5, 0, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 2, 1], [0, 5, 4]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 2, 1], [0, 5, 4]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 1, 4], [2, 3, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 1, 4], [2, 3, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 3, 0], [1, 4, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 3, 0], [1, 4, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[0, 5, 4], [3, 2, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[0, 5, 4], [3, 2, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 5, 3], [1, 4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 5, 3], [1, 4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[0, 5, 4], [2, 3, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[0, 5, 4], [2, 3, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 4, 0], [3, 2, 1]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 4, 0], [3, 2, 1]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 5, 4], [1, 2, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 5, 4], [1, 2, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 0, 2], [4, 3, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 0, 2], [4, 3, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(board = [[0, 5, 1], [3, 4, 2]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[0, 5, 1], [3, 4, 2]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 1, 2], [4, 0, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 1, 2], [4, 0, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 3, 5], [4, 0, 2]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 3, 5], [4, 0, 2]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 3, 0], [2, 4, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 3, 0], [2, 4, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 2, 0], [1, 5, 4]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 2, 0], [1, 5, 4]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 1, 2], [0, 4, 5]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 1, 2], [0, 4, 5]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 0, 2], [5, 3, 4]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 0, 2], [5, 3, 4]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 5, 3], [2, 4, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 5, 3], [2, 4, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 1, 2], [4, 3, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 1, 2], [4, 3, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 2, 3], [4, 1, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 2, 3], [4, 1, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 5, 3], [2, 0, 4]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 5, 3], [2, 0, 4]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 5, 2], [4, 1, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 5, 2], [4, 1, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 4, 0], [3, 5, 2]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 4, 0], [3, 5, 2]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 3, 5], [0, 1, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 3, 5], [0, 1, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 1, 2], [5, 3, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 1, 2], [5, 3, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 0, 1], [4, 2, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 0, 1], [4, 2, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 4, 3], [2, 1, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 4, 3], [2, 1, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 0, 5], [4, 3, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 0, 5], [4, 3, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 1, 3], [4, 5, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 1, 3], [4, 5, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 1, 0], [5, 3, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 1, 0], [5, 3, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 3, 1], [5, 0, 2]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 3, 1], [5, 0, 2]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 0, 1], [4, 3, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 0, 1], [4, 3, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 5, 1], [0, 4, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 5, 1], [0, 4, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 0, 2], [3, 5, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 0, 2], [3, 5, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[1, 3, 2], [4, 0, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[1, 3, 2], [4, 0, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 1, 2], [4, 5, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 1, 2], [4, 5, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 2, 0], [5, 1, 3]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 2, 0], [5, 1, 3]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 2, 3], [0, 4, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 2, 3], [0, 4, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 5, 1], [0, 3, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 5, 1], [0, 3, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 3, 0], [1, 2, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 3, 0], [1, 2, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 5, 3], [2, 0, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 5, 3], [2, 0, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[0, 5, 2], [1, 3, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[0, 5, 2], [1, 3, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 1, 3], [0, 5, 4]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 1, 3], [0, 5, 4]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 3, 5], [2, 0, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 3, 5], [2, 0, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(board = [[4, 2, 3], [1, 5, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[4, 2, 3], [1, 5, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 5, 3], [4, 0, 1]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 5, 3], [4, 0, 1]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 3, 1], [5, 4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 3, 1], [5, 4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[5, 1, 2], [0, 4, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[5, 1, 2], [0, 4, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(board = [[3, 0, 1], [4, 5, 2]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[3, 0, 1], [4, 5, 2]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(board = [[2, 3, 5], [4, 1, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [[2, 3, 5], [4, 1, 0]]) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(board = [[4, 1, 2], [0, 5, 3]]) == 4
    assert candidate(board = [[3, 2, 4], [1, 5, 0]]) == 14
    assert candidate(board = [[0, 1, 2], [4, 5, 3]]) == 3
    assert candidate(board = [[1, 2, 3], [4, 0, 5]]) == 1
    assert candidate(board = [[1, 2, 0], [3, 4, 5]]) == 13
    assert candidate(board = [[1, 0, 2], [4, 5, 3]]) == 2
    assert candidate(board = [[1, 2, 3], [5, 4, 0]]) == -1
    assert candidate(board = [[0, 1, 2], [3, 4, 5]]) == 15
    assert candidate(board = [[1, 0, 3], [4, 2, 5]]) == 2
    assert candidate(board = [[1, 2, 3], [0, 4, 5]]) == 2
    assert candidate(board = [[4, 1, 2], [5, 0, 3]]) == 5
    assert candidate(board = [[3, 4, 2], [0, 1, 5]]) == -1
    assert candidate(board = [[2, 0, 3], [1, 5, 4]]) == -1
    assert candidate(board = [[2, 5, 3], [0, 4, 1]]) == 14
    assert candidate(board = [[1, 3, 0], [4, 2, 5]]) == 3
    assert candidate(board = [[2, 3, 1], [4, 0, 5]]) == 15
    assert candidate(board = [[4, 1, 0], [2, 5, 3]]) == 7
    assert candidate(board = [[5, 3, 0], [4, 1, 2]]) == 17
    assert candidate(board = [[1, 3, 5], [2, 4, 0]]) == -1
    assert candidate(board = [[2, 3, 4], [1, 0, 5]]) == -1
    assert candidate(board = [[5, 3, 4], [1, 2, 0]]) == 12
    assert candidate(board = [[1, 2, 5], [0, 4, 3]]) == -1
    assert candidate(board = [[4, 3, 2], [1, 5, 0]]) == 20
    assert candidate(board = [[3, 5, 4], [0, 2, 1]]) == 14
    assert candidate(board = [[5, 1, 3], [4, 0, 2]]) == 15
    assert candidate(board = [[2, 3, 0], [1, 5, 4]]) == -1
    assert candidate(board = [[1, 2, 0], [5, 4, 3]]) == -1
    assert candidate(board = [[1, 4, 2], [3, 5, 0]]) == 16
    assert candidate(board = [[2, 3, 4], [5, 0, 1]]) == 15
    assert candidate(board = [[3, 2, 1], [0, 5, 4]]) == 20
    assert candidate(board = [[5, 1, 4], [2, 3, 0]]) == 14
    assert candidate(board = [[5, 3, 0], [1, 4, 2]]) == -1
    assert candidate(board = [[0, 5, 4], [3, 2, 1]]) == 15
    assert candidate(board = [[2, 5, 3], [1, 4, 0]]) == -1
    assert candidate(board = [[0, 5, 4], [2, 3, 1]]) == -1
    assert candidate(board = [[5, 4, 0], [3, 2, 1]]) == 13
    assert candidate(board = [[3, 5, 4], [1, 2, 0]]) == -1
    assert candidate(board = [[5, 0, 2], [4, 3, 1]]) == 16
    assert candidate(board = [[0, 5, 1], [3, 4, 2]]) == 13
    assert candidate(board = [[5, 1, 2], [4, 0, 3]]) == -1
    assert candidate(board = [[1, 3, 5], [4, 0, 2]]) == 5
    assert candidate(board = [[1, 3, 0], [2, 4, 5]]) == -1
    assert candidate(board = [[3, 2, 0], [1, 5, 4]]) == 13
    assert candidate(board = [[3, 1, 2], [0, 4, 5]]) == 16
    assert candidate(board = [[1, 0, 2], [5, 3, 4]]) == 14
    assert candidate(board = [[1, 5, 3], [2, 4, 0]]) == 14
    assert candidate(board = [[5, 1, 2], [4, 3, 0]]) == -1
    assert candidate(board = [[5, 2, 3], [4, 1, 0]]) == -1
    assert candidate(board = [[1, 5, 3], [2, 0, 4]]) == 13
    assert candidate(board = [[3, 5, 2], [4, 1, 0]]) == -1
    assert candidate(board = [[1, 4, 0], [3, 5, 2]]) == 15
    assert candidate(board = [[4, 3, 5], [0, 1, 2]]) == -1
    assert candidate(board = [[4, 1, 2], [5, 3, 0]]) == 6
    assert candidate(board = [[3, 0, 1], [4, 2, 5]]) == -1
    assert candidate(board = [[5, 4, 3], [2, 1, 0]]) == 14
    assert candidate(board = [[1, 0, 5], [4, 3, 2]]) == 6
    assert candidate(board = [[2, 1, 3], [4, 5, 0]]) == -1
    assert candidate(board = [[2, 1, 0], [5, 3, 4]]) == -1
    assert candidate(board = [[4, 3, 1], [5, 0, 2]]) == 9
    assert candidate(board = [[5, 0, 1], [4, 3, 2]]) == -1
    assert candidate(board = [[2, 5, 1], [0, 4, 3]]) == -1
    assert candidate(board = [[4, 0, 2], [3, 5, 1]]) == 14
    assert candidate(board = [[1, 3, 2], [4, 0, 5]]) == -1
    assert candidate(board = [[3, 1, 2], [4, 5, 0]]) == 14
    assert candidate(board = [[4, 2, 0], [5, 1, 3]]) == 7
    assert candidate(board = [[5, 2, 3], [0, 4, 1]]) == -1
    assert candidate(board = [[4, 5, 1], [0, 3, 2]]) == -1
    assert candidate(board = [[4, 3, 0], [1, 2, 5]]) == -1
    assert candidate(board = [[4, 5, 3], [2, 0, 1]]) == -1
    assert candidate(board = [[0, 5, 2], [1, 3, 4]]) == -1
    assert candidate(board = [[2, 1, 3], [0, 5, 4]]) == 14
    assert candidate(board = [[4, 3, 5], [2, 0, 1]]) == 9
    assert candidate(board = [[4, 2, 3], [1, 5, 0]]) == -1
    assert candidate(board = [[2, 5, 3], [4, 0, 1]]) == 13
    assert candidate(board = [[2, 3, 1], [5, 4, 0]]) == -1
    assert candidate(board = [[5, 1, 2], [0, 4, 3]]) == -1
    assert candidate(board = [[3, 0, 1], [4, 5, 2]]) == 12
    assert candidate(board = [[2, 3, 5], [4, 1, 0]]) == -1


