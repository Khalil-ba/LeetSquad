def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0], [-8, -2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0], [-8, -2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0], [-2, -1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0], [-2, -1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-4, 3], [-3, -4]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-4, 3], [-3, -4]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 3, 4], [0, 1, 5]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 3, 4], [0, 1, 5]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3], [-4, 5, -6], [-7, -8, 9]]) == 2016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3], [-4, 5, -6], [-7, -8, 9]]) == 2016: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2], [-3, 4]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2], [-3, 4]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, -3, 4], [-1, -2, 3], [1, 2, -5]]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, -3, 4], [-1, -2, 3], [1, 2, -5]]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -2, 1], [1, -2, 1], [3, -4, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -2, 1], [1, -2, 1], [3, -4, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1], [1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1], [1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0], [-2, -3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0], [-2, -3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2], [3, 4]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2], [3, 4]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 3], [0, -4]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 3], [0, -4]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-4, -4], [-4, -4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-4, -4], [-4, -4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 2016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 2016: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -4, -7], [-2, -5, -8], [-3, -6, -9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -4, -7], [-2, -5, -8], [-3, -6, -9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 3, -1, 4], [1, -2, 3, -3], [-4, 5, -6, 7], [-8, -9, 10, 11]]) == 59400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 3, -1, 4], [1, -2, 3, -3], [-4, 5, -6, 7], [-8, -9, 10, 11]]) == 59400: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-2, -3, 0, -4], [-1, -2, -3, 1], [0, -1, -2, -3], [2, 3, 4, -5]]) == 1440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-2, -3, 0, -4], [-1, -2, -3, 1], [0, -1, -2, -3], [2, 3, 4, -5]]) == 1440: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0, 1], [0, 0, 0], [1, 0, -1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0, 1], [0, 0, 0], [1, 0, -1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [11, -12, 13, -14, 15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 450227165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [11, -12, 13, -14, 15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 450227165: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1, -1], [1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1, -1], [1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-4, 3, -2, 1], [2, -1, 3, -4], [3, -4, 2, 1], [4, 1, -3, 2]]) == 576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-4, 3, -2, 1], [2, -1, 3, -4], [3, -4, 2, 1], [4, 1, -3, 2]]) == 576: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-3, 3, -4, 1], [2, -1, 2, -3], [-2, 3, -2, 1], [4, -4, 3, -3]]) == 1728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-3, 3, -4, 1], [2, -1, 2, -3], [-2, 3, -2, 1], [4, -4, 3, -3]]) == 1728: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3, 4, -5], [5, -6, 7, -8, 9], [-10, 11, -12, 13, -14], [15, -16, 17, -18, 19], [-20, 21, -22, 23, -24]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3, 4, -5], [5, -6, 7, -8, 9], [-10, 11, -12, 13, -14], [15, -16, 17, -18, 19], [-20, 21, -22, 23, -24]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0, 1, 0, -1], [-1, 1, 0, 1, -1], [0, -1, 1, -1, 0], [1, -1, 0, 1, -1], [-1, 0, 1, 0, -1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0, 1, 0, -1], [-1, 1, 0, 1, -1], [0, -1, 1, -1, 0], [1, -1, 0, 1, -1], [-1, 0, 1, 0, -1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, -2, 3, -3], [-3, 3, -2, 2], [2, -2, 3, -3], [-3, 3, -2, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, -2, 3, -3], [-3, 3, -2, 2], [2, -2, 3, -3], [-3, 3, -2, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 3, -4, 2], [-2, 1, -1, 0], [3, -3, 2, -3], [4, 0, -1, 2]]) == 216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 3, -4, 2], [-2, 1, -1, 0], [3, -3, 2, -3], [4, 0, -1, 2]]) == 216: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3, 4, 5], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3, 4, 5], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0, 0, 0], [-2, 0, 0, 0], [-3, 0, 0, 0], [-4, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0, 0, 0], [-2, 0, 0, 0], [-3, 0, 0, 0], [-4, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) == 75000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) == 75000: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-3, -2, 1], [-2, -1, 3], [-1, 3, -2]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-3, -2, 1], [-2, -1, 3], [-1, 3, -2]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 3, 2, 1], [3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 3, 2, 1], [3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-2, 0, 2, 0], [-1, -2, -3, -1], [0, 1, 0, 1], [2, -2, 1, -3]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-2, 0, 2, 0], [-1, -2, -3, -1], [0, 1, 0, 1], [2, -2, 1, -3]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3, 4], [-2, 3, -4, 5], [3, -4, 5, -6], [4, 5, -6, 7]]) == 5040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3, 4], [-2, 3, -4, 5], [3, -4, 5, -6], [4, 5, -6, 7]]) == 5040: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 2, -3], [2, -2, 3, 4], [-3, 3, -4, 5], [0, -1, 2, -2]]) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 2, -3], [2, -2, 3, 4], [-3, 3, -4, 5], [0, -1, 2, -2]]) == 480: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == 1965600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == 1965600: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-4, 3, 2, -1, 0], [0, 2, -3, 1, 4], [-1, 2, -1, 3, -2], [3, -2, 1, -1, 2], [1, -3, 2, -2, -4]]) == 4608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-4, 3, 2, -1, 0], [0, 2, -3, 1, 4], [-1, 2, -1, 3, -2], [3, -2, 1, -1, 2], [1, -3, 2, -2, -4]]) == 4608: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 3, 2, 1], [3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 3, 2, 1], [3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, 3, 4], [5, 6, -7, 8], [-9, 10, 11, -12], [13, -14, 15, 16]]) == 1188000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, 3, 4], [5, 6, -7, 8], [-9, 10, 11, -12], [13, -14, 15, 16]]) == 1188000: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -2, 3, -4], [4, -1, 2, -3], [3, 2, -1, 4]]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -2, 3, -4], [4, -1, 2, -3], [3, 2, -1, 4]]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, -1, 2], [1, 2, -1], [2, -1, 4], [-1, 4, -1]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, -1, 2], [1, 2, -1], [2, -1, 4], [-1, 4, -1]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 0], [1, 0, 1], [0, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 0], [1, 0, 1], [0, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3, 4], [4, 3, 2, 1, 0], [-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3, 4], [4, 3, 2, 1, 0], [-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1], [0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1], [0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2], [3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3]]) == 13608000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2], [3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3]]) == 13608000: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 732633558
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 732633558: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0, -1], [0, -1, 0], [-1, 0, -1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0, -1], [0, -1, 0], [-1, 0, -1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 1], [0, -1, 0], [-1, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 1], [0, -1, 0], [-1, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0, 0, -1], [0, -1, 0, -1], [0, 0, -1, 0], [-1, 0, 0, -1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0, 0, -1], [0, -1, 0, -1], [0, 0, -1, 0], [-1, 0, 0, -1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -1, 3], [2, -3, 4, -2], [3, -1, -2, 2], [1, -3, 2, -1]]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -1, 3], [2, -3, 4, -2], [3, -1, -2, 2], [1, -3, 2, -1]]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, -3, -2], [-2, 1, 0], [3, -5, 6]]) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, -3, -2], [-2, 1, 0], [3, -5, 6]]) == 720: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 3, 0, 4], [0, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 3, 0, 4], [0, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3, 4, -5], [2, -3, 4, -5, 6], [-3, 4, -5, 6, -7], [4, -5, 6, -7, 8], [-5, 6, -7, 8, -9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3, 4, -5], [2, -3, 4, -5, 6], [-3, 4, -5, 6, -7], [4, -5, 6, -7, 8], [-5, 6, -7, 8, -9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 1512000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 1512000: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 0, 2], [-1, 2, 3, -1], [0, 1, -1, 1], [2, -2, 1, -3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 0, 2], [-1, 2, 3, -1], [0, 1, -1, 1], [2, -2, 1, -3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]) == 674358851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]) == 674358851: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-4, -3, -2, -1], [-3, -2, -1, 0], [-2, -1, 0, 1], [-1, 0, 1, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-4, -3, -2, -1], [-3, -2, -1, 0], [-2, -1, 0, 1], [-1, 0, 1, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-2, -3, -4], [-1, -5, -6], [-7, -8, -9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-2, -3, -4], [-1, -5, -6], [-7, -8, -9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 5040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 5040: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6], [-3, -4, -5, -6, -7], [-4, -5, -6, -7, -8], [-5, -6, -7, -8, -9]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6], [-3, -4, -5, -6, -7], [-4, -5, -6, -7, -8], [-5, -6, -7, -8, -9]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == 36960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == 36960: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 2, -2, 3, -3], [4, -4, 5, -5, 6, -6], [7, -7, 8, -8, 9, -9], [10, -10, 11, -11, 12, -12], [13, -13, 14, -14, 15, -15]]) == 605239993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 2, -2, 3, -3], [4, -4, 5, -5, 6, -6], [7, -7, 8, -8, 9, -9], [10, -10, 11, -11, 12, -12], [13, -13, 14, -14, 15, -15]]) == 605239993: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3, -4], [-2, -3, -3, -4], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3, -4], [-2, -3, -3, -4], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -2, 3, -4], [5, 6, -7, 8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 1008000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -2, 3, -4], [5, 6, -7, 8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 1008000: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-2, -3, 1, -4], [-3, -2, 1, 3], [-1, 2, -3, 1]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-2, -3, 1, -4], [-3, -2, 1, 3], [-1, 2, -3, 1]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, -1, -2, 3], [-1, 2, 1, -1], [-2, -1, 3, 4], [1, -3, 2, 1]]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, -1, -2, 3], [-1, 2, 1, -1], [-2, -1, 3, 4], [1, -3, 2, 1]]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26]]) == 544121446
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26]]) == 544121446: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, -4, 3, -3], [-3, 3, -2, 2], [2, -2, 3, -3], [-3, 3, -2, 2]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, -4, 3, -3], [-3, 3, -2, 2], [2, -2, 3, -3], [-3, 3, -2, 2]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3, -4], [-4, -5, -6, -7], [-8, -9, -10, -11], [-12, -13, -14, -15]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3, -4], [-4, -5, -6, -7], [-8, -9, -10, -11], [-12, -13, -14, -15]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 362880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 362880: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-4, -3, -2, -1], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 8640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-4, -3, -2, -1], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 8640: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, -1, 1], [1, -1, 0], [-1, 0, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, -1, 1], [1, -1, 0], [-1, 0, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -3, 4], [-4, 1, -2, 3], [2, -1, 4, -3], [3, 4, -1, 2]]) == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -3, 4], [-4, 1, -2, 3], [2, -1, 4, -3], [3, 4, -1, 2]]) == 288: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-2, -3, 0, -1], [-1, -2, -3, -4], [0, -1, -2, -3], [-3, -4, -5, -6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-2, -3, 0, -1], [-1, -2, -3, -4], [0, -1, -2, -3], [-3, -4, -5, -6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, -1, 3, -4], [1, 0, 5, -1], [3, -2, 4, 1]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, -1, 3, -4], [1, 0, 5, -1], [3, -2, 4, 1]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, -1, 2], [2, -3, 4], [-1, 2, -3]]) == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, -1, 2], [2, -3, 4], [-1, 2, -3]]) == 288: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, -2, -3], [-3, -4, -5], [-5, -6, -7]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, -2, -3], [-3, -4, -5], [-5, -6, -7]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 0, 1], [0, 1, 0], [1, 0, -1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 0, 1], [0, 1, 0], [1, 0, -1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-4, -3, -2], [-2, -1, 0], [3, -5, 6]]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-4, -3, -2], [-2, -1, 0], [3, -5, 6]]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-4, -4, -4, -4], [-4, -4, -4, -4], [-4, -4, -4, -4], [-4, -4, -4, -4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-4, -4, -4, -4], [-4, -4, -4, -4], [-4, -4, -4, -4], [-4, -4, -4, -4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-2, 3, -1, 4], [-1, 2, -3, 5], [3, -4, 5, -6], [4, -5, 6, -7]]) == 10080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-2, 3, -1, 4], [-1, 2, -3, 5], [3, -4, 5, -6], [4, -5, 6, -7]]) == 10080: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, -1, 2, -4], [-2, 3, -1, 2], [4, -2, 3, -1], [-2, 1, -3, 4]]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, -1, 2, -4], [-2, 3, -1, 2], [4, -2, 3, -1], [-2, 1, -3, 4]]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 2016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 2016: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, -2, 3, 4, -1], [-1, 3, 2, 1, -2], [1, 2, -3, 2, -1], [3, 1, -2, -1, 2], [1, -2, 2, 1, -3]]) == 864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, -2, 3, 4, -1], [-1, 3, 2, 1, -2], [1, 2, -3, 2, -1], [3, 1, -2, -1, 2], [1, -2, 2, 1, -3]]) == 864: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, -3, 4, 5], [-1, 3, 2, -2], [2, -1, -2, -1], [1, 2, 3, -1]]) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, -3, 4, 5], [-1, 3, 2, -2], [2, -1, -2, -1], [1, 2, 3, -1]]) == 240: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 3, 4], [1, 0, 1], [4, 3, 2], [3, 2, 1]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 3, 4], [1, 0, 1], [4, 3, 2], [3, 2, 1]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 3, -1, -4, 1], [-2, 1, 2, 3, -1], [3, -2, -1, 1, 2], [1, 2, -3, 4, -2]]) == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 3, -1, -4, 1], [-2, 1, 2, 3, -1], [3, -2, -1, 1, 2], [1, 2, -3, 4, -2]]) == 288: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 5040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 5040: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]) == 674358851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]) == 674358851: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[-1, 2, -1, 3], [1, -2, 1, -1], [2, 1, -1, -3], [1, -1, -2, 1]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[-1, 2, -1, 3], [1, -2, 1, -1], [2, 1, -1, -3], [1, -1, -2, 1]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 3, 4, 5]]) == 72000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 3, 4, 5]]) == 72000: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, -1, -2, -3], [-1, 0, -1, -2], [-2, -1, 0, -1], [-3, -2, -1, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, -1, -2, -3], [-1, 0, -1, -2], [-2, -1, 0, -1], [-3, -2, -1, 0]]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]) == -1
    assert candidate(grid = [[-1, 0], [-8, -2]]) == 0
    assert candidate(grid = [[-1, 0], [-2, -1]]) == 0
    assert candidate(grid = [[-4, 3], [-3, -4]]) == 48
    assert candidate(grid = [[0, 0], [0, 0]]) == 0
    assert candidate(grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 1
    assert candidate(grid = [[2, 3, 4], [0, 1, 5]]) == 120
    assert candidate(grid = [[-1, 2, -3], [-4, 5, -6], [-7, -8, 9]]) == 2016
    assert candidate(grid = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]) == -1
    assert candidate(grid = [[-1, 2], [-3, 4]]) == 12
    assert candidate(grid = [[2, -3, 4], [-1, -2, 3], [1, 2, -5]]) == 360
    assert candidate(grid = [[1, -2, 1], [1, -2, 1], [3, -4, 1]]) == 8
    assert candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
    assert candidate(grid = [[1, 1], [1, 1]]) == 1
    assert candidate(grid = [[-1, 0], [-2, -3]]) == 0
    assert candidate(grid = [[1, 2], [3, 4]]) == 12
    assert candidate(grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 1
    assert candidate(grid = [[1, 3], [0, -4]]) == 0
    assert candidate(grid = [[-4, -4], [-4, -4]]) == -1
    assert candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 2016
    assert candidate(grid = [[-1, -4, -7], [-2, -5, -8], [-3, -6, -9]]) == -1
    assert candidate(grid = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]) == -1
    assert candidate(grid = [[2, 3, -1, 4], [1, -2, 3, -3], [-4, 5, -6, 7], [-8, -9, 10, 11]]) == 59400
    assert candidate(grid = [[-2, -3, 0, -4], [-1, -2, -3, 1], [0, -1, -2, -3], [2, 3, 4, -5]]) == 1440
    assert candidate(grid = [[-1, 0, 1], [0, 0, 0], [1, 0, -1]]) == 0
    assert candidate(grid = [[-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0], [-1, 0, 0, 0]]) == 0
    assert candidate(grid = [[-1, 2, -3, 4, -5], [6, -7, 8, -9, 10], [11, -12, 13, -14, 15], [16, -17, 18, -19, 20], [21, -22, 23, -24, 25]]) == 450227165
    assert candidate(grid = [[-1, -1, -1, -1], [1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, 1]]) == 1
    assert candidate(grid = [[-4, 3, -2, 1], [2, -1, 3, -4], [3, -4, 2, 1], [4, 1, -3, 2]]) == 576
    assert candidate(grid = [[-3, 3, -4, 1], [2, -1, 2, -3], [-2, 3, -2, 1], [4, -4, 3, -3]]) == 1728
    assert candidate(grid = [[-1, 2, -3, 4, -5], [5, -6, 7, -8, 9], [-10, 11, -12, 13, -14], [15, -16, 17, -18, 19], [-20, 21, -22, 23, -24]]) == -1
    assert candidate(grid = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]) == -1
    assert candidate(grid = [[-1, 0, 1, 0, -1], [-1, 1, 0, 1, -1], [0, -1, 1, -1, 0], [1, -1, 0, 1, -1], [-1, 0, 1, 0, -1]]) == 1
    assert candidate(grid = [[2, -2, 3, -3], [-3, 3, -2, 2], [2, -2, 3, -3], [-3, 3, -2, 2]]) == -1
    assert candidate(grid = [[-1, 3, -4, 2], [-2, 1, -1, 0], [3, -3, 2, -3], [4, 0, -1, 2]]) == 216
    assert candidate(grid = [[0, 1, 2, 3, 4, 5], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1]]) == 0
    assert candidate(grid = [[-1, 0, 0, 0], [-2, 0, 0, 0], [-3, 0, 0, 0], [-4, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) == 75000
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 0
    assert candidate(grid = [[-3, -2, 1], [-2, -1, 3], [-1, 3, -2]]) == 36
    assert candidate(grid = [[4, 3, 2, 1], [3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2]]) == 0
    assert candidate(grid = [[-2, 0, 2, 0], [-1, -2, -3, -1], [0, 1, 0, 1], [2, -2, 1, -3]]) == 36
    assert candidate(grid = [[1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1], [-1, 1, -1, 1, -1], [1, -1, 1, -1, 1]]) == 1
    assert candidate(grid = [[-1, 2, -3, 4], [-2, 3, -4, 5], [3, -4, 5, -6], [4, 5, -6, 7]]) == 5040
    assert candidate(grid = [[1, -1, 2, -3], [2, -2, 3, 4], [-3, 3, -4, 5], [0, -1, 2, -2]]) == 480
    assert candidate(grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == 1965600
    assert candidate(grid = [[-4, 3, 2, -1, 0], [0, 2, -3, 1, 4], [-1, 2, -1, 3, -2], [3, -2, 1, -1, 2], [1, -3, 2, -2, -4]]) == 4608
    assert candidate(grid = [[4, 3, 2, 1], [3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2]]) == 0
    assert candidate(grid = [[-1, 2, 3, 4], [5, 6, -7, 8], [-9, 10, 11, -12], [13, -14, 15, 16]]) == 1188000
    assert candidate(grid = [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]) == -1
    assert candidate(grid = [[1, -2, 3, -4], [4, -1, 2, -3], [3, 2, -1, 4]]) == 144
    assert candidate(grid = [[4, -1, 2], [1, 2, -1], [2, -1, 4], [-1, 4, -1]]) == 32
    assert candidate(grid = [[1, -1, 0], [1, 0, 1], [0, 1, 1]]) == 0
    assert candidate(grid = [[0, 1, 2, 3, 4], [4, 3, 2, 1, 0], [-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]]) == 0
    assert candidate(grid = [[0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1], [0, 0, 0, 0]]) == 0
    assert candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2], [3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3]]) == 13608000
    assert candidate(grid = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == 732633558
    assert candidate(grid = [[-1, 0, -1], [0, -1, 0], [-1, 0, -1]]) == 0
    assert candidate(grid = [[0, 0, 1], [0, -1, 0], [-1, 0, 0]]) == 0
    assert candidate(grid = [[-1, 0, 0, -1], [0, -1, 0, -1], [0, 0, -1, 0], [-1, 0, 0, -1]]) == 0
    assert candidate(grid = [[-1, -2, -3, -4], [-2, -3, -4, -5], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == -1
    assert candidate(grid = [[-1, 2, -1, 3], [2, -3, 4, -2], [3, -1, -2, 2], [1, -3, 2, -1]]) == 96
    assert candidate(grid = [[4, -3, -2], [-2, 1, 0], [3, -5, 6]]) == 720
    assert candidate(grid = [[0, 3, 0, 4], [0, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0]]) == 0
    assert candidate(grid = [[-1, 2, -3, 4, -5], [2, -3, 4, -5, 6], [-3, 4, -5, 6, -7], [4, -5, 6, -7, 8], [-5, 6, -7, 8, -9]]) == -1
    assert candidate(grid = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12], [-13, 14, -15, 16]]) == 1512000
    assert candidate(grid = [[1, -1, 0, 2], [-1, 2, 3, -1], [0, 1, -1, 1], [2, -2, 1, -3]]) == 0
    assert candidate(grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]) == 674358851
    assert candidate(grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 1
    assert candidate(grid = [[-4, -3, -2, -1], [-3, -2, -1, 0], [-2, -1, 0, 1], [-1, 0, 1, 2]]) == 0
    assert candidate(grid = [[-2, -3, -4], [-1, -5, -6], [-7, -8, -9]]) == -1
    assert candidate(grid = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 362880
    assert candidate(grid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 5040
    assert candidate(grid = [[-1, -2, -3, -4, -5], [-2, -3, -4, -5, -6], [-3, -4, -5, -6, -7], [-4, -5, -6, -7, -8], [-5, -6, -7, -8, -9]]) == -1
    assert candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == 36960
    assert candidate(grid = [[1, -1, 2, -2, 3, -3], [4, -4, 5, -5, 6, -6], [7, -7, 8, -8, 9, -9], [10, -10, 11, -11, 12, -12], [13, -13, 14, -14, 15, -15]]) == 605239993
    assert candidate(grid = [[-1, -2, -3, -4], [-2, -3, -3, -4], [-3, -4, -5, -6], [-4, -5, -6, -7]]) == -1
    assert candidate(grid = [[1, -2, 3, -4], [5, 6, -7, 8], [-9, 10, -11, 12], [13, -14, 15, -16]]) == 1008000
    assert candidate(grid = [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]) == 0
    assert candidate(grid = [[-2, -3, 1, -4], [-3, -2, 1, 3], [-1, 2, -3, 1]]) == 72
    assert candidate(grid = [[4, -1, -2, 3], [-1, 2, 1, -1], [-2, -1, 3, 4], [1, -3, 2, 1]]) == 96
    assert candidate(grid = [[2, 3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21], [22, 23, 24, 25, 26]]) == 544121446
    assert candidate(grid = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]) == 0
    assert candidate(grid = [[4, -4, 3, -3], [-3, 3, -2, 2], [2, -2, 3, -3], [-3, 3, -2, 2]]) == -1
    assert candidate(grid = [[-1, -2, -3, -4], [-4, -5, -6, -7], [-8, -9, -10, -11], [-12, -13, -14, -15]]) == -1
    assert candidate(grid = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]) == 362880
    assert candidate(grid = [[-4, -3, -2, -1], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 8640
    assert candidate(grid = [[0, -1, 1], [1, -1, 0], [-1, 0, 1]]) == 0
    assert candidate(grid = [[-1, 2, -3, 4], [-4, 1, -2, 3], [2, -1, 4, -3], [3, 4, -1, 2]]) == 288
    assert candidate(grid = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]) == 0
    assert candidate(grid = [[-2, -3, 0, -1], [-1, -2, -3, -4], [0, -1, -2, -3], [-3, -4, -5, -6]]) == 0
    assert candidate(grid = [[2, -1, 3, -4], [1, 0, 5, -1], [3, -2, 4, 1]]) == 30
    assert candidate(grid = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]) == 0
    assert candidate(grid = [[4, -1, 2], [2, -3, 4], [-1, 2, -3]]) == 288
    assert candidate(grid = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 36
    assert candidate(grid = [[-1, -2, -3], [-3, -4, -5], [-5, -6, -7]]) == -1
    assert candidate(grid = [[-1, 0, 1], [0, 1, 0], [1, 0, -1]]) == 0
    assert candidate(grid = [[-4, -3, -2], [-2, -1, 0], [3, -5, 6]]) == 360
    assert candidate(grid = [[-4, -4, -4, -4], [-4, -4, -4, -4], [-4, -4, -4, -4], [-4, -4, -4, -4]]) == -1
    assert candidate(grid = [[-2, 3, -1, 4], [-1, 2, -3, 5], [3, -4, 5, -6], [4, -5, 6, -7]]) == 10080
    assert candidate(grid = [[1, -1, 2, -4], [-2, 3, -1, 2], [4, -2, 3, -1], [-2, 1, -3, 4]]) == -1
    assert candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 2016
    assert candidate(grid = [[2, -2, 3, 4, -1], [-1, 3, 2, 1, -2], [1, 2, -3, 2, -1], [3, 1, -2, -1, 2], [1, -2, 2, 1, -3]]) == 864
    assert candidate(grid = [[2, -3, 4, 5], [-1, 3, 2, -2], [2, -1, -2, -1], [1, 2, 3, -1]]) == 240
    assert candidate(grid = [[2, 3, 4], [1, 0, 1], [4, 3, 2], [3, 2, 1]]) == 48
    assert candidate(grid = [[-1, 3, -1, -4, 1], [-2, 1, 2, 3, -1], [3, -2, -1, 1, 2], [1, 2, -3, 4, -2]]) == 288
    assert candidate(grid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]) == 5040
    assert candidate(grid = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]) == 674358851
    assert candidate(grid = [[-1, 2, -1, 3], [1, -2, 1, -1], [2, 1, -1, -3], [1, -1, -2, 1]]) == 18
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 3, 4, 5]]) == 72000
    assert candidate(grid = [[0, -1, -2, -3], [-1, 0, -1, -2], [-2, -1, 0, -1], [-3, -2, -1, 0]]) == 0


