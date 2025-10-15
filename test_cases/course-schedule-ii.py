def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2]]) == [0, 1, 2, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2]]) == [0, 1, 2, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [2, 1]]) == [0, 4, 5, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [2, 1]]) == [0, 4, 5, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[0, 1], [1, 2], [2, 0]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[0, 1], [1, 2], [2, 0]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2], [0, 1]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2], [0, 1]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[0, 1], [0, 2], [1, 2]]) == [2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[0, 1], [0, 2], [1, 2]]) == [2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [0, 1]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [0, 1]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 4, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 4, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [7, 5]]) == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [7, 5]]) == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]) == [0, 4, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]) == [0, 4, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 1,prerequisites = []) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 1,prerequisites = []) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 2,prerequisites = [[1, 0]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 2,prerequisites = [[1, 0]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [2, 0], [3, 2], [4, 2], [5, 3], [5, 4], [6, 5], [7, 6], [8, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [2, 0], [3, 2], [4, 2], [5, 3], [5, 4], [6, 5], [7, 6], [8, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [10, 5], [11, 6], [11, 7], [11, 8], [11, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [10, 5], [11, 6], [11, 7], [11, 8], [11, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [7, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [7, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [12, 8], [12, 9], [13, 10], [13, 11], [14, 12], [14, 13], [15, 14], [16, 14], [17, 15], [17, 16], [18, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [12, 8], [12, 9], [13, 10], [13, 11], [14, 12], [14, 13], [15, 14], [16, 14], [17, 15], [17, 16], [18, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [10, 8], [11, 9], [12, 10], [13, 11], [14, 12], [15, 13], [16, 14], [17, 15], [18, 16], [19, 17], [18, 19]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [10, 8], [11, 9], [12, 10], [13, 11], [14, 12], [15, 13], [16, 14], [17, 15], [18, 16], [19, 17], [18, 19]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 18]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [8, 4], [9, 5], [9, 6], [10, 7], [10, 8], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [8, 4], [9, 5], [9, 6], [10, 7], [10, 8], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 2], [6, 3], [7, 4], [7, 5], [7, 6], [8, 4], [8, 5], [8, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 2], [6, 3], [7, 4], [7, 5], [7, 6], [8, 4], [8, 5], [8, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9], [14, 10], [14, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9], [14, 10], [14, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 14,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8], [13, 9], [13, 10], [13, 11], [13, 12]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 14,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8], [13, 9], [13, 10], [13, 11], [13, 12]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [4, 3], [5, 2], [5, 3], [6, 3], [6, 4], [7, 3], [7, 4], [7, 5], [8, 4], [8, 5], [8, 6], [9, 4], [9, 5], [9, 6], [9, 7], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [16, 15], [17, 10], [17, 11], [17, 12], [17, 13], [17, 14], [17, 15], [17, 16], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15], [18, 16], [18, 17], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [4, 3], [5, 2], [5, 3], [6, 3], [6, 4], [7, 3], [7, 4], [7, 5], [8, 4], [8, 5], [8, 6], [9, 4], [9, 5], [9, 6], [9, 7], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [16, 15], [17, 10], [17, 11], [17, 12], [17, 13], [17, 14], [17, 15], [17, 16], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15], [18, 16], [18, 17], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 6], [10, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 6], [10, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6], [15, 7], [16, 7], [17, 8], [18, 8], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6], [15, 7], [16, 7], [17, 8], [18, 8], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [7, 6], [8, 5], [8, 6], [8, 7], [9, 7], [10, 7], [10, 8], [11, 7], [11, 8], [11, 9], [11, 10], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [13, 9], [13, 10], [13, 11], [13, 12], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [7, 6], [8, 5], [8, 6], [8, 7], [9, 7], [10, 7], [10, 8], [11, 7], [11, 8], [11, 9], [11, 10], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [13, 9], [13, 10], [13, 11], [13, 12], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 1], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 1], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [0, 11]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [0, 11]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8], [19, 16]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8], [19, 16]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [6, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [6, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [1, 2], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5], [7, 6], [8, 7], [9, 7], [9, 8]]) == [0, 2, 1, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [1, 2], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5], [7, 6], [8, 7], [9, 7], [9, 8]]) == [0, 2, 1, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 18,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 1], [5, 3], [6, 2], [6, 4], [7, 3], [7, 4], [8, 5], [8, 6], [9, 5], [9, 6], [10, 7], [10, 8], [11, 7], [11, 8], [12, 9], [12, 10], [13, 10], [13, 11], [14, 12], [14, 13], [15, 13], [16, 14], [16, 15], [17, 15], [17, 16]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 18,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 1], [5, 3], [6, 2], [6, 4], [7, 3], [7, 4], [8, 5], [8, 6], [9, 5], [9, 6], [10, 7], [10, 8], [11, 7], [11, 8], [12, 9], [12, 10], [13, 10], [13, 11], [14, 12], [14, 13], [15, 13], [16, 14], [16, 15], [17, 15], [17, 16]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 5,prerequisites = [[1, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3]]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 5,prerequisites = [[1, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3]]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [7, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [7, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 5], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 5], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [11, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [11, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 6], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 6], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [13, 14]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [13, 14]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 3], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [13, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 3], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [13, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [10, 8], [10, 9], [10, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [10, 8], [10, 9], [10, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [7, 8]]) == [0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [7, 8]]) == [0, 1, 2, 3, 4, 5, 6, 8, 9, 7]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [7, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [7, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8], [19, 9], [18, 10], [17, 11], [16, 12], [15, 13], [14, 14], [13, 15], [12, 16], [11, 17], [10, 18], [9, 19], [8, 19]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8], [19, 9], [18, 10], [17, 11], [16, 12], [15, 13], [14, 14], [13, 15], [12, 16], [11, 17], [10, 18], [9, 19], [8, 19]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [5, 9]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [5, 9]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [12, 10], [13, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [12, 10], [13, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [5, 6], [7, 8], [9, 7]]) == [0, 1, 2, 3, 4, 6, 8, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [5, 6], [7, 8], [9, 7]]) == [0, 1, 2, 3, 4, 6, 8, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [14, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [14, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5]]) == [0, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5]]) == [0, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [10, 8], [11, 9], [12, 10], [12, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [10, 8], [11, 9], [12, 10], [12, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [2, 0], [3, 2], [3, 1], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [2, 0], [3, 2], [3, 1], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 6], [9, 7], [10, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 6], [9, 7], [10, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [8, 3]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [8, 3]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 1], [8, 2], [9, 2], [10, 2], [11, 3], [12, 3], [13, 4], [14, 4], [15, 5], [16, 5], [17, 6], [18, 6], [19, 7], [19, 8], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 1], [8, 2], [9, 2], [10, 2], [11, 3], [12, 3], [13, 4], [14, 4], [15, 5], [16, 5], [17, 6], [18, 6], [19, 7], [19, 8], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [12, 10], [12, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [12, 10], [12, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [13, 7], [12, 8], [11, 9], [10, 10], [9, 11], [8, 12], [7, 13], [6, 14]]) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [13, 7], [12, 8], [11, 9], [10, 10], [9, 11], [8, 12], [7, 13], [6, 14]]) == []: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [6, 3], [6, 4], [7, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [6, 3], [6, 4], [7, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [7, 5], [8, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [7, 5], [8, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 11,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 11,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 16,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [6, 1], [6, 3], [7, 1], [7, 4], [8, 2], [8, 3], [8, 4], [9, 2], [9, 3], [9, 4], [10, 3], [10, 4], [11, 4], [12, 5], [12, 6], [12, 7], [12, 8], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [14, 6], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [15, 7], [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 16,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [6, 1], [6, 3], [7, 1], [7, 4], [8, 2], [8, 3], [8, 4], [9, 2], [9, 3], [9, 4], [10, 3], [10, 4], [11, 4], [12, 5], [12, 6], [12, 7], [12, 8], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [14, 6], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [15, 7], [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5], [7, 6], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5], [7, 6], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 3], [8, 4], [8, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 3], [8, 4], [8, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [4, 6], [5, 7], [8, 4], [8, 5], [9, 8]]) == [0, 1, 2, 3, 6, 7, 4, 5, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [4, 6], [5, 7], [8, 4], [8, 5], [9, 8]]) == [0, 1, 2, 3, 6, 7, 4, 5, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 5], [9, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 5], [9, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1]]) == [0, 1, 2, 3]
    assert candidate(numCourses = 7,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2]]) == [0, 1, 2, 3, 4, 5, 6]
    assert candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]) == [0, 1, 2, 3, 4]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [2, 1]]) == [0, 4, 5, 1, 2, 3]
    assert candidate(numCourses = 3,prerequisites = [[0, 1], [1, 2], [2, 0]]) == []
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [1, 2], [0, 1]]) == []
    assert candidate(numCourses = 3,prerequisites = [[0, 1], [0, 2], [1, 2]]) == [2, 1, 0]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [0, 1]]) == []
    assert candidate(numCourses = 5,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 4, 1, 2, 3]
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [7, 5]]) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(numCourses = 5,prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]) == [0, 4, 1, 2, 3]
    assert candidate(numCourses = 4,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert candidate(numCourses = 3,prerequisites = [[1, 0], [2, 1]]) == [0, 1, 2]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(numCourses = 1,prerequisites = []) == [0]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [5, 3]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(numCourses = 2,prerequisites = [[1, 0]]) == [0, 1]
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [2, 0], [3, 2], [4, 2], [5, 3], [5, 4], [6, 5], [7, 6], [8, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [10, 5], [11, 6], [11, 7], [11, 8], [11, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 2], [8, 2], [9, 3], [10, 3]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [7, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [12, 8], [12, 9], [13, 10], [13, 11], [14, 12], [14, 13], [15, 14], [16, 14], [17, 15], [17, 16], [18, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [10, 8], [11, 9], [12, 10], [13, 11], [14, 12], [15, 13], [16, 14], [17, 15], [18, 16], [19, 17], [18, 19]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 18]
    assert candidate(numCourses = 11,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [8, 4], [9, 5], [9, 6], [10, 7], [10, 8], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 2], [6, 3], [7, 4], [7, 5], [7, 6], [8, 4], [8, 5], [8, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [0, 8]]) == []
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9], [14, 10], [14, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 14,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [10, 6], [11, 7], [12, 8], [13, 9], [13, 10], [13, 11], [13, 12]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 1], [4, 3], [5, 2], [5, 3], [6, 3], [6, 4], [7, 3], [7, 4], [7, 5], [8, 4], [8, 5], [8, 6], [9, 4], [9, 5], [9, 6], [9, 7], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [16, 9], [16, 10], [16, 11], [16, 12], [16, 13], [16, 14], [16, 15], [17, 10], [17, 11], [17, 12], [17, 13], [17, 14], [17, 15], [17, 16], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15], [18, 16], [18, 17], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]) == []
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 5], [8, 5], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 6], [13, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 5], [11, 6], [10, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 6], [15, 7], [16, 7], [17, 8], [18, 8], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [12, 11], [13, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [4, 3], [5, 4], [6, 4], [7, 5], [7, 6], [8, 5], [8, 6], [8, 7], [9, 7], [10, 7], [10, 8], [11, 7], [11, 8], [11, 9], [11, 10], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [13, 9], [13, 10], [13, 11], [13, 12], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 1], [6, 2], [7, 3], [7, 4], [8, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9], [11, 10], [0, 11]]) == []
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8], [19, 16]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [6, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [1, 2], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5], [7, 6], [8, 7], [9, 7], [9, 8]]) == [0, 2, 1, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 18,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 1], [5, 3], [6, 2], [6, 4], [7, 3], [7, 4], [8, 5], [8, 6], [9, 5], [9, 6], [10, 7], [10, 8], [11, 7], [11, 8], [12, 9], [12, 10], [13, 10], [13, 11], [14, 12], [14, 13], [15, 13], [16, 14], [16, 15], [17, 15], [17, 16]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    assert candidate(numCourses = 5,prerequisites = [[1, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3]]) == [0, 1, 2, 3, 4]
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [7, 4], [7, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 5], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 3], [6, 3], [7, 4], [8, 4], [9, 7], [10, 7], [11, 8], [11, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 6], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [9, 4], [10, 5], [11, 5], [12, 6], [13, 7], [14, 7], [13, 14]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 13]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 3], [6, 3], [7, 4], [8, 5], [9, 5], [10, 6], [11, 6], [12, 7], [13, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [10, 5], [11, 6], [11, 7], [10, 8], [10, 9], [10, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 4], [8, 5], [9, 6], [7, 8]]) == [0, 1, 2, 3, 4, 5, 6, 8, 9, 7]
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [7, 5], [7, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [15, 6], [16, 7], [17, 7], [18, 8], [19, 8], [19, 9], [18, 10], [17, 11], [16, 12], [15, 13], [14, 14], [13, 15], [12, 16], [11, 17], [10, 18], [9, 19], [8, 19]]) == []
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [5, 9]]) == []
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [12, 10], [13, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [5, 6], [7, 8], [9, 7]]) == [0, 1, 2, 3, 4, 6, 8, 5, 7, 9]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [14, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 8,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5]]) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [10, 8], [11, 9], [12, 10], [12, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [2, 0], [3, 2], [3, 1], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(numCourses = 12,prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 6], [9, 7], [10, 8], [10, 9], [11, 10]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert candidate(numCourses = 6,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4]]) == [0, 1, 2, 3, 4, 5]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 4], [7, 4], [8, 5], [9, 5], [10, 5], [11, 6], [12, 7], [13, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [8, 3]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(numCourses = 20,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 1], [8, 2], [9, 2], [10, 2], [11, 3], [12, 3], [13, 4], [14, 4], [15, 5], [16, 5], [17, 6], [18, 6], [19, 7], [19, 8], [19, 9], [19, 10], [19, 11], [19, 12], [19, 13], [19, 14], [19, 15], [19, 16], [19, 17], [19, 18]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(numCourses = 13,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [9, 5], [10, 6], [10, 7], [11, 8], [11, 9], [12, 10], [12, 11]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 3], [9, 4], [10, 4], [11, 5], [12, 5], [13, 6], [14, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [4, 2], [5, 2], [6, 3], [7, 3], [8, 4], [8, 5], [9, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 15,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [10, 4], [11, 4], [12, 5], [13, 5], [14, 6], [13, 7], [12, 8], [11, 9], [10, 10], [9, 11], [8, 12], [7, 13], [6, 14]]) == []
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [6, 3], [6, 4], [7, 5], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [6, 3], [7, 4], [7, 5], [8, 6], [9, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 11,prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(numCourses = 16,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [5, 2], [6, 1], [6, 3], [7, 1], [7, 4], [8, 2], [8, 3], [8, 4], [9, 2], [9, 3], [9, 4], [10, 3], [10, 4], [11, 4], [12, 5], [12, 6], [12, 7], [12, 8], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [14, 6], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [15, 7], [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 3], [6, 4], [6, 5], [7, 6], [8, 6], [9, 7], [9, 8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(numCourses = 9,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 3], [8, 4], [8, 5], [8, 6], [8, 7]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 0], [4, 1], [5, 1], [6, 2], [7, 2], [8, 3], [9, 3], [4, 6], [5, 7], [8, 4], [8, 5], [9, 8]]) == [0, 1, 2, 3, 6, 7, 4, 5, 8, 9]
    assert candidate(numCourses = 10,prerequisites = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2], [7, 3], [8, 4], [9, 5], [9, 6]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


