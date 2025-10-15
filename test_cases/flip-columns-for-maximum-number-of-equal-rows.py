def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1], [1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1], [1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1], [0, 0, 0], [1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1], [0, 0, 0], [1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1], [1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1], [1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1], [1, 0, 1, 0], [0, 1, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1], [1, 0, 1, 0], [0, 1, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0], [0, 0], [1, 1], [1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0], [0, 0], [1, 1], [1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 1], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 0, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 1], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 0, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 0, 1], [1, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 0, 1], [1, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 1], [1, 0, 1, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 1], [1, 0, 1, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 1, 1], [1, 1, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 1, 1], [1, 1, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 1, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 1, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 1, 1, 0, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 1, 1, 0, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(matrix = [[0, 1], [1, 0]]) == 2
    assert candidate(matrix = [[1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]) == 3
    assert candidate(matrix = [[1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 0, 0]]) == 1
    assert candidate(matrix = [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1]]) == 3
    assert candidate(matrix = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1]]) == 2
    assert candidate(matrix = [[1, 1, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert candidate(matrix = [[0, 1], [1, 1]]) == 1
    assert candidate(matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]) == 2
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]) == 3
    assert candidate(matrix = [[1, 0, 0, 1], [1, 0, 1, 0], [0, 1, 0, 0]]) == 1
    assert candidate(matrix = [[0, 0], [0, 0], [1, 1], [1, 1]]) == 4
    assert candidate(matrix = [[0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0]]) == 4
    assert candidate(matrix = [[1, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1]]) == 4
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]]) == 2
    assert candidate(matrix = [[1, 1, 1, 0, 1], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 0, 0, 1]]) == 2
    assert candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]]) == 4
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1], [1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]) == 2
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 2
    assert candidate(matrix = [[1, 0, 0, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1, 0, 0, 0]]) == 2
    assert candidate(matrix = [[1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 4
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0]]) == 2
    assert candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2
    assert candidate(matrix = [[1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[0, 1, 1, 0, 1], [1, 0, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0]]) == 4
    assert candidate(matrix = [[0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0]]) == 4
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2
    assert candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 2
    assert candidate(matrix = [[1, 0, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0]]) == 1
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 2
    assert candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 1], [1, 0, 1, 0, 0]]) == 2
    assert candidate(matrix = [[1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) == 2
    assert candidate(matrix = [[0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 1, 1], [1, 1, 0, 0, 0]]) == 2
    assert candidate(matrix = [[1, 1, 1, 0, 1, 0], [0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]]) == 2
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 4
    assert candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 0, 1]]) == 2
    assert candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1]]) == 4
    assert candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1]]) == 4
    assert candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 4
    assert candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 1
    assert candidate(matrix = [[0, 1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 1]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1]]) == 2
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 3
    assert candidate(matrix = [[1, 1, 1, 0, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0]]) == 2
    assert candidate(matrix = [[0, 0, 1, 1, 0], [0, 0, 1, 1, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 0]]) == 2
    assert candidate(matrix = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 3
    assert candidate(matrix = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1]]) == 4
    assert candidate(matrix = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 1, 1, 0]]) == 2
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0]]) == 2
    assert candidate(matrix = [[1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]]) == 4
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]]) == 2
    assert candidate(matrix = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1]]) == 4
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1]]) == 4
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0]]) == 3
    assert candidate(matrix = [[1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 2
    assert candidate(matrix = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 4
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]) == 2
    assert candidate(matrix = [[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]]) == 4
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 2
    assert candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]) == 1
    assert candidate(matrix = [[0, 0, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]) == 2
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]) == 2
    assert candidate(matrix = [[0, 1, 1, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 0, 1]]) == 2
    assert candidate(matrix = [[1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 0, 1, 1, 1]]) == 3
    assert candidate(matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]) == 2
    assert candidate(matrix = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]) == 1
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1]]) == 2
    assert candidate(matrix = [[0, 1, 1, 1, 0, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]) == 3


