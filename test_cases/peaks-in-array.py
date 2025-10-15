def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 2, 5],queries = [[2, 3, 4], [1, 0, 4]]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 2, 5],queries = [[2, 3, 4], [1, 0, 4]]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 4, 2, 1, 5],queries = [[2, 2, 4], [1, 0, 2], [1, 0, 4]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 4, 2, 1, 5],queries = [[2, 2, 4], [1, 0, 2], [1, 0, 4]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 1, 8], [2, 3, 1], [1, 1, 8], [2, 5, 7], [1, 0, 4]]) == [3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 1, 8], [2, 3, 1], [1, 1, 8], [2, 5, 7], [1, 0, 4]]) == [3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 7], [2, 2, 6], [2, 4, 3], [1, 0, 8]]) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 7], [2, 2, 6], [2, 4, 3], [1, 0, 8]]) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[2, 0, 10], [1, 1, 11], [2, 1, 9], [1, 1, 11], [2, 2, 8], [1, 1, 11], [2, 3, 7], [1, 1, 11], [2, 4, 6], [1, 1, 11]]) == [3, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[2, 0, 10], [1, 1, 11], [2, 1, 9], [1, 1, 11], [2, 2, 8], [1, 1, 11], [2, 3, 7], [1, 1, 11], [2, 4, 6], [1, 1, 11]]) == [3, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 10, 8], [1, 0, 28], [2, 15, 13], [1, 8, 20]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 10, 8], [1, 0, 28], [2, 15, 13], [1, 8, 20]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 1, 13], [2, 7, 1], [1, 1, 13]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 1, 13], [2, 7, 1], [1, 1, 13]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 10], [2, 4, 3], [1, 3, 11], [2, 8, 4], [1, 0, 12]]) == [4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 10], [2, 4, 3], [1, 3, 11], [2, 8, 4], [1, 0, 12]]) == [4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 0, 8], [2, 1, 3], [1, 0, 8], [2, 3, 5], [1, 0, 8], [2, 5, 7], [1, 0, 8]]) == [3, 3, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 0, 8], [2, 1, 3], [1, 0, 8], [2, 3, 5], [1, 0, 8], [2, 5, 7], [1, 0, 8]]) == [3, 3, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 1, 10], [1, 0, 8], [2, 3, 9], [1, 2, 7]]) == [0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 1, 10], [1, 0, 8], [2, 3, 9], [1, 2, 7]]) == [0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 0, 14], [2, 6, 10], [1, 0, 14], [2, 4, 8], [1, 0, 14], [2, 7, 11], [1, 0, 14]]) == [0, 1, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 0, 14], [2, 6, 10], [1, 0, 14], [2, 4, 8], [1, 0, 14], [2, 7, 11], [1, 0, 14]]) == [0, 1, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 14], [2, 7, 18], [1, 0, 14], [2, 10, 12], [1, 0, 14]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 14], [2, 7, 18], [1, 0, 14], [2, 10, 12], [1, 0, 14]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10],queries = [[1, 0, 8], [2, 1, 25], [1, 0, 8], [2, 3, 30], [1, 0, 8]]) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10],queries = [[1, 0, 8], [2, 1, 25], [1, 0, 8], [2, 3, 30], [1, 0, 8]]) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100],queries = [[1, 1, 7], [2, 2, 150], [1, 0, 8], [2, 4, 200], [1, 0, 8]]) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100],queries = [[1, 1, 7], [2, 2, 150], [1, 0, 8], [2, 4, 200], [1, 0, 8]]) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 9], [2, 2, 8], [1, 1, 9], [2, 4, 6], [1, 1, 9], [2, 6, 4], [1, 1, 9]]) == [0, 1, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 9], [2, 2, 8], [1, 1, 9], [2, 4, 6], [1, 1, 9], [2, 6, 4], [1, 1, 9]]) == [0, 1, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],queries = [[2, 2, 5], [1, 0, 9], [2, 6, 8], [1, 1, 8]]) == [4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],queries = [[2, 2, 5], [1, 0, 9], [2, 6, 8], [1, 1, 8]]) == [4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, 8, 3, 9, 4, 10, 5, 11, 6, 12, 7, 13, 8, 14, 9, 15],queries = [[1, 0, 16], [2, 1, 5], [1, 3, 15], [2, 9, 12], [1, 0, 16]]) == [7, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, 8, 3, 9, 4, 10, 5, 11, 6, 12, 7, 13, 8, 14, 9, 15],queries = [[1, 0, 16], [2, 1, 5], [1, 3, 15], [2, 9, 12], [1, 0, 16]]) == [7, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 8], [2, 4, 3], [1, 1, 8], [2, 6, 2], [1, 1, 8]]) == [3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 8], [2, 4, 3], [1, 1, 8], [2, 6, 2], [1, 1, 8]]) == [3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9],queries = [[2, 2, 4], [1, 0, 16], [2, 8, 7], [1, 6, 12]]) == [6, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9],queries = [[2, 2, 4], [1, 0, 16], [2, 8, 7], [1, 6, 12]]) == [6, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4],queries = [[1, 1, 13], [2, 2, 3], [1, 1, 13], [2, 4, 5], [1, 1, 13], [2, 6, 7], [1, 1, 13], [2, 8, 9], [1, 1, 13], [2, 10, 11], [1, 1, 13], [2, 12, 13], [1, 1, 13]]) == [6, 6, 6, 6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4],queries = [[1, 1, 13], [2, 2, 3], [1, 1, 13], [2, 4, 5], [1, 1, 13], [2, 6, 7], [1, 1, 13], [2, 8, 9], [1, 1, 13], [2, 10, 11], [1, 1, 13], [2, 12, 13], [1, 1, 13]]) == [6, 6, 6, 6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 8], [2, 5, 10], [1, 1, 8]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 8], [2, 5, 10], [1, 1, 8]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[2, 5, 6], [1, 0, 18], [2, 10, 9], [1, 4, 14]]) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[2, 5, 6], [1, 0, 18], [2, 10, 9], [1, 4, 14]]) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 0, 10], [2, 4, 10], [1, 0, 10], [2, 2, 1], [1, 0, 10]]) == [5, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 0, 10], [2, 4, 10], [1, 0, 10], [2, 2, 1], [1, 0, 10]]) == [5, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 2, 18], [2, 9, 12], [1, 2, 18], [2, 12, 8], [1, 2, 18]]) == [1, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 2, 18], [2, 9, 12], [1, 2, 18], [2, 12, 8], [1, 2, 18]]) == [1, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 18], [2, 4, 5], [1, 0, 18], [2, 10, 11], [1, 0, 18]]) == [1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 18], [2, 4, 5], [1, 0, 18], [2, 10, 11], [1, 0, 18]]) == [1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 2, 3, 1, 2, 3, 1, 2],queries = [[1, 0, 9], [2, 2, 5], [1, 1, 8], [2, 5, 3], [1, 0, 8]]) == [3, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 2, 3, 1, 2, 3, 1, 2],queries = [[1, 0, 9], [2, 2, 5], [1, 1, 8], [2, 5, 3], [1, 0, 8]]) == [3, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],queries = [[1, 2, 8], [2, 3, 3], [1, 0, 9], [2, 5, 8], [1, 1, 7]]) == [3, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],queries = [[1, 2, 8], [2, 3, 3], [1, 0, 9], [2, 5, 8], [1, 1, 7]]) == [3, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 0, 14], [2, 7, 20], [1, 0, 14], [2, 10, 15], [1, 0, 14]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 0, 14], [2, 7, 20], [1, 0, 14], [2, 10, 15], [1, 0, 14]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40],queries = [[1, 1, 9], [2, 4, 25], [1, 0, 8], [2, 7, 34], [1, 2, 7]]) == [3, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40],queries = [[1, 1, 9], [2, 4, 25], [1, 0, 8], [2, 7, 34], [1, 2, 7]]) == [3, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 8, 2, 9, 1, 10, 4, 11, 5, 12, 6, 13],queries = [[1, 1, 12], [2, 5, 1], [1, 1, 12], [2, 9, 8], [1, 0, 13]]) == [5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 8, 2, 9, 1, 10, 4, 11, 5, 12, 6, 13],queries = [[1, 1, 12], [2, 5, 1], [1, 1, 12], [2, 9, 8], [1, 0, 13]]) == [5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 5, 3], [1, 0, 9], [2, 4, 5], [1, 2, 7]]) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 5, 3], [1, 0, 9], [2, 4, 5], [1, 2, 7]]) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[1, 0, 12], [2, 5, 4], [1, 3, 9], [2, 6, 3], [1, 0, 12]]) == [3, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[1, 0, 12], [2, 5, 4], [1, 3, 9], [2, 6, 3], [1, 0, 12]]) == [3, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],queries = [[1, 0, 18], [2, 1, 2], [1, 0, 18], [2, 3, 4], [1, 0, 18], [2, 5, 6], [1, 0, 18], [2, 7, 8], [1, 0, 18], [2, 9, 10], [1, 0, 18], [2, 11, 12], [1, 0, 18]]) == [9, 9, 9, 9, 9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],queries = [[1, 0, 18], [2, 1, 2], [1, 0, 18], [2, 3, 4], [1, 0, 18], [2, 5, 6], [1, 0, 18], [2, 7, 8], [1, 0, 18], [2, 9, 10], [1, 0, 18], [2, 11, 12], [1, 0, 18]]) == [9, 9, 9, 9, 9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 110, 80, 120, 70, 130, 60, 140, 50],queries = [[1, 2, 8], [2, 3, 100], [1, 0, 9], [2, 6, 90], [1, 1, 7]]) == [2, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 110, 80, 120, 70, 130, 60, 140, 50],queries = [[1, 2, 8], [2, 3, 100], [1, 0, 9], [2, 6, 90], [1, 1, 7]]) == [2, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15, 8, 16, 9, 17, 10, 18],queries = [[1, 0, 20], [2, 2, 7], [1, 1, 19], [2, 6, 12], [1, 0, 20]]) == [9, 9, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15, 8, 16, 9, 17, 10, 18],queries = [[1, 0, 20], [2, 2, 7], [1, 1, 19], [2, 6, 12], [1, 0, 20]]) == [9, 9, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12],queries = [[1, 1, 12], [2, 3, 6], [1, 2, 11], [2, 7, 10], [1, 0, 13]]) == [5, 4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12],queries = [[1, 1, 12], [2, 3, 6], [1, 2, 11], [2, 7, 10], [1, 0, 13]]) == [5, 4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 2, 5, 4, 3, 6, 4, 7, 5, 8, 6, 9, 7],queries = [[1, 1, 14], [2, 3, 3], [1, 1, 14], [2, 10, 10], [1, 1, 14]]) == [6, 6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 2, 5, 4, 3, 6, 4, 7, 5, 8, 6, 9, 7],queries = [[1, 1, 14], [2, 3, 3], [1, 1, 14], [2, 10, 10], [1, 1, 14]]) == [6, 6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[1, 1, 17], [2, 9, 2], [1, 1, 17], [2, 12, 3], [1, 1, 17]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[1, 1, 17], [2, 9, 2], [1, 1, 17], [2, 12, 3], [1, 1, 17]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1],queries = [[1, 2, 10], [2, 5, 5], [1, 2, 10], [2, 7, 7], [1, 2, 10]]) == [2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1],queries = [[1, 2, 10], [2, 5, 5], [1, 2, 10], [2, 7, 7], [1, 2, 10]]) == [2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],queries = [[1, 1, 8], [2, 3, 3], [1, 0, 9], [2, 5, 2], [1, 1, 7]]) == [3, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],queries = [[1, 1, 8], [2, 3, 3], [1, 0, 9], [2, 5, 2], [1, 1, 7]]) == [3, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[2, 3, 6], [1, 1, 8], [2, 5, 7], [1, 3, 7]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[2, 3, 6], [1, 1, 8], [2, 5, 7], [1, 3, 7]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10, 5, 1],queries = [[2, 4, 7], [1, 0, 10], [2, 8, 2], [1, 3, 9]]) == [3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10, 5, 1],queries = [[2, 4, 7], [1, 0, 10], [2, 8, 2], [1, 3, 9]]) == [3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],queries = [[1, 0, 10], [2, 5, 5], [2, 6, 6], [1, 0, 10]]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],queries = [[1, 0, 10], [2, 5, 5], [2, 6, 6], [1, 0, 10]]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 0, 9], [2, 4, 5], [1, 0, 9], [2, 2, 3], [1, 0, 9], [2, 6, 7], [1, 0, 9]]) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 0, 9], [2, 4, 5], [1, 0, 9], [2, 2, 3], [1, 0, 9], [2, 6, 7], [1, 0, 9]]) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10, 5],queries = [[1, 0, 8], [2, 1, 7], [1, 0, 8], [2, 3, 9], [1, 0, 8], [2, 5, 8], [1, 0, 8]]) == [4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10, 5],queries = [[1, 0, 8], [2, 1, 7], [1, 0, 8], [2, 3, 9], [1, 0, 8], [2, 5, 8], [1, 0, 8]]) == [4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1],queries = [[1, 0, 9], [2, 1, 4], [1, 0, 9], [2, 3, 5], [1, 0, 9], [2, 5, 7], [1, 0, 9]]) == [3, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1],queries = [[1, 0, 9], [2, 1, 4], [1, 0, 9], [2, 3, 5], [1, 0, 9], [2, 5, 7], [1, 0, 9]]) == [3, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8],queries = [[1, 0, 14], [2, 1, 1], [1, 0, 14], [2, 3, 4], [1, 0, 14], [2, 5, 6], [1, 0, 14]]) == [7, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8],queries = [[1, 0, 14], [2, 1, 1], [1, 0, 14], [2, 3, 4], [1, 0, 14], [2, 5, 6], [1, 0, 14]]) == [7, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[1, 2, 12], [2, 5, 55], [1, 2, 12], [2, 9, 95], [1, 2, 12]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[1, 2, 12], [2, 5, 55], [1, 2, 12], [2, 9, 95], [1, 2, 12]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35, 45],queries = [[1, 1, 10], [2, 5, 28], [1, 2, 9], [2, 8, 33], [1, 3, 11]]) == [4, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35, 45],queries = [[1, 1, 10], [2, 5, 28], [1, 2, 9], [2, 8, 33], [1, 3, 11]]) == [4, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 2, 8, 7, 9, 6, 10],queries = [[1, 1, 9], [2, 4, 7], [2, 6, 5], [1, 1, 9]]) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 2, 8, 7, 9, 6, 10],queries = [[1, 1, 9], [2, 4, 7], [2, 6, 5], [1, 1, 9]]) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 9, 1, 9, 1, 9, 1, 9],queries = [[1, 0, 8], [2, 1, 2], [1, 0, 8], [2, 3, 4], [1, 0, 8], [2, 5, 6], [1, 0, 8], [2, 7, 8], [1, 0, 8]]) == [3, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 9, 1, 9, 1, 9, 1, 9],queries = [[1, 0, 8], [2, 1, 2], [1, 0, 8], [2, 3, 4], [1, 0, 8], [2, 5, 6], [1, 0, 8], [2, 7, 8], [1, 0, 8]]) == [3, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 8], [2, 4, 10], [1, 0, 8]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 8], [2, 4, 10], [1, 0, 8]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 2, 8], [2, 3, 11], [1, 2, 8], [2, 7, 12], [1, 2, 8]]) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 2, 8], [2, 3, 11], [1, 2, 8], [2, 7, 12], [1, 2, 8]]) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21],queries = [[1, 1, 19], [2, 2, 10], [1, 1, 19], [2, 4, 20], [1, 1, 19], [2, 6, 30], [1, 1, 19], [2, 8, 40], [1, 1, 19], [2, 10, 50], [1, 1, 19], [2, 12, 60], [1, 1, 19], [2, 14, 70], [1, 1, 19], [2, 16, 80], [1, 1, 19], [2, 18, 90], [1, 1, 19]]) == [8, 8, 8, 8, 8, 8, 8, 8, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21],queries = [[1, 1, 19], [2, 2, 10], [1, 1, 19], [2, 4, 20], [1, 1, 19], [2, 6, 30], [1, 1, 19], [2, 8, 40], [1, 1, 19], [2, 10, 50], [1, 1, 19], [2, 12, 60], [1, 1, 19], [2, 14, 70], [1, 1, 19], [2, 16, 80], [1, 1, 19], [2, 18, 90], [1, 1, 19]]) == [8, 8, 8, 8, 8, 8, 8, 8, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[1, 0, 8], [2, 3, 2], [1, 1, 7]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[1, 0, 8], [2, 3, 2], [1, 1, 7]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[1, 1, 8], [2, 3, 65], [1, 2, 9], [2, 6, 55], [1, 0, 9]]) == [0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[1, 1, 8], [2, 3, 65], [1, 2, 9], [2, 6, 55], [1, 0, 9]]) == [0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[2, 5, 5], [1, 0, 16], [2, 10, 10], [1, 5, 11]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[2, 5, 5], [1, 0, 16], [2, 10, 10], [1, 5, 11]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 1001, 998, 1002, 997, 1003, 996, 1004, 995],queries = [[1, 0, 9], [2, 2, 1000], [1, 1, 8], [2, 4, 1001], [1, 0, 8]]) == [4, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 1001, 998, 1002, 997, 1003, 996, 1004, 995],queries = [[1, 0, 9], [2, 2, 1000], [1, 1, 8], [2, 4, 1001], [1, 0, 8]]) == [4, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40],queries = [[1, 0, 9], [2, 3, 50], [1, 2, 8], [2, 6, 10], [1, 0, 9]]) == [4, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40],queries = [[1, 0, 9], [2, 3, 50], [1, 2, 8], [2, 6, 10], [1, 0, 9]]) == [4, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 0, 9], [2, 4, 5], [1, 0, 9], [2, 3, 6], [1, 0, 9]]) == [0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 0, 9], [2, 4, 5], [1, 0, 9], [2, 3, 6], [1, 0, 9]]) == [0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 1, 8], [2, 2, 10], [2, 4, 20], [1, 0, 8]]) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 1, 8], [2, 2, 10], [2, 4, 20], [1, 0, 8]]) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],queries = [[1, 0, 16], [2, 6, 6], [1, 3, 13], [2, 10, 10], [1, 0, 16]]) == [2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],queries = [[1, 0, 16], [2, 6, 6], [1, 3, 13], [2, 10, 10], [1, 0, 16]]) == [2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 5, 3], [1, 0, 9], [2, 4, 10], [1, 1, 8], [2, 8, 5]]) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 5, 3], [1, 0, 9], [2, 4, 10], [1, 1, 8], [2, 8, 5]]) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550],queries = [[1, 0, 10], [2, 2, 225], [1, 0, 10], [2, 6, 375], [1, 0, 10]]) == [5, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550],queries = [[1, 0, 10], [2, 2, 225], [1, 0, 10], [2, 6, 375], [1, 0, 10]]) == [5, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40],queries = [[1, 0, 8], [2, 3, 15], [1, 0, 8], [1, 2, 6]]) == [4, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40],queries = [[1, 0, 8], [2, 3, 15], [1, 0, 8], [1, 2, 6]]) == [4, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 1, 7], [2, 5, 7], [1, 1, 7]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 1, 7], [2, 5, 7], [1, 1, 7]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65],queries = [[1, 1, 11], [2, 2, 18], [1, 1, 11], [2, 4, 28], [1, 1, 11], [2, 6, 38], [1, 1, 11], [2, 8, 48], [1, 1, 11]]) == [4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65],queries = [[1, 1, 11], [2, 2, 18], [1, 1, 11], [2, 4, 28], [1, 1, 11], [2, 6, 38], [1, 1, 11], [2, 8, 48], [1, 1, 11]]) == [4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 0, 8], [2, 1, 2], [2, 3, 3], [1, 0, 8]]) == [4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 0, 8], [2, 1, 2], [2, 3, 3], [1, 0, 8]]) == [4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],queries = [[1, 0, 20], [2, 1, 10], [1, 0, 20], [2, 3, 15], [1, 0, 20], [2, 5, 18], [1, 0, 20], [2, 7, 20], [1, 0, 20]]) == [7, 7, 7, 8, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],queries = [[1, 0, 20], [2, 1, 10], [1, 0, 20], [2, 3, 15], [1, 0, 20], [2, 5, 18], [1, 0, 20], [2, 7, 20], [1, 0, 20]]) == [7, 7, 7, 8, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],queries = [[1, 0, 9], [2, 2, 3], [1, 1, 8], [2, 4, 5], [1, 2, 7]]) == [4, 3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],queries = [[1, 0, 9], [2, 2, 3], [1, 1, 8], [2, 4, 5], [1, 2, 7]]) == [4, 3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 5, 6], [1, 0, 9], [2, 4, 7], [1, 0, 9]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 5, 6], [1, 0, 9], [2, 4, 7], [1, 0, 9]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 1, 7], [2, 4, 5], [1, 1, 7]]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 1, 7], [2, 4, 5], [1, 1, 7]]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 2, 4, 6, 5, 7, 8, 9, 7, 11, 10],queries = [[1, 0, 12], [2, 2, 5], [1, 1, 11], [2, 5, 8], [1, 0, 12]]) == [4, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 2, 4, 6, 5, 7, 8, 9, 7, 11, 10],queries = [[1, 0, 12], [2, 2, 5], [1, 1, 11], [2, 5, 8], [1, 0, 12]]) == [4, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 6, 7, 8, 2, 4, 5, 6, 3, 2, 1],queries = [[1, 1, 12], [2, 5, 10], [1, 1, 12], [2, 8, 9], [1, 1, 12]]) == [2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 6, 7, 8, 2, 4, 5, 6, 3, 2, 1],queries = [[1, 1, 12], [2, 5, 10], [1, 1, 12], [2, 8, 9], [1, 1, 12]]) == [2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[1, 1, 7], [2, 3, 5], [1, 1, 7]]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[1, 1, 7], [2, 3, 5], [1, 1, 7]]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],queries = [[1, 0, 9], [2, 4, 6], [1, 0, 9], [2, 5, 8], [1, 0, 9]]) == [4, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],queries = [[1, 0, 9], [2, 4, 6], [1, 0, 9], [2, 5, 8], [1, 0, 9]]) == [4, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],queries = [[2, 1, 50], [1, 0, 10], [2, 3, 50], [1, 2, 8]]) == [4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],queries = [[2, 1, 50], [1, 0, 10], [2, 3, 50], [1, 2, 8]]) == [4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 8], [2, 4, 5], [1, 1, 8], [2, 7, 8], [1, 0, 9]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 8], [2, 4, 5], [1, 1, 8], [2, 7, 8], [1, 0, 9]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 25, 30, 5, 40, 35, 50, 45, 60],queries = [[1, 0, 10], [2, 4, 20], [1, 3, 9], [2, 6, 30], [1, 5, 8]]) == [4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 25, 30, 5, 40, 35, 50, 45, 60],queries = [[1, 0, 10], [2, 4, 20], [1, 3, 9], [2, 6, 30], [1, 5, 8]]) == [4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 10, 12, 11, 13, 12, 14, 13, 15],queries = [[1, 1, 8], [2, 3, 15], [1, 0, 9], [2, 6, 11], [1, 2, 7]]) == [3, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 10, 12, 11, 13, 12, 14, 13, 15],queries = [[1, 1, 8], [2, 3, 15], [1, 0, 9], [2, 6, 11], [1, 2, 7]]) == [3, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[1, 1, 7], [2, 4, 10], [1, 1, 7]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[1, 1, 7], [2, 4, 10], [1, 1, 7]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 7, 5, 9, 7, 11, 9, 13, 11, 15],queries = [[1, 1, 9], [2, 4, 8], [1, 1, 9], [2, 6, 10], [1, 1, 9], [2, 8, 14], [1, 1, 9]]) == [4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 7, 5, 9, 7, 11, 9, 13, 11, 15],queries = [[1, 1, 9], [2, 4, 8], [1, 1, 9], [2, 6, 10], [1, 1, 9], [2, 8, 14], [1, 1, 9]]) == [4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 2, 5, 3, 1, 4, 2, 5],queries = [[2, 3, 4], [1, 0, 4], [2, 5, 6], [1, 4, 9]]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 2, 5, 3, 1, 4, 2, 5],queries = [[2, 3, 4], [1, 0, 4], [2, 5, 6], [1, 4, 9]]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 8, 9],queries = [[1, 2, 5], [2, 4, 6], [1, 2, 5], [2, 3, 5], [1, 2, 5]]) == [1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 8, 9],queries = [[1, 2, 5], [2, 4, 6], [1, 2, 5], [2, 3, 5], [1, 2, 5]]) == [1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[1, 0, 16], [2, 2, 10], [1, 0, 16], [2, 5, 8], [1, 0, 16], [2, 8, 12], [1, 0, 16]]) == [4, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[1, 0, 16], [2, 2, 10], [1, 0, 16], [2, 5, 8], [1, 0, 16], [2, 8, 12], [1, 0, 16]]) == [4, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 5, 6], [1, 0, 9], [2, 4, 3], [1, 0, 9]]) == [0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 5, 6], [1, 0, 9], [2, 4, 3], [1, 0, 9]]) == [0, 0, 1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [3, 1, 4, 2, 5],queries = [[2, 3, 4], [1, 0, 4]]) == [0]
    assert candidate(nums = [4, 1, 4, 2, 1, 5],queries = [[2, 2, 4], [1, 0, 2], [1, 0, 4]]) == [0, 1]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 1, 8], [2, 3, 1], [1, 1, 8], [2, 5, 7], [1, 0, 4]]) == [3, 2, 1]
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 7], [2, 2, 6], [2, 4, 3], [1, 0, 8]]) == [3, 3]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[2, 0, 10], [1, 1, 11], [2, 1, 9], [1, 1, 11], [2, 2, 8], [1, 1, 11], [2, 3, 7], [1, 1, 11], [2, 4, 6], [1, 1, 11]]) == [3, 2, 2, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 10, 8], [1, 0, 28], [2, 15, 13], [1, 8, 20]]) == [1, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 1, 13], [2, 7, 1], [1, 1, 13]]) == [0, 1]
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 10], [2, 4, 3], [1, 3, 11], [2, 8, 4], [1, 0, 12]]) == [4, 4, 5]
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 0, 8], [2, 1, 3], [1, 0, 8], [2, 3, 5], [1, 0, 8], [2, 5, 7], [1, 0, 8]]) == [3, 3, 1, 1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 1, 10], [1, 0, 8], [2, 3, 9], [1, 2, 7]]) == [0, 0, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 0, 14], [2, 6, 10], [1, 0, 14], [2, 4, 8], [1, 0, 14], [2, 7, 11], [1, 0, 14]]) == [0, 1, 2, 2]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 14], [2, 7, 18], [1, 0, 14], [2, 10, 12], [1, 0, 14]]) == [0, 1, 2]
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10],queries = [[1, 0, 8], [2, 1, 25], [1, 0, 8], [2, 3, 30], [1, 0, 8]]) == [4, 4, 4]
    assert candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100],queries = [[1, 1, 7], [2, 2, 150], [1, 0, 8], [2, 4, 200], [1, 0, 8]]) == [3, 3, 3]
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 9], [2, 2, 8], [1, 1, 9], [2, 4, 6], [1, 1, 9], [2, 6, 4], [1, 1, 9]]) == [0, 1, 2, 2]
    assert candidate(nums = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],queries = [[2, 2, 5], [1, 0, 9], [2, 6, 8], [1, 1, 8]]) == [4, 3]
    assert candidate(nums = [7, 2, 8, 3, 9, 4, 10, 5, 11, 6, 12, 7, 13, 8, 14, 9, 15],queries = [[1, 0, 16], [2, 1, 5], [1, 3, 15], [2, 9, 12], [1, 0, 16]]) == [7, 6, 5]
    assert candidate(nums = [1, 5, 1, 5, 1, 5, 1, 5, 1, 5],queries = [[1, 1, 8], [2, 4, 3], [1, 1, 8], [2, 6, 2], [1, 1, 8]]) == [3, 3, 3]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9],queries = [[2, 2, 4], [1, 0, 16], [2, 8, 7], [1, 6, 12]]) == [6, 1]
    assert candidate(nums = [5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4],queries = [[1, 1, 13], [2, 2, 3], [1, 1, 13], [2, 4, 5], [1, 1, 13], [2, 6, 7], [1, 1, 13], [2, 8, 9], [1, 1, 13], [2, 10, 11], [1, 1, 13], [2, 12, 13], [1, 1, 13]]) == [6, 6, 6, 6, 6, 6, 6]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 8], [2, 5, 10], [1, 1, 8]]) == [0, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[2, 5, 6], [1, 0, 18], [2, 10, 9], [1, 4, 14]]) == [1, 1]
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 0, 10], [2, 4, 10], [1, 0, 10], [2, 2, 1], [1, 0, 10]]) == [5, 4, 4]
    assert candidate(nums = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 2, 18], [2, 9, 12], [1, 2, 18], [2, 12, 8], [1, 2, 18]]) == [1, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 18], [2, 4, 5], [1, 0, 18], [2, 10, 11], [1, 0, 18]]) == [1, 1, 1]
    assert candidate(nums = [5, 3, 4, 2, 3, 1, 2, 3, 1, 2],queries = [[1, 0, 9], [2, 2, 5], [1, 1, 8], [2, 5, 3], [1, 0, 8]]) == [3, 3, 2]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],queries = [[1, 2, 8], [2, 3, 3], [1, 0, 9], [2, 5, 8], [1, 1, 7]]) == [3, 3, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[1, 0, 14], [2, 7, 20], [1, 0, 14], [2, 10, 15], [1, 0, 14]]) == [0, 1, 2]
    assert candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40],queries = [[1, 1, 9], [2, 4, 25], [1, 0, 8], [2, 7, 34], [1, 2, 7]]) == [3, 3, 1]
    assert candidate(nums = [7, 3, 8, 2, 9, 1, 10, 4, 11, 5, 12, 6, 13],queries = [[1, 1, 12], [2, 5, 1], [1, 1, 12], [2, 9, 8], [1, 0, 13]]) == [5, 5, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 5, 3], [1, 0, 9], [2, 4, 5], [1, 2, 7]]) == [1, 1]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[1, 0, 12], [2, 5, 4], [1, 3, 9], [2, 6, 3], [1, 0, 12]]) == [3, 1, 3]
    assert candidate(nums = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],queries = [[1, 0, 18], [2, 1, 2], [1, 0, 18], [2, 3, 4], [1, 0, 18], [2, 5, 6], [1, 0, 18], [2, 7, 8], [1, 0, 18], [2, 9, 10], [1, 0, 18], [2, 11, 12], [1, 0, 18]]) == [9, 9, 9, 9, 9, 9, 9]
    assert candidate(nums = [100, 90, 110, 80, 120, 70, 130, 60, 140, 50],queries = [[1, 2, 8], [2, 3, 100], [1, 0, 9], [2, 6, 90], [1, 1, 7]]) == [2, 4, 3]
    assert candidate(nums = [8, 1, 9, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15, 8, 16, 9, 17, 10, 18],queries = [[1, 0, 20], [2, 2, 7], [1, 1, 19], [2, 6, 12], [1, 0, 20]]) == [9, 9, 9]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12],queries = [[1, 1, 12], [2, 3, 6], [1, 2, 11], [2, 7, 10], [1, 0, 13]]) == [5, 4, 6]
    assert candidate(nums = [5, 3, 4, 2, 5, 4, 3, 6, 4, 7, 5, 8, 6, 9, 7],queries = [[1, 1, 14], [2, 3, 3], [1, 1, 14], [2, 10, 10], [1, 1, 14]]) == [6, 6, 5]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[1, 1, 17], [2, 9, 2], [1, 1, 17], [2, 12, 3], [1, 1, 17]]) == [0, 1, 2]
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1],queries = [[1, 2, 10], [2, 5, 5], [1, 2, 10], [2, 7, 7], [1, 2, 10]]) == [2, 3, 4]
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],queries = [[1, 1, 8], [2, 3, 3], [1, 0, 9], [2, 5, 2], [1, 1, 7]]) == [3, 3, 1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[2, 3, 6], [1, 1, 8], [2, 5, 7], [1, 3, 7]]) == [0, 1]
    assert candidate(nums = [5, 1, 4, 3, 2, 6, 7, 8, 9, 10, 5, 1],queries = [[2, 4, 7], [1, 0, 10], [2, 8, 2], [1, 3, 9]]) == [3, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],queries = [[1, 0, 10], [2, 5, 5], [2, 6, 6], [1, 0, 10]]) == [0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 0, 9], [2, 4, 5], [1, 0, 9], [2, 2, 3], [1, 0, 9], [2, 6, 7], [1, 0, 9]]) == [0, 0, 0, 0]
    assert candidate(nums = [5, 10, 5, 10, 5, 10, 5, 10, 5],queries = [[1, 0, 8], [2, 1, 7], [1, 0, 8], [2, 3, 9], [1, 0, 8], [2, 5, 8], [1, 0, 8]]) == [4, 4, 4, 4]
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1],queries = [[1, 0, 9], [2, 1, 4], [1, 0, 9], [2, 3, 5], [1, 0, 9], [2, 5, 7], [1, 0, 9]]) == [3, 3, 3, 4]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8],queries = [[1, 0, 14], [2, 1, 1], [1, 0, 14], [2, 3, 4], [1, 0, 14], [2, 5, 6], [1, 0, 14]]) == [7, 6, 6, 6]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[1, 2, 12], [2, 5, 55], [1, 2, 12], [2, 9, 95], [1, 2, 12]]) == [0, 0, 0]
    assert candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40, 35, 45],queries = [[1, 1, 10], [2, 5, 28], [1, 2, 9], [2, 8, 33], [1, 3, 11]]) == [4, 3, 3]
    assert candidate(nums = [5, 1, 4, 3, 2, 8, 7, 9, 6, 10],queries = [[1, 1, 9], [2, 4, 7], [2, 6, 5], [1, 1, 9]]) == [3, 3]
    assert candidate(nums = [9, 1, 9, 1, 9, 1, 9, 1, 9],queries = [[1, 0, 8], [2, 1, 2], [1, 0, 8], [2, 3, 4], [1, 0, 8], [2, 5, 6], [1, 0, 8], [2, 7, 8], [1, 0, 8]]) == [3, 3, 3, 3, 3]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 8], [2, 4, 10], [1, 0, 8]]) == [0, 1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 2, 8], [2, 3, 11], [1, 2, 8], [2, 7, 12], [1, 2, 8]]) == [0, 1, 2]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21],queries = [[1, 1, 19], [2, 2, 10], [1, 1, 19], [2, 4, 20], [1, 1, 19], [2, 6, 30], [1, 1, 19], [2, 8, 40], [1, 1, 19], [2, 10, 50], [1, 1, 19], [2, 12, 60], [1, 1, 19], [2, 14, 70], [1, 1, 19], [2, 16, 80], [1, 1, 19], [2, 18, 90], [1, 1, 19]]) == [8, 8, 8, 8, 8, 8, 8, 8, 8, 9]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[1, 0, 8], [2, 3, 2], [1, 1, 7]]) == [0, 1]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[1, 1, 8], [2, 3, 65], [1, 2, 9], [2, 6, 55], [1, 0, 9]]) == [0, 0, 1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[2, 5, 5], [1, 0, 16], [2, 10, 10], [1, 5, 11]]) == [0, 1]
    assert candidate(nums = [1000, 999, 1001, 998, 1002, 997, 1003, 996, 1004, 995],queries = [[1, 0, 9], [2, 2, 1000], [1, 1, 8], [2, 4, 1001], [1, 0, 8]]) == [4, 3, 3]
    assert candidate(nums = [10, 20, 15, 25, 20, 30, 25, 35, 30, 40],queries = [[1, 0, 9], [2, 3, 50], [1, 2, 8], [2, 6, 10], [1, 0, 9]]) == [4, 3, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 0, 9], [2, 4, 5], [1, 0, 9], [2, 3, 6], [1, 0, 9]]) == [0, 0, 1]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 1, 8], [2, 2, 10], [2, 4, 20], [1, 0, 8]]) == [3, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],queries = [[1, 0, 16], [2, 6, 6], [1, 3, 13], [2, 10, 10], [1, 0, 16]]) == [2, 3, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[2, 5, 3], [1, 0, 9], [2, 4, 10], [1, 1, 8], [2, 8, 5]]) == [1, 1]
    assert candidate(nums = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550],queries = [[1, 0, 10], [2, 2, 225], [1, 0, 10], [2, 6, 375], [1, 0, 10]]) == [5, 4, 4]
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40],queries = [[1, 0, 8], [2, 3, 15], [1, 0, 8], [1, 2, 6]]) == [4, 3, 1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 1, 7], [2, 5, 7], [1, 1, 7]]) == [0, 1]
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65],queries = [[1, 1, 11], [2, 2, 18], [1, 1, 11], [2, 4, 28], [1, 1, 11], [2, 6, 38], [1, 1, 11], [2, 8, 48], [1, 1, 11]]) == [4, 4, 4, 4, 4]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5],queries = [[1, 0, 8], [2, 1, 2], [2, 3, 3], [1, 0, 8]]) == [4, 2]
    assert candidate(nums = [1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],queries = [[1, 0, 20], [2, 1, 10], [1, 0, 20], [2, 3, 15], [1, 0, 20], [2, 5, 18], [1, 0, 20], [2, 7, 20], [1, 0, 20]]) == [7, 7, 7, 8, 8]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],queries = [[1, 0, 9], [2, 2, 3], [1, 1, 8], [2, 4, 5], [1, 2, 7]]) == [4, 3, 1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 5, 6], [1, 0, 9], [2, 4, 7], [1, 0, 9]]) == [0, 0, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 1, 7], [2, 4, 5], [1, 1, 7]]) == [0, 0]
    assert candidate(nums = [5, 1, 3, 2, 4, 6, 5, 7, 8, 9, 7, 11, 10],queries = [[1, 0, 12], [2, 2, 5], [1, 1, 11], [2, 5, 8], [1, 0, 12]]) == [4, 3, 4]
    assert candidate(nums = [5, 3, 4, 6, 7, 8, 2, 4, 5, 6, 3, 2, 1],queries = [[1, 1, 12], [2, 5, 10], [1, 1, 12], [2, 8, 9], [1, 1, 12]]) == [2, 2, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[1, 1, 7], [2, 3, 5], [1, 1, 7]]) == [0, 0]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7],queries = [[1, 0, 9], [2, 4, 6], [1, 0, 9], [2, 5, 8], [1, 0, 9]]) == [4, 3, 3]
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],queries = [[2, 1, 50], [1, 0, 10], [2, 3, 50], [1, 2, 8]]) == [4, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[1, 1, 8], [2, 4, 5], [1, 1, 8], [2, 7, 8], [1, 0, 9]]) == [0, 0, 0]
    assert candidate(nums = [10, 20, 15, 25, 30, 5, 40, 35, 50, 45, 60],queries = [[1, 0, 10], [2, 4, 20], [1, 3, 9], [2, 6, 30], [1, 5, 8]]) == [4, 2, 0]
    assert candidate(nums = [10, 11, 10, 12, 11, 13, 12, 14, 13, 15],queries = [[1, 1, 8], [2, 3, 15], [1, 0, 9], [2, 6, 11], [1, 2, 7]]) == [3, 4, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],queries = [[1, 1, 7], [2, 4, 10], [1, 1, 7]]) == [0, 1]
    assert candidate(nums = [5, 3, 7, 5, 9, 7, 11, 9, 13, 11, 15],queries = [[1, 1, 9], [2, 4, 8], [1, 1, 9], [2, 6, 10], [1, 1, 9], [2, 8, 14], [1, 1, 9]]) == [4, 4, 4, 4]
    assert candidate(nums = [3, 1, 4, 2, 5, 3, 1, 4, 2, 5],queries = [[2, 3, 4], [1, 0, 4], [2, 5, 6], [1, 4, 9]]) == [0, 2]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 8, 9],queries = [[1, 2, 5], [2, 4, 6], [1, 2, 5], [2, 3, 5], [1, 2, 5]]) == [1, 0, 0]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],queries = [[1, 0, 16], [2, 2, 10], [1, 0, 16], [2, 5, 8], [1, 0, 16], [2, 8, 12], [1, 0, 16]]) == [4, 4, 4, 5]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[1, 0, 9], [2, 5, 6], [1, 0, 9], [2, 4, 3], [1, 0, 9]]) == [0, 0, 1]


