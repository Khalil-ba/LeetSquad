def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5],value = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5],value = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],value = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],value = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30],value = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30],value = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4],value = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4],value = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -10, -15, -20, -25],value = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -10, -15, -20, -25],value = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],value = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],value = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40],value = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40],value = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -10, 7, 13, 6, 8],value = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -10, 7, 13, 6, 8],value = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -10, 7, 13, 6, 8],value = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -10, 7, 13, 6, 8],value = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],value = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],value = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],value = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],value = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],value = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],value = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -4, -3, -2, -1],value = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -4, -3, -2, -1],value = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],value = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],value = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],value = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],value = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6],value = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6],value = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5],value = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5],value = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 13) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 13) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150],value = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150],value = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],value = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],value = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],value = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],value = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],value = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],value = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 16) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 16) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 7) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 7) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],value = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],value = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7],value = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7],value = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],value = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],value = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],value = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],value = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],value = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],value = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100],value = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100],value = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],value = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],value = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],value = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],value = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 2000000000, -2000000000, 0],value = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 2000000000, -2000000000, 0],value = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],value = 3) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],value = 3) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 3) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 3) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],value = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],value = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],value = 7) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],value = 7) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0],value = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0],value = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 1) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 1) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 7) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 7) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 120, 131, 142, 153, 164, 175, 186, 197, 208, 219],value = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 120, 131, 142, 153, 164, 175, 186, 197, 208, 219],value = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81],value = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81],value = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],value = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],value = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 12) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 12) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60],value = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60],value = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],value = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],value = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996],value = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996],value = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],value = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],value = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],value = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],value = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],value = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],value = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],value = 1000000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],value = 1000000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],value = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],value = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],value = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],value = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81],value = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81],value = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],value = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],value = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],value = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],value = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19],value = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19],value = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],value = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],value = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],value = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],value = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 19) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 19) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27],value = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27],value = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],value = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],value = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],value = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],value = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 0],value = 100000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 0],value = 100000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],value = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],value = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],value = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],value = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],value = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],value = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],value = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],value = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],value = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],value = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],value = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],value = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],value = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],value = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000000, -2000000000, -3000000000, -4000000000, -5000000000],value = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000000, -2000000000, -3000000000, -4000000000, -5000000000],value = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],value = 1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],value = 1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5],value = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5],value = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],value = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],value = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],value = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],value = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],value = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],value = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500],value = 150) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500],value = 150) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 7) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 7) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29],value = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29],value = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25],value = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25],value = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],value = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],value = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 4) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 4) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],value = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],value = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],value = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],value = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],value = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],value = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],value = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],value = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],value = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],value = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 7) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 7) == 26: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0, 1, 2, 3, 4, 5],value = 1) == 6
    assert candidate(nums = [0, 0, 0, 0],value = 3) == 1
    assert candidate(nums = [10, 15, 20, 25, 30],value = 5) == 1
    assert candidate(nums = [-1, -2, -3, -4],value = 2) == 4
    assert candidate(nums = [-5, -10, -15, -20, -25],value = 5) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5],value = 3) == 3
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1000000000) == 1
    assert candidate(nums = [10, 20, 30, 40],value = 10) == 1
    assert candidate(nums = [1, -10, 7, 13, 6, 8],value = 7) == 2
    assert candidate(nums = [1, -10, 7, 13, 6, 8],value = 5) == 4
    assert candidate(nums = [-5, -4, -3, -2, -1],value = 3) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],value = 2) == 10
    assert candidate(nums = [100, 200, 300, 400, 500],value = 3) == 3
    assert candidate(nums = [-5, -4, -3, -2, -1],value = 2) == 4
    assert candidate(nums = [1, 1, 1, 1, 1],value = 1) == 5
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1000000000) == 1
    assert candidate(nums = [10, 20, 30, 40, 50],value = 10) == 1
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000],value = 1) == 4
    assert candidate(nums = [2, 3, 4, 5, 6],value = 3) == 4
    assert candidate(nums = [0, 1, 2, 3, 4, 5],value = 6) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 13) == 13
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150],value = 20) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 5) == 1
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],value = 1) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],value = 2) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 2) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],value = 25) == 1
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91],value = 5) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 16) == 16
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 7) == 31
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],value = 100) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7],value = 3) == 6
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],value = 100000) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 1) == 20
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 30
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],value = 10) == 1
    assert candidate(nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],value = 3) == 9
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100],value = 10) == 2
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],value = 3) == 18
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],value = 10) == 1
    assert candidate(nums = [1000000000, -1000000000, 2000000000, -2000000000, 0],value = 1000000000) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],value = 3) == 30
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 2) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 3) == 18
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100],value = 10) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],value = 7) == 15
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0],value = 1) == 7
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 10) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 1) == 31
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 7) == 26
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 5) == 1
    assert candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 120, 131, 142, 153, 164, 175, 186, 197, 208, 219],value = 11) == 0
    assert candidate(nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81],value = 5) == 2
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],value = 1) == 10
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 12) == 24
    assert candidate(nums = [10, 20, 30, 40, 50, 60],value = 15) == 1
    assert candidate(nums = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109],value = 11) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],value = 2) == 0
    assert candidate(nums = [-1000000000, -999999999, -999999998, -999999997, -999999996],value = 5) == 5
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],value = 1000) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 11) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],value = 5) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],value = 5) == 10
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 20
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 5) == 20
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],value = 2) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 1) == 10
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],value = 1000000000) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],value = 3) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 10) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 5) == 30
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],value = 1) == 10
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 5) == 1
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81],value = 4) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],value = 4) == 16
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],value = 2) == 10
    assert candidate(nums = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19],value = 3) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],value = 5) == 30
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],value = 3) == 9
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],value = 2) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 19) == 19
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27],value = 3) == 1
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],value = 1000000000) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],value = 1) == 11
    assert candidate(nums = [1000000000, -1000000000, 500000000, -500000000, 0],value = 100000000) == 1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],value = 5) == 10
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],value = 10) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 10) == 20
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],value = 2) == 1
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 3) == 9
    assert candidate(nums = [1000000000, 999999999, 999999998, 999999997, 999999996],value = 5) == 5
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 16
    assert candidate(nums = [1, 1, 1, 1, 1],value = 2) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 4) == 20
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],value = 1000000000) == 1
    assert candidate(nums = [-100, -50, -25, -10, -5, -1, 0, 1, 5, 10, 25, 50, 100],value = 25) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],value = 3) == 15
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],value = 1) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],value = 2) == 0
    assert candidate(nums = [-1000000000, -2000000000, -3000000000, -4000000000, -5000000000],value = 1000000000) == 1
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],value = 1000000) == 1
    assert candidate(nums = [-1, -1, -2, -2, -3, -3, -4, -4, -5, -5],value = 3) == 6
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],value = 1) == 10
    assert candidate(nums = [-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000],value = 100) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20],value = 5) == 20
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],value = 6) == 6
    assert candidate(nums = [-100, -200, -300, -400, -500],value = 150) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],value = 7) == 14
    assert candidate(nums = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29],value = 3) == 0
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25],value = 4) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],value = 5) == 1
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],value = 3) == 20
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],value = 4) == 21
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],value = 15) == 1
    assert candidate(nums = [1000000000, 1000000001, 1000000002, 1000000003, 1000000004],value = 1) == 5
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15],value = 5) == 15
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],value = 5) == 1
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],value = 6) == 0
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],value = 1000000000) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],value = 1) == 10
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],value = 7) == 26


