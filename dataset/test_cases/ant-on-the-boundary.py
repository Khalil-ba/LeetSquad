def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, 2, -2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, 2, -2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, -10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, -10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, -30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, -30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, -30, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, -30, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 10, -10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 10, -10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, -4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, -4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 5, -5, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 5, -5, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, -3, -4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, -3, -4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, -3, 1, 4, -4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, -3, 1, 4, -4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -3, 2, -4, 1, -1, 3, -3, 2, -2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -3, 2, -4, 1, -1, 3, -3, 2, -2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, -3, 1, 4, -4, -6, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, -3, 1, 4, -4, -6, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 3, -3, 2, -5, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 3, -3, 2, -5, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, -10, 1, 2, 3, 4, -10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, -10, 1, 2, 3, 4, -10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -2, -2, 6, -2, -2, -2, 6, -2, -2, -2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -2, -2, 6, -2, -2, -2, 6, -2, -2, -2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -1, 2, -1, 2, -1, 2, -1, 2, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -1, 2, -1, 2, -1, 2, -1, 2, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -15]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -15]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, -10, 1, -1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, -10, 1, -1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 3, -6, 4, -1, -6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 3, -6, 4, -1, -6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 10, -10, 10, -10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 10, -10, 10, -10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, 3, -3, 3, -3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, 3, -3, 3, -3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, -4, 1, 1, 1, 1, -4, 1, 1, 1, 1, -4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, -4, 1, 1, 1, 1, -4, 1, 1, 1, 1, -4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -3, 2, -6, 1, 1, 1, -1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -3, 2, -6, 1, 1, 1, -1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, -1, -3, 2, 2, -4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, -1, -3, 2, 2, -4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -3, 3, -7, 4, -2, 2, -4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -3, 3, -7, 4, -2, 2, -4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-7, 3, 4, -1, -2, 2, 1, -4, 6, -2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-7, 3, 4, -1, -2, 2, 1, -4, 6, -2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, 4, -2, -2, 4, -2, -2, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, 4, -2, -2, 4, -2, -2, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, 2, 2, -4, 4, -5, 5, -6, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, 2, 2, -4, 4, -5, 5, -6, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, -9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, -9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, -10, 5, -5, 5, -5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, -10, 5, -5, 5, -5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, 5, -1, 4, -6, 2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, 5, -1, 4, -6, 2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, 1, 2, -4, 1, 1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, 1, 2, -4, 1, 1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 5, 5, -5, 5, -5, 5, -5, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 5, 5, -5, 5, -5, 5, -5, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, -3, -2, -1, 4, -4, 5, -5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, -3, -2, -1, 4, -4, 5, -5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, -4, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, -4, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -45]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -45]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, -6, 1, -1, 1, -1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, -6, 1, -1, 1, -1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 2, -2, 2, -2, -2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 2, -2, 2, -2, -2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, 2, -2, 2, -2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, 2, -2, 2, -2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 5, -5, 5, -5, 5, -5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 5, -5, 5, -5, 5, -5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 5, 5, -3, 3, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 5, 5, -3, 3, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -2, -2, -2, -1, 8, -1, -2, -2, -2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -2, -2, -2, -1, 8, -1, -2, -2, -2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, -1, 2, -5, 0, 3, -3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, -1, 2, -5, 0, 3, -3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, -2, -1, 10, -5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, -2, -1, 10, -5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, -2, 3, -1, -2, 3, -1, -2, 3, -1, -2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, -2, 3, -1, -2, 3, -1, -2, 3, -1, -2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -3, -1, -2, 3, -4, 1, 1, 1, -3, 5, -2, -1, 1, -1, -1, -1, -1, -1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -3, -1, -2, 3, -4, 1, 1, 1, -3, 5, -2, -1, 1, -1, -1, -1, -1, -1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -5, 5, -3, 3, -2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -5, 5, -3, 3, -2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, -3, 2, -1, 4, -3, 2, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, -3, 2, -1, 4, -3, 2, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 3, -6, 4, -1, -2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 3, -6, 4, -1, -2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, -2, -3, -4, -5, -6, -7, -8, -9, 45]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, -2, -3, -4, -5, -6, -7, -8, -9, 45]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 3, -8, 2, -2, 4, -4, 6, -6, 5, -5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 3, -8, 2, -2, 4, -4, 6, -6, 5, -5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, -8, 2, 2, 2, 2, -8]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, -8, 2, 2, 2, 2, -8]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, -5, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, -5, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 5, 3, -8, 2, 1, -2, 2, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 5, 3, -8, 2, 1, -2, 2, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -3, 3, -3, 3, -3, 3, -3, 3, -3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -3, 3, -3, 3, -3, 3, -3, 3, -3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, -2, 1, -1, 3, -3, 2, -1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, -2, 1, -1, 3, -3, 2, -1, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 15]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 15]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, -5, 4, -4, -3, 3, 2, -2, 1, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, -5, 4, -4, -3, 3, 2, -2, 1, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 5, 5, -1, 1, -1, 1, 0, 3, -3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 5, 5, -1, 1, -1, 1, 0, 3, -3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 5, -5, 3, -3, 2, -2, 1, -1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 5, -5, 3, -3, 2, -2, 1, -1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -5, 5, -5, 5, -5]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -5, 5, -5, 5, -5]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -3, -4, 1, 2, -2, -1, 4, -6, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -3, -4, 1, 2, -2, -1, 4, -6, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -2, 3, -3, 4, -4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -2, 3, -3, 4, -4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, -2, -1, 1, 5, -5, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, -2, -1, 1, 5, -5, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, 3, -6, 1, 2, -3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, 3, -6, 1, 2, -3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -3, -2, 1, 2, -1, 2, -2]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -3, -2, 1, 2, -1, 2, -2]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -1, -1, 2, -2, 2, -1, 1, -2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -1, -1, 2, -2, 2, -1, 1, -2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -15, 5, 5, 5, -15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -15, 5, 5, 5, -15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, -1, -3, 2, 1, -3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, -1, -3, 2, 1, -3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, 4, -1, -1, -1, -1, 4, -1, -1, -1, -1, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, 4, -1, -1, -1, -1, 4, -1, -1, -1, -1, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, -1, -2, -3, -4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, -1, -2, -3, -4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -2, -3, 1, 2, -1, 3, -3, 2, -2, 5, -5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -2, -3, 1, 2, -1, 3, -3, 2, -2, 5, -5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -1, -2, -1, 4, -4, 1, 1, 1, -3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -1, -2, -1, 4, -4, 1, 1, 1, -3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, -3, 2, -2, 2, -2, 3, -7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, -3, 2, -2, 2, -2, 3, -7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, -9, 4, -5, 3, -2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, -9, 4, -5, 3, -2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, -14, 7, -7, 7, -7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, -14, 7, -7, 7, -7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, 5, 5, 6, 6, -7, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, 5, 5, 6, 6, -7, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -10, 5, 5, -10, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -10, 5, 5, -10, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, -9, 3, -3, 3, -3, 3, -3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, -9, 3, -3, 3, -3, 3, -3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -2, 1, -1, 3, -3, 2, -2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -2, 1, -1, 3, -3, 2, -2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, -1, -2, 1, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, -1, -2, 1, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, -1, 2, -5, 6, -3, 2, -1, 5, -10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, -1, 2, -5, 6, -3, 2, -1, 5, -10]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-1, 1, -1, 1]) == 2
    assert candidate(nums = [10]) == 0
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [-2, 2, -2, 2]) == 2
    assert candidate(nums = [1, -1, 1, -1]) == 2
    assert candidate(nums = [2, 3, -5]) == 1
    assert candidate(nums = [5, 5, -10]) == 1
    assert candidate(nums = [10, 10, 10, -30]) == 1
    assert candidate(nums = [1, 2, 3, -6]) == 1
    assert candidate(nums = [10, 20, -30, 10]) == 1
    assert candidate(nums = [10, -5, -5]) == 1
    assert candidate(nums = [10, -10, 10, -10]) == 2
    assert candidate(nums = [1, 1, 1, 1, -4]) == 1
    assert candidate(nums = [-5, 5, -5, 5]) == 2
    assert candidate(nums = [-10]) == 0
    assert candidate(nums = [-1, -2, -3, 6]) == 1
    assert candidate(nums = [3, 2, -3, -4]) == 0
    assert candidate(nums = [5, -2, -3, 1, 4, -4]) == 1
    assert candidate(nums = [-5, -5, 10]) == 1
    assert candidate(nums = [7, -3, 2, -4, 1, -1, 3, -3, 2, -2]) == 0
    assert candidate(nums = [5, -2, -3, 1, 4, -4, -6, 6]) == 1
    assert candidate(nums = [-1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 6
    assert candidate(nums = [5, -2, 3, -3, 2, -5, 1]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -20]) == 0
    assert candidate(nums = [1, 2, 3, 4, -10, 1, 2, 3, 4, -10]) == 2
    assert candidate(nums = [-2, -2, -2, 6, -2, -2, -2, 6, -2, -2, -2]) == 2
    assert candidate(nums = [2, -1, 2, -1, 2, -1, 2, -1, 2, -1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, -15]) == 1
    assert candidate(nums = [5, 5, -10, 1, -1, 1]) == 2
    assert candidate(nums = [5, -2, 3, -6, 4, -1, -6]) == 1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4]) == 4
    assert candidate(nums = [10, -10, 10, -10, 10, -10]) == 3
    assert candidate(nums = [-3, 3, -3, 3, -3, 3]) == 3
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 1]) == 0
    assert candidate(nums = [1, 1, 1, 1, -4, 1, 1, 1, 1, -4, 1, 1, 1, 1, -4]) == 3
    assert candidate(nums = [7, -3, 2, -6, 1, 1, 1, -1, 1]) == 1
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 8
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == 5
    assert candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 11
    assert candidate(nums = [4, -1, -3, 2, 2, -4]) == 2
    assert candidate(nums = [7, -3, 3, -7, 4, -2, 2, -4]) == 2
    assert candidate(nums = [-7, 3, 4, -1, -2, 2, 1, -4, 6, -2]) == 3
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 0
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 9]) == 1
    assert candidate(nums = [-2, 4, -2, -2, 4, -2, -2, 4]) == 2
    assert candidate(nums = [-1, -1, 2, 2, -4, 4, -5, 5, -6, 6]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, -9]) == 1
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 5
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 10
    assert candidate(nums = [5, 5, -10, 5, -5, 5, -5]) == 3
    assert candidate(nums = [-3, -2, 5, -1, 4, -6, 2, 3]) == 1
    assert candidate(nums = [-3, 1, 2, -4, 1, 1, 1, -1]) == 1
    assert candidate(nums = [-10, 5, 5, -5, 5, -5, 5, -5, 5]) == 4
    assert candidate(nums = [-1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == 0
    assert candidate(nums = [1, 2, 3, -3, -2, -1, 4, -4, 5, -5]) == 3
    assert candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, -4, 1, 1, 1]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, -45]) == 1
    assert candidate(nums = [2, 2, 2, -6, 1, -1, 1, -1, 1]) == 3
    assert candidate(nums = [5, -3, 2, -2, 2, -2, -2, 2]) == 1
    assert candidate(nums = [-2, 2, -2, 2, -2, 2]) == 3
    assert candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [-5, 5, -5, 5, -5, 5, -5]) == 3
    assert candidate(nums = [-10, 5, 5, -3, 3, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(nums = [7, -2, -2, -2, -1, 8, -1, -2, -2, -2]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1]) == 3
    assert candidate(nums = [4, -1, 2, -5, 0, 3, -3]) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 1
    assert candidate(nums = [5, -2, -2, -1, 10, -5, 5]) == 1
    assert candidate(nums = [3, -1, -2, 3, -1, -2, 3, -1, -2, 3, -1, -2]) == 4
    assert candidate(nums = [7, -3, -1, -2, 3, -4, 1, 1, 1, -3, 5, -2, -1, 1, -1, -1, -1, -1, -1, 1]) == 3
    assert candidate(nums = [1, -1, 2, -2, 3, -3]) == 3
    assert candidate(nums = [-10, 10, -5, 5, -3, 3, -2, 2]) == 4
    assert candidate(nums = [4, -3, 2, -1, 4, -3, 2, -1]) == 0
    assert candidate(nums = [5, -2, 3, -6, 4, -1, -2, 3]) == 1
    assert candidate(nums = [10, -1, -2, -3, -4, -5, -6, -7, -8, -9, 45]) == 1
    assert candidate(nums = [10, -5, 3, -8, 2, -2, 4, -4, 6, -6, 5, -5]) == 5
    assert candidate(nums = [2, 2, 2, 2, -8, 2, 2, 2, 2, -8]) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -100]) == 0
    assert candidate(nums = [2, 3, -5, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == 9
    assert candidate(nums = [-10, 5, 3, -8, 2, 1, -2, 2, 1, -1]) == 0
    assert candidate(nums = [3, -3, 3, -3, 3, -3, 3, -3, 3, -3]) == 5
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == 10
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10]) == 4
    assert candidate(nums = [1, 1, -2, 1, -1, 3, -3, 2, -1, -1]) == 4
    assert candidate(nums = [-1, -2, -3, -4, -5, 15]) == 1
    assert candidate(nums = [2, 3, -5, 4, -4, -3, 3, 2, -2, 1, -1]) == 5
    assert candidate(nums = [-10, 5, 5, -1, 1, -1, 1, 0, 3, -3]) == 5
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == 0
    assert candidate(nums = [10, -10, 5, -5, 3, -3, 2, -2, 1, -1]) == 5
    assert candidate(nums = [-10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, -5, 5, -5, 5, -5]) == 3
    assert candidate(nums = [7, -3, -4, 1, 2, -2, -1, 4, -6, 2]) == 3
    assert candidate(nums = [2, -2, 3, -3, 4, -4]) == 3
    assert candidate(nums = [5, -2, -2, -1, 1, 5, -5, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2]) == 1
    assert candidate(nums = [5, -2, 3, -6, 1, 2, -3]) == 2
    assert candidate(nums = [7, -3, -2, 1, 2, -1, 2, -2]) == 0
    assert candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [2, -1, -1, 2, -2, 2, -1, 1, -2, 2]) == 3
    assert candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, -15, 5, 5, 5, -15]) == 2
    assert candidate(nums = [4, -1, -3, 2, 1, -3]) == 2
    assert candidate(nums = [-1, -1, -1, -1, 4, -1, -1, -1, -1, 4, -1, -1, -1, -1, 4]) == 3
    assert candidate(nums = [1, 2, 3, 4, -1, -2, -3, -4]) == 1
    assert candidate(nums = [2, -2, 2, -2, 2, -2, 2, -2, 2, -2]) == 5
    assert candidate(nums = [5, -2, -3, 1, 2, -1, 3, -3, 2, -2, 5, -5]) == 1
    assert candidate(nums = [3, -1, -2, -1, 4, -4, 1, 1, 1, -3]) == 2
    assert candidate(nums = [-10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [7, -3, 2, -2, 2, -2, 3, -7]) == 1
    assert candidate(nums = [7, 2, -9, 4, -5, 3, -2, 1]) == 2
    assert candidate(nums = [7, 7, -14, 7, -7, 7, -7]) == 3
    assert candidate(nums = [-1, -2, -3, -4, 5, 5, 6, 6, -7, 7]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1]) == 4
    assert candidate(nums = [1, -1, 1, -1, 1, -1]) == 3
    assert candidate(nums = [5, -10, 5, 5, -10, 5]) == 2
    assert candidate(nums = [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, 1, 1, 1, 1, -5, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == 8
    assert candidate(nums = [3, 3, 3, -9, 3, -3, 3, -3, 3, -3]) == 4
    assert candidate(nums = [-1, 2, -2, 1, -1, 3, -3, 2, -2]) == 1
    assert candidate(nums = [2, 3, -1, -2, 1, -3, 4, -4, 5, -5, 6, -6, 7, -7]) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55]) == 1
    assert candidate(nums = [4, -1, 2, -5, 6, -3, 2, -1, 5, -10]) == 1


