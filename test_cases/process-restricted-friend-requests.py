def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [0, 3]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [0, 3]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,restrictions = [],requests = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,restrictions = [],requests = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [1, 2]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [1, 2]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,restrictions = [[0, 1], [1, 2], [2, 3]],requests = [[0, 4], [1, 2], [3, 1], [3, 4]]) == [True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,restrictions = [[0, 1], [1, 2], [2, 3]],requests = [[0, 4], [1, 2], [3, 1], [3, 4]]) == [True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,restrictions = [[1, 4], [2, 5]],requests = [[0, 3], [1, 2], [3, 4]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,restrictions = [[1, 4], [2, 5]],requests = [[0, 3], [1, 2], [3, 4]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [4, 5], [2, 4]]) == [True, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [4, 5], [2, 4]]) == [True, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,restrictions = [[0, 1]],requests = [[1, 2], [0, 2]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,restrictions = [[0, 1]],requests = [[1, 2], [0, 2]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,restrictions = [[0, 1]],requests = [[0, 2], [2, 1]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,restrictions = [[0, 1]],requests = [[0, 2], [2, 1]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 5], [2, 7], [4, 9], [1, 6]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 5], [2, 7], [4, 9], [1, 6]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [0, 5], [2, 7], [4, 9], [6, 11]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [0, 5], [2, 7], [4, 9], [6, 11]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,restrictions = [[0, 6], [1, 5], [2, 4]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == [True, True, True, False, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,restrictions = [[0, 6], [1, 5], [2, 4]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == [True, True, True, False, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,restrictions = [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 10]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,restrictions = [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 10]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,restrictions = [[0, 3], [1, 4], [2, 5], [6, 8]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [8, 2]]) == [True, True, False, True, True, True, True, False, True, True, False, False, True, True, True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,restrictions = [[0, 3], [1, 4], [2, 5], [6, 8]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [8, 2]]) == [True, True, False, True, True, True, True, False, True, True, False, False, True, True, True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == [True, True, False, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == [True, True, False, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 9]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 3], [5, 2], [6, 1], [7, 0], [8, 5], [9, 4]]) == [True, True, True, True, False, True, False, True, True, False, False, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 9]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 3], [5, 2], [6, 1], [7, 0], [8, 5], [9, 4]]) == [True, True, True, True, False, True, False, True, True, False, False, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 0], [14, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 0], [14, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 4], [1, 5], [2, 6], [3, 7]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 5]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 4], [1, 5], [2, 6], [3, 7]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 5]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 7], [1, 6], [2, 5], [3, 4]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == [True, True, True, False, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 7], [1, 6], [2, 5], [3, 4]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == [True, True, True, False, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 0], [6, 1], [7, 2], [8, 3]]) == [True, True, True, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 0], [6, 1], [7, 2], [8, 3]]) == [True, True, True, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 5], [9, 10], [10, 11], [11, 12], [12, 9], [13, 14], [14, 13]],requests = [[0, 3], [1, 4], [2, 0], [3, 1], [4, 2], [5, 8], [6, 9], [7, 10], [8, 11], [9, 12], [10, 5], [11, 6], [12, 7]]) == [True, True, False, False, False, False, True, True, True, False, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 5], [9, 10], [10, 11], [11, 12], [12, 9], [13, 14], [14, 13]],requests = [[0, 3], [1, 4], [2, 0], [3, 1], [4, 2], [5, 8], [6, 9], [7, 10], [8, 11], [9, 12], [10, 5], [11, 6], [12, 7]]) == [True, True, False, False, False, False, True, True, True, False, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 11]]) == [True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 11]]) == [True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 4], [1, 5], [2, 6], [3, 7]],requests = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 5], [1, 6], [2, 7], [3, 4]]) == [True, True, True, True, True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 4], [1, 5], [2, 6], [3, 7]],requests = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 5], [1, 6], [2, 7], [3, 4]]) == [True, True, True, True, True, True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [0, 5], [1, 6], [2, 7], [3, 4]]) == [True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [0, 5], [1, 6], [2, 7], [3, 4]]) == [True, True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4]],requests = [[0, 4], [1, 5], [2, 6], [3, 7]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4]],requests = [[0, 4], [1, 5], [2, 6], [3, 7]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 5], [2, 7], [4, 9], [1, 6], [3, 8]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 5], [2, 7], [4, 9], [1, 6], [3, 8]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 0], [9, 1]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 0], [9, 1]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]],requests = [[0, 6], [1, 5], [2, 4], [3, 0], [4, 1], [5, 2], [6, 3]]) == [True, False, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]],requests = [[0, 6], [1, 5], [2, 4], [3, 0], [4, 1], [5, 2], [6, 3]]) == [True, False, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == [True, True, True, True, False, True, True, True, True, False, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == [True, True, True, True, False, True, True, True, True, False, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 0], [6, 1], [7, 2]]) == [True, False, True, True, True, False, True, True, False, False, True, False, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 0], [6, 1], [7, 2]]) == [True, False, True, True, True, False, True, True, False, False, True, False, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 0]],requests = [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [12, 14], [14, 1]]) == [True, True, True, True, True, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 0]],requests = [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [12, 14], [14, 1]]) == [True, True, True, True, True, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [0, 8]],requests = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 8], [0, 7], [1, 6], [2, 5], [3, 4]]) == [False, True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [0, 8]],requests = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 8], [0, 7], [1, 6], [2, 5], [3, 4]]) == [False, True, True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]]) == [True, True, True, True, False, True, True, True, True, False, True, True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]]) == [True, True, True, True, False, True, True, True, True, False, True, True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]]) == [True, True, True, True, False, True, True, True, True, False, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]]) == [True, True, True, True, False, True, True, True, True, False, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,restrictions = [[0, 2], [1, 3], [4, 6]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [1, 4], [2, 5]]) == [True, False, True, True, True, False, True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,restrictions = [[0, 2], [1, 3], [4, 6]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [1, 4], [2, 5]]) == [True, False, True, True, True, False, True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 6], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 6], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 0], [6, 1], [7, 2], [8, 3], [9, 4]]) == [True, True, False, True, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 0], [6, 1], [7, 2], [8, 3], [9, 4]]) == [True, True, False, True, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 0], [14, 1]],requests = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 0]]) == [True, True, True, True, True, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 0], [14, 1]],requests = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 0]]) == [True, True, True, True, True, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],requests = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],requests = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,restrictions = [[0, 2], [1, 3], [4, 6]],requests = [[0, 1], [2, 3], [4, 5], [5, 6], [0, 3], [2, 5]]) == [True, True, True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,restrictions = [[0, 2], [1, 3], [4, 6]],requests = [[0, 1], [2, 3], [4, 5], [5, 6], [0, 3], [2, 5]]) == [True, True, True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1]]) == [True, True, True, True, True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1]]) == [True, True, True, True, True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1], [0, 4]]) == [True, True, True, True, True, True, False, False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1], [0, 4]]) == [True, True, True, True, True, True, False, False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == [True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, False, False, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == [True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, False, False, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [1, 4], [3, 4]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [1, 4], [3, 4]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],requests = [[0, 6], [1, 5], [2, 4], [3, 0], [4, 1], [5, 2], [6, 3]]) == [True, True, True, True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],requests = [[0, 6], [1, 5], [2, 4], [3, 0], [4, 1], [5, 2], [6, 3]]) == [True, True, True, True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]],requests = [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]],requests = [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 1], [2, 3], [4, 5], [5, 6], [6, 7]],requests = [[0, 2], [1, 4], [3, 5], [5, 7], [0, 7], [4, 6]]) == [True, True, True, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 1], [2, 3], [4, 5], [5, 6], [6, 7]],requests = [[0, 2], [1, 4], [3, 5], [5, 7], [0, 7], [4, 6]]) == [True, True, True, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 7], [10, 11], [11, 12], [12, 10], [13, 14]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 0], [12, 1], [13, 2], [14, 3]]) == [True, True, True, True, True, True, True, True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 7], [10, 11], [11, 12], [12, 10], [13, 14]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 0], [12, 1], [13, 2], [14, 3]]) == [True, True, True, True, True, True, True, True, True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7], [0, 4], [2, 6], [1, 5], [3, 7], [0, 6], [2, 4], [1, 7], [3, 5]]) == [True, True, True, True, False, False, False, False, True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7], [0, 4], [2, 6], [1, 5], [3, 7], [0, 6], [2, 4], [1, 7], [3, 5]]) == [True, True, True, True, False, False, False, False, True, True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]],requests = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]],requests = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 9], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]) == [False, False, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 9], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]) == [False, False, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],requests = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],requests = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],requests = [[0, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],requests = [[0, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == [True, True, True, True, False, True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == [True, True, True, True, False, True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [0, 7], [1, 6]]) == [True, True, True, True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [0, 7], [1, 6]]) == [True, True, True, True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 5], [1, 4], [2, 3], [6, 11], [7, 10], [8, 9], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 5], [1, 4], [2, 3], [6, 11], [7, 10], [8, 9], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 0], [10, 1]]) == [True, True, True, True, True, True, True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 0], [10, 1]]) == [True, True, True, True, True, True, True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15], [16, 18], [17, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15], [16, 18], [17, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 6]]) == [True, True, True, True, True, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 6]]) == [True, True, True, True, True, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,restrictions = [[0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == [True, True, True, True, True, True, False, True, True, True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,restrictions = [[0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == [True, True, True, True, True, True, False, True, True, True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1], [0, 8], [1, 7], [2, 6], [3, 5], [4, 3], [5, 2], [6, 1], [7, 0], [8, 6], [0, 4], [1, 5], [2, 7], [3, 8]]) == [True, True, True, True, True, True, True, False, False, True, True, True, True, False, False, False, False, True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1], [0, 8], [1, 7], [2, 6], [3, 5], [4, 3], [5, 2], [6, 1], [7, 0], [8, 6], [0, 4], [1, 5], [2, 7], [3, 8]]) == [True, True, True, True, True, True, True, False, False, True, True, True, True, False, False, False, False, True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,restrictions = [[0, 3], [1, 4], [2, 5], [6, 9], [7, 10], [8, 11]],requests = [[0, 1], [1, 2], [3, 4], [4, 5], [6, 7], [7, 8], [9, 10], [10, 11], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,restrictions = [[0, 3], [1, 4], [2, 5], [6, 9], [7, 10], [8, 11]],requests = [[0, 1], [1, 2], [3, 4], [4, 5], [6, 7], [7, 8], [9, 10], [10, 11], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [0, 5], [1, 4]]) == [True, True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [0, 5], [1, 4]]) == [True, True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == [True, True, True, True, False, True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == [True, True, True, True, False, True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,restrictions = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],requests = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == [True, True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,restrictions = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],requests = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == [True, True, True, True, True, False, False, False, False]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [0, 3]]) == [True, True, False]
    assert candidate(n = 4,restrictions = [],requests = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [True, True, True, True]
    assert candidate(n = 4,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [1, 2]]) == [True, True, False]
    assert candidate(n = 5,restrictions = [[0, 1], [1, 2], [2, 3]],requests = [[0, 4], [1, 2], [3, 1], [3, 4]]) == [True, False, True, False]
    assert candidate(n = 6,restrictions = [[1, 4], [2, 5]],requests = [[0, 3], [1, 2], [3, 4]]) == [True, True, True]
    assert candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == [True, True, True, True, True, True]
    assert candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [4, 5], [2, 4]]) == [True, True, False, True]
    assert candidate(n = 3,restrictions = [[0, 1]],requests = [[1, 2], [0, 2]]) == [True, False]
    assert candidate(n = 3,restrictions = [[0, 1]],requests = [[0, 2], [2, 1]]) == [True, False]
    assert candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 5], [2, 7], [4, 9], [1, 6]]) == [True, True, True, True]
    assert candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [0, 5], [2, 7], [4, 9], [6, 11]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 7,restrictions = [[0, 6], [1, 5], [2, 4]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == [True, True, True, False, True, True, False]
    assert candidate(n = 20,restrictions = [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 10]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 9,restrictions = [[0, 3], [1, 4], [2, 5], [6, 8]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [8, 2]]) == [True, True, False, True, True, True, True, False, True, True, False, False, True, True, True, False, False, True]
    assert candidate(n = 7,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == [True, True, False, True, True, False, False]
    assert candidate(n = 10,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 9]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 9], [1, 8], [2, 7], [3, 6], [4, 3], [5, 2], [6, 1], [7, 0], [8, 5], [9, 4]]) == [True, True, True, True, False, True, False, True, True, False, False, False, False, True, False]
    assert candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 0], [14, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False]
    assert candidate(n = 8,restrictions = [[0, 4], [1, 5], [2, 6], [3, 7]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 5]]) == [True, True, True, True, False]
    assert candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, False]
    assert candidate(n = 8,restrictions = [[0, 7], [1, 6], [2, 5], [3, 4]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == [True, True, True, False, True, True, True, False]
    assert candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 0], [6, 1], [7, 2], [8, 3]]) == [True, True, True, True, False, False, False, False, False]
    assert candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]
    assert candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 5], [9, 10], [10, 11], [11, 12], [12, 9], [13, 14], [14, 13]],requests = [[0, 3], [1, 4], [2, 0], [3, 1], [4, 2], [5, 8], [6, 9], [7, 10], [8, 11], [9, 12], [10, 5], [11, 6], [12, 7]]) == [True, True, False, False, False, False, True, True, True, False, True, True, True]
    assert candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 11]]) == [True, True, True, True, True, True, True]
    assert candidate(n = 8,restrictions = [[0, 4], [1, 5], [2, 6], [3, 7]],requests = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 5], [1, 6], [2, 7], [3, 4]]) == [True, True, True, True, True, True, True, True, False, False, False, False]
    assert candidate(n = 8,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [0, 5], [1, 6], [2, 7], [3, 4]]) == [True, True, True, True, False, False, False, False]
    assert candidate(n = 8,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4]],requests = [[0, 4], [1, 5], [2, 6], [3, 7]]) == [True, True, True, True]
    assert candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 5], [2, 7], [4, 9], [1, 6], [3, 8]]) == [True, True, True, True, True]
    assert candidate(n = 10,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 0], [9, 1]]) == [True, True, True, True, True, True]
    assert candidate(n = 7,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]],requests = [[0, 6], [1, 5], [2, 4], [3, 0], [4, 1], [5, 2], [6, 3]]) == [True, False, True, False, False, False, False]
    assert candidate(n = 15,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == [True, True, True, True, False, True, True, True, True, False, True, True, True, True]
    assert candidate(n = 8,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 0], [6, 1], [7, 2]]) == [True, False, True, True, True, False, True, True, False, False, True, False, False, False, True, False]
    assert candidate(n = 15,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 0]],requests = [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [12, 14], [14, 1]]) == [True, True, True, True, True, True, False, True]
    assert candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [0, 8]],requests = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 8], [0, 7], [1, 6], [2, 5], [3, 4]]) == [False, True, True, True, True, False, False, False, False]
    assert candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 2], [2, 4], [4, 6], [6, 8], [8, 0]]) == [True, True, True, True, False, True, True, True, True, False, True, True, False, True, False]
    assert candidate(n = 10,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 0], [9, 1]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 15,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12], [8, 13], [9, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0]]) == [True, True, True, True, False, True, True, True, True, False, True, True, True, True, True]
    assert candidate(n = 7,restrictions = [[0, 2], [1, 3], [4, 6]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0], [0, 3], [1, 4], [2, 5]]) == [True, False, True, True, True, False, True, False, False, True]
    assert candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 6], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]
    assert candidate(n = 10,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 0], [6, 1], [7, 2], [8, 3], [9, 4]]) == [True, True, False, True, True, False, False, False, False, False]
    assert candidate(n = 15,restrictions = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 0], [14, 1]],requests = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 0]]) == [True, True, True, True, True, True, False, True]
    assert candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]],requests = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 7,restrictions = [[0, 2], [1, 3], [4, 6]],requests = [[0, 1], [2, 3], [4, 5], [5, 6], [0, 3], [2, 5]]) == [True, True, True, False, False, True]
    assert candidate(n = 9,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1]]) == [True, True, True, True, True, True, False, False, False]
    assert candidate(n = 9,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 0]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1], [0, 4]]) == [True, True, True, True, True, True, False, False, True, True]
    assert candidate(n = 15,restrictions = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 0], [0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]) == [True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, False, False, False, False, False, False, True]
    assert candidate(n = 5,restrictions = [[0, 2], [1, 3]],requests = [[0, 1], [2, 3], [1, 4], [3, 4]]) == [True, True, True, False]
    assert candidate(n = 7,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],requests = [[0, 6], [1, 5], [2, 4], [3, 0], [4, 1], [5, 2], [6, 3]]) == [True, True, True, True, False, False, True]
    assert candidate(n = 20,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 0]],requests = [[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [10, 15], [11, 16], [12, 17], [13, 18], [14, 19]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 10,restrictions = [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],requests = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, False]
    assert candidate(n = 8,restrictions = [[0, 1], [2, 3], [4, 5], [5, 6], [6, 7]],requests = [[0, 2], [1, 4], [3, 5], [5, 7], [0, 7], [4, 6]]) == [True, True, True, True, False, True]
    assert candidate(n = 15,restrictions = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 4], [7, 8], [8, 9], [9, 7], [10, 11], [11, 12], [12, 10], [13, 14]],requests = [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [10, 14], [11, 0], [12, 1], [13, 2], [14, 3]]) == [True, True, True, True, True, True, True, True, True, True, True, False, False, False, False]
    assert candidate(n = 8,restrictions = [[0, 2], [1, 3], [4, 6], [5, 7]],requests = [[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7], [0, 4], [2, 6], [1, 5], [3, 7], [0, 6], [2, 4], [1, 7], [3, 5]]) == [True, True, True, True, False, False, False, False, True, True, True, True, False, False, False, False]
    assert candidate(n = 7,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]],requests = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 0], [5, 1], [6, 2]]) == [True, True, True, False, False, False, False]
    assert candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]],requests = [[0, 9], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]) == [False, False, False, False, False, False, False, False, False, False]
    assert candidate(n = 12,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],requests = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 0], [7, 1], [8, 2], [9, 3], [10, 4], [11, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 10,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],requests = [[0, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True]
    assert candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == [True, True, True, True, False, True, True, True, True, False]
    assert candidate(n = 8,restrictions = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [0, 7], [1, 6]]) == [True, True, True, True, True, True, False, False]
    assert candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 5], [1, 4], [2, 3], [6, 11], [7, 10], [8, 9], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, False, False, False, False, False, False]
    assert candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 12,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True, True, True, True, True, False, False]
    assert candidate(n = 11,restrictions = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 0], [10, 1]]) == [True, True, True, True, True, True, True, True, True, False, False]
    assert candidate(n = 20,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]],requests = [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15], [16, 18], [17, 19], [0, 19], [1, 18], [2, 17], [3, 16], [4, 15], [5, 14], [6, 13], [7, 12], [8, 11], [9, 10]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False]
    assert candidate(n = 12,restrictions = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 6]]) == [True, True, True, True, True, False, False, False, False, False, False]
    assert candidate(n = 15,restrictions = [[0, 7], [1, 8], [2, 9], [3, 10], [4, 11], [5, 12], [6, 13], [7, 14]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == [True, True, True, True, True, True, False, True, True, True, True, True, True, False]
    assert candidate(n = 9,restrictions = [[0, 1], [2, 3], [4, 5], [6, 7]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 0], [8, 1], [0, 8], [1, 7], [2, 6], [3, 5], [4, 3], [5, 2], [6, 1], [7, 0], [8, 6], [0, 4], [1, 5], [2, 7], [3, 8]]) == [True, True, True, True, True, True, True, False, False, True, True, True, True, False, False, False, False, True, True, True, False, False]
    assert candidate(n = 12,restrictions = [[0, 3], [1, 4], [2, 5], [6, 9], [7, 10], [8, 11]],requests = [[0, 1], [1, 2], [3, 4], [4, 5], [6, 7], [7, 8], [9, 10], [10, 11], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, True]
    assert candidate(n = 6,restrictions = [[0, 1], [2, 3], [4, 5]],requests = [[0, 2], [1, 3], [2, 4], [3, 5], [0, 5], [1, 4]]) == [True, True, True, True, False, False]
    assert candidate(n = 10,restrictions = [[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 10,restrictions = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]],requests = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == [True, True, True, True, False, True, True, True, True, False]
    assert candidate(n = 8,restrictions = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],requests = [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [0, 1], [2, 3], [4, 5], [6, 7]]) == [True, True, True, True, True, False, False, False, False]


