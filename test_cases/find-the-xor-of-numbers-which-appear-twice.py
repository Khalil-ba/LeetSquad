def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 30, 30, 40, 50]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 30, 30, 40, 50]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 9, 9, 10, 10, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 9, 9, 10, 10, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 20, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 20, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 6, 7, 7, 8, 8, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 6, 7, 7, 8, 8, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 7, 8, 8, 7]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 7, 8, 8, 7]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 6, 6, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 6, 6, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 1, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 1, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 4, 5, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 4, 5, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 25, 25, 35]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 25, 25, 35]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 11, 11, 12]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 11, 11, 12]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 30, 20, 30, 40]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 30, 20, 30, 40]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 7, 8, 8, 9, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 7, 8, 8, 9, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 33, 44, 44, 55, 55, 66, 66]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 33, 44, 44, 55, 55, 66, 66]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 7, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 7, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 5, 6, 7, 5, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 5, 6, 7, 5, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20, 30, 30, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20, 30, 30, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 4, 20, 36]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 4, 20, 36]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 60, 70, 80, 90, 100]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 60, 70, 80, 90, 100]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 5, 6, 7, 8]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 5, 6, 7, 8]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 1, 3, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 1, 3, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 33, 36, 39, 42, 45, 48]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 33, 36, 39, 42, 45, 48]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 50, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 50, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 45, 44, 44, 43, 43, 42, 42, 41, 41, 40, 40, 39, 39, 38, 38, 37, 37, 36, 36, 35, 35, 34, 34, 33, 33, 32, 32, 31, 31, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24, 24, 23, 23, 22, 22, 21, 21, 20, 20, 19, 19, 18, 18, 17, 17, 16, 16, 15, 15, 14, 14, 13, 13, 12, 12, 11, 11, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 45, 44, 44, 43, 43, 42, 42, 41, 41, 40, 40, 39, 39, 38, 38, 37, 37, 36, 36, 35, 35, 34, 34, 33, 33, 32, 32, 31, 31, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24, 24, 23, 23, 22, 22, 21, 21, 20, 20, 19, 19, 18, 18, 17, 17, 16, 16, 15, 15, 14, 14, 13, 13, 12, 12, 11, 11, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 15, 30]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 15, 30]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 50]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 50]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 50, 7, 14, 21, 28, 35, 42, 49]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 50, 7, 14, 21, 28, 35, 42, 49]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [14, 28, 14, 42, 56, 70, 84, 56, 70, 84, 98, 98]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [14, 28, 14, 42, 56, 70, 84, 56, 70, 84, 98, 98]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 3, 6, 9]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 3, 6, 9]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 35, 40, 45, 50, 35, 40, 45]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 35, 40, 45, 50, 35, 40, 45]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 3, 6, 9, 12, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 3, 6, 9, 12, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 5, 10, 15, 20, 25, 30, 35, 5, 10, 15, 20, 25, 30]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 5, 10, 15, 20, 25, 30, 35, 5, 10, 15, 20, 25, 30]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 15, 16, 17, 18, 19]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 15, 16, 17, 18, 19]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 16, 17, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 49, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 16, 17, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 49, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 3, 5, 7, 7, 9, 11, 11, 13, 15, 15, 17, 19, 19, 21, 21, 23, 25, 25]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 3, 5, 7, 7, 9, 11, 11, 13, 15, 15, 17, 19, 19, 21, 21, 23, 25, 25]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 7, 30, 40]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 7, 30, 40]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 13, 26, 39, 52, 65, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 8, 16, 24, 32, 40, 48]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 13, 26, 39, 52, 65, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 8, 16, 24, 32, 40, 48]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 46, 47, 48, 49, 50, 45, 46, 47, 48, 49, 50]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 46, 47, 48, 49, 50, 45, 46, 47, 48, 49, 50]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 42, 24, 24, 36, 36, 18, 18, 30, 30, 21, 21, 9, 9, 27, 27, 33, 33, 15, 15]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 42, 24, 24, 36, 36, 18, 18, 30, 30, 21, 21, 9, 9, 27, 27, 33, 33, 15, 15]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 45, 30, 30, 25, 25, 20, 15, 10, 5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 45, 30, 30, 25, 25, 20, 15, 10, 5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 55, 60, 65, 70]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 55, 60, 65, 70]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 199]) == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 199]) == 208: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 1, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 1, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 1, 2, 3, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 1, 2, 3, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 3, 6, 9, 12, 15, 18, 21]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 3, 6, 9, 12, 15, 18, 21]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 15, 15, 20, 25, 25, 30, 35, 35, 40, 45, 45, 50, 50]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 15, 15, 20, 25, 25, 30, 35, 35, 40, 45, 45, 50, 50]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 46, 47, 48, 49, 50, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 46, 47, 48, 49, 50, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 1, 2, 3, 4, 5]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 1, 2, 3, 4, 5]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 1, 3, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 1, 3, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 17, 19, 19, 21, 21, 23, 23, 25, 25, 27, 27, 29, 29, 31, 31, 33, 33, 35, 35, 37, 37, 39, 39, 41, 41, 43, 43, 45, 45, 47, 47, 49, 49, 51, 51]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 17, 19, 19, 21, 21, 23, 23, 25, 25, 27, 27, 29, 29, 31, 31, 33, 33, 35, 35, 37, 37, 39, 39, 41, 41, 43, 43, 45, 45, 47, 47, 49, 49, 51, 51]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 33, 44, 55, 66, 77, 88, 99, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 33, 44, 55, 66, 77, 88, 99, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 23, 25, 25, 27, 27, 29, 29, 31, 31, 33, 33, 35, 35, 37, 37, 39, 39, 41, 41, 43, 43, 45, 45, 47, 47, 49, 49]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 23, 25, 25, 27, 27, 29, 29, 31, 31, 33, 33, 35, 35, 37, 37, 39, 39, 41, 41, 43, 43, 45, 45, 47, 47, 49, 49]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 2, 4, 6, 8, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 2, 4, 6, 8, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 20, 25, 30, 35, 40, 45, 50, 15, 20, 25, 30, 35, 40, 45, 50]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 20, 25, 30, 35, 40, 45, 50, 15, 20, 25, 30, 35, 40, 45, 50]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 30, 40, 40, 50, 20]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 30, 40, 40, 50, 20]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 10, 40, 50, 60, 70, 80, 90, 50, 20, 100]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 10, 40, 50, 60, 70, 80, 90, 50, 20, 100]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 50, 8, 16, 24, 32, 40, 48]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 50, 8, 16, 24, 32, 40, 48]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 24, 13, 24, 42, 35, 13, 47, 50, 40, 47, 35, 40, 50]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 24, 13, 24, 42, 35, 13, 47, 50, 40, 47, 35, 40, 50]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 30, 15, 60, 45, 30, 15, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 30, 15, 60, 45, 30, 15, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 26, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 26, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 57: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 10, 20, 30, 30, 40, 50]) == 20
    assert candidate(nums = [8, 8, 9, 9, 10, 10, 11]) == 11
    assert candidate(nums = [10, 10, 20, 20, 30]) == 30
    assert candidate(nums = [5, 5, 6, 7, 7, 8, 8, 9]) == 10
    assert candidate(nums = [4, 5, 6, 7, 8, 8, 7]) == 15
    assert candidate(nums = [30, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
    assert candidate(nums = [5, 5, 5, 5, 6, 6, 7]) == 6
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4]) == 4
    assert candidate(nums = [1, 2, 2, 1]) == 3
    assert candidate(nums = [1, 2, 1, 3]) == 1
    assert candidate(nums = [4, 5, 6, 4, 5, 7]) == 1
    assert candidate(nums = [42]) == 0
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]) == 1
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [15, 15, 25, 25, 35]) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 50
    assert candidate(nums = [10, 10, 11, 11, 12]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 1
    assert candidate(nums = [10, 10, 20, 30, 20, 30, 40]) == 0
    assert candidate(nums = [4, 5, 6, 7, 8, 8, 9, 9]) == 1
    assert candidate(nums = [33, 33, 44, 44, 55, 55, 66, 66]) == 120
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [4, 5, 6, 7, 4, 5]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 5]) == 0
    assert candidate(nums = [1, 2, 3]) == 0
    assert candidate(nums = [49, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 49
    assert candidate(nums = [7]) == 0
    assert candidate(nums = [4, 5, 6, 7, 5, 4]) == 1
    assert candidate(nums = [10, 10, 20, 30, 30, 40]) == 20
    assert candidate(nums = [2, 2]) == 2
    assert candidate(nums = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 4, 20, 36]) == 4
    assert candidate(nums = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 1]) == 23
    assert candidate(nums = [4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24]) == 24
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 60, 70, 80, 90, 100]) == 14
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 5, 6, 7, 8]) == 12
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 1, 3, 5]) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]) == 26
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 33, 36, 39, 42, 45, 48]) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]) == 26
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 50, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]) == 0
    assert candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 0
    assert candidate(nums = [45, 45, 44, 44, 43, 43, 42, 42, 41, 41, 40, 40, 39, 39, 38, 38, 37, 37, 36, 36, 35, 35, 34, 34, 33, 33, 32, 32, 31, 31, 30, 30, 29, 29, 28, 28, 27, 27, 26, 26, 25, 25, 24, 24, 23, 23, 22, 22, 21, 21, 20, 20, 19, 19, 18, 18, 17, 17, 16, 16, 15, 15, 14, 14, 13, 13, 12, 12, 11, 11, 10, 10]) == 0
    assert candidate(nums = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 15, 30]) == 17
    assert candidate(nums = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31]) == 1
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 50]) == 51
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 50, 7, 14, 21, 28, 35, 42, 49]) == 56
    assert candidate(nums = [14, 28, 14, 42, 56, 70, 84, 56, 70, 84, 98, 98]) == 70
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 0
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]) == 59
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 3, 6, 9]) == 12
    assert candidate(nums = [1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 10
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 35, 40, 45, 50, 35, 40, 45]) == 50
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 11
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5]) == 7
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 3, 6, 9, 12, 15]) == 15
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 5, 10, 15, 20, 25, 30, 35, 5, 10, 15, 20, 25, 30]) == 8
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 31
    assert candidate(nums = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 15, 16, 17, 18, 19]) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 16, 17, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 49, 50]) == 5
    assert candidate(nums = [1, 3, 3, 5, 7, 7, 9, 11, 11, 13, 15, 15, 17, 19, 19, 21, 21, 23, 25, 25]) == 31
    assert candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 7, 30, 40]) == 49
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 0
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 3
    assert candidate(nums = [49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 3
    assert candidate(nums = [13, 26, 39, 52, 65, 13, 26, 39, 52, 65, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 8, 16, 24, 32, 40, 48]) == 125
    assert candidate(nums = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 26, 27, 28, 29, 30]) == 7
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert candidate(nums = [45, 46, 47, 48, 49, 50, 45, 46, 47, 48, 49, 50]) == 31
    assert candidate(nums = [42, 42, 24, 24, 36, 36, 18, 18, 30, 30, 21, 21, 9, 9, 27, 27, 33, 33, 15, 15]) == 51
    assert candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == 1
    assert candidate(nums = [45, 45, 30, 30, 25, 25, 20, 15, 10, 5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]) == 42
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 55, 60, 65, 70]) == 11
    assert candidate(nums = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 3
    assert candidate(nums = [23, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 199]) == 208
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 1, 3]) == 2
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6]) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 1, 2, 3, 4, 5]) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21]) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 22
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [3, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 3, 6, 9, 12, 15, 18, 21]) == 11
    assert candidate(nums = [5, 5, 10, 15, 15, 20, 25, 25, 30, 35, 35, 40, 45, 45, 50, 50]) == 47
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20]) == 20
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50]) == 38
    assert candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [45, 46, 47, 48, 49, 50, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 31
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 27
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 1, 2, 3, 4, 5]) == 56
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 1, 3, 5]) == 7
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1]) == 11
    assert candidate(nums = [23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50]) == 45
    assert candidate(nums = [17, 17, 19, 19, 21, 21, 23, 23, 25, 25, 27, 27, 29, 29, 31, 31, 33, 33, 35, 35, 37, 37, 39, 39, 41, 41, 43, 43, 45, 45, 47, 47, 49, 49, 51, 51]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15]) == 1
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 11, 22, 33, 44, 55, 66, 77, 88, 99, 1]) == 19
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]) == 56
    assert candidate(nums = [3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21, 23, 23, 25, 25, 27, 27, 29, 29, 31, 31, 33, 33, 35, 35, 37, 37, 39, 39, 41, 41, 43, 43, 45, 45, 47, 47, 49, 49]) == 48
    assert candidate(nums = [5, 5, 10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50]) == 7
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 2, 4, 6, 8, 10]) == 2
    assert candidate(nums = [15, 20, 25, 30, 35, 40, 45, 50, 15, 20, 25, 30, 35, 40, 45, 50]) == 8
    assert candidate(nums = [10, 20, 10, 30, 40, 40, 50, 20]) == 54
    assert candidate(nums = [10, 20, 30, 10, 40, 50, 60, 70, 80, 90, 50, 20, 100]) == 44
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 50, 8, 16, 24, 32, 40, 48]) == 56
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 0
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [42, 24, 13, 24, 42, 35, 13, 47, 50, 40, 47, 35, 40, 50]) == 41
    assert candidate(nums = [45, 30, 15, 60, 45, 30, 15, 60, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 11
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 7
    assert candidate(nums = [25, 26, 26, 27, 28, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) == 57


