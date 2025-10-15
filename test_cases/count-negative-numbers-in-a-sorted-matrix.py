def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1], [-1, -1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1], [-1, -1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-3], [-2], [-1], [0], [1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-3], [-2], [-1], [0], [1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1], [-5, -5, -5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1], [-5, -5, -5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 2], [1, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 2], [1, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1], [-1, -1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1], [-1, -1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 2, 1], [4, 3, 1], [3, 2, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 2, 1], [4, 3, 1], [3, 2, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3], [4, 5, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3], [4, 5, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[100, 90, 80, -10], [-9, -8, -7, -6], [-5, -4, -3, -2], [-4, -3, -2, -1]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[100, 90, 80, -10], [-9, -8, -7, -6], [-5, -4, -3, -2], [-4, -3, -2, -1]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3], [0, -1, -2], [-3, -4, -5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3], [0, -1, -2], [-3, -4, -5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, 0, -1], [2, 1, 0, -1, -2], [1, 0, -1, -2, -3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, 0, -1], [2, 1, 0, -1, -2], [1, 0, -1, -2, -3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0], [0, -1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0], [0, -1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, -1, 0, 0, 0], [-1, -1, -1, 0, 0], [-1, -1, -1, -1, 0]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, -1, 0, 0, 0], [-1, -1, -1, 0, 0], [-1, -1, -1, -1, 0]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, -1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, -1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[50, 40, 30, 20, 10, 0, -10, -20], [-5, -10, -15, -20, -25, -30, -35, -40], [-50, -60, -70, -80, -90, -100, -110, -120]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[50, 40, 30, 20, 10, 0, -10, -20], [-5, -10, -15, -20, -25, -30, -35, -40], [-50, -60, -70, -80, -90, -100, -110, -120]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0, -1], [7, 6, 5, 4, 3, 2, 1, 0, -1, -2], [6, 5, 4, 3, 2, 1, 0, -1, -2, -3], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -6], [2, 1, 0, -1, -2, -3, -4, -5, -6, -7], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0, -1], [7, 6, 5, 4, 3, 2, 1, 0, -1, -2], [6, 5, 4, 3, 2, 1, 0, -1, -2, -3], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -6], [2, 1, 0, -1, -2, -3, -4, -5, -6, -7], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-99, -98, -97, -96, -95, -94, -93, -92, -91, -90], [-89, -88, -87, -86, -85, -84, -83, -82, -81, -80], [-79, -78, -77, -76, -75, -74, -73, -72, -71, -70], [-69, -68, -67, -66, -65, -64, -63, -62, -61, -60], [-59, -58, -57, -56, -55, -54, -53, -52, -51, -50], [-49, -48, -47, -46, -45, -44, -43, -42, -41, -40], [-39, -38, -37, -36, -35, -34, -33, -32, -31, -30], [-29, -28, -27, -26, -25, -24, -23, -22, -21, -20], [-19, -18, -17, -16, -15, -14, -13, -12, -11, -10], [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-99, -98, -97, -96, -95, -94, -93, -92, -91, -90], [-89, -88, -87, -86, -85, -84, -83, -82, -81, -80], [-79, -78, -77, -76, -75, -74, -73, -72, -71, -70], [-69, -68, -67, -66, -65, -64, -63, -62, -61, -60], [-59, -58, -57, -56, -55, -54, -53, -52, -51, -50], [-49, -48, -47, -46, -45, -44, -43, -42, -41, -40], [-39, -38, -37, -36, -35, -34, -33, -32, -31, -30], [-29, -28, -27, -26, -25, -24, -23, -22, -21, -20], [-19, -18, -17, -16, -15, -14, -13, -12, -11, -10], [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 1, -1, 1, -1, 1, -1, 1, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2], [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 1, -1, 1, -1, 1, -1, 1, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2], [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1, -1, -1, -1], [1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1, -1, -1, -1], [1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, -9, 8, -8], [7, -7, 6, -6], [5, -5, 4, -4], [3, -3, 2, -2], [1, -1, 0, -1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, -9, 8, -8], [7, -7, 6, -6], [5, -5, 4, -4], [3, -3, 2, -2], [1, -1, 0, -1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[99, 98, 97, 96, 95, 94], [93, 92, 91, 90, -1, -2], [-3, -4, -5, -6, -7, -8], [-9, -10, -11, -12, -13, -14]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[99, 98, 97, 96, 95, 94], [93, 92, 91, 90, -1, -2], [-3, -4, -5, -6, -7, -8], [-9, -10, -11, -12, -13, -14]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, -10, 20, -20, 30, -30], [9, -9, 18, -18, 27, -27], [8, -8, 16, -16, 24, -24], [7, -7, 14, -14, 21, -21]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, -10, 20, -20, 30, -30], [9, -9, 18, -18, 27, -27], [8, -8, 16, -16, 24, -24], [7, -7, 14, -14, 21, -21]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, -1], [0, 0, -1, -1, -1], [0, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, -1], [0, 0, -1, -1, -1], [0, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-5, -4, -3, -2, -1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-5, -4, -3, -2, -1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, 0, -1], [0, -1, 0, -1, 0], [-1, 0, -1, 0, -1], [0, -1, 0, -1, 0], [-1, 0, -1, 0, -1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, 0, -1], [0, -1, 0, -1, 0], [-1, 0, -1, 0, -1], [0, -1, 0, -1, 0], [-1, 0, -1, 0, -1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-50, -40, -30, -20, -10], [30, 20, 10, 0, -10], [-20, -10, 0, 10, 20], [10, 0, 10, 20, 30], [0, 10, 20, 30, 40]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-50, -40, -30, -20, -10], [30, 20, 10, 0, -10], [-20, -10, 0, 10, 20], [10, 0, 10, 20, 30], [0, 10, 20, 30, 40]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[90, 80, 70, 60, 50, 40, 30, 20, 10, 0], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[90, 80, 70, 60, 50, 40, 30, 20, 10, 0], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-5, -4, -3, -2, -1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-5, -4, -3, -2, -1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1, 0], [1, 0, -1, -1], [1, -1, -1, -1], [-1, -1, -1, -1]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1, 0], [1, 0, -1, -1], [1, -1, -1, -1], [-1, -1, -1, -1]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-3, -2, -1, 0], [2, 1, 0, -1], [1, 0, -1, -2], [0, -1, -2, -3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-3, -2, -1, 0], [2, 1, 0, -1], [1, 0, -1, -2], [0, -1, -2, -3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, -5, 3, 2, -1], [-3, 0, -1, 0, -4], [-5, -6, -7, -8, -9]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, -5, 3, 2, -1], [-3, 0, -1, 0, -4], [-5, -6, -7, -8, -9]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0, -1], [7, 6, 5, 4, 3, 2, 1, 0, -1, -2], [6, 5, 4, 3, 2, 1, 0, -1, -2, -3], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -6], [2, 1, 0, -1, -2, -3, -4, -5, -6, -7], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0, -1], [7, 6, 5, 4, 3, 2, 1, 0, -1, -2], [6, 5, 4, 3, 2, 1, 0, -1, -2, -3], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -6], [2, 1, 0, -1, -2, -3, -4, -5, -6, -7], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-100, -99, -98, -97, -96], [0, 0, 0, -1, -2], [-3, -4, -5, -6, -7], [-8, -9, -10, -11, -12]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-100, -99, -98, -97, -96], [0, 0, 0, -1, -2], [-3, -4, -5, -6, -7], [-8, -9, -10, -11, -12]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, -2, -3], [-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, -2, -3], [-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-2, -3, -4, -5, -6, -7, -8, -9, -10, -11], [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-2, -3, -4, -5, -6, -7, -8, -9, -10, -11], [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, -1, -1], [0, 0, 0, 0, 0, 0, 0, -1, -1, -1], [0, 0, 0, 0, 0, 0, -1, -1, -1, -1], [0, 0, 0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 0, 0, -1, -1, -1, -1, -1, -1], [0, 0, 0, -1, -1, -1, -1, -1, -1, -1], [0, 0, -1, -1, -1, -1, -1, -1, -1, -1], [0, -1, -1, -1, -1, -1, -1, -1, -1, -1]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, -1, -1], [0, 0, 0, 0, 0, 0, 0, -1, -1, -1], [0, 0, 0, 0, 0, 0, -1, -1, -1, -1], [0, 0, 0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 0, 0, -1, -1, -1, -1, -1, -1], [0, 0, 0, -1, -1, -1, -1, -1, -1, -1], [0, 0, -1, -1, -1, -1, -1, -1, -1, -1], [0, -1, -1, -1, -1, -1, -1, -1, -1, -1]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0, 1, 2, 3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0, 1, 2, 3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, -10, 20, -20], [5, -5, 15, -15], [0, 0, 0, 0], [-1, -2, -3, -4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, -10, 20, -20], [5, -5, 15, -15], [0, 0, 0, 0], [-1, -2, -3, -4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [89, 88, 87, 86, 85, 84, 83, 82, 81, 80], [79, 78, 77, 76, 75, 74, 73, 72, 71, 70], [69, 68, 67, 66, 65, 64, 63, 62, 61, 60], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-11, -12, -13, -14, -15, -16, -17, -18, -19, -20], [-21, -22, -23, -24, -25, -26, -27, -28, -29, -30], [-31, -32, -33, -34, -35, -36, -37, -38, -39, -40], [-41, -42, -43, -44, -45, -46, -47, -48, -49, -50]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [89, 88, 87, 86, 85, 84, 83, 82, 81, 80], [79, 78, 77, 76, 75, 74, 73, 72, 71, 70], [69, 68, 67, 66, 65, 64, 63, 62, 61, 60], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-11, -12, -13, -14, -15, -16, -17, -18, -19, -20], [-21, -22, -23, -24, -25, -26, -27, -28, -29, -30], [-31, -32, -33, -34, -35, -36, -37, -38, -39, -40], [-41, -42, -43, -44, -45, -46, -47, -48, -49, -50]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 1, 0, -1, -2], [1, 0, -1, -2, -3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 1, 0, -1, -2], [1, 0, -1, -2, -3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[100, 90, 80, 70, 60, 50, 40, 30, 20, 10], [90, 80, 70, 60, 50, 40, 30, 20, 10, 0], [80, 70, 60, 50, 40, 30, 20, 10, 0, -10], [70, 60, 50, 40, 30, 20, 10, 0, -10, -20], [60, 50, 40, 30, 20, 10, 0, -10, -20, -30]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[100, 90, 80, 70, 60, 50, 40, 30, 20, 10], [90, 80, 70, 60, 50, 40, 30, 20, 10, 0], [80, 70, 60, 50, 40, 30, 20, 10, 0, -10], [70, 60, 50, 40, 30, 20, 10, 0, -10, -20], [60, 50, 40, 30, 20, 10, 0, -10, -20, -30]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, -1, -2], [2, 1, -2, -3, -4], [1, 0, -3, -4, -5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, -1, -2], [2, 1, -2, -3, -4], [1, 0, -3, -4, -5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[99, 98, 97, 96, 95], [-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -101, -102, -103, -104]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[99, 98, 97, 96, 95], [-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -101, -102, -103, -104]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, -5, -4, -3], [-7, -6, -5, -4], [-8, -7, -6, -5], [-9, -8, -7, -6]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, -5, -4, -3], [-7, -6, -5, -4], [-8, -7, -6, -5], [-9, -8, -7, -6]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[50, 40, 30, 20, 10], [45, 35, 25, 15, 5], [40, 30, 20, 10, 0], [35, 25, 15, 5, -5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[50, 40, 30, 20, 10], [45, 35, 25, 15, 5], [40, 30, 20, 10, 0], [35, 25, 15, 5, -5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6], [-3, -4, -5, -6, -7], [-4, -5, -6, -7, -8], [-5, -6, -7, -8, -9]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6], [-3, -4, -5, -6, -7], [-4, -5, -6, -7, -8], [-5, -6, -7, -8, -9]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, -1], [0, 0, 0, -1, -2], [0, 0, -1, -2, -3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, -1], [0, 0, 0, -1, -2], [0, 0, -1, -2, -3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-100, -99, -98, -97, -96, -95, -94, -93, -92, -91], [-90, -89, -88, -87, -86, -85, -84, -83, -82, -81], [-80, -79, -78, -77, -76, -75, -74, -73, -72, -71], [-70, -69, -68, -67, -66, -65, -64, -63, -62, -61], [-60, -59, -58, -57, -56, -55, -54, -53, -52, -51], [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41], [-40, -39, -38, -37, -36, -35, -34, -33, -32, -31], [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21], [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11], [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-100, -99, -98, -97, -96, -95, -94, -93, -92, -91], [-90, -89, -88, -87, -86, -85, -84, -83, -82, -81], [-80, -79, -78, -77, -76, -75, -74, -73, -72, -71], [-70, -69, -68, -67, -66, -65, -64, -63, -62, -61], [-60, -59, -58, -57, -56, -55, -54, -53, -52, -51], [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41], [-40, -39, -38, -37, -36, -35, -34, -33, -32, -31], [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21], [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11], [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-5, -4, -3, -2, -1], [-10, -9, -8, -7, -6], [-15, -14, -13, -12, -11], [-20, -19, -18, -17, -16], [-25, -24, -23, -22, -21]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-5, -4, -3, -2, -1], [-10, -9, -8, -7, -6], [-15, -14, -13, -12, -11], [-20, -19, -18, -17, -16], [-25, -24, -23, -22, -21]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0], [0, 0, -1, -2], [0, -1, -2, -3], [-1, -2, -3, -4]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0], [0, 0, -1, -2], [0, -1, -2, -3], [-1, -2, -3, -4]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0], [0, 0, 0, -1], [0, 0, -1, -1], [0, -1, -1, -1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0], [0, 0, 0, -1], [0, 0, -1, -1], [0, -1, -1, -1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[50, 40, 30, 20, 10], [45, 35, 25, 15, 5], [40, 30, 20, 10, 0], [35, 25, 15, 5, -5], [30, 20, 10, 0, -10]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[50, 40, 30, 20, 10], [45, 35, 25, 15, 5], [40, 30, 20, 10, 0], [35, 25, 15, 5, -5], [30, 20, 10, 0, -10]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 8, 6, 4, 2, 0, -2, -4], [-6, -8, -10, -12, -14, -16, -18, -20], [-10, -12, -14, -16, -18, -20, -22, -24]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 8, 6, 4, 2, 0, -2, -4], [-6, -8, -10, -12, -14, -16, -18, -20], [-10, -12, -14, -16, -18, -20, -22, -24]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-10, -20, -30, -40], [-20, -30, -40, -50], [-30, -40, -50, -60], [-40, -50, -60, -70]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-10, -20, -30, -40], [-20, -30, -40, -50], [-30, -40, -50, -60], [-40, -50, -60, -70]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-10, -20, -30, -40, -50, -60, -70, -80, -90], [-110, -120, -130, -140, -150, -160, -170, -180, -190], [-200, -210, -220, -230, -240, -250, -260, -270, -280]]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-10, -20, -30, -40, -50, -60, -70, -80, -90], [-110, -120, -130, -140, -150, -160, -170, -180, -190], [-200, -210, -220, -230, -240, -250, -260, -270, -280]]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-100, -99, -98, -97], [-96, -95, -94, -93], [-92, -91, -90, -89], [-88, -87, -86, -85]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-100, -99, -98, -97], [-96, -95, -94, -93], [-92, -91, -90, -89], [-88, -87, -86, -85]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 20, 30, 40, 50], [20, 30, 40, 50, 60], [30, 40, 50, 60, 70], [40, 50, 60, 70, 80], [50, 60, 70, 80, 90]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 20, 30, 40, 50], [20, 30, 40, 50, 60], [30, 40, 50, 60, 70], [40, 50, 60, 70, 80], [50, 60, 70, 80, 90]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-100, -99, -98, -97, -96, -95, -94, -93, -92, -91], [-90, -89, -88, -87, -86, -85, -84, -83, -82, -81], [-80, -79, -78, -77, -76, -75, -74, -73, -72, -71], [-70, -69, -68, -67, -66, -65, -64, -63, -62, -61]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-100, -99, -98, -97, -96, -95, -94, -93, -92, -91], [-90, -89, -88, -87, -86, -85, -84, -83, -82, -81], [-80, -79, -78, -77, -76, -75, -74, -73, -72, -71], [-70, -69, -68, -67, -66, -65, -64, -63, -62, -61]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-50, -49, -48, -47, -46, -45], [-44, -43, -42, -41, -40, -39], [-38, -37, -36, -35, -34, -33], [-32, -31, -30, -29, -28, -27]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-50, -49, -48, -47, -46, -45], [-44, -43, -42, -41, -40, -39], [-38, -37, -36, -35, -34, -33], [-32, -31, -30, -29, -28, -27]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-100, -99, -98], [-99, -98, -97], [-98, -97, -96], [-97, -96, -95]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-100, -99, -98], [-99, -98, -97], [-98, -97, -96], [-97, -96, -95]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 5, 0, -10, -20], [-5, -15, -20, -25, -30], [-1, -2, -3, -4, -5]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 5, 0, -10, -20], [-5, -15, -20, -25, -30], [-1, -2, -3, -4, -5]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 0], [1, -1, 0], [1, -1, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 0], [1, -1, 0], [1, -1, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1], [-1, -2, -3], [-2, -3, -4], [-3, -4, -5]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1], [-1, -2, -3], [-2, -3, -4], [-3, -4, -5]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 7, 5, 3, 1], [-1, -3, -5, -7, -9], [-2, -4, -6, -8, -10], [-3, -6, -9, -12, -15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 7, 5, 3, 1], [-1, -3, -5, -7, -9], [-2, -4, -6, -8, -10], [-3, -6, -9, -12, -15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [0, 0, -1], [0, -1, -2], [-1, -2, -3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [0, 0, -1], [0, -1, -2], [-1, -2, -3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, -1], [3, 2, 1, -1, -2], [2, 1, -1, -2, -3], [1, -1, -2, -3, -4]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, -1], [3, 2, 1, -1, -2], [2, 1, -1, -2, -3], [1, -1, -2, -3, -4]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, -1], [-1, 0, 1], [0, 1, -1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, -1], [-1, 0, 1], [0, 1, -1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, -1], [8, 7, 6, 5, 4, 3, 2, 1, -2, -3], [7, 6, 5, 4, 3, 2, 1, -3, -4, -5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, -1], [8, 7, 6, 5, 4, 3, 2, 1, -2, -3], [7, 6, 5, 4, 3, 2, 1, -3, -4, -5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, -1], [0, 0, 0, -1, -1, -2], [-1, -1, -2, -3, -4, -5]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, -1], [0, 0, 0, -1, -1, -2], [-1, -1, -2, -3, -4, -5]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-2, -1, 0, 1, 2], [3, 4, 5, 6, 7], [8, 9, 10, 11, 12], [-13, -14, -15, -16, -17], [-18, -19, -20, -21, -22]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-2, -1, 0, 1, 2], [3, 4, 5, 6, 7], [8, 9, 10, 11, 12], [-13, -14, -15, -16, -17], [-18, -19, -20, -21, -22]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 4, 3, 2, 1], [-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 4, 3, 2, 1], [-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, -1], [8, 7, 6, 5, 4, 3, 2, 1, -1, -2], [7, 6, 5, 4, 3, 2, 1, -1, -2, -3], [6, 5, 4, 3, 2, 1, -1, -2, -3, -4], [5, 4, 3, 2, 1, -1, -2, -3, -4, -5], [4, 3, 2, 1, -1, -2, -3, -4, -5, -6], [3, 2, 1, -1, -2, -3, -4, -5, -6, -7], [2, 1, -1, -2, -3, -4, -5, -6, -7, -8], [1, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, -1], [8, 7, 6, 5, 4, 3, 2, 1, -1, -2], [7, 6, 5, 4, 3, 2, 1, -1, -2, -3], [6, 5, 4, 3, 2, 1, -1, -2, -3, -4], [5, 4, 3, 2, 1, -1, -2, -3, -4, -5], [4, 3, 2, 1, -1, -2, -3, -4, -5, -6], [3, 2, 1, -1, -2, -3, -4, -5, -6, -7], [2, 1, -1, -2, -3, -4, -5, -6, -7, -8], [1, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[100, -50, 0], [90, -40, 0], [80, -30, 0], [70, -20, 0], [60, -10, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[100, -50, 0], [90, -40, 0], [80, -30, 0], [70, -20, 0], [60, -10, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[50, 20, 10, 0, -10, -20], [-30, -40, -50, -60, -70, -80], [-90, -100, -110, -120, -130, -140]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[50, 20, 10, 0, -10, -20], [-30, -40, -50, -60, -70, -80], [-90, -100, -110, -120, -130, -140]]) == 14: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [[-1, -1], [-1, -1]]) == 4
    assert candidate(grid = [[-3], [-2], [-1], [0], [1]]) == 0
    assert candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 12
    assert candidate(grid = [[-1, -1, -1], [-5, -5, -5]]) == 6
    assert candidate(grid = [[3, 2], [1, 0]]) == 0
    assert candidate(grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
    assert candidate(grid = [[1, -1], [-1, -1]]) == 3
    assert candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 16
    assert candidate(grid = [[5, 2, 1], [4, 3, 1], [3, 2, 1]]) == 0
    assert candidate(grid = [[1, 2, 3], [4, 5, 6]]) == 0
    assert candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == 12
    assert candidate(grid = [[100, 90, 80, -10], [-9, -8, -7, -6], [-5, -4, -3, -2], [-4, -3, -2, -1]]) == 13
    assert candidate(grid = [[1]]) == 0
    assert candidate(grid = [[-5]]) == 1
    assert candidate(grid = [[1, 2, 3], [0, -1, -2], [-3, -4, -5]]) == 5
    assert candidate(grid = [[-1]]) == 1
    assert candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, 0, -1], [2, 1, 0, -1, -2], [1, 0, -1, -2, -3]]) == 6
    assert candidate(grid = [[-1, 0], [0, -1]]) == 1
    assert candidate(grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == 0
    assert candidate(grid = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [-11, 12, -13, 14, -15], [16, -17, 18, -19, 20]]) == 10
    assert candidate(grid = [[1, 0, 0, 0, 0], [-1, 0, 0, 0, 0], [-1, -1, 0, 0, 0], [-1, -1, -1, 0, 0], [-1, -1, -1, -1, 0]]) == 20
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, -1]]) == 1
    assert candidate(grid = [[50, 40, 30, 20, 10, 0, -10, -20], [-5, -10, -15, -20, -25, -30, -35, -40], [-50, -60, -70, -80, -90, -100, -110, -120]]) == 18
    assert candidate(grid = [[-100, -99, -98, -97, -96], [-95, -94, -93, -92, -91], [-90, -89, -88, -87, -86], [-85, -84, -83, -82, -81], [-80, -79, -78, -77, -76]]) == 25
    assert candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0, -1], [7, 6, 5, 4, 3, 2, 1, 0, -1, -2], [6, 5, 4, 3, 2, 1, 0, -1, -2, -3], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -6], [2, 1, 0, -1, -2, -3, -4, -5, -6, -7], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8]]) == 36
    assert candidate(grid = [[-99, -98, -97, -96, -95, -94, -93, -92, -91, -90], [-89, -88, -87, -86, -85, -84, -83, -82, -81, -80], [-79, -78, -77, -76, -75, -74, -73, -72, -71, -70], [-69, -68, -67, -66, -65, -64, -63, -62, -61, -60], [-59, -58, -57, -56, -55, -54, -53, -52, -51, -50], [-49, -48, -47, -46, -45, -44, -43, -42, -41, -40], [-39, -38, -37, -36, -35, -34, -33, -32, -31, -30], [-29, -28, -27, -26, -25, -24, -23, -22, -21, -20], [-19, -18, -17, -16, -15, -14, -13, -12, -11, -10], [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]]) == 100
    assert candidate(grid = [[1, -1, 1, -1, 1, -1, 1, -1, 1, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2], [-3, -3, -3, -3, -3, -3, -3, -3, -3, -3]]) == 30
    assert candidate(grid = [[1, 1, 1, -1, -1, -1], [1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]) == 13
    assert candidate(grid = [[9, -9, 8, -8], [7, -7, 6, -6], [5, -5, 4, -4], [3, -3, 2, -2], [1, -1, 0, -1]]) == 15
    assert candidate(grid = [[99, 98, 97, 96, 95, 94], [93, 92, 91, 90, -1, -2], [-3, -4, -5, -6, -7, -8], [-9, -10, -11, -12, -13, -14]]) == 14
    assert candidate(grid = [[10, -10, 20, -20, 30, -30], [9, -9, 18, -18, 27, -27], [8, -8, 16, -16, 24, -24], [7, -7, 14, -14, 21, -21]]) == 20
    assert candidate(grid = [[0, 0, 0, 0, -1], [0, 0, -1, -1, -1], [0, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == 13
    assert candidate(grid = [[-5, -4, -3, -2, -1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 0
    assert candidate(grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]) == 20
    assert candidate(grid = [[1, 0, -1, 0, -1], [0, -1, 0, -1, 0], [-1, 0, -1, 0, -1], [0, -1, 0, -1, 0], [-1, 0, -1, 0, -1]]) == 15
    assert candidate(grid = [[-50, -40, -30, -20, -10], [30, 20, 10, 0, -10], [-20, -10, 0, 10, 20], [10, 0, 10, 20, 30], [0, 10, 20, 30, 40]]) == 0
    assert candidate(grid = [[90, 80, 70, 60, 50, 40, 30, 20, 10, 0], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]]) == 10
    assert candidate(grid = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[-5, -4, -3, -2, -1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[-1, -1, -1, 0], [1, 0, -1, -1], [1, -1, -1, -1], [-1, -1, -1, -1]]) == 11
    assert candidate(grid = [[-3, -2, -1, 0], [2, 1, 0, -1], [1, 0, -1, -2], [0, -1, -2, -3]]) == 6
    assert candidate(grid = [[10, -5, 3, 2, -1], [-3, 0, -1, 0, -4], [-5, -6, -7, -8, -9]]) == 14
    assert candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0, -1], [7, 6, 5, 4, 3, 2, 1, 0, -1, -2], [6, 5, 4, 3, 2, 1, 0, -1, -2, -3], [5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [3, 2, 1, 0, -1, -2, -3, -4, -5, -6], [2, 1, 0, -1, -2, -3, -4, -5, -6, -7], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8]]) == 36
    assert candidate(grid = [[-100, -99, -98, -97, -96], [0, 0, 0, -1, -2], [-3, -4, -5, -6, -7], [-8, -9, -10, -11, -12]]) == 14
    assert candidate(grid = [[1, -1, -2, -3], [-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6]]) == 15
    assert candidate(grid = [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-2, -3, -4, -5, -6, -7, -8, -9, -10, -11], [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12]]) == 30
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, -1, -1], [0, 0, 0, 0, 0, 0, 0, -1, -1, -1], [0, 0, 0, 0, 0, 0, -1, -1, -1, -1], [0, 0, 0, 0, 0, -1, -1, -1, -1, -1], [0, 0, 0, 0, -1, -1, -1, -1, -1, -1], [0, 0, 0, -1, -1, -1, -1, -1, -1, -1], [0, 0, -1, -1, -1, -1, -1, -1, -1, -1], [0, -1, -1, -1, -1, -1, -1, -1, -1, -1]]) == 45
    assert candidate(grid = [[-1, 0, 1, 2, 3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50]]) == 14
    assert candidate(grid = [[10, -10, 20, -20], [5, -5, 15, -15], [0, 0, 0, 0], [-1, -2, -3, -4]]) == 4
    assert candidate(grid = [[99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [89, 88, 87, 86, 85, 84, 83, 82, 81, 80], [79, 78, 77, 76, 75, 74, 73, 72, 71, 70], [69, 68, 67, 66, 65, 64, 63, 62, 61, 60], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-11, -12, -13, -14, -15, -16, -17, -18, -19, -20], [-21, -22, -23, -24, -25, -26, -27, -28, -29, -30], [-31, -32, -33, -34, -35, -36, -37, -38, -39, -40], [-41, -42, -43, -44, -45, -46, -47, -48, -49, -50]]) == 50
    assert candidate(grid = [[-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1]]) == 15
    assert candidate(grid = [[2, 1, 0, -1, -2], [1, 0, -1, -2, -3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6]]) == 19
    assert candidate(grid = [[100, 90, 80, 70, 60, 50, 40, 30, 20, 10], [90, 80, 70, 60, 50, 40, 30, 20, 10, 0], [80, 70, 60, 50, 40, 30, 20, 10, 0, -10], [70, 60, 50, 40, 30, 20, 10, 0, -10, -20], [60, 50, 40, 30, 20, 10, 0, -10, -20, -30]]) == 6
    assert candidate(grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == 0
    assert candidate(grid = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12], [-13, -14, -15, -16]]) == 16
    assert candidate(grid = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == 20
    assert candidate(grid = [[1, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0
    assert candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, -1, -2], [2, 1, -2, -3, -4], [1, 0, -3, -4, -5]]) == 8
    assert candidate(grid = [[99, 98, 97, 96, 95], [-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -101, -102, -103, -104]]) == 15
    assert candidate(grid = [[10, -5, -4, -3], [-7, -6, -5, -4], [-8, -7, -6, -5], [-9, -8, -7, -6]]) == 15
    assert candidate(grid = [[50, 40, 30, 20, 10], [45, 35, 25, 15, 5], [40, 30, 20, 10, 0], [35, 25, 15, 5, -5]]) == 1
    assert candidate(grid = [[-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6], [-3, -4, -5, -6, -7], [-4, -5, -6, -7, -8], [-5, -6, -7, -8, -9]]) == 25
    assert candidate(grid = [[1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9], [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 90
    assert candidate(grid = [[0, 0, 0, 0, -1], [0, 0, 0, -1, -2], [0, 0, -1, -2, -3], [0, -1, -2, -3, -4], [-1, -2, -3, -4, -5]]) == 15
    assert candidate(grid = [[-100, -99, -98, -97, -96, -95, -94, -93, -92, -91], [-90, -89, -88, -87, -86, -85, -84, -83, -82, -81], [-80, -79, -78, -77, -76, -75, -74, -73, -72, -71], [-70, -69, -68, -67, -66, -65, -64, -63, -62, -61], [-60, -59, -58, -57, -56, -55, -54, -53, -52, -51], [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41], [-40, -39, -38, -37, -36, -35, -34, -33, -32, -31], [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21], [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11], [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]]) == 100
    assert candidate(grid = [[-5, -4, -3, -2, -1], [-10, -9, -8, -7, -6], [-15, -14, -13, -12, -11], [-20, -19, -18, -17, -16], [-25, -24, -23, -22, -21]]) == 25
    assert candidate(grid = [[0, 0, 0, 0], [0, 0, -1, -2], [0, -1, -2, -3], [-1, -2, -3, -4]]) == 9
    assert candidate(grid = [[1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1]]) == 20
    assert candidate(grid = [[0, 0, 0, 0], [0, 0, 0, -1], [0, 0, -1, -1], [0, -1, -1, -1]]) == 6
    assert candidate(grid = [[50, 40, 30, 20, 10], [45, 35, 25, 15, 5], [40, 30, 20, 10, 0], [35, 25, 15, 5, -5], [30, 20, 10, 0, -10]]) == 2
    assert candidate(grid = [[10, 8, 6, 4, 2, 0, -2, -4], [-6, -8, -10, -12, -14, -16, -18, -20], [-10, -12, -14, -16, -18, -20, -22, -24]]) == 18
    assert candidate(grid = [[-10, -20, -30, -40], [-20, -30, -40, -50], [-30, -40, -50, -60], [-40, -50, -60, -70]]) == 16
    assert candidate(grid = [[-10, -20, -30, -40, -50, -60, -70, -80, -90], [-110, -120, -130, -140, -150, -160, -170, -180, -190], [-200, -210, -220, -230, -240, -250, -260, -270, -280]]) == 27
    assert candidate(grid = [[-100, -99, -98, -97], [-96, -95, -94, -93], [-92, -91, -90, -89], [-88, -87, -86, -85]]) == 16
    assert candidate(grid = [[10, 20, 30, 40, 50], [20, 30, 40, 50, 60], [30, 40, 50, 60, 70], [40, 50, 60, 70, 80], [50, 60, 70, 80, 90]]) == 0
    assert candidate(grid = [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == 0
    assert candidate(grid = [[-100, -99, -98, -97, -96, -95, -94, -93, -92, -91], [-90, -89, -88, -87, -86, -85, -84, -83, -82, -81], [-80, -79, -78, -77, -76, -75, -74, -73, -72, -71], [-70, -69, -68, -67, -66, -65, -64, -63, -62, -61]]) == 40
    assert candidate(grid = [[-50, -49, -48, -47, -46, -45], [-44, -43, -42, -41, -40, -39], [-38, -37, -36, -35, -34, -33], [-32, -31, -30, -29, -28, -27]]) == 24
    assert candidate(grid = [[-100, -99, -98], [-99, -98, -97], [-98, -97, -96], [-97, -96, -95]]) == 12
    assert candidate(grid = [[10, 5, 0, -10, -20], [-5, -15, -20, -25, -30], [-1, -2, -3, -4, -5]]) == 12
    assert candidate(grid = [[1, -1, 0], [1, -1, 0], [1, -1, 0]]) == 6
    assert candidate(grid = [[1, 0, -1], [-1, -2, -3], [-2, -3, -4], [-3, -4, -5]]) == 10
    assert candidate(grid = [[9, 7, 5, 3, 1], [-1, -3, -5, -7, -9], [-2, -4, -6, -8, -10], [-3, -6, -9, -12, -15]]) == 15
    assert candidate(grid = [[0, 0, 0], [0, 0, -1], [0, -1, -2], [-1, -2, -3]]) == 6
    assert candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, -1], [3, 2, 1, -1, -2], [2, 1, -1, -2, -3], [1, -1, -2, -3, -4]]) == 10
    assert candidate(grid = [[1, 0, -1], [-1, 0, 1], [0, 1, -1]]) == 1
    assert candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, -1], [8, 7, 6, 5, 4, 3, 2, 1, -2, -3], [7, 6, 5, 4, 3, 2, 1, -3, -4, -5]]) == 6
    assert candidate(grid = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, -1], [0, 0, 0, -1, -1, -2], [-1, -1, -2, -3, -4, -5]]) == 11
    assert candidate(grid = [[-2, -1, 0, 1, 2], [3, 4, 5, 6, 7], [8, 9, 10, 11, 12], [-13, -14, -15, -16, -17], [-18, -19, -20, -21, -22]]) == 10
    assert candidate(grid = [[1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4], [1, -1, 2, -2, 3, -3, 4, -4]]) == 28
    assert candidate(grid = [[5, 4, 3, 2, 1, 0, -1, -2, -3, -4], [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 9
    assert candidate(grid = [[5, 4, 3, 2, 1], [-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10]]) == 10
    assert candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, -1], [8, 7, 6, 5, 4, 3, 2, 1, -1, -2], [7, 6, 5, 4, 3, 2, 1, -1, -2, -3], [6, 5, 4, 3, 2, 1, -1, -2, -3, -4], [5, 4, 3, 2, 1, -1, -2, -3, -4, -5], [4, 3, 2, 1, -1, -2, -3, -4, -5, -6], [3, 2, 1, -1, -2, -3, -4, -5, -6, -7], [2, 1, -1, -2, -3, -4, -5, -6, -7, -8], [1, -1, -2, -3, -4, -5, -6, -7, -8, -9]]) == 45
    assert candidate(grid = [[100, -50, 0], [90, -40, 0], [80, -30, 0], [70, -20, 0], [60, -10, 0]]) == 10
    assert candidate(grid = [[50, 20, 10, 0, -10, -20], [-30, -40, -50, -60, -70, -80], [-90, -100, -110, -120, -130, -140]]) == 14


