def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [2, 5, 3, 6, 4, 7, 5, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [2, 5, 3, 6, 4, 7, 5, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5]) == [2, 5, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5]) == [2, 5, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000]) == [-1, 1000000000, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000]) == [-1, 1000000000, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 8, 5]) == [2, 5, 5, 6, 7, 7, 8, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 8, 5]) == [2, 5, 5, 6, 7, 7, 8, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 4, 3]) == [2, -1, 3, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 4, 3]) == [2, -1, 3, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 2, 6, 3, 4, 8, 9]) == [9, 2, 8, 3, 9, 8, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 2, 6, 3, 4, 8, 9]) == [9, 2, 8, 3, 9, 8, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8]) == [2, 7, 3, 8, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8]) == [2, 7, 3, 8, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 0]) == [2, 5, 5, 6, 7, 8, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 0]) == [2, 5, 5, 6, 7, 8, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == [3, 4, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == [3, 4, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [1, -1, 1, -1, 1, -1, 1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [1, -1, 1, -1, 1, -1, 1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 3]) == [4, 3, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 3]) == [4, 3, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 3, 2, 7, 8]) == [7, 8, 8, 8, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 3, 2, 7, 8]) == [7, 8, 8, 8, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [2, 5, 5, 6, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [2, 5, 5, 6, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4]) == [-1, -1, 4, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4]) == [-1, -1, 4, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 5, 6, 2, 3, 1, 4, 2, 3]) == [6, 6, -1, -1, 4, -1, 2, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 5, 6, 2, 3, 1, 4, 2, 3]) == [6, 6, -1, -1, 4, -1, 2, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 14, 12, 13, 15, 0]) == [2, 14, 3, 14, 4, 14, 5, 14, 11, 14, 12, -1, 15, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 14, 12, 13, 15, 0]) == [2, 14, 3, 14, 4, 14, 5, 14, 11, 14, 12, -1, 15, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 0, 4, 5, 6, 7, 8, 9]) == [5, 5, 5, 5, 6, 7, 8, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 0, 4, 5, 6, 7, 8, 9]) == [5, 5, 5, 5, 6, 7, 8, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == [2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == [2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 3, 9, 3, 7, 5, 1, 8, 2, 8, 4, 8, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1]) == [5, 5, 9, 9, 6, -1, 5, 7, 7, 9, 7, -1, 8, -1, 4, 8, 4, 9, 6, 7, 4, 7, 7, 7, 7, 9, 9, 9, 8, -1, 8, 8, 8, 9, 9, 7, 7, -1, 8, 9, 7, -1, 5, 8, 8, 2, 9, 4, 9, 6, 9, 7, 4, 7, 7, 7, 7, 9, 9, 9, 8, -1, 8, 8, 8, -1, -1, 7, 7, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 3, 9, 3, 7, 5, 1, 8, 2, 8, 4, 8, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1]) == [5, 5, 9, 9, 6, -1, 5, 7, 7, 9, 7, -1, 8, -1, 4, 8, 4, 9, 6, 7, 4, 7, 7, 7, 7, 9, 9, 9, 8, -1, 8, 8, 8, 9, 9, 7, 7, -1, 8, 9, 7, -1, 5, 8, 8, 2, 9, 4, 9, 6, 9, 7, 4, 7, 7, 7, 7, 9, 9, 9, 8, -1, 8, 8, 8, -1, -1, 7, 7, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]) == [2, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]) == [2, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [-1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [-1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, 8, 8, 8, 8, 8, 8, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, 8, 8, 8, 8, 8, 8, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == [2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == [2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [-1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [-1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 9, 2, 8, 7, 10, 6, 11]) == [3, 8, 8, 11, 7, 11, 11, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 9, 2, 8, 7, 10, 6, 11]) == [3, 8, 8, 11, 7, 11, 11, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [30, 40, 20, 50, 30, 60, 40, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [30, 40, 20, 50, 30, 60, 40, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 4, 2, 7, 6, 8]) == [3, 6, 7, 6, 6, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 4, 2, 7, 6, 8]) == [3, 6, 7, 6, 6, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 2, 3, 5, 1, 6, 0, 7, 8, 9]) == [5, 6, 5, 6, 7, 7, 8, 8, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 2, 3, 5, 1, 6, 0, 7, 8, 9]) == [5, 6, 5, 6, 7, 7, 8, 8, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [2, 2, 3, 3, 4, 4, 5, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [2, 2, 3, 3, 4, 4, 5, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 1, 3, 4, 7, 8, 0, 9]) == [7, 3, 8, 4, 7, 8, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 1, 3, 4, 7, 8, 0, 9]) == [7, 3, 8, 4, 7, 8, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15]) == [2, 12, 3, 12, 4, 12, 5, 12, 11, 12, 13, 14, 15, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15]) == [2, 12, 3, 12, 4, 12, 5, 12, 11, 12, 13, 14, 15, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 4, 2, 3, 4, 1, 5, 6]) == [4, 4, 4, 6, 4, 5, 6, 6, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 4, 2, 3, 4, 1, 5, 6]) == [4, 4, 4, 6, 4, 5, 6, 6, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8]) == [3, 3, 4, 4, 3, 4, 4, 6, 5, 4, 5, 6, 6, 8, 7, 6, 7, 8, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8]) == [3, 3, 4, 4, 3, 4, 4, 6, 5, 4, 5, 6, 6, 8, 7, 6, 7, 8, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [5, 5, 9, 9, 6, -1, 5, 7, 7, 9, 7, -1, 8, -1, 4, 8, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [5, 5, 9, 9, 6, -1, 5, 7, 7, 9, 7, -1, 8, -1, 4, 8, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, -1, 2, -1, 2, -1, 2, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, -1, 2, -1, 2, -1, 2, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 7, 10, 8, 6, 9, 2, 4]) == [3, 10, 10, 8, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 7, 10, 8, 6, 9, 2, 4]) == [3, 10, 10, 8, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15]) == [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 14, 15, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15]) == [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 14, 15, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [1, -1, 2, -1, 3, -1, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [1, -1, 2, -1, 3, -1, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 8, 7, 11, 10, 9, 13, 12, 6, 14, 15, 16, 17, 18, 19, 20]) == [2, 4, 4, 7, 7, 10, 10, 12, 12, 12, 15, 15, 15, 16, 17, 18, 19, 20, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 8, 7, 11, 10, 9, 13, 12, 6, 14, 15, 16, 17, 18, 19, 20]) == [2, 4, 4, 7, 7, 10, 10, 12, 12, 12, 15, 15, 15, 16, 17, 18, 19, 20, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 2, 4, 7, 6, 8]) == [3, 6, 7, 7, 6, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 2, 4, 7, 6, 8]) == [3, 6, 7, 7, 6, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]) == [8, 8, 8, 8, 8, 8, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]) == [8, 8, 8, 8, 8, 8, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 1, 1, 3, 3, 4, 4, 5, 5]) == [3, 3, 3, 3, 4, 4, 5, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 1, 1, 3, 3, 4, 4, 5, 5]) == [3, 3, 3, 3, 4, 4, 5, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]) == [1, 2, 2, 3, 3, 4, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]) == [1, 2, 2, 3, 3, 4, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10]) == [2, 5, 5, 8, 8, 8, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10]) == [2, 5, 5, 8, 8, 8, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4, 9, 0]) == [-1, 2, 7, 3, 9, 4, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4, 9, 0]) == [-1, 2, 7, 3, 9, 4, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, -1, -1, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, -1, -1, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [3, 3, -1, 3, 3, -1, 3, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [3, 3, -1, 3, 3, -1, 3, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 7, 6, 5, 9, 8, 10]) == [2, 7, 7, 6, 8, 8, 8, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 7, 6, 5, 9, 8, 10]) == [2, 7, 7, 6, 8, 8, 8, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12]) == [10, 2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12]) == [10, 2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-1, -1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-1, -1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 6]) == [2, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 6]) == [2, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == [1, 3, 3, 5, 5, 7, 7, 9, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == [1, 3, 3, 5, 5, 7, 7, 9, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [-1, 2, -1, 2, -1, 2, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [-1, 2, -1, 2, -1, 2, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [2, 4, 4, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [2, 4, 4, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 2, 7, 8, 6, 9, 10]) == [8, 3, 8, 8, 8, 9, 10, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 2, 7, 8, 6, 9, 10]) == [8, 3, 8, 8, 8, 9, 10, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 4, 7, 6, 8, 10, 9, 11, 12, 13, 14, 15, 16, 17]) == [4, 6, 6, 10, 10, 9, 12, 12, 13, 14, 15, 16, 17, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 4, 7, 6, 8, 10, 9, 11, 12, 13, 14, 15, 16, 17]) == [4, 6, 6, 10, 10, 9, 12, 12, 13, 14, 15, 16, 17, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 3, 2, 4, 8, 6, 7, 9, 0]) == [3, 6, 8, 8, 6, -1, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 3, 2, 4, 8, 6, 7, 9, 0]) == [3, 6, 8, 8, 6, -1, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == [3, 4, 5, 5, 5, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == [3, 4, 5, 5, 5, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [2, -1, 3, -1, 4, -1, 5, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [2, -1, 3, -1, 4, -1, 5, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 38, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 38, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [4, 5, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [4, 5, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 0, 9, 0, 9, 0, 9, 0, 9, 0]) == [-1, 9, -1, 9, -1, 9, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 0, 9, 0, 9, 0, 9, 0, 9, 0]) == [-1, 9, -1, 9, -1, 9, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1]) == [6, 6, -1, 9, 4, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1]) == [6, 6, -1, 9, 4, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 5, 3, 7, 10, 2, 6, 9, 4]) == [9, 3, 10, 10, 9, -1, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 5, 3, 7, 10, 2, 6, 9, 4]) == [9, 3, 10, 10, 9, -1, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -1, 3, 4, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -1, 3, 4, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 5, 6, 0, 3, 4, 9, 8, 7]) == [6, 6, 9, 8, 4, 9, 8, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 5, 6, 0, 3, 4, 9, 8, 7]) == [6, 6, 9, 8, 4, 9, 8, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 10, 9]) == [2, 4, 4, 7, 7, 8, 10, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 10, 9]) == [2, 4, 4, 7, 7, 8, 10, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, 10, -1, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, 10, -1, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 91, 82, 73, 64, 55, 46, 37, 28, 19, 10]) == [30, 40, 50, 60, 70, 80, 90, 100, 91, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 91, 82, 73, 64, 55, 46, 37, 28, 19, 10]) == [30, 40, 50, 60, 70, 80, 90, 100, 91, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == [30, 40, 50, 60, 70, 80, 90, 100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == [30, 40, 50, 60, 70, 80, 90, 100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 5, 6, 2, 3, 1, 8]) == [6, 6, 8, -1, 8, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 5, 6, 2, 3, 1, 8]) == [6, 6, 8, -1, 8, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [-1, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [-1, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 31, 32, 33, 34, 35]) == [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 34, 35, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 31, 32, 33, 34, 35]) == [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 34, 35, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 2, 6, 1, 7, 4, 8, 0, 9]) == [6, 7, 7, 8, 4, 9, 9, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 2, 6, 1, 7, 4, 8, 0, 9]) == [6, 7, 7, 8, 4, 9, 9, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 1, 3, 1, 2, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, 3, -1, 2, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 1, 3, 1, 2, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, 3, -1, 2, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, 10, 9, 9, 9, 9, 9, 9, 9, 9, -1, -1, 9, 9, 9, 9, 9, 9, 9, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, 10, 9, 9, 9, 9, 9, 9, 9, 9, -1, -1, 9, 9, 9, 9, 9, 9, 9, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 3, 4, 4, 3, 5, 6, 6, 5, 7, 8, 8, 7, 9]) == [2, 4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 3, 4, 4, 3, 5, 6, 6, 5, 7, 8, 8, 7, 9]) == [2, 4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, -1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, -1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == [3, 4, 2, 5, 3, 6, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == [3, 4, 2, 5, 3, 6, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 10, 2, 9, 4, 8, 6, 7, 5, 3, 1]) == [2, -1, 4, -1, 6, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 10, 2, 9, 4, 8, 6, 7, 5, 3, 1]) == [2, -1, 4, -1, 6, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 101, 201, 102, 202, 103, 203, 104, 204]) == [101, 202, 102, 203, 103, 204, 104, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 101, 201, 102, 202, 103, 203, 104, 204]) == [101, 202, 102, 203, 103, 204, 104, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 2, 4, 6, 1, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [7, 6, 6, 7, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 2, 4, 6, 1, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [7, 6, 6, 7, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 24, 54, 32, 54, 68, 27, 89, 10, 70, 29, 33, 63, 96, 99, 78, 76, 65, 84, 88]) == [54, 32, 89, 68, 89, 70, 70, 99, 29, 99, 63, 96, 99, -1, -1, 88, 88, 88, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 24, 54, 32, 54, 68, 27, 89, 10, 70, 29, 33, 63, 96, 99, 78, 76, 65, 84, 88]) == [54, 32, 89, 68, 89, 70, 70, 99, 29, 99, 63, 96, 99, -1, -1, 88, 88, 88, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [3, 4, 4, -1, -1, 4, 3, 4, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [3, 4, 4, -1, -1, 4, 3, 4, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [-1, 3, 2, -1, 3, 2, -1, 3, 2, -1, 3, 2, -1, 3, 2, -1, -1, 2, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [-1, 3, 2, -1, 3, 2, -1, 3, 2, -1, 3, 2, -1, 3, 2, -1, -1, 2, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 10, 11, 9, 3, 4, 6, 7, 8]) == [2, 11, 11, -1, -1, -1, 6, 7, 8, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 10, 11, 9, 3, 4, 6, 7, 8]) == [2, 11, 11, -1, -1, -1, 6, 7, 8, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 11, 7, 12, 13, 14, 6, 15, 16, 17, 8, 18, 19, 9, 10, 5, 20, 21, 22, 1]) == [7, 13, 13, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 20, 21, 21, 22, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 11, 7, 12, 13, 14, 6, 15, 16, 17, 8, 18, 19, 9, 10, 5, 20, 21, 22, 1]) == [7, 13, 13, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 20, 21, 21, 22, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 25, 40, 35, 50]) == [30, 25, 35, 35, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 25, 40, 35, 50]) == [30, 25, 35, 35, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 3]) == [4, 3, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 3]) == [4, 3, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1]) == [3, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1]) == [3, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [-1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [-1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 11, 1, 2, 10, 11, 1]) == [11, 11, -1, 10, 11, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 11, 1, 2, 10, 11, 1]) == [11, 11, -1, 10, 11, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 4, 2, 1]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 4, 2, 1]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 80, 60, 40, 20]) == [80, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 80, 60, 40, 20]) == [80, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 1]) == [-1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 1]) == [-1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 5, 4, 7, 3, 6]) == [2, 6, 4, 6, 6, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 5, 4, 7, 3, 6]) == [2, 6, 4, 6, 6, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 6, 7, 8]) == [7, 3, 7, 7, 8, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 6, 7, 8]) == [7, 3, 7, 7, 8, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == [3, 4, 5, 6, 7, 8, 10, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == [3, 4, 5, 6, 7, 8, 10, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == [-1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == [-1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 11, 12, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 11, 12, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 3, 4, 18, 5, 6]) == [3, -1, 18, 5, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 3, 4, 18, 5, 6]) == [3, -1, 18, 5, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 2, 3]) == [-1, 2, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 2, 3]) == [-1, 2, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == [-1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == [-1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5]) == [-1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5]) == [-1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 4, 6, 7, 5, 3, 9, 1]) == [-1, 6, 7, 9, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 4, 6, 7, 5, 3, 9, 1]) == [-1, 6, 7, 9, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4]) == [2, 7, 3, -1, 4, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4]) == [2, 7, 3, -1, 4, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7]) == [2, 5, 5, 6, 7, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7]) == [2, 5, 5, 6, 7, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8]) == [2, 7, 3, 8, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8]) == [2, 7, 3, 8, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10]) == [2, 7, 3, 7, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10]) == [2, 7, 3, 7, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == [3, 4, 4, 5, 5, 6, 6, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == [3, 4, 4, 5, 5, 6, 6, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 1, 2, 10, 6, 9, 7, 3, 4]) == [10, 9, 10, 6, -1, 7, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 1, 2, 10, 6, 9, 7, 3, 4]) == [10, 9, 10, 6, -1, 7, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100]) == [-1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100]) == [-1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 6, 5]) == [2, 6, 6, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 6, 5]) == [2, 6, 6, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 2, 4, 6, 7, 1, 5]) == [-1, 4, 6, 7, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 2, 4, 6, 7, 1, 5]) == [-1, 4, 6, 7, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == [4, 3, 6, 6, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == [4, 3, 6, 6, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0]) == [1, -1, 1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0]) == [1, -1, 1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 3, -1, 3, 3, -1, 3, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 3, -1, 3, 3, -1, 3, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == [3, 4, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == [3, 4, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 1, 6, 1, 4, 1, 2, 1, 1, 1, 9, 1, 4, 1, 1, 1, 1, 1, 1]) == [-1, 4, 4, -1, 2, -1, 9, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 1, 6, 1, 4, 1, 2, 1, 1, 1, 9, 1, 4, 1, 1, 1, 1, 1, 1]) == [-1, 4, 4, -1, 2, -1, 9, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4]) == [-1, -1, 4, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4]) == [-1, -1, 4, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == [2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == [2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 5, 12, 9, 16, 15]) == [9, 9, 15, 15, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 5, 12, 9, 16, 15]) == [9, 9, 15, 15, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10]) == [2, 5, 5, 7, 6, 9, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10]) == [2, 5, 5, 7, 6, 9, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 4, 5, 3, 5, 10, 15]) == [10, 15, 5, 15, 10, 15, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 4, 5, 3, 5, 10, 15]) == [10, 15, 5, 15, 10, 15, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7]) == [-1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7]) == [-1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4]) == [-1, 2, 7, 3, -1, 4, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4]) == [-1, 2, 7, 3, -1, 4, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 2, 6, 4, 3]) == [-1, 2, -1, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 2, 6, 4, 3]) == [-1, 2, -1, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40]) == [30, 40, 20, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40]) == [30, 40, 20, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == [3, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == [3, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6]) == [2, 7, 3, 8, 4, 9, 5, -1, 6, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6]) == [2, 7, 3, 8, 4, 9, 5, -1, 6, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 3, 11, 1, 15, 9]) == [15, 15, -1, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 3, 11, 1, 15, 9]) == [15, 15, -1, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 8, 9, 10, 11, 5, 3, 12, 0]) == [8, 12, 10, 11, 12, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 8, 9, 10, 11, 5, 3, 12, 0]) == [8, 12, 10, 11, 12, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5]) == [2, 5, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5]) == [2, 5, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == [2, 7, 3, 8, 4, 9, 5, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == [2, 7, 3, 8, 4, 9, 5, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10]) == [7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10]) == [7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 0, 3, 0, 4]) == [2, 3, 4, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 0, 3, 0, 4]) == [2, 3, 4, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 3, -1, -1, 3, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 3, -1, -1, 3, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 3, 6, 4, 7, 8]) == [2, 5, 5, 6, 7, 4, 8, 8, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 3, 6, 4, 7, 8]) == [2, 5, 5, 6, 7, 4, 8, 8, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 4, 3, 5, 7, 2, 8, 6, 1]) == [-1, 7, 7, 8, -1, 6, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 4, 3, 5, 7, 2, 8, 6, 1]) == [-1, 7, 7, 8, -1, 6, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 1, 6, 2, 7, 3, 8, 4, 9]) == [-1, 7, 2, 8, 3, 9, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 1, 6, 2, 7, 3, 8, 4, 9]) == [-1, 7, 2, 8, 3, 9, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 2, 18]) == [18, 18, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 2, 18]) == [18, 18, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5, 0]) == [3, 4, 4, 5, 5, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5, 0]) == [3, 4, 4, 5, 5, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 2, 3, 4, 6, 7, 8, 9, 10]) == [2, 7, 4, 6, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 2, 3, 4, 6, 7, 8, 9, 10]) == [2, 7, 4, 6, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4, 5]) == [3, 4, 5, 5, 5, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4, 5]) == [3, 4, 5, 5, 5, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 6, 4, 7]) == [7, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 6, 4, 7]) == [7, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 3, 5, 6, 4, 3, 2, 1, 2, 3, 4]) == [2, 5, 3, 6, 6, -1, -1, -1, -1, 4, 3, 4, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 3, 5, 6, 4, 3, 2, 1, 2, 3, 4]) == [2, 5, 3, 6, 6, -1, -1, -1, -1, 4, 3, 4, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 3, 2, 1]) == [2, 5, 5, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 3, 2, 1]) == [2, 5, 5, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 2, 3, 4, 0]) == [-1, 3, 4, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 2, 3, 4, 0]) == [-1, 3, 4, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1]) == [1, -1, 1, -1, 1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1]) == [1, -1, 1, -1, 1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5]) == [3, 4, 4, 5, 5, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5]) == [3, 4, 4, 5, 5, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60]) == [15, 25, 25, 35, 35, 45, 45, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60]) == [15, 25, 25, 35, 35, 45, 45, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 0, 4, 3, 5, 6, 7, 8, 9]) == [4, 3, 3, 6, 6, 7, 8, 9, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 0, 4, 3, 5, 6, 7, 8, 9]) == [4, 3, 3, 6, 6, 7, 8, 9, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == [3, 3, 4, 4, 5, 5, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == [3, 3, 4, 4, 5, 5, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 1, 5, 2, 7]) == [-1, 2, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 1, 5, 2, 7]) == [-1, 2, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == [2, -1, 2, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == [2, -1, 2, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [2, 5, 3, 6, 4, 7, 5, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5]) == [2, 5, 5, -1, -1]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1000000000, 0, 1000000000, 0, 1000000000]) == [-1, 1000000000, -1, -1, -1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 7, 8, 5]) == [2, 5, 5, 6, 7, 7, 8, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [1, 5, 2, 4, 3]) == [2, -1, 3, -1, -1]
    assert candidate(nums = [7, 1, 5, 2, 6, 3, 4, 8, 9]) == [9, 2, 8, 3, 9, 8, 9, -1, -1]
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8]) == [2, 7, 3, 8, 4, -1, -1, -1]
    assert candidate(nums = [3, 3]) == [-1, -1]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 0]) == [2, 5, 5, 6, 7, 8, 9, -1, -1, -1]
    assert candidate(nums = [0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5]) == [3, 4, 5, -1, -1]
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == [1, -1, 1, -1, 1, -1, 1, -1, -1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 4, 3]) == [4, 3, -1, -1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 6, 3, 2, 7, 8]) == [7, 8, 8, 8, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [2, 5, 5, 6, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]
    assert candidate(nums = [5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 3, 1, 2, 4]) == [-1, -1, 4, -1, -1]
    assert candidate(nums = [10, 10, 10, 10, 10]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1]
    assert candidate(nums = [2, 1, 5, 6, 2, 3, 1, 4, 2, 3]) == [6, 6, -1, -1, 4, -1, 2, -1, -1, -1]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 14, 12, 13, 15, 0]) == [2, 14, 3, 14, 4, 14, 5, 14, 11, 14, 12, -1, 15, -1, -1, -1]
    assert candidate(nums = [3, 2, 1, 0, 4, 5, 6, 7, 8, 9]) == [5, 5, 5, 5, 6, 7, 8, 9, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == [2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, -1, -1, -1]
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 3, 9, 3, 7, 5, 1, 8, 2, 8, 4, 8, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1]) == [5, 5, 9, 9, 6, -1, 5, 7, 7, 9, 7, -1, 8, -1, 4, 8, 4, 9, 6, 7, 4, 7, 7, 7, 7, 9, 9, 9, 8, -1, 8, 8, 8, 9, 9, 7, 7, -1, 8, 9, 7, -1, 5, 8, 8, 2, 9, 4, 9, 6, 9, 7, 4, 7, 7, 7, 7, 9, 9, 9, 8, -1, 8, 8, 8, -1, -1, 7, 7, -1, -1, -1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1]) == [2, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1, -1]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [-1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, -1, -1, -1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, 8, 8, 8, 8, 8, 8, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == [2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10, 8, -1, -1, -1]
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == [-1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, 5, -1, -1, -1, -1]
    assert candidate(nums = [1, 5, 3, 9, 2, 8, 7, 10, 6, 11]) == [3, 8, 8, 11, 7, 11, 11, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, -1, -1]
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [30, 40, 20, 50, 30, 60, 40, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, -1, -1, -1, -1]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 5, 3, 4, 2, 7, 6, 8]) == [3, 6, 7, 6, 6, -1, -1, -1]
    assert candidate(nums = [3, 4, 2, 3, 5, 1, 6, 0, 7, 8, 9]) == [5, 6, 5, 6, 7, 7, 8, 8, 9, -1, -1]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [2, 2, 3, 3, 4, 4, 5, 5, -1, -1]
    assert candidate(nums = [5, 2, 6, 1, 3, 4, 7, 8, 0, 9]) == [7, 3, 8, 4, 7, 8, 9, -1, -1, -1]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, -1, -1]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15]) == [2, 12, 3, 12, 4, 12, 5, 12, 11, 12, 13, 14, 15, -1, -1]
    assert candidate(nums = [2, 1, 3, 4, 2, 3, 4, 1, 5, 6]) == [4, 4, 4, 6, 4, 5, 6, 6, -1, -1]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8]) == [3, 3, 4, 4, 3, 4, 4, 6, 5, 4, 5, 6, 6, 8, 7, 6, 7, 8, -1, -1]
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [5, 5, 9, 9, 6, -1, 5, 7, 7, 9, 7, -1, 8, -1, 4, 8, 4, -1, -1, -1]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, -1, 2, -1, 2, -1, 2, -1, -1, -1]
    assert candidate(nums = [1, 5, 3, 7, 10, 8, 6, 9, 2, 4]) == [3, 10, 10, 8, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 2, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15]) == [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 14, 15, -1, -1]
    assert candidate(nums = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [1, -1, 2, -1, 3, -1, 4, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 5, 4, 8, 7, 11, 10, 9, 13, 12, 6, 14, 15, 16, 17, 18, 19, 20]) == [2, 4, 4, 7, 7, 10, 10, 12, 12, 12, 15, 15, 15, 16, 17, 18, 19, 20, -1, -1]
    assert candidate(nums = [1, 5, 3, 2, 4, 7, 6, 8]) == [3, 6, 7, 7, 6, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]) == [8, 8, 8, 8, 8, 8, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -1]
    assert candidate(nums = [2, 2, 1, 1, 3, 3, 4, 4, 5, 5]) == [3, 3, 3, 3, 4, 4, 5, 5, -1, -1]
    assert candidate(nums = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]) == [1, 2, 2, 3, 3, 4, 4, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 6, 5, 4, 9, 8, 7, 10]) == [2, 5, 5, 8, 8, 8, -1, -1, -1, -1]
    assert candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4, 9, 0]) == [-1, 2, 7, 3, 9, 4, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, -1, -1, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [3, 3, -1, 3, 3, -1, 3, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 7, 6, 5, 9, 8, 10]) == [2, 7, 7, 6, 8, 8, 8, -1, -1, -1]
    assert candidate(nums = [8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12]) == [10, 2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, -1, -1, -1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-1, -1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [1, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 2, 5, 2, 2, 2, 2, 2, 6]) == [2, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]
    assert candidate(nums = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == [1, 3, 3, 5, 5, 7, 7, 9, 9, -1, -1]
    assert candidate(nums = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == [-1, 2, -1, 2, -1, 2, -1, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [2, 4, 4, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]
    assert candidate(nums = [5, 1, 4, 3, 2, 7, 8, 6, 9, 10]) == [8, 3, 8, 8, 8, 9, 10, 10, -1, -1]
    assert candidate(nums = [3, 5, 4, 7, 6, 8, 10, 9, 11, 12, 13, 14, 15, 16, 17]) == [4, 6, 6, 10, 10, 9, 12, 12, 13, 14, 15, 16, 17, -1, -1]
    assert candidate(nums = [1, 5, 3, 2, 4, 8, 6, 7, 9, 0]) == [3, 6, 8, 8, 6, -1, 9, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == [3, 4, 5, 5, 5, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [2, -1, 3, -1, 4, -1, 5, -1, -1, -1]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 38, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [3, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 21, 20]) == [4, 5, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16, 18, 18, 20, 20, -1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [9, 0, 9, 0, 9, 0, 9, 0, 9, 0]) == [-1, 9, -1, 9, -1, 9, -1, -1, -1, -1]
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1]) == [6, 6, -1, 9, 4, -1, -1, -1, -1]
    assert candidate(nums = [8, 1, 5, 3, 7, 10, 2, 6, 9, 4]) == [9, 3, 10, 10, 9, -1, 9, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -1, 3, 4, 5, -1, -1]
    assert candidate(nums = [2, 1, 5, 6, 0, 3, 4, 9, 8, 7]) == [6, 6, 9, 8, 4, 9, 8, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 10, 9]) == [2, 4, 4, 7, 7, 8, 10, 9, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, 10, -1, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 91, 82, 73, 64, 55, 46, 37, 28, 19, 10]) == [30, 40, 50, 60, 70, 80, 90, 100, 91, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == [30, 40, 50, 60, 70, 80, 90, 100, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [2, 1, 5, 6, 2, 3, 1, 8]) == [6, 6, 8, -1, 8, -1, -1, -1]
    assert candidate(nums = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [-1, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1]
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 31, 32, 33, 34, 35]) == [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 34, 35, -1, -1]
    assert candidate(nums = [3, 5, 2, 6, 1, 7, 4, 8, 0, 9]) == [6, 7, 7, 8, 4, 9, 9, -1, -1, -1]
    assert candidate(nums = [5, 1, 4, 1, 3, 1, 2, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, 3, -1, 2, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, 10, 9, 9, 9, 9, 9, 9, 9, 9, -1, -1, 9, 9, 9, 9, 9, 9, 9, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 2, 1, 3, 4, 4, 3, 5, 6, 6, 5, 7, 8, 8, 7, 9]) == [2, 4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, -1, -1, -1, -1]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, -1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -1]
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == [3, 4, 2, 5, 3, 6, 4, -1, -1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, 2, -1, -1, -1]
    assert candidate(nums = [0, 10, 2, 9, 4, 8, 6, 7, 5, 3, 1]) == [2, -1, 4, -1, 6, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 4, 5, 6, 7, 8, 9, 9, -1, 8, 8, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [100, 200, 101, 201, 102, 202, 103, 203, 104, 204]) == [101, 202, 102, 203, 103, 204, 104, -1, -1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, -1, -1, -1, -1]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 3, 2, 4, 6, 1, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [7, 6, 6, 7, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, -1, -1]
    assert candidate(nums = [50, 24, 54, 32, 54, 68, 27, 89, 10, 70, 29, 33, 63, 96, 99, 78, 76, 65, 84, 88]) == [54, 32, 89, 68, 89, 70, 70, 99, 29, 99, 63, 96, 99, -1, -1, 88, 88, 88, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [3, 4, 4, -1, -1, 4, 3, 4, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [-1, 3, 2, -1, 3, 2, -1, 3, 2, -1, 3, 2, -1, 3, 2, -1, -1, 2, -1, -1, -1]
    assert candidate(nums = [1, 5, 2, 10, 11, 9, 3, 4, 6, 7, 8]) == [2, 11, 11, -1, -1, -1, 6, 7, 8, -1, -1]
    assert candidate(nums = [0, 11, 7, 12, 13, 14, 6, 15, 16, 17, 8, 18, 19, 9, 10, 5, 20, 21, 22, 1]) == [7, 13, 13, 14, 15, 16, 16, 17, 18, 19, 19, 20, 21, 20, 21, 21, 22, -1, -1, -1]
    assert candidate(nums = [1, 10, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [10, 20, 30, 25, 40, 35, 50]) == [30, 25, 35, 35, -1, -1, -1]
    assert candidate(nums = [1, 2, 4, 3]) == [4, 3, -1, -1]
    assert candidate(nums = [1, 2, 3, 2, 1]) == [3, -1, -1, -1, -1]
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [-1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 10, 11, 1, 2, 10, 11, 1]) == [11, 11, -1, 10, 11, -1, -1, -1]
    assert candidate(nums = [5, 3, 4, 2, 1]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [1, 100, 80, 60, 40, 20]) == [80, -1, -1, -1, -1, -1]
    assert candidate(nums = [3, 2, 1]) == [-1, -1, -1]
    assert candidate(nums = [1, 5, 2, 5, 4, 7, 3, 6]) == [2, 6, 4, 6, 6, -1, -1, -1]
    assert candidate(nums = [5, 1, 4, 3, 6, 7, 8]) == [7, 3, 7, 7, 8, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == [3, 4, 5, 6, 7, 8, 10, 9, -1, -1]
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == [-1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 10, 11, 12, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [11, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 10, 3, 4, 18, 5, 6]) == [3, -1, 18, 5, -1, -1, -1]
    assert candidate(nums = [5, 1, 4, 2, 3]) == [-1, 2, -1, -1, -1]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [1]) == [-1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5]) == [-1, -1, -1, -1, -1, -1]
    assert candidate(nums = [8, 2, 4, 6, 7, 5, 3, 9, 1]) == [-1, 6, 7, 9, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4]) == [2, 7, 3, -1, 4, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7]) == [2, 5, 5, 6, 7, -1, -1]
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8]) == [2, 7, 3, 8, 4, -1, -1, -1]
    assert candidate(nums = [0, 1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1, -1]
    assert candidate(nums = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10]) == [2, 7, 3, 7, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == [3, 4, 4, 5, 5, 6, 6, -1, -1, -1]
    assert candidate(nums = [5, 8, 1, 2, 10, 6, 9, 7, 3, 4]) == [10, 9, 10, 6, -1, 7, -1, -1, -1, -1]
    assert candidate(nums = [2, 1]) == [-1, -1]
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [100, 100, 100]) == [-1, -1, -1]
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 6, 5]) == [2, 6, 6, 5, -1, -1]
    assert candidate(nums = [1000000000, 999999999, 888888888, 777777777, 666666666]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [8, 1, 2, 4, 6, 7, 1, 5]) == [-1, 4, 6, 7, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]) == [4, 3, 6, 6, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0]) == [1, -1, 1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [3, 3, -1, 3, 3, -1, 3, -1, -1]
    assert candidate(nums = [5, 4, 3, 2, 1, 0]) == [-1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5]) == [3, 4, 5, -1, -1]
    assert candidate(nums = [10, 1, 1, 6, 1, 4, 1, 2, 1, 1, 1, 9, 1, 4, 1, 1, 1, 1, 1, 1]) == [-1, 4, 4, -1, 2, -1, 9, 4, 4, 4, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 3, 1, 2, 4]) == [-1, -1, 4, -1, -1]
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == [2, 7, 3, 8, 4, 9, 5, 10, 6, 11, 7, 12, 8, 13, 9, 14, 10, -1, -1, -1]
    assert candidate(nums = [8, 5, 12, 9, 16, 15]) == [9, 9, 15, 15, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10]) == [2, 5, 5, 7, 6, 9, 9, 10, -1, -1]
    assert candidate(nums = [3, 3]) == [-1, -1]
    assert candidate(nums = [5, 8, 4, 5, 3, 5, 10, 15]) == [10, 15, 5, 15, 10, 15, -1, -1]
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7]) == [-1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [8, 1, 5, 2, 6, 3, 7, 4]) == [-1, 2, 7, 3, -1, 4, -1, -1]
    assert candidate(nums = [7, 1, 5, 2, 6, 4, 3]) == [-1, 2, -1, 4, -1, -1, -1]
    assert candidate(nums = [10, 20, 10, 30, 20, 40]) == [30, 40, 20, -1, -1, -1]
    assert candidate(nums = [1, 2, 3]) == [3, -1, -1]
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6]) == [2, 7, 3, 8, 4, 9, 5, -1, 6, -1, -1]
    assert candidate(nums = [10, 3, 11, 1, 15, 9]) == [15, 15, -1, 9, -1, -1]
    assert candidate(nums = [1, 10, 8, 9, 10, 11, 5, 3, 12, 0]) == [8, 12, 10, 11, 12, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5]) == [2, 5, 5, -1, -1]
    assert candidate(nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 10, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9]) == [2, 7, 3, 8, 4, 9, 5, -1, -1, -1]
    assert candidate(nums = [0, 1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1, -1]
    assert candidate(nums = [5, 6, 7, 8, 9, 10]) == [7, 8, 9, 10, -1, -1]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 4, 5, 6, 7, 8, 9, -1, -1]
    assert candidate(nums = [0, 1, 2, 0, 3, 0, 4]) == [2, 3, 4, 4, -1, -1, -1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2]) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == [3, 3, -1, -1, 3, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 6, 4, 7, 8]) == [2, 5, 5, 6, 7, 4, 8, 8, -1, -1]
    assert candidate(nums = [10, 4, 3, 5, 7, 2, 8, 6, 1]) == [-1, 7, 7, 8, -1, 6, -1, -1, -1]
    assert candidate(nums = [10, 5, 1, 6, 2, 7, 3, 8, 4, 9]) == [-1, 7, 2, 8, 3, 9, 4, -1, -1, -1]
    assert candidate(nums = [10, 5, 15, 2, 18]) == [18, 18, -1, -1, -1]
    assert candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5, 0]) == [3, 4, 4, 5, 5, -1, -1, -1, -1]
    assert candidate(nums = [1, 5, 2, 3, 4, 6, 7, 8, 9, 10]) == [2, 7, 4, 6, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5]) == [3, 4, 5, 5, 5, -1, -1]
    assert candidate(nums = [5, 2, 6, 4, 7]) == [7, 4, -1, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 3, 5, 6, 4, 3, 2, 1, 2, 3, 4]) == [2, 5, 3, 6, 6, -1, -1, -1, -1, 4, 3, 4, -1, -1]
    assert candidate(nums = [1, 3, 2, 4, 5, 3, 2, 1]) == [2, 5, 5, -1, -1, -1, -1, -1]
    assert candidate(nums = [5, 1, 2, 3, 4, 0]) == [-1, 3, 4, -1, -1, -1]
    assert candidate(nums = [0, 1, 0, 1, 0, 1, 0, 1]) == [1, -1, 1, -1, 1, -1, -1, -1]
    assert candidate(nums = [1, 2, 0, 3, 0, 4, 0, 5]) == [3, 4, 4, 5, 5, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1]
    assert candidate(nums = [10, 20, 15, 30, 25, 40, 35, 50, 45, 60]) == [15, 25, 25, 35, 35, 45, 45, -1, -1, -1]
    assert candidate(nums = [1, 2, 0, 4, 3, 5, 6, 7, 8, 9]) == [4, 3, 3, 6, 6, 7, 8, 9, -1, -1]
    assert candidate(nums = [5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    assert candidate(nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == [3, 3, 4, 4, 5, 5, -1, -1, -1, -1]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 4, 5, 6, 7, 8, 9, 10, -1, -1]
    assert candidate(nums = [8, 1, 5, 2, 7]) == [-1, 2, -1, -1, -1]
    assert candidate(nums = [1, 2, 1, 2, 1, 2, 1]) == [2, -1, 2, -1, -1, -1, -1]
    assert candidate(nums = [2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]


