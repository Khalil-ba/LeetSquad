def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,languages = [[1, 2], [2, 3], [3, 1]],friendships = [[1, 2], [2, 3], [3, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,languages = [[1, 2], [2, 3], [3, 1]],friendships = [[1, 2], [2, 3], [3, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,languages = [[1], [2], [1, 2]],friendships = [[1, 2], [1, 3], [2, 3]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,languages = [[1], [2], [1, 2]],friendships = [[1, 2], [1, 3], [2, 3]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 3], [2, 4], [1, 2], [3, 4]],friendships = [[1, 2], [2, 3], [3, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 3], [2, 4], [1, 2], [3, 4]],friendships = [[1, 2], [2, 3], [3, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [2, 3], [3, 4], [1, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [2, 3], [3, 4], [1, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,languages = [[2], [1, 3], [1, 2], [3]],friendships = [[1, 4], [1, 2], [3, 4], [2, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,languages = [[2], [1, 3], [1, 2], [3]],friendships = [[1, 4], [1, 2], [3, 4], [2, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,languages = [[1, 2], [1, 2]],friendships = [[1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,languages = [[1, 2], [1, 2]],friendships = [[1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,languages = [[1, 2, 3], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,languages = [[1, 2, 3], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 2], [3, 4], [1, 3], [2, 4]],friendships = [[1, 2], [1, 3], [2, 3], [3, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 2], [3, 4], [1, 3], [2, 4]],friendships = [[1, 2], [1, 3], [2, 3], [3, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1, 2, 3], [4, 5], [6, 7], [8, 9], [10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1, 2, 3], [4, 5], [6, 7], [8, 9], [10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,languages = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]],friendships = [[1, 2], [3, 4], [5, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,languages = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]],friendships = [[1, 2], [3, 4], [5, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [4, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4], [1, 4], [2, 3], [1, 2], [3, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [4, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4], [1, 4], [2, 3], [1, 2], [3, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 1], [10, 1, 2]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 1], [10, 1, 2]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 1]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 1]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,languages = [[1, 3], [2], [1, 2], [3, 2]],friendships = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,languages = [[1, 3], [2], [1, 2], [3, 2]],friendships = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 1], [9, 2]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 1], [9, 2]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2, 3], [4, 5], [1, 4], [2, 5], [3]],friendships = [[1, 4], [2, 5], [3, 5], [1, 3], [2, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2, 3], [4, 5], [1, 4], [2, 5], [3]],friendships = [[1, 4], [2, 5], [3, 5], [1, 3], [2, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,languages = [[1], [2], [3], [1, 2], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [4, 6]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,languages = [[1], [2], [3], [1, 2], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [4, 6]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1, 2, 3], [4, 5], [6, 7, 8], [9, 10], [1, 5, 9], [2, 6, 10], [3, 7, 4], [8, 1]],friendships = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 5], [2, 6], [3, 7], [4, 8], [5, 7], [6, 8]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1, 2, 3], [4, 5], [6, 7, 8], [9, 10], [1, 5, 9], [2, 6, 10], [3, 7, 4], [8, 1]],friendships = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 5], [2, 6], [3, 7], [4, 8], [5, 7], [6, 8]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,languages = [[1], [2], [3], [4], [5], [6], [7], [8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 1], [8, 2]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,languages = [[1], [2], [3], [4], [5], [6], [7], [8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 1], [8, 2]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,languages = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]],friendships = [[1, 3], [2, 4], [5, 7], [6, 8], [1, 5], [2, 6], [3, 7], [4, 8]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,languages = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]],friendships = [[1, 3], [2, 4], [5, 7], [6, 8], [1, 5], [2, 6], [3, 7], [4, 8]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 1], [8, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 1], [8, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 2], [3, 4], [2, 3], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 2], [3, 4], [2, 3], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 1], [7, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 1], [7, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1, 3, 5], [2, 4, 6], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 4], [2, 5], [3, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1, 3, 5], [2, 4, 6], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 4], [2, 5], [3, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,languages = [[1], [1, 3], [2], [2, 3], [3]],friendships = [[1, 3], [2, 3], [4, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,languages = [[1], [1, 3], [2], [2, 3], [3]],friendships = [[1, 3], [2, 3], [4, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1, 3, 5], [2, 4, 6], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 1], [2, 3, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1, 3, 5], [2, 4, 6], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 1], [2, 3, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,languages = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11], [8, 9, 10, 11, 12], [9, 10, 11, 12, 13], [10, 11, 12, 13, 14], [11, 12, 13, 14, 15], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 1], [15, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,languages = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11], [8, 9, 10, 11, 12], [9, 10, 11, 12, 13], [10, 11, 12, 13, 14], [11, 12, 13, 14, 15], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 1], [15, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1], [2], [3], [4], [5], [1, 2], [3, 4], [4, 5], [1, 3], [2, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1], [2], [3], [4], [5], [1, 2], [3, 4], [4, 5], [1, 3], [2, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,languages = [[1, 2], [3, 4], [5, 6], [7], [1, 3], [2, 4], [5, 7]],friendships = [[1, 3], [1, 5], [1, 7], [2, 4], [2, 6], [3, 5], [3, 7], [4, 6], [4, 7], [5, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,languages = [[1, 2], [3, 4], [5, 6], [7], [1, 3], [2, 4], [5, 7]],friendships = [[1, 3], [1, 5], [1, 7], [2, 4], [2, 6], [3, 5], [3, 7], [4, 6], [4, 7], [5, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,languages = [[1, 2, 3, 4], [5, 6], [7], [1, 2], [3, 4], [5, 6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,languages = [[1, 2, 3, 4], [5, 6], [7], [1, 2], [3, 4], [5, 6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [4, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [4, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,languages = [[1], [2], [3], [4], [5], [6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,languages = [[1], [2], [3], [4], [5], [6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,languages = [[1], [1], [1], [1], [2], [2], [2], [2]],friendships = [[1, 5], [2, 6], [3, 7], [4, 8]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,languages = [[1], [1], [1], [1], [2], [2], [2], [2]],friendships = [[1, 5], [2, 6], [3, 7], [4, 8]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]],friendships = [[1, 3], [3, 5], [5, 7], [7, 2], [2, 4], [4, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]],friendships = [[1, 3], [3, 5], [5, 7], [7, 2], [2, 4], [4, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,languages = [[1], [2], [3], [1, 4], [5, 6], [6, 7], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,languages = [[1], [2], [3], [1, 4], [5, 6], [6, 7], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1], [5, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1], [5, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,languages = [[1, 3, 5], [2, 4, 6], [1, 2, 3], [4, 5, 6], [1, 4, 7], [2, 5, 7], [3, 6, 7]],friendships = [[1, 2], [3, 4], [5, 6], [7, 1], [2, 5], [4, 7], [6, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,languages = [[1, 3, 5], [2, 4, 6], [1, 2, 3], [4, 5, 6], [1, 4, 7], [2, 5, 7], [3, 6, 7]],friendships = [[1, 2], [3, 4], [5, 6], [7, 1], [2, 5], [4, 7], [6, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [1, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [1, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,languages = [[1, 2], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3], [1, 2], [2, 3], [1, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,languages = [[1, 2], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3], [1, 2], [2, 3], [1, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,languages = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,languages = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 2], [3, 4], [2, 3], [1, 4], [1, 3]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 2], [3, 4], [2, 3], [1, 4], [1, 3]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 1], [4, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 1], [4, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2, 3, 4, 5]],friendships = [[1, 1], [1, 1], [1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2, 3, 4, 5]],friendships = [[1, 1], [1, 1], [1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,languages = [[1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [1, 8]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,languages = [[1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [1, 8]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5], [2, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5], [2, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2], [4, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2], [4, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1], [5, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1], [5, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,languages = [[1, 2, 3], [4, 5, 6], [1, 4], [2, 5], [3, 6], [1, 2, 3, 4, 5, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5], [2, 6]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,languages = [[1, 2, 3], [4, 5, 6], [1, 4], [2, 5], [3, 6], [1, 2, 3, 4, 5, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5], [2, 6]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,languages = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12], [1, 5, 9, 12], [2, 6, 10, 11], [3, 4, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],friendships = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [8, 9], [8, 10], [8, 11], [8, 12], [9, 10], [9, 11], [9, 12], [10, 11], [10, 12], [11, 12]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,languages = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12], [1, 5, 9, 12], [2, 6, 10, 11], [3, 4, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],friendships = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [8, 9], [8, 10], [8, 11], [8, 12], [9, 10], [9, 11], [9, 12], [10, 11], [10, 12], [11, 12]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,languages = [[1], [2], [3], [4], [5], [6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,languages = [[1], [2], [3], [4], [5], [6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,languages = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]],friendships = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,languages = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]],friendships = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,languages = [[1, 2], [3, 4], [1, 3], [2, 5], [4, 5]],friendships = [[1, 2], [3, 4], [2, 3], [4, 5], [1, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,languages = [[1, 2], [3, 4], [1, 3], [2, 5], [4, 5]],friendships = [[1, 2], [3, 4], [2, 3], [4, 5], [1, 3]]) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 3
    assert candidate(n = 3,languages = [[1, 2], [2, 3], [3, 1]],friendships = [[1, 2], [2, 3], [3, 1]]) == 0
    assert candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 0
    assert candidate(n = 2,languages = [[1], [2], [1, 2]],friendships = [[1, 2], [1, 3], [2, 3]]) == 1
    assert candidate(n = 4,languages = [[1, 3], [2, 4], [1, 2], [3, 4]],friendships = [[1, 2], [2, 3], [3, 4]]) == 2
    assert candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [2, 3], [3, 4], [1, 4]]) == 3
    assert candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 4
    assert candidate(n = 3,languages = [[2], [1, 3], [1, 2], [3]],friendships = [[1, 4], [1, 2], [3, 4], [2, 3]]) == 2
    assert candidate(n = 2,languages = [[1, 2], [1, 2]],friendships = [[1, 2]]) == 0
    assert candidate(n = 3,languages = [[1, 2, 3], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3]]) == 0
    assert candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0
    assert candidate(n = 4,languages = [[1, 2], [3, 4], [1, 3], [2, 4]],friendships = [[1, 2], [1, 3], [2, 3], [3, 4]]) == 2
    assert candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 4
    assert candidate(n = 4,languages = [[1], [2], [3], [4]],friendships = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]) == 3
    assert candidate(n = 10,languages = [[1, 2, 3], [4, 5], [6, 7], [8, 9], [10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5]]) == 4
    assert candidate(n = 6,languages = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]],friendships = [[1, 2], [3, 4], [5, 6]]) == 4
    assert candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [4, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4], [1, 4], [2, 3], [1, 2], [3, 4]]) == 2
    assert candidate(n = 10,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 1], [10, 1, 2]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 3
    assert candidate(n = 12,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 1]]) == 11
    assert candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 5
    assert candidate(n = 3,languages = [[1, 3], [2], [1, 2], [3, 2]],friendships = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]) == 1
    assert candidate(n = 9,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 1], [9, 2]]) == 7
    assert candidate(n = 5,languages = [[1, 2, 3], [4, 5], [1, 4], [2, 5], [3]],friendships = [[1, 4], [2, 5], [3, 5], [1, 3], [2, 4]]) == 1
    assert candidate(n = 3,languages = [[1], [2], [3], [1, 2], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [4, 6]]) == 2
    assert candidate(n = 10,languages = [[1, 2, 3], [4, 5], [6, 7, 8], [9, 10], [1, 5, 9], [2, 6, 10], [3, 7, 4], [8, 1]],friendships = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 5], [2, 6], [3, 7], [4, 8], [5, 7], [6, 8]]) == 5
    assert candidate(n = 8,languages = [[1], [2], [3], [4], [5], [6], [7], [8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 1], [8, 2]]) == 7
    assert candidate(n = 8,languages = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]],friendships = [[1, 3], [2, 4], [5, 7], [6, 8], [1, 5], [2, 6], [3, 7], [4, 8]]) == 6
    assert candidate(n = 8,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 1], [8, 2]]) == 6
    assert candidate(n = 4,languages = [[1, 2], [3, 4], [2, 3], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 2
    assert candidate(n = 9,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 1]]) == 0
    assert candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0
    assert candidate(n = 7,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 1], [7, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 0
    assert candidate(n = 10,languages = [[1, 3, 5], [2, 4, 6], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [1, 4], [2, 5], [3, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 7
    assert candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 9
    assert candidate(n = 5,languages = [[1], [2], [3], [4], [5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == 4
    assert candidate(n = 3,languages = [[1], [1, 3], [2], [2, 3], [3]],friendships = [[1, 3], [2, 3], [4, 5]]) == 1
    assert candidate(n = 10,languages = [[1, 3, 5], [2, 4, 6], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 1], [2, 3, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 6
    assert candidate(n = 10,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]) == 0
    assert candidate(n = 15,languages = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11], [8, 9, 10, 11, 12], [9, 10, 11, 12, 13], [10, 11, 12, 13, 14], [11, 12, 13, 14, 15], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12], [11, 13], [12, 14], [13, 15], [14, 1], [15, 2]]) == 2
    assert candidate(n = 5,languages = [[1], [2], [3], [4], [5], [1, 2], [3, 4], [4, 5], [1, 3], [2, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 7
    assert candidate(n = 7,languages = [[1, 2], [3, 4], [5, 6], [7], [1, 3], [2, 4], [5, 7]],friendships = [[1, 3], [1, 5], [1, 7], [2, 4], [2, 6], [3, 5], [3, 7], [4, 6], [4, 7], [5, 6]]) == 5
    assert candidate(n = 5,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1], [1, 3], [2, 4], [3, 5], [4, 1], [5, 2]]) == 3
    assert candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]) == 9
    assert candidate(n = 7,languages = [[1, 2, 3, 4], [5, 6], [7], [1, 2], [3, 4], [5, 6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 5
    assert candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [4, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0
    assert candidate(n = 7,languages = [[1], [2], [3], [4], [5], [6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 6
    assert candidate(n = 8,languages = [[1], [1], [1], [1], [2], [2], [2], [2]],friendships = [[1, 5], [2, 6], [3, 7], [4, 8]]) == 4
    assert candidate(n = 7,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]],friendships = [[1, 3], [3, 5], [5, 7], [7, 2], [2, 4], [4, 6]]) == 5
    assert candidate(n = 7,languages = [[1], [2], [3], [1, 4], [5, 6], [6, 7], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1]]) == 4
    assert candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1], [5, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0
    assert candidate(n = 7,languages = [[1, 3, 5], [2, 4, 6], [1, 2, 3], [4, 5, 6], [1, 4, 7], [2, 5, 7], [3, 6, 7]],friendships = [[1, 2], [3, 4], [5, 6], [7, 1], [2, 5], [4, 7], [6, 3]]) == 2
    assert candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 5
    assert candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [1, 4]]) == 0
    assert candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 5
    assert candidate(n = 6,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]) == 0
    assert candidate(n = 3,languages = [[1, 2], [2, 3], [1, 3]],friendships = [[1, 2], [2, 3], [1, 3], [1, 2], [2, 3], [1, 3]]) == 0
    assert candidate(n = 3,languages = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0
    assert candidate(n = 4,languages = [[1, 2], [3, 4], [2, 3], [1, 4], [1, 3]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) == 2
    assert candidate(n = 4,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 1], [4, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1]]) == 0
    assert candidate(n = 5,languages = [[1, 2, 3, 4, 5]],friendships = [[1, 1], [1, 1], [1, 1]]) == 0
    assert candidate(n = 4,languages = [[1, 2], [2, 3], [3, 4], [1, 4]],friendships = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]) == 2
    assert candidate(n = 10,languages = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],friendships = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]]) == 9
    assert candidate(n = 8,languages = [[1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [1, 8]]) == 1
    assert candidate(n = 6,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5], [2, 6]]) == 4
    assert candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2], [4, 5]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) == 2
    assert candidate(n = 5,languages = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1], [5, 1, 2]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]) == 0
    assert candidate(n = 10,languages = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [1, 10]]) == 0
    assert candidate(n = 6,languages = [[1, 2, 3], [4, 5, 6], [1, 4], [2, 5], [3, 6], [1, 2, 3, 4, 5, 6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5], [2, 6]]) == 3
    assert candidate(n = 6,languages = [[1], [2], [3], [4], [5], [6]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 1], [6, 2]]) == 5
    assert candidate(n = 12,languages = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12], [1, 5, 9, 12], [2, 6, 10, 11], [3, 4, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],friendships = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [8, 9], [8, 10], [8, 11], [8, 12], [9, 10], [9, 11], [9, 12], [10, 11], [10, 12], [11, 12]]) == 7
    assert candidate(n = 7,languages = [[1], [2], [3], [4], [5], [6], [7]],friendships = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 1], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 1], [7, 2]]) == 6
    assert candidate(n = 8,languages = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]],friendships = [[1, 2], [3, 4], [5, 6], [7, 8], [1, 3], [2, 4], [5, 7], [6, 8]]) == 6
    assert candidate(n = 5,languages = [[1, 2], [3, 4], [1, 3], [2, 5], [4, 5]],friendships = [[1, 2], [3, 4], [2, 3], [4, 5], [1, 3]]) == 2


