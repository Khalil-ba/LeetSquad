def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(numCourses = 2,prerequisites = [[1, 0], [0, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 2,prerequisites = [[1, 0], [0, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 1,prerequisites = []) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 1,prerequisites = []) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 2,prerequisites = [[1, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 2,prerequisites = [[1, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8], [13, 9], [14, 10], [14, 11], [14, 12], [15, 13], [16, 13], [17, 14], [18, 15], [18, 16], [19, 17], [19, 18]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8], [13, 9], [14, 10], [14, 11], [14, 12], [15, 13], [16, 13], [17, 14], [18, 15], [18, 16], [19, 17], [19, 18]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [8, 5], [9, 6], [9, 7]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [8, 5], [9, 6], [9, 7]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [5, 4], [6, 5], [7, 6], [8, 7], [8, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [5, 4], [6, 5], [7, 6], [8, 7], [8, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [5, 2], [6, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [5, 2], [6, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [4, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [4, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [7, 4], [8, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [7, 4], [8, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [7, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [7, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [7, 9], [8, 10]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [7, 9], [8, 10]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13], [15, 14], [16, 15], [17, 16], [18, 17], [19, 18], [0, 19]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13], [15, 14], [16, 15], [17, 16], [18, 17], [19, 18], [0, 19]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4], [6, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4], [6, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 1], [7, 1], [8, 2], [9, 2], [10, 3], [11, 3], [12, 4], [12, 5], [12, 6], [12, 7]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 1], [7, 1], [8, 2], [9, 2], [10, 3], [11, 3], [12, 4], [12, 5], [12, 6], [12, 7]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [12, 8], [13, 9], [13, 10], [14, 11], [14, 12]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [12, 8], [13, 9], [13, 10], [14, 11], [14, 12]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [4, 6], [5, 7]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [4, 6], [5, 7]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [10, 7], [10, 8]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [10, 7], [10, 8]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [5, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [5, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8], [13, 9], [14, 10], [14, 11], [14, 12]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8], [13, 9], [14, 10], [14, 11], [14, 12]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 0], [2, 1], [3, 4], [4, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 0], [2, 1], [3, 4], [4, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [6, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 19], [11, 19], [12, 19], [13, 19], [14, 19], [15, 19], [16, 19], [17, 19], [18, 19]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [6, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 19], [11, 19], [12, 19], [13, 19], [14, 19], [15, 19], [16, 19], [17, 19], [18, 19]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [5, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [5, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [6, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [6, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 2], [5, 3], [6, 4], [6, 5], [7, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 2], [5, 3], [6, 4], [6, 5], [7, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [4, 6], [5, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [4, 6], [5, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [8, 9]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [8, 9]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [0, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [0, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [5, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [5, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 2], [6, 3], [7, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 2], [6, 3], [7, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7], [10, 8], [11, 8]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7], [10, 8], [11, 8]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [0, 7]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [0, 7]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [6, 7]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [6, 7]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [9, 7]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [9, 7]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 3], [5, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 3], [5, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [9, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [9, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [1, 9]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [1, 9]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [7, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [7, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4], [6, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4], [6, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [6, 7], [7, 8], [8, 9], [9, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [6, 7], [7, 8], [8, 9], [9, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7], [14, 8], [14, 9]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7], [14, 8], [14, 9]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [5, 2], [6, 3], [7, 3], [8, 4], [9, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [5, 2], [6, 3], [7, 3], [8, 4], [9, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 4], [5, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 4], [5, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [5, 4], [6, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [5, 4], [6, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [6, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [6, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 0], [7, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 0], [7, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [12, 8], [13, 9], [13, 10], [14, 11], [14, 12], [15, 13], [16, 13], [17, 14], [18, 14], [19, 15], [19, 16]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [12, 8], [13, 9], [13, 10], [14, 11], [14, 12], [15, 13], [16, 13], [17, 14], [18, 14], [19, 15], [19, 16]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8], [8, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8], [8, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [0, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [0, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7], [15, 7], [16, 8], [17, 8], [18, 9], [19, 9], [15, 12], [16, 13], [17, 14], [18, 15], [19, 16]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7], [15, 7], [16, 8], [17, 8], [18, 9], [19, 9], [15, 12], [16, 13], [17, 14], [18, 15], [19, 16]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [7, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [7, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [10, 7], [11, 8], [12, 9], [13, 10], [14, 11], [14, 12]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [10, 7], [11, 8], [12, 9], [13, 10], [14, 11], [14, 12]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(numCourses = 2,prerequisites = [[1, 0], [0, 1]]) == False
    assert candidate(numCourses = 5,prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]) == True
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == True
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]]) == True
    assert candidate(numCourses = 1,prerequisites = []) == True
    assert candidate(numCourses = 2,prerequisites = [[1, 0]]) == True
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8], [13, 9], [14, 10], [14, 11], [14, 12], [15, 13], [16, 13], [17, 14], [18, 15], [18, 16], [19, 17], [19, 18]]) == True
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [8, 5], [9, 6], [9, 7]]) == True
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [5, 4], [6, 5], [7, 6], [8, 7], [8, 5]]) == True
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [5, 2], [6, 3]]) == True
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5]]) == True
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == True
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [4, 8]]) == False
    assert candidate(numCourses = 6,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == False
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [7, 4], [8, 5]]) == True
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 4], [6, 4], [7, 5], [7, 6]]) == True
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [7, 9], [8, 10]]) == True
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13], [15, 14], [16, 15], [17, 16], [18, 17], [19, 18], [0, 19]]) == False
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4], [6, 5]]) == True
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8]]) == False
    assert candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 1], [7, 1], [8, 2], [9, 2], [10, 3], [11, 3], [12, 4], [12, 5], [12, 6], [12, 7]]) == True
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [12, 8], [13, 9], [13, 10], [14, 11], [14, 12]]) == True
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [4, 6], [5, 7]]) == True
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]) == False
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]]) == True
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 9]]) == True
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13]]) == True
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4]]) == True
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == False
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == True
    assert candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [10, 7], [10, 8]]) == True
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]) == True
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]]) == False
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [5, 6]]) == True
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7], [11, 8], [12, 8], [13, 9], [14, 10], [14, 11], [14, 12]]) == True
    assert candidate(numCourses = 5,prerequisites = [[1, 0], [2, 1], [3, 4], [4, 3]]) == False
    assert candidate(numCourses = 20,prerequisites = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [2, 7], [2, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [6, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 19], [11, 19], [12, 19], [13, 19], [14, 19], [15, 19], [16, 19], [17, 19], [18, 19]]) == True
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [5, 0]]) == True
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [6, 5]]) == True
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 2], [5, 3], [6, 4], [6, 5], [7, 6]]) == True
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [4, 6], [5, 6]]) == True
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [8, 9]]) == True
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [0, 6]]) == False
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9]]) == True
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [5, 6]]) == True
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6]]) == True
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6]]) == True
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 2], [6, 3], [7, 3]]) == True
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7], [10, 8], [11, 8]]) == True
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0], [0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]) == False
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [0, 7]]) == False
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [6, 7]]) == False
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [9, 7]]) == True
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 3], [5, 3]]) == True
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9], [9, 1]]) == False
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == True
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [1, 9]]) == False
    assert candidate(numCourses = 15,prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == True
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5]]) == True
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]) == True
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [7, 6]]) == True
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4], [6, 5]]) == True
    assert candidate(numCourses = 10,prerequisites = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [6, 7], [7, 8], [8, 9], [9, 6]]) == False
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]) == True
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7], [14, 8], [14, 9]]) == True
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [5, 2], [6, 3], [7, 3], [8, 4], [9, 5]]) == True
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 4], [5, 3]]) == True
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [5, 4], [6, 5]]) == True
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [6, 3]]) == True
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 0], [7, 6]]) == True
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [12, 8], [13, 9], [13, 10], [14, 11], [14, 12], [15, 13], [16, 13], [17, 14], [18, 14], [19, 15], [19, 16]]) == True
    assert candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [10, 7]]) == True
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7]]) == True
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8], [8, 0]]) == False
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [0, 8]]) == False
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7], [15, 7], [16, 8], [17, 8], [18, 9], [19, 9], [15, 12], [16, 13], [17, 14], [18, 15], [19, 16]]) == True
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [7, 5]]) == True
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [10, 7], [11, 8], [12, 9], [13, 10], [14, 11], [14, 12]]) == True
    assert candidate(numCourses = 7,prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == False


