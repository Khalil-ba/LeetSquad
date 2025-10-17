def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,trust = []) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,trust = []) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,trust = [[1, 3], [2, 3], [3, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,trust = [[1, 3], [2, 3], [3, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,trust = [[1, 2], [1, 3], [1, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,trust = [[1, 2], [1, 3], [1, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,trust = [[1, 3], [2, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,trust = [[1, 3], [2, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,trust = [[1, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,trust = [[1, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,trust = [[1, 2], [2, 1], [1, 3], [3, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,trust = [[1, 2], [2, 1], [1, 3], [3, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 3], [2, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 3], [2, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,trust = [[1, 15], [2, 15], [3, 15], [4, 15], [5, 15], [6, 15], [7, 15], [8, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15], [14, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,trust = [[1, 15], [2, 15], [3, 15], [4, 15], [5, 15], [6, 15], [7, 15], [8, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15], [14, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 3], [2, 3], [3, 5], [4, 5], [5, 7], [6, 7], [7, 9], [8, 9], [9, 10], [10, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 3], [2, 3], [3, 5], [4, 5], [5, 7], [6, 7], [7, 9], [8, 9], [9, 10], [10, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [5, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [5, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 1], [4, 2], [5, 1], [5, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 1], [4, 2], [5, 1], [5, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,trust = [[1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,trust = [[1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 5], [2, 5], [3, 5], [4, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 5], [2, 5], [3, 5], [4, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [4, 6]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [4, 6]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,trust = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,trust = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,trust = [[1, 13], [2, 13], [3, 13], [4, 13], [5, 13], [6, 13], [7, 13], [8, 13], [9, 13], [10, 13], [11, 13], [12, 13]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,trust = [[1, 13], [2, 13], [3, 13], [4, 13], [5, 13], [6, 13], [7, 13], [8, 13], [9, 13], [10, 13], [11, 13], [12, 13]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [8, 7], [9, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [8, 7], [9, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 3], [2, 3], [4, 5], [5, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 3], [2, 3], [4, 5], [5, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [5, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [5, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 3], [2, 3], [4, 3], [5, 3], [1, 5], [2, 5], [4, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 3], [2, 3], [4, 3], [5, 3], [1, 5], [2, 5], [4, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [9, 8], [10, 8]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [9, 8], [10, 8]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 3], [2, 3], [3, 1], [4, 5], [5, 4], [1, 5], [2, 6], [6, 2], [3, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 3], [2, 3], [3, 1], [4, 5], [5, 4], [1, 5], [2, 6], [6, 2], [3, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [5, 8]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [5, 8]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [10, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [10, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,trust = [[1, 2], [1, 3], [2, 3], [3, 1], [4, 5], [4, 6], [5, 6], [6, 4], [7, 8], [7, 9], [8, 9], [9, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,trust = [[1, 2], [1, 3], [2, 3], [3, 1], [4, 5], [4, 6], [5, 6], [6, 4], [7, 8], [7, 9], [8, 9], [9, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [7, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [7, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,trust = [[1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,trust = [[1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 2], [2, 1], [3, 4], [4, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 2], [2, 1], [3, 4], [4, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 7], [8, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 7], [8, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 2], [8, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 2], [8, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [1, 2], [2, 1], [1, 3], [3, 1], [1, 4], [4, 1], [1, 5], [5, 1], [1, 6], [6, 1], [1, 7], [7, 1], [1, 8], [8, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [1, 2], [2, 1], [1, 3], [3, 1], [1, 4], [4, 1], [1, 5], [5, 1], [1, 6], [6, 1], [1, 7], [7, 1], [1, 8], [8, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 3], [2, 3], [4, 3], [5, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 3], [2, 3], [4, 3], [5, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,trust = [[1, 20], [2, 20], [3, 20], [4, 20], [5, 20], [6, 20], [7, 20], [8, 20], [9, 20], [10, 20], [11, 20], [12, 20], [13, 20], [14, 20], [15, 20], [16, 20], [17, 20], [18, 20], [19, 20], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,trust = [[1, 20], [2, 20], [3, 20], [4, 20], [5, 20], [6, 20], [7, 20], [8, 20], [9, 20], [10, 20], [11, 20], [12, 20], [13, 20], [14, 20], [15, 20], [16, 20], [17, 20], [18, 20], [19, 20], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [1, 5], [2, 5], [3, 5], [5, 6], [6, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [1, 5], [2, 5], [3, 5], [5, 6], [6, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 3], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 3], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 3], [2, 3], [3, 1], [4, 5], [5, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 3], [2, 3], [3, 1], [4, 5], [5, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [7, 6], [8, 6]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [7, 6], [8, 6]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 2], [2, 1], [3, 4], [4, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 2], [2, 1], [3, 4], [4, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,trust = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100], [6, 100], [7, 100], [8, 100], [9, 100], [10, 100], [11, 100], [12, 100], [13, 100], [14, 100], [15, 100], [16, 100], [17, 100], [18, 100], [19, 100], [20, 100], [21, 100], [22, 100], [23, 100], [24, 100], [25, 100], [26, 100], [27, 100], [28, 100], [29, 100], [30, 100], [31, 100], [32, 100], [33, 100], [34, 100], [35, 100], [36, 100], [37, 100], [38, 100], [39, 100], [40, 100], [41, 100], [42, 100], [43, 100], [44, 100], [45, 100], [46, 100], [47, 100], [48, 100], [49, 100], [50, 100], [51, 100], [52, 100], [53, 100], [54, 100], [55, 100], [56, 100], [57, 100], [58, 100], [59, 100], [60, 100], [61, 100], [62, 100], [63, 100], [64, 100], [65, 100], [66, 100], [67, 100], [68, 100], [69, 100], [70, 100], [71, 100], [72, 100], [73, 100], [74, 100], [75, 100], [76, 100], [77, 100], [78, 100], [79, 100], [80, 100], [81, 100], [82, 100], [83, 100], [84, 100], [85, 100], [86, 100], [87, 100], [88, 100], [89, 100], [90, 100], [91, 100], [92, 100], [93, 100], [94, 100], [95, 100], [96, 100], [97, 100], [98, 100], [99, 100]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,trust = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100], [6, 100], [7, 100], [8, 100], [9, 100], [10, 100], [11, 100], [12, 100], [13, 100], [14, 100], [15, 100], [16, 100], [17, 100], [18, 100], [19, 100], [20, 100], [21, 100], [22, 100], [23, 100], [24, 100], [25, 100], [26, 100], [27, 100], [28, 100], [29, 100], [30, 100], [31, 100], [32, 100], [33, 100], [34, 100], [35, 100], [36, 100], [37, 100], [38, 100], [39, 100], [40, 100], [41, 100], [42, 100], [43, 100], [44, 100], [45, 100], [46, 100], [47, 100], [48, 100], [49, 100], [50, 100], [51, 100], [52, 100], [53, 100], [54, 100], [55, 100], [56, 100], [57, 100], [58, 100], [59, 100], [60, 100], [61, 100], [62, 100], [63, 100], [64, 100], [65, 100], [66, 100], [67, 100], [68, 100], [69, 100], [70, 100], [71, 100], [72, 100], [73, 100], [74, 100], [75, 100], [76, 100], [77, 100], [78, 100], [79, 100], [80, 100], [81, 100], [82, 100], [83, 100], [84, 100], [85, 100], [86, 100], [87, 100], [88, 100], [89, 100], [90, 100], [91, 100], [92, 100], [93, 100], [94, 100], [95, 100], [96, 100], [97, 100], [98, 100], [99, 100]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [9, 5], [1, 10], [2, 10], [3, 10], [4, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [9, 5], [1, 10], [2, 10], [3, 10], [4, 10]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,trust = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,trust = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
    assert candidate(n = 1,trust = []) == 1
    assert candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == -1
    assert candidate(n = 3,trust = [[1, 3], [2, 3], [3, 1]]) == -1
    assert candidate(n = 4,trust = [[1, 2], [1, 3], [1, 4]]) == -1
    assert candidate(n = 3,trust = [[1, 3], [2, 3]]) == 3
    assert candidate(n = 2,trust = [[1, 2]]) == 2
    assert candidate(n = 3,trust = [[1, 2], [2, 1], [1, 3], [3, 1]]) == -1
    assert candidate(n = 8,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == -1
    assert candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 1]]) == -1
    assert candidate(n = 8,trust = [[1, 3], [2, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3]]) == 3
    assert candidate(n = 15,trust = [[1, 15], [2, 15], [3, 15], [4, 15], [5, 15], [6, 15], [7, 15], [8, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15], [14, 15]]) == 15
    assert candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 5]]) == -1
    assert candidate(n = 10,trust = [[1, 3], [2, 3], [3, 5], [4, 5], [5, 7], [6, 7], [7, 9], [8, 9], [9, 10], [10, 1]]) == -1
    assert candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [5, 4]]) == 4
    assert candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8]]) == 8
    assert candidate(n = 10,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 5
    assert candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7]]) == 7
    assert candidate(n = 5,trust = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 1], [4, 2], [5, 1], [5, 3]]) == -1
    assert candidate(n = 11,trust = [[1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]]) == 11
    assert candidate(n = 5,trust = [[1, 5], [2, 5], [3, 5], [4, 5]]) == 5
    assert candidate(n = 6,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [4, 6]]) == -1
    assert candidate(n = 9,trust = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == -1
    assert candidate(n = 13,trust = [[1, 13], [2, 13], [3, 13], [4, 13], [5, 13], [6, 13], [7, 13], [8, 13], [9, 13], [10, 13], [11, 13], [12, 13]]) == 13
    assert candidate(n = 9,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [8, 7], [9, 7]]) == 7
    assert candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 1]]) == -1
    assert candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]]) == 9
    assert candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 6
    assert candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 10
    assert candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5]]) == -1
    assert candidate(n = 6,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 2]]) == -1
    assert candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == -1
    assert candidate(n = 10,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == -1
    assert candidate(n = 5,trust = [[1, 3], [2, 3], [4, 5], [5, 4]]) == -1
    assert candidate(n = 7,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [5, 1]]) == -1
    assert candidate(n = 5,trust = [[1, 3], [2, 3], [4, 3], [5, 3], [1, 5], [2, 5], [4, 5]]) == 3
    assert candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 1]]) == -1
    assert candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 1]]) == -1
    assert candidate(n = 5,trust = [[1, 4], [2, 4], [3, 4], [4, 5], [5, 4]]) == -1
    assert candidate(n = 10,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [9, 8], [10, 8]]) == 8
    assert candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 1]]) == 12
    assert candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12]]) == 12
    assert candidate(n = 6,trust = [[1, 3], [2, 3], [3, 1], [4, 5], [5, 4], [1, 5], [2, 6], [6, 2], [3, 4]]) == -1
    assert candidate(n = 8,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [5, 8]]) == -1
    assert candidate(n = 10,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1
    assert candidate(n = 10,trust = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == -1
    assert candidate(n = 10,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [10, 1]]) == -1
    assert candidate(n = 8,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5]]) == 5
    assert candidate(n = 9,trust = [[1, 2], [1, 3], [2, 3], [3, 1], [4, 5], [4, 6], [5, 6], [6, 4], [7, 8], [7, 9], [8, 9], [9, 7]]) == -1
    assert candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [7, 4]]) == 4
    assert candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 7]]) == -1
    assert candidate(n = 11,trust = [[1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 11
    assert candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 10]]) == -1
    assert candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9]]) == -1
    assert candidate(n = 5,trust = [[1, 2], [2, 1], [3, 4], [4, 3]]) == -1
    assert candidate(n = 10,trust = [[2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 1
    assert candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 7], [8, 1]]) == -1
    assert candidate(n = 8,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 2], [8, 3]]) == -1
    assert candidate(n = 5,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == -1
    assert candidate(n = 6,trust = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == -1
    assert candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [1, 2], [2, 1], [1, 3], [3, 1], [1, 4], [4, 1], [1, 5], [5, 1], [1, 6], [6, 1], [1, 7], [7, 1], [1, 8], [8, 1]]) == 9
    assert candidate(n = 5,trust = [[1, 3], [2, 3], [4, 3], [5, 3]]) == 3
    assert candidate(n = 20,trust = [[1, 20], [2, 20], [3, 20], [4, 20], [5, 20], [6, 20], [7, 20], [8, 20], [9, 20], [10, 20], [11, 20], [12, 20], [13, 20], [14, 20], [15, 20], [16, 20], [17, 20], [18, 20], [19, 20], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 1]]) == 20
    assert candidate(n = 10,trust = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == -1
    assert candidate(n = 5,trust = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]) == 5
    assert candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6]]) == 6
    assert candidate(n = 8,trust = [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 8
    assert candidate(n = 7,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [1, 5], [2, 5], [3, 5], [5, 6], [6, 7]]) == -1
    assert candidate(n = 6,trust = [[1, 3], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 4]]) == -1
    assert candidate(n = 9,trust = [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9]]) == 9
    assert candidate(n = 5,trust = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 4]]) == -1
    assert candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 7
    assert candidate(n = 7,trust = [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 1]]) == -1
    assert candidate(n = 6,trust = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6]]) == -1
    assert candidate(n = 5,trust = [[1, 3], [2, 3], [3, 1], [4, 5], [5, 4]]) == -1
    assert candidate(n = 8,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [7, 6], [8, 6]]) == 6
    assert candidate(n = 12,trust = [[1, 12], [2, 12], [3, 12], [4, 12], [5, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 1]]) == -1
    assert candidate(n = 6,trust = [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 2], [2, 1], [3, 4], [4, 3]]) == 6
    assert candidate(n = 10,trust = [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 10
    assert candidate(n = 10,trust = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == -1
    assert candidate(n = 5,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [5, 1]]) == -1
    assert candidate(n = 100,trust = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100], [6, 100], [7, 100], [8, 100], [9, 100], [10, 100], [11, 100], [12, 100], [13, 100], [14, 100], [15, 100], [16, 100], [17, 100], [18, 100], [19, 100], [20, 100], [21, 100], [22, 100], [23, 100], [24, 100], [25, 100], [26, 100], [27, 100], [28, 100], [29, 100], [30, 100], [31, 100], [32, 100], [33, 100], [34, 100], [35, 100], [36, 100], [37, 100], [38, 100], [39, 100], [40, 100], [41, 100], [42, 100], [43, 100], [44, 100], [45, 100], [46, 100], [47, 100], [48, 100], [49, 100], [50, 100], [51, 100], [52, 100], [53, 100], [54, 100], [55, 100], [56, 100], [57, 100], [58, 100], [59, 100], [60, 100], [61, 100], [62, 100], [63, 100], [64, 100], [65, 100], [66, 100], [67, 100], [68, 100], [69, 100], [70, 100], [71, 100], [72, 100], [73, 100], [74, 100], [75, 100], [76, 100], [77, 100], [78, 100], [79, 100], [80, 100], [81, 100], [82, 100], [83, 100], [84, 100], [85, 100], [86, 100], [87, 100], [88, 100], [89, 100], [90, 100], [91, 100], [92, 100], [93, 100], [94, 100], [95, 100], [96, 100], [97, 100], [98, 100], [99, 100]]) == 100
    assert candidate(n = 6,trust = [[1, 4], [2, 4], [3, 4], [5, 4], [6, 4]]) == 4
    assert candidate(n = 7,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5]]) == 5
    assert candidate(n = 10,trust = [[1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [9, 5], [1, 10], [2, 10], [3, 10], [4, 10]]) == -1
    assert candidate(n = 10,trust = [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == -1


