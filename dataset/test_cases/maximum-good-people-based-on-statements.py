def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0], [1, 2, 1], [0, 1, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0], [1, 2, 1], [0, 1, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 2], [1, 2, 2, 0], [0, 2, 2, 1], [2, 0, 1, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 2], [1, 2, 2, 0], [0, 2, 2, 1], [2, 0, 1, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2], [2, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2], [2, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 0], [0, 2, 1, 0], [1, 1, 2, 0], [0, 0, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 0], [0, 2, 1, 0], [1, 1, 2, 0], [0, 0, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1], [0, 2, 1], [0, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1], [0, 2, 1], [0, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 0, 0], [2, 2, 0, 0], [0, 0, 2, 1], [0, 0, 1, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 0, 0], [2, 2, 0, 0], [0, 0, 2, 1], [0, 0, 1, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0, 0, 0], [0, 2, 1, 1, 1], [0, 1, 2, 1, 0], [0, 1, 1, 2, 1], [0, 1, 0, 1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0, 0, 0], [0, 2, 1, 1, 1], [0, 1, 2, 1, 0], [0, 1, 1, 2, 1], [0, 1, 0, 1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1], [0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1], [0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2], [2, 2, 0, 2], [2, 0, 2, 2], [2, 2, 2, 2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2], [2, 2, 0, 2], [2, 0, 2, 2], [2, 2, 2, 2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0], [0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0], [0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 2, 0], [1, 0, 1, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 2, 0], [1, 0, 1, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 1], [0, 2, 1], [1, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 1], [0, 2, 1], [1, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 1, 2], [1, 2, 0, 2], [0, 0, 2, 1], [2, 2, 1, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 1, 2], [1, 2, 0, 2], [0, 0, 2, 1], [2, 2, 1, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0, 1, 0, 1], [0, 2, 1, 0, 0, 0], [0, 1, 2, 1, 1, 0], [1, 0, 1, 2, 1, 1], [0, 0, 1, 1, 2, 0], [1, 0, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0, 1, 0, 1], [0, 2, 1, 0, 0, 0], [0, 1, 2, 1, 1, 0], [1, 0, 1, 2, 1, 1], [0, 0, 1, 1, 2, 0], [1, 0, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 2, 1, 2, 1, 2, 0], [1, 2, 2, 0, 1, 0, 1, 0, 1], [0, 2, 2, 1, 0, 1, 0, 1, 0], [2, 0, 1, 2, 0, 2, 1, 2, 1], [1, 1, 0, 0, 2, 1, 0, 1, 0], [2, 0, 1, 2, 1, 2, 1, 2, 0], [1, 0, 1, 0, 0, 1, 2, 1, 1], [2, 1, 0, 2, 0, 2, 1, 2, 0], [0, 1, 0, 1, 0, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 2, 1, 2, 1, 2, 0], [1, 2, 2, 0, 1, 0, 1, 0, 1], [0, 2, 2, 1, 0, 1, 0, 1, 0], [2, 0, 1, 2, 0, 2, 1, 2, 1], [1, 1, 0, 0, 2, 1, 0, 1, 0], [2, 0, 1, 2, 1, 2, 1, 2, 0], [1, 0, 1, 0, 0, 1, 2, 1, 1], [2, 1, 0, 2, 0, 2, 1, 2, 0], [0, 1, 0, 1, 0, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[1, 0, 1, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 0, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[1, 0, 1, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 0, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 2, 1], [1, 2, 1, 0, 2], [0, 1, 2, 1, 0], [2, 0, 1, 2, 0], [1, 2, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 2, 1], [1, 2, 1, 0, 2], [0, 1, 2, 1, 0], [2, 0, 1, 2, 0], [1, 2, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 2, 1, 0, 2, 0], [0, 2, 0, 0, 2, 0, 1], [2, 0, 2, 0, 2, 1, 0], [1, 0, 0, 2, 0, 0, 1], [0, 2, 2, 0, 2, 0, 0], [2, 0, 1, 0, 0, 2, 1], [0, 1, 0, 1, 0, 1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 2, 1, 0, 2, 0], [0, 2, 0, 0, 2, 0, 1], [2, 0, 2, 0, 2, 1, 0], [1, 0, 0, 2, 0, 0, 1], [0, 2, 2, 0, 2, 0, 0], [2, 0, 1, 0, 0, 2, 1], [0, 1, 0, 1, 0, 1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 1, 0, 0, 0, 0], [2, 1, 2, 1, 0, 0, 0], [2, 0, 1, 2, 1, 0, 0], [2, 0, 0, 1, 2, 1, 0], [2, 0, 0, 0, 1, 2, 1], [2, 0, 0, 0, 0, 1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 1, 0, 0, 0, 0], [2, 1, 2, 1, 0, 0, 0], [2, 0, 1, 2, 1, 0, 0], [2, 0, 0, 1, 2, 1, 0], [2, 0, 0, 0, 1, 2, 1], [2, 0, 0, 0, 0, 1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0, 1, 1, 0], [0, 2, 1, 0, 1, 1], [0, 1, 2, 1, 0, 0], [1, 0, 1, 2, 1, 1], [1, 1, 0, 1, 2, 0], [0, 1, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0, 1, 1, 0], [0, 2, 1, 0, 1, 1], [0, 1, 2, 1, 0, 0], [1, 0, 1, 2, 1, 1], [1, 1, 0, 1, 2, 0], [0, 1, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 1, 0, 0, 1, 0], [2, 2, 1, 1, 0, 2, 2, 0], [2, 1, 2, 2, 0, 0, 2, 1], [1, 1, 2, 2, 2, 1, 0, 0], [0, 0, 0, 2, 2, 0, 2, 1], [0, 2, 0, 1, 0, 2, 2, 1], [1, 2, 2, 0, 2, 2, 2, 0], [0, 0, 1, 0, 1, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 1, 0, 0, 1, 0], [2, 2, 1, 1, 0, 2, 2, 0], [2, 1, 2, 2, 0, 0, 2, 1], [1, 1, 2, 2, 2, 1, 0, 0], [0, 0, 0, 2, 2, 0, 2, 1], [0, 2, 0, 1, 0, 2, 2, 1], [1, 2, 2, 0, 2, 2, 2, 0], [0, 0, 1, 0, 1, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 2, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 2, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 2, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 2, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 2, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 2, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 2, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 2, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 0, 0], [1, 2, 1, 0, 0], [1, 1, 2, 1, 1], [0, 0, 1, 2, 0], [0, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 0, 0], [1, 2, 1, 0, 0], [1, 1, 2, 1, 1], [0, 0, 1, 2, 0], [0, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 1, 0], [1, 2, 1, 0, 1], [0, 1, 2, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 1, 0], [1, 2, 1, 0, 1], [0, 1, 2, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0, 1, 0, 0], [0, 2, 1, 0, 1, 0], [0, 1, 2, 0, 0, 1], [1, 0, 0, 2, 1, 0], [0, 1, 0, 1, 2, 0], [0, 0, 1, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0, 1, 0, 0], [0, 2, 1, 0, 1, 0], [0, 1, 2, 0, 0, 1], [1, 0, 0, 2, 1, 0], [0, 1, 0, 1, 2, 0], [0, 0, 1, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 1, 0, 1, 1, 0, 1, 0], [0, 2, 1, 0, 1, 0, 1, 1, 0], [1, 1, 2, 0, 1, 0, 0, 0, 1], [0, 0, 0, 2, 1, 1, 1, 0, 1], [1, 1, 1, 1, 2, 1, 0, 0, 0], [1, 0, 0, 1, 1, 2, 1, 0, 1], [0, 1, 0, 1, 0, 1, 2, 1, 0], [1, 1, 0, 0, 0, 0, 1, 2, 1], [0, 0, 1, 1, 0, 1, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 1, 0, 1, 1, 0, 1, 0], [0, 2, 1, 0, 1, 0, 1, 1, 0], [1, 1, 2, 0, 1, 0, 0, 0, 1], [0, 0, 0, 2, 1, 1, 1, 0, 1], [1, 1, 1, 1, 2, 1, 0, 0, 0], [1, 0, 0, 1, 1, 2, 1, 0, 1], [0, 1, 0, 1, 0, 1, 2, 1, 0], [1, 1, 0, 0, 0, 0, 1, 2, 1], [0, 0, 1, 1, 0, 1, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 1, 1, 0, 0, 1, 0, 1, 1], [0, 2, 0, 0, 1, 1, 0, 1, 0, 0], [1, 0, 2, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 2, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 2, 1, 0, 1, 1, 0], [0, 1, 1, 1, 1, 2, 0, 0, 1, 1], [1, 0, 1, 0, 0, 0, 2, 1, 1, 0], [0, 1, 0, 1, 1, 0, 1, 2, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 2, 0], [1, 0, 0, 1, 0, 1, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 1, 1, 0, 0, 1, 0, 1, 1], [0, 2, 0, 0, 1, 1, 0, 1, 0, 0], [1, 0, 2, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 2, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 2, 1, 0, 1, 1, 0], [0, 1, 1, 1, 1, 2, 0, 0, 1, 1], [1, 0, 1, 0, 0, 0, 2, 1, 1, 0], [0, 1, 0, 1, 1, 0, 1, 2, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 2, 0], [1, 0, 0, 1, 0, 1, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0, 0], [0, 1, 2, 1, 0, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0, 0], [0, 0, 0, 1, 2, 1, 0, 0], [0, 0, 0, 0, 1, 2, 1, 0], [0, 0, 0, 0, 0, 1, 2, 1], [0, 0, 0, 0, 0, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0, 0], [0, 1, 2, 1, 0, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0, 0], [0, 0, 0, 1, 2, 1, 0, 0], [0, 0, 0, 0, 1, 2, 1, 0], [0, 0, 0, 0, 0, 1, 2, 1], [0, 0, 0, 0, 0, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 1, 0, 2, 0, 2, 1, 0, 1, 2], [2, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2], [1, 0, 2, 2, 0, 1, 2, 1, 2, 0, 1], [0, 1, 2, 2, 1, 0, 2, 0, 1, 2, 0], [2, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2], [0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 1], [2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 2], [1, 0, 1, 0, 0, 0, 0, 2, 1, 0, 1], [0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 0], [1, 0, 0, 2, 0, 1, 0, 0, 0, 2, 1], [2, 2, 1, 0, 2, 1, 2, 1, 0, 1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 1, 0, 2, 0, 2, 1, 0, 1, 2], [2, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2], [1, 0, 2, 2, 0, 1, 2, 1, 2, 0, 1], [0, 1, 2, 2, 1, 0, 2, 0, 1, 2, 0], [2, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2], [0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 1], [2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 2], [1, 0, 1, 0, 0, 0, 0, 2, 1, 0, 1], [0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 0], [1, 0, 0, 2, 0, 1, 0, 0, 0, 2, 1], [2, 2, 1, 0, 2, 1, 2, 1, 0, 1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 1, 1, 0, 1, 0], [0, 2, 0, 0, 1, 0, 1], [1, 0, 2, 0, 0, 1, 0], [1, 0, 0, 2, 1, 0, 1], [0, 1, 0, 1, 2, 1, 0], [1, 0, 1, 0, 1, 2, 1], [0, 1, 0, 1, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 1, 1, 0, 1, 0], [0, 2, 0, 0, 1, 0, 1], [1, 0, 2, 0, 0, 1, 0], [1, 0, 0, 2, 1, 0, 1], [0, 1, 0, 1, 2, 1, 0], [1, 0, 1, 0, 1, 2, 1], [0, 1, 0, 1, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 0, 1, 0], [2, 2, 0, 1, 0, 1], [2, 0, 2, 1, 1, 0], [0, 1, 1, 2, 2, 2], [1, 0, 1, 2, 2, 0], [0, 1, 0, 2, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 0, 1, 0], [2, 2, 0, 1, 0, 1], [2, 0, 2, 1, 1, 0], [0, 1, 1, 2, 2, 2], [1, 0, 1, 2, 2, 0], [0, 1, 0, 2, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 1, 0, 1, 1], [0, 2, 0, 0, 0, 0], [1, 0, 2, 1, 1, 0], [0, 0, 1, 2, 0, 1], [1, 0, 1, 0, 2, 1], [1, 0, 0, 1, 1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 1, 0, 1, 1], [0, 2, 0, 0, 0, 0], [1, 0, 2, 1, 1, 0], [0, 0, 1, 2, 0, 1], [1, 0, 1, 0, 2, 1], [1, 0, 0, 1, 1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 2, 0, 2], [1, 2, 0, 1, 2], [2, 0, 2, 1, 0], [0, 1, 1, 2, 2], [2, 2, 0, 2, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 2, 0, 2], [1, 2, 0, 1, 2], [2, 0, 2, 1, 0], [0, 1, 1, 2, 2], [2, 2, 0, 2, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 2, 1], [1, 2, 1, 2, 0], [0, 1, 2, 0, 2], [2, 2, 0, 2, 1], [1, 0, 2, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 2, 1], [1, 2, 1, 2, 0], [0, 1, 2, 0, 2], [2, 2, 0, 2, 1], [1, 0, 2, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0, 0, 0, 0, 0], [0, 2, 1, 1, 1, 1, 0], [0, 1, 2, 1, 0, 0, 1], [0, 1, 1, 2, 1, 0, 1], [0, 1, 0, 1, 2, 1, 0], [0, 1, 0, 0, 1, 2, 1], [0, 0, 1, 1, 0, 1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0, 0, 0, 0, 0], [0, 2, 1, 1, 1, 1, 0], [0, 1, 2, 1, 0, 0, 1], [0, 1, 1, 2, 1, 0, 1], [0, 1, 0, 1, 2, 1, 0], [0, 1, 0, 0, 1, 2, 1], [0, 0, 1, 1, 0, 1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 0, 0, 0, 0, 0], [2, 2, 0, 2, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 0, 0], [0, 2, 0, 2, 0, 2, 0, 0], [0, 0, 2, 0, 2, 0, 2, 0], [0, 0, 0, 2, 0, 2, 0, 2], [0, 0, 0, 0, 2, 0, 2, 0], [0, 0, 0, 0, 0, 2, 0, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 0, 0, 0, 0, 0], [2, 2, 0, 2, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 0, 0], [0, 2, 0, 2, 0, 2, 0, 0], [0, 0, 2, 0, 2, 0, 2, 0], [0, 0, 0, 2, 0, 2, 0, 2], [0, 0, 0, 0, 2, 0, 2, 0], [0, 0, 0, 0, 0, 2, 0, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 1, 0, 0], [2, 2, 0, 0, 1], [1, 0, 2, 0, 1], [0, 0, 0, 2, 0], [0, 1, 1, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 1, 0, 0], [2, 2, 0, 0, 1], [1, 0, 2, 0, 1], [0, 0, 0, 2, 0], [0, 1, 1, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 0, 0, 0], [2, 0, 2, 0, 1, 0, 1], [2, 0, 0, 2, 0, 1, 0], [2, 0, 1, 0, 2, 0, 1], [2, 0, 0, 1, 0, 2, 0], [2, 0, 1, 0, 1, 0, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 0, 0, 0], [2, 0, 2, 0, 1, 0, 1], [2, 0, 0, 2, 0, 1, 0], [2, 0, 1, 0, 2, 0, 1], [2, 0, 0, 1, 0, 2, 0], [2, 0, 1, 0, 1, 0, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 0, 0, 0, 1], [1, 2, 1, 1, 1, 0, 0], [0, 1, 2, 0, 1, 1, 1], [0, 1, 0, 2, 1, 0, 0], [0, 1, 1, 1, 2, 1, 0], [0, 0, 1, 0, 1, 2, 1], [1, 0, 1, 0, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 0, 0, 0, 1], [1, 2, 1, 1, 1, 0, 0], [0, 1, 2, 0, 1, 1, 1], [0, 1, 0, 2, 1, 0, 0], [0, 1, 1, 1, 2, 1, 0], [0, 0, 1, 0, 1, 2, 1], [1, 0, 1, 0, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 0, 1, 1, 0], [2, 2, 1, 1, 0, 0], [0, 1, 2, 0, 1, 1], [1, 1, 0, 2, 0, 1], [1, 0, 1, 0, 2, 0], [0, 0, 1, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 0, 1, 1, 0], [2, 2, 1, 1, 0, 0], [0, 1, 2, 0, 1, 1], [1, 1, 0, 2, 0, 1], [1, 0, 1, 0, 2, 0], [0, 0, 1, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 1, 1, 0, 0], [0, 2, 2, 1, 1, 0], [1, 2, 2, 0, 0, 1], [1, 1, 0, 2, 2, 1], [0, 1, 0, 2, 2, 0], [0, 0, 1, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 1, 1, 0, 0], [0, 2, 2, 1, 1, 0], [1, 2, 2, 0, 0, 1], [1, 1, 0, 2, 2, 1], [0, 1, 0, 2, 2, 0], [0, 0, 1, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 1, 1, 0, 0], [2, 0, 2, 1, 2, 0, 1, 1], [2, 0, 1, 2, 0, 1, 0, 1], [2, 1, 2, 0, 2, 0, 1, 0], [2, 1, 0, 1, 0, 2, 1, 0], [2, 0, 1, 0, 1, 1, 2, 1], [2, 0, 1, 1, 0, 0, 1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 1, 1, 0, 0], [2, 0, 2, 1, 2, 0, 1, 1], [2, 0, 1, 2, 0, 1, 0, 1], [2, 1, 2, 0, 2, 0, 1, 0], [2, 1, 0, 1, 0, 2, 1, 0], [2, 0, 1, 0, 1, 1, 2, 1], [2, 0, 1, 1, 0, 0, 1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 1, 0], [2, 2, 2, 1, 0, 2], [2, 2, 2, 1, 2, 1], [2, 1, 1, 2, 0, 1], [1, 0, 2, 0, 2, 2], [0, 2, 1, 1, 2, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 1, 0], [2, 2, 2, 1, 0, 2], [2, 2, 2, 1, 2, 1], [2, 1, 1, 2, 0, 1], [1, 0, 2, 0, 2, 2], [0, 2, 1, 1, 2, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0, 0], [1, 2, 1, 1, 1, 1, 1, 1, 1], [0, 1, 2, 0, 0, 0, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0, 0, 0], [0, 1, 0, 0, 2, 0, 0, 0, 0], [0, 1, 0, 0, 0, 2, 0, 0, 0], [0, 1, 0, 0, 0, 0, 2, 0, 0], [0, 1, 0, 0, 0, 0, 0, 2, 0], [0, 1, 0, 0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0, 0], [1, 2, 1, 1, 1, 1, 1, 1, 1], [0, 1, 2, 0, 0, 0, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0, 0, 0], [0, 1, 0, 0, 2, 0, 0, 0, 0], [0, 1, 0, 0, 0, 2, 0, 0, 0], [0, 1, 0, 0, 0, 0, 2, 0, 0], [0, 1, 0, 0, 0, 0, 0, 2, 0], [0, 1, 0, 0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 1, 0, 0, 0, 0, 0], [2, 2, 0, 1, 0, 0, 0, 0], [1, 0, 2, 0, 1, 0, 0, 0], [0, 1, 0, 2, 0, 1, 0, 0], [0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 1, 0, 2, 0, 1], [0, 0, 0, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 1, 0, 0, 0, 0, 0], [2, 2, 0, 1, 0, 0, 0, 0], [1, 0, 2, 0, 1, 0, 0, 0], [0, 1, 0, 2, 0, 1, 0, 0], [0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 1, 0, 2, 0, 1], [0, 0, 0, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 0, 1], [1, 2, 0, 1, 0], [1, 0, 2, 0, 1], [0, 1, 0, 2, 1], [1, 0, 1, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 0, 1], [1, 2, 0, 1, 0], [1, 0, 2, 0, 1], [0, 1, 0, 2, 1], [1, 0, 1, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 1, 0, 1], [1, 2, 0, 0, 1, 0], [1, 0, 2, 1, 0, 0], [1, 0, 1, 2, 1, 0], [0, 1, 0, 1, 2, 1], [1, 0, 0, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 1, 0, 1], [1, 2, 0, 0, 1, 0], [1, 0, 2, 1, 0, 0], [1, 0, 1, 2, 1, 0], [0, 1, 0, 1, 2, 1], [1, 0, 0, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 2, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 2, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 2, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 2, 0], [0, 0, 0, 0, 1, 0, 0, 1, 0, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 2, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 2, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 2, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 2, 0], [0, 0, 0, 0, 1, 0, 0, 1, 0, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 0, 1, 2, 0], [1, 2, 0, 1, 0, 1, 0], [1, 0, 2, 1, 0, 0, 1], [0, 1, 1, 2, 0, 0, 0], [1, 0, 0, 0, 2, 1, 1], [2, 1, 0, 0, 1, 2, 0], [0, 0, 1, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 0, 1, 2, 0], [1, 2, 0, 1, 0, 1, 0], [1, 0, 2, 1, 0, 0, 1], [0, 1, 1, 2, 0, 0, 0], [1, 0, 0, 0, 2, 1, 1], [2, 1, 0, 0, 1, 2, 0], [0, 0, 1, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 0, 0, 1, 0, 0], [0, 2, 1, 0, 1, 1], [0, 1, 2, 1, 0, 0], [1, 0, 1, 2, 0, 1], [0, 1, 0, 0, 2, 0], [0, 1, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 0, 0, 1, 0, 0], [0, 2, 1, 0, 1, 1], [0, 1, 2, 1, 0, 0], [1, 0, 1, 2, 0, 1], [0, 1, 0, 0, 2, 0], [0, 1, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 1, 0, 0, 0, 0], [2, 2, 1, 0, 0, 0, 0], [1, 1, 2, 1, 1, 1, 0], [0, 0, 1, 2, 1, 0, 1], [0, 0, 1, 1, 2, 1, 0], [0, 0, 1, 0, 1, 2, 1], [0, 0, 0, 1, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 1, 0, 0, 0, 0], [2, 2, 1, 0, 0, 0, 0], [1, 1, 2, 1, 1, 1, 0], [0, 0, 1, 2, 1, 0, 1], [0, 0, 1, 1, 2, 1, 0], [0, 0, 1, 0, 1, 2, 1], [0, 0, 0, 1, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 1, 0, 1, 1, 0], [1, 2, 0, 0, 1, 0, 1, 0], [1, 0, 2, 1, 0, 0, 0, 1], [1, 0, 1, 2, 1, 0, 1, 0], [0, 1, 0, 1, 2, 1, 1, 0], [1, 0, 0, 0, 1, 2, 0, 1], [1, 1, 0, 1, 1, 0, 2, 0], [0, 0, 1, 0, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 1, 0, 1, 1, 0], [1, 2, 0, 0, 1, 0, 1, 0], [1, 0, 2, 1, 0, 0, 0, 1], [1, 0, 1, 2, 1, 0, 1, 0], [0, 1, 0, 1, 2, 1, 1, 0], [1, 0, 0, 0, 1, 2, 0, 1], [1, 1, 0, 1, 1, 0, 2, 0], [0, 0, 1, 0, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 1, 0, 0], [1, 2, 0, 0, 1, 1], [1, 0, 2, 1, 0, 0], [1, 0, 1, 2, 1, 0], [0, 1, 0, 1, 2, 1], [0, 1, 0, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 1, 0, 0], [1, 2, 0, 0, 1, 1], [1, 0, 2, 1, 0, 0], [1, 0, 1, 2, 1, 0], [0, 1, 0, 1, 2, 1], [0, 1, 0, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 1, 0, 0, 0, 0, 0], [1, 0, 2, 0, 1, 0, 0, 0, 0], [0, 1, 0, 2, 0, 1, 0, 0, 0], [0, 0, 1, 0, 2, 0, 1, 0, 0], [0, 0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 0, 1, 0, 2, 0, 1], [0, 0, 0, 0, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 1, 0, 0, 0, 0, 0], [1, 0, 2, 0, 1, 0, 0, 0, 0], [0, 1, 0, 2, 0, 1, 0, 0, 0], [0, 0, 1, 0, 2, 0, 1, 0, 0], [0, 0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 0, 1, 0, 2, 0, 1], [0, 0, 0, 0, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 1, 2, 0, 1, 0], [2, 2, 2, 0, 2, 1, 0, 1], [2, 2, 2, 1, 0, 0, 0, 0], [1, 0, 1, 2, 2, 1, 0, 0], [2, 2, 0, 2, 2, 0, 1, 0], [0, 1, 0, 1, 0, 2, 0, 1], [1, 0, 0, 0, 1, 0, 2, 0], [0, 1, 0, 0, 0, 1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 1, 2, 0, 1, 0], [2, 2, 2, 0, 2, 1, 0, 1], [2, 2, 2, 1, 0, 0, 0, 0], [1, 0, 1, 2, 2, 1, 0, 0], [2, 2, 0, 2, 2, 0, 1, 0], [0, 1, 0, 1, 0, 2, 0, 1], [1, 0, 0, 0, 1, 0, 2, 0], [0, 1, 0, 0, 0, 1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 1, 1, 0, 0, 0], [2, 1, 2, 0, 2, 1, 0], [2, 1, 0, 2, 2, 0, 1], [2, 0, 2, 2, 2, 1, 1], [2, 0, 1, 0, 1, 2, 0], [2, 0, 0, 1, 1, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 1, 1, 0, 0, 0], [2, 1, 2, 0, 2, 1, 0], [2, 1, 0, 2, 2, 0, 1], [2, 0, 2, 2, 2, 1, 1], [2, 0, 1, 0, 1, 2, 0], [2, 0, 0, 1, 1, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 2, 1, 2], [1, 2, 2, 0, 1, 0], [0, 2, 2, 1, 0, 1], [2, 0, 1, 2, 0, 2], [1, 1, 0, 0, 2, 1], [2, 0, 1, 2, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 2, 1, 2], [1, 2, 2, 0, 1, 0], [0, 2, 2, 1, 0, 1], [2, 0, 1, 2, 0, 2], [1, 1, 0, 0, 2, 1], [2, 0, 1, 2, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 2, 0, 1, 0, 1, 0, 0], [1, 2, 0, 1, 0, 1, 0, 1, 1], [2, 0, 2, 1, 0, 0, 1, 0, 0], [0, 1, 1, 2, 0, 0, 0, 1, 1], [1, 0, 0, 0, 2, 1, 1, 0, 0], [0, 1, 0, 1, 1, 2, 0, 1, 1], [1, 0, 1, 0, 1, 0, 2, 0, 0], [0, 1, 0, 1, 0, 1, 0, 2, 1], [0, 1, 0, 1, 0, 1, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 2, 0, 1, 0, 1, 0, 0], [1, 2, 0, 1, 0, 1, 0, 1, 1], [2, 0, 2, 1, 0, 0, 1, 0, 0], [0, 1, 1, 2, 0, 0, 0, 1, 1], [1, 0, 0, 0, 2, 1, 1, 0, 0], [0, 1, 0, 1, 1, 2, 0, 1, 1], [1, 0, 1, 0, 1, 0, 2, 0, 0], [0, 1, 0, 1, 0, 1, 0, 2, 1], [0, 1, 0, 1, 0, 1, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 1, 1, 0, 0], [0, 0, 0, 2, 0, 0, 1, 0], [0, 0, 1, 0, 2, 0, 0, 1], [0, 0, 1, 0, 0, 2, 1, 0], [0, 0, 0, 1, 0, 1, 2, 0], [0, 0, 0, 0, 1, 0, 0, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 1, 1, 0, 0], [0, 0, 0, 2, 0, 0, 1, 0], [0, 0, 1, 0, 2, 0, 0, 1], [0, 0, 1, 0, 0, 2, 1, 0], [0, 0, 0, 1, 0, 1, 2, 0], [0, 0, 0, 0, 1, 0, 0, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 1, 0, 0, 0, 0, 0], [1, 0, 2, 1, 0, 0, 0, 0, 0], [0, 1, 1, 2, 0, 1, 0, 0, 0], [0, 0, 0, 0, 2, 0, 1, 0, 1], [0, 0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 0, 1, 0, 2, 1, 0], [0, 0, 0, 0, 0, 1, 1, 2, 0], [0, 0, 0, 0, 1, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 1, 0, 0, 0, 0, 0], [1, 0, 2, 1, 0, 0, 0, 0, 0], [0, 1, 1, 2, 0, 1, 0, 0, 0], [0, 0, 0, 0, 2, 0, 1, 0, 1], [0, 0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 0, 1, 0, 2, 1, 0], [0, 0, 0, 0, 0, 1, 1, 2, 0], [0, 0, 0, 0, 1, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 1, 1, 1, 0], [2, 0, 2, 0, 1, 0, 0], [2, 1, 0, 2, 0, 1, 1], [2, 1, 1, 0, 2, 0, 1], [2, 1, 0, 1, 0, 2, 0], [2, 0, 0, 1, 1, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 1, 1, 1, 0], [2, 0, 2, 0, 1, 0, 0], [2, 1, 0, 2, 0, 1, 1], [2, 1, 1, 0, 2, 0, 1], [2, 1, 0, 1, 0, 2, 0], [2, 0, 0, 1, 1, 0, 2]]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(statements = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]) == 2
    assert candidate(statements = [[2, 1, 0], [1, 2, 1], [0, 1, 0]]) == 0
    assert candidate(statements = [[2, 1, 0, 2], [1, 2, 2, 0], [0, 2, 2, 1], [2, 0, 1, 2]]) == 2
    assert candidate(statements = [[2, 2], [2, 2]]) == 2
    assert candidate(statements = [[2, 1, 0, 0], [0, 2, 1, 0], [1, 1, 2, 0], [0, 0, 0, 2]]) == 1
    assert candidate(statements = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 2
    assert candidate(statements = [[2, 1, 1], [0, 2, 1], [0, 0, 2]]) == 1
    assert candidate(statements = [[2, 2, 0, 0], [2, 2, 0, 0], [0, 0, 2, 1], [0, 0, 1, 2]]) == 2
    assert candidate(statements = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]) == 1
    assert candidate(statements = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]) == 3
    assert candidate(statements = [[2, 0, 0, 0, 0], [0, 2, 1, 1, 1], [0, 1, 2, 1, 0], [0, 1, 1, 2, 1], [0, 1, 0, 1, 2]]) == 1
    assert candidate(statements = [[2, 1], [0, 2]]) == 1
    assert candidate(statements = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]) == 0
    assert candidate(statements = [[2, 2, 2, 2], [2, 2, 0, 2], [2, 0, 2, 2], [2, 2, 2, 2]]) == 3
    assert candidate(statements = [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]) == 1
    assert candidate(statements = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]) == 3
    assert candidate(statements = [[2, 0], [0, 2]]) == 1
    assert candidate(statements = [[2, 2, 2, 0], [2, 2, 2, 1], [2, 2, 2, 0], [1, 0, 1, 2]]) == 2
    assert candidate(statements = [[2, 0, 1], [0, 2, 1], [1, 1, 2]]) == 0
    assert candidate(statements = [[2, 0, 1, 2], [1, 2, 0, 2], [0, 0, 2, 1], [2, 2, 1, 2]]) == 2
    assert candidate(statements = [[2, 0, 0, 1, 0, 1], [0, 2, 1, 0, 0, 0], [0, 1, 2, 1, 1, 0], [1, 0, 1, 2, 1, 1], [0, 0, 1, 1, 2, 0], [1, 0, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 1, 0, 2, 1, 2, 1, 2, 0], [1, 2, 2, 0, 1, 0, 1, 0, 1], [0, 2, 2, 1, 0, 1, 0, 1, 0], [2, 0, 1, 2, 0, 2, 1, 2, 1], [1, 1, 0, 0, 2, 1, 0, 1, 0], [2, 0, 1, 2, 1, 2, 1, 2, 0], [1, 0, 1, 0, 0, 1, 2, 1, 1], [2, 1, 0, 2, 0, 2, 1, 2, 0], [0, 1, 0, 1, 0, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[1, 0, 1, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 0, 1, 1]]) == 0
    assert candidate(statements = [[2, 1, 0, 2, 1], [1, 2, 1, 0, 2], [0, 1, 2, 1, 0], [2, 0, 1, 2, 0], [1, 2, 0, 0, 2]]) == 0
    assert candidate(statements = [[2, 0, 2, 1, 0, 2, 0], [0, 2, 0, 0, 2, 0, 1], [2, 0, 2, 0, 2, 1, 0], [1, 0, 0, 2, 0, 0, 1], [0, 2, 2, 0, 2, 0, 0], [2, 0, 1, 0, 0, 2, 1], [0, 1, 0, 1, 0, 1, 2]]) == 1
    assert candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 1, 0, 0, 0, 0], [2, 1, 2, 1, 0, 0, 0], [2, 0, 1, 2, 1, 0, 0], [2, 0, 0, 1, 2, 1, 0], [2, 0, 0, 0, 1, 2, 1], [2, 0, 0, 0, 0, 1, 2]]) == 1
    assert candidate(statements = [[2, 0, 0, 1, 1, 0], [0, 2, 1, 0, 1, 1], [0, 1, 2, 1, 0, 0], [1, 0, 1, 2, 1, 1], [1, 1, 0, 1, 2, 0], [0, 1, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 2, 2, 1, 0, 0, 1, 0], [2, 2, 1, 1, 0, 2, 2, 0], [2, 1, 2, 2, 0, 0, 2, 1], [1, 1, 2, 2, 2, 1, 0, 0], [0, 0, 0, 2, 2, 0, 2, 1], [0, 2, 0, 1, 0, 2, 2, 1], [1, 2, 2, 0, 2, 2, 2, 0], [0, 0, 1, 0, 1, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 2, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 2, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 2, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 2, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 2, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 2, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]]) == 2
    assert candidate(statements = [[2, 1, 1, 0, 0], [1, 2, 1, 0, 0], [1, 1, 2, 1, 1], [0, 0, 1, 2, 0], [0, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 1, 0, 1, 0], [1, 2, 1, 0, 1], [0, 1, 2, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 0, 0, 1, 0, 0], [0, 2, 1, 0, 1, 0], [0, 1, 2, 0, 0, 1], [1, 0, 0, 2, 1, 0], [0, 1, 0, 1, 2, 0], [0, 0, 1, 0, 0, 2]]) == 0
    assert candidate(statements = [[2, 0, 1, 0, 1, 1, 0, 1, 0], [0, 2, 1, 0, 1, 0, 1, 1, 0], [1, 1, 2, 0, 1, 0, 0, 0, 1], [0, 0, 0, 2, 1, 1, 1, 0, 1], [1, 1, 1, 1, 2, 1, 0, 0, 0], [1, 0, 0, 1, 1, 2, 1, 0, 1], [0, 1, 0, 1, 0, 1, 2, 1, 0], [1, 1, 0, 0, 0, 0, 1, 2, 1], [0, 0, 1, 1, 0, 1, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 0, 1, 1, 0, 0, 1, 0, 1, 1], [0, 2, 0, 0, 1, 1, 0, 1, 0, 0], [1, 0, 2, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 2, 0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 2, 1, 0, 1, 1, 0], [0, 1, 1, 1, 1, 2, 0, 0, 1, 1], [1, 0, 1, 0, 0, 0, 2, 1, 1, 0], [0, 1, 0, 1, 1, 0, 1, 2, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 2, 0], [1, 0, 0, 1, 0, 1, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0, 0], [0, 1, 2, 1, 0, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0, 0], [0, 0, 0, 1, 2, 1, 0, 0], [0, 0, 0, 0, 1, 2, 1, 0], [0, 0, 0, 0, 0, 1, 2, 1], [0, 0, 0, 0, 0, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 2, 1, 0, 2, 0, 2, 1, 0, 1, 2], [2, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2], [1, 0, 2, 2, 0, 1, 2, 1, 2, 0, 1], [0, 1, 2, 2, 1, 0, 2, 0, 1, 2, 0], [2, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2], [0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 1], [2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 2], [1, 0, 1, 0, 0, 0, 0, 2, 1, 0, 1], [0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 0], [1, 0, 0, 2, 0, 1, 0, 0, 0, 2, 1], [2, 2, 1, 0, 2, 1, 2, 1, 0, 1, 2]]) == 1
    assert candidate(statements = [[2, 0, 1, 1, 0, 1, 0], [0, 2, 0, 0, 1, 0, 1], [1, 0, 2, 0, 0, 1, 0], [1, 0, 0, 2, 1, 0, 1], [0, 1, 0, 1, 2, 1, 0], [1, 0, 1, 0, 1, 2, 1], [0, 1, 0, 1, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 2, 2, 0, 1, 0], [2, 2, 0, 1, 0, 1], [2, 0, 2, 1, 1, 0], [0, 1, 1, 2, 2, 2], [1, 0, 1, 2, 2, 0], [0, 1, 0, 2, 0, 2]]) == 0
    assert candidate(statements = [[2, 0, 1, 0, 1, 1], [0, 2, 0, 0, 0, 0], [1, 0, 2, 1, 1, 0], [0, 0, 1, 2, 0, 1], [1, 0, 1, 0, 2, 1], [1, 0, 0, 1, 1, 2]]) == 1
    assert candidate(statements = [[2, 1, 2, 0, 2], [1, 2, 0, 1, 2], [2, 0, 2, 1, 0], [0, 1, 1, 2, 2], [2, 2, 0, 2, 1]]) == 1
    assert candidate(statements = [[2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2]]) == 1
    assert candidate(statements = [[2, 1, 0, 2, 1], [1, 2, 1, 2, 0], [0, 1, 2, 0, 2], [2, 2, 0, 2, 1], [1, 0, 2, 1, 2]]) == 0
    assert candidate(statements = [[2, 0, 0, 0, 0, 0, 0], [0, 2, 1, 1, 1, 1, 0], [0, 1, 2, 1, 0, 0, 1], [0, 1, 1, 2, 1, 0, 1], [0, 1, 0, 1, 2, 1, 0], [0, 1, 0, 0, 1, 2, 1], [0, 0, 1, 1, 0, 1, 2]]) == 1
    assert candidate(statements = [[2, 2, 2, 0, 0, 0, 0, 0], [2, 2, 0, 2, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 0, 0], [0, 2, 0, 2, 0, 2, 0, 0], [0, 0, 2, 0, 2, 0, 2, 0], [0, 0, 0, 2, 0, 2, 0, 2], [0, 0, 0, 0, 2, 0, 2, 0], [0, 0, 0, 0, 0, 2, 0, 2]]) == 2
    assert candidate(statements = [[2, 2, 1, 0, 0], [2, 2, 0, 0, 1], [1, 0, 2, 0, 1], [0, 0, 0, 2, 0], [0, 1, 1, 0, 2]]) == 1
    assert candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 0, 0, 0], [2, 0, 2, 0, 1, 0, 1], [2, 0, 0, 2, 0, 1, 0], [2, 0, 1, 0, 2, 0, 1], [2, 0, 0, 1, 0, 2, 0], [2, 0, 1, 0, 1, 0, 2]]) == 4
    assert candidate(statements = [[2, 1, 0, 0, 0, 0, 1], [1, 2, 1, 1, 1, 0, 0], [0, 1, 2, 0, 1, 1, 1], [0, 1, 0, 2, 1, 0, 0], [0, 1, 1, 1, 2, 1, 0], [0, 0, 1, 0, 1, 2, 1], [1, 0, 1, 0, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 2, 0, 1, 1, 0], [2, 2, 1, 1, 0, 0], [0, 1, 2, 0, 1, 1], [1, 1, 0, 2, 0, 1], [1, 0, 1, 0, 2, 0], [0, 0, 1, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 2, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]]) == 10
    assert candidate(statements = [[2, 0, 1, 1, 0, 0], [0, 2, 2, 1, 1, 0], [1, 2, 2, 0, 0, 1], [1, 1, 0, 2, 2, 1], [0, 1, 0, 2, 2, 0], [0, 0, 1, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 0, 1, 1, 0, 0], [2, 0, 2, 1, 2, 0, 1, 1], [2, 0, 1, 2, 0, 1, 0, 1], [2, 1, 2, 0, 2, 0, 1, 0], [2, 1, 0, 1, 0, 2, 1, 0], [2, 0, 1, 0, 1, 1, 2, 1], [2, 0, 1, 1, 0, 0, 1, 2]]) == 1
    assert candidate(statements = [[2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2]]) == 8
    assert candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 12
    assert candidate(statements = [[2, 2, 2, 2, 1, 0], [2, 2, 2, 1, 0, 2], [2, 2, 2, 1, 2, 1], [2, 1, 1, 2, 0, 1], [1, 0, 2, 0, 2, 2], [0, 2, 1, 1, 2, 2]]) == 4
    assert candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0, 0], [1, 2, 1, 1, 1, 1, 1, 1, 1], [0, 1, 2, 0, 0, 0, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0, 0, 0], [0, 1, 0, 0, 2, 0, 0, 0, 0], [0, 1, 0, 0, 0, 2, 0, 0, 0], [0, 1, 0, 0, 0, 0, 2, 0, 0], [0, 1, 0, 0, 0, 0, 0, 2, 0], [0, 1, 0, 0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(statements = [[2, 2, 1, 0, 0, 0, 0, 0], [2, 2, 0, 1, 0, 0, 0, 0], [1, 0, 2, 0, 1, 0, 0, 0], [0, 1, 0, 2, 0, 1, 0, 0], [0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 1, 0, 2, 0, 1], [0, 0, 0, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 1, 1, 0, 1], [1, 2, 0, 1, 0], [1, 0, 2, 0, 1], [0, 1, 0, 2, 1], [1, 0, 1, 1, 2]]) == 0
    assert candidate(statements = [[2, 1, 1, 1, 0, 1], [1, 2, 0, 0, 1, 0], [1, 0, 2, 1, 0, 0], [1, 0, 1, 2, 1, 0], [0, 1, 0, 1, 2, 1], [1, 0, 0, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 2, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 2, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 2, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 2, 0], [0, 0, 0, 0, 1, 0, 0, 1, 0, 2]]) == 2
    assert candidate(statements = [[2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [2, 2, 2, 2, 0, 0, 0, 0], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2], [0, 0, 0, 0, 2, 2, 2, 2]]) == 4
    assert candidate(statements = [[2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2], [2, 2, 2, 1, 2, 2, 2, 2, 2]]) == 9
    assert candidate(statements = [[2, 1, 1, 0, 1, 2, 0], [1, 2, 0, 1, 0, 1, 0], [1, 0, 2, 1, 0, 0, 1], [0, 1, 1, 2, 0, 0, 0], [1, 0, 0, 0, 2, 1, 1], [2, 1, 0, 0, 1, 2, 0], [0, 0, 1, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 0, 0, 1, 0, 0], [0, 2, 1, 0, 1, 1], [0, 1, 2, 1, 0, 0], [1, 0, 1, 2, 0, 1], [0, 1, 0, 0, 2, 0], [0, 1, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 2, 1, 0, 0, 0, 0], [2, 2, 1, 0, 0, 0, 0], [1, 1, 2, 1, 1, 1, 0], [0, 0, 1, 2, 1, 0, 1], [0, 0, 1, 1, 2, 1, 0], [0, 0, 1, 0, 1, 2, 1], [0, 0, 0, 1, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 1, 2, 0, 2, 1, 2, 0, 2, 1], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]]) == 8
    assert candidate(statements = [[2, 1, 1, 1, 0, 1, 1, 0], [1, 2, 0, 0, 1, 0, 1, 0], [1, 0, 2, 1, 0, 0, 0, 1], [1, 0, 1, 2, 1, 0, 1, 0], [0, 1, 0, 1, 2, 1, 1, 0], [1, 0, 0, 0, 1, 2, 0, 1], [1, 1, 0, 1, 1, 0, 2, 0], [0, 0, 1, 0, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 1, 1, 1, 0, 0], [1, 2, 0, 0, 1, 1], [1, 0, 2, 1, 0, 0], [1, 0, 1, 2, 1, 0], [0, 1, 0, 1, 2, 1], [0, 1, 0, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 1, 0, 0, 0, 0, 0], [1, 0, 2, 0, 1, 0, 0, 0, 0], [0, 1, 0, 2, 0, 1, 0, 0, 0], [0, 0, 1, 0, 2, 0, 1, 0, 0], [0, 0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 0, 1, 0, 2, 0, 1], [0, 0, 0, 0, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 2, 2, 1, 2, 0, 1, 0], [2, 2, 2, 0, 2, 1, 0, 1], [2, 2, 2, 1, 0, 0, 0, 0], [1, 0, 1, 2, 2, 1, 0, 0], [2, 2, 0, 2, 2, 0, 1, 0], [0, 1, 0, 1, 0, 2, 0, 1], [1, 0, 0, 0, 1, 0, 2, 0], [0, 1, 0, 0, 0, 1, 0, 2]]) == 0
    assert candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 1, 1, 0, 0, 0], [2, 1, 2, 0, 2, 1, 0], [2, 1, 0, 2, 2, 0, 1], [2, 0, 2, 2, 2, 1, 1], [2, 0, 1, 0, 1, 2, 0], [2, 0, 0, 1, 1, 0, 2]]) == 1
    assert candidate(statements = [[2, 1, 0, 2, 1, 2], [1, 2, 2, 0, 1, 0], [0, 2, 2, 1, 0, 1], [2, 0, 1, 2, 0, 2], [1, 1, 0, 0, 2, 1], [2, 0, 1, 2, 1, 2]]) == 0
    assert candidate(statements = [[2, 1, 2, 0, 1, 0, 1, 0, 0], [1, 2, 0, 1, 0, 1, 0, 1, 1], [2, 0, 2, 1, 0, 0, 1, 0, 0], [0, 1, 1, 2, 0, 0, 0, 1, 1], [1, 0, 0, 0, 2, 1, 1, 0, 0], [0, 1, 0, 1, 1, 2, 0, 1, 1], [1, 0, 1, 0, 1, 0, 2, 0, 0], [0, 1, 0, 1, 0, 1, 0, 2, 1], [0, 1, 0, 1, 0, 1, 0, 1, 2]]) == 0
    assert candidate(statements = [[2, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 1, 1, 0, 0], [0, 0, 0, 2, 0, 0, 1, 0], [0, 0, 1, 0, 2, 0, 0, 1], [0, 0, 1, 0, 0, 2, 1, 0], [0, 0, 0, 1, 0, 1, 2, 0], [0, 0, 0, 0, 1, 0, 0, 2]]) == 2
    assert candidate(statements = [[2, 1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 1, 0, 0, 0, 0, 0], [1, 0, 2, 1, 0, 0, 0, 0, 0], [0, 1, 1, 2, 0, 1, 0, 0, 0], [0, 0, 0, 0, 2, 0, 1, 0, 1], [0, 0, 0, 1, 0, 2, 0, 1, 0], [0, 0, 0, 0, 1, 0, 2, 1, 0], [0, 0, 0, 0, 0, 1, 1, 2, 0], [0, 0, 0, 0, 1, 0, 0, 0, 2]]) == 0
    assert candidate(statements = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 0, 1, 1, 1, 0], [2, 0, 2, 0, 1, 0, 0], [2, 1, 0, 2, 0, 1, 1], [2, 1, 1, 0, 2, 0, 1], [2, 1, 0, 1, 0, 2, 0], [2, 0, 0, 1, 1, 0, 2]]) == 1


