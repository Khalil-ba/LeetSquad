def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5]) == [-3, -1, 1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5]) == [-3, -1, 1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10]) == [-1, 0, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10]) == [-1, 0, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3]) == [-2, -1, 0, 1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3]) == [-2, -1, 0, 1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46]) == [-3, -1, 1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46]) == [-3, -1, 1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == [-3, -1, 1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == [-3, -1, 1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5]) == [0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5]) == [0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42]) == [0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42]) == [0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == [-3, -1, 1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == [-3, -1, 1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3]) == [-1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3]) == [-1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [-2, -1, 0, 1, 1, 2, 3, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [-2, -1, 0, 1, 1, 2, 3, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 3, 4, 2]) == [-2, -1, 0, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 3, 4, 2]) == [-2, -1, 0, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1]) == [-2, -1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1]) == [-2, -1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 2, 1]) == [-1, 0, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 2, 1]) == [-1, 0, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10]) == [-3, -1, 1, 3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10]) == [-3, -1, 1, 3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 23, 12, 34, 56, 78, 90, 12, 34, 56]) == [-5, -3, -2, -2, -1, 1, 3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 23, 12, 34, 56, 78, 90, 12, 34, 56]) == [-5, -3, -2, -2, -1, 1, 3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 13, 24, 35, 42, 13, 24, 35]) == [-3, -2, -1, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 13, 24, 35, 42, 13, 24, 35]) == [-3, -2, -1, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 20, 10, 30, 20, 10]) == [-2, -1, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 20, 10, 30, 20, 10]) == [-2, -1, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 23, 12, 45, 56, 78, 89, 90, 12, 23]) == [-6, -5, -4, -2, 0, 2, 4, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 23, 12, 45, 56, 78, 89, 90, 12, 23]) == [-6, -5, -4, -2, 0, 2, 4, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [-3, -3, -3, -2, -1, -1, -1, 0, 1, 1, 1, 2, 3, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [-3, -3, -3, -2, -1, -1, -1, 0, 1, 1, 1, 2, 3, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [-2, -2, -2, -2, -1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [-2, -2, -2, -2, -1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [-28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [-28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [-4, -4, -4, -4, -3, -2, -2, -2, -2, -1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [-4, -4, -4, -4, -3, -2, -2, -2, -2, -1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1, 3, 2, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1, 3, 2, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == [-9, -9, -8, -7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == [-9, -9, -8, -7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [-1, 0, 0, 0, 0, 0, 0, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [-1, 0, 0, 0, 0, 0, 0, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == [-3, -2, -1, 0, 0, 0, 0, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == [-3, -2, -1, 0, 0, 0, 0, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [-2, -1, 0, 0, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [-2, -1, 0, 0, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [-2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [-2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 4, 4, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [-4, -4, -3, -3, -3, -3, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 4, 4, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [-4, -4, -3, -3, -3, -3, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 4, 3, 5, 6, 7, 8, 9]) == [-7, -6, -4, -4, -2, -1, 1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 4, 3, 5, 6, 7, 8, 9]) == [-7, -6, -4, -4, -2, -1, 1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 3, 1, 4, 1, 3, 2, 3, 4, 2, 1, 3, 4, 2, 1, 3, 2, 4, 1]) == [-3, -2, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 3, 1, 4, 1, 3, 2, 3, 4, 2, 1, 3, 4, 2, 1, 3, 2, 4, 1]) == [-3, -2, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [-8, -7, -6, -5, -4, -3, -2, -1, -1, -1, 0, 0, 2, 3, 3, 4, 5, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [-8, -7, -6, -5, -4, -3, -2, -1, -1, -1, 0, 0, 2, 3, 3, 4, 5, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17, 16, 18, 17, 19, 18, 20, 19]) == [-19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17, 16, 18, 17, 19, 18, 20, 19]) == [-19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == [-3, -3, -3, -3, -2, -1, -1, -1, -1, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == [-3, -3, -3, -3, -2, -1, -1, -1, -1, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [-10, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [-10, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [-18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [-18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]) == [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]) == [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21]) == [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21]) == [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == [-3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == [-3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 20, 10, 30, 30, 40, 40, 50, 50]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 20, 10, 30, 30, 40, 40, 50, 50]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == [-48, -46, -44, -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == [-48, -46, -44, -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-4, -2, -2, 0, 0, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-4, -2, -2, 0, 0, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [-4, -4, -3, -2, -2, -1, 0, 0, 1, 2, 2, 3, 4, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [-4, -4, -3, -2, -2, -1, 0, 0, 1, 2, 2, 3, 4, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == [-3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == [-3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 10, 10, 5, 5, 1, 1, 20, 20, 25, 25, 30, 30, 35, 35]) == [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 10, 10, 5, 5, 1, 1, 20, 20, 25, 25, 30, 30, 35, 35]) == [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 8, 8, 8, 9, 9, 9, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [-7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 8, 8, 8, 9, 9, 9, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [-7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == [-4, -3, -2, -2, -2, -1, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == [-4, -3, -2, -2, -2, -1, 1, 2, 3, 4, 5]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 2, 4, 5]) == [-3, -1, 1, 3, 5]
    assert candidate(nums = [10, 20, 10, 20, 10]) == [-1, 0, 0, 1, 2]
    assert candidate(nums = [1, 1, 2, 2, 3]) == [-2, -1, 0, 1, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    assert candidate(nums = [1]) == [1]
    assert candidate(nums = [50, 49, 48, 47, 46]) == [-3, -1, 1, 3, 5]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [10, 20, 30, 40, 50]) == [-3, -1, 1, 3, 5]
    assert candidate(nums = [5, 5, 5, 5, 5]) == [0, 0, 0, 0, 1]
    assert candidate(nums = [42, 42, 42, 42, 42]) == [0, 0, 0, 0, 1]
    assert candidate(nums = [1, 2, 3, 4, 5]) == [-3, -1, 1, 3, 5]
    assert candidate(nums = [1, 2, 2, 3, 3]) == [-1, 0, 1, 2, 3]
    assert candidate(nums = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [-2, -1, 0, 1, 1, 2, 3, 3, 3, 4]
    assert candidate(nums = [3, 2, 3, 4, 2]) == [-2, -1, 0, 2, 3]
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    assert candidate(nums = [1, 2, 3, 2, 1]) == [-2, -1, 1, 2, 3]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(nums = [1, 2, 1, 2, 1]) == [-1, 0, 0, 1, 2]
    assert candidate(nums = [50, 40, 30, 20, 10]) == [-3, -1, 1, 3, 5]
    assert candidate(nums = [34, 23, 12, 34, 56, 78, 90, 12, 34, 56]) == [-5, -3, -2, -2, -1, 1, 3, 4, 5, 6]
    assert candidate(nums = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]
    assert candidate(nums = [42, 13, 24, 35, 42, 13, 24, 35]) == [-3, -2, -1, 0, 1, 2, 3, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [10, 20, 30, 20, 10, 30, 20, 10]) == [-2, -1, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [34, 23, 12, 45, 56, 78, 89, 90, 12, 23]) == [-6, -5, -4, -2, 0, 2, 4, 6, 7, 8]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == [-3, -3, -3, -2, -1, -1, -1, 0, 1, 1, 1, 2, 3, 3, 3, 4]
    assert candidate(nums = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == [-2, -2, -2, -2, -1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 1, 2, 3, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [-28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [-4, -4, -4, -4, -3, -2, -2, -2, -2, -1, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 1, 3, 2, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == [-9, -9, -8, -7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10]
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [-1, 0, 0, 0, 0, 0, 0, 0, 1, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]
    assert candidate(nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == [-3, -2, -1, 0, 0, 0, 0, 0, 1, 2, 3, 4]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == [-2, -1, 0, 0, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [10, 20, 10, 30, 20, 40, 30, 50, 40, 60]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 2, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == [-2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [1, 1, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 4, 4, 3, 3, 2, 2, 1, 1, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [-4, -4, -3, -3, -3, -3, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [1, 3, 2, 3, 4, 3, 5, 6, 7, 8, 9]) == [-7, -6, -4, -4, -2, -1, 1, 3, 5, 7, 9]
    assert candidate(nums = [1, 3, 2, 3, 1, 4, 1, 3, 2, 3, 4, 2, 1, 3, 4, 2, 1, 3, 2, 4, 1]) == [-3, -2, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]) == [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == [-8, -7, -6, -5, -4, -3, -2, -1, -1, -1, 0, 0, 2, 3, 3, 4, 5, 7, 8, 9]
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17, 16, 18, 17, 19, 18, 20, 19]) == [-19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
    assert candidate(nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == [-3, -3, -3, -3, -2, -1, -1, -1, -1, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 4]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == [-10, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [-18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40]) == [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11]
    assert candidate(nums = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == [-13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]
    assert candidate(nums = [42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21, 42, 21]) == [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 4, 5]
    assert candidate(nums = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]) == [-5, -4, -3, -2, -1, 0, 1, 3, 4, 6]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == [-3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4]
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    assert candidate(nums = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [10, 20, 20, 10, 30, 30, 40, 40, 50, 50]) == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == [-48, -46, -44, -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    assert candidate(nums = [5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [-4, -2, -2, 0, 0, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [-4, -4, -3, -2, -2, -1, 0, 0, 1, 2, 2, 3, 4, 4, 5]
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == [-3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [15, 15, 10, 10, 5, 5, 1, 1, 20, 20, 25, 25, 30, 30, 35, 35]) == [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7, 3, 5, 7]) == [-2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-2, -1, 0, 0, 0, 0, 1, 2, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [-4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    assert candidate(nums = [7, 7, 7, 8, 8, 8, 9, 9, 9, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [-7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [-9, -8, -7, -6, -5, -3, -1, 1, 3, 5, 6, 7, 8, 9, 10]
    assert candidate(nums = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == [-4, -3, -2, -2, -2, -1, 1, 2, 3, 4, 5]


