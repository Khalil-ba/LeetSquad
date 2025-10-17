def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(height = [1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(height = [4, 3, 2, 1, 4]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [4, 3, 2, 1, 4]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(height = [8, 10, 14, 0, 13, 10, 9, 9, 8, 9]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [8, 10, 14, 0, 13, 10, 9, 9, 8, 9]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 3, 4, 5, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 3, 4, 5, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 3, 10, 5, 7, 8, 9]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 3, 10, 5, 7, 8, 9]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 4, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 4, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 2, 5, 25, 24, 5]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 2, 5, 25, 24, 5]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1]) == 220000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1]) == 220000: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 8, 6, 2, 5, 4, 8, 3, 7, 9, 10, 11, 10, 9, 7, 3, 8, 4, 5, 2, 6, 8, 5, 3, 7, 9, 1, 4, 6, 8]) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 8, 6, 2, 5, 4, 8, 3, 7, 9, 10, 11, 10, 9, 7, 3, 8, 4, 5, 2, 6, 8, 5, 3, 7, 9, 1, 4, 6, 8]) == 224: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 160: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(height = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 300000: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 2, 5, 25, 24, 5, 2, 3, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 2, 5, 25, 24, 5, 2, 3, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(height = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]) == 45000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]) == 45000: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 1, 5, 6, 2, 3, 1, 4, 5, 1, 5, 6, 2, 3, 1, 4, 5, 1]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 1, 5, 6, 2, 3, 1, 4, 5, 1, 5, 6, 2, 3, 1, 4, 5, 1]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(height = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 25000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 25000: {e}')
    
    total += 1
    try:
        result = candidate(height = [10000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(height = [1000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 3, 10, 5, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 3, 10, 5, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(height = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986]) == 139804
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986]) == 139804: {e}')
    
    total += 1
    try:
        result = candidate(height = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 19000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 19000: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(height = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 19000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 19000: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(height = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60]) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60]) == 950: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 12, 4, 3, 2, 1, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 12, 4, 3, 2, 1, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 176: {e}')
    
    total += 1
    try:
        result = candidate(height = [3, 9, 3, 4, 7, 2, 12, 6, 5, 10, 1, 8]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [3, 9, 3, 4, 7, 2, 12, 6, 5, 10, 1, 8]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 10, 8, 3, 7, 6, 10, 4, 1, 9]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 10, 8, 3, 7, 6, 10, 4, 1, 9]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(height = [100, 200, 300, 400, 300, 200, 100, 200, 300, 400, 300, 200, 100]) == 2400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [100, 200, 300, 400, 300, 200, 100, 200, 300, 400, 300, 200, 100]) == 2400: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 12, 11]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 12, 11]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 18, 16, 14, 12, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 18, 16, 14, 12, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(height = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(height = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 24000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 24000: {e}')
    
    total += 1
    try:
        result = candidate(height = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 1539
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 1539: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(height = [9985, 9984, 9983, 9982, 9981, 9980, 9979, 9978, 9977, 9976, 9975, 9974, 9973, 9972, 9971]) == 139594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [9985, 9984, 9983, 9982, 9981, 9980, 9979, 9978, 9977, 9976, 9975, 9974, 9973, 9972, 9971]) == 139594: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(height = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(height = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 25, 7]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 25, 7]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(height = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000]) == 240000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000]) == 240000: {e}')
    
    total += 1
    try:
        result = candidate(height = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(height = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 5, 4, 3, 2, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 5, 4, 3, 2, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(height = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 100, 1, 1, 1]) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 100, 1, 1, 1]) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 15, 5, 4, 3, 2, 1, 15, 1, 2, 3, 4, 5, 15, 5, 4, 3, 2, 1]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 15, 5, 4, 3, 2, 1, 15, 1, 2, 3, 4, 5, 15, 5, 4, 3, 2, 1]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 3, 8, 4, 2, 7, 9, 6, 1]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 3, 8, 4, 2, 7, 9, 6, 1]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(height = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(height = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 170: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(height = [8, 10, 12, 10, 6, 5, 4, 3, 2, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [8, 10, 12, 10, 6, 5, 4, 3, 2, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 2, 15, 1, 5, 3]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 2, 15, 1, 5, 3]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(height = [100, 20, 300, 40, 500, 60, 700, 80, 900, 1000, 100, 900, 80, 700, 60, 500, 40, 300, 20, 100]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [100, 20, 300, 40, 500, 60, 700, 80, 900, 1000, 100, 900, 80, 700, 60, 500, 40, 300, 20, 100]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(height = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(height = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 10, 11, 12, 13, 14]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 10, 11, 12, 13, 14]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(height = [100, 50, 30, 60, 100, 40, 20, 80, 70, 90, 10]) == 810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [100, 50, 30, 60, 100, 40, 20, 80, 70, 90, 10]) == 810: {e}')
    
    total += 1
    try:
        result = candidate(height = [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(height = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(height = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(height = [1, 1]) == 1
    assert candidate(height = [4, 3, 2, 1, 4]) == 16
    assert candidate(height = [8, 10, 14, 0, 13, 10, 9, 9, 8, 9]) == 72
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert candidate(height = [2, 3, 4, 5, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 81
    assert candidate(height = [2, 3, 10, 5, 7, 8, 9]) == 36
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(height = [1, 2, 4, 3]) == 4
    assert candidate(height = [1, 2, 3, 4, 5]) == 6
    assert candidate(height = [1, 3, 2, 5, 25, 24, 5]) == 24
    assert candidate(height = [1, 2, 1]) == 2
    assert candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 25
    assert candidate(height = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1]) == 220000
    assert candidate(height = [5, 8, 6, 2, 5, 4, 8, 3, 7, 9, 10, 11, 10, 9, 7, 3, 8, 4, 5, 2, 6, 8, 5, 3, 7, 9, 1, 4, 6, 8]) == 224
    assert candidate(height = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 160
    assert candidate(height = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 180
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 120
    assert candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200
    assert candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 56
    assert candidate(height = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == 50
    assert candidate(height = [5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5]) == 128
    assert candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 19
    assert candidate(height = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]) == 300000
    assert candidate(height = [1, 3, 2, 5, 25, 24, 5, 2, 3, 1]) == 24
    assert candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 190
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50
    assert candidate(height = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]) == 45000
    assert candidate(height = [2, 1, 5, 6, 2, 3, 1, 4, 5, 1, 5, 6, 2, 3, 1, 4, 5, 1]) == 70
    assert candidate(height = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 25000
    assert candidate(height = [10000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 25
    assert candidate(height = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 90
    assert candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 180
    assert candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 120
    assert candidate(height = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]) == 66
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(height = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 2000
    assert candidate(height = [1000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29
    assert candidate(height = [2, 3, 10, 5, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 240
    assert candidate(height = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 90
    assert candidate(height = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986]) == 139804
    assert candidate(height = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 19000
    assert candidate(height = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(height = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 19000
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 400
    assert candidate(height = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60]) == 950
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 12, 4, 3, 2, 1, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 176
    assert candidate(height = [3, 9, 3, 4, 7, 2, 12, 6, 5, 10, 1, 8]) == 80
    assert candidate(height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 180
    assert candidate(height = [5, 10, 8, 3, 7, 6, 10, 4, 1, 9]) == 72
    assert candidate(height = [100, 200, 300, 400, 300, 200, 100, 200, 300, 400, 300, 200, 100]) == 2400
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 12, 11]) == 80
    assert candidate(height = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]) == 36
    assert candidate(height = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 18, 16, 14, 12, 10]) == 100
    assert candidate(height = [1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 56
    assert candidate(height = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(height = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 500
    assert candidate(height = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 24000
    assert candidate(height = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 1539
    assert candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000]) == 29
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 50
    assert candidate(height = [9985, 9984, 9983, 9982, 9981, 9980, 9979, 9978, 9977, 9976, 9975, 9974, 9973, 9972, 9971]) == 139594
    assert candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 70
    assert candidate(height = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 250
    assert candidate(height = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 56
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 450
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 25, 7]) == 49
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 136
    assert candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 80
    assert candidate(height = [10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000]) == 240000
    assert candidate(height = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000]) == 5000
    assert candidate(height = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000]) == 50000
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 180
    assert candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 95
    assert candidate(height = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 120
    assert candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10000]) == 25
    assert candidate(height = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 5, 4, 3, 2, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1]) == 75
    assert candidate(height = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 16
    assert candidate(height = [1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 100, 1, 1, 1, 1, 1, 100, 1, 1, 1]) == 1200
    assert candidate(height = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 48
    assert candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 190
    assert candidate(height = [10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10, 9, 8, 10]) == 180
    assert candidate(height = [1, 2, 3, 4, 5, 15, 5, 4, 3, 2, 1, 15, 1, 2, 3, 4, 5, 15, 5, 4, 3, 2, 1]) == 180
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 50
    assert candidate(height = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 36
    assert candidate(height = [5, 3, 8, 4, 2, 7, 9, 6, 1]) == 35
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 112
    assert candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 120
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
    assert candidate(height = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 45
    assert candidate(height = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 140
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 100
    assert candidate(height = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
    assert candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 14
    assert candidate(height = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]) == 170
    assert candidate(height = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == 48
    assert candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 90
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 200
    assert candidate(height = [8, 10, 12, 10, 6, 5, 4, 3, 2, 1]) == 25
    assert candidate(height = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 55
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 2, 15, 1, 5, 3]) == 80
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == 180
    assert candidate(height = [100, 20, 300, 40, 500, 60, 700, 80, 900, 1000, 100, 900, 80, 700, 60, 500, 40, 300, 20, 100]) == 5500
    assert candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 44
    assert candidate(height = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 800
    assert candidate(height = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 190
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 200
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 10, 11, 12, 13, 14]) == 104
    assert candidate(height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 29
    assert candidate(height = [1, 3, 5, 7, 9, 11, 13, 15, 13, 11, 9, 7, 5, 3, 1]) == 56
    assert candidate(height = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56
    assert candidate(height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 144
    assert candidate(height = [1, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100, 2, 3, 100]) == 1500
    assert candidate(height = [100, 50, 30, 60, 100, 40, 20, 80, 70, 90, 10]) == 810
    assert candidate(height = [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7]) == 98
    assert candidate(height = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36


