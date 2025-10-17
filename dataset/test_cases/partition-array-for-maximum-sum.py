def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [1],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 45: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 15, 7, 9, 2, 5, 10],k = 3) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 15, 7, 9, 2, 5, 10],k = 3) == 84: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50],k = 3) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50],k = 3) == 190: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 1, 2, 3, 9],k = 3) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 1, 2, 3, 9],k = 3) == 45: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 5, 10, 15, 20],k = 2) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 5, 10, 15, 20],k = 2) == 66: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 1, 4, 7, 8, 5, 6, 9],k = 3) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 1, 4, 7, 8, 5, 6, 9],k = 3) == 62: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1],k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1],k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 58: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 54: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5],k = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5],k = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1],k = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1],k = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 60: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 75: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5],k = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5],k = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3],k = 4) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3],k = 4) == 83: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10],k = 9) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10],k = 9) == 90: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 1, 2, 4, 3],k = 2) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 1, 2, 4, 3],k = 2) == 19: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 75: {e}')
    
    total += 1
    try:
        result = candidate(arr = [4, 3, 2, 5, 6],k = 2) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [4, 3, 2, 5, 6],k = 2) == 24: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 6) == 143
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 6) == 143: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 75: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],k = 8) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],k = 8) == 180: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 5, 4, 2, 1, 9, 3, 7, 6, 10, 11, 13, 12, 14, 15, 17, 16, 18, 19, 20, 22, 21, 23, 24, 26, 25, 27, 28, 30, 29, 31, 32, 33, 35, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],k = 6) == 2007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 5, 4, 2, 1, 9, 3, 7, 6, 10, 11, 13, 12, 14, 15, 17, 16, 18, 19, 20, 22, 21, 23, 24, 26, 25, 27, 28, 30, 29, 31, 32, 33, 35, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],k = 6) == 2007: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 7) == 1422
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 7) == 1422: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 229: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 7500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 7500: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 1, 5, 7, 3, 6, 4, 8, 2, 10],k = 2) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 1, 5, 7, 3, 6, 4, 8, 2, 10],k = 2) == 80: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 1, 5, 3, 6, 4, 2, 9, 8, 11, 10, 12],k = 6) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 1, 5, 3, 6, 4, 2, 9, 8, 11, 10, 12],k = 6) == 118: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 49: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3, 9],k = 4) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3, 9],k = 4) == 117: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 2) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 2) == 58: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [7, 3, 6, 1, 4, 9, 2, 8, 5, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],k = 7) == 835
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [7, 3, 6, 1, 4, 9, 2, 8, 5, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],k = 7) == 835: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 1, 5, 2, 2, 2, 2, 2, 5],k = 4) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 1, 5, 2, 2, 2, 2, 2, 5],k = 4) == 50: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 1, 2, 3, 9, 3, 2, 4, 5, 6],k = 3) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 1, 2, 3, 9, 3, 2, 4, 5, 6],k = 3) == 75: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1],k = 3) == 334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1],k = 3) == 334: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 7) == 6700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 7) == 6700: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 139: {e}')
    
    total += 1
    try:
        result = candidate(arr = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2],k = 3) == 458
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2],k = 3) == 458: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 1) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 1) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 240: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 423
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 423: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 25) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 25) == 300: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 999999999, 888888888, 777777777, 666666666],k = 2) == 4555555552
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 999999999, 888888888, 777777777, 666666666],k = 2) == 4555555552: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 150: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 2) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 2) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 160: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 5) == 1375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 5) == 1375: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6],k = 3) == 4800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6],k = 3) == 4800: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 2) == 1270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 2) == 1270: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 15) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 15) == 900: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 150: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 7, 9, 2, 6, 1, 8, 4, 10, 11, 12, 13, 14, 15],k = 5) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 7, 9, 2, 6, 1, 8, 4, 10, 11, 12, 13, 14, 15],k = 5) == 170: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991],k = 10) == 10000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991],k = 10) == 10000000000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 2) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 2) == 480: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 120: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 300: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 1, 2, 3, 9, 1, 4, 5, 1, 6, 7, 8, 1, 9],k = 4) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 1, 2, 3, 9, 1, 4, 5, 1, 6, 7, 8, 1, 9],k = 4) == 122: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 130: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 7) == 881
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 7) == 881: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 2) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 2) == 50: {e}')
    
    total += 1
    try:
        result = candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 192: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 100, 1, 1, 100, 1, 1, 100, 1, 1],k = 3) == 910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 100, 1, 1, 100, 1, 1, 100, 1, 1],k = 3) == 910: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1],k = 4) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1],k = 4) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 68: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 3) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 3) == 54: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 2, 7, 1, 8, 3, 6, 4, 9, 10, 11, 12, 13, 14, 15],k = 8) == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 2, 7, 1, 8, 3, 6, 4, 9, 10, 11, 12, 13, 14, 15],k = 8) == 176: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 49: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 2) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 2) == 200: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 300: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 675: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 502
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 502: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 162: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 15) == 1320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 15) == 1320: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 10) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 10) == 150: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 750: {e}')
    
    total += 1
    try:
        result = candidate(arr = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 150],k = 6) == 1590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 150],k = 6) == 1590: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 4) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 4) == 480: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 2) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 2) == 90: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 3, 4, 6, 2, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29],k = 6) == 563
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 3, 4, 6, 2, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29],k = 6) == 563: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 250: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 25) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 25) == 300: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 6, 1, 2, 8, 7, 3, 4, 5, 6, 7, 8, 9],k = 5) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 6, 1, 2, 8, 7, 3, 4, 5, 6, 7, 8, 9],k = 5) == 106: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 200: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],k = 2) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],k = 2) == 180: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 420: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 175: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 4) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 4) == 147: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 250: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 111: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 4) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 4) == 135: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 229: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5],k = 3) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5],k = 3) == 89: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [1],k = 1) == 1
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 45
    assert candidate(arr = [1, 15, 7, 9, 2, 5, 10],k = 3) == 84
    assert candidate(arr = [10, 20, 30, 40, 50],k = 3) == 190
    assert candidate(arr = [9, 1, 2, 3, 9],k = 3) == 45
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 1) == 55
    assert candidate(arr = [2, 3, 5, 10, 15, 20],k = 2) == 66
    assert candidate(arr = [3, 2, 1, 4, 7, 8, 5, 6, 9],k = 3) == 62
    assert candidate(arr = [5, 4, 3, 2, 1],k = 1) == 15
    assert candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 58
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 50
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3) == 54
    assert candidate(arr = [5, 5, 5, 5, 5],k = 5) == 25
    assert candidate(arr = [5, 4, 3, 2, 1],k = 5) == 25
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 60
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 10
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 75
    assert candidate(arr = [1, 2, 3, 4, 5],k = 3) == 19
    assert candidate(arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3],k = 4) == 83
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 100
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10],k = 9) == 90
    assert candidate(arr = [2, 3, 1, 2, 4, 3],k = 2) == 19
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 75
    assert candidate(arr = [4, 3, 2, 5, 6],k = 2) == 24
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 6) == 143
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 75
    assert candidate(arr = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],k = 8) == 180
    assert candidate(arr = [8, 5, 4, 2, 1, 9, 3, 7, 6, 10, 11, 13, 12, 14, 15, 17, 16, 18, 19, 20, 22, 21, 23, 24, 26, 25, 27, 28, 30, 29, 31, 32, 33, 35, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],k = 6) == 2007
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 7) == 1422
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 229
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 7500
    assert candidate(arr = [9, 1, 5, 7, 3, 6, 4, 8, 2, 10],k = 2) == 80
    assert candidate(arr = [7, 1, 5, 3, 6, 4, 2, 9, 8, 11, 10, 12],k = 6) == 118
    assert candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 49
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 20
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 55
    assert candidate(arr = [9, 1, 2, 3, 9, 1, 2, 3, 9, 1, 2, 3, 9],k = 4) == 117
    assert candidate(arr = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1],k = 2) == 58
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 20) == 20
    assert candidate(arr = [7, 3, 6, 1, 4, 9, 2, 8, 5, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],k = 7) == 835
    assert candidate(arr = [5, 1, 1, 5, 2, 2, 2, 2, 2, 5],k = 4) == 50
    assert candidate(arr = [9, 1, 2, 3, 9, 3, 2, 4, 5, 6],k = 3) == 75
    assert candidate(arr = [5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1, 4, 1, 5, 1],k = 3) == 334
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 7) == 6700
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 139
    assert candidate(arr = [40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2],k = 3) == 458
    assert candidate(arr = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 1) == 2000
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 4) == 240
    assert candidate(arr = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 7) == 423
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 25) == 300
    assert candidate(arr = [1000000000, 999999999, 888888888, 777777777, 666666666],k = 2) == 4555555552
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 150
    assert candidate(arr = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],k = 2) == 1050
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 160
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 5) == 1375
    assert candidate(arr = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5, 600, 6],k = 3) == 4800
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 2) == 1270
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 15
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 15) == 900
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 4) == 20
    assert candidate(arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 150
    assert candidate(arr = [5, 3, 7, 9, 2, 6, 1, 8, 4, 10, 11, 12, 13, 14, 15],k = 5) == 170
    assert candidate(arr = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991],k = 10) == 10000000000
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 2) == 480
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1) == 120
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 300
    assert candidate(arr = [9, 1, 2, 3, 9, 1, 4, 5, 1, 6, 7, 8, 1, 9],k = 4) == 122
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 5) == 130
    assert candidate(arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9],k = 7) == 881
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 2) == 50
    assert candidate(arr = [8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 192
    assert candidate(arr = [5, 1, 100, 1, 1, 100, 1, 1, 100, 1, 1],k = 3) == 910
    assert candidate(arr = [5, 4, 3, 2, 1],k = 4) == 21
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 68
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 3) == 54
    assert candidate(arr = [5, 2, 7, 1, 8, 3, 6, 4, 9, 10, 11, 12, 13, 14, 15],k = 8) == 176
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 20
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 2) == 49
    assert candidate(arr = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],k = 2) == 200
    assert candidate(arr = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 300
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 15) == 675
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 4) == 502
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 162
    assert candidate(arr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 10) == 10000
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],k = 15) == 1320
    assert candidate(arr = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10],k = 10) == 150
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 750
    assert candidate(arr = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 150],k = 6) == 1590
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],k = 4) == 480
    assert candidate(arr = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 2) == 90
    assert candidate(arr = [5, 1, 3, 4, 6, 2, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29],k = 6) == 563
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 5) == 250
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 25) == 300
    assert candidate(arr = [5, 6, 1, 2, 8, 7, 3, 4, 5, 6, 7, 8, 9],k = 5) == 106
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 5) == 200
    assert candidate(arr = [1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9],k = 2) == 180
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 2) == 420
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 10) == 175
    assert candidate(arr = [5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 4) == 147
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 250
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 50) == 111
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 4) == 135
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 3) == 229
    assert candidate(arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5],k = 3) == 89


