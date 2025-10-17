def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [0, 2]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [0, 2]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4]],queries = [[0, 3], [1, 4], [2, 3]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4]],queries = [[0, 3], [1, 4], [2, 3]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2]],queries = [[0, 2], [2, 0]]) == [True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2]],queries = [[0, 2], [2, 0]]) == [True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 2,prerequisites = [],queries = [[1, 0], [0, 1]]) == [False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 2,prerequisites = [],queries = [[1, 0], [0, 1]]) == [False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [3, 4]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [3, 4]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 4], [2, 3]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 4], [2, 3]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2], [1, 0], [2, 0]],queries = [[1, 0], [1, 2]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2], [1, 0], [2, 0]],queries = [[1, 0], [1, 2]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 2,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0]]) == [False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 2,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0]]) == [False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 2], [2, 0], [3, 0]]) == [True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 2], [2, 0], [3, 0]]) == [True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 5], [0, 4], [1, 2]]) == [True, True, True, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 5], [0, 4], [1, 2]]) == [True, True, True, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [1, 11], [1, 12], [2, 7], [2, 8]]) == [True, True, True, True, True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [1, 11], [1, 12], [2, 7], [2, 8]]) == [True, True, True, True, True, True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7]]) == [True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7]]) == [True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],queries = [[0, 7], [1, 5], [2, 4], [3, 6], [5, 7]]) == [True, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],queries = [[0, 7], [1, 5], [2, 4], [3, 6], [5, 7]]) == [True, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4]]) == [True, True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4]]) == [True, True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 3], [1, 2]]) == [True, True, False, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 3], [1, 2]]) == [True, True, False, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 8], [4, 9], [5, 10], [5, 11], [6, 10], [6, 11], [7, 11], [8, 11], [9, 11]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 10], [1, 11], [2, 10], [2, 11], [3, 11], [4, 11]]) == [True, True, True, True, True, False, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 8], [4, 9], [5, 10], [5, 11], [6, 10], [6, 11], [7, 11], [8, 11], [9, 11]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 10], [1, 11], [2, 10], [2, 11], [3, 11], [4, 11]]) == [True, True, True, True, True, False, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 7], [4, 8]],queries = [[0, 7], [0, 8], [1, 7], [1, 8], [2, 7], [2, 8], [0, 3], [0, 4]]) == [True, True, True, True, False, False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 7], [4, 8]],queries = [[0, 7], [0, 8], [1, 7], [1, 8], [2, 7], [2, 8], [0, 3], [0, 4]]) == [True, True, True, True, False, False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == [True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == [True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 7], [5, 7], [6, 8]],queries = [[0, 7], [0, 8], [1, 5], [1, 6], [2, 7], [2, 8], [3, 7], [3, 8], [4, 7], [5, 7], [6, 8]]) == [True, True, False, False, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 7], [5, 7], [6, 8]],queries = [[0, 7], [0, 8], [1, 5], [1, 6], [2, 7], [2, 8], [3, 7], [3, 8], [4, 7], [5, 7], [6, 8]]) == [True, True, False, False, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == [True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == [True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 5], [1, 2]]) == [True, False, False, True, False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 5], [1, 2]]) == [True, False, False, True, False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 6], [4, 6], [5, 6]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 5], [0, 4], [0, 3]]) == [True, True, True, True, True, True, False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 6], [4, 6], [5, 6]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 5], [0, 4], [0, 3]]) == [True, True, True, True, True, True, False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8]],queries = [[0, 3], [0, 7], [1, 8], [2, 6], [3, 5]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8]],queries = [[0, 3], [0, 7], [1, 8], [2, 6], [3, 5]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [0, 4], [1, 5], [2, 6], [3, 7], [4, 8]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4], [5, 3], [6, 2], [7, 1], [8, 0]]) == [True, True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [0, 4], [1, 5], [2, 6], [3, 7], [4, 8]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4], [5, 3], [6, 2], [7, 1], [8, 0]]) == [True, True, True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6]],queries = [[0, 3], [1, 5], [2, 6], [3, 6]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6]],queries = [[0, 3], [1, 5], [2, 6], [3, 6]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [2, 5], [4, 6], [5, 6]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 5]]) == [True, True, True, False, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [2, 5], [4, 6], [5, 6]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 5]]) == [True, True, True, False, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 3]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 3]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5]],queries = [[0, 5], [1, 4], [2, 4], [3, 5], [1, 3], [2, 3]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5]],queries = [[0, 5], [1, 4], [2, 4], [3, 5], [1, 3], [2, 3]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]],queries = [[0, 3], [0, 4], [0, 5], [1, 2], [1, 5], [2, 3], [2, 4]]) == [True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]],queries = [[0, 3], [0, 4], [0, 5], [1, 2], [1, 5], [2, 3], [2, 4]]) == [True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 5], [3, 6], [4, 6], [5, 6], [6, 7]],queries = [[0, 3], [0, 4], [0, 5], [1, 6], [1, 7], [2, 6], [2, 7]]) == [True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 5], [3, 6], [4, 6], [5, 6], [6, 7]],queries = [[0, 3], [0, 4], [0, 5], [1, 6], [1, 7], [2, 6], [2, 7]]) == [True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 2], [1, 2], [2, 3], [3, 5], [3, 6], [6, 7], [7, 5]],queries = [[0, 5], [0, 7], [1, 5], [1, 7], [2, 5], [2, 7], [3, 7]]) == [True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 2], [1, 2], [2, 3], [3, 5], [3, 6], [6, 7], [7, 5]],queries = [[0, 5], [0, 7], [1, 5], [1, 7], [2, 5], [2, 7], [3, 7]]) == [True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [2, 7], [2, 6], [2, 5], [3, 6], [3, 5], [4, 6], [4, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, False, True, False, False, True, False, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [2, 7], [2, 6], [2, 5], [3, 6], [3, 5], [4, 6], [4, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, False, True, False, False, True, False, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 10], [8, 11]],queries = [[0, 10], [0, 11], [1, 10], [1, 11], [2, 10], [2, 11], [3, 10], [3, 11], [4, 10], [4, 11]]) == [True, True, True, True, True, True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 10], [8, 11]],queries = [[0, 10], [0, 11], [1, 10], [1, 11], [2, 10], [2, 11], [3, 10], [3, 11], [4, 10], [4, 11]]) == [True, True, True, True, True, True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [4, 3]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [4, 3]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2], [3, 5]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2], [3, 5]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5], [0, 4], [1, 4], [2, 4]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5], [0, 4], [1, 4], [2, 4]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7], [1, 6], [2, 5], [3, 4]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [3, 4], [3, 5], [3, 6], [3, 7], [4, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7], [1, 6], [2, 5], [3, 4]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [3, 4], [3, 5], [3, 6], [3, 7], [4, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [1, 5], [1, 6]]) == [True, True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [1, 5], [1, 6]]) == [True, True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 2], [1, 3]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 2], [1, 3]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 6]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 6]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [1, 5], [1, 6], [2, 5], [2, 6], [3, 6], [4, 6]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [1, 5], [1, 6], [2, 5], [2, 6], [3, 6], [4, 6]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 11,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],queries = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == [True, True, True, True, True, True, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 11,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],queries = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == [True, True, True, True, True, True, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [0, 4], [1, 4], [2, 5]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [0, 4], [1, 4], [2, 5]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [0, 2], [2, 4], [3, 4], [4, 5]],queries = [[0, 5], [2, 5], [3, 5], [0, 3], [5, 0]]) == [True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [0, 2], [2, 4], [3, 4], [4, 5]],queries = [[0, 5], [2, 5], [3, 5], [0, 3], [5, 0]]) == [True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 10], [10, 0]]) == [True, True, True, True, True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 10], [10, 0]]) == [True, True, True, True, True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [1, 2], [3, 4], [5, 6], [7, 8]],queries = [[0, 9], [2, 8], [4, 7], [6, 5], [0, 8]]) == [True, True, True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [1, 2], [3, 4], [5, 6], [7, 8]],queries = [[0, 9], [2, 8], [4, 7], [6, 5], [0, 8]]) == [True, True, True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 8], [6, 8]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 5], [1, 6], [1, 7], [1, 8], [2, 3], [2, 4], [2, 7], [2, 8], [3, 8], [4, 8], [5, 6], [6, 7]]) == [True, True, True, True, True, True, False, False, True, True, False, False, False, True, False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 8], [6, 8]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 5], [1, 6], [1, 7], [1, 8], [2, 3], [2, 4], [2, 7], [2, 8], [3, 8], [4, 8], [5, 6], [6, 7]]) == [True, True, True, True, True, True, False, False, True, True, False, False, False, True, False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 2], [1, 2], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7]],queries = [[0, 5], [0, 6], [0, 7], [1, 5], [1, 6], [1, 7], [2, 6], [2, 7], [3, 6], [3, 7], [4, 6], [4, 7]]) == [True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 2], [1, 2], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7]],queries = [[0, 5], [0, 6], [0, 7], [1, 5], [1, 6], [1, 7], [2, 6], [2, 7], [3, 6], [3, 7], [4, 6], [4, 7]]) == [True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5], [0, 4]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5], [0, 4]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [0, 8], [1, 7], [2, 6], [3, 5]]) == [True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [0, 8], [1, 7], [2, 6], [3, 5]]) == [True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 7], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 7], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]],queries = [[0, 5], [0, 6], [1, 5], [1, 6], [2, 5], [2, 6], [3, 6]]) == [True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]],queries = [[0, 5], [0, 6], [1, 5], [1, 6], [2, 5], [2, 6], [3, 6]]) == [True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [0, 8], [1, 6], [3, 9], [5, 4]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [0, 8], [1, 6], [3, 9], [5, 4]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 3], [1, 4], [2, 5]],queries = [[0, 6], [1, 5], [2, 4], [0, 5], [3, 4], [0, 4], [4, 6], [1, 3]]) == [True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 3], [1, 4], [2, 5]],queries = [[0, 6], [1, 5], [2, 4], [0, 5], [3, 4], [0, 4], [4, 6], [1, 3]]) == [True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14]],queries = [[0, 13], [0, 14], [1, 13], [1, 14], [2, 13], [2, 14], [3, 13], [3, 14], [4, 13], [4, 14]]) == [True, True, True, True, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14]],queries = [[0, 13], [0, 14], [1, 13], [1, 14], [2, 13], [2, 14], [3, 13], [3, 14], [4, 13], [4, 14]]) == [True, True, True, True, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 4], [1, 2], [1, 3], [2, 4], [3, 4]],queries = [[0, 2], [0, 3], [1, 4], [2, 3], [3, 2]]) == [True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 4], [1, 2], [1, 3], [2, 4], [3, 4]],queries = [[0, 2], [0, 3], [1, 4], [2, 3], [3, 2]]) == [True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9]],queries = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 9], [2, 9], [3, 5], [3, 6], [4, 7]]) == [True, True, True, True, True, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9]],queries = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 9], [2, 9], [3, 5], [3, 6], [4, 7]]) == [True, True, True, True, True, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]],queries = [[0, 11], [1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]]) == [True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]],queries = [[0, 11], [1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]]) == [True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [6, 7], [2, 6]],queries = [[0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [6, 7], [2, 6]],queries = [[0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 8], [4, 9], [5, 10], [5, 11], [6, 11], [6, 12], [7, 13], [8, 13], [9, 13], [10, 14], [11, 14], [12, 14]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14]]) == [True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 8], [4, 9], [5, 10], [5, 11], [6, 11], [6, 12], [7, 13], [8, 13], [9, 13], [10, 14], [11, 14], [12, 14]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14]]) == [True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 4], [5, 6]],queries = [[0, 4], [0, 5], [0, 6], [1, 3], [1, 5], [1, 6], [2, 5], [2, 6], [3, 5], [4, 6]]) == [True, True, True, True, False, False, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 4], [5, 6]],queries = [[0, 4], [0, 5], [0, 6], [1, 3], [1, 5], [1, 6], [2, 5], [2, 6], [3, 5], [4, 6]]) == [True, True, True, True, False, False, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 2], [1, 2], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7], [6, 8], [7, 9]],queries = [[0, 5], [1, 6], [2, 8], [3, 9], [4, 7], [5, 8]]) == [True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 2], [1, 2], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7], [6, 8], [7, 9]],queries = [[0, 5], [1, 6], [2, 8], [3, 9], [4, 7], [5, 8]]) == [True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],queries = [[0, 3], [0, 5], [1, 6], [3, 5], [4, 6]]) == [True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],queries = [[0, 3], [0, 5], [1, 6], [3, 5], [4, 6]]) == [True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9]]) == [True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9]]) == [True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 2], [1, 0], [2, 0]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 2], [1, 0], [2, 0]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [3, 0], [1, 2]]) == [True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [3, 0], [1, 2]]) == [True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 2], [3, 4]]) == [True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 2], [3, 4]]) == [True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [0, 3], [3, 4], [1, 4]],queries = [[0, 2], [2, 0], [0, 4], [4, 0]]) == [True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [0, 3], [3, 4], [1, 4]],queries = [[0, 2], [2, 0], [0, 4], [4, 0]]) == [True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [5, 0], [1, 4], [4, 1]]) == [True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [5, 0], [1, 4], [4, 1]]) == [True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [2, 0]],queries = [[0, 1], [2, 1], [1, 2]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [2, 0]],queries = [[0, 1], [2, 1], [1, 2]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 3], [2, 3]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 3], [2, 3]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 0], [0, 2], [2, 3], [3, 4]],queries = [[1, 4], [0, 4], [0, 3], [0, 2]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 0], [0, 2], [2, 3], [3, 4]],queries = [[1, 4], [0, 4], [0, 3], [0, 2]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 2]],queries = [[0, 1], [1, 2], [0, 2], [3, 0]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 2]],queries = [[0, 1], [1, 2], [0, 2], [3, 0]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],queries = [[1, 5], [1, 4], [2, 5], [3, 5], [4, 5]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],queries = [[1, 5], [1, 4], [2, 5], [3, 5], [4, 5]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 3], [1, 3], [0, 2]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 3], [1, 3], [0, 2]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [0, 3], [1, 3], [2, 3]]) == [False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [0, 3], [1, 3], [2, 3]]) == [False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 2]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 2]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [3, 1]]) == [True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [3, 1]]) == [True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [2, 3], [3, 0]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [2, 3], [3, 0]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 4], [2, 4], [3, 5], [4, 5]],queries = [[1, 5], [2, 5], [3, 4]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 4], [2, 4], [3, 5], [4, 5]],queries = [[1, 5], [2, 5], [3, 4]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3]]) == [True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3]]) == [True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]],queries = [[5, 0], [5, 1], [4, 2], [4, 3], [2, 1]]) == [True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]],queries = [[5, 0], [5, 1], [4, 2], [4, 3], [2, 1]]) == [True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[0, 1]],queries = [[0, 1], [1, 0], [1, 2]]) == [True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[0, 1]],queries = [[0, 1], [1, 0], [1, 2]]) == [True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[0, 3], [3, 0], [1, 2], [2, 1]]) == [True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[0, 3], [3, 0], [1, 2], [2, 1]]) == [True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 2]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 2]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 2], [1, 3], [0, 3], [2, 1]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 2], [1, 3], [0, 3], [2, 1]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [0, 2], [1, 3], [2, 0]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [0, 2], [1, 3], [2, 0]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]],queries = [[0, 1], [0, 3], [0, 5], [1, 2], [2, 3], [3, 4]]) == [False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]],queries = [[0, 1], [0, 3], [0, 5], [1, 2], [2, 3], [3, 4]]) == [False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1]],queries = [[0, 3], [1, 3], [2, 3]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1]],queries = [[0, 3], [1, 3], [2, 3]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0], [1, 2], [0, 2]]) == [False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0], [1, 2], [0, 2]]) == [False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [0, 3]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [0, 3]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 2], [2, 3], [3, 4], [4, 5]],queries = [[1, 5], [2, 4], [3, 5], [0, 5]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 2], [2, 3], [3, 4], [4, 5]],queries = [[1, 5], [2, 4], [3, 5], [0, 5]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [1, 0], [2, 0]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [1, 0], [2, 0]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 0], [2, 3], [3, 2]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 0], [2, 3], [3, 2]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 2]],queries = [[0, 1], [1, 2], [0, 2], [2, 0], [1, 0], [2, 1]]) == [True, True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 2]],queries = [[0, 1], [1, 2], [0, 2], [2, 0], [1, 0], [2, 1]]) == [True, True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 2], [2, 3], [3, 4], [1, 3], [1, 4]],queries = [[0, 1], [1, 0], [2, 4]]) == [False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 2], [2, 3], [3, 4], [1, 3], [1, 4]],queries = [[0, 1], [1, 0], [2, 4]]) == [False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2], [0, 2]]) == [False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2], [0, 2]]) == [False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 3], [1, 3], [2, 3]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 3], [1, 3], [2, 3]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 4], [2, 4], [3, 4]],queries = [[0, 4], [1, 4], [2, 4], [3, 4], [4, 0]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 4], [2, 4], [3, 4]],queries = [[0, 4], [1, 4], [2, 4], [3, 4], [4, 0]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [3, 0]]) == [True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [3, 0]]) == [True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [5, 0], [2, 3], [3, 2]]) == [True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [5, 0], [2, 3], [3, 2]]) == [True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 1], [0, 4], [1, 3], [2, 4], [4, 0]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 1], [0, 4], [1, 3], [2, 4], [4, 0]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[0, 5], [1, 4], [2, 5], [0, 3], [3, 2]]) == [False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[0, 5], [1, 4], [2, 5], [0, 3], [3, 2]]) == [False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [1, 4], [0, 3], [1, 3], [0, 2], [1, 2], [2, 4], [0, 1], [2, 3], [4, 0]]) == [True, True, True, True, True, True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [1, 4], [0, 3], [1, 3], [0, 2], [1, 2], [2, 4], [0, 1], [2, 3], [4, 0]]) == [True, True, True, True, True, True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[0, 1]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[0, 1]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [4, 5]]) == [False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [4, 5]]) == [False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [2, 3]]) == [True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [2, 3]]) == [True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [3, 0], [1, 2], [0, 2]]) == [True, False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [3, 0], [1, 2], [0, 2]]) == [True, False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[0, 3], [1, 3], [2, 3], [3, 0]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[0, 3], [1, 3], [2, 3], [3, 0]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [2, 5]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [2, 5]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [],queries = [[1, 0], [0, 1], [2, 1]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [],queries = [[1, 0], [0, 1], [2, 1]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [2, 0], [1, 2]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [2, 0], [1, 2]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [2, 0]],queries = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 0]]) == [False, True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [2, 0]],queries = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 0]]) == [False, True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 3], [3, 2]],queries = [[0, 2], [1, 3], [2, 0], [0, 1]]) == [True, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 3], [3, 2]],queries = [[0, 2], [1, 3], [2, 0], [0, 1]]) == [True, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 2], [1, 4], [1, 5], [2, 3], [3, 4], [3, 5]],queries = [[1, 3], [1, 4], [2, 5], [3, 1]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 2], [1, 4], [1, 5], [2, 3], [3, 4], [3, 5]],queries = [[1, 3], [1, 4], [2, 5], [3, 1]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 5]],queries = [[1, 4], [2, 5], [3, 4], [0, 5]]) == [True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 5]],queries = [[1, 4], [2, 5], [3, 4], [0, 5]]) == [True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2], [2, 0]]) == [False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2], [2, 0]]) == [False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [3, 4]],queries = [[0, 2], [3, 4]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [3, 4]],queries = [[0, 2], [3, 4]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2], [0, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2], [0, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [2, 4]]) == [True, False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [2, 4]]) == [True, False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [6, 5]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6]]) == [False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [6, 5]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6]]) == [False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[2, 0], [2, 1]]) == [False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[2, 0], [2, 1]]) == [False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [0, 2]]) == [False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [0, 2]]) == [False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [2, 3], [1, 3], [2, 4], [3, 5]],queries = [[0, 3], [2, 5], [0, 5], [1, 2]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [2, 3], [1, 3], [2, 4], [3, 5]],queries = [[0, 3], [2, 5], [0, 5], [1, 2]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],queries = [[0, 4], [1, 4], [2, 4]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],queries = [[0, 4], [1, 4], [2, 4]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]],queries = [[0, 3], [0, 4], [1, 5], [2, 3]]) == [True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]],queries = [[0, 3], [0, 4], [1, 5], [2, 3]]) == [True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 2], [2, 3], [3, 4], [4, 0]],queries = [[1, 4], [4, 1], [0, 3], [3, 2]]) == [True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 2], [2, 3], [3, 4], [4, 0]],queries = [[1, 4], [4, 1], [0, 3], [3, 2]]) == [True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2], [2, 0]],queries = [[1, 0], [2, 0], [0, 1]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2], [2, 0]],queries = [[1, 0], [2, 0], [0, 1]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [0, 2], [1, 0]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [0, 2], [1, 0]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0]]) == [False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0]]) == [False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[0, 1], [0, 2]],queries = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 0], [0, 2]]) == [True, False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[0, 1], [0, 2]],queries = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 0], [0, 2]]) == [True, False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [0, 3], [3, 0]]) == [False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [0, 3], [3, 0]]) == [False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2], [3, 1]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2], [3, 1]]) == [True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 2], [1, 0], [2, 1]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 2], [1, 0], [2, 1]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[1, 3], [2, 3], [3, 0], [3, 1]]) == [True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[1, 3], [2, 3], [3, 0], [3, 1]]) == [True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 0]]) == [False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 0]]) == [False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 4], [2, 4], [3, 4]],queries = [[0, 4], [1, 2], [2, 0], [3, 1]]) == [True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 4], [2, 4], [3, 4]],queries = [[0, 4], [1, 2], [2, 0], [3, 1]]) == [True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 0]]) == [False, False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 0]]) == [False, False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4]],queries = [[0, 3], [0, 4]]) == [True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4]],queries = [[0, 3], [0, 4]]) == [True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4]],queries = [[0, 4], [0, 3], [1, 4], [2, 3], [3, 4]]) == [True, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4]],queries = [[0, 4], [0, 3], [1, 4], [2, 3], [3, 4]]) == [True, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 2], [2, 0]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 2], [2, 0]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 2], [1, 0]],queries = [[0, 1], [1, 0], [2, 0]]) == [False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 2], [1, 0]],queries = [[0, 1], [1, 0], [2, 0]]) == [False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]],queries = [[0, 1], [1, 2], [0, 2]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]],queries = [[0, 1], [1, 2], [0, 2]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2]]) == [False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2]]) == [False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [2, 3], [3, 0]]) == [False, False, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [2, 3], [3, 0]]) == [False, False, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 0]],queries = [[0, 1], [0, 2], [0, 3], [1, 2]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 0]],queries = [[0, 1], [0, 2], [0, 3], [1, 2]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 4], [2, 0]]) == [True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 4], [2, 0]]) == [True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 5]],queries = [[1, 4], [4, 1], [1, 5], [5, 1]]) == [True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 5]],queries = [[1, 4], [4, 1], [1, 5], [5, 1]]) == [True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [1, 2]]) == [False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [1, 2]]) == [False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 1], [1, 3], [0, 3]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 1], [1, 3], [0, 3]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [2, 3], [4, 5]],queries = [[0, 1], [2, 3], [4, 5], [3, 4]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [2, 3], [4, 5]],queries = [[0, 1], [2, 3], [4, 5], [3, 4]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [2, 1]]) == [False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [2, 1]]) == [False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5]]) == [False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5]]) == [False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[3, 0], [5, 0], [4, 2], [1, 2]]) == [True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[3, 0], [5, 0], [4, 2], [1, 2]]) == [True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [1, 4], [2, 4]],queries = [[0, 4], [1, 4], [2, 3], [3, 4]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [1, 4], [2, 4]],queries = [[0, 4], [1, 4], [2, 3], [3, 4]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2]],queries = [[0, 1], [2, 0], [0, 3], [3, 0], [2, 3]]) == [False, True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2]],queries = [[0, 1], [2, 0], [0, 3], [3, 0], [2, 3]]) == [False, True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [0, 2], [3, 0]]) == [True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [0, 2], [3, 0]]) == [True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 1], [1, 3], [0, 4], [2, 3], [4, 2]]) == [True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 1], [1, 3], [0, 4], [2, 3], [4, 2]]) == [True, True, True, True, False]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0]]) == [True, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [0, 2]]) == [True, True, True]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4]],queries = [[0, 3], [1, 4], [2, 3]]) == [True, True, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2]],queries = [[0, 2], [2, 0]]) == [True, False]
    assert candidate(numCourses = 2,prerequisites = [],queries = [[1, 0], [0, 1]]) == [False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [3, 4]]) == [True, True, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 4], [2, 3]]) == [True, True, True, True]
    assert candidate(numCourses = 3,prerequisites = [[1, 2], [1, 0], [2, 0]],queries = [[1, 0], [1, 2]]) == [True, True]
    assert candidate(numCourses = 2,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0]]) == [False, True]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 2], [2, 0], [3, 0]]) == [True, True, False, False]
    assert candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 5], [0, 4], [1, 2]]) == [True, True, True, False, False, True, False]
    assert candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [1, 11], [1, 12], [2, 7], [2, 8]]) == [True, True, True, True, True, True, True, True, False, False, False, False]
    assert candidate(numCourses = 15,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [7, 7]]) == [True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],queries = [[0, 7], [1, 5], [2, 4], [3, 6], [5, 7]]) == [True, False, False, False, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4]]) == [True, True, True, True, True, False]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 3], [1, 2]]) == [True, True, False, False, False, True, False]
    assert candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 8], [4, 9], [5, 10], [5, 11], [6, 10], [6, 11], [7, 11], [8, 11], [9, 11]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 10], [1, 11], [2, 10], [2, 11], [3, 11], [4, 11]]) == [True, True, True, True, True, False, True, True, True, True, True]
    assert candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 7], [4, 8]],queries = [[0, 7], [0, 8], [1, 7], [1, 8], [2, 7], [2, 8], [0, 3], [0, 4]]) == [True, True, True, True, False, False, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == [True, True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 7], [5, 7], [6, 8]],queries = [[0, 7], [0, 8], [1, 5], [1, 6], [2, 7], [2, 8], [3, 7], [3, 8], [4, 7], [5, 7], [6, 8]]) == [True, True, False, False, True, True, True, True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == [True, True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2]]) == [True, True, True, True]
    assert candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 5], [1, 2]]) == [True, False, False, True, False, False, True, False]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 6], [4, 6], [5, 6]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 5], [0, 4], [0, 3]]) == [True, True, True, True, True, True, False, True, True]
    assert candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8]],queries = [[0, 3], [0, 7], [1, 8], [2, 6], [3, 5]]) == [True, True, True, True, False]
    assert candidate(numCourses = 9,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [0, 4], [1, 5], [2, 6], [3, 7], [4, 8]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 4], [5, 3], [6, 2], [7, 1], [8, 0]]) == [True, True, True, True, True, False, False, False, False]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5], [5, 6]],queries = [[0, 3], [1, 5], [2, 6], [3, 6]]) == [True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, True, True, True]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [2, 5], [4, 6], [5, 6]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 5]]) == [True, True, True, False, True, True, False]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 3]]) == [True, True, True, True, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5]],queries = [[0, 5], [1, 4], [2, 4], [3, 5], [1, 3], [2, 3]]) == [True, True, True, True, True, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]],queries = [[0, 3], [0, 4], [0, 5], [1, 2], [1, 5], [2, 3], [2, 4]]) == [True, True, True, False, False, False, False]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 5], [3, 6], [4, 6], [5, 6], [6, 7]],queries = [[0, 3], [0, 4], [0, 5], [1, 6], [1, 7], [2, 6], [2, 7]]) == [True, True, True, True, True, True, True]
    assert candidate(numCourses = 8,prerequisites = [[0, 2], [1, 2], [2, 3], [3, 5], [3, 6], [6, 7], [7, 5]],queries = [[0, 5], [0, 7], [1, 5], [1, 7], [2, 5], [2, 7], [3, 7]]) == [True, True, True, True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1], [1, 8], [1, 7], [1, 6], [1, 5], [1, 4], [2, 7], [2, 6], [2, 5], [3, 6], [3, 5], [4, 6], [4, 5]]) == [True, True, True, True, True, True, True, True, True, True, True, False, True, False, False, True, False, True, True, False, False, False, False]
    assert candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 10], [8, 11]],queries = [[0, 10], [0, 11], [1, 10], [1, 11], [2, 10], [2, 11], [3, 10], [3, 11], [4, 10], [4, 11]]) == [True, True, True, True, True, True, True, True, False, False]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [4, 3]]) == [True, True, True, True, False]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2], [3, 5]]) == [True, True, True, True, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5], [0, 4], [1, 4], [2, 4]]) == [True, True, True, True, True, True]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [0, 7], [1, 6], [2, 5], [3, 4]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [3, 4], [3, 5], [3, 6], [3, 7], [4, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [1, 5], [1, 6]]) == [True, True, True, True, False, False]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 6], [2, 5], [3, 4], [0, 2], [1, 3]]) == [True, True, True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 8], [1, 7], [2, 6], [3, 5], [4, 6]]) == [True, True, True, True, False]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7]]) == [True, True, True, True, True, True]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [1, 5], [1, 6], [2, 5], [2, 6], [3, 6], [4, 6]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 11,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],queries = [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == [True, True, True, True, True, True, False, False, False, False]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [0, 4], [1, 4], [2, 5]]) == [True, True, True, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [0, 2], [2, 4], [3, 4], [4, 5]],queries = [[0, 5], [2, 5], [3, 5], [0, 3], [5, 0]]) == [True, True, True, False, False]
    assert candidate(numCourses = 15,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]],queries = [[0, 14], [1, 13], [2, 12], [3, 11], [4, 10], [5, 9], [6, 8], [0, 10], [10, 0]]) == [True, True, True, True, True, True, True, True, False]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [1, 2], [3, 4], [5, 6], [7, 8]],queries = [[0, 9], [2, 8], [4, 7], [6, 5], [0, 8]]) == [True, True, True, False, True]
    assert candidate(numCourses = 9,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 8], [6, 8]],queries = [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 5], [1, 6], [1, 7], [1, 8], [2, 3], [2, 4], [2, 7], [2, 8], [3, 8], [4, 8], [5, 6], [6, 7]]) == [True, True, True, True, True, True, False, False, True, True, False, False, False, True, False, True, False, False]
    assert candidate(numCourses = 8,prerequisites = [[0, 2], [1, 2], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7]],queries = [[0, 5], [0, 6], [0, 7], [1, 5], [1, 6], [1, 7], [2, 6], [2, 7], [3, 6], [3, 7], [4, 6], [4, 7]]) == [True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5], [0, 4]]) == [True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [0, 8], [1, 7], [2, 6], [3, 5]]) == [True, True, True, False, False]
    assert candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 7], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, False]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]],queries = [[0, 5], [0, 6], [1, 5], [1, 6], [2, 5], [2, 6], [3, 6]]) == [True, True, True, True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [0, 8], [1, 6], [3, 9], [5, 4]]) == [True, True, True, True, False]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [0, 3], [1, 4], [2, 5]],queries = [[0, 6], [1, 5], [2, 4], [0, 5], [3, 4], [0, 4], [4, 6], [1, 3]]) == [True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14]],queries = [[0, 13], [0, 14], [1, 13], [1, 14], [2, 13], [2, 14], [3, 13], [3, 14], [4, 13], [4, 14]]) == [True, True, True, True, False, False, False, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 4], [1, 2], [1, 3], [2, 4], [3, 4]],queries = [[0, 2], [0, 3], [1, 4], [2, 3], [3, 2]]) == [True, True, True, False, False]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9]],queries = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 9], [2, 9], [3, 5], [3, 6], [4, 7]]) == [True, True, True, True, True, False, False, False, False, False]
    assert candidate(numCourses = 12,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]],queries = [[0, 11], [1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]]) == [True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]) == [True, True, False, False, False]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [6, 7], [2, 6]],queries = [[0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, False, False]
    assert candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 8], [4, 9], [5, 10], [5, 11], [6, 11], [6, 12], [7, 13], [8, 13], [9, 13], [10, 14], [11, 14], [12, 14]],queries = [[0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14]]) == [True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == [True, True, True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 4], [5, 6]],queries = [[0, 4], [0, 5], [0, 6], [1, 3], [1, 5], [1, 6], [2, 5], [2, 6], [3, 5], [4, 6]]) == [True, True, True, True, False, False, True, True, False, False]
    assert candidate(numCourses = 10,prerequisites = [[0, 2], [1, 2], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7], [6, 8], [7, 9]],queries = [[0, 5], [1, 6], [2, 8], [3, 9], [4, 7], [5, 8]]) == [True, True, True, True, True, True]
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],queries = [[0, 3], [0, 5], [1, 6], [3, 5], [4, 6]]) == [True, True, False, False, False]
    assert candidate(numCourses = 12,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],queries = [[0, 11], [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [0, 8], [1, 7], [2, 6], [3, 5], [0, 7], [1, 6], [2, 5], [3, 4]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],queries = [[0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9]]) == [True, True, True, True, True, True, True, True]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True]
    assert candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 2], [1, 0], [2, 0]]) == [False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [3, 0], [1, 2]]) == [True, False, True]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 2], [3, 4]]) == [True, True, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [0, 3], [3, 4], [1, 4]],queries = [[0, 2], [2, 0], [0, 4], [4, 0]]) == [True, False, True, False]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [5, 0], [1, 4], [4, 1]]) == [True, False, True, False]
    assert candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [2, 0]],queries = [[0, 1], [2, 1], [1, 2]]) == [False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 3], [2, 3]]) == [False, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[1, 0], [0, 2], [2, 3], [3, 4]],queries = [[1, 4], [0, 4], [0, 3], [0, 2]]) == [True, True, True, True]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 2]],queries = [[0, 1], [1, 2], [0, 2], [3, 0]]) == [True, True, True, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, False, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],queries = [[1, 5], [1, 4], [2, 5], [3, 5], [4, 5]]) == [True, True, True, True, True]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 3], [1, 3], [0, 2]]) == [False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [0, 3], [1, 3], [2, 3]]) == [False, False, False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 2]]) == [True, True]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [3, 1]]) == [True, False, True, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [2, 3], [3, 0]]) == [True, True, True, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 4], [2, 4], [3, 5], [4, 5]],queries = [[1, 5], [2, 5], [3, 4]]) == [True, True, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3]]) == [True, False, True]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]],queries = [[5, 0], [5, 1], [4, 2], [4, 3], [2, 1]]) == [True, True, False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[0, 1]],queries = [[0, 1], [1, 0], [1, 2]]) == [True, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[0, 3], [3, 0], [1, 2], [2, 1]]) == [True, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 2]]) == [True, True, False]
    assert candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [False, False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 2], [1, 3], [0, 3], [2, 1]]) == [False, False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [0, 2], [1, 3], [2, 0]]) == [True, True, True, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]],queries = [[0, 1], [0, 3], [0, 5], [1, 2], [2, 3], [3, 4]]) == [False, False, False, False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1]],queries = [[0, 3], [1, 3], [2, 3]]) == [False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0], [1, 2], [0, 2]]) == [False, True, False, False]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [0, 3]]) == [False, False, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 2], [2, 3], [3, 4], [4, 5]],queries = [[1, 5], [2, 4], [3, 5], [0, 5]]) == [True, True, True, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [1, 0], [2, 0]]) == [False, False, False]
    assert candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 0], [2, 3], [3, 2]]) == [False, False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 2]],queries = [[0, 1], [1, 2], [0, 2], [2, 0], [1, 0], [2, 1]]) == [True, True, True, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[1, 2], [2, 3], [3, 4], [1, 3], [1, 4]],queries = [[0, 1], [1, 0], [2, 4]]) == [False, False, True]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [2, 3]],queries = [[0, 1], [1, 2], [2, 3], [3, 0]]) == [True, False, True, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2], [0, 2]]) == [False, True, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 3], [1, 3], [2, 3]]) == [False, False, False]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [4, 5]],queries = [[0, 5], [1, 5], [2, 5]]) == [True, True, True]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 4], [2, 4], [3, 4]],queries = [[0, 4], [1, 4], [2, 4], [3, 4], [4, 0]]) == [True, True, True, True, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [3, 0]]) == [True, False, True, False]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [5, 0], [2, 3], [3, 2]]) == [True, False, True, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 1], [0, 4], [1, 3], [2, 4], [4, 0]]) == [True, True, True, True, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[0, 5], [1, 4], [2, 5], [0, 3], [3, 2]]) == [False, False, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [1, 4], [0, 3], [1, 3], [0, 2], [1, 2], [2, 4], [0, 1], [2, 3], [4, 0]]) == [True, True, True, True, True, True, True, True, True, False]
    assert candidate(numCourses = 3,prerequisites = [[0, 1]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [True, False, False, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [4, 5]]) == [False, False, False, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [2, 3]]) == [True, False, True]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [3, 0], [1, 2], [0, 2]]) == [True, False, True, True]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[0, 3], [1, 3], [2, 3], [3, 0]]) == [True, True, True, False]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [2, 5]]) == [True, True]
    assert candidate(numCourses = 3,prerequisites = [],queries = [[1, 0], [0, 1], [2, 1]]) == [False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [2, 0], [1, 2]]) == [False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [2, 0]],queries = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 0]]) == [False, True, False, False, True]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, True, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [0, 3], [3, 2]],queries = [[0, 2], [1, 3], [2, 0], [0, 1]]) == [True, False, False, True]
    assert candidate(numCourses = 6,prerequisites = [[1, 2], [1, 4], [1, 5], [2, 3], [3, 4], [3, 5]],queries = [[1, 3], [1, 4], [2, 5], [3, 1]]) == [True, True, True, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 5]],queries = [[1, 4], [2, 5], [3, 4], [0, 5]]) == [True, False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2], [2, 0]]) == [False, True, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [3, 4]],queries = [[0, 2], [3, 4]]) == [True, True]
    assert candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [False, False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 2], [0, 2]],queries = [[0, 1], [1, 0], [0, 2], [2, 0]]) == [False, False, True, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3]],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [False, False, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 4], [4, 0], [1, 3], [2, 4]]) == [True, False, True, True]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5]]) == [False, False, False, False]
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [6, 5]],queries = [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6]]) == [False, False, False, False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[2, 0], [2, 1]]) == [False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [0, 2]]) == [False, True, False]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [2, 3], [1, 3], [2, 4], [3, 5]],queries = [[0, 3], [2, 5], [0, 5], [1, 2]]) == [True, True, True, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],queries = [[0, 4], [1, 4], [2, 4]]) == [True, True, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]],queries = [[0, 3], [0, 4], [1, 5], [2, 3]]) == [True, True, False, False]
    assert candidate(numCourses = 5,prerequisites = [[1, 2], [2, 3], [3, 4], [4, 0]],queries = [[1, 4], [4, 1], [0, 3], [3, 2]]) == [True, False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 2], [2, 0]],queries = [[1, 0], [2, 0], [0, 1]]) == [True, True, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 1], [0, 2], [1, 0]]) == [False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0]],queries = [[0, 1], [1, 0]]) == [False, True]
    assert candidate(numCourses = 3,prerequisites = [[0, 1], [0, 2]],queries = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 0], [0, 2]]) == [True, False, False, False, False, True]
    assert candidate(numCourses = 4,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2], [2, 1]]) == [False, False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [0, 3], [3, 0]]) == [False, False, False, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],queries = [[0, 5], [1, 4], [2, 3], [0, 2], [3, 1]]) == [True, True, True, True, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 2]],queries = [[0, 2], [1, 0], [2, 1]]) == [False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]],queries = [[1, 3], [2, 3], [3, 0], [3, 1]]) == [True, True, False, False]
    assert candidate(numCourses = 8,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],queries = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == [True, True, True, True, True, True, True]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 0]]) == [False, False, False, False, True]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 4], [2, 4], [3, 4]],queries = [[0, 4], [1, 2], [2, 0], [3, 1]]) == [True, False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 0]]) == [False, False, False, False, True]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4]],queries = [[0, 3], [0, 4]]) == [True, True]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4]],queries = [[0, 4], [0, 3], [1, 4], [2, 3], [3, 4]]) == [True, True, True, False, False]
    assert candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 2], [2, 0]]) == [False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 2], [1, 0]],queries = [[0, 1], [1, 0], [2, 0]]) == [False, True, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]],queries = [[0, 1], [1, 2], [0, 2]]) == [False, False, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 2]]) == [False, True]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]],queries = [[0, 1], [1, 3], [2, 3], [3, 0]]) == [False, False, False, True]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 0]],queries = [[0, 1], [0, 2], [0, 3], [1, 2]]) == [False, False, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4]],queries = [[0, 3], [0, 4], [1, 4], [2, 0]]) == [True, True, False, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 2], [1, 3], [2, 4], [3, 5]],queries = [[1, 4], [4, 1], [1, 5], [5, 1]]) == [True, False, True, False]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2]],queries = [[0, 1], [1, 0], [1, 2]]) == [False, True, True]
    assert candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [1, 2]]) == [False, False, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 1], [1, 3], [0, 3]]) == [True, True, True]
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [2, 3], [4, 5]],queries = [[0, 1], [2, 3], [4, 5], [3, 4]]) == [True, True, True, False]
    assert candidate(numCourses = 3,prerequisites = [],queries = [[0, 1], [1, 0], [2, 1]]) == [False, False, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]],queries = [[0, 5], [1, 5], [2, 5], [3, 5]]) == [False, False, False, False]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2]],queries = [[3, 0], [5, 0], [4, 2], [1, 2]]) == [True, True, False, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3], [1, 4], [2, 4]],queries = [[0, 4], [1, 4], [2, 3], [3, 4]]) == [True, True, True, False]
    assert candidate(numCourses = 4,prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2]],queries = [[0, 1], [2, 0], [0, 3], [3, 0], [2, 3]]) == [False, True, False, True, False]
    assert candidate(numCourses = 4,prerequisites = [[0, 1], [1, 2], [2, 3]],queries = [[0, 3], [1, 3], [0, 2], [3, 0]]) == [True, True, True, False]
    assert candidate(numCourses = 5,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]],queries = [[0, 1], [1, 3], [0, 4], [2, 3], [4, 2]]) == [True, True, True, True, False]


