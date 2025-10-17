def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4], [0, 0, 0, 0], [5, 6, 7, 8], [9, 10, 11, 12]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4], [0, 0, 0, 0], [5, 6, 7, 8], [9, 10, 11, 12]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[3, 0, 0], [1, 0, 0], [2, 0, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[3, 0, 0], [1, 0, 0], [2, 0, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 0], [0, 0, 0], [2, 0, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 0], [0, 0, 0], [2, 0, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0], [0, 0, 0], [0, 0, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0], [0, 0, 0], [0, 0, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1], [1, 0, 1], [1, 1, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1], [1, 0, 1], [1, 1, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[4, 2, 3], [0, 0, 5], [8, 7, 6]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[4, 2, 3], [0, 0, 5], [8, 7, 6]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2], [3, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2], [3, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 2]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 2]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 2, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 2, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1], [2, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1], [2, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5], [0, 6, 0, 0, 7], [8, 0, 0, 0, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5], [0, 6, 0, 0, 7], [8, 0, 0, 0, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8, 9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8, 9, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 0, 0, 3], [0, 0, 0, 0, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 0], [5, 6, 0, 7, 8]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 0, 0, 3], [0, 0, 0, 0, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 0], [5, 6, 0, 7, 8]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 2, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 2, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10], [0, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10], [0, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[10, 1, 3, 0, 5], [9, 0, 0, 0, 4], [8, 6, 7, 0, 2], [0, 0, 0, 0, 0], [1, 0, 0, 0, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[10, 1, 3, 0, 5], [9, 0, 0, 0, 4], [8, 6, 7, 0, 2], [0, 0, 0, 0, 0], [1, 0, 0, 0, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 3, 0, 0, 5], [0, 6, 7, 8, 0], [0, 0, 0, 0, 0], [9, 10, 11, 12, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 3, 0, 0, 5], [0, 6, 7, 8, 0], [0, 0, 0, 0, 0], [9, 10, 11, 12, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 2, 3, 0, 1], [1, 0, 4, 5, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 6, 7, 8, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 2, 3, 0, 1], [1, 0, 4, 5, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 6, 7, 8, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [17, 18, 19, 20, 21, 22, 23, 24]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [17, 18, 19, 20, 21, 22, 23, 24]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 3, 0, 4], [0, 0, 5, 0, 6, 7], [8, 9, 0, 0, 0, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 3, 0, 4], [0, 0, 5, 0, 6, 7], [8, 9, 0, 0, 0, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 3, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 3, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 0, 4, 5], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10], [0, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 0, 4, 5], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10], [0, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 3, 0, 5], [2, 0, 0, 0], [6, 7, 8, 0], [0, 9, 10, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 3, 0, 5], [2, 0, 0, 0], [6, 7, 8, 0], [0, 9, 10, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1], [0, 2, 0, 3, 0], [1, 0, 4, 0, 5], [0, 6, 0, 7, 0], [1, 0, 0, 0, 8]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1], [0, 2, 0, 3, 0], [1, 0, 4, 0, 5], [0, 6, 0, 7, 0], [1, 0, 0, 0, 8]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [3, 4, 0, 0, 5, 0], [0, 0, 0, 0, 0, 0], [6, 7, 0, 0, 8, 0], [0, 0, 9, 10, 0, 11]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [3, 4, 0, 0, 5, 0], [0, 0, 0, 0, 0, 0], [6, 7, 0, 0, 8, 0], [0, 0, 9, 10, 0, 11]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[3, 0, 1], [0, 0, 0], [2, 0, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[3, 0, 1], [0, 0, 0], [2, 0, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 0, 0], [0, 0, 0, 0, 0], [14, 15, 16, 17, 18]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 0, 0], [0, 0, 0, 0, 0], [14, 15, 16, 17, 18]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 0, 0, 0, 0, 0], [14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 0, 0, 0, 0, 0], [14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 0, 3, 0, 1], [4, 0, 0, 0, 0], [6, 0, 7, 0, 0], [0, 0, 0, 0, 0], [8, 0, 9, 0, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 0, 3, 0, 1], [4, 0, 0, 0, 0], [6, 0, 7, 0, 0], [0, 0, 0, 0, 0], [8, 0, 9, 0, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 0, 0, 3], [1, 0, 0, 0], [0, 2, 0, 0], [4, 0, 0, 6]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 0, 0, 3], [1, 0, 0, 0], [0, 2, 0, 0], [4, 0, 0, 6]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[10, 11, 12, 13], [0, 0, 0, 0], [9, 8, 7, 6], [5, 4, 3, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[10, 11, 12, 13], [0, 0, 0, 0], [9, 8, 7, 6], [5, 4, 3, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[3, 0, 1, 4, 5], [0, 0, 0, 0, 0], [1, 0, 2, 0, 0], [0, 0, 0, 0, 0], [7, 6, 0, 8, 9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[3, 0, 1, 4, 5], [0, 0, 0, 0, 0], [1, 0, 2, 0, 0], [0, 0, 0, 0, 0], [7, 6, 0, 8, 9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 0, 0, 3], [0, 0, 0, 0, 0], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13], [14, 15, 16, 17, 18]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 0, 0, 3], [0, 0, 0, 0, 0], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13], [14, 15, 16, 17, 18]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0], [0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0], [0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 0, 0, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 0, 0, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[10, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[10, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[2, 1, 3, 4, 5], [0, 0, 0, 0, 0], [10, 9, 8, 7, 6], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[2, 1, 3, 4, 5], [0, 0, 0, 0, 0], [10, 9, 8, 7, 6], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 0, 0], [0, 3, 0, 4], [5, 6, 7, 8], [9, 0, 0, 10]]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 0, 0], [0, 3, 0, 4], [5, 6, 7, 8], [9, 0, 0, 10]]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 0, 0, 0], [0, 0, 0, 0, 0, 0], [16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 0, 0, 0], [0, 0, 0, 0, 0, 0], [16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 0, 4, 5], [0, 0, 0, 0, 0], [6, 7, 0, 8, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 0, 4, 5], [0, 0, 0, 0, 0], [6, 7, 0, 8, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8, 9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8, 9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 0, 0, 0], [0, 2, 0, 3, 0], [0, 0, 4, 0, 0], [0, 5, 0, 6, 0], [0, 0, 0, 7, 8]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 0, 0, 0], [0, 2, 0, 3, 0], [0, 0, 4, 0, 0], [0, 5, 0, 6, 0], [0, 0, 0, 7, 8]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 3]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 3]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [23, 24, 25, 26, 27, 28, 29, 30, 31]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [23, 24, 25, 26, 27, 28, 29, 30, 31]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 32, 33, 34, 35, 36]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 32, 33, 34, 35, 36]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[2, 3, 0, 4, 5], [0, 0, 0, 0, 0], [1, 6, 7, 8, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[2, 3, 0, 4, 5], [0, 0, 0, 0, 0], [1, 6, 7, 8, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 0, 4], [1, 0, 0, 0], [3, 6, 7, 8], [0, 0, 0, 9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 0, 4], [1, 0, 0, 0], [3, 6, 7, 8], [0, 0, 0, 9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 9]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 9]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6], [7, 0, 0, 0, 0, 0], [0, 8, 9, 10, 0, 0], [0, 0, 0, 0, 0, 0], [11, 12, 13, 0, 0, 0], [0, 0, 14, 15, 16, 17]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6], [7, 0, 0, 0, 0, 0], [0, 8, 9, 10, 0, 0], [0, 0, 0, 0, 0, 0], [11, 12, 13, 0, 0, 0], [0, 0, 14, 15, 16, 17]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 0, 0, 3, 4], [5, 0, 0, 0, 0, 6], [7, 8, 0, 0, 0, 9], [0, 0, 10, 11, 0, 0], [12, 13, 0, 0, 14, 15], [16, 17, 18, 19, 0, 20]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 0, 0, 3, 4], [5, 0, 0, 0, 0, 6], [7, 8, 0, 0, 0, 9], [0, 0, 10, 11, 0, 0], [12, 13, 0, 0, 14, 15], [16, 17, 18, 19, 0, 20]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [10, 9, 8, 7, 6], [15, 0, 0, 0, 11], [14, 13, 12, 0, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [10, 9, 8, 7, 6], [15, 0, 0, 0, 11], [14, 13, 12, 0, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 1, 3, 2, 4], [0, 0, 0, 0, 0], [8, 6, 7, 9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 1, 3, 2, 4], [0, 0, 0, 0, 0], [8, 6, 7, 9, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 1, 2, 3, 4], [0, 9, 10, 11, 0], [8, 7, 6, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 1, 2, 3, 4], [0, 9, 10, 11, 0], [8, 7, 6, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [1, 0, 0, 0, 0], [2, 0, 0, 0, 3], [4, 0, 0, 0, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [1, 0, 0, 0, 0], [2, 0, 0, 0, 3], [4, 0, 0, 0, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[3, 2, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 4, 5, 6], [0, 0, 7, 8, 9], [10, 11, 12, 13, 14]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[3, 2, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 4, 5, 6], [0, 0, 7, 8, 9], [10, 11, 12, 13, 14]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[10, 1, 3, 12, 11], [0, 0, 0, 0, 0], [5, 4, 0, 0, 6], [0, 0, 0, 0, 0], [8, 9, 7, 13, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[10, 1, 3, 12, 11], [0, 0, 0, 0, 0], [5, 4, 0, 0, 6], [0, 0, 0, 0, 0], [8, 9, 7, 13, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[2, 1, 0, 0, 5], [0, 0, 3, 0, 0], [0, 6, 0, 4, 0], [7, 0, 0, 0, 8]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[2, 1, 0, 0, 5], [0, 0, 3, 0, 0], [0, 6, 0, 4, 0], [7, 0, 0, 0, 8]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[5, 1, 0, 0, 8], [0, 0, 0, 0, 0], [0, 2, 0, 3, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 6], [0, 0, 0, 7, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[5, 1, 0, 0, 8], [0, 0, 0, 0, 0], [0, 2, 0, 3, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 6], [0, 0, 0, 7, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 2, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 2, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 3, 1, 0, 5], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 3, 1, 0, 5], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 0, 4, 5, 6, 0, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 0, 4, 5, 6, 0, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[2, 3, 0, 4], [1, 0, 0, 5], [8, 7, 6, 0], [0, 9, 10, 11]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[2, 3, 0, 4], [1, 0, 0, 5], [8, 7, 6, 0], [0, 9, 10, 11]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 2, 3, 0, 0], [0, 0, 0, 0, 0], [4, 5, 6, 0, 0], [0, 0, 0, 0, 0], [7, 8, 9, 10, 11]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 2, 3, 0, 0], [0, 0, 0, 0, 0], [4, 5, 6, 0, 0], [0, 0, 0, 0, 0], [7, 8, 9, 10, 11]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(forest = [[1, 10, 3, 4, 5], [0, 9, 0, 0, 0], [6, 8, 7, 0, 1], [2, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(forest = [[1, 10, 3, 4, 5], [0, 9, 0, 0, 0], [6, 8, 7, 0, 1], [2, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == 32: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(forest = [[1, 2, 3, 4], [0, 0, 0, 0], [5, 6, 7, 8], [9, 10, 11, 12]]) == -1
    assert candidate(forest = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]) == 0
    assert candidate(forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]) == 6
    assert candidate(forest = [[3, 0, 0], [1, 0, 0], [2, 0, 0]]) == 4
    assert candidate(forest = [[1, 1, 0], [0, 0, 0], [2, 0, 0]]) == -1
    assert candidate(forest = [[1, 0, 0], [0, 0, 0], [0, 0, 2]]) == -1
    assert candidate(forest = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]) == 6
    assert candidate(forest = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]) == -1
    assert candidate(forest = [[1, 1, 1], [1, 0, 1], [1, 1, 2]]) == 4
    assert candidate(forest = [[4, 2, 3], [0, 0, 5], [8, 7, 6]]) == 10
    assert candidate(forest = [[1, 2], [3, 4]]) == 4
    assert candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0]]) == 0
    assert candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 2]]) == 7
    assert candidate(forest = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 2, 1]]) == 5
    assert candidate(forest = [[1, 1], [2, 0]]) == 1
    assert candidate(forest = [[1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 9]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5], [0, 6, 0, 0, 7], [8, 0, 0, 0, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8, 9, 10]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]]) == -1
    assert candidate(forest = [[1, 2, 0, 0, 3], [0, 0, 0, 0, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 0], [5, 6, 0, 7, 8]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 2, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]) == 4
    assert candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10], [0, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == -1
    assert candidate(forest = [[10, 1, 3, 0, 5], [9, 0, 0, 0, 4], [8, 6, 7, 0, 2], [0, 0, 0, 0, 0], [1, 0, 0, 0, 3]]) == -1
    assert candidate(forest = [[1, 3, 0, 0, 5], [0, 6, 7, 8, 0], [0, 0, 0, 0, 0], [9, 10, 11, 12, 4]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]]) == -1
    assert candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 2, 3, 0, 1], [1, 0, 4, 5, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 6, 7, 8, 1]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [17, 18, 19, 20, 21, 22, 23, 24]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 40
    assert candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 3, 0, 4], [0, 0, 5, 0, 6, 7], [8, 9, 0, 0, 0, 0]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 3, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 4]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[1, 2, 0, 4, 5], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10], [0, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[1, 3, 0, 5], [2, 0, 0, 0], [6, 7, 8, 0], [0, 9, 10, 4]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1], [0, 2, 0, 3, 0], [1, 0, 4, 0, 5], [0, 6, 0, 7, 0], [1, 0, 0, 0, 8]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [3, 4, 0, 0, 5, 0], [0, 0, 0, 0, 0, 0], [6, 7, 0, 0, 8, 0], [0, 0, 9, 10, 0, 11]]) == -1
    assert candidate(forest = [[3, 0, 1], [0, 0, 0], [2, 0, 5]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 0, 0], [0, 0, 0, 0, 0], [14, 15, 16, 17, 18]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [7, 8, 9, 10, 11, 12], [13, 0, 0, 0, 0, 0], [14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25]]) == -1
    assert candidate(forest = [[1, 2, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 5]]) == -1
    assert candidate(forest = [[5, 0, 3, 0, 1], [4, 0, 0, 0, 0], [6, 0, 7, 0, 0], [0, 0, 0, 0, 0], [8, 0, 9, 0, 2]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[5, 0, 0, 3], [1, 0, 0, 0], [0, 2, 0, 0], [4, 0, 0, 6]]) == -1
    assert candidate(forest = [[10, 11, 12, 13], [0, 0, 0, 0], [9, 8, 7, 6], [5, 4, 3, 2]]) == -1
    assert candidate(forest = [[3, 0, 1, 4, 5], [0, 0, 0, 0, 0], [1, 0, 2, 0, 0], [0, 0, 0, 0, 0], [7, 6, 0, 8, 9]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]) == 5
    assert candidate(forest = [[1, 2, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]) == -1
    assert candidate(forest = [[1, 2, 0, 0, 3], [0, 0, 0, 0, 0], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13], [14, 15, 16, 17, 18]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0], [0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15]]) == -1
    assert candidate(forest = [[1, 2, 3, 0, 0, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[10, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == -1
    assert candidate(forest = [[2, 1, 3, 4, 5], [0, 0, 0, 0, 0], [10, 9, 8, 7, 6], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == -1
    assert candidate(forest = [[1, 2, 0, 0], [0, 3, 0, 4], [5, 6, 7, 8], [9, 0, 0, 10]]) == 22
    assert candidate(forest = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]) == 14
    assert candidate(forest = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 0, 0, 0], [0, 0, 0, 0, 0, 0], [16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27]]) == -1
    assert candidate(forest = [[1, 2, 0, 4, 5], [0, 0, 0, 0, 0], [6, 7, 0, 8, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 2]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 3]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [2, 3, 4, 5, 6, 7, 8, 9]]) == -1
    assert candidate(forest = [[1, 1, 0, 0, 0], [0, 2, 0, 3, 0], [0, 0, 4, 0, 0], [0, 5, 0, 6, 0], [0, 0, 0, 7, 8]]) == -1
    assert candidate(forest = [[1, 2, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 3]]) == 14
    assert candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [23, 24, 25, 26, 27, 28, 29, 30, 31]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 32, 33, 34, 35, 36]]) == -1
    assert candidate(forest = [[2, 3, 0, 4, 5], [0, 0, 0, 0, 0], [1, 6, 7, 8, 9], [0, 0, 0, 0, 0], [10, 11, 12, 13, 14]]) == -1
    assert candidate(forest = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 9]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]) == -1
    assert candidate(forest = [[1, 2, 0, 4], [1, 0, 0, 0], [3, 6, 7, 8], [0, 0, 0, 9]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 9]]) == 8
    assert candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[1, 2, 3, 4, 5, 6], [7, 0, 0, 0, 0, 0], [0, 8, 9, 10, 0, 0], [0, 0, 0, 0, 0, 0], [11, 12, 13, 0, 0, 0], [0, 0, 14, 15, 16, 17]]) == -1
    assert candidate(forest = [[1, 2, 0, 0, 3, 4], [5, 0, 0, 0, 0, 6], [7, 8, 0, 0, 0, 9], [0, 0, 10, 11, 0, 0], [12, 13, 0, 0, 14, 15], [16, 17, 18, 19, 0, 20]]) == -1
    assert candidate(forest = [[5, 4, 3, 2, 1], [0, 0, 0, 0, 0], [10, 9, 8, 7, 6], [15, 0, 0, 0, 11], [14, 13, 12, 0, 0]]) == -1
    assert candidate(forest = [[5, 1, 3, 2, 4], [0, 0, 0, 0, 0], [8, 6, 7, 9, 10]]) == -1
    assert candidate(forest = [[5, 1, 2, 3, 4], [0, 9, 10, 11, 0], [8, 7, 6, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 18
    assert candidate(forest = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [6, 7, 8, 9, 10]]) == -1
    assert candidate(forest = [[5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [1, 0, 0, 0, 0], [2, 0, 0, 0, 3], [4, 0, 0, 0, 5]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(forest = [[3, 2, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 4, 5, 6], [0, 0, 7, 8, 9], [10, 11, 12, 13, 14]]) == -1
    assert candidate(forest = [[10, 1, 3, 12, 11], [0, 0, 0, 0, 0], [5, 4, 0, 0, 6], [0, 0, 0, 0, 0], [8, 9, 7, 13, 2]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24]]) == -1
    assert candidate(forest = [[2, 1, 0, 0, 5], [0, 0, 3, 0, 0], [0, 6, 0, 4, 0], [7, 0, 0, 0, 8]]) == -1
    assert candidate(forest = [[5, 1, 0, 0, 8], [0, 0, 0, 0, 0], [0, 2, 0, 3, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 6], [0, 0, 0, 7, 0]]) == -1
    assert candidate(forest = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 2, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == -1
    assert candidate(forest = [[1, 3, 1, 0, 5], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1]]) == -1
    assert candidate(forest = [[1, 2, 3, 0, 4, 5, 6, 0, 7, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]]) == -1
    assert candidate(forest = [[2, 3, 0, 4], [1, 0, 0, 5], [8, 7, 6, 0], [0, 9, 10, 11]]) == -1
    assert candidate(forest = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]]) == -1
    assert candidate(forest = [[1, 2, 3, 0, 0], [0, 0, 0, 0, 0], [4, 5, 6, 0, 0], [0, 0, 0, 0, 0], [7, 8, 9, 10, 11]]) == -1
    assert candidate(forest = [[1, 10, 3, 4, 5], [0, 9, 0, 0, 0], [6, 8, 7, 0, 1], [2, 0, 0, 0, 0], [11, 12, 13, 14, 15]]) == 32


