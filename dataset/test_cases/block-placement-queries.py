def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 2], [1, 3], [2, 5, 3], [1, 4], [2, 5, 1]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 2], [1, 3], [2, 5, 3], [1, 4], [2, 5, 1]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 3], [2, 5, 2], [1, 10], [2, 10, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 3], [2, 5, 2], [1, 10], [2, 10, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [2, 4, 1], [2, 4, 2]]) == [False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [2, 4, 1], [2, 4, 2]]) == [False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 12, 3]]) == [False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 12, 3]]) == [False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 1], [1, 3], [1, 4], [2, 5, 1]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 1], [1, 3], [1, 4], [2, 5, 1]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 10, 5]]) == [False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 10, 5]]) == [False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 3], [1, 2], [2, 5, 2], [1, 4], [2, 5, 3]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 3], [1, 2], [2, 5, 2], [1, 4], [2, 5, 3]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 5], [1, 10], [2, 10, 3], [2, 10, 7]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 5], [1, 10], [2, 10, 3], [2, 10, 7]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 4, 2]]) == [False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 4, 2]]) == [False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [2, 6, 2], [2, 6, 4]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [2, 6, 2], [2, 6, 4]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 10, 4], [1, 15], [2, 15, 7]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 10, 4], [1, 15], [2, 15, 7]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 5, 2], [2, 10, 8]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 5, 2], [2, 10, 8]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [1, 3], [2, 5, 2]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [1, 3], [2, 5, 2]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [1, 5], [2, 10, 3], [2, 5, 2]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [1, 5], [2, 10, 3], [2, 5, 2]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]) == [False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]) == [False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 5], [1, 10], [2, 12, 3], [2, 12, 7], [2, 12, 10]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 5], [1, 10], [2, 12, 3], [2, 12, 7], [2, 12, 10]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 2, 1], [1, 3], [2, 4, 2], [1, 5], [2, 6, 3], [1, 7], [2, 8, 4], [1, 9], [2, 10, 5]]) == [True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 2, 1], [1, 3], [2, 4, 2], [1, 5], [2, 6, 3], [1, 7], [2, 8, 4], [1, 9], [2, 10, 5]]) == [True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [2, 10, 5], [2, 10, 4], [2, 10, 3], [2, 10, 2], [2, 10, 1], [1, 12], [2, 12, 6], [2, 12, 5], [2, 12, 4], [2, 12, 3], [2, 12, 2], [2, 12, 1]]) == [False, False, False, True, True, False, False, False, False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [2, 10, 5], [2, 10, 4], [2, 10, 3], [2, 10, 2], [2, 10, 1], [1, 12], [2, 12, 6], [2, 12, 5], [2, 12, 4], [2, 12, 3], [2, 12, 2], [2, 12, 1]]) == [False, False, False, True, True, False, False, False, False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 5], [2, 5, 4], [2, 5, 3], [2, 5, 2], [2, 5, 1]]) == [False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 5], [2, 5, 4], [2, 5, 3], [2, 5, 2], [2, 5, 1]]) == [False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [2, 10, 9], [2, 10, 3], [2, 10, 5]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [2, 10, 9], [2, 10, 3], [2, 10, 5]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 9], [2, 10, 8], [2, 10, 7], [2, 10, 6], [2, 10, 5], [2, 10, 4], [2, 10, 3], [2, 10, 2], [2, 10, 1]]) == [False, False, False, False, False, False, False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 9], [2, 10, 8], [2, 10, 7], [2, 10, 6], [2, 10, 5], [2, 10, 4], [2, 10, 3], [2, 10, 2], [2, 10, 1]]) == [False, False, False, False, False, False, False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [2, 10, 8], [2, 8, 4], [2, 6, 2]]) == [False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [2, 10, 8], [2, 8, 4], [2, 6, 2]]) == [False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 8], [2, 10, 4], [2, 10, 2]]) == [False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 8], [2, 10, 4], [2, 10, 2]]) == [False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 2], [2, 5, 3], [2, 5, 4], [2, 5, 5]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 2], [2, 5, 3], [2, 5, 4], [2, 5, 5]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 1], [2, 5, 2], [2, 5, 3], [2, 5, 4], [2, 5, 5]]) == [True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 1], [2, 5, 2], [2, 5, 3], [2, 5, 4], [2, 5, 5]]) == [True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 10], [2, 5, 4], [2, 10, 8], [1, 15], [2, 20, 5], [2, 20, 10], [2, 20, 15], [2, 20, 20]]) == [True, True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 10], [2, 5, 4], [2, 10, 8], [1, 15], [2, 20, 5], [2, 20, 10], [2, 20, 15], [2, 20, 20]]) == [True, True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [1, 12], [1, 14], [1, 16], [1, 18], [1, 20], [2, 21, 10], [2, 21, 20], [2, 21, 30], [2, 21, 40], [2, 21, 50]]) == [False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [1, 12], [1, 14], [1, 16], [1, 18], [1, 20], [2, 21, 10], [2, 21, 20], [2, 21, 30], [2, 21, 40], [2, 21, 50]]) == [False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [1, 11], [1, 13], [1, 15], [1, 17], [1, 19], [2, 20, 1], [2, 20, 2], [2, 20, 3], [2, 20, 4], [2, 20, 5], [2, 20, 6], [2, 20, 7], [2, 20, 8], [2, 20, 9], [2, 20, 10]]) == [True, True, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [1, 11], [1, 13], [1, 15], [1, 17], [1, 19], [2, 20, 1], [2, 20, 2], [2, 20, 3], [2, 20, 4], [2, 20, 5], [2, 20, 6], [2, 20, 7], [2, 20, 8], [2, 20, 9], [2, 20, 10]]) == [True, True, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 4], [2, 5, 3], [1, 6], [2, 7, 4], [1, 8], [2, 9, 5]]) == [True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 4], [2, 5, 3], [1, 6], [2, 7, 4], [1, 8], [2, 9, 5]]) == [True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [1, 4], [1, 5], [2, 5, 4], [2, 5, 1]]) == [False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [1, 4], [1, 5], [2, 5, 4], [2, 5, 1]]) == [False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1], [2, 10, 5], [2, 9, 4], [2, 8, 3], [2, 7, 2], [2, 6, 1]]) == [False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1], [2, 10, 5], [2, 9, 4], [2, 8, 3], [2, 7, 2], [2, 6, 1]]) == [False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [2, 3, 1], [1, 4], [2, 5, 2], [1, 6], [2, 7, 3], [1, 8], [2, 9, 4], [1, 10], [2, 11, 5], [1, 12], [2, 13, 6]]) == [True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [2, 3, 1], [1, 4], [2, 5, 2], [1, 6], [2, 7, 3], [1, 8], [2, 9, 4], [1, 10], [2, 11, 5], [1, 12], [2, 13, 6]]) == [True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 12, 3], [1, 7], [2, 10, 6], [2, 8, 2]]) == [True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 12, 3], [1, 7], [2, 10, 6], [2, 8, 2]]) == [True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [2, 2, 1], [2, 2, 2], [1, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3], [1, 4], [2, 4, 1], [2, 4, 2], [2, 4, 3], [2, 4, 4]]) == [True, False, True, False, False, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [2, 2, 1], [2, 2, 2], [1, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3], [1, 4], [2, 4, 1], [2, 4, 2], [2, 4, 3], [2, 4, 4]]) == [True, False, True, False, False, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [1, 12], [1, 14], [2, 16, 12], [2, 16, 8], [2, 16, 4], [2, 16, 6], [2, 16, 10], [2, 16, 14]]) == [False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [1, 12], [1, 14], [2, 16, 12], [2, 16, 8], [2, 16, 4], [2, 16, 6], [2, 16, 10], [2, 16, 14]]) == [False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 2], [2, 10, 4], [2, 10, 6], [2, 10, 8], [2, 10, 10]]) == [True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 2], [2, 10, 4], [2, 10, 6], [2, 10, 8], [2, 10, 10]]) == [True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 4], [1, 5], [2, 6, 3], [2, 7, 4], [2, 8, 5]]) == [True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 4], [1, 5], [2, 6, 3], [2, 7, 4], [2, 8, 5]]) == [True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 2, 1], [1, 3], [2, 4, 2], [1, 5], [2, 6, 3], [1, 7], [2, 8, 4], [1, 9], [2, 10, 5], [1, 11], [2, 12, 6], [1, 13], [2, 14, 7], [1, 14], [2, 15, 8], [1, 16], [2, 17, 9], [1, 17], [2, 18, 10]]) == [True, True, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 2, 1], [1, 3], [2, 4, 2], [1, 5], [2, 6, 3], [1, 7], [2, 8, 4], [1, 9], [2, 10, 5], [1, 11], [2, 12, 6], [1, 13], [2, 14, 7], [1, 14], [2, 15, 8], [1, 16], [2, 17, 9], [1, 17], [2, 18, 10]]) == [True, True, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 3, 1], [2, 3, 2], [1, 4], [1, 5], [2, 6, 3], [2, 6, 5], [1, 7], [2, 8, 4]]) == [True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 3, 1], [2, 3, 2], [1, 4], [1, 5], [2, 6, 3], [2, 6, 5], [1, 7], [2, 8, 4]]) == [True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 10, 1], [2, 10, 2], [2, 10, 3], [2, 10, 4], [2, 10, 5], [2, 10, 6], [2, 10, 7], [2, 10, 8], [2, 10, 9], [2, 10, 10]]) == [True, False, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 10, 1], [2, 10, 2], [2, 10, 3], [2, 10, 4], [2, 10, 5], [2, 10, 6], [2, 10, 7], [2, 10, 8], [2, 10, 9], [2, 10, 10]]) == [True, False, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5], [2, 6, 6]]) == [True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5], [2, 6, 6]]) == [True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [2, 4, 1], [2, 4, 2], [1, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5]]) == [False, True, True, True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [2, 4, 1], [2, 4, 2], [1, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5]]) == [False, True, True, True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 11, 10], [2, 11, 9], [2, 11, 8], [2, 11, 7], [2, 11, 6], [2, 11, 5], [2, 11, 4], [2, 11, 3], [2, 11, 2], [2, 11, 1]]) == [False, False, False, False, False, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 11, 10], [2, 11, 9], [2, 11, 8], [2, 11, 7], [2, 11, 6], [2, 11, 5], [2, 11, 4], [2, 11, 3], [2, 11, 2], [2, 11, 1]]) == [False, False, False, False, False, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [2, 10, 4], [1, 15], [2, 15, 6], [1, 20], [2, 20, 8], [2, 20, 9]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [2, 10, 4], [1, 15], [2, 15, 6], [1, 20], [2, 20, 8], [2, 20, 9]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 10, 2], [2, 8, 2], [2, 6, 2], [2, 4, 2], [2, 2, 2]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 10, 2], [2, 8, 2], [2, 6, 2], [2, 4, 2], [2, 2, 2]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 1, 1], [1, 2], [2, 2, 2], [1, 3], [2, 3, 3], [1, 4], [2, 4, 4], [1, 5], [2, 5, 5], [1, 6], [2, 6, 6], [1, 7], [2, 7, 7], [1, 8], [2, 8, 8], [1, 9], [2, 9, 9], [1, 10], [2, 10, 10]]) == [True, False, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 1, 1], [1, 2], [2, 2, 2], [1, 3], [2, 3, 3], [1, 4], [2, 4, 4], [1, 5], [2, 5, 5], [1, 6], [2, 6, 6], [1, 7], [2, 7, 7], [1, 8], [2, 8, 8], [1, 9], [2, 9, 9], [1, 10], [2, 10, 10]]) == [True, False, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 20, 5], [1, 15], [2, 25, 10], [1, 20], [2, 30, 15], [1, 25], [2, 40, 20], [1, 30], [2, 50, 25]]) == [True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 20, 5], [1, 15], [2, 25, 10], [1, 20], [2, 30, 15], [1, 25], [2, 40, 20], [1, 30], [2, 50, 25]]) == [True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 20, 5], [2, 20, 15]]) == [False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 20, 5], [2, 20, 15]]) == [False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 10, 5]]) == [False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 10, 5]]) == [False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 20], [2, 20, 10], [1, 5], [2, 20, 15], [1, 15], [2, 20, 12], [2, 20, 18]]) == [True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 20], [2, 20, 10], [1, 5], [2, 20, 15], [1, 15], [2, 20, 12], [2, 20, 18]]) == [True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 4], [2, 10, 5], [2, 10, 6]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 4], [2, 10, 5], [2, 10, 6]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [2, 10, 3], [1, 6], [2, 10, 3], [2, 10, 4]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [2, 10, 3], [1, 6], [2, 10, 3], [2, 10, 4]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 3], [1, 6], [2, 6, 3], [2, 6, 4]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 3], [1, 6], [2, 6, 3], [2, 6, 4]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 3], [1, 6], [2, 10, 4], [1, 1], [2, 10, 9]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 3], [1, 6], [2, 10, 4], [1, 1], [2, 10, 9]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 5], [2, 10, 6]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 5], [2, 10, 6]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 12, 7], [1, 8], [2, 15, 9]]) == [False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 12, 7], [1, 8], [2, 15, 9]]) == [False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 3], [1, 6], [2, 8, 4], [1, 5], [2, 10, 3]]) == [False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 3], [1, 6], [2, 8, 4], [1, 5], [2, 10, 3]]) == [False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [2, 5, 4], [1, 15], [2, 15, 10], [2, 10, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [2, 5, 4], [1, 15], [2, 15, 10], [2, 10, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 3], [1, 6], [1, 9], [2, 12, 7], [2, 12, 5]]) == [False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 3], [1, 6], [1, 9], [2, 12, 7], [2, 12, 5]]) == [False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 3]]) == [False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 3]]) == [False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 2], [2, 4, 2]]) == [False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 2], [2, 4, 2]]) == [False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 3], [2, 5, 4]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 3], [2, 5, 4]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 15, 4], [2, 15, 6], [1, 8], [2, 15, 7]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 15, 4], [2, 15, 6], [1, 8], [2, 15, 7]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 10], [1, 5], [2, 10, 4], [1, 3], [2, 10, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 10], [1, 5], [2, 10, 4], [1, 3], [2, 10, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 3], [1, 5], [2, 10, 5], [1, 8], [2, 10, 2]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 3], [1, 5], [2, 10, 5], [1, 8], [2, 10, 2]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 4], [1, 3], [2, 4, 1], [1, 4], [2, 5, 2]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 4], [1, 3], [2, 4, 1], [1, 4], [2, 5, 2]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 10, 3], [2, 20, 8]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 10, 3], [2, 20, 8]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 5], [2, 5, 2], [1, 10], [2, 10, 5]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 5], [2, 5, 2], [1, 10], [2, 10, 5]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 2], [1, 3], [1, 7], [2, 9, 4]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 2], [1, 3], [1, 7], [2, 9, 4]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 2], [2, 3, 3]]) == [False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 2], [2, 3, 3]]) == [False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 15, 10], [1, 5], [2, 8, 3]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 15, 10], [1, 5], [2, 8, 3]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 15, 5], [2, 15, 10], [2, 15, 20]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 15, 5], [2, 15, 10], [2, 15, 20]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 3], [2, 10, 6]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 3], [2, 10, 6]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 4, 3], [2, 3, 1], [2, 5, 4]]) == [False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 4, 3], [2, 3, 1], [2, 5, 4]]) == [False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 9], [2, 10, 10], [2, 10, 11]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 9], [2, 10, 10], [2, 10, 11]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 1], [1, 3], [2, 5, 2], [1, 4], [2, 5, 2]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 1], [1, 3], [2, 5, 2], [1, 4], [2, 5, 2]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 2], [1, 2], [1, 3], [2, 5, 2], [2, 4, 2]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 2], [1, 2], [1, 3], [2, 5, 2], [2, 4, 2]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 15, 5], [2, 15, 10], [1, 5], [2, 15, 4]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 15, 5], [2, 15, 10], [1, 5], [2, 15, 4]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [2, 5, 4], [1, 3], [2, 3, 2], [2, 5, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [2, 5, 4], [1, 3], [2, 3, 2], [2, 5, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 4]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 4]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [2, 4, 2], [2, 6, 3]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [2, 4, 2], [2, 6, 3]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 5], [2, 5, 1]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 5], [2, 5, 1]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 2], [1, 7], [2, 10, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 2], [1, 7], [2, 10, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [1, 8], [2, 10, 7], [1, 6], [2, 10, 8]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [1, 8], [2, 10, 7], [1, 6], [2, 10, 8]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [2, 10, 10], [1, 5], [2, 10, 5], [2, 10, 1], [2, 10, 9]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [2, 10, 10], [1, 5], [2, 10, 5], [2, 10, 1], [2, 10, 9]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 3], [2, 6, 2], [2, 6, 4]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 3], [2, 6, 2], [2, 6, 4]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 8, 3], [1, 15], [2, 20, 5]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 8, 3], [1, 15], [2, 20, 5]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [1, 5], [2, 10, 4], [2, 10, 5], [1, 3], [2, 10, 2]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [1, 5], [2, 10, 4], [2, 10, 5], [1, 3], [2, 10, 2]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 2], [1, 3], [2, 4, 2], [1, 7], [2, 8, 6]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 2], [1, 3], [2, 4, 2], [1, 7], [2, 8, 6]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 20, 15], [2, 20, 20]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 20, 15], [2, 20, 20]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 5], [1, 10], [2, 10, 5]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 5], [1, 10], [2, 10, 5]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 3], [1, 5], [2, 5, 2], [1, 7], [2, 10, 4]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 3], [1, 5], [2, 5, 2], [1, 7], [2, 10, 4]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [1, 3], [2, 10, 2], [2, 5, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [1, 3], [2, 10, 2], [2, 5, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 3], [1, 2], [1, 4], [2, 5, 2], [1, 3], [2, 5, 1]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 3], [1, 2], [1, 4], [2, 5, 2], [1, 3], [2, 5, 1]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 8, 2], [2, 8, 3], [2, 8, 4]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 8, 2], [2, 8, 3], [2, 8, 4]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 3], [1, 5], [1, 7], [2, 8, 2]]) == [True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 3], [1, 5], [1, 7], [2, 8, 2]]) == [True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 10, 4], [2, 10, 5]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 10, 4], [2, 10, 5]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 10, 1], [1, 5], [2, 10, 4], [1, 10], [2, 10, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 10, 1], [1, 5], [2, 10, 4], [1, 10], [2, 10, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 15, 4], [2, 15, 6], [2, 15, 5]]) == [True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 15, 4], [2, 15, 6], [2, 15, 5]]) == [True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [1, 5], [2, 8, 2], [1, 3], [2, 6, 2]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [1, 5], [2, 8, 2], [1, 3], [2, 6, 2]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 3], [2, 10, 2], [1, 7], [2, 10, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 3], [2, 10, 2], [1, 7], [2, 10, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 2], [2, 3, 1]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 2], [2, 3, 1]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 4, 3], [2, 4, 2], [2, 4, 1]]) == [False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 4, 3], [2, 4, 2], [2, 4, 1]]) == [False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [2, 10, 5], [2, 10, 10], [1, 5], [2, 5, 2]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [2, 10, 5], [2, 10, 10], [1, 5], [2, 5, 2]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 15, 1], [1, 5], [2, 10, 5], [1, 10], [2, 15, 5]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 15, 1], [1, 5], [2, 10, 5], [1, 10], [2, 15, 5]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 3], [1, 5], [2, 10, 2]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 3], [1, 5], [2, 10, 2]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 8], [2, 8, 4], [1, 6], [2, 8, 3]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 8], [2, 8, 4], [1, 6], [2, 8, 3]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 5, 3], [2, 5, 1]]) == [False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 5, 3], [2, 5, 1]]) == [False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 3], [1, 3], [2, 5, 2]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 3], [1, 3], [2, 5, 2]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 7, 3], [1, 15], [2, 15, 6]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 7, 3], [1, 15], [2, 15, 6]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 3], [2, 5, 2], [1, 4], [2, 4, 2]]) == [False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 3], [2, 5, 2], [1, 4], [2, 4, 2]]) == [False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 3], [2, 4, 2], [2, 6, 3]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 3], [2, 4, 2], [2, 6, 3]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [1, 5], [1, 8], [2, 10, 3], [2, 10, 2], [2, 10, 1]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [1, 5], [1, 8], [2, 10, 3], [2, 10, 2], [2, 10, 1]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [2, 10, 3]]) == [False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [2, 10, 3]]) == [False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 4], [2, 6, 3], [1, 2], [2, 8, 6], [1, 6], [2, 10, 5]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 4], [2, 6, 3], [1, 2], [2, 8, 6], [1, 6], [2, 10, 5]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 9, 3], [1, 15], [2, 14, 5]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 9, 3], [1, 15], [2, 14, 5]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 5], [2, 10, 2]]) == [True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 5], [2, 10, 2]]) == [True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 6], [1, 5], [2, 10, 4]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 6], [1, 5], [2, 10, 4]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [1, 5], [2, 12, 4], [2, 8, 3]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [1, 5], [2, 12, 4], [2, 8, 3]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 1], [2, 3, 2]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 1], [2, 3, 2]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 4], [2, 10, 5]]) == [False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 4], [2, 10, 5]]) == [False, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 3], [1, 5], [1, 7], [2, 8, 2], [2, 8, 4], [2, 8, 6]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 3], [1, 5], [1, 7], [2, 8, 2], [2, 8, 4], [2, 8, 6]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 5], [2, 10, 4], [1, 8], [2, 10, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 5], [2, 10, 4], [1, 8], [2, 10, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 10], [1, 5], [2, 15, 5], [2, 10, 3], [1, 12], [2, 15, 4]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 10], [1, 5], [2, 15, 5], [2, 10, 3], [1, 12], [2, 15, 4]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 5, 4], [1, 3], [2, 3, 2], [1, 5], [2, 5, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 5, 4], [1, 3], [2, 3, 2], [1, 5], [2, 5, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 15, 6], [2, 15, 10], [2, 15, 11]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 15, 6], [2, 15, 10], [2, 15, 11]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 1, 1], [1, 1], [2, 1, 1]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 1, 1], [1, 1], [2, 1, 1]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[1, 5], [1, 10], [2, 8, 3], [2, 12, 5]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[1, 5], [1, 10], [2, 8, 3], [2, 12, 5]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(queries = [[2, 10, 5], [1, 3], [2, 10, 3], [1, 7], [2, 10, 4]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(queries = [[2, 10, 5], [1, 3], [2, 10, 3], [1, 7], [2, 10, 4]]) == [True, True, True]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(queries = [[2, 5, 2], [1, 3], [2, 5, 3], [1, 4], [2, 5, 1]]) == [True, True, True]
    assert candidate(queries = [[2, 10, 5], [1, 3], [2, 5, 2], [1, 10], [2, 10, 3]]) == [True, True, True]
    assert candidate(queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]) == [True, True, False]
    assert candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [2, 4, 1], [2, 4, 2]]) == [False, True, True]
    assert candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 12, 3]]) == [False, True]
    assert candidate(queries = [[2, 5, 1], [1, 3], [1, 4], [2, 5, 1]]) == [True, True]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 10, 5]]) == [False]
    assert candidate(queries = [[2, 5, 3], [1, 2], [2, 5, 2], [1, 4], [2, 5, 3]]) == [True, True, False]
    assert candidate(queries = [[1, 1], [1, 5], [1, 10], [2, 10, 3], [2, 10, 7]]) == [True, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 4, 2]]) == [False]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [2, 6, 2], [2, 6, 4]]) == [True, False]
    assert candidate(queries = [[1, 5], [1, 10], [2, 10, 4], [1, 15], [2, 15, 7]]) == [True, False]
    assert candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 5, 2], [2, 10, 8]]) == [True, True, False]
    assert candidate(queries = [[1, 10], [2, 10, 5], [1, 3], [2, 5, 2]]) == [True, True]
    assert candidate(queries = [[1, 10], [1, 5], [2, 10, 3], [2, 5, 2]]) == [True, True]
    assert candidate(queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]) == [False, True, True]
    assert candidate(queries = [[1, 1], [1, 5], [1, 10], [2, 12, 3], [2, 12, 7], [2, 12, 10]]) == [True, False, False]
    assert candidate(queries = [[1, 1], [2, 2, 1], [1, 3], [2, 4, 2], [1, 5], [2, 6, 3], [1, 7], [2, 8, 4], [1, 9], [2, 10, 5]]) == [True, True, False, False, False]
    assert candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [2, 10, 5], [2, 10, 4], [2, 10, 3], [2, 10, 2], [2, 10, 1], [1, 12], [2, 12, 6], [2, 12, 5], [2, 12, 4], [2, 12, 3], [2, 12, 2], [2, 12, 1]]) == [False, False, False, True, True, False, False, False, False, True, True]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 5], [2, 5, 4], [2, 5, 3], [2, 5, 2], [2, 5, 1]]) == [False, False, False, False, True]
    assert candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [2, 10, 9], [2, 10, 3], [2, 10, 5]]) == [False, False, False]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 9], [2, 10, 8], [2, 10, 7], [2, 10, 6], [2, 10, 5], [2, 10, 4], [2, 10, 3], [2, 10, 2], [2, 10, 1]]) == [False, False, False, False, False, False, False, True, True]
    assert candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [2, 10, 8], [2, 8, 4], [2, 6, 2]]) == [False, False, True]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 8], [2, 10, 4], [2, 10, 2]]) == [False, False, True]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 2], [2, 5, 3], [2, 5, 4], [2, 5, 5]]) == [False, False, False, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 1], [2, 5, 2], [2, 5, 3], [2, 5, 4], [2, 5, 5]]) == [True, False, False, False, False]
    assert candidate(queries = [[1, 1], [1, 10], [2, 5, 4], [2, 10, 8], [1, 15], [2, 20, 5], [2, 20, 10], [2, 20, 15], [2, 20, 20]]) == [True, True, True, False, False, False]
    assert candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [1, 12], [1, 14], [1, 16], [1, 18], [1, 20], [2, 21, 10], [2, 21, 20], [2, 21, 30], [2, 21, 40], [2, 21, 50]]) == [False, False, False, False, False]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [1, 11], [1, 13], [1, 15], [1, 17], [1, 19], [2, 20, 1], [2, 20, 2], [2, 20, 3], [2, 20, 4], [2, 20, 5], [2, 20, 6], [2, 20, 7], [2, 20, 8], [2, 20, 9], [2, 20, 10]]) == [True, True, False, False, False, False, False, False, False, False]
    assert candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 4], [2, 5, 3], [1, 6], [2, 7, 4], [1, 8], [2, 9, 5]]) == [True, True, True, False, False]
    assert candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [1, 4], [1, 5], [2, 5, 4], [2, 5, 1]]) == [False, False, True]
    assert candidate(queries = [[1, 10], [1, 9], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [1, 3], [1, 2], [1, 1], [2, 10, 5], [2, 9, 4], [2, 8, 3], [2, 7, 2], [2, 6, 1]]) == [False, False, False, False, True]
    assert candidate(queries = [[1, 2], [2, 3, 1], [1, 4], [2, 5, 2], [1, 6], [2, 7, 3], [1, 8], [2, 9, 4], [1, 10], [2, 11, 5], [1, 12], [2, 13, 6]]) == [True, True, False, False, False, False]
    assert candidate(queries = [[1, 5], [1, 10], [2, 12, 3], [1, 7], [2, 10, 6], [2, 8, 2]]) == [True, False, True]
    assert candidate(queries = [[1, 1], [1, 2], [2, 2, 1], [2, 2, 2], [1, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3], [1, 4], [2, 4, 1], [2, 4, 2], [2, 4, 3], [2, 4, 4]]) == [True, False, True, False, False, True, False, False, False]
    assert candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [1, 12], [1, 14], [2, 16, 12], [2, 16, 8], [2, 16, 4], [2, 16, 6], [2, 16, 10], [2, 16, 14]]) == [False, False, False, False, False, False]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 10, 2], [2, 10, 4], [2, 10, 6], [2, 10, 8], [2, 10, 10]]) == [True, False, False, False, False]
    assert candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 4], [1, 5], [2, 6, 3], [2, 7, 4], [2, 8, 5]]) == [True, True, True, False, False]
    assert candidate(queries = [[1, 1], [2, 2, 1], [1, 3], [2, 4, 2], [1, 5], [2, 6, 3], [1, 7], [2, 8, 4], [1, 9], [2, 10, 5], [1, 11], [2, 12, 6], [1, 13], [2, 14, 7], [1, 14], [2, 15, 8], [1, 16], [2, 17, 9], [1, 17], [2, 18, 10]]) == [True, True, False, False, False, False, False, False, False, False]
    assert candidate(queries = [[1, 1], [2, 3, 1], [2, 3, 2], [1, 4], [1, 5], [2, 6, 3], [2, 6, 5], [1, 7], [2, 8, 4]]) == [True, True, True, False, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 10, 1], [2, 10, 2], [2, 10, 3], [2, 10, 4], [2, 10, 5], [2, 10, 6], [2, 10, 7], [2, 10, 8], [2, 10, 9], [2, 10, 10]]) == [True, False, False, False, False, False, False, False, False, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5], [2, 6, 6]]) == [True, False, False, False, False, False]
    assert candidate(queries = [[1, 1], [2, 2, 2], [1, 3], [2, 4, 1], [2, 4, 2], [1, 5], [2, 6, 1], [2, 6, 2], [2, 6, 3], [2, 6, 4], [2, 6, 5]]) == [False, True, True, True, True, False, False, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 11, 10], [2, 11, 9], [2, 11, 8], [2, 11, 7], [2, 11, 6], [2, 11, 5], [2, 11, 4], [2, 11, 3], [2, 11, 2], [2, 11, 1]]) == [False, False, False, False, False, False, False, False, False, True]
    assert candidate(queries = [[1, 5], [2, 10, 4], [1, 15], [2, 15, 6], [1, 20], [2, 20, 8], [2, 20, 9]]) == [True, True, True, True]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 10, 2], [2, 8, 2], [2, 6, 2], [2, 4, 2], [2, 2, 2]]) == [True, True, True, True, False]
    assert candidate(queries = [[1, 1], [2, 1, 1], [1, 2], [2, 2, 2], [1, 3], [2, 3, 3], [1, 4], [2, 4, 4], [1, 5], [2, 5, 5], [1, 6], [2, 6, 6], [1, 7], [2, 7, 7], [1, 8], [2, 8, 8], [1, 9], [2, 9, 9], [1, 10], [2, 10, 10]]) == [True, False, False, False, False, False, False, False, False, False]
    assert candidate(queries = [[1, 10], [2, 20, 5], [1, 15], [2, 25, 10], [1, 20], [2, 30, 15], [1, 25], [2, 40, 20], [1, 30], [2, 50, 25]]) == [True, True, False, False, False]
    assert candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 20, 5], [2, 20, 15]]) == [False, True, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 10, 5]]) == [False]
    assert candidate(queries = [[1, 20], [2, 20, 10], [1, 5], [2, 20, 15], [1, 15], [2, 20, 12], [2, 20, 18]]) == [True, True, False, False]
    assert candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 4], [2, 10, 5], [2, 10, 6]]) == [True, True, True, False]
    assert candidate(queries = [[1, 5], [2, 10, 3], [1, 6], [2, 10, 3], [2, 10, 4]]) == [True, True, True]
    assert candidate(queries = [[1, 3], [1, 6], [2, 6, 3], [2, 6, 4]]) == [True, False]
    assert candidate(queries = [[1, 3], [1, 6], [2, 10, 4], [1, 1], [2, 10, 9]]) == [True, False]
    assert candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 5], [2, 10, 6]]) == [True, True, False]
    assert candidate(queries = [[1, 5], [1, 10], [2, 12, 7], [1, 8], [2, 15, 9]]) == [False, False]
    assert candidate(queries = [[1, 3], [1, 6], [2, 8, 4], [1, 5], [2, 10, 3]]) == [False, True]
    assert candidate(queries = [[1, 5], [2, 5, 4], [1, 15], [2, 15, 10], [2, 10, 3]]) == [True, True, True]
    assert candidate(queries = [[1, 3], [1, 6], [1, 9], [2, 12, 7], [2, 12, 5]]) == [False, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 3]]) == [False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 2], [2, 4, 2]]) == [False, False]
    assert candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 3], [2, 5, 4]]) == [True, True, True]
    assert candidate(queries = [[1, 5], [1, 10], [2, 15, 4], [2, 15, 6], [1, 8], [2, 15, 7]]) == [True, False, False]
    assert candidate(queries = [[2, 10, 10], [1, 5], [2, 10, 4], [1, 3], [2, 10, 3]]) == [True, True, True]
    assert candidate(queries = [[2, 10, 3], [1, 5], [2, 10, 5], [1, 8], [2, 10, 2]]) == [True, True, True]
    assert candidate(queries = [[2, 5, 4], [1, 3], [2, 4, 1], [1, 4], [2, 5, 2]]) == [True, True, True]
    assert candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 10, 3], [2, 20, 8]]) == [True, False]
    assert candidate(queries = [[2, 10, 5], [1, 5], [2, 5, 2], [1, 10], [2, 10, 5]]) == [True, True, True]
    assert candidate(queries = [[2, 5, 2], [1, 3], [1, 7], [2, 9, 4]]) == [True, True]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 2], [2, 3, 3]]) == [False, False]
    assert candidate(queries = [[1, 10], [2, 15, 10], [1, 5], [2, 8, 3]]) == [True, True]
    assert candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 15, 5], [2, 15, 10], [2, 15, 20]]) == [True, False, False]
    assert candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 3], [2, 10, 6]]) == [True, True, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 4, 3], [2, 3, 1], [2, 5, 4]]) == [False, True, False]
    assert candidate(queries = [[1, 10], [2, 10, 9], [2, 10, 10], [2, 10, 11]]) == [True, True, False]
    assert candidate(queries = [[2, 5, 1], [1, 3], [2, 5, 2], [1, 4], [2, 5, 2]]) == [True, True, True]
    assert candidate(queries = [[2, 5, 2], [1, 2], [1, 3], [2, 5, 2], [2, 4, 2]]) == [True, True, True]
    assert candidate(queries = [[1, 10], [2, 15, 5], [2, 15, 10], [1, 5], [2, 15, 4]]) == [True, True, True]
    assert candidate(queries = [[1, 5], [2, 5, 4], [1, 3], [2, 3, 2], [2, 5, 3]]) == [True, True, True]
    assert candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 4]]) == [True, True]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [2, 4, 2], [2, 6, 3]]) == [True, False]
    assert candidate(queries = [[1, 10], [2, 10, 5], [1, 5], [2, 10, 5], [2, 5, 1]]) == [True, True, True]
    assert candidate(queries = [[2, 10, 1], [1, 5], [2, 10, 2], [1, 7], [2, 10, 3]]) == [True, True, True]
    assert candidate(queries = [[1, 10], [2, 10, 5], [1, 8], [2, 10, 7], [1, 6], [2, 10, 8]]) == [True, True, False]
    assert candidate(queries = [[1, 10], [2, 10, 5], [2, 10, 10], [1, 5], [2, 10, 5], [2, 10, 1], [2, 10, 9]]) == [True, True, True, True, False]
    assert candidate(queries = [[1, 5], [1, 3], [2, 6, 2], [2, 6, 4]]) == [True, False]
    assert candidate(queries = [[1, 5], [1, 10], [2, 8, 3], [1, 15], [2, 20, 5]]) == [True, True]
    assert candidate(queries = [[1, 10], [1, 5], [2, 10, 4], [2, 10, 5], [1, 3], [2, 10, 2]]) == [True, True, True]
    assert candidate(queries = [[2, 5, 2], [1, 3], [2, 4, 2], [1, 7], [2, 8, 6]]) == [True, True, False]
    assert candidate(queries = [[1, 5], [1, 10], [1, 15], [2, 20, 10], [2, 20, 15], [2, 20, 20]]) == [False, False, False]
    assert candidate(queries = [[2, 10, 5], [1, 5], [1, 10], [2, 10, 5]]) == [True, True]
    assert candidate(queries = [[1, 3], [1, 5], [2, 5, 2], [1, 7], [2, 10, 4]]) == [True, False]
    assert candidate(queries = [[1, 10], [2, 10, 5], [1, 3], [2, 10, 2], [2, 5, 3]]) == [True, True, True]
    assert candidate(queries = [[2, 5, 3], [1, 2], [1, 4], [2, 5, 2], [1, 3], [2, 5, 1]]) == [True, True, True]
    assert candidate(queries = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 8, 2], [2, 8, 3], [2, 8, 4]]) == [True, False, False]
    assert candidate(queries = [[1, 3], [1, 5], [1, 7], [2, 8, 2]]) == [True]
    assert candidate(queries = [[1, 5], [1, 10], [2, 10, 4], [2, 10, 5]]) == [True, True]
    assert candidate(queries = [[1, 1], [2, 10, 1], [1, 5], [2, 10, 4], [1, 10], [2, 10, 3]]) == [True, True, True]
    assert candidate(queries = [[1, 5], [1, 10], [2, 15, 4], [2, 15, 6], [2, 15, 5]]) == [True, False, True]
    assert candidate(queries = [[1, 10], [1, 5], [2, 8, 2], [1, 3], [2, 6, 2]]) == [True, True]
    assert candidate(queries = [[2, 10, 5], [1, 3], [2, 10, 2], [1, 7], [2, 10, 3]]) == [True, True, True]
    assert candidate(queries = [[1, 1], [2, 2, 1], [2, 3, 2], [1, 2], [2, 3, 1]]) == [True, True, True]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 4, 3], [2, 4, 2], [2, 4, 1]]) == [False, False, True]
    assert candidate(queries = [[1, 10], [2, 10, 5], [2, 10, 10], [1, 5], [2, 5, 2]]) == [True, True, True]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]) == [True, False, False]
    assert candidate(queries = [[2, 15, 1], [1, 5], [2, 10, 5], [1, 10], [2, 15, 5]]) == [True, True, True]
    assert candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 3], [1, 5], [2, 10, 2]]) == [True, True, True]
    assert candidate(queries = [[1, 5], [1, 8], [2, 8, 4], [1, 6], [2, 8, 3]]) == [True, True]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 5, 3], [2, 5, 1]]) == [False, True]
    assert candidate(queries = [[2, 5, 3], [1, 3], [2, 5, 2]]) == [True, True]
    assert candidate(queries = [[1, 5], [1, 10], [2, 7, 3], [1, 15], [2, 15, 6]]) == [True, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 3], [2, 5, 2], [1, 4], [2, 4, 2]]) == [False, True, False]
    assert candidate(queries = [[1, 5], [1, 3], [2, 4, 2], [2, 6, 3]]) == [True, True]
    assert candidate(queries = [[1, 2], [1, 5], [1, 8], [2, 10, 3], [2, 10, 2], [2, 10, 1]]) == [True, True, True]
    assert candidate(queries = [[1, 2], [1, 4], [1, 6], [1, 8], [2, 10, 3]]) == [False]
    assert candidate(queries = [[1, 4], [2, 6, 3], [1, 2], [2, 8, 6], [1, 6], [2, 10, 5]]) == [True, False, False]
    assert candidate(queries = [[1, 5], [1, 10], [2, 9, 3], [1, 15], [2, 14, 5]]) == [True, True]
    assert candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 5], [2, 10, 2]]) == [True, False, True]
    assert candidate(queries = [[2, 10, 5], [1, 3], [1, 7], [2, 10, 6], [1, 5], [2, 10, 4]]) == [True, False, False]
    assert candidate(queries = [[1, 10], [1, 5], [2, 12, 4], [2, 8, 3]]) == [True, True]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [2, 3, 1], [2, 3, 2]]) == [True, False]
    assert candidate(queries = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 5, 4], [2, 10, 5]]) == [False, True]
    assert candidate(queries = [[1, 3], [1, 5], [1, 7], [2, 8, 2], [2, 8, 4], [2, 8, 6]]) == [True, False, False]
    assert candidate(queries = [[2, 10, 5], [1, 5], [2, 10, 4], [1, 8], [2, 10, 3]]) == [True, True, True]
    assert candidate(queries = [[1, 10], [1, 5], [2, 15, 5], [2, 10, 3], [1, 12], [2, 15, 4]]) == [True, True, True]
    assert candidate(queries = [[2, 5, 4], [1, 3], [2, 3, 2], [1, 5], [2, 5, 3]]) == [True, True, True]
    assert candidate(queries = [[1, 5], [1, 10], [2, 15, 6], [2, 15, 10], [2, 15, 11]]) == [False, False, False]
    assert candidate(queries = [[2, 1, 1], [1, 1], [2, 1, 1]]) == [True, True]
    assert candidate(queries = [[1, 5], [1, 10], [2, 8, 3], [2, 12, 5]]) == [True, True]
    assert candidate(queries = [[2, 10, 5], [1, 3], [2, 10, 3], [1, 7], [2, 10, 4]]) == [True, True, True]


