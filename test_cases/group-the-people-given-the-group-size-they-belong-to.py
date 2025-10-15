def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 2, 1, 1]) == [[0], [3], [4], [1, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 2, 1, 1]) == [[0], [3], [4], [1, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 1, 1, 1, 1, 1]) == [[0], [1], [2], [3], [4], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 1, 1, 1, 1, 1]) == [[0], [1], [2], [3], [4], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 2, 1]) == [[0], [3], [1, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 2, 1]) == [[0], [3], [1, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 3, 3, 3, 4, 4, 4, 4]) == [[0, 1], [2, 3, 4], [5, 6, 7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 3, 3, 3, 4, 4, 4, 4]) == [[0, 1], [2, 3, 4], [5, 6, 7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 3, 3, 3]) == [[0, 1], [2, 3, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 3, 3, 3]) == [[0, 1], [2, 3, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 3, 3, 3, 3, 3, 3]) == [[0, 1], [2, 3, 4], [5, 6, 7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 3, 3, 3, 3, 3, 3]) == [[0, 1], [2, 3, 4], [5, 6, 7]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 1, 1]) == [[0, 1], [2], [3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 1, 1]) == [[0, 1], [2], [3]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 1, 3, 3, 3, 2]) == [[0, 5], [1], [2, 3, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 1, 3, 3, 3, 2]) == [[0, 5], [1], [2, 3, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 1, 1, 1, 1]) == [[0], [1], [2], [3], [4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 1, 1, 1, 1]) == [[0], [1], [2], [3], [4]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 3, 1, 3]) == [[0, 1, 2], [3, 4, 6], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 3, 1, 3]) == [[0, 1, 2], [3, 4, 6], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 3, 4, 5]) == [[0], [1], [2], [3], [4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 3, 4, 5]) == [[0], [1], [2], [3], [4]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [4, 4, 4, 4]) == [[0, 1, 2, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [4, 4, 4, 4]) == [[0, 1, 2, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9], [10, 11], [12, 13, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9], [10, 11], [12, 13, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == [[0, 1, 2, 3, 4], [5, 6, 7], [8, 9], [10, 11], [12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == [[0, 1, 2, 3, 4], [5, 6, 7], [8, 9], [10, 11], [12]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [7, 2, 2, 7, 7, 2, 2, 2, 7, 7, 7, 7, 7]) == [[0, 3, 4, 8, 9, 10, 11], [12], [1, 2], [5, 6], [7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [7, 2, 2, 7, 7, 2, 2, 2, 7, 7, 7, 7, 7]) == [[0, 3, 4, 8, 9, 10, 11], [12], [1, 2], [5, 6], [7]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2]) == [[0, 1, 2], [3, 4], [5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2]) == [[0, 1, 2], [3, 4], [5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9], [10, 11], [12, 13], [14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9], [10, 11], [12, 13], [14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 3, 2, 3, 3, 1]) == [[0, 3], [1, 2, 4], [5], [6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 3, 2, 3, 3, 1]) == [[0, 3], [1, 2, 4], [5], [6]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4]) == [[0, 1, 2], [3], [4, 5], [6], [7], [8], [9], [10], [11, 12, 13, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4]) == [[0, 1, 2], [3], [4, 5], [6], [7], [8], [9], [10], [11, 12, 13, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10], [11], [12], [13], [14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10], [11], [12], [13], [14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == [[0, 2], [3], [1, 4, 5], [6], [7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == [[0, 2], [3], [1, 4, 5], [6], [7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2]) == [[0, 3], [4, 7], [8, 11], [1, 2, 5], [6, 9, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2]) == [[0, 3], [4, 7], [8, 11], [1, 2, 5], [6, 9, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [[0, 2], [4, 6], [8, 10], [12, 14], [1, 3, 5], [7, 9, 11], [13, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [[0, 2], [4, 6], [8, 10], [12, 14], [1, 3, 5], [7, 9, 11], [13, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 3, 2, 1, 3, 4, 3, 4, 2, 1, 4, 3, 2, 1, 3, 4, 3, 2, 1, 4]) == [[0], [4], [10], [14], [19], [1, 3], [9, 13], [18], [2, 5, 7], [12, 15, 17], [6, 8, 11, 16], [20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 3, 2, 1, 3, 4, 3, 4, 2, 1, 4, 3, 2, 1, 3, 4, 3, 2, 1, 4]) == [[0], [4], [10], [14], [19], [1, 3], [9, 13], [18], [2, 5, 7], [12, 15, 17], [6, 8, 11, 16], [20]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]) == [[0, 5], [10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]) == [[0, 5], [10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [[0, 1], [2, 3, 4], [5], [6, 7, 8, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [[0, 1], [2, 3, 4], [5], [6, 7, 8, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1]) == [[0, 1, 2], [3], [4, 5], [6], [7], [8], [9], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1]) == [[0, 1, 2], [3], [4, 5], [6], [7], [8], [9], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == [[0, 1, 2, 3, 4, 5, 6], [7], [8], [9], [10], [11], [12], [13], [14, 15], [16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == [[0, 1, 2, 3, 4, 5, 6], [7], [8], [9], [10], [11], [12], [13], [14, 15], [16]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 2, 3, 3, 2, 3]) == [[0, 2], [5], [1, 3, 4], [6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 2, 3, 3, 2, 3]) == [[0, 2], [5], [1, 3, 4], [6]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6], [7], [8], [9], [10], [11], [12], [13]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6], [7], [8], [9], [10], [11], [12], [13]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [4, 3, 3, 4, 2, 2, 4, 3, 3, 4, 2, 2, 4, 3, 3, 4, 2, 2]) == [[0, 3, 6, 9], [12, 15], [1, 2, 7], [8, 13, 14], [4, 5], [10, 11], [16, 17]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [4, 3, 3, 4, 2, 2, 4, 3, 3, 4, 2, 2, 4, 3, 3, 4, 2, 2]) == [[0, 3, 6, 9], [12, 15], [1, 2, 7], [8, 13, 14], [4, 5], [10, 11], [16, 17]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21, 22], [23, 24, 25], [26, 27, 28], [29], [30, 31, 32, 33], [34, 35, 36, 37], [38, 39, 40, 41], [42, 43, 44, 45]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21, 22], [23, 24, 25], [26, 27, 28], [29], [30, 31, 32, 33], [34, 35, 36, 37], [38, 39, 40, 41], [42, 43, 44, 45]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15], [16], [17], [18], [19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15], [16], [17], [18], [19]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [[0], [10], [1, 9], [2, 8], [3, 7], [4, 6], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [[0], [10], [1, 9], [2, 8], [3, 7], [4, 6], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [4, 4, 4, 4, 3, 3, 3, 2, 2, 1]) == [[0, 1, 2, 3], [4, 5, 6], [7, 8], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [4, 4, 4, 4, 3, 3, 3, 2, 2, 1]) == [[0, 1, 2, 3], [4, 5, 6], [7, 8], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [[0, 5, 10, 15], [1, 6, 11, 16], [2, 7, 12], [17], [3, 8], [13, 18], [4], [9], [14], [19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [[0, 5, 10, 15], [1, 6, 11, 16], [2, 7, 12], [17], [3, 8], [13, 18], [4], [9], [14], [19]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21, 22, 23]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21, 22, 23]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9], [10], [11], [12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9], [10], [11], [12]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [25, 26, 27, 28, 29], [30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [25, 26, 27, 28, 29], [30]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [[0, 2], [4, 6], [8, 10], [1, 3, 5], [7, 9, 11]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [[0, 2], [4, 6], [8, 10], [1, 3, 5], [7, 9, 11]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [[0], [10], [1, 9], [2, 8], [3, 7], [4, 6], [5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [[0], [10], [1, 9], [2, 8], [3, 7], [4, 6], [5]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30], [31, 32], [33, 34], [35, 36], [37, 38], [39, 40], [41, 42], [43]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30], [31, 32], [33, 34], [35, 36], [37, 38], [39, 40], [41, 42], [43]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9], [10], [11]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9], [10], [11]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [4, 4, 4, 4, 2, 2, 2, 2]) == [[0, 1, 2, 3], [4, 5], [6, 7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [4, 4, 4, 4, 2, 2, 2, 2]) == [[0, 1, 2, 3], [4, 5], [6, 7]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3], [4], [5, 6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3], [4], [5, 6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 2, 3, 3, 2, 2, 3, 2]) == [[0, 2], [5, 6], [8], [1, 3, 4], [7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 2, 3, 3, 2, 2, 3, 2]) == [[0, 2], [5, 6], [8], [1, 3, 4], [7]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17], [18, 19]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17], [18, 19]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19], [20, 21, 22, 23, 24, 25, 26, 27], [28, 29], [30, 31, 32, 33, 34, 35, 36], [37, 38, 39], [40, 41, 42, 43, 44, 45], [46, 47, 48, 49], [50, 51, 52, 53, 54], [55, 56, 57, 58, 59], [60, 61, 62, 63], [64, 65, 66, 67], [68, 69], [70, 71, 72], [73, 74, 75], [76, 77, 78], [79], [80, 81], [82, 83], [84, 85], [86, 87], [88, 89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19], [20, 21, 22, 23, 24, 25, 26, 27], [28, 29], [30, 31, 32, 33, 34, 35, 36], [37, 38, 39], [40, 41, 42, 43, 44, 45], [46, 47, 48, 49], [50, 51, 52, 53, 54], [55, 56, 57, 58, 59], [60, 61, 62, 63], [64, 65, 66, 67], [68, 69], [70, 71, 72], [73, 74, 75], [76, 77, 78], [79], [80, 81], [82, 83], [84, 85], [86, 87], [88, 89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 9], [1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 9], [1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 2]) == [[0, 1, 2], [7, 8, 9], [10], [3, 4], [5, 6], [11]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 2]) == [[0, 1, 2], [7, 8, 9], [10], [3, 4], [5, 6], [11]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [[0, 2, 4, 6, 8], [1], [3], [5], [7], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [[0, 2, 4, 6, 8], [1], [3], [5], [7], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [8, 1, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 1]) == [[0, 2, 3, 4, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 22, 23, 24, 25], [1], [5], [21], [26]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [8, 1, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 1]) == [[0, 2, 3, 4, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 22, 23, 24, 25], [1], [5], [21], [26]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [22, 23], [24, 25], [26], [27]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [22, 23], [24, 25], [26], [27]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == [[0], [1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == [[0], [1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [5, 1, 5, 5, 5, 1, 5, 5, 5, 5, 1]) == [[0, 2, 3, 4, 6], [7, 8, 9], [1], [5], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [5, 1, 5, 5, 5, 1, 5, 5, 5, 5, 1]) == [[0, 2, 3, 4, 6], [7, 8, 9], [1], [5], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5], [6], [7], [8], [9], [10], [11]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5], [6], [7], [8], [9], [10], [11]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [[0], [5], [1, 6], [2, 7], [3, 8], [4, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [[0], [5], [1, 6], [2, 7], [3, 8], [4, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(groupSizes = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(groupSizes = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(groupSizes = [1, 2, 2, 1, 1]) == [[0], [3], [4], [1, 2]]
    assert candidate(groupSizes = [1, 1, 1, 1, 1, 1]) == [[0], [1], [2], [3], [4], [5]]
    assert candidate(groupSizes = [1, 2, 2, 1]) == [[0], [3], [1, 2]]
    assert candidate(groupSizes = [2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5]]
    assert candidate(groupSizes = [2, 2, 3, 3, 3, 4, 4, 4, 4]) == [[0, 1], [2, 3, 4], [5, 6, 7, 8]]
    assert candidate(groupSizes = [2, 2, 3, 3, 3]) == [[0, 1], [2, 3, 4]]
    assert candidate(groupSizes = [2, 2, 3, 3, 3, 3, 3, 3]) == [[0, 1], [2, 3, 4], [5, 6, 7]]
    assert candidate(groupSizes = [2, 2, 1, 1]) == [[0, 1], [2], [3]]
    assert candidate(groupSizes = [2, 1, 3, 3, 3, 2]) == [[0, 5], [1], [2, 3, 4]]
    assert candidate(groupSizes = [1, 1, 1, 1, 1]) == [[0], [1], [2], [3], [4]]
    assert candidate(groupSizes = [3, 3, 3, 3, 3, 1, 3]) == [[0, 1, 2], [3, 4, 6], [5]]
    assert candidate(groupSizes = [1, 2, 3, 4, 5]) == [[0], [1], [2], [3], [4]]
    assert candidate(groupSizes = [5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4]]
    assert candidate(groupSizes = [4, 4, 4, 4]) == [[0, 1, 2, 3]]
    assert candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9], [10, 11], [12, 13, 14]]
    assert candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9]]
    assert candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7]]
    assert candidate(groupSizes = [5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1]) == [[0, 1, 2, 3, 4], [5, 6, 7], [8, 9], [10, 11], [12]]
    assert candidate(groupSizes = [7, 2, 2, 7, 7, 2, 2, 2, 7, 7, 7, 7, 7]) == [[0, 3, 4, 8, 9, 10, 11], [12], [1, 2], [5, 6], [7]]
    assert candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2]) == [[0, 1, 2], [3, 4], [5, 6]]
    assert candidate(groupSizes = [5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [[0, 1, 2, 3, 4], [5], [6], [7], [8], [9], [10, 11], [12, 13], [14]]
    assert candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    assert candidate(groupSizes = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43]]
    assert candidate(groupSizes = [2, 3, 3, 2, 3, 3, 1]) == [[0, 3], [1, 2, 4], [5], [6]]
    assert candidate(groupSizes = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4]) == [[0, 1, 2], [3], [4, 5], [6], [7], [8], [9], [10], [11, 12, 13, 14]]
    assert candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13]]
    assert candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10], [11], [12], [13], [14]]
    assert candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]
    assert candidate(groupSizes = [2, 3, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == [[0, 2], [3], [1, 4, 5], [6], [7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21]]
    assert candidate(groupSizes = [2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2]) == [[0, 3], [4, 7], [8, 11], [1, 2, 5], [6, 9, 10]]
    assert candidate(groupSizes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9]]
    assert candidate(groupSizes = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [[0, 2], [4, 6], [8, 10], [12, 14], [1, 3, 5], [7, 9, 11], [13, 15]]
    assert candidate(groupSizes = [1, 2, 3, 2, 1, 3, 4, 3, 4, 2, 1, 4, 3, 2, 1, 3, 4, 3, 2, 1, 4]) == [[0], [4], [10], [14], [19], [1, 3], [9, 13], [18], [2, 5, 7], [12, 15, 17], [6, 8, 11, 16], [20]]
    assert candidate(groupSizes = [2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]) == [[0, 5], [10], [1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14]]
    assert candidate(groupSizes = [2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [[0, 1], [2, 3, 4], [5], [6, 7, 8, 9]]
    assert candidate(groupSizes = [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30]]
    assert candidate(groupSizes = [3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1]) == [[0, 1, 2], [3], [4, 5], [6], [7], [8], [9], [10]]
    assert candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == [[0, 1, 2, 3, 4, 5, 6], [7], [8], [9], [10], [11], [12], [13], [14, 15], [16]]
    assert candidate(groupSizes = [2, 3, 2, 3, 3, 2, 3]) == [[0, 2], [5], [1, 3, 4], [6]]
    assert candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6], [7], [8], [9], [10], [11], [12], [13]]
    assert candidate(groupSizes = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]
    assert candidate(groupSizes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13, 14]]
    assert candidate(groupSizes = [4, 3, 3, 4, 2, 2, 4, 3, 3, 4, 2, 2, 4, 3, 3, 4, 2, 2]) == [[0, 3, 6, 9], [12, 15], [1, 2, 7], [8, 13, 14], [4, 5], [10, 11], [16, 17]]
    assert candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14]]
    assert candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21, 22], [23, 24, 25], [26, 27, 28], [29], [30, 31, 32, 33], [34, 35, 36, 37], [38, 39, 40, 41], [42, 43, 44, 45]]
    assert candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15], [16], [17], [18], [19]]
    assert candidate(groupSizes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [[0], [10], [1, 9], [2, 8], [3, 7], [4, 6], [5]]
    assert candidate(groupSizes = [4, 4, 4, 4, 3, 3, 3, 2, 2, 1]) == [[0, 1, 2, 3], [4, 5, 6], [7, 8], [9]]
    assert candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
    assert candidate(groupSizes = [4, 4, 4, 4, 4, 4, 4, 4]) == [[0, 1, 2, 3], [4, 5, 6, 7]]
    assert candidate(groupSizes = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [[0, 5, 10, 15], [1, 6, 11, 16], [2, 7, 12], [17], [3, 8], [13, 18], [4], [9], [14], [19]]
    assert candidate(groupSizes = [7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21, 22, 23]]
    assert candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9], [10], [11], [12]]
    assert candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [25, 26, 27, 28, 29], [30]]
    assert candidate(groupSizes = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [[0, 2], [4, 6], [8, 10], [1, 3, 5], [7, 9, 11]]
    assert candidate(groupSizes = [6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14]]
    assert candidate(groupSizes = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [[0], [10], [1, 9], [2, 8], [3, 7], [4, 6], [5]]
    assert candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30], [31, 32], [33, 34], [35, 36], [37, 38], [39, 40], [41, 42], [43]]
    assert candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]]
    assert candidate(groupSizes = [3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5, 6], [7, 8], [9], [10], [11]]
    assert candidate(groupSizes = [4, 4, 4, 4, 2, 2, 2, 2]) == [[0, 1, 2, 3], [4, 5], [6, 7]]
    assert candidate(groupSizes = [4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3], [4], [5, 6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36]]
    assert candidate(groupSizes = [2, 3, 2, 3, 3, 2, 2, 3, 2]) == [[0, 2], [5, 6], [8], [1, 3, 4], [7]]
    assert candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17], [18, 19]]
    assert candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19], [20, 21, 22, 23, 24, 25, 26, 27], [28, 29], [30, 31, 32, 33, 34, 35, 36], [37, 38, 39], [40, 41, 42, 43, 44, 45], [46, 47, 48, 49], [50, 51, 52, 53, 54], [55, 56, 57, 58, 59], [60, 61, 62, 63], [64, 65, 66, 67], [68, 69], [70, 71, 72], [73, 74, 75], [76, 77, 78], [79], [80, 81], [82, 83], [84, 85], [86, 87], [88, 89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99]]
    assert candidate(groupSizes = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15]]
    assert candidate(groupSizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 9], [1, 10], [2, 11], [3, 12], [4, 13], [5, 14], [6, 15], [7, 16], [8, 17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33]]
    assert candidate(groupSizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    assert candidate(groupSizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
    assert candidate(groupSizes = [3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 2]) == [[0, 1, 2], [7, 8, 9], [10], [3, 4], [5, 6], [11]]
    assert candidate(groupSizes = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [[0, 2, 4, 6, 8], [1], [3], [5], [7], [9]]
    assert candidate(groupSizes = [8, 1, 8, 8, 8, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 8, 8, 8, 8, 1]) == [[0, 2, 3, 4, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 22, 23, 24, 25], [1], [5], [21], [26]]
    assert candidate(groupSizes = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [22, 23], [24, 25], [26], [27]]
    assert candidate(groupSizes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == [[0], [1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15]]
    assert candidate(groupSizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
    assert candidate(groupSizes = [5, 1, 5, 5, 5, 1, 5, 5, 5, 5, 1]) == [[0, 2, 3, 4, 6], [7, 8, 9], [1], [5], [10]]
    assert candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29]]
    assert candidate(groupSizes = [6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2, 3, 4, 5], [6], [7], [8], [9], [10], [11]]
    assert candidate(groupSizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
    assert candidate(groupSizes = [3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[0, 1, 2], [3, 4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29]]
    assert candidate(groupSizes = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [[0], [5], [1, 6], [2, 7], [3, 8], [4, 9]]
    assert candidate(groupSizes = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == [[0], [1, 2], [3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16]]
    assert candidate(groupSizes = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]


