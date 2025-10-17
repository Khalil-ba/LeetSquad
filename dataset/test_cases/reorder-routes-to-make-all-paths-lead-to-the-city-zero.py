def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 7,connections = [[1, 0], [2, 0], [3, 1], [4, 0], [5, 0], [6, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,connections = [[1, 0], [2, 0], [3, 1], [4, 0], [5, 0], [6, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,connections = [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,connections = [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,connections = [[0, 1], [0, 2], [3, 2], [4, 2], [5, 4], [6, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,connections = [[0, 1], [0, 2], [3, 2], [4, 2], [5, 4], [6, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,connections = [[2, 0], [3, 0], [1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,connections = [[2, 0], [3, 0], [1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[0, 1], [2, 0], [3, 2], [4, 2], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[0, 1], [2, 0], [3, 2], [4, 2], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,connections = [[1, 0], [2, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,connections = [[1, 0], [2, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,connections = [[0, 1], [0, 2], [3, 2], [4, 3], [5, 4], [6, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,connections = [[0, 1], [0, 2], [3, 2], [4, 3], [5, 4], [6, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,connections = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,connections = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [7, 16], [7, 17], [8, 18], [8, 19]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [7, 16], [7, 17], [8, 18], [8, 19]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20], [10, 21], [10, 22], [11, 23], [11, 24], [12, 25], [12, 26], [13, 27], [13, 28], [14, 29]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20], [10, 21], [10, 22], [11, 23], [11, 24], [12, 25], [12, 26], [13, 27], [13, 28], [14, 29]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,connections = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [6, 7], [0, 8], [8, 9], [9, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,connections = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [6, 7], [0, 8], [8, 9], [9, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [9, 10], [10, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [9, 10], [10, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [5, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [13, 14]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [5, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [13, 14]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,connections = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9], [5, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,connections = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9], [5, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 16,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14], [8, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14], [8, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 16,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[9, 0], [7, 6], [3, 2], [4, 2], [6, 3], [0, 5], [8, 0], [0, 9]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[9, 0], [7, 6], [3, 2], [4, 2], [6, 3], [0, 5], [8, 0], [0, 9]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11], [6, 12], [7, 13]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11], [6, 12], [7, 13]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [0, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [0, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 12], [12, 13]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 12], [12, 13]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17], [10, 18], [11, 19]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17], [10, 18], [11, 19]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [6, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [6, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,connections = [[0, 1], [1, 2], [0, 3], [3, 4], [2, 5], [5, 6], [4, 7], [7, 8]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,connections = [[0, 1], [1, 2], [0, 3], [3, 4], [2, 5], [5, 6], [4, 7], [7, 8]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [11, 12]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [11, 12]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [8, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [8, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20], [10, 21], [10, 22], [11, 23], [11, 24]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20], [10, 21], [10, 22], [11, 23], [11, 24]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [1, 15], [15, 16], [16, 17]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [1, 15], [15, 16], [16, 17]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 21,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 21,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,connections = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [2, 7], [7, 8], [8, 9], [0, 10], [10, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,connections = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [2, 7], [7, 8], [8, 9], [0, 10], [10, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 14,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 7,connections = [[1, 0], [2, 0], [3, 1], [4, 0], [5, 0], [6, 4]]) == 0
    assert candidate(n = 6,connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert candidate(n = 5,connections = [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert candidate(n = 10,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9
    assert candidate(n = 7,connections = [[0, 1], [0, 2], [3, 2], [4, 2], [5, 4], [6, 4]]) == 2
    assert candidate(n = 4,connections = [[2, 0], [3, 0], [1, 2]]) == 0
    assert candidate(n = 10,connections = [[0, 1], [2, 0], [3, 2], [4, 2], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]) == 1
    assert candidate(n = 7,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 6
    assert candidate(n = 3,connections = [[1, 0], [2, 0]]) == 0
    assert candidate(n = 7,connections = [[0, 1], [0, 2], [3, 2], [4, 3], [5, 4], [6, 5]]) == 2
    assert candidate(n = 7,connections = [[1, 0], [2, 0], [3, 1], [4, 1], [5, 2], [6, 2]]) == 0
    assert candidate(n = 20,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [7, 16], [7, 17], [8, 18], [8, 19]]) == 19
    assert candidate(n = 12,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 11
    assert candidate(n = 30,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20], [10, 21], [10, 22], [11, 23], [11, 24], [12, 25], [12, 26], [13, 27], [13, 28], [14, 29]]) == 29
    assert candidate(n = 11,connections = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [6, 7], [0, 8], [8, 9], [9, 10]]) == 10
    assert candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [9, 10], [10, 11]]) == 11
    assert candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17]]) == 17
    assert candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9]]) == 9
    assert candidate(n = 15,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [5, 8], [5, 9], [6, 10], [7, 11], [8, 12], [9, 13], [13, 14]]) == 14
    assert candidate(n = 11,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 10
    assert candidate(n = 11,connections = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9], [5, 10]]) == 10
    assert candidate(n = 15,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14]]) == 14
    assert candidate(n = 13,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [7, 12]]) == 12
    assert candidate(n = 18,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17]]) == 17
    assert candidate(n = 15,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14]]) == 14
    assert candidate(n = 16,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [5, 11], [6, 12], [6, 13], [7, 14], [8, 15]]) == 15
    assert candidate(n = 16,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15]]) == 15
    assert candidate(n = 9,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8]]) == 8
    assert candidate(n = 8,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 5]]) == 6
    assert candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11]]) == 11
    assert candidate(n = 12,connections = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [4, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 11
    assert candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19]]) == 19
    assert candidate(n = 10,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9]]) == 9
    assert candidate(n = 10,connections = [[9, 0], [7, 6], [3, 2], [4, 2], [6, 3], [0, 5], [8, 0], [0, 9]]) == 2
    assert candidate(n = 12,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11]]) == 11
    assert candidate(n = 12,connections = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 11
    assert candidate(n = 10,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9
    assert candidate(n = 14,connections = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 11], [6, 12], [7, 13]]) == 13
    assert candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [0, 15], [15, 16], [16, 17], [17, 18], [18, 19]]) == 19
    assert candidate(n = 12,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11]]) == 11
    assert candidate(n = 14,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 12], [12, 13]]) == 13
    assert candidate(n = 9,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 8
    assert candidate(n = 8,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 7
    assert candidate(n = 20,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17], [10, 18], [11, 19]]) == 19
    assert candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [6, 9]]) == 9
    assert candidate(n = 9,connections = [[0, 1], [1, 2], [0, 3], [3, 4], [2, 5], [5, 6], [4, 7], [7, 8]]) == 8
    assert candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [8, 16], [9, 17]]) == 17
    assert candidate(n = 13,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 10], [6, 11], [11, 12]]) == 12
    assert candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [8, 9]]) == 9
    assert candidate(n = 25,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20], [10, 21], [10, 22], [11, 23], [11, 24]]) == 24
    assert candidate(n = 18,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [1, 15], [15, 16], [16, 17]]) == 17
    assert candidate(n = 21,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16], [8, 17], [8, 18], [9, 19], [9, 20]]) == 20
    assert candidate(n = 12,connections = [[0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [2, 7], [7, 8], [8, 9], [0, 10], [10, 11]]) == 11
    assert candidate(n = 15,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 14
    assert candidate(n = 15,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]) == 14
    assert candidate(n = 14,connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]]) == 13
    assert candidate(n = 10,connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 9


