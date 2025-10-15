def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 0, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 0, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 100, -100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 100, -100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 0, 2, -3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 0, 2, -3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -10, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -10, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -12.5, 6.25]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -12.5, 6.25]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, 0, -1, 1, 0, -1, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, 0, -1, 1, 0, -1, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 0, 60, 70, 80, 90]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 0, 60, 70, 80, 90]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-50, 50, -50, 50, -50, 50, -50, 50, -50, 50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-50, 50, -50, 50, -50, 50, -50, 50, -50, 50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, -10, 4, -2, 0.5, 0.2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, -10, 4, -2, 0.5, 0.2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 0, 100, -100, 100, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 0, 100, -100, 100, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, -99, 100, -100, 101, -101]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, -99, 100, -100, 101, -101]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -10, 100, -1000, 10000, -100000, 1000000, -10000000, 100000000, -1000000000]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -10, 100, -1000, 10000, -100000, 1000000, -10000000, 100000000, -1000000000]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 100, -100, 1000, -1000, 10000, -10000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 100, -100, 1000, -1000, 10000, -10000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -12.5, 0.5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -12.5, 0.5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50, 25, -25]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50, 25, -25]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3, 4, 0, -4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3, 4, 0, -4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 0, 25, -10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 0, 25, -10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, -96, -95, -94]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, -96, -95, -94]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10, -10, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10, -10, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 20, -10, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 20, -10, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -16]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -16]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, -400, -500, 600, -700, 800, -900, 1000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, -400, -500, 600, -700, 800, -900, 1000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1, 2, 3, 4, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1, 2, 3, 4, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 100, -100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 100, -100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 100, -10, 10, -1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 100, -10, 10, -1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, -200, -300, -400, -500, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, -200, -300, -400, -500, 1]) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-1]) == -1
    assert candidate(nums = [1]) == 1
    assert candidate(nums = [0, 0, 0]) == 0
    assert candidate(nums = [-99, -98, -97, -96, -95, -94, -93, -92, -91, -90]) == 1
    assert candidate(nums = [100, -100, 100]) == -1
    assert candidate(nums = [0]) == 0
    assert candidate(nums = [100, -100, 1]) == -1
    assert candidate(nums = [-100, 0, 100]) == 0
    assert candidate(nums = [-1, -2, -3, -4, 3, 2, 1]) == 1
    assert candidate(nums = [100, -100, 100, -100]) == 1
    assert candidate(nums = [-1, -2, -3, -4]) == 1
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [-1, 1, -1, 1, -1]) == -1
    assert candidate(nums = [1, 5, 0, 2, -3]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5]) == 1
    assert candidate(nums = [-1, -2, -3]) == -1
    assert candidate(nums = [-1, 0, 1, -1, 0, 1, -1, 0, 1]) == 0
    assert candidate(nums = [100, -50, 25, -10, 5]) == 1
    assert candidate(nums = [100, -50, 25, -12.5, 6.25]) == 1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1
    assert candidate(nums = [0, 1, -1, 2, -2, 3, -3]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
    assert candidate(nums = [-1, 1, 0, -1, 1, 0, -1, 1, 0]) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [10, -10, 20, -20, 30, -30]) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 0, 60, 70, 80, 90]) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, -1]) == -1
    assert candidate(nums = [1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1]) == 0
    assert candidate(nums = [-50, 50, -50, 50, -50, 50, -50, 50, -50, 50]) == -1
    assert candidate(nums = [50, 25, -10, 4, -2, 0.5, 0.2]) == 1
    assert candidate(nums = [-100, 0, 100, -100, 100, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]) == -1
    assert candidate(nums = [-1, -1, -1, -1, -1]) == -1
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == 1
    assert candidate(nums = [0, 0, 0, 0]) == 0
    assert candidate(nums = [-100, -99, -98, -97, -96, -95, -94, -93, -92, -91, -90, -89, -88, -87, -86, -85, -84, -83, -82, -81, -80, -79, -78, -77, -76, -75, -74, -73, -72, -71, -70, -69, -68, -67, -66, -65, -64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == 0
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1]) == -1
    assert candidate(nums = [99, -99, 100, -100, 101, -101]) == -1
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]) == 0
    assert candidate(nums = [1, -10, 100, -1000, 10000, -100000, 1000000, -10000000, 100000000, -1000000000]) == -1
    assert candidate(nums = [0, 1, 2, 3]) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == -1
    assert candidate(nums = [10, -10, 100, -100, 1000, -1000, 10000, -10000]) == 1
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(nums = [0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [1, -1, 2, -2, 3, -3]) == -1
    assert candidate(nums = [100, -50, 25, -12.5, 0.5]) == 1
    assert candidate(nums = [-1, 0, 1, 0, -1, 0, 1, 0, -1, 0]) == 0
    assert candidate(nums = [100, -100, 50, -50, 25, -25]) == -1
    assert candidate(nums = [100, -100, 50, -50, 25, -25, 12, -12, 6, -6]) == -1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 1
    assert candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3, 4, 0, -4]) == 0
    assert candidate(nums = [100, -50, 0, 25, -10]) == 0
    assert candidate(nums = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1
    assert candidate(nums = [99, 98, 97, -96, -95, -94]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 0]) == 0
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == 1
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 1
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(nums = [99, -99, 98, -98, 97, -97, 96, -96, 95, -95]) == -1
    assert candidate(nums = [-10, 10, -10, 10]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10]) == 0
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == 1
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, -1]) == -1
    assert candidate(nums = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]) == -1
    assert candidate(nums = [-10, -20, -30, -40, -50]) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == 0
    assert candidate(nums = [100, -50, 20, -10, 5]) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -16]) == -1
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 1
    assert candidate(nums = [100, 200, 300, -400, -500, 600, -700, 800, -900, 1000]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1]) == 1
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == -1
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80]) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(nums = [-1, 0, 1, 2, 3, 4, 5]) == 0
    assert candidate(nums = [100, -100, 100, -100, 100]) == 1
    assert candidate(nums = [1, -1, 1, -1, 1, -1]) == -1
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == -1
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == -1
    assert candidate(nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0]) == 0
    assert candidate(nums = [100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100]) == 1
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100]) == 1
    assert candidate(nums = [-100, 100, -10, 10, -1, 1]) == -1
    assert candidate(nums = [-100, -200, -300, -400, -500, 1]) == -1


