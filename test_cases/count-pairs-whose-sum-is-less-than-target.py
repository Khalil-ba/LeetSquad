def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],target = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],target = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50],target = -80) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50],target = -80) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],target = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],target = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],target = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],target = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],target = -3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],target = -3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],target = -5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],target = -5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-6, 2, 5, -2, -7, -1, 3],target = -2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-6, 2, 5, -2, -7, -1, 3],target = -2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],target = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],target = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],target = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],target = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],target = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],target = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, 2, 3, 1],target = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, 2, 3, 1],target = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],target = -8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],target = -8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -50, 25, -25],target = 0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -50, 25, -25],target = 0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -10, 3, 8, 0, -2],target = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -10, 3, 8, 0, -2],target = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, -25, 0, 15, -15, 10, -10, 5, -5, 20, -20],target = 0) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, -25, 0, 15, -15, 10, -10, 5, -5, 20, -20],target = 0) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 15, 5, -5, -15, -25, 35, 45, 55, -45],target = 0) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 15, 5, -5, -15, -25, 35, 45, 55, -45],target = 0) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-15, -25, -35, -45, -55],target = -70) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-15, -25, -35, -45, -55],target = -70) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],target = -2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],target = -2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2, -3, -4, -5, -6, -7, -8, -9],target = -3) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2, -3, -4, -5, -6, -7, -8, -9],target = -3) == 42: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],target = 25) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],target = 25) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-3, -2, -1, 0, 1, 2, 3],target = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-3, -2, -1, 0, 1, 2, 3],target = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = 0) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = 0) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45],target = 5) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45],target = 5) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],target = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],target = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],target = 50) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],target = 50) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30],target = -10) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30],target = -10) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 1128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 1128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 160: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-49, -47, -45, -43, -41, -39, -37, -35, -33, -31, -29, -27, -25, -23, -21, -19, -17, -15, -13, -11],target = -50) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-49, -47, -45, -43, -41, -39, -37, -35, -33, -31, -29, -27, -25, -23, -21, -19, -17, -15, -13, -11],target = -50) == 134: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 46, 47, 48, 49, 50, -45, -46, -47, -48, -49, -50],target = 0) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 46, 47, 48, 49, 50, -45, -46, -47, -48, -49, -50],target = 0) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 7, 1, 8, 4, 3, 6],target = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 7, 1, 8, 4, 3, 6],target = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 15, -15, 25, -25, 35],target = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 15, -15, 25, -25, 35],target = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 50, 45, 35, 25, 15, 5, 0, -5, -15, -25, -35, -45, -50, -45, -35, -25, -15, -5, 0, 5, 15, 25, 35, 45, 50, 45, 35, 25, 15, 5, 0, -5, -15, -25, -35, -45, -50, -45, -35, -25, -15, -5],target = 10) == 604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 50, 45, 35, 25, 15, 5, 0, -5, -15, -25, -35, -45, -50, -45, -35, -25, -15, -5, 0, 5, 15, 25, 35, 45, 50, 45, 35, 25, 15, 5, 0, -5, -15, -25, -35, -45, -50, -45, -35, -25, -15, -5],target = 10) == 604: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, -50, 40, -40, 30, -30, 20, -20, 10, -10],target = 1) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, -50, 40, -40, 30, -30, 20, -20, 10, -10],target = 1) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, -2, -3, 3],target = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, -2, -3, 3],target = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 15, -15, 25, -25],target = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 15, -15, 25, -25],target = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 0, 10, -20, 20, -30, 30, -40, 40, -50, 50],target = 10) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 0, 10, -20, 20, -30, 30, -40, 40, -50, 50],target = 10) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-45, -40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45],target = -5) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-45, -40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45],target = -5) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -31, -33, -35, -37, -39, -41, -43, -45, -47, -49, -50],target = 10) == 775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -31, -33, -35, -37, -39, -41, -43, -45, -47, -49, -50],target = 10) == 775: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3],target = 0) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3],target = 0) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-4, -3, -2, -1, 0, 1, 2, 3, 4],target = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-4, -3, -2, -1, 0, 1, 2, 3, 4],target = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17],target = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17],target = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, -10, -20, -30],target = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, -10, -20, -30],target = 10) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 50) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 50) == 625: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],target = 8) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],target = 8) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-2, -3, -4, -5, -6, 1, 2, 3, 4, 5],target = -5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-2, -3, -4, -5, -6, 1, 2, 3, 4, 5],target = -5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [48, 49, 50, -48, -49, -50],target = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [48, 49, 50, -48, -49, -50],target = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50],target = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50],target = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -5) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -5) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25],target = 10) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25],target = 10) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 50) == 576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 50) == 576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 180) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 180) == 43: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],target = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],target = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],target = 200) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],target = 200) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0],target = 1) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0],target = 1) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, 30, 35, 40, 45, 50, -30, -35, -40, -45, -50],target = 15) == 129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, 30, 35, 40, 45, 50, -30, -35, -40, -45, -50],target = 15) == 129: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1, 1, 0],target = 1) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1, 1, 0],target = 1) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],target = 0) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],target = 0) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40],target = 90) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40],target = 90) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -25, 0, 50, -100],target = 0) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -25, 0, 50, -100],target = 0) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 25) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 25) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30, 40],target = -15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30, 40],target = -15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = 0) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = 0) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],target = 30) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],target = 30) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],target = 2) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],target = 2) == 35: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50, -60],target = -5) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50, -60],target = -5) == 33: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30],target = 90) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30],target = 90) == 170: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50],target = -25) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50],target = -25) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 24, 25, 26, 27, 28, 29, 30],target = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 24, 25, 26, 27, 28, 29, 30],target = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, 0, 50, -40, 40],target = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, 0, 50, -40, 40],target = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55],target = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55],target = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3],target = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3],target = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-25, -25, -25, -25, -25],target = -50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-25, -25, -25, -25, -25],target = -50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0],target = -10) == 1245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0],target = -10) == 1245: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30],target = -5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30],target = -5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],target = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],target = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 0],target = -5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 0],target = -5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30],target = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30],target = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40],target = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40],target = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-49, -48, -47, -46, -45, -44, -43, -42, -41, -40],target = -80) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-49, -48, -47, -46, -45, -44, -43, -42, -41, -40],target = -80) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, -45, 44, -44, 43, -43, 42],target = 0) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, -45, 44, -44, 43, -43, 42],target = 0) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 0, 10, 20, 30, 40, 50],target = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 0, 10, 20, 30, 40, 50],target = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],target = 0) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],target = 0) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 20) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 20) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],target = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],target = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],target = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],target = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],target = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],target = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5],target = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5],target = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5],target = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5],target = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [49, -49, 48, -48, 47, -47, 46, -46, 45, -45],target = 0) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [49, -49, 48, -48, 47, -47, 46, -46, 45, -45],target = 0) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70],target = -100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70],target = -100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -5, -5, -5, -5, 5, 5, 5, 5, 5],target = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -5, -5, -5, -5, 5, 5, 5, 5, 5],target = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, 10, 20, 30, 0],target = -15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, 10, 20, 30, 0],target = -15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == 90: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 190) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 190) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -11) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -11) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, -3, 6, 2, 7, 4, 1, -5, -10],target = 5) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, -3, 6, 2, 7, 4, 1, -5, -10],target = 5) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46],target = 99) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46],target = 99) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 17, 42, 8, 3, 19, 5, 28],target = 30) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 17, 42, 8, 3, 19, 5, 28],target = 30) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -2, 2, -3, 3],target = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -2, 2, -3, 3],target = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15],target = 45) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15],target = 45) == 46: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [5, 5, 5, 5, 5],target = 15) == 10
    assert candidate(nums = [-10, -20, -30, -40, -50],target = -80) == 1
    assert candidate(nums = [1, 3, 5, 7, 9],target = 10) == 4
    assert candidate(nums = [1, 1, 1, 1, 1],target = 3) == 10
    assert candidate(nums = [0, 0, 0, 0, 0],target = 0) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],target = 10) == 10
    assert candidate(nums = [-1, -2, -3, -4, -5],target = -3) == 9
    assert candidate(nums = [-5, -4, -3, -2, -1],target = -5) == 6
    assert candidate(nums = [-6, 2, 5, -2, -7, -1, 3],target = -2) == 10
    assert candidate(nums = [0, 0, 0, 0, 0],target = 1) == 10
    assert candidate(nums = [0, 0, 0, 0],target = 1) == 6
    assert candidate(nums = [10, 20, 30, 40, 50],target = 100) == 10
    assert candidate(nums = [-1, 1, 2, 3, 1],target = 2) == 3
    assert candidate(nums = [-5, -4, -3, -2, -1],target = -8) == 1
    assert candidate(nums = [50, -50, 25, -25],target = 0) == 2
    assert candidate(nums = [-5, -10, 3, 8, 0, -2],target = 1) == 9
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -15) == 6
    assert candidate(nums = [25, -25, 0, 15, -15, 10, -10, 5, -5, 20, -20],target = 0) == 25
    assert candidate(nums = [25, 15, 5, -5, -15, -25, 35, 45, 55, -45],target = 0) == 13
    assert candidate(nums = [-15, -25, -35, -45, -55],target = -70) == 4
    assert candidate(nums = [-5, -4, -3, -2, -1],target = -2) == 10
    assert candidate(nums = [-1, -1, -2, -3, -4, -5, -6, -7, -8, -9],target = -3) == 42
    assert candidate(nums = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50],target = 25) == 32
    assert candidate(nums = [-3, -2, -1, 0, 1, 2, 3],target = 1) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = 0) == 90
    assert candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45],target = 5) == 90
    assert candidate(nums = [0, 0, 0, 0, 0],target = 0) == 0
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],target = 50) == 64
    assert candidate(nums = [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30],target = -10) == 25
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 1128
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 30) == 160
    assert candidate(nums = [-49, -47, -45, -43, -41, -39, -37, -35, -33, -31, -29, -27, -25, -23, -21, -19, -17, -15, -13, -11],target = -50) == 134
    assert candidate(nums = [45, 46, 47, 48, 49, 50, -45, -46, -47, -48, -49, -50],target = 0) == 30
    assert candidate(nums = [5, 2, 7, 1, 8, 4, 3, 6],target = 10) == 16
    assert candidate(nums = [5, -5, 15, -15, 25, -25, 35],target = 0) == 6
    assert candidate(nums = [5, 15, 25, 35, 45, 50, 45, 35, 25, 15, 5, 0, -5, -15, -25, -35, -45, -50, -45, -35, -25, -15, -5, 0, 5, 15, 25, 35, 45, 50, 45, 35, 25, 15, 5, 0, -5, -15, -25, -35, -45, -50, -45, -35, -25, -15, -5],target = 10) == 604
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],target = 1) == 45
    assert candidate(nums = [50, -50, 40, -40, 30, -30, 20, -20, 10, -10],target = 1) == 25
    assert candidate(nums = [-1, 0, 1, 2, -2, -3, 3],target = 1) == 12
    assert candidate(nums = [5, -5, 15, -15, 25, -25],target = 0) == 6
    assert candidate(nums = [-10, 0, 10, -20, 20, -30, 30, -40, 40, -50, 50],target = 10) == 30
    assert candidate(nums = [-45, -40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45],target = -5) == 72
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 50, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -31, -33, -35, -37, -39, -41, -43, -45, -47, -49, -50],target = 10) == 775
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3],target = 0) == 9
    assert candidate(nums = [-4, -3, -2, -1, 0, 1, 2, 3, 4],target = 1) == 20
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17],target = 15) == 8
    assert candidate(nums = [30, 20, 10, 0, -10, -20, -30],target = 10) == 12
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 50) == 625
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],target = 8) == 25
    assert candidate(nums = [-2, -3, -4, -5, -6, 1, 2, 3, 4, 5],target = -5) == 9
    assert candidate(nums = [48, 49, 50, -48, -49, -50],target = 0) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 15) == 12
    assert candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50],target = 10) == 20
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -5) == 41
    assert candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25],target = 10) == 35
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],target = 50) == 576
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 180) == 43
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],target = 1) == 20
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],target = 200) == 44
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0],target = 1) == 21
    assert candidate(nums = [25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, 30, 35, 40, 45, 50, -30, -35, -40, -45, -50],target = 15) == 129
    assert candidate(nums = [-1, 0, 1, 0, -1, 1, 0],target = 1) == 14
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10],target = 0) == 20
    assert candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40],target = 90) == 25
    assert candidate(nums = [100, -50, 25, -25, 0, 50, -100],target = 0) == 9
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 25) == 29
    assert candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30, 40],target = -15) == 12
    assert candidate(nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],target = 0) == 25
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],target = 30) == 27
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],target = -15) == 6
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5],target = 2) == 35
    assert candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50, -60],target = -5) == 33
    assert candidate(nums = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30],target = 90) == 170
    assert candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50],target = -25) == 16
    assert candidate(nums = [23, 24, 25, 26, 27, 28, 29, 30],target = 50) == 4
    assert candidate(nums = [-50, 0, 50, -40, 40],target = 10) == 6
    assert candidate(nums = [15, 25, 35, 45, 55],target = 100) == 9
    assert candidate(nums = [1, -1, 2, -2, 3, -3],target = 0) == 6
    assert candidate(nums = [-25, -25, -25, -25, -25],target = -50) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == 20
    assert candidate(nums = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0],target = -10) == 1245
    assert candidate(nums = [-40, -30, -20, -10, 0, 10, 20, 30],target = -5) == 16
    assert candidate(nums = [0, 0, 0, 0, 0],target = 1) == 10
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 0],target = -5) == 25
    assert candidate(nums = [10, -10, 20, -20, 30, -30],target = 0) == 6
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 36
    assert candidate(nums = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40],target = 20) == 9
    assert candidate(nums = [-49, -48, -47, -46, -45, -44, -43, -42, -41, -40],target = -80) == 45
    assert candidate(nums = [45, -45, 44, -44, 43, -43, 42],target = 0) == 9
    assert candidate(nums = [-10, 0, 10, 20, 30, 40, 50],target = 0) == 1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],target = 0) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 20) == 75
    assert candidate(nums = [5, 4, 3, 2, 1],target = 6) == 4
    assert candidate(nums = [5, 4, 3, 2, 1],target = 7) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],target = 0) == 10
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5],target = 4) == 9
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 20) == 20
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5],target = 3) == 6
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 10) == 0
    assert candidate(nums = [49, -49, 48, -48, 47, -47, 46, -46, 45, -45],target = 0) == 20
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70],target = -100) == 4
    assert candidate(nums = [-5, -5, -5, -5, -5, 5, 5, 5, 5, 5],target = 0) == 10
    assert candidate(nums = [-10, -20, -30, 10, 20, 30, 0],target = -15) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == 90
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 190) == 44
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 15) == 36
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],target = -11) == 20
    assert candidate(nums = [5, 8, -3, 6, 2, 7, 4, 1, -5, -10],target = 5) == 24
    assert candidate(nums = [50, 49, 48, 47, 46],target = 99) == 9
    assert candidate(nums = [23, 17, 42, 8, 3, 19, 5, 28],target = 30) == 11
    assert candidate(nums = [-1, 0, 1, -2, 2, -3, 3],target = 1) == 12
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15],target = 45) == 46


