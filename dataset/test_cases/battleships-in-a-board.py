def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X'], ['.', '.', '.'], ['X', 'X', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X'], ['.', '.', '.'], ['X', 'X', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.'], ['.', 'X', '.'], ['.', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.'], ['.', 'X', '.'], ['.', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.'], ['X', 'X', '.'], ['.', '.', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.'], ['X', 'X', '.'], ['.', '.', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.'], ['.', 'X', 'X', 'X'], ['.', 'X', '.', '.'], ['.', '.', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.'], ['.', 'X', 'X', 'X'], ['.', 'X', '.', '.'], ['.', '.', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', 'X', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', 'X', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', 'X', '.'], ['X', '.', '.', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', 'X', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', 'X', '.'], ['X', '.', '.', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', 'X', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', 'X', 'X'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', 'X', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', 'X', 'X'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', 'X', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', 'X', '.', 'X'], ['.', '.', '.', 'X', '.', '.'], ['X', 'X', '.', 'X', 'X', 'X'], ['.', 'X', '.', '.', '.', '.'], ['X', 'X', '.', 'X', '.', 'X']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', 'X', '.', 'X'], ['.', '.', '.', 'X', '.', '.'], ['X', 'X', '.', 'X', 'X', 'X'], ['.', 'X', '.', '.', '.', '.'], ['X', 'X', '.', 'X', '.', 'X']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.'], ['X', 'X', 'X', '.'], ['.', 'X', '.', '.'], ['.', 'X', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.'], ['X', 'X', 'X', '.'], ['.', 'X', '.', '.'], ['.', 'X', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.'], ['X', 'X', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', 'X', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.'], ['X', 'X', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', 'X', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', '.', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', '.', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', '.'], ['X', '.', '.', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', '.'], ['X', '.', '.', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', 'X', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', 'X', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', '.'], ['.', '.', '.', 'X'], ['X', 'X', 'X', 'X'], ['.', 'X', '.', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', '.'], ['.', '.', '.', 'X'], ['X', 'X', 'X', 'X'], ['.', 'X', '.', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.'], ['X', 'X', 'X', 'X'], ['.', '.', '.', '.'], ['X', '.', 'X', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.'], ['X', 'X', 'X', 'X'], ['.', '.', '.', '.'], ['X', '.', 'X', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', '.', '.'], ['X', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', '.', '.'], ['X', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', 'X', '.', 'X', '.', 'X'], ['X', '.', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', 'X', '.', 'X', '.', 'X'], ['X', '.', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['X', 'X', 'X', '.', '.', '.'], ['.', '.', '.', 'X', 'X', 'X'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['X', 'X', 'X', '.', '.', '.'], ['.', '.', '.', 'X', 'X', 'X'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', 'X'], ['.', '.', 'X', 'X'], ['X', '.', 'X', '.'], ['.', 'X', 'X', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', 'X'], ['.', '.', 'X', 'X'], ['X', '.', 'X', '.'], ['.', 'X', 'X', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', 'X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', 'X', '.', '.', 'X', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', 'X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', 'X', '.', '.', 'X', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.'], ['X', '.', 'X', '.'], ['X', '.', '.', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.'], ['X', '.', 'X', '.'], ['X', '.', '.', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', 'X', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', 'X', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X']]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X']]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', 'X', '.', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', 'X', '.', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X'], ['.', '.', '.', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X'], ['.', '.', '.', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.'], ['.', '.', '.', '.'], ['X', '.', 'X', '.'], ['.', '.', '.', '.']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.'], ['.', '.', '.', '.'], ['X', '.', 'X', '.'], ['.', '.', '.', '.']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.'], ['X', '.', 'X', 'X'], ['.', 'X', '.', '.'], ['X', '.', 'X', '.']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.'], ['X', '.', 'X', 'X'], ['.', 'X', '.', '.'], ['X', '.', 'X', '.']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.']]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.']]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.']]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.']]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', 'X', '.', 'X', '.'], ['X', 'X', '.', 'X', 'X'], ['.', 'X', '.', 'X', '.'], ['X', 'X', '.', 'X', 'X'], ['.', 'X', '.', 'X', '.']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', 'X', '.', 'X', '.'], ['X', 'X', '.', 'X', 'X'], ['.', 'X', '.', 'X', '.'], ['X', 'X', '.', 'X', 'X'], ['.', 'X', '.', 'X', '.']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', '.'], ['X', '.', 'X', '.'], ['.', '.', '.', '.'], ['.', 'X', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', '.'], ['X', '.', 'X', '.'], ['.', '.', '.', '.'], ['.', 'X', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.'], ['X', '.', 'X', '.'], ['X', '.', 'X', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.'], ['X', '.', 'X', '.'], ['X', '.', 'X', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', 'X'], ['X', '.', 'X', '.'], ['.', '.', 'X', 'X'], ['.', '.', 'X', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', 'X'], ['X', '.', 'X', '.'], ['.', '.', 'X', 'X'], ['.', '.', 'X', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', '.', '.', '.', '.', 'X'], ['.', '.', 'X', 'X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.', '.', 'X']]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', '.', '.', '.', '.', 'X'], ['.', '.', 'X', 'X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.', '.', 'X']]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X']]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X']]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', '.', 'X'], ['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', '.', 'X'], ['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', '.', 'X'], ['X', '.', 'X', 'X', '.'], ['.', '.', '.', 'X', 'X'], ['X', 'X', '.', 'X', '.']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', '.', 'X'], ['X', '.', 'X', 'X', '.'], ['.', '.', '.', 'X', 'X'], ['X', 'X', '.', 'X', '.']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', '.'], ['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', '.'], ['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.'], ['.', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.'], ['.', 'X', '.', '.', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.'], ['.', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.'], ['.', 'X', '.', '.', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', 'X', 'X'], ['X', '.', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', 'X', 'X'], ['X', '.', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.'], ['.', 'X', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.'], ['.', 'X', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', 'X', '.', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', 'X', '.', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', 'X', 'X', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', 'X', 'X', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', 'X', 'X'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', 'X', 'X'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X']]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X']]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', 'X'], ['.', 'X', '.', 'X'], ['.', 'X', '.', 'X']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', 'X'], ['.', 'X', '.', 'X'], ['.', 'X', '.', 'X']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', 'X', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', 'X', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['X', 'X', 'X', 'X', '.'], ['.', '.', 'X', 'X', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['X', 'X', 'X', 'X', '.'], ['.', '.', 'X', 'X', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', 'X', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', 'X', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X']]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X']]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', 'X'], ['X', 'X', '.', 'X'], ['.', '.', '.', 'X'], ['X', 'X', 'X', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', 'X'], ['X', 'X', '.', 'X'], ['.', '.', '.', 'X'], ['X', 'X', 'X', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X']]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X']]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', 'X', 'X', 'X'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', 'X', 'X', 'X'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', 'X'], ['X', 'X', 'X', 'X', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', 'X'], ['X', 'X', 'X', 'X', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', 'X', '.', '.']]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', 'X', '.', '.']]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', 'X', 'X', '.', 'X', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X', '.', 'X', 'X', '.', 'X']]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', 'X', 'X', '.', 'X', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X', '.', 'X', 'X', '.', 'X']]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', 'X', 'X'], ['.', '.', '.', '.'], ['X', 'X', 'X', 'X'], ['.', '.', '.', '.']]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', 'X', 'X'], ['.', '.', '.', '.'], ['X', 'X', 'X', 'X'], ['.', '.', '.', '.']]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', 'X', '.', '.'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', 'X', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', 'X', '.', '.'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', 'X', 'X']]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(board = [['X', '.', '.', '.'], ['X', 'X', '.', '.'], ['.', '.', '.', 'X'], ['.', '.', 'X', 'X']]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['X', '.', '.', '.'], ['X', 'X', '.', '.'], ['.', '.', '.', 'X'], ['.', '.', 'X', 'X']]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(board = [['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']]) == 2
    assert candidate(board = [['X', 'X', 'X'], ['.', '.', '.'], ['X', 'X', 'X']]) == 2
    assert candidate(board = [['.']]) == 0
    assert candidate(board = [['X', '.', '.'], ['.', 'X', '.'], ['.', '.', 'X']]) == 3
    assert candidate(board = [['X', '.', '.'], ['X', 'X', '.'], ['.', '.', 'X']]) == 2
    assert candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 3
    assert candidate(board = [['.', '.', '.', '.'], ['.', 'X', 'X', 'X'], ['.', 'X', '.', '.'], ['.', '.', '.', '.']]) == 1
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 5
    assert candidate(board = [['.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', 'X', '.']]) == 2
    assert candidate(board = [['X', 'X', 'X', 'X', '.'], ['X', '.', '.', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', 'X', 'X']]) == 2
    assert candidate(board = [['X', '.', '.', 'X', 'X'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', 'X', 'X']]) == 3
    assert candidate(board = [['X', '.', '.', 'X', '.', 'X'], ['.', '.', '.', 'X', '.', '.'], ['X', 'X', '.', 'X', 'X', 'X'], ['.', 'X', '.', '.', '.', '.'], ['X', 'X', '.', 'X', '.', 'X']]) == 7
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.']]) == 3
    assert candidate(board = [['X', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X']]) == 5
    assert candidate(board = [['.', '.', '.', '.'], ['X', 'X', 'X', '.'], ['.', 'X', '.', '.'], ['.', 'X', '.', '.']]) == 1
    assert candidate(board = [['X', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', 'X']]) == 3
    assert candidate(board = [['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 6
    assert candidate(board = [['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.'], ['X', 'X', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', 'X', 'X']]) == 2
    assert candidate(board = [['X', 'X', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', '.', '.', '.']]) == 1
    assert candidate(board = [['X', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', '.'], ['X', '.', '.', '.']]) == 3
    assert candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 2
    assert candidate(board = [['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.']]) == 2
    assert candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', 'X', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 2
    assert candidate(board = [['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 5
    assert candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 2
    assert candidate(board = [['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 2
    assert candidate(board = [['X', 'X', 'X', '.'], ['.', '.', '.', 'X'], ['X', 'X', 'X', 'X'], ['.', 'X', '.', '.']]) == 3
    assert candidate(board = [['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.']]) == 1
    assert candidate(board = [['.', '.', '.', '.'], ['X', 'X', 'X', 'X'], ['.', '.', '.', '.'], ['X', '.', 'X', '.']]) == 3
    assert candidate(board = [['X', 'X', '.', '.', '.'], ['X', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 1
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', 'X'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', 'X']]) == 5
    assert candidate(board = [['X', '.', '.', 'X', '.', 'X', '.', 'X'], ['X', '.', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.']]) == 8
    assert candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X']]) == 4
    assert candidate(board = [['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 2
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 5
    assert candidate(board = [['X', '.', 'X', '.'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X'], ['X', '.', '.', 'X']]) == 3
    assert candidate(board = [['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['X', 'X', 'X', '.', '.', '.'], ['.', '.', '.', 'X', 'X', 'X'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]) == 2
    assert candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4
    assert candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 1
    assert candidate(board = [['X', 'X', '.', 'X'], ['.', '.', 'X', 'X'], ['X', '.', 'X', '.'], ['.', 'X', 'X', 'X']]) == 5
    assert candidate(board = [['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 3
    assert candidate(board = [['X', '.', '.', '.', 'X', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', 'X', '.', '.', 'X', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']]) == 8
    assert candidate(board = [['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.']]) == 1
    assert candidate(board = [['X', '.', 'X', '.'], ['X', '.', 'X', '.'], ['X', '.', '.', '.']]) == 2
    assert candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', 'X', 'X']]) == 3
    assert candidate(board = [['X', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.'], ['X', '.', '.', 'X', '.']]) == 4
    assert candidate(board = [['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X']]) == 14
    assert candidate(board = [['.', '.', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['X', 'X', 'X', '.', '.'], ['.', '.', 'X', '.', '.']]) == 3
    assert candidate(board = [['X', 'X', 'X', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X'], ['.', '.', '.', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', 'X', 'X', 'X']]) == 4
    assert candidate(board = [['X', '.', 'X', '.'], ['.', '.', '.', '.'], ['X', '.', 'X', '.'], ['.', '.', '.', '.']]) == 4
    assert candidate(board = [['X', '.', '.', '.'], ['X', '.', 'X', 'X'], ['.', 'X', '.', '.'], ['X', '.', 'X', '.']]) == 5
    assert candidate(board = [['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.']]) == 12
    assert candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.']]) == 13
    assert candidate(board = [['.', 'X', '.', 'X', '.'], ['X', 'X', '.', 'X', 'X'], ['.', 'X', '.', 'X', '.'], ['X', 'X', '.', 'X', 'X'], ['.', 'X', '.', 'X', '.']]) == 4
    assert candidate(board = [['X', 'X', '.', '.'], ['X', '.', 'X', '.'], ['.', '.', '.', '.'], ['.', 'X', '.', 'X']]) == 4
    assert candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X']]) == 3
    assert candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.']]) == 1
    assert candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 1
    assert candidate(board = [['X', '.', 'X', '.'], ['X', '.', 'X', '.'], ['X', '.', 'X', '.']]) == 2
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 5
    assert candidate(board = [['X', 'X', '.', 'X'], ['X', '.', 'X', '.'], ['.', '.', 'X', 'X'], ['.', '.', 'X', '.']]) == 3
    assert candidate(board = [['.', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 4
    assert candidate(board = [['X', 'X', '.', '.', '.', '.', '.', 'X'], ['.', '.', 'X', 'X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.', '.', 'X']]) == 8
    assert candidate(board = [['X', 'X', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X']]) == 6
    assert candidate(board = [['X', 'X', 'X', '.', '.'], ['.', '.', '.', 'X', 'X'], ['.', '.', '.', '.', 'X'], ['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.']]) == 3
    assert candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 3
    assert candidate(board = [['X', 'X', 'X', '.', 'X'], ['X', '.', 'X', 'X', '.'], ['.', '.', '.', 'X', 'X'], ['X', 'X', '.', 'X', '.']]) == 3
    assert candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 0
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', '.'], ['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 7
    assert candidate(board = [['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X'], ['X', 'X', 'X', '.', 'X']]) == 2
    assert candidate(board = [['.', '.', '.', '.', '.'], ['.', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.'], ['.', 'X', '.', '.', '.']]) == 2
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 3
    assert candidate(board = [['X', '.', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', 'X', 'X'], ['X', '.', '.', 'X']]) == 3
    assert candidate(board = [['X', '.', '.', '.'], ['.', 'X', '.', '.'], ['.', '.', 'X', '.'], ['.', '.', '.', 'X']]) == 4
    assert candidate(board = [['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 13
    assert candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 1
    assert candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', 'X', '.', '.'], ['X', '.', '.', 'X', '.'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X']]) == 4
    assert candidate(board = [['X', '.', '.', '.', '.'], ['X', '.', 'X', 'X', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', 'X', '.', '.'], ['X', '.', '.', '.', 'X']]) == 4
    assert candidate(board = [['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.']]) == 2
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 3
    assert candidate(board = [['X', '.', 'X', 'X', 'X'], ['X', '.', '.', '.', '.'], ['X', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X']]) == 2
    assert candidate(board = [['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X']]) == 10
    assert candidate(board = [['X', 'X', '.', 'X'], ['.', 'X', '.', 'X'], ['.', 'X', '.', 'X']]) == 2
    assert candidate(board = [['X', 'X', 'X', 'X', 'X'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4
    assert candidate(board = [['X', 'X', 'X', 'X', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', '.', '.', '.', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 1
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['X', 'X', 'X', 'X', '.'], ['.', '.', 'X', 'X', 'X'], ['X', '.', 'X', '.', 'X'], ['X', '.', 'X', '.', 'X']]) == 4
    assert candidate(board = [['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.'], ['.', 'X', '.', 'X', '.']]) == 2
    assert candidate(board = [['X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', '.', 'X'], ['.', '.', '.', '.', '.']]) == 4
    assert candidate(board = [['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]) == 1
    assert candidate(board = [['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', 'X', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.']]) == 4
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X'], ['.', 'X', '.', 'X', '.'], ['X', '.', 'X', '.', 'X']]) == 13
    assert candidate(board = [['X', 'X', '.', 'X'], ['X', 'X', '.', 'X'], ['.', '.', '.', 'X'], ['X', 'X', 'X', 'X']]) == 3
    assert candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['X', 'X', 'X', 'X', 'X']]) == 1
    assert candidate(board = [['X', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.'], ['X', '.', 'X', 'X', 'X'], ['.', '.', '.', 'X', '.'], ['.', '.', '.', 'X', '.']]) == 2
    assert candidate(board = [['X', '.', 'X', '.', 'X'], ['.', '.', 'X', '.', 'X'], ['X', 'X', 'X', 'X', '.'], ['.', '.', '.', '.', '.'], ['X', '.', 'X', '.', 'X']]) == 7
    assert candidate(board = [['X', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'X', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', 'X', '.', '.']]) == 7
    assert candidate(board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]) == 0
    assert candidate(board = [['X', 'X', '.', 'X', 'X', '.', 'X', 'X', '.', 'X'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['X', 'X', '.', 'X', 'X', '.', 'X', 'X', '.', 'X']]) == 9
    assert candidate(board = [['X', 'X', 'X', 'X'], ['.', '.', '.', '.'], ['X', 'X', 'X', 'X'], ['.', '.', '.', '.']]) == 2
    assert candidate(board = [['X', 'X', '.', '.'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', 'X', 'X']]) == 3
    assert candidate(board = [['X', '.', '.', '.'], ['X', 'X', '.', '.'], ['.', '.', '.', 'X'], ['.', '.', 'X', 'X']]) == 3


