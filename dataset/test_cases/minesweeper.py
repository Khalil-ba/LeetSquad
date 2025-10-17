def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 0]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 0]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '1', '1'], ['B', 'B', '1', 'M', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '1', '1'], ['B', 'B', '1', 'M', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],click = [1, 2]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],click = [1, 2]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'M', 'E']],click = [1, 1]) == [['E', 'E', 'E'], ['E', '1', 'E'], ['E', 'M', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'M', 'E']],click = [1, 1]) == [['E', 'E', 'E'], ['E', '1', 'E'], ['E', 'M', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', '1', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', '1', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E']],click = [0, 0]) == [['B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E']],click = [0, 0]) == [['B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 0]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 0]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 1]) == [['E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 1]) == [['E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['M']],click = [0, 0]) == [['X']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['M']],click = [0, 0]) == [['X']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'M', 'E', 'E'], ['E', '2', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'M', 'E', 'E'], ['E', '2', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', '1', '1', '1'], ['B', '1', 'M', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', '1', '1', '1'], ['B', '1', 'M', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],click = [1, 2]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],click = [1, 2]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', '2', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', '2', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 1]) == [['E', '1', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 1]) == [['E', '1', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 3]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', '2', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 3]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', '2', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', '1', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', '1', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', '1', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', '1', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '1', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '1', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'M', 'E'], ['E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'M', 'E'], ['E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E', 'E', 'E']],click = [7, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E', 'E', 'E']],click = [7, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [6, 6]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [6, 6]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M'], ['E', 'E', '1', 'E'], ['M', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M'], ['E', 'E', '1', 'E'], ['M', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', '1', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', '1', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']],click = [4, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']],click = [4, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 5]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', '2', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 5]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', '2', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', '2', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', '2', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', '1', 'M', 'E'], ['B', 'B', '1', '1', '1'], ['1', '1', 'B', 'B', 'B'], ['M', '1', 'B', 'B', 'B'], ['E', '1', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', '1', 'M', 'E'], ['B', 'B', '1', '1', '1'], ['1', '1', 'B', 'B', 'B'], ['M', '1', 'B', 'B', 'B'], ['E', '1', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 6]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', '1', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 6]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', '1', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', '1', 'E', 'E', 'E'], ['B', '1', 'M', 'M', 'E'], ['B', '1', '2', '2', '1'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', '1', 'E', 'E', 'E'], ['B', '1', 'M', 'M', 'E'], ['B', '1', '2', '2', '1'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B'], ['B', '1', 'M', '1', 'B', 'B'], ['B', '1', '1', '2', '1', '1'], ['B', 'B', 'B', '1', 'M', 'E'], ['B', 'B', 'B', '1', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B'], ['B', '1', 'M', '1', 'B', 'B'], ['B', '1', '1', '2', '1', '1'], ['B', 'B', 'B', '1', 'M', 'E'], ['B', 'B', 'B', '1', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '1', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '1', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E']],click = [4, 0]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M'], ['2', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E']],click = [4, 0]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M'], ['2', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', '1', 'M', '1', 'B', 'B', 'B', 'B'], ['B', '1', '1', '2', '1', '1', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', '1', 'M', '1', 'B', 'B', 'B', 'B'], ['B', '1', '1', '2', '1', '1', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', '1', '2', '2', '1'], ['B', '1', 'M', 'M', 'E'], ['B', '1', '2', '2', '1'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', '1', '2', '2', '1'], ['B', '1', 'M', 'M', 'E'], ['B', '1', '2', '2', '1'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', '1', '1', '1', 'B', 'B'], ['B', 'B', 'B', '1', 'M', '1', 'B', 'B'], ['B', 'B', 'B', '1', '1', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', '1', '1', '1', 'B', 'B'], ['B', 'B', 'B', '1', 'M', '1', 'B', 'B'], ['B', 'B', 'B', '1', '1', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', '8', 'M', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', '8', 'M', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1'], ['M', '1', 'B', '1', 'M'], ['E', '1', 'B', '1', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1'], ['M', '1', 'B', '1', 'M'], ['E', '1', 'B', '1', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['1', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['1', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E']],click = [7, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E']],click = [7, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '2', '2', '1', 'B'], ['E', 'M', 'M', '1', 'B'], ['E', 'E', 'E', '1', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '2', '2', '1', 'B'], ['E', 'M', 'M', '1', 'B'], ['E', 'E', 'E', '1', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 8]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', '1', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 8]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', '1', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['1', '1', '2', '1', '1'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['1', '1', '2', '1', '1'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', '1']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', '1']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', '1', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', '1', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']],click = [2, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['M', 'E', 'X', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']],click = [2, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['M', 'E', 'X', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'M', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', '2', '1', '2', '1', '2', '1'], ['E', 'M', 'E', 'M', 'E', 'M', 'E', 'M']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'M', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', '2', '1', '2', '1', '2', '1'], ['E', 'M', 'E', 'M', 'E', 'M', 'E', 'M']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', '1', 'M', '1', 'B'], ['B', 'B', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', '1', 'M', '1', 'B'], ['B', 'B', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '3', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '3', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', '3', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', '3', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['M', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['M', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 8]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 8]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'E', 'E', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', 'B', 'B', 'B', '1', '1'], ['M', '1', 'B', 'B', 'B', 'B', '1', 'M']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'E', 'E', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', 'B', 'B', 'B', '1', '1'], ['M', '1', 'B', 'B', 'B', 'B', '1', 'M']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M']],click = [4, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M']],click = [4, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1', '1'], ['M', '1', 'B', '1', 'M', 'E'], ['E', '2', '1', '2', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1', '1'], ['M', '1', 'B', '1', 'M', 'E'], ['E', '2', '1', '2', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', '1', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', '1', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '1', '1', '1', '1'], ['E', 'M', 'E', 'E', 'M']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '1', '1', '1', '1'], ['E', 'M', 'E', 'E', 'M']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 7]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 7]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'M'], ['E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'M'], ['E', 'E', 'M', 'E'], ['E', 'E', '2', 'E'], ['E', 'M', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'M'], ['E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'M'], ['E', 'E', 'M', 'E'], ['E', 'E', '2', 'E'], ['E', 'M', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '1', '1'], ['B', 'B', '1', 'M', 'E'], ['B', 'B', '1', '1', '1'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '1', '1'], ['B', 'B', '1', 'M', 'E'], ['B', 'B', '1', '1', '1'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1'], ['M', '1', 'B', '1', 'M'], ['1', '1', 'B', '1', '1'], ['B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1'], ['M', '1', 'B', '1', 'M'], ['1', '1', 'B', '1', '1'], ['B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', '2', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', '2', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 3]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 3]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]: {e}')
    
    total += 1
    try:
        result = candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'E']],click = [0, 8]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', '1', '1', '2', '1', '1', 'B'], ['B', 'B', 'B', 'B', '1', 'M', '1', 'B', 'B', 'B']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'E']],click = [0, 8]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', '1', '1', '2', '1', '1', 'B'], ['B', 'B', 'B', 'B', '1', 'M', '1', 'B', 'B', 'B']]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 0]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '1', '1'], ['B', 'B', '1', 'M', 'E']]
    assert candidate(board = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],click = [1, 2]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'M', 'E']],click = [1, 1]) == [['E', 'E', 'E'], ['E', '1', 'E'], ['E', 'M', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', '1', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E']]
    assert candidate(board = [['E']],click = [0, 0]) == [['B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 0]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 1]) == [['E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']]
    assert candidate(board = [['M']],click = [0, 0]) == [['X']]
    assert candidate(board = [['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'M', 'E', 'E'], ['E', '2', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B'], ['B', '1', '1', '1'], ['B', '1', 'M', 'E']]
    assert candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['B', '1', 'E', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']],click = [1, 2]) == [['B', '1', 'E', '1', 'B'], ['B', '1', 'X', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', '2', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 1]) == [['E', '1', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 3]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', '2', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', '1', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', '1', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '1', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'M', 'E'], ['E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E', 'E', 'E']],click = [7, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [6, 6]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M'], ['E', 'E', '1', 'E'], ['M', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', '1', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E']],click = [4, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 5]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', '2', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', '2', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', '1', 'M', 'E'], ['B', 'B', '1', '1', '1'], ['1', '1', 'B', 'B', 'B'], ['M', '1', 'B', 'B', 'B'], ['E', '1', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 6]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', '1', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', '1', 'E', 'E', 'E'], ['B', '1', 'M', 'M', 'E'], ['B', '1', '2', '2', '1'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B'], ['B', '1', 'M', '1', 'B', 'B'], ['B', '1', '1', '2', '1', '1'], ['B', 'B', 'B', '1', 'M', 'E'], ['B', 'B', 'B', '1', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '1', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E']],click = [4, 0]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M'], ['2', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', '1', 'M', '1', 'B', 'B', 'B', 'B'], ['B', '1', '1', '2', '1', '1', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', '1', '2', '2', '1'], ['B', '1', 'M', 'M', 'E'], ['B', '1', '2', '2', '1'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', '1', '1', '1', 'B', 'B'], ['B', 'B', 'B', '1', 'M', '1', 'B', 'B'], ['B', 'B', 'B', '1', '1', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [2, 1]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'M', '8', 'M', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1'], ['M', '1', 'B', '1', 'M'], ['E', '1', 'B', '1', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['1', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E']],click = [7, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '2', '2', '1', 'B'], ['E', 'M', 'M', '1', 'B'], ['E', 'E', 'E', '1', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 8]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', '1', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['1', '1', '2', '1', '1'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', '1']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', '1', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']],click = [2, 2]) == [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E'], ['M', 'E', 'X', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'M', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', '2', '1', '2', '1', '2', '1'], ['E', 'M', 'E', 'M', 'E', 'M', 'E', 'M']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', '1', 'M', '1', 'B'], ['B', 'B', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '3', 'E', 'E', 'E', 'E'], ['M', 'M', 'M', 'M', 'M', 'M', 'M'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E'], ['E', 'E', '3', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'M', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['M', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [5, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [0, 8]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', '1', 'M', 'M', 'M', '1', 'B', 'B'], ['B', 'B', '1', '2', '3', '2', '1', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 1]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'X', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'E', 'E', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', 'B', 'B', 'B', '1', '1'], ['M', '1', 'B', 'B', 'B', 'B', '1', 'M']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M']],click = [4, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1', '1'], ['M', '1', 'B', '1', 'M', 'E'], ['E', '2', '1', '2', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'M', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', '1', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'M']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B'], ['1', '1', '1', '1', '1'], ['E', 'M', 'E', 'E', 'M']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 7]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', '1', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'M'], ['E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'M'], ['E', 'E', 'M', 'E'], ['E', 'E', '2', 'E'], ['E', 'M', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['B', 'B', 'B', 'B', 'B'], ['B', 'B', '1', '1', '1'], ['B', 'B', '1', 'M', 'E'], ['B', 'B', '1', '1', '1'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 4]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [1, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['M', 'E', 'E', 'E', 'M'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['B', 'B', 'B', 'B', 'B'], ['1', '1', 'B', '1', '1'], ['M', '1', 'B', '1', 'M'], ['1', '1', 'B', '1', '1'], ['B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['M', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [0, 0]) == [['X', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'X', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'M', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E'], ['E', 'E', 'M', 'M', 'E'], ['E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E'], ['E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']],click = [1, 1]) == [['E', 'E', 'E', 'E'], ['E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [3, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'M', 'E', 'E'], ['E', 'E', 'E', '2', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 2]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', '2', 'E', 'E', 'E'], ['E', 'M', 'M', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']],click = [2, 3]) == [['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'X', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']],click = [4, 3]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    assert candidate(board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E', 'M', 'E', 'E', 'E', 'E']],click = [0, 8]) == [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', '1', '1', '1', 'B', 'B', '1', '1', '1', 'B'], ['B', '1', 'M', '1', 'B', 'B', '1', 'M', '1', 'B'], ['B', '1', '1', '1', '1', '1', '2', '1', '1', 'B'], ['B', 'B', 'B', 'B', '1', 'M', '1', 'B', 'B', 'B']]


