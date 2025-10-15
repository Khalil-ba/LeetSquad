def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, -1, 8, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, -1, 8, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 7, 3, 6, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 7, 3, 6, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -500, 250, 250, -1000, 500, 500, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -500, 250, 250, -1000, 500, 500, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 0, -100, 0, 100, 0, -100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 0, -100, 0, 100, 0, -100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, 25, -100, 50, 50]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, 25, -100, 50, 50]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 2, -4, 3, 0, 1, -2, 3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 2, -4, 3, 0, 1, -2, 3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -10, 10, 5, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -10, 10, 5, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 5, -5, 5, -5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 5, -5, 5, -5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -2, 1, 6, -4, 2, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -2, 1, 6, -4, 2, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, -300, 400, -500, 600, -700, 800]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, -300, 400, -500, 600, -700, 800]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 2, -4, 3, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 2, -4, 3, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -1500, 600, 700]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -1500, 600, 700]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 0, 1000, -1000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 0, 1000, -1000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 500, -250, 125, -62, 31, -15, 7, -3, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 500, -250, 125, -62, 31, -15, 7, -3, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, 4, -3, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, 4, -3, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, -210]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, -210]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 0, 5, -5, 5, -5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 0, 5, -5, 5, -5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 0, 1, -1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 0, 1, -1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 10, 10, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 10, 10, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -500, 250, -125, 62, -31, 15, -7, 3, -1, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -500, 250, -125, 62, -31, 15, -7, 3, -1, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6, 3, -3, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6, 3, -3, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 500, -500, 250, -250]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 500, -500, 250, -250]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 500, -500, 0, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 500, -500, 0, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 1, 5, 2, -4, 3, 0, 0, 0, 0]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 1, 5, 2, -4, 3, 0, 0, 0, 0]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -500, 250, -125, 62, -31, 15, -7, 3, -1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -500, 250, -125, 62, -31, 15, -7, 3, -1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -20, 20, -30, 30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -20, 20, -30, 30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0]) == 20: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, -1, 4]) == 2
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [1, 100]) == -1
    assert candidate(nums = [0, 1]) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5]) == -1
    assert candidate(nums = [2, 5]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == -1
    assert candidate(nums = [1, 0]) == 0
    assert candidate(nums = [2, 3, -1, 8, 4]) == 3
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6]) == -1
    assert candidate(nums = [-1, -1, -1, -1]) == -1
    assert candidate(nums = [1, 7, 3, 6, 5, 6]) == 3
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [1000, -1000, 1000, -1000]) == -1
    assert candidate(nums = [1, 1]) == -1
    assert candidate(nums = [1, 2, 3]) == -1
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000]) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5, -6]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [1000, -500, 250, 250, -1000, 500, 500, 0, 0, 0]) == 0
    assert candidate(nums = [100, 0, -100, 0, 100, 0, -100]) == 3
    assert candidate(nums = [100, -50, 25, 25, -100, 50, 50]) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == -1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == -1
    assert candidate(nums = [7, 1, 5, 2, -4, 3, 0, 1, -2, 3]) == -1
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1
    assert candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == 0
    assert candidate(nums = [5, -10, 10, 5, 0]) == -1
    assert candidate(nums = [-5, 5, -5, 5, -5, 5]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == -1
    assert candidate(nums = [3, -2, 1, 6, -4, 2, 5]) == -1
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == -1
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40]) == 6
    assert candidate(nums = [100, 200, -300, 400, -500, 600, -700, 800]) == -1
    assert candidate(nums = [7, 1, 5, 2, -4, 3, 0]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == -1
    assert candidate(nums = [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]) == -1
    assert candidate(nums = [10, -10, 20, -20, 30, -30]) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, -1500, 600, 700]) == -1
    assert candidate(nums = [1000, -1000, 0, 1000, -1000]) == 2
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == -1
    assert candidate(nums = [-1000, 500, -250, 125, -62, 31, -15, 7, -3, 1]) == -1
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5]) == 0
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
    assert candidate(nums = [-1, -2, -3, -4, -5, 15]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]) == 9
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == -1
    assert candidate(nums = [1, -2, 3, 4, -3, 2]) == -1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, -210]) == -1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [10, -10, 0, 5, -5, 5, -5]) == 2
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == -1
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == -1
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000, 1000, -1000]) == -1
    assert candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40]) == -1
    assert candidate(nums = [0, 1, 0, -1, 0, 1, 0, -1]) == 0
    assert candidate(nums = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == -1
    assert candidate(nums = [1000, -1000, 500, -500, 250, -250, 125, -125]) == -1
    assert candidate(nums = [0, 1, 2, 3, 4, 3, 2, 1, 0]) == 4
    assert candidate(nums = [1, -1, 0, 1, -1]) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 7
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [10, 20, 30, 10, 10, 30]) == -1
    assert candidate(nums = [1000, -500, 250, -125, 62, -31, 15, -7, 3, -1, 0]) == -1
    assert candidate(nums = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(nums = [1000, -1000, 1000, -1000, 1000, -1000]) == -1
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6, 3, -3, 1, -1]) == -1
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == -1
    assert candidate(nums = [1, -1, 2, -2, 3, -3]) == -1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == -1
    assert candidate(nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 9
    assert candidate(nums = [1000, -1000, 500, -500, 250, -250]) == -1
    assert candidate(nums = [1000, -1000, 500, -500, 0, 0]) == 4
    assert candidate(nums = [7, 1, 5, 2, -4, 3, 0, 0, 0, 0]) == -1
    assert candidate(nums = [1000, -500, 250, -125, 62, -31, 15, -7, 3, -1, 1]) == -1
    assert candidate(nums = [-10, 10, -20, 20, -30, 30]) == -1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0]) == 20


