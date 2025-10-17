def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9],k = 3,x = 2) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9],k = 3,x = 2) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],k = 2,x = 2) == [-1, -2, -3, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],k = 2,x = 2) == [-1, -2, -3, -4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, -3, -2, 3],k = 3,x = 2) == [-1, -2, -2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, -3, -2, 3],k = 3,x = 2) == [-1, -2, -2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9],k = 3,x = 1) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9],k = 3,x = 1) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],k = 4,x = 3) == [-20, -30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],k = 4,x = 3) == [-20, -30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],k = 3,x = 3) == [-10, -20, -30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],k = 3,x = 3) == [-10, -20, -30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],k = 4,x = 2) == [-30, -40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],k = 4,x = 2) == [-30, -40]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],k = 2,x = 2) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],k = 2,x = 2) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, 1, 2, -3, 0, -3],k = 2,x = 1) == [-3, 0, -3, -3, -3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, 1, 2, -3, 0, -3],k = 2,x = 1) == [-3, 0, -3, -3, -3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 8,x = 4) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 8,x = 4) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41],k = 5,x = 2) == [-49, -48, -47, -46, -45, -44]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41],k = 5,x = 2) == [-49, -48, -47, -46, -45, -44]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5],k = 5,x = 1) == [0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5],k = 5,x = 1) == [0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 3,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 3,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 0, -2, 0, -3, 0, -4, 0, -5, 0, -6, 0, -7, 0, -8, 0, -9, 0, -10],k = 4,x = 2) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 0, -2, 0, -3, 0, -4, 0, -5, 0, -6, 0, -7, 0, -8, 0, -9, 0, -10],k = 4,x = 2) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40],k = 5,x = 2) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40],k = 5,x = 2) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 3) == [0, -1, 0, -2, 0, -3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 3) == [0, -1, 0, -2, 0, -3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],k = 5,x = 5) == [-5, -10, -15, -20, -25, -30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],k = 5,x = 5) == [-5, -10, -15, -20, -25, -30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -10, 5, -15, 20, -25, 0, 30, -35],k = 4,x = 2) == [-10, -10, -15, -15, 0, -25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -10, 5, -15, 20, -25, 0, 30, -35],k = 4,x = 2) == [-10, -10, -15, -15, 0, -25]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],k = 10,x = 5) == [-1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],k = 10,x = 5) == [-1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 6,x = 2) == [-5, -6, -7, -8, -9, -10, -11, -12, -13, -14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 6,x = 2) == [-5, -6, -7, -8, -9, -10, -11, -12, -13, -14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 2) == [-1, -2, -2, -3, -3, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 2) == [-1, -2, -2, -3, -3, -4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],k = 5,x = 2) == [-40, -40, -40, -40, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],k = 5,x = 2) == [-40, -40, -40, -40, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10,x = 5) == [0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10,x = 5) == [0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10,x = 5) == [-6, -6, -6, -6, -6, -6, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10,x = 5) == [-6, -6, -6, -6, -6, -6, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46, 45, -45],k = 7,x = 4) == [0, -47, 0, -46, 0, -45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46, 45, -45],k = 7,x = 4) == [0, -47, 0, -46, 0, -45]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 10,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 10,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -13, 14, -14, 15, -15, 16, -16],k = 6,x = 3) == [-2, -2, -4, -4, -6, -6, -8, -8, -10, -10, -12, -12, -13, -13, -14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -13, 14, -14, 15, -15, 16, -16],k = 6,x = 3) == [-2, -2, -4, -4, -6, -6, -8, -8, -10, -10, -12, -12, -13, -13, -14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5,x = 2) == [-4, -5, -6, -7, -8, -9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5,x = 2) == [-4, -5, -6, -7, -8, -9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 4,x = 3) == [0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 4,x = 3) == [0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, 10, 20, 30, 40, 50],k = 4,x = 3) == [-20, -30, -30, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, 10, 20, 30, 40, 50],k = 4,x = 3) == [-20, -30, -30, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,x = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,x = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5],k = 6,x = 4) == [-2, -1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5],k = 6,x = 4) == [-2, -1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],k = 5,x = 3) == [-30, -30, -30, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],k = 5,x = 3) == [-30, -30, -30, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,x = 2) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,x = 2) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, -2, 0, -3, 0, -4, 0, -5, 0],k = 3,x = 2) == [-1, -1, -2, 0, -3, 0, -4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, -2, 0, -3, 0, -4, 0, -5, 0],k = 3,x = 2) == [-1, -1, -2, 0, -3, 0, -4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 10,x = 5) == [-6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 10,x = 5) == [-6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, 4, 5, -6, -7, 8, 9, -10],k = 4,x = 2) == [-2, -2, -3, -6, -6, -6, -7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, 4, 5, -6, -7, 8, 9, -10],k = 4,x = 2) == [-2, -2, -3, -6, -6, -6, -7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 5,x = 3) == [0, -10, 0, -20, 0, -30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 5,x = 3) == [0, -10, 0, -20, 0, -30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8],k = 6,x = 3) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8],k = 6,x = 3) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4],k = 3,x = 1) == [-1, -2, -2, -2, -3, -3, -3, -4, -4, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4],k = 3,x = 1) == [-1, -2, -2, -2, -3, -3, -3, -4, -4, -4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 2) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 2) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10,x = 3) == [0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10,x = 3) == [0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 6,x = 4) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 6,x = 4) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4],k = 4,x = 2) == [-1, -1, -2, -2, -3, -3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4],k = 4,x = 2) == [-1, -1, -2, -2, -3, -3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 6,x = 3) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 6,x = 3) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -10, 40, -20, 30, -30, 20, -40, 10, -50, 0, 5, -5, 15, -15, 25, -25, 35, -35, 45],k = 5,x = 2) == [-10, -20, -20, -30, -30, -40, -40, -40, -5, -5, -5, -5, -15, -15, -25, -25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -10, 40, -20, 30, -30, 20, -40, 10, -50, 0, 5, -5, 15, -15, 25, -25, 35, -35, 45],k = 5,x = 2) == [-10, -20, -20, -30, -30, -40, -40, -40, -5, -5, -5, -5, -15, -15, -25, -25]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 6,x = 1) == [0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 6,x = 1) == [0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4,x = 1) == [0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4,x = 1) == [0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],k = 5,x = 2) == [0, 0, -4, -4, -4, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],k = 5,x = 2) == [0, 0, -4, -4, -4, -4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6],k = 7,x = 5) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6],k = 7,x = 5) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 4,x = 2) == [-10, -10, -20, -20, -30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 4,x = 2) == [-10, -10, -20, -20, -30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],k = 5,x = 2) == [-40, -30, -20, -10, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],k = 5,x = 2) == [-40, -30, -20, -10, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 3, -1, 7, -8, 2, -6, 4, -9],k = 4,x = 2) == [-1, -1, -1, -1, -6, -6, -6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 3, -1, 7, -8, 2, -6, 4, -9],k = 4,x = 2) == [-1, -1, -1, -1, -6, -6, -6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, -5, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40, 45, -45, 50, -50],k = 7,x = 4) == [0, -5, -5, -10, 0, -15, 0, -20, 0, -25, 0, -30, 0, -35]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, -5, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40, 45, -45, 50, -50],k = 7,x = 4) == [0, -5, -5, -10, 0, -15, 0, -20, 0, -25, 0, -30, 0, -35]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 0, 5, -10, 15, -20, 25, -30, 35, -40],k = 4,x = 2) == [-5, 0, -10, -10, -20, -20, -30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 0, 5, -10, 15, -20, 25, -30, 35, -40],k = 4,x = 2) == [-5, 0, -10, -10, -20, -20, -30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 3) == [-1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 3) == [-1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 6,x = 4) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 6,x = 4) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 5,x = 3) == [0, -48, 0, -47, 0, -46]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 5,x = 3) == [0, -48, 0, -47, 0, -46]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 7,x = 5) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 7,x = 5) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 5,x = 2) == [-1, -2, -2, -3, -3, -4, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 5,x = 2) == [-1, -2, -2, -3, -3, -4, -4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4,x = 2) == [-2, -3, -4, -5, -6, -7, -8, -9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4,x = 2) == [-2, -3, -4, -5, -6, -7, -8, -9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 1) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 1) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 6,x = 4) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 6,x = 4) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40],k = 6,x = 4) == [-20, -10, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40],k = 6,x = 4) == [-20, -10, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50],k = 5,x = 4) == [0, 0, 0, 0, 0, -10, -20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50],k = 5,x = 4) == [0, 0, 0, 0, 0, -10, -20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 5,x = 3) == [-1, 0, -2, 0, -3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 5,x = 3) == [-1, 0, -2, 0, -3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 8,x = 4) == [-1, -3, -3, -5, -5, -7, -7, -9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 8,x = 4) == [-1, -3, -3, -5, -5, -7, -7, -9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4,x = 3) == [-1, -2, -3, -4, -5, -6, -7, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4,x = 3) == [-1, -2, -3, -4, -5, -6, -7, -8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3,x = 2) == [0, -1, 0, -1, 0, -1, 0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3,x = 2) == [0, -1, 0, -1, 0, -1, 0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10,x = 5) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10,x = 5) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 3) == [-1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 3) == [-1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 6,x = 3) == [-1, -3, -3, -5, -5, -7, -7, -9, -9, -11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 6,x = 3) == [-1, -3, -3, -5, -5, -7, -7, -9, -9, -11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, -5, -10, 15, -15, 20, -20, 25, -25, 30],k = 4,x = 2) == [-5, -5, -10, -10, -15, -15, -20, -20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, -5, -10, 15, -15, 20, -20, 25, -25, 30],k = 4,x = 2) == [-5, -5, -10, -10, -15, -15, -20, -20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, -1, -2, 5, -3, 6, -4, 8, -5, 9, -6, 10, -7, 11, -8, 12, -9, 13, -10],k = 5,x = 3) == [0, -1, -1, -2, 0, -3, 0, -4, 0, -5, 0, -6, 0, -7, 0, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, -1, -2, 5, -3, 6, -4, 8, -5, 9, -6, 10, -7, 11, -8, 12, -9, 13, -10],k = 5,x = 3) == [0, -1, -1, -2, 0, -3, 0, -4, 0, -5, 0, -6, 0, -7, 0, -8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7,x = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7,x = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 4,x = 2) == [-1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 4,x = 2) == [-1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4],k = 5,x = 2) == [-1, 0, -2, -2, 0, -3, -3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4],k = 5,x = 2) == [-1, 0, -2, -2, 0, -3, -3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, 0, 50, -49, 0, 49, -48, 0, 48, -47, 0, 47],k = 5,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, 0, 50, -49, 0, 49, -48, 0, 48, -47, 0, 47],k = 5,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, 0, 50, -49, 49, -48, 48, -47, 47],k = 6,x = 4) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, 0, 50, -49, 49, -48, 48, -47, 47],k = 6,x = 4) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],k = 5,x = 4) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],k = 5,x = 4) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 4,x = 2) == [-10, -10, -20, -20, -30, -30, -40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 4,x = 2) == [-10, -10, -20, -20, -30, -30, -40]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 5,x = 4) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 5,x = 4) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 4,x = 1) == [0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 4,x = 1) == [0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 2) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 2) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, 0, 10, 20, 30, -40, 40, -50, 50],k = 6,x = 3) == [-10, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, 0, 10, 20, 30, -40, 40, -50, 50],k = 6,x = 3) == [-10, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],k = 5,x = 3) == [-1, 0, -3, 0, -5, 0, -7, 0, -9, 0, -11, 0, -13, 0, -15, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],k = 5,x = 3) == [-1, 0, -3, 0, -5, 0, -7, 0, -9, 0, -11, 0, -13, 0, -15, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4],k = 5,x = 3) == [0, -1, 0, -2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4],k = 5,x = 3) == [0, -1, 0, -2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 5) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 5) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12],k = 8,x = 6) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12],k = 8,x = 6) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 5,x = 3) == [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 5,x = 3) == [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, -1, 0, 0, 0, 0],k = 4,x = 1) == [0, 0, -1, -1, -1, -1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, -1, 0, 0, 0, 0],k = 4,x = 1) == [0, 0, -1, -1, -1, -1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],k = 10,x = 3) == [-5, -7, -7, -9, -9, -11, -11, -13, -13, -15, -15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],k = 10,x = 3) == [-5, -7, -7, -9, -9, -11, -11, -13, -13, -15, -15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -3, 6, -6, 9, -9, 12, -12, 15, -15],k = 7,x = 3) == [-3, -6, -6, -9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -3, 6, -6, 9, -9, 12, -12, 15, -15],k = 7,x = 3) == [-3, -6, -6, -9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 2) == [-1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 2) == [-1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, -10, -20, -30, 10, 20, 30, -10, -20, -30],k = 6,x = 3) == [-10, -10, -10, -10, -10, -10, -10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, -10, -20, -30, 10, 20, 30, -10, -20, -30],k = 6,x = 3) == [-10, -10, -10, -10, -10, -10, -10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4],k = 3,x = 1) == [-1, -2, -2, -2, -3, -3, -3, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4],k = 3,x = 1) == [-1, -2, -2, -2, -3, -3, -3, -4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],k = 3,x = 2) == [-10, -15, -20, -25, -30, -35, -40, -45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],k = 3,x = 2) == [-10, -15, -20, -25, -30, -35, -40, -45]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0],k = 6,x = 2) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0],k = 6,x = 2) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, -2, -3, 1, -4, 5, -6, 7, -8],k = 3,x = 2) == [-2, -2, -3, 0, -4, 0, -6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, -2, -3, 1, -4, 5, -6, 7, -8],k = 3,x = 2) == [-2, -2, -3, 0, -4, 0, -6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50],k = 5,x = 3) == [-10, 0, -20, 0, -30, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50],k = 5,x = 3) == [-10, 0, -20, 0, -30, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 6, 7, 8, 9],k = 3,x = 2) == [0, 0, 0]
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 2,x = 2) == [-1, -2, -3, -4]
    assert candidate(nums = [1, -1, -3, -2, 3],k = 3,x = 2) == [-1, -2, -2]
    assert candidate(nums = [5, 6, 7, 8, 9],k = 3,x = 1) == [0, 0, 0]
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 4,x = 3) == [-20, -30]
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 3,x = 3) == [-10, -20, -30]
    assert candidate(nums = [-10, -20, -30, -40, -50],k = 4,x = 2) == [-30, -40]
    assert candidate(nums = [5, 4, 3, 2, 1],k = 2,x = 2) == [0, 0, 0, 0]
    assert candidate(nums = [-3, 1, 2, -3, 0, -3],k = 2,x = 1) == [-3, 0, -3, -3, -3]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 8,x = 4) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7]
    assert candidate(nums = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41],k = 5,x = 2) == [-49, -48, -47, -46, -45, -44]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5],k = 5,x = 1) == [0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5]
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 3,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [0, -1, 0, -2, 0, -3, 0, -4, 0, -5, 0, -6, 0, -7, 0, -8, 0, -9, 0, -10],k = 4,x = 2) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -8, -8, -9]
    assert candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40],k = 5,x = 2) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 3) == [0, -1, 0, -2, 0, -3]
    assert candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],k = 5,x = 5) == [-5, -10, -15, -20, -25, -30]
    assert candidate(nums = [-5, -10, 5, -15, 20, -25, 0, 30, -35],k = 4,x = 2) == [-10, -10, -15, -15, 0, -25]
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10],k = 10,x = 5) == [-1, -2, -2, -3, -3, -4, -4, -5, -5, -6, -6]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 6,x = 2) == [-5, -6, -7, -8, -9, -10, -11, -12, -13, -14]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 2) == [-1, -2, -2, -3, -3, -4]
    assert candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],k = 5,x = 2) == [-40, -40, -40, -40, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10,x = 5) == [0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10,x = 5) == [-6, -6, -6, -6, -6, -6, 0, 0, 0, 0, 0]
    assert candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46, 45, -45],k = 7,x = 4) == [0, -47, 0, -46, 0, -45]
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 10,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -13, 14, -14, 15, -15, 16, -16],k = 6,x = 3) == [-2, -2, -4, -4, -6, -6, -8, -8, -10, -10, -12, -12, -13, -13, -14]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5,x = 2) == [-4, -5, -6, -7, -8, -9]
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],k = 4,x = 3) == [0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-10, -20, -30, -40, -50, 10, 20, 30, 40, 50],k = 4,x = 3) == [-20, -30, -30, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10,x = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5],k = 6,x = 4) == [-2, -1, 0, 0, 0]
    assert candidate(nums = [-10, -20, -30, -40, -50, 50, 40, 30, 20, 10],k = 5,x = 3) == [-30, -30, -30, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3,x = 2) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, -1, -2, 0, -3, 0, -4, 0, -5, 0],k = 3,x = 2) == [-1, -1, -2, 0, -3, 0, -4, 0]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],k = 10,x = 5) == [-6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]
    assert candidate(nums = [-1, -2, -3, 4, 5, -6, -7, 8, 9, -10],k = 4,x = 2) == [-2, -2, -3, -6, -6, -6, -7]
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 5,x = 3) == [0, -10, 0, -20, 0, -30]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8],k = 6,x = 3) == [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5, -6]
    assert candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4],k = 3,x = 1) == [-1, -2, -2, -2, -3, -3, -3, -4, -4, -4]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 2) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10,x = 3) == [0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8]
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 6,x = 4) == [0, 0, 0, 0, 0]
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4],k = 4,x = 2) == [-1, -1, -2, -2, -3, -3]
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 6,x = 3) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [50, -10, 40, -20, 30, -30, 20, -40, 10, -50, 0, 5, -5, 15, -15, 25, -25, 35, -35, 45],k = 5,x = 2) == [-10, -20, -20, -30, -30, -40, -40, -40, -5, -5, -5, -5, -15, -15, -25, -25]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 6,x = 1) == [0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4,x = 1) == [0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1],k = 5,x = 2) == [0, 0, -4, -4, -4, -4]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6],k = 7,x = 5) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 4,x = 2) == [-10, -10, -20, -20, -30]
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],k = 5,x = 2) == [-40, -30, -20, -10, 0, 0, 0]
    assert candidate(nums = [10, -5, 3, -1, 7, -8, 2, -6, 4, -9],k = 4,x = 2) == [-1, -1, -1, -1, -6, -6, -6]
    assert candidate(nums = [5, 10, -5, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40, 45, -45, 50, -50],k = 7,x = 4) == [0, -5, -5, -10, 0, -15, 0, -20, 0, -25, 0, -30, 0, -35]
    assert candidate(nums = [-5, 0, 5, -10, 15, -20, 25, -30, 35, -40],k = 4,x = 2) == [-5, 0, -10, -10, -20, -20, -30]
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 3) == [-1, -1, -1, -1, -1, -1]
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 6,x = 4) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 5,x = 3) == [0, -48, 0, -47, 0, -46]
    assert candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 7,x = 5) == [0, 0, 0, 0]
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 5,x = 2) == [-1, -2, -2, -3, -3, -4, -4]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4,x = 2) == [-2, -3, -4, -5, -6, -7, -8, -9]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 1) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [50, -50, 49, -49, 48, -48, 47, -47, 46, -46],k = 6,x = 4) == [0, 0, 0, 0, 0]
    assert candidate(nums = [-50, -40, -30, -20, -10, 0, 10, 20, 30, 40],k = 6,x = 4) == [-20, -10, 0, 0, 0]
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50],k = 5,x = 4) == [0, 0, 0, 0, 0, -10, -20]
    assert candidate(nums = [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5],k = 5,x = 3) == [-1, 0, -2, 0, -3, 0]
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 8,x = 4) == [-1, -3, -3, -5, -5, -7, -7, -9]
    assert candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4,x = 3) == [-1, -2, -3, -4, -5, -6, -7, -8]
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3,x = 2) == [0, -1, 0, -1, 0, -1, 0, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10,x = 5) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 3) == [-1, -1, -1, -1]
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15],k = 6,x = 3) == [-1, -3, -3, -5, -5, -7, -7, -9, -9, -11]
    assert candidate(nums = [5, 10, -5, -10, 15, -15, 20, -20, 25, -25, 30],k = 4,x = 2) == [-5, -5, -10, -10, -15, -15, -20, -20]
    assert candidate(nums = [2, 3, -1, -2, 5, -3, 6, -4, 8, -5, 9, -6, 10, -7, 11, -8, 12, -9, 13, -10],k = 5,x = 3) == [0, -1, -1, -2, 0, -3, 0, -4, 0, -5, 0, -6, 0, -7, 0, -8]
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3,x = 1) == [-1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7,x = 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 4,x = 2) == [-1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4],k = 5,x = 2) == [-1, 0, -2, -2, 0, -3, -3, 0]
    assert candidate(nums = [-50, 0, 50, -49, 0, 49, -48, 0, 48, -47, 0, 47],k = 5,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-50, 0, 50, -49, 49, -48, 48, -47, 47],k = 6,x = 4) == [0, 0, 0, 0]
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],k = 5,x = 4) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -6, -7, -8]
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 4,x = 2) == [-10, -10, -20, -20, -30, -30, -40]
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40],k = 5,x = 4) == [0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7,x = 3) == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 4,x = 1) == [0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 2) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-10, -20, -30, 0, 10, 20, 30, -40, 40, -50, 50],k = 6,x = 3) == [-10, 0, 0, 0, 0, 0]
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],k = 5,x = 3) == [-1, 0, -3, 0, -5, 0, -7, 0, -9, 0, -11, 0, -13, 0, -15, 0]
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4],k = 5,x = 3) == [0, -1, 0, -2, 0]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5,x = 5) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12],k = 8,x = 6) == [0, 0, 0, 0, 0]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],k = 5,x = 3) == [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]
    assert candidate(nums = [0, 0, 0, 0, 0, -1, 0, 0, 0, 0],k = 4,x = 1) == [0, 0, -1, -1, -1, -1, 0]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20],k = 10,x = 3) == [-5, -7, -7, -9, -9, -11, -11, -13, -13, -15, -15]
    assert candidate(nums = [3, -3, 6, -6, 9, -9, 12, -12, 15, -15],k = 7,x = 3) == [-3, -6, -6, -9]
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],k = 5,x = 2) == [-1, -1, -1, -1, -1, -1]
    assert candidate(nums = [10, 20, 30, -10, -20, -30, 10, 20, 30, -10, -20, -30],k = 6,x = 3) == [-10, -10, -10, -10, -10, -10, -10]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 3,x = 1) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [-1, 0, 1, -2, 0, 2, -3, 0, 3, -4],k = 3,x = 1) == [-1, -2, -2, -2, -3, -3, -3, -4]
    assert candidate(nums = [-5, -10, -15, -20, -25, -30, -35, -40, -45, -50],k = 3,x = 2) == [-10, -15, -20, -25, -30, -35, -40, -45]
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0],k = 6,x = 2) == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert candidate(nums = [3, -2, -3, 1, -4, 5, -6, 7, -8],k = 3,x = 2) == [-2, -2, -3, 0, -4, 0, -6]
    assert candidate(nums = [-10, 10, -20, 20, -30, 30, -40, 40, -50, 50],k = 5,x = 3) == [-10, 0, -20, 0, -30, 0]


