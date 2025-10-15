def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [[0, 1], [2, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1], [2, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [1, 0, 0], [0, 2, -1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [1, 0, 0], [0, 2, -1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 2], [-1, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 2], [-1, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 1], [0, 0, 0], [2, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 1], [0, 0, 0], [2, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 2], [-1, 0, -1, -1], [0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 2], [-1, 0, -1, -1], [0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0], [0, 0, 0], [0, 0, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0], [0, 0, 0], [0, 0, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0], [0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0], [0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1], [0, 0, 0], [0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1], [0, 0, 0], [0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, 0], [0, 0, 0, 0], [0, 0, 2, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, 0], [0, 0, 0, 0], [0, 0, 2, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1], [0], [0], [2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1], [0], [0], [2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, -1, 0], [0, -1, 0, 0, 2], [0, 0, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, -1, 0], [0, -1, 0, 0, 2], [0, 0, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1], [0, 0, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1], [0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1], [0, 0, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1], [0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [-1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [-1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 972: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0], [0, 0, 0, -1, 2, -1, 0], [0, 0, 0, 0, -1, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0], [0, 0, 0, -1, 2, -1, 0], [0, 0, 0, 0, -1, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, -1, 2, 0], [0, 0, 0, 0, 0, 0]]) == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, -1, 2, 0], [0, 0, 0, 0, 0, 0]]) == 272: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2], [0, 0, 0, -1, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2], [0, 0, 0, -1, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, -1, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, -1, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 378: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2]]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2]]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 378: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 2, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 2, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, -1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, -1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [2, -1, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [2, -1, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, -1], [0, 0, -1, 0], [0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, -1], [0, 0, -1, 0], [0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 1], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 1], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, -1], [0, 0, 2, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, -1], [0, 0, 2, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, -1, -1, -1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, -1, -1, -1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, -1], [0, 0, 2, 0], [0, 0, -1, 0], [0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, -1], [0, 0, 2, 0], [0, 0, -1, 0], [0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, -1, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, -1, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 378
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 378: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2]]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2]]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, -1, -1, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, -1, -1, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 1], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 1], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 2, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 2, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 2, -1, 0], [0, 0, 0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 2, -1, 0], [0, 0, 0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 2, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 2, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, -1, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, -1, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 2, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 2, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, 2, -1, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, 2, -1, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, -1], [0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, -1], [0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2]]) == 1670
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2]]) == 1670: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 2], [-1, 0, -1, 0, -1], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 2], [-1, 0, -1, 0, -1], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, -1, 2, -1], [0, -1, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, -1, 2, -1], [0, -1, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 2], [0, 0, -1, -1, 0], [0, -1, 0, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 2], [0, 0, -1, -1, 0], [0, -1, 0, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [[0, 1], [2, 0]]) == 0
    assert candidate(grid = [[0, 0, 0], [1, 0, 0], [0, 2, -1]]) == 0
    assert candidate(grid = [[1, 0, -1, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 2], [-1, 0, 0], [0, 0, 0]]) == 0
    assert candidate(grid = [[0, 0, 1], [0, 0, 0], [2, 0, 0]]) == 2
    assert candidate(grid = [[1, 0, 0, 2], [-1, 0, -1, -1], [0, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0], [0, 0, 0], [0, 0, 2]]) == 2
    assert candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
    assert candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
    assert candidate(grid = [[1, 0], [0, 2]]) == 0
    assert candidate(grid = [[1, 0, -1], [0, 0, 0], [0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, -1, 0], [0, 0, 0, 0], [0, 0, 2, 0]]) == 0
    assert candidate(grid = [[1, 0, 2]]) == 1
    assert candidate(grid = [[1, 0, 0, 2]]) == 1
    assert candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 0]]) == 0
    assert candidate(grid = [[1], [0], [0], [2]]) == 1
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, -1, 0], [0, -1, 0, 0, 2], [0, 0, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1], [0, 0, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1], [0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0], [0, -1, 0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [-1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 2]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 104
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 972
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0], [0, 0, 0, -1, 2, -1, 0], [0, 0, 0, 0, -1, 0, 0]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, -1, 2, 0], [0, 0, 0, 0, 0, 0]]) == 272
    assert candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2], [0, 0, 0, -1, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, -1, 2]]) == 1
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 378
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 2]]) == 46
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 378
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 2, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, -1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [2, -1, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, -1], [0, 0, -1, 0], [0, 0, 0, 2]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 1], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0]]) == 3
    assert candidate(grid = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, -1], [0, 0, 2, 0]]) == 0
    assert candidate(grid = [[1, -1, -1, -1, -1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 20
    assert candidate(grid = [[1, 0, 0, -1], [0, 0, 2, 0], [0, 0, -1, 0], [0, 0, 0, 0]]) == 0
    assert candidate(grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, -1, 0], [0, 0, 0, -1, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 378
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 2]]) == 68
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, -1, -1, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 1], [0, -1, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0]]) == 11
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 2, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 42
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 2, -1, 0], [0, 0, 0, 0, 0]]) == 1
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 2, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, -1, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, -1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0]]) == 4
    assert candidate(grid = [[1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 2, 0]]) == 1
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
    assert candidate(grid = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 2, 0, 0, 0]]) == 1
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, -1, 2, -1, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, -1, 0, -1, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, -1], [0, 0, 0, 2]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, -1, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, -1, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 2]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2]]) == 1670
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == 48
    assert candidate(grid = [[1, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 2], [-1, 0, -1, 0, -1], [0, 0, 0, 0, 0], [0, -1, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, -1, 2, -1], [0, -1, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 2], [0, 0, -1, -1, 0], [0, -1, 0, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 2]]) == 0


