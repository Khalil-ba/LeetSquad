def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,edges = [[0, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,edges = [[0, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[0, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[0, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,edges = []) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,edges = []) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [0, 2], [1, 3], [2, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [0, 2], [1, 3], [2, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[0, 1], [1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[0, 1], [1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [0, 2], [0, 3], [0, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [0, 2], [0, 3], [0, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [2, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [2, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,edges = []) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,edges = []) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[1, 2], [2, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[1, 2], [2, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [2, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [2, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,edges = [[1, 0], [2, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,edges = [[1, 0], [2, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 2], [1, 3], [1, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 2], [1, 3], [1, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [0, 2], [0, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [0, 2], [0, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [2, 3], [3, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [2, 3], [3, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [0, 2], [3, 4], [5, 6]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [0, 2], [3, 4], [5, 6]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [2, 0], [3, 4]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [2, 0], [3, 4]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 10], [9, 11], [10, 11]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 10], [9, 11], [10, 11]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [4, 6], [5, 7], [8, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [4, 6], [5, 7], [8, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [0, 2], [3, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [0, 2], [3, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 6], [4, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 6], [4, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [6, 6]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [6, 6]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3], [3, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3], [3, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5], [0, 2], [1, 3], [4, 0], [5, 1], [2, 4], [3, 5]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5], [0, 2], [1, 3], [4, 0], [5, 1], [2, 4], [3, 5]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [3, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [3, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [1, 6], [2, 7], [2, 8], [2, 9], [3, 10], [3, 11], [3, 12], [4, 13], [5, 13], [6, 13], [7, 14], [8, 14], [9, 14]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [1, 6], [2, 7], [2, 8], [2, 9], [3, 10], [3, 11], [3, 12], [4, 13], [5, 13], [6, 13], [7, 14], [8, 14], [9, 14]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 6], [7, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 6], [7, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 7], [6, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 7], [6, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,edges = [[1, 2], [2, 3], [3, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,edges = [[1, 2], [2, 3], [3, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,edges = [[0, 2], [0, 3], [1, 2], [1, 4], [2, 5], [3, 5], [4, 5], [5, 6], [6, 7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,edges = [[0, 2], [0, 3], [1, 2], [1, 4], [2, 5], [3, 5], [4, 5], [5, 6], [6, 7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 6], [4, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 6], [4, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 6]]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == 0
    assert candidate(n = 2,edges = [[0, 1]]) == 0
    assert candidate(n = 3,edges = [[0, 1]]) == -1
    assert candidate(n = 2,edges = []) == -1
    assert candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5]]) == -1
    assert candidate(n = 4,edges = [[0, 1], [0, 2], [1, 3], [2, 3]]) == 0
    assert candidate(n = 6,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == 0
    assert candidate(n = 3,edges = [[0, 1], [1, 2]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [0, 2], [0, 3], [0, 4]]) == 0
    assert candidate(n = 4,edges = [[0, 1], [2, 3]]) == -1
    assert candidate(n = 1,edges = []) == 0
    assert candidate(n = 3,edges = [[1, 2], [2, 0]]) == 1
    assert candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [2, 4]]) == 0
    assert candidate(n = 3,edges = [[1, 0], [2, 0]]) == -1
    assert candidate(n = 4,edges = [[0, 2], [1, 3], [1, 2]]) == -1
    assert candidate(n = 4,edges = [[0, 1], [0, 2], [0, 3]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [2, 3], [3, 4]]) == -1
    assert candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5]]) == -1
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 5]]) == 0
    assert candidate(n = 7,edges = [[0, 1], [0, 2], [3, 4], [5, 6]]) == -1
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [2, 0], [3, 4]]) == 3
    assert candidate(n = 5,edges = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4]]) == 0
    assert candidate(n = 12,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 0
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9]]) == -1
    assert candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 8], [6, 8], [7, 9], [8, 10], [9, 11], [10, 11]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4]]) == -1
    assert candidate(n = 10,edges = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 2], [1, 3], [4, 6], [5, 7], [8, 0]]) == -1
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 0
    assert candidate(n = 12,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [6, 8]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [0, 2], [3, 4]]) == -1
    assert candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3]]) == 0
    assert candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7]]) == 0
    assert candidate(n = 9,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 0
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 4]]) == 0
    assert candidate(n = 6,edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0], [5, 1]]) == -1
    assert candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 6], [4, 6]]) == 0
    assert candidate(n = 7,edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3], [6, 6]]) == -1
    assert candidate(n = 6,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [3, 4], [4, 5]]) == 0
    assert candidate(n = 4,edges = [[0, 1], [1, 2], [2, 3], [3, 0]]) == -1
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == -1
    assert candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == 0
    assert candidate(n = 6,edges = [[0, 1], [2, 3], [4, 5], [0, 2], [1, 3], [4, 0], [5, 1], [2, 4], [3, 5]]) == -1
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 0
    assert candidate(n = 7,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [3, 6]]) == 0
    assert candidate(n = 9,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 0
    assert candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 0
    assert candidate(n = 10,edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == 1
    assert candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 3], [2, 4]]) == 0
    assert candidate(n = 7,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 0]]) == -1
    assert candidate(n = 6,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]) == -1
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
    assert candidate(n = 11,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]]) == 0
    assert candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9]]) == 0
    assert candidate(n = 15,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]) == -1
    assert candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 9]]) == 0
    assert candidate(n = 15,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [1, 6], [2, 7], [2, 8], [2, 9], [3, 10], [3, 11], [3, 12], [4, 13], [5, 13], [6, 13], [7, 14], [8, 14], [9, 14]]) == 0
    assert candidate(n = 6,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4], [4, 5]]) == 0
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0]]) == -1
    assert candidate(n = 5,edges = [[0, 1], [0, 2], [1, 3], [1, 4]]) == 0
    assert candidate(n = 12,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 6], [7, 8]]) == 0
    assert candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 7], [6, 8]]) == 0
    assert candidate(n = 4,edges = [[1, 2], [2, 3], [3, 0]]) == 1
    assert candidate(n = 8,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 7], [5, 7], [6, 7]]) == 0
    assert candidate(n = 5,edges = [[0, 1], [1, 2], [2, 3], [3, 4]]) == 0
    assert candidate(n = 8,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 4]]) == 0
    assert candidate(n = 8,edges = [[0, 2], [0, 3], [1, 2], [1, 4], [2, 5], [3, 5], [4, 5], [5, 6], [6, 7]]) == -1
    assert candidate(n = 10,edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [0, 9]]) == 0
    assert candidate(n = 9,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8]]) == 0
    assert candidate(n = 6,edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == -1
    assert candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 0
    assert candidate(n = 7,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 6], [4, 5]]) == 0
    assert candidate(n = 10,edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [2, 7], [3, 8], [3, 9]]) == 0
    assert candidate(n = 10,edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 6]]) == 0


