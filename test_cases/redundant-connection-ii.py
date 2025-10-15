def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(edges = [[3, 1], [4, 1], [5, 2], [3, 2], [3, 5]]) == [3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[3, 1], [4, 1], [5, 2], [3, 2], [3, 5]]) == [3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 1]]) == [3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 1]]) == [3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[3, 1], [4, 1], [5, 2], [3, 5], [4, 2]]) == [4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[3, 1], [4, 1], [5, 2], [3, 5], [4, 2]]) == [4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 1], [4, 3]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 1], [4, 3]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[2, 1], [3, 1], [1, 4], [4, 3]]) == [3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[2, 1], [3, 1], [1, 4], [4, 3]]) == [3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 3]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 3]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 2], [1, 5], [5, 2]]) == [4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 2], [1, 5], [5, 2]]) == [4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 1], [1, 4]]) == [3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 1], [1, 4]]) == [3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 2]]) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 2]]) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[2, 1], [3, 1], [4, 2], [1, 4]]) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[2, 1], [3, 1], [4, 2], [1, 4]]) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19], [15, 20], [16, 21], [17, 22], [18, 23], [19, 24], [20, 25], [21, 26], [22, 27], [23, 28], [24, 29], [25, 30], [30, 1]]) == [30, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19], [15, 20], [16, 21], [17, 22], [18, 23], [19, 24], [20, 25], [21, 26], [22, 27], [23, 28], [24, 29], [25, 30], [30, 1]]) == [30, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 3]]) == [12, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 3]]) == [12, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 4]]) == [12, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 4]]) == [12, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 8]]) == [14, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 8]]) == [14, 8]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1]]) == [15, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1]]) == [15, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[3, 1], [4, 1], [5, 1], [3, 2], [3, 4], [3, 5]]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[3, 1], [4, 1], [5, 1], [3, 2], [3, 4], [3, 5]]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]) == [5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]) == [5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 5], [3, 6]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 5], [3, 6]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[10, 1], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[10, 1], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [3, 6]]) == [5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [3, 6]]) == [5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[5, 1], [1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[5, 1], [1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 4]]) == [10, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 4]]) == [10, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4], [7, 1]]) == [6, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4], [7, 1]]) == [6, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [3, 6], [6, 7]]) == [5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [3, 6], [6, 7]]) == [5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == [10, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == [10, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [2, 4]]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [2, 4]]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 6]]) == [11, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 6]]) == [11, 6]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 1]]) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 1]]) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 11]]) == [1, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 11]]) == [1, 11]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6]]) == [5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6]]) == [5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3]]) == [5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3]]) == [5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 10]]) == [25, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 10]]) == [25, 10]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[5, 2], [1, 5], [4, 1], [3, 5], [4, 3]]) == [3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[5, 2], [1, 5], [4, 1], [3, 5], [4, 3]]) == [3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == [9, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == [9, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 3]]) == [9, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 3]]) == [9, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5], [1, 5]]) == [10, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5], [1, 5]]) == [10, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 1], [12, 2]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 1], [12, 2]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 5], [1, 9]]) == [8, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 5], [1, 9]]) == [8, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 5]]) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 5]]) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 5], [5, 4], [4, 2], [1, 4]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 5], [5, 4], [4, 2], [1, 4]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 2]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 2]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 8], [8, 9], [9, 10], [10, 7]]) == [6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 8], [8, 9], [9, 10], [10, 7]]) == [6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 1]]) == [11, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 1]]) == [11, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19], [15, 20], [16, 21], [17, 22], [18, 23], [19, 24], [20, 25], [21, 26], [22, 27], [23, 28], [24, 29], [25, 30], [30, 15]]) == [30, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19], [15, 20], [16, 21], [17, 22], [18, 23], [19, 24], [20, 25], [21, 26], [22, 27], [23, 28], [24, 29], [25, 30], [30, 15]]) == [30, 15]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 3]]) == [11, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 3]]) == [11, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3], [2, 4]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3], [2, 4]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[5, 3], [1, 5], [2, 3], [4, 1], [5, 2], [4, 5]]) == [5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[5, 3], [1, 5], [2, 3], [4, 1], [5, 2], [4, 5]]) == [5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 5]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 5]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == [6, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == [6, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 2]]) == [10, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 2]]) == [10, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 7]]) == [13, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 7]]) == [13, 7]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6], [6, 7]]) == [5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6], [6, 7]]) == [5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 4]]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 4]]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [6, 8], [7, 8], [8, 2]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [6, 8], [7, 8], [8, 2]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3]]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3]]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 5]]) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 5]]) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 15]]) == [30, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 15]]) == [30, 15]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 6]]) == [9, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 6]]) == [9, 6]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 5]]) == [12, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 5]]) == [12, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 1]]) == [30, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 1]]) == [30, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 2]]) == [5, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 2]]) == [5, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 1], [20, 2]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 1], [20, 2]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4]]) == [6, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4]]) == [6, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 10], [3, 10], [5, 10]]) == [10, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 10], [3, 10], [5, 10]]) == [10, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 5]]) == [20, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 5]]) == [20, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 2]]) == [9, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 2]]) == [9, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [1, 13]]) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [1, 13]]) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5]]) == [10, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5]]) == [10, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 3]]) == [10, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 3]]) == [10, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [5, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [5, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4], [1, 9], [9, 10], [10, 1]]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4], [1, 9], [9, 10], [10, 1]]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 3], [3, 5]]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 3], [3, 5]]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [4, 2]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [4, 2]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [9, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [9, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 4]]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 4]]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[2, 3], [4, 3], [5, 3], [1, 4], [2, 5], [4, 5]]) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[2, 3], [4, 3], [5, 3], [1, 4], [2, 5], [4, 5]]) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 9]]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 9]]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 10], [5, 10]]) == [10, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 10], [5, 10]]) == [10, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 1], [6, 1]]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 1], [6, 1]]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5], [1, 10]]) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5], [1, 10]]) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 7]]) == [14, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 7]]) == [14, 7]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 6], [4, 6], [5, 6], [2, 3]]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 6], [4, 6], [5, 6], [2, 3]]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 13]]) == [20, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 13]]) == [20, 13]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4]]) == [8, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4]]) == [8, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 7]]) == [9, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 7]]) == [9, 7]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 2]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 2]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 4]]) == [9, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 4]]) == [9, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 1]]) == [5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 1]]) == [5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [6, 4]]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [6, 4]]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [9, 5]]) == [9, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [9, 5]]) == [9, 5]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(edges = [[3, 1], [4, 1], [5, 2], [3, 2], [3, 5]]) == [3, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 1]]) == [3, 1]
    assert candidate(edges = [[3, 1], [4, 1], [5, 2], [3, 5], [4, 2]]) == [4, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 1], [4, 3]]) == [2, 3]
    assert candidate(edges = [[2, 1], [3, 1], [1, 4], [4, 3]]) == [3, 1]
    assert candidate(edges = [[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 2], [1, 5], [5, 2]]) == [4, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 1], [1, 4]]) == [3, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 2]]) == [3, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1]
    assert candidate(edges = [[2, 1], [3, 1], [4, 2], [1, 4]]) == [2, 1]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19], [15, 20], [16, 21], [17, 22], [18, 23], [19, 24], [20, 25], [21, 26], [22, 27], [23, 28], [24, 29], [25, 30], [30, 1]]) == [30, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 3]]) == [12, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 4]]) == [12, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 8]]) == [14, 8]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1]]) == [15, 1]
    assert candidate(edges = [[3, 1], [4, 1], [5, 1], [3, 2], [3, 4], [3, 5]]) == [3, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1], [20, 1]]) == [5, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 5], [3, 6]]) == [2, 3]
    assert candidate(edges = [[10, 1], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [2, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [3, 6]]) == [5, 1]
    assert candidate(edges = [[5, 1], [1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [5, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 4]]) == [10, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4], [7, 1]]) == [6, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [3, 6], [6, 7]]) == [5, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == [10, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [2, 4]]) == [3, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 6]]) == [11, 6]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 1]]) == [2, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 11]]) == [1, 11]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6]]) == [5, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3]]) == [5, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 10]]) == [25, 10]
    assert candidate(edges = [[5, 2], [1, 5], [4, 1], [3, 5], [4, 3]]) == [3, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3]]) == [2, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == [9, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 3]]) == [9, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5], [1, 5]]) == [10, 5]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 1], [12, 2]]) == [1, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 5], [1, 9]]) == [8, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 5]]) == [4, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 5], [5, 4], [4, 2], [1, 4]]) == [1, 2]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 2]]) == [1, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 8], [8, 9], [9, 10], [10, 7]]) == [6, 7]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 1]]) == [11, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3]]) == [2, 3]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19], [15, 20], [16, 21], [17, 22], [18, 23], [19, 24], [20, 25], [21, 26], [22, 27], [23, 28], [24, 29], [25, 30], [30, 15]]) == [30, 15]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 3]]) == [11, 3]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == [2, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3], [2, 4]]) == [2, 3]
    assert candidate(edges = [[5, 3], [1, 5], [2, 3], [4, 1], [5, 2], [4, 5]]) == [5, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 5]]) == [2, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == [6, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 2]]) == [10, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 7]]) == [13, 7]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6], [6, 7]]) == [5, 3]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 4]]) == [3, 4]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [6, 8], [7, 8], [8, 2]]) == [1, 2]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3]]) == [1, 3]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 5]]) == [2, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 15]]) == [30, 15]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 6]]) == [9, 6]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 5]]) == [12, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 1]]) == [30, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 2]]) == [5, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 1], [20, 2]]) == [1, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4]]) == [6, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 10], [3, 10], [5, 10]]) == [10, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 5]]) == [20, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 2]]) == [9, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [1, 13]]) == [4, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5]]) == [10, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 3]]) == [10, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [1, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [5, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4], [1, 9], [9, 10], [10, 1]]) == [3, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [1, 3], [3, 5]]) == [2, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [4, 2]]) == [1, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [9, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 4]]) == [3, 4]
    assert candidate(edges = [[2, 3], [4, 3], [5, 3], [1, 4], [2, 5], [4, 5]]) == [2, 5]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 9]]) == [8, 9]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1], [2, 10], [5, 10]]) == [10, 1]
    assert candidate(edges = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 1], [6, 1]]) == [1, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 5], [1, 10]]) == [4, 5]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 7]]) == [14, 7]
    assert candidate(edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 6], [4, 6], [5, 6], [2, 3]]) == [1, 3]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 13]]) == [20, 13]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 4]]) == [8, 4]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 7]]) == [9, 7]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 2]]) == [1, 2]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 4]]) == [9, 4]
    assert candidate(edges = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 1]]) == [5, 1]
    assert candidate(edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3], [6, 4]]) == [3, 4]
    assert candidate(edges = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [9, 5]]) == [9, 5]


