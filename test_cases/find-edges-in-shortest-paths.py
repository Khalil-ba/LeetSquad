def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1, 2], [0, 2, 2], [1, 2, 3], [1, 3, 2], [2, 3, 1], [2, 4, 4], [3, 4, 2]]) == [False, True, False, False, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1, 2], [0, 2, 2], [1, 2, 3], [1, 3, 2], [2, 3, 1], [2, 4, 4], [3, 4, 2]]) == [False, True, False, False, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 2], [0, 2, 5], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 1], [4, 5, 3], [5, 6, 2]]) == [True, False, True, False, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 2], [0, 2, 5], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 1], [4, 5, 3], [5, 6, 2]]) == [True, False, True, False, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 1]]) == [True, True, True, False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 1]]) == [True, True, True, False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 6, 1], [2, 7, 1], [3, 8, 1], [3, 9, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1]]) == [False, False, True, False, False, False, False, False, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 6, 1], [2, 7, 1], [3, 8, 1], [3, 9, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1]]) == [False, False, True, False, False, False, False, False, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 4, 1], [4, 5, 2], [5, 6, 3]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 4, 1], [4, 5, 2], [5, 6, 3]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [0, 4, 10]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [0, 4, 10]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[0, 1, 1], [0, 2, 5], [1, 2, 2]]) == [True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[0, 1, 1], [0, 2, 5], [1, 2, 2]]) == [True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]) == [True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]) == [True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3], [4, 5, 2]]) == [True, True, True, False, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3], [4, 5, 2]]) == [True, True, True, False, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[0, 1, 1], [1, 2, 1], [0, 2, 4]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[0, 1, 1], [1, 2, 1], [0, 2, 4]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1, 1], [0, 2, 1], [1, 3, 1], [1, 4, 1], [2, 5, 1], [2, 6, 1], [3, 7, 1], [3, 8, 1], [4, 9, 1], [4, 10, 1], [5, 11, 1], [5, 12, 1], [6, 13, 1], [6, 14, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1]]) == [False, True, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1, 1], [0, 2, 1], [1, 3, 1], [1, 4, 1], [2, 5, 1], [2, 6, 1], [3, 7, 1], [3, 8, 1], [4, 9, 1], [4, 10, 1], [5, 11, 1], [5, 12, 1], [6, 13, 1], [6, 14, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1]]) == [False, True, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,edges = [[0, 1, 5], [0, 2, 5], [1, 3, 3], [1, 4, 2], [2, 5, 3], [2, 6, 4], [3, 7, 1], [3, 8, 2], [4, 9, 1], [5, 10, 2], [5, 11, 3], [6, 12, 1], [6, 13, 4], [7, 14, 1], [7, 15, 2], [8, 16, 1], [8, 17, 2], [9, 18, 2], [10, 19, 1], [10, 20, 2], [11, 21, 2], [11, 22, 1], [12, 23, 1], [12, 24, 2], [13, 23, 2], [13, 24, 3]]) == [False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,edges = [[0, 1, 5], [0, 2, 5], [1, 3, 3], [1, 4, 2], [2, 5, 3], [2, 6, 4], [3, 7, 1], [3, 8, 2], [4, 9, 1], [5, 10, 2], [5, 11, 3], [6, 12, 1], [6, 13, 4], [7, 14, 1], [7, 15, 2], [8, 16, 1], [8, 17, 2], [9, 18, 2], [10, 19, 1], [10, 20, 2], [11, 21, 2], [11, 22, 1], [12, 23, 1], [12, 24, 2], [13, 23, 2], [13, 24, 3]]) == [False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 5], [0, 2, 2], [1, 3, 1], [1, 4, 6], [2, 5, 3], [3, 6, 2], [4, 7, 4], [5, 8, 5], [6, 9, 1], [7, 9, 3], [8, 9, 2]]) == [True, False, True, False, False, True, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 5], [0, 2, 2], [1, 3, 1], [1, 4, 6], [2, 5, 3], [3, 6, 2], [4, 7, 4], [5, 8, 5], [6, 9, 1], [7, 9, 3], [8, 9, 2]]) == [True, False, True, False, False, True, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1, 10], [0, 2, 20], [1, 3, 5], [1, 4, 10], [2, 5, 15], [3, 6, 20], [4, 7, 25], [5, 8, 30], [6, 9, 35], [7, 10, 40], [8, 11, 45], [9, 12, 50], [10, 13, 55], [11, 14, 60], [0, 6, 65], [1, 7, 70], [2, 8, 75], [3, 9, 80], [4, 10, 85], [5, 11, 90], [6, 12, 95], [7, 13, 100], [8, 14, 105]]) == [False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1, 10], [0, 2, 20], [1, 3, 5], [1, 4, 10], [2, 5, 15], [3, 6, 20], [4, 7, 25], [5, 8, 30], [6, 9, 35], [7, 10, 40], [8, 11, 45], [9, 12, 50], [10, 13, 55], [11, 14, 60], [0, 6, 65], [1, 7, 70], [2, 8, 75], [3, 9, 80], [4, 10, 85], [5, 11, 90], [6, 12, 95], [7, 13, 100], [8, 14, 105]]) == [False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1, 3], [0, 2, 2], [1, 3, 1], [2, 4, 4], [3, 5, 2], [4, 6, 3], [5, 7, 1], [6, 8, 5], [7, 9, 2], [8, 10, 1], [9, 11, 3], [10, 11, 2], [0, 5, 7], [1, 6, 8], [2, 7, 9], [3, 8, 10], [4, 9, 11]]) == [True, False, True, False, True, False, True, False, True, False, True, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1, 3], [0, 2, 2], [1, 3, 1], [2, 4, 4], [3, 5, 2], [4, 6, 3], [5, 7, 1], [6, 8, 5], [7, 9, 2], [8, 10, 1], [9, 11, 3], [10, 11, 2], [0, 5, 7], [1, 6, 8], [2, 7, 9], [3, 8, 10], [4, 9, 11]]) == [True, False, True, False, True, False, True, False, True, False, True, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 2], [1, 2, 2], [2, 3, 1], [3, 4, 3], [4, 5, 2], [5, 6, 1], [6, 7, 2], [7, 8, 3], [8, 9, 2], [0, 9, 10]]) == [False, False, False, False, False, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 2], [1, 2, 2], [2, 3, 1], [3, 4, 3], [4, 5, 2], [5, 6, 1], [6, 7, 2], [7, 8, 3], [8, 9, 2], [0, 9, 10]]) == [False, False, False, False, False, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 2], [2, 5, 3], [2, 6, 4], [3, 7, 2], [3, 8, 3], [4, 9, 1], [4, 10, 4], [5, 11, 2], [5, 12, 3], [6, 13, 4], [6, 14, 5], [7, 8, 1], [9, 10, 2], [11, 12, 3], [13, 14, 4]]) == [False, True, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 2], [2, 5, 3], [2, 6, 4], [3, 7, 2], [3, 8, 3], [4, 9, 1], [4, 10, 4], [5, 11, 2], [5, 12, 3], [6, 13, 4], [6, 14, 5], [7, 8, 1], [9, 10, 2], [11, 12, 3], [13, 14, 4]]) == [False, True, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 2], [0, 2, 4], [0, 3, 1], [1, 4, 3], [1, 5, 1], [2, 3, 2], [2, 6, 5], [3, 7, 1], [4, 8, 2], [5, 8, 3], [6, 9, 4], [7, 9, 3], [8, 9, 1]]) == [False, False, True, False, False, False, False, True, False, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 2], [0, 2, 4], [0, 3, 1], [1, 4, 3], [1, 5, 1], [2, 3, 2], [2, 6, 5], [3, 7, 1], [4, 8, 2], [5, 8, 3], [6, 9, 4], [7, 9, 3], [8, 9, 1]]) == [False, False, True, False, False, False, False, True, False, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 5], [0, 2, 10], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 6, 1], [6, 0, 3]]) == [False, False, False, False, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 5], [0, 2, 10], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 6, 1], [6, 0, 3]]) == [False, False, False, False, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1, 2], [0, 2, 4], [1, 3, 3], [1, 4, 1], [2, 4, 2], [2, 5, 5], [3, 6, 2], [4, 6, 1], [4, 7, 4], [5, 8, 3], [6, 9, 2], [7, 10, 1], [8, 10, 3], [9, 11, 2], [10, 11, 1]]) == [True, False, False, True, False, False, False, True, False, False, True, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1, 2], [0, 2, 4], [1, 3, 3], [1, 4, 1], [2, 4, 2], [2, 5, 5], [3, 6, 2], [4, 6, 1], [4, 7, 4], [5, 8, 3], [6, 9, 2], [7, 10, 1], [8, 10, 3], [9, 11, 2], [10, 11, 1]]) == [True, False, False, True, False, False, False, True, False, False, True, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 2, 4], [1, 3, 5], [2, 4, 6], [2, 5, 7], [3, 4, 8], [3, 5, 9], [4, 6, 10], [5, 6, 11]]) == [False, True, False, False, False, True, False, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 2, 4], [1, 3, 5], [2, 4, 6], [2, 5, 7], [3, 4, 8], [3, 5, 9], [4, 6, 10], [5, 6, 11]]) == [False, True, False, False, False, True, False, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [2, 3, 1], [3, 4, 4], [4, 5, 2], [5, 6, 1], [2, 4, 6], [0, 5, 7], [1, 6, 8]]) == [False, False, False, False, False, False, True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [2, 3, 1], [3, 4, 4], [4, 5, 2], [5, 6, 1], [2, 4, 6], [0, 5, 7], [1, 6, 8]]) == [False, False, False, False, False, False, True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 4], [1, 5, 5], [2, 6, 6], [2, 7, 7], [3, 8, 8], [4, 5, 9], [4, 6, 10], [5, 7, 11], [6, 8, 12], [7, 8, 13]]) == [False, False, True, False, False, False, False, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 4], [1, 5, 5], [2, 6, 6], [2, 7, 7], [3, 8, 8], [4, 5, 9], [4, 6, 10], [5, 7, 11], [6, 8, 12], [7, 8, 13]]) == [False, False, True, False, False, False, False, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 6], [2, 5, 4], [2, 6, 2], [3, 7, 3], [4, 8, 1], [5, 8, 3], [6, 9, 5], [7, 9, 2], [8, 9, 4]]) == [False, True, False, False, False, True, False, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 6], [2, 5, 4], [2, 6, 2], [3, 7, 3], [4, 8, 1], [5, 8, 3], [6, 9, 5], [7, 9, 2], [8, 9, 4]]) == [False, True, False, False, False, True, False, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 2], [1, 4, 1], [2, 3, 3], [2, 4, 7], [3, 5, 1], [4, 6, 4], [5, 7, 2], [6, 7, 1]]) == [False, True, False, False, True, False, True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 2], [1, 4, 1], [2, 3, 3], [2, 4, 7], [3, 5, 1], [4, 6, 4], [5, 7, 2], [6, 7, 1]]) == [False, True, False, False, True, False, True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 10], [0, 2, 20], [1, 3, 5], [1, 4, 15], [2, 3, 20], [2, 5, 10], [3, 6, 15], [4, 6, 5], [5, 7, 5], [6, 7, 10]]) == [False, True, False, False, False, True, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 10], [0, 2, 20], [1, 3, 5], [1, 4, 15], [2, 3, 20], [2, 5, 10], [3, 6, 15], [4, 6, 5], [5, 7, 5], [6, 7, 10]]) == [False, True, False, False, False, True, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 3], [0, 2, 1], [1, 3, 2], [1, 4, 4], [2, 5, 2], [3, 6, 1], [4, 6, 1], [5, 7, 2], [6, 8, 3], [7, 9, 1], [8, 9, 2]]) == [False, True, False, False, True, False, False, True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 3], [0, 2, 1], [1, 3, 2], [1, 4, 4], [2, 5, 2], [3, 6, 1], [4, 6, 1], [5, 7, 2], [6, 8, 3], [7, 9, 1], [8, 9, 2]]) == [False, True, False, False, True, False, False, True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 2], [3, 6, 5], [4, 7, 1], [5, 8, 3], [6, 9, 4], [7, 10, 2], [8, 11, 1], [9, 12, 3], [10, 13, 4], [11, 14, 2], [12, 14, 5]]) == [False, True, False, False, True, False, False, True, False, False, True, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 2], [3, 6, 5], [4, 7, 1], [5, 8, 3], [6, 9, 4], [7, 10, 2], [8, 11, 1], [9, 12, 3], [10, 13, 4], [11, 14, 2], [12, 14, 5]]) == [False, True, False, False, True, False, False, True, False, False, True, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 2, 2], [1, 3, 6], [2, 3, 4], [2, 4, 3], [3, 4, 1], [3, 5, 2], [4, 5, 3], [4, 6, 4], [5, 6, 2]]) == [False, True, False, False, False, True, False, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 2, 2], [1, 3, 6], [2, 3, 4], [2, 4, 3], [3, 4, 1], [3, 5, 2], [4, 5, 3], [4, 6, 4], [5, 6, 2]]) == [False, True, False, False, False, True, False, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 5], [0, 2, 10], [1, 3, 2], [1, 4, 3], [2, 3, 1], [2, 5, 4], [3, 6, 3], [4, 6, 2], [5, 6, 1], [6, 7, 5]]) == [True, False, True, True, False, False, True, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 5], [0, 2, 10], [1, 3, 2], [1, 4, 3], [2, 3, 1], [2, 5, 4], [3, 6, 3], [4, 6, 2], [5, 6, 1], [6, 7, 5]]) == [True, False, True, True, False, False, True, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 4], [1, 4, 2], [2, 5, 1], [2, 6, 3], [3, 7, 2], [3, 8, 4], [4, 9, 2], [5, 10, 3], [5, 11, 1], [6, 12, 4], [6, 13, 1], [7, 14, 2], [7, 15, 3], [8, 16, 1], [8, 17, 4], [9, 18, 2], [10, 19, 3], [11, 12, 2], [13, 14, 1], [15, 16, 2], [17, 18, 3], [18, 19, 4]]) == [False, True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 4], [1, 4, 2], [2, 5, 1], [2, 6, 3], [3, 7, 2], [3, 8, 4], [4, 9, 2], [5, 10, 3], [5, 11, 1], [6, 12, 4], [6, 13, 1], [7, 14, 2], [7, 15, 3], [8, 16, 1], [8, 17, 4], [9, 18, 2], [10, 19, 3], [11, 12, 2], [13, 14, 1], [15, 16, 2], [17, 18, 3], [18, 19, 4]]) == [False, True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [2, 5, 2], [3, 6, 3], [4, 7, 1], [5, 8, 2], [6, 9, 3], [7, 8, 1], [7, 9, 2], [8, 9, 3]]) == [True, False, False, True, False, False, True, False, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [2, 5, 2], [3, 6, 3], [4, 7, 1], [5, 8, 2], [6, 9, 3], [7, 8, 1], [7, 9, 2], [8, 9, 3]]) == [True, False, False, True, False, False, True, False, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [1, 4, 5], [2, 5, 2], [2, 6, 3], [3, 6, 1], [3, 7, 4], [4, 8, 2], [4, 9, 3], [5, 9, 1], [5, 10, 2], [6, 10, 3], [7, 8, 1], [8, 9, 2], [8, 10, 1], [9, 10, 2]]) == [True, True, True, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [1, 4, 5], [2, 5, 2], [2, 6, 3], [3, 6, 1], [3, 7, 4], [4, 8, 2], [4, 9, 3], [5, 9, 1], [5, 10, 2], [6, 10, 3], [7, 8, 1], [8, 9, 2], [8, 10, 1], [9, 10, 2]]) == [True, True, True, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 3, 6], [2, 4, 7], [3, 5, 8], [4, 5, 9], [5, 6, 10], [5, 7, 11], [5, 8, 12], [6, 9, 13], [7, 10, 14], [8, 11, 15], [9, 10, 16], [10, 11, 17]]) == [True, False, True, False, False, False, True, False, False, False, True, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 3, 6], [2, 4, 7], [3, 5, 8], [4, 5, 9], [5, 6, 10], [5, 7, 11], [5, 8, 12], [6, 9, 13], [7, 10, 14], [8, 11, 15], [9, 10, 16], [10, 11, 17]]) == [True, False, True, False, False, False, True, False, False, False, True, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 5], [2, 6, 6], [3, 7, 7], [4, 8, 8], [5, 9, 9], [6, 9, 9], [7, 8, 10]]) == [False, True, False, False, True, False, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 5], [2, 6, 6], [3, 7, 7], [4, 8, 8], [5, 9, 9], [6, 9, 9], [7, 8, 10]]) == [False, True, False, False, True, False, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [2, 4, 1], [3, 4, 1], [4, 5, 2], [5, 6, 1], [6, 7, 2], [4, 7, 3]]) == [True, False, False, True, False, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [2, 4, 1], [3, 4, 1], [4, 5, 2], [5, 6, 1], [6, 7, 2], [4, 7, 3]]) == [True, False, False, True, False, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 4, 1], [2, 6, 1], [3, 5, 1], [3, 7, 1], [4, 8, 1], [5, 8, 1], [6, 9, 1], [7, 9, 1], [8, 9, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [0, 7, 1], [0, 8, 1], [0, 9, 1]]) == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 4, 1], [2, 6, 1], [3, 5, 1], [3, 7, 1], [4, 8, 1], [5, 8, 1], [6, 9, 1], [7, 9, 1], [8, 9, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [0, 7, 1], [0, 8, 1], [0, 9, 1]]) == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1, 2], [0, 2, 4], [1, 3, 1], [1, 4, 3], [2, 5, 2], [2, 6, 4], [3, 7, 1], [4, 8, 1], [5, 9, 2], [6, 10, 1], [7, 11, 3], [8, 12, 2], [9, 13, 3], [10, 14, 1], [11, 15, 2], [12, 16, 1], [13, 17, 3], [14, 18, 2], [15, 19, 1], [16, 18, 2], [17, 19, 3]]) == [True, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1, 2], [0, 2, 4], [1, 3, 1], [1, 4, 3], [2, 5, 2], [2, 6, 4], [3, 7, 1], [4, 8, 1], [5, 9, 2], [6, 10, 1], [7, 11, 3], [8, 12, 2], [9, 13, 3], [10, 14, 1], [11, 15, 2], [12, 16, 1], [13, 17, 3], [14, 18, 2], [15, 19, 1], [16, 18, 2], [17, 19, 3]]) == [True, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 1], [0, 2, 2], [1, 2, 1], [1, 3, 3], [2, 3, 1], [2, 4, 2], [3, 4, 1], [3, 5, 3], [4, 5, 1], [4, 6, 2], [5, 6, 1]]) == [True, True, True, False, True, True, True, False, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 1], [0, 2, 2], [1, 2, 1], [1, 3, 3], [2, 3, 1], [2, 4, 2], [3, 4, 1], [3, 5, 3], [4, 5, 1], [4, 6, 2], [5, 6, 1]]) == [True, True, True, False, True, True, True, False, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 5, 1], [2, 5, 2], [3, 5, 3], [4, 5, 4], [5, 6, 5], [5, 7, 6], [5, 8, 7], [6, 8, 8], [7, 8, 9]]) == [True, False, False, False, True, False, False, False, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 5, 1], [2, 5, 2], [3, 5, 3], [4, 5, 4], [5, 6, 5], [5, 7, 6], [5, 8, 7], [6, 8, 8], [7, 8, 9]]) == [True, False, False, False, True, False, False, False, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7], [3, 7, 8], [3, 8, 9], [4, 8, 10], [4, 9, 11], [5, 10, 12], [5, 11, 13], [6, 10, 14], [6, 11, 15], [7, 11, 16], [8, 11, 17], [9, 11, 18]]) == [False, True, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7], [3, 7, 8], [3, 8, 9], [4, 8, 10], [4, 9, 11], [5, 10, 12], [5, 11, 13], [6, 10, 14], [6, 11, 15], [7, 11, 16], [8, 11, 17], [9, 11, 18]]) == [False, True, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [2, 4, 1], [3, 5, 4], [4, 6, 2], [5, 7, 3], [6, 8, 1], [7, 9, 2], [8, 9, 4]]) == [False, True, False, True, False, True, False, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [2, 4, 1], [3, 5, 4], [4, 6, 2], [5, 7, 3], [6, 8, 1], [7, 9, 2], [8, 9, 4]]) == [False, True, False, True, False, True, False, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 1], [1, 4, 4], [2, 5, 2], [3, 6, 3], [4, 7, 2], [5, 6, 1], [6, 7, 4]]) == [True, False, False, True, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 1], [1, 4, 4], [2, 5, 2], [3, 6, 3], [4, 7, 2], [5, 6, 1], [6, 7, 4]]) == [True, False, False, True, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,edges = [[0, 1, 2], [0, 2, 1], [0, 3, 3], [1, 4, 2], [1, 5, 4], [2, 4, 1], [2, 6, 3], [3, 7, 2], [3, 8, 1], [4, 5, 2], [5, 6, 3], [6, 7, 2], [7, 8, 1], [8, 5, 1]]) == [False, False, True, False, False, False, False, False, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,edges = [[0, 1, 2], [0, 2, 1], [0, 3, 3], [1, 4, 2], [1, 5, 4], [2, 4, 1], [2, 6, 3], [3, 7, 2], [3, 8, 1], [4, 5, 2], [5, 6, 3], [6, 7, 2], [7, 8, 1], [8, 5, 1]]) == [False, False, True, False, False, False, False, False, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 5, 2], [5, 6, 2], [6, 7, 2], [7, 8, 2], [8, 9, 2], [9, 10, 2], [10, 11, 2]]) == [True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 5, 2], [5, 6, 2], [6, 7, 2], [7, 8, 2], [8, 9, 2], [9, 10, 2], [10, 11, 2]]) == [True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1, 3], [0, 2, 5], [0, 3, 4], [1, 4, 2], [1, 5, 6], [2, 4, 3], [2, 6, 4], [3, 7, 5], [3, 8, 7], [4, 9, 2], [5, 9, 1], [6, 9, 3], [7, 10, 2], [8, 10, 3], [9, 11, 2]]) == [True, False, False, True, False, False, False, False, False, True, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1, 3], [0, 2, 5], [0, 3, 4], [1, 4, 2], [1, 5, 6], [2, 4, 3], [2, 6, 4], [3, 7, 5], [3, 8, 7], [4, 9, 2], [5, 9, 1], [6, 9, 3], [7, 10, 2], [8, 10, 3], [9, 11, 2]]) == [True, False, False, True, False, False, False, False, False, True, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 4], [1, 4, 6], [2, 3, 3], [2, 4, 5], [3, 5, 2], [4, 5, 1], [5, 6, 7], [5, 7, 8], [6, 7, 9]]) == [False, True, False, False, True, False, True, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 4], [1, 4, 6], [2, 3, 3], [2, 4, 5], [3, 5, 2], [4, 5, 1], [5, 6, 7], [5, 7, 8], [6, 7, 9]]) == [False, True, False, False, True, False, True, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 1], [2, 4, 1], [2, 5, 4], [3, 6, 3], [4, 6, 2], [5, 6, 1]]) == [False, True, False, False, True, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 1], [2, 4, 1], [2, 5, 4], [3, 6, 3], [4, 6, 2], [5, 6, 1]]) == [False, True, False, False, True, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 5], [0, 2, 2], [1, 3, 3], [1, 4, 7], [2, 3, 1], [2, 4, 6], [3, 5, 4], [3, 6, 2], [4, 7, 5], [5, 8, 3], [6, 8, 2], [7, 9, 1], [8, 9, 4]]) == [False, True, False, False, True, False, False, True, False, False, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 5], [0, 2, 2], [1, 3, 3], [1, 4, 7], [2, 3, 1], [2, 4, 6], [3, 5, 4], [3, 6, 2], [4, 7, 5], [5, 8, 3], [6, 8, 2], [7, 9, 1], [8, 9, 4]]) == [False, True, False, False, True, False, False, True, False, False, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,edges = [[0, 1, 10], [0, 2, 20], [1, 2, 5], [1, 3, 15], [2, 3, 10], [2, 4, 20], [3, 4, 5], [3, 5, 15], [4, 5, 10], [4, 6, 20], [5, 6, 5], [5, 7, 15], [6, 7, 10], [6, 8, 20], [7, 8, 5], [7, 9, 15], [8, 9, 10], [8, 10, 20], [9, 10, 5], [9, 11, 15], [10, 11, 10], [10, 12, 20], [11, 12, 5], [11, 13, 15], [12, 13, 10], [12, 14, 20], [13, 14, 5], [14, 15, 10], [14, 16, 20], [15, 16, 5], [15, 17, 15], [16, 17, 10], [16, 18, 20], [17, 18, 5], [17, 19, 15], [18, 19, 10]]) == [True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, False, True, True, True, False, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,edges = [[0, 1, 10], [0, 2, 20], [1, 2, 5], [1, 3, 15], [2, 3, 10], [2, 4, 20], [3, 4, 5], [3, 5, 15], [4, 5, 10], [4, 6, 20], [5, 6, 5], [5, 7, 15], [6, 7, 10], [6, 8, 20], [7, 8, 5], [7, 9, 15], [8, 9, 10], [8, 10, 20], [9, 10, 5], [9, 11, 15], [10, 11, 10], [10, 12, 20], [11, 12, 5], [11, 13, 15], [12, 13, 10], [12, 14, 20], [13, 14, 5], [14, 15, 10], [14, 16, 20], [15, 16, 5], [15, 17, 15], [16, 17, 10], [16, 18, 20], [17, 18, 5], [17, 19, 15], [18, 19, 10]]) == [True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, False, True, True, True, False, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 2], [2, 5, 1], [2, 6, 2], [3, 7, 1], [4, 7, 2], [5, 8, 1], [6, 8, 2], [7, 8, 1]]) == [True, True, True, False, True, False, True, False, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 2], [2, 5, 1], [2, 6, 2], [3, 7, 1], [4, 7, 2], [5, 8, 1], [6, 8, 2], [7, 8, 1]]) == [True, True, True, False, True, False, True, False, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 2], [1, 4, 8], [2, 5, 3], [3, 6, 4], [4, 7, 3], [5, 8, 2], [6, 9, 5], [7, 10, 4], [8, 11, 3], [9, 11, 2]]) == [False, True, False, False, True, False, False, True, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 2], [1, 4, 8], [2, 5, 3], [3, 6, 4], [4, 7, 3], [5, 8, 2], [6, 9, 5], [7, 10, 4], [8, 11, 3], [9, 11, 2]]) == [False, True, False, False, True, False, False, True, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 10, 10], [10, 11, 11], [11, 12, 12], [12, 13, 13], [13, 14, 14], [14, 15, 15], [15, 16, 16], [16, 17, 17], [17, 18, 18], [18, 19, 19], [19, 20, 20], [20, 21, 21], [21, 22, 22], [22, 23, 23], [23, 24, 24], [24, 25, 25], [25, 26, 26], [26, 27, 27], [27, 28, 28], [28, 29, 29], [0, 29, 100]]) == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 10, 10], [10, 11, 11], [11, 12, 12], [12, 13, 13], [13, 14, 14], [14, 15, 15], [15, 16, 16], [16, 17, 17], [17, 18, 18], [18, 19, 19], [19, 20, 20], [20, 21, 21], [21, 22, 22], [22, 23, 23], [23, 24, 24], [24, 25, 25], [25, 26, 26], [26, 27, 27], [27, 28, 28], [28, 29, 29], [0, 29, 100]]) == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [1, 4, 6], [2, 4, 5], [2, 5, 3], [3, 5, 1], [3, 6, 2], [4, 6, 3], [5, 6, 4]]) == [True, False, False, True, False, False, False, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [1, 4, 6], [2, 4, 5], [2, 5, 3], [3, 5, 1], [3, 6, 2], [4, 6, 3], [5, 6, 4]]) == [True, False, False, True, False, False, False, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 4], [0, 2, 3], [1, 3, 2], [1, 4, 5], [2, 5, 1], [3, 6, 3], [4, 6, 2], [5, 7, 4], [6, 7, 1], [0, 3, 6], [1, 2, 7]]) == [False, True, False, False, True, False, False, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 4], [0, 2, 3], [1, 3, 2], [1, 4, 5], [2, 5, 1], [3, 6, 3], [4, 6, 2], [5, 7, 4], [6, 7, 1], [0, 3, 6], [1, 2, 7]]) == [False, True, False, False, True, False, False, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 3], [2, 5, 2], [2, 6, 4], [3, 7, 1], [4, 8, 1], [5, 9, 2], [6, 10, 1], [7, 11, 3], [8, 12, 2], [9, 13, 3], [10, 14, 1], [11, 12, 2], [12, 13, 1], [13, 14, 2]]) == [False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 3], [2, 5, 2], [2, 6, 4], [3, 7, 1], [4, 8, 1], [5, 9, 2], [6, 10, 1], [7, 11, 3], [8, 12, 2], [9, 13, 3], [10, 14, 1], [11, 12, 2], [12, 13, 1], [13, 14, 2]]) == [False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1, 10], [0, 2, 15], [1, 2, 5], [1, 3, 20], [2, 3, 10], [2, 4, 15], [3, 4, 5], [3, 5, 25], [4, 5, 10], [4, 6, 15], [5, 6, 5], [5, 7, 20], [6, 7, 10], [6, 8, 15], [7, 8, 5], [7, 9, 25], [8, 9, 10], [8, 10, 15], [9, 10, 5], [9, 11, 20], [10, 11, 10], [10, 12, 15], [11, 12, 5], [11, 13, 20], [12, 13, 10], [12, 14, 15], [13, 14, 5]]) == [True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1, 10], [0, 2, 15], [1, 2, 5], [1, 3, 20], [2, 3, 10], [2, 4, 15], [3, 4, 5], [3, 5, 25], [4, 5, 10], [4, 6, 15], [5, 6, 5], [5, 7, 20], [6, 7, 10], [6, 8, 15], [7, 8, 5], [7, 9, 25], [8, 9, 10], [8, 10, 15], [9, 10, 5], [9, 11, 20], [10, 11, 10], [10, 12, 15], [11, 12, 5], [11, 13, 20], [12, 13, 10], [12, 14, 15], [13, 14, 5]]) == [True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 10], [0, 2, 5], [0, 3, 20], [1, 4, 2], [2, 4, 15], [2, 5, 1], [3, 6, 5], [4, 6, 10], [5, 6, 2]]) == [False, True, False, False, False, True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 10], [0, 2, 5], [0, 3, 20], [1, 4, 2], [2, 4, 15], [2, 5, 1], [3, 6, 5], [4, 6, 10], [5, 6, 2]]) == [False, True, False, False, False, True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 3, 1], [2, 4, 6], [3, 5, 7], [3, 6, 8], [4, 5, 9], [4, 6, 10], [5, 7, 11], [6, 7, 12]]) == [False, True, False, False, True, False, True, False, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 3, 1], [2, 4, 6], [3, 5, 7], [3, 6, 8], [4, 5, 9], [4, 6, 10], [5, 7, 11], [6, 7, 12]]) == [False, True, False, False, True, False, True, False, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 2, 2], [1, 3, 6], [2, 3, 1], [2, 4, 4], [3, 4, 2], [3, 5, 3], [4, 5, 1], [5, 6, 2], [6, 7, 3], [7, 8, 4], [8, 9, 5], [6, 9, 7]]) == [False, True, False, False, True, False, True, True, True, True, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 2, 2], [1, 3, 6], [2, 3, 1], [2, 4, 4], [3, 4, 2], [3, 5, 3], [4, 5, 1], [5, 6, 2], [6, 7, 3], [7, 8, 4], [8, 9, 5], [6, 9, 7]]) == [False, True, False, False, True, False, True, True, True, True, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1, 1], [0, 2, 4], [1, 2, 2], [1, 3, 5], [2, 3, 1], [2, 4, 2], [3, 4, 3], [3, 5, 6], [4, 5, 1], [4, 6, 4], [5, 6, 2], [5, 7, 3], [6, 7, 1]]) == [True, False, True, False, False, True, False, False, True, False, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1, 1], [0, 2, 4], [1, 2, 2], [1, 3, 5], [2, 3, 1], [2, 4, 2], [3, 4, 3], [3, 5, 6], [4, 5, 1], [4, 6, 4], [5, 6, 2], [5, 7, 3], [6, 7, 1]]) == [True, False, True, False, False, True, False, False, True, False, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [1, 5, 2], [2, 6, 1], [2, 7, 2], [3, 8, 1], [3, 9, 2], [4, 10, 1], [5, 11, 1], [6, 12, 1], [7, 13, 1], [8, 14, 1], [9, 14, 2], [10, 11, 1], [11, 12, 1], [12, 13, 1], [13, 14, 1]]) == [False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [1, 5, 2], [2, 6, 1], [2, 7, 2], [3, 8, 1], [3, 9, 2], [4, 10, 1], [5, 11, 1], [6, 12, 1], [7, 13, 1], [8, 14, 1], [9, 14, 2], [10, 11, 1], [11, 12, 1], [12, 13, 1], [13, 14, 1]]) == [False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 1], [2, 4, 2], [2, 5, 2], [3, 6, 1], [4, 6, 1], [4, 7, 1], [5, 8, 2], [6, 9, 1], [7, 9, 1], [8, 10, 2], [9, 11, 1], [10, 12, 1], [11, 13, 2], [12, 13, 1], [13, 14, 1]]) == [True, False, True, True, False, False, True, True, True, False, True, True, False, True, False, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 1], [2, 4, 2], [2, 5, 2], [3, 6, 1], [4, 6, 1], [4, 7, 1], [5, 8, 2], [6, 9, 1], [7, 9, 1], [8, 10, 2], [9, 11, 1], [10, 12, 1], [11, 13, 2], [12, 13, 1], [13, 14, 1]]) == [True, False, True, True, False, False, True, True, True, False, True, True, False, True, False, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1, 5], [0, 2, 10], [1, 3, 3], [1, 4, 7], [2, 3, 2], [2, 5, 8], [3, 4, 1], [3, 6, 4], [4, 7, 6], [5, 6, 1], [6, 7, 2], [6, 8, 3], [7, 9, 5], [8, 9, 1]]) == [True, False, True, False, False, False, False, True, False, False, False, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1, 5], [0, 2, 10], [1, 3, 3], [1, 4, 7], [2, 3, 2], [2, 5, 8], [3, 4, 1], [3, 6, 4], [4, 7, 6], [5, 6, 1], [6, 7, 2], [6, 8, 3], [7, 9, 5], [8, 9, 1]]) == [True, False, True, False, False, False, False, True, False, False, False, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 10], [2, 4, 10], [3, 4, 10], [4, 5, 10], [4, 6, 20], [5, 6, 10]]) == [True, False, False, True, False, False, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 10], [2, 4, 10], [3, 4, 10], [4, 5, 10], [4, 6, 20], [5, 6, 10]]) == [True, False, False, True, False, False, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 1], [2, 4, 2], [2, 5, 2], [3, 6, 4], [4, 6, 3], [4, 7, 2], [5, 8, 3], [6, 8, 2], [7, 8, 1]]) == [True, False, False, True, False, False, False, False, True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 1], [2, 4, 2], [2, 5, 2], [3, 6, 4], [4, 6, 3], [4, 7, 2], [5, 8, 3], [6, 8, 2], [7, 8, 1]]) == [True, False, False, True, False, False, False, False, True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1, 1], [0, 2, 1], [1, 3, 1], [1, 4, 1], [2, 3, 1], [2, 4, 1], [3, 5, 1], [4, 5, 1]]) == [True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1, 1], [0, 2, 1], [1, 3, 1], [1, 4, 1], [2, 3, 1], [2, 4, 1], [3, 5, 1], [4, 5, 1]]) == [True, True, True, True, True, True, True, True]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 5,edges = [[0, 1, 2], [0, 2, 2], [1, 2, 3], [1, 3, 2], [2, 3, 1], [2, 4, 4], [3, 4, 2]]) == [False, True, False, False, True, False, True]
    assert candidate(n = 7,edges = [[0, 1, 2], [0, 2, 5], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 1], [4, 5, 3], [5, 6, 2]]) == [True, False, True, False, True, True, True, True]
    assert candidate(n = 5,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 1]]) == [True, True, True, False, True, True]
    assert candidate(n = 10,edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 6, 1], [2, 7, 1], [3, 8, 1], [3, 9, 1], [4, 5, 1], [6, 7, 1], [8, 9, 1]]) == [False, False, True, False, False, False, False, False, True, False, False, False]
    assert candidate(n = 7,edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 4, 1], [4, 5, 2], [5, 6, 3]]) == [True, True, True, True, True, True]
    assert candidate(n = 5,edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [0, 4, 10]]) == [True, True, True, True, True]
    assert candidate(n = 3,edges = [[0, 1, 1], [0, 2, 5], [1, 2, 2]]) == [True, False, True]
    assert candidate(n = 4,edges = [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]]) == [True, False, False, True]
    assert candidate(n = 6,edges = [[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3], [4, 5, 2]]) == [True, True, True, False, True, True, True, False]
    assert candidate(n = 3,edges = [[0, 1, 1], [1, 2, 1], [0, 2, 4]]) == [True, True, False]
    assert candidate(n = 15,edges = [[0, 1, 1], [0, 2, 1], [1, 3, 1], [1, 4, 1], [2, 5, 1], [2, 6, 1], [3, 7, 1], [3, 8, 1], [4, 9, 1], [4, 10, 1], [5, 11, 1], [5, 12, 1], [6, 13, 1], [6, 14, 1], [7, 8, 1], [9, 10, 1], [11, 12, 1], [13, 14, 1]]) == [False, True, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False]
    assert candidate(n = 25,edges = [[0, 1, 5], [0, 2, 5], [1, 3, 3], [1, 4, 2], [2, 5, 3], [2, 6, 4], [3, 7, 1], [3, 8, 2], [4, 9, 1], [5, 10, 2], [5, 11, 3], [6, 12, 1], [6, 13, 4], [7, 14, 1], [7, 15, 2], [8, 16, 1], [8, 17, 2], [9, 18, 2], [10, 19, 1], [10, 20, 2], [11, 21, 2], [11, 22, 1], [12, 23, 1], [12, 24, 2], [13, 23, 2], [13, 24, 3]]) == [False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False]
    assert candidate(n = 10,edges = [[0, 1, 5], [0, 2, 2], [1, 3, 1], [1, 4, 6], [2, 5, 3], [3, 6, 2], [4, 7, 4], [5, 8, 5], [6, 9, 1], [7, 9, 3], [8, 9, 2]]) == [True, False, True, False, False, True, False, False, True, False, False]
    assert candidate(n = 15,edges = [[0, 1, 10], [0, 2, 20], [1, 3, 5], [1, 4, 10], [2, 5, 15], [3, 6, 20], [4, 7, 25], [5, 8, 30], [6, 9, 35], [7, 10, 40], [8, 11, 45], [9, 12, 50], [10, 13, 55], [11, 14, 60], [0, 6, 65], [1, 7, 70], [2, 8, 75], [3, 9, 80], [4, 10, 85], [5, 11, 90], [6, 12, 95], [7, 13, 100], [8, 14, 105]]) == [False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True]
    assert candidate(n = 12,edges = [[0, 1, 3], [0, 2, 2], [1, 3, 1], [2, 4, 4], [3, 5, 2], [4, 6, 3], [5, 7, 1], [6, 8, 5], [7, 9, 2], [8, 10, 1], [9, 11, 3], [10, 11, 2], [0, 5, 7], [1, 6, 8], [2, 7, 9], [3, 8, 10], [4, 9, 11]]) == [True, False, True, False, True, False, True, False, True, False, True, False, False, False, False, False, False]
    assert candidate(n = 10,edges = [[0, 1, 2], [1, 2, 2], [2, 3, 1], [3, 4, 3], [4, 5, 2], [5, 6, 1], [6, 7, 2], [7, 8, 3], [8, 9, 2], [0, 9, 10]]) == [False, False, False, False, False, False, False, False, False, True]
    assert candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 2], [2, 5, 3], [2, 6, 4], [3, 7, 2], [3, 8, 3], [4, 9, 1], [4, 10, 4], [5, 11, 2], [5, 12, 3], [6, 13, 4], [6, 14, 5], [7, 8, 1], [9, 10, 2], [11, 12, 3], [13, 14, 4]]) == [False, True, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False]
    assert candidate(n = 10,edges = [[0, 1, 2], [0, 2, 4], [0, 3, 1], [1, 4, 3], [1, 5, 1], [2, 3, 2], [2, 6, 5], [3, 7, 1], [4, 8, 2], [5, 8, 3], [6, 9, 4], [7, 9, 3], [8, 9, 1]]) == [False, False, True, False, False, False, False, True, False, False, False, True, False]
    assert candidate(n = 7,edges = [[0, 1, 5], [0, 2, 10], [1, 2, 1], [1, 3, 4], [2, 3, 2], [3, 4, 3], [4, 5, 2], [5, 6, 1], [6, 0, 3]]) == [False, False, False, False, False, False, False, False, True]
    assert candidate(n = 12,edges = [[0, 1, 2], [0, 2, 4], [1, 3, 3], [1, 4, 1], [2, 4, 2], [2, 5, 5], [3, 6, 2], [4, 6, 1], [4, 7, 4], [5, 8, 3], [6, 9, 2], [7, 10, 1], [8, 10, 3], [9, 11, 2], [10, 11, 1]]) == [True, False, False, True, False, False, False, True, False, False, True, False, False, True, False]
    assert candidate(n = 7,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 2, 4], [1, 3, 5], [2, 4, 6], [2, 5, 7], [3, 4, 8], [3, 5, 9], [4, 6, 10], [5, 6, 11]]) == [False, True, False, False, False, True, False, False, False, True, False]
    assert candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [2, 3, 1], [3, 4, 4], [4, 5, 2], [5, 6, 1], [2, 4, 6], [0, 5, 7], [1, 6, 8]]) == [False, False, False, False, False, False, True, False, True, False]
    assert candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 4], [1, 5, 5], [2, 6, 6], [2, 7, 7], [3, 8, 8], [4, 5, 9], [4, 6, 10], [5, 7, 11], [6, 8, 12], [7, 8, 13]]) == [False, False, True, False, False, False, False, True, False, False, False, False, False]
    assert candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 6], [2, 5, 4], [2, 6, 2], [3, 7, 3], [4, 8, 1], [5, 8, 3], [6, 9, 5], [7, 9, 2], [8, 9, 4]]) == [False, True, False, False, False, True, False, False, False, True, False, False]
    assert candidate(n = 8,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 2], [1, 4, 1], [2, 3, 3], [2, 4, 7], [3, 5, 1], [4, 6, 4], [5, 7, 2], [6, 7, 1]]) == [False, True, False, False, True, False, True, False, True, False]
    assert candidate(n = 8,edges = [[0, 1, 10], [0, 2, 20], [1, 3, 5], [1, 4, 15], [2, 3, 20], [2, 5, 10], [3, 6, 15], [4, 6, 5], [5, 7, 5], [6, 7, 10]]) == [False, True, False, False, False, True, False, False, True, False]
    assert candidate(n = 10,edges = [[0, 1, 3], [0, 2, 1], [1, 3, 2], [1, 4, 4], [2, 5, 2], [3, 6, 1], [4, 6, 1], [5, 7, 2], [6, 8, 3], [7, 9, 1], [8, 9, 2]]) == [False, True, False, False, True, False, False, True, False, True, False]
    assert candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 2], [3, 6, 5], [4, 7, 1], [5, 8, 3], [6, 9, 4], [7, 10, 2], [8, 11, 1], [9, 12, 3], [10, 13, 4], [11, 14, 2], [12, 14, 5]]) == [False, True, False, False, True, False, False, True, False, False, True, False, False, True, False]
    assert candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 2, 2], [1, 3, 6], [2, 3, 4], [2, 4, 3], [3, 4, 1], [3, 5, 2], [4, 5, 3], [4, 6, 4], [5, 6, 2]]) == [False, True, False, False, False, True, False, False, False, True, False]
    assert candidate(n = 8,edges = [[0, 1, 5], [0, 2, 10], [1, 3, 2], [1, 4, 3], [2, 3, 1], [2, 5, 4], [3, 6, 3], [4, 6, 2], [5, 6, 1], [6, 7, 5]]) == [True, False, True, True, False, False, True, True, False, True]
    assert candidate(n = 20,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 4], [1, 4, 2], [2, 5, 1], [2, 6, 3], [3, 7, 2], [3, 8, 4], [4, 9, 2], [5, 10, 3], [5, 11, 1], [6, 12, 4], [6, 13, 1], [7, 14, 2], [7, 15, 3], [8, 16, 1], [8, 17, 4], [9, 18, 2], [10, 19, 3], [11, 12, 2], [13, 14, 1], [15, 16, 2], [17, 18, 3], [18, 19, 4]]) == [False, True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False]
    assert candidate(n = 10,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [2, 5, 2], [3, 6, 3], [4, 7, 1], [5, 8, 2], [6, 9, 3], [7, 8, 1], [7, 9, 2], [8, 9, 3]]) == [True, False, False, True, False, False, True, False, False, False, True, False]
    assert candidate(n = 11,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [1, 4, 5], [2, 5, 2], [2, 6, 3], [3, 6, 1], [3, 7, 4], [4, 8, 2], [4, 9, 3], [5, 9, 1], [5, 10, 2], [6, 10, 3], [7, 8, 1], [8, 9, 2], [8, 10, 1], [9, 10, 2]]) == [True, True, True, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False]
    assert candidate(n = 12,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 3, 6], [2, 4, 7], [3, 5, 8], [4, 5, 9], [5, 6, 10], [5, 7, 11], [5, 8, 12], [6, 9, 13], [7, 10, 14], [8, 11, 15], [9, 10, 16], [10, 11, 17]]) == [True, False, True, False, False, False, True, False, False, False, True, False, False, True, False, False]
    assert candidate(n = 10,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 5], [2, 6, 6], [3, 7, 7], [4, 8, 8], [5, 9, 9], [6, 9, 9], [7, 8, 10]]) == [False, True, False, False, True, False, False, False, True, False, False]
    assert candidate(n = 8,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [2, 4, 1], [3, 4, 1], [4, 5, 2], [5, 6, 1], [6, 7, 2], [4, 7, 3]]) == [True, False, False, True, False, False, False, False, False, True]
    assert candidate(n = 10,edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 4, 1], [2, 6, 1], [3, 5, 1], [3, 7, 1], [4, 8, 1], [5, 8, 1], [6, 9, 1], [7, 9, 1], [8, 9, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [0, 7, 1], [0, 8, 1], [0, 9, 1]]) == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]
    assert candidate(n = 20,edges = [[0, 1, 2], [0, 2, 4], [1, 3, 1], [1, 4, 3], [2, 5, 2], [2, 6, 4], [3, 7, 1], [4, 8, 1], [5, 9, 2], [6, 10, 1], [7, 11, 3], [8, 12, 2], [9, 13, 3], [10, 14, 1], [11, 15, 2], [12, 16, 1], [13, 17, 3], [14, 18, 2], [15, 19, 1], [16, 18, 2], [17, 19, 3]]) == [True, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False]
    assert candidate(n = 7,edges = [[0, 1, 1], [0, 2, 2], [1, 2, 1], [1, 3, 3], [2, 3, 1], [2, 4, 2], [3, 4, 1], [3, 5, 3], [4, 5, 1], [4, 6, 2], [5, 6, 1]]) == [True, True, True, False, True, True, True, False, True, True, True]
    assert candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 5, 1], [2, 5, 2], [3, 5, 3], [4, 5, 4], [5, 6, 5], [5, 7, 6], [5, 8, 7], [6, 8, 8], [7, 8, 9]]) == [True, False, False, False, True, False, False, False, False, False, True, False, False]
    assert candidate(n = 12,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7], [3, 7, 8], [3, 8, 9], [4, 8, 10], [4, 9, 11], [5, 10, 12], [5, 11, 13], [6, 10, 14], [6, 11, 15], [7, 11, 16], [8, 11, 17], [9, 11, 18]]) == [False, True, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False]
    assert candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [2, 4, 1], [3, 5, 4], [4, 6, 2], [5, 7, 3], [6, 8, 1], [7, 9, 2], [8, 9, 4]]) == [False, True, False, True, False, True, False, True, False, True]
    assert candidate(n = 8,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 1], [1, 4, 4], [2, 5, 2], [3, 6, 3], [4, 7, 2], [5, 6, 1], [6, 7, 4]]) == [True, False, False, True, False, False, True, False, False]
    assert candidate(n = 9,edges = [[0, 1, 2], [0, 2, 1], [0, 3, 3], [1, 4, 2], [1, 5, 4], [2, 4, 1], [2, 6, 3], [3, 7, 2], [3, 8, 1], [4, 5, 2], [5, 6, 3], [6, 7, 2], [7, 8, 1], [8, 5, 1]]) == [False, False, True, False, False, False, False, False, True, False, False, False, False, False]
    assert candidate(n = 12,edges = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 5, 2], [5, 6, 2], [6, 7, 2], [7, 8, 2], [8, 9, 2], [9, 10, 2], [10, 11, 2]]) == [True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(n = 12,edges = [[0, 1, 3], [0, 2, 5], [0, 3, 4], [1, 4, 2], [1, 5, 6], [2, 4, 3], [2, 6, 4], [3, 7, 5], [3, 8, 7], [4, 9, 2], [5, 9, 1], [6, 9, 3], [7, 10, 2], [8, 10, 3], [9, 11, 2]]) == [True, False, False, True, False, False, False, False, False, True, False, False, False, False, True]
    assert candidate(n = 8,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 4], [1, 4, 6], [2, 3, 3], [2, 4, 5], [3, 5, 2], [4, 5, 1], [5, 6, 7], [5, 7, 8], [6, 7, 9]]) == [False, True, False, False, True, False, True, False, False, True, False]
    assert candidate(n = 7,edges = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [1, 4, 1], [2, 4, 1], [2, 5, 4], [3, 6, 3], [4, 6, 2], [5, 6, 1]]) == [False, True, False, False, True, False, False, True, False]
    assert candidate(n = 10,edges = [[0, 1, 5], [0, 2, 2], [1, 3, 3], [1, 4, 7], [2, 3, 1], [2, 4, 6], [3, 5, 4], [3, 6, 2], [4, 7, 5], [5, 8, 3], [6, 8, 2], [7, 9, 1], [8, 9, 4]]) == [False, True, False, False, True, False, False, True, False, False, True, False, True]
    assert candidate(n = 20,edges = [[0, 1, 10], [0, 2, 20], [1, 2, 5], [1, 3, 15], [2, 3, 10], [2, 4, 20], [3, 4, 5], [3, 5, 15], [4, 5, 10], [4, 6, 20], [5, 6, 5], [5, 7, 15], [6, 7, 10], [6, 8, 20], [7, 8, 5], [7, 9, 15], [8, 9, 10], [8, 10, 20], [9, 10, 5], [9, 11, 15], [10, 11, 10], [10, 12, 20], [11, 12, 5], [11, 13, 15], [12, 13, 10], [12, 14, 20], [13, 14, 5], [14, 15, 10], [14, 16, 20], [15, 16, 5], [15, 17, 15], [16, 17, 10], [16, 18, 20], [17, 18, 5], [17, 19, 15], [18, 19, 10]]) == [True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, False, True, True, True, False, True, True, True]
    assert candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 2], [2, 5, 1], [2, 6, 2], [3, 7, 1], [4, 7, 2], [5, 8, 1], [6, 8, 2], [7, 8, 1]]) == [True, True, True, False, True, False, True, False, True, False, True]
    assert candidate(n = 12,edges = [[0, 1, 10], [0, 2, 5], [1, 3, 2], [1, 4, 8], [2, 5, 3], [3, 6, 4], [4, 7, 3], [5, 8, 2], [6, 9, 5], [7, 10, 4], [8, 11, 3], [9, 11, 2]]) == [False, True, False, False, True, False, False, True, False, False, True, False]
    assert candidate(n = 30,edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 10, 10], [10, 11, 11], [11, 12, 12], [12, 13, 13], [13, 14, 14], [14, 15, 15], [15, 16, 16], [16, 17, 17], [17, 18, 18], [18, 19, 19], [19, 20, 20], [20, 21, 21], [21, 22, 22], [22, 23, 23], [23, 24, 24], [24, 25, 25], [25, 26, 26], [26, 27, 27], [27, 28, 28], [28, 29, 29], [0, 29, 100]]) == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]
    assert candidate(n = 7,edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [1, 4, 6], [2, 4, 5], [2, 5, 3], [3, 5, 1], [3, 6, 2], [4, 6, 3], [5, 6, 4]]) == [True, False, False, True, False, False, False, False, True, False, False]
    assert candidate(n = 8,edges = [[0, 1, 4], [0, 2, 3], [1, 3, 2], [1, 4, 5], [2, 5, 1], [3, 6, 3], [4, 6, 2], [5, 7, 4], [6, 7, 1], [0, 3, 6], [1, 2, 7]]) == [False, True, False, False, True, False, False, True, False, False, False]
    assert candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 3], [2, 5, 2], [2, 6, 4], [3, 7, 1], [4, 8, 1], [5, 9, 2], [6, 10, 1], [7, 11, 3], [8, 12, 2], [9, 13, 3], [10, 14, 1], [11, 12, 2], [12, 13, 1], [13, 14, 2]]) == [False, True, False, False, False, True, False, False, False, True, False, False, False, True, False, False, False]
    assert candidate(n = 15,edges = [[0, 1, 10], [0, 2, 15], [1, 2, 5], [1, 3, 20], [2, 3, 10], [2, 4, 15], [3, 4, 5], [3, 5, 25], [4, 5, 10], [4, 6, 15], [5, 6, 5], [5, 7, 20], [6, 7, 10], [6, 8, 15], [7, 8, 5], [7, 9, 25], [8, 9, 10], [8, 10, 15], [9, 10, 5], [9, 11, 20], [10, 11, 10], [10, 12, 15], [11, 12, 5], [11, 13, 20], [12, 13, 10], [12, 14, 15], [13, 14, 5]]) == [True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True]
    assert candidate(n = 7,edges = [[0, 1, 10], [0, 2, 5], [0, 3, 20], [1, 4, 2], [2, 4, 15], [2, 5, 1], [3, 6, 5], [4, 6, 10], [5, 6, 2]]) == [False, True, False, False, False, True, False, False, True]
    assert candidate(n = 8,edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 3, 1], [2, 4, 6], [3, 5, 7], [3, 6, 8], [4, 5, 9], [4, 6, 10], [5, 7, 11], [6, 7, 12]]) == [False, True, False, False, True, False, True, False, False, False, True, False]
    assert candidate(n = 10,edges = [[0, 1, 5], [0, 2, 3], [1, 2, 2], [1, 3, 6], [2, 3, 1], [2, 4, 4], [3, 4, 2], [3, 5, 3], [4, 5, 1], [5, 6, 2], [6, 7, 3], [7, 8, 4], [8, 9, 5], [6, 9, 7]]) == [False, True, False, False, True, False, True, True, True, True, False, False, False, True]
    assert candidate(n = 8,edges = [[0, 1, 1], [0, 2, 4], [1, 2, 2], [1, 3, 5], [2, 3, 1], [2, 4, 2], [3, 4, 3], [3, 5, 6], [4, 5, 1], [4, 6, 4], [5, 6, 2], [5, 7, 3], [6, 7, 1]]) == [True, False, True, False, False, True, False, False, True, False, True, True, True]
    assert candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 1], [1, 5, 2], [2, 6, 1], [2, 7, 2], [3, 8, 1], [3, 9, 2], [4, 10, 1], [5, 11, 1], [6, 12, 1], [7, 13, 1], [8, 14, 1], [9, 14, 2], [10, 11, 1], [11, 12, 1], [12, 13, 1], [13, 14, 1]]) == [False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False]
    assert candidate(n = 15,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 1], [1, 4, 1], [2, 4, 2], [2, 5, 2], [3, 6, 1], [4, 6, 1], [4, 7, 1], [5, 8, 2], [6, 9, 1], [7, 9, 1], [8, 10, 2], [9, 11, 1], [10, 12, 1], [11, 13, 2], [12, 13, 1], [13, 14, 1]]) == [True, False, True, True, False, False, True, True, True, False, True, True, False, True, False, True, False, True]
    assert candidate(n = 10,edges = [[0, 1, 5], [0, 2, 10], [1, 3, 3], [1, 4, 7], [2, 3, 2], [2, 5, 8], [3, 4, 1], [3, 6, 4], [4, 7, 6], [5, 6, 1], [6, 7, 2], [6, 8, 3], [7, 9, 5], [8, 9, 1]]) == [True, False, True, False, False, False, False, True, False, False, False, True, False, True]
    assert candidate(n = 7,edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 10], [2, 4, 10], [3, 4, 10], [4, 5, 10], [4, 6, 20], [5, 6, 10]]) == [True, False, False, True, False, False, True, True, True]
    assert candidate(n = 9,edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 1], [2, 4, 2], [2, 5, 2], [3, 6, 4], [4, 6, 3], [4, 7, 2], [5, 8, 3], [6, 8, 2], [7, 8, 1]]) == [True, False, False, True, False, False, False, False, True, False, False, True]
    assert candidate(n = 6,edges = [[0, 1, 1], [0, 2, 1], [1, 3, 1], [1, 4, 1], [2, 3, 1], [2, 4, 1], [3, 5, 1], [4, 5, 1]]) == [True, True, True, True, True, True, True, True]


