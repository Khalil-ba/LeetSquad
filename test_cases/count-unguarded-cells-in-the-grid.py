def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 4,n = 6,guards = [[0, 0], [1, 1], [2, 3]],walls = [[0, 1], [2, 2], [1, 4]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 6,guards = [[0, 0], [1, 1], [2, 3]],walls = [[0, 1], [2, 2], [1, 4]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,guards = [[1, 1]],walls = [[0, 1], [1, 0], [2, 1], [1, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,guards = [[1, 1]],walls = [[0, 1], [1, 0], [2, 1], [1, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,guards = [[2, 2]],walls = [[0, 0], [4, 4]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,guards = [[2, 2]],walls = [[0, 0], [4, 4]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[3, 3], [6, 6]],walls = [[1, 1], [8, 8]]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[3, 3], [6, 6]],walls = [[1, 1], [8, 8]]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6,guards = [[1, 1], [4, 4]],walls = [[2, 2], [3, 3]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6,guards = [[1, 1], [4, 4]],walls = [[2, 2], [3, 3]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 12,guards = [[1, 1], [5, 5], [9, 9]],walls = [[2, 2], [6, 6], [10, 10], [3, 3], [7, 7], [11, 11]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 12,guards = [[1, 1], [5, 5], [9, 9]],walls = [[2, 2], [6, 6], [10, 10], [3, 3], [7, 7], [11, 11]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],walls = [[1, 1]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],walls = [[1, 1]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 5,guards = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]],walls = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 5,guards = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]],walls = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 10,guards = [[5, 2], [10, 7], [15, 3], [18, 8]],walls = [[0, 5], [4, 9], [9, 4], [14, 8], [19, 3], [7, 0]]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 10,guards = [[5, 2], [10, 7], [15, 3], [18, 8]],walls = [[0, 5], [4, 9], [9, 4], [14, 8], [19, 3], [7, 0]]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 20,guards = [[2, 5], [4, 8], [10, 15]],walls = [[3, 3], [6, 7], [9, 12], [11, 14]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 20,guards = [[2, 5], [4, 8], [10, 15]],walls = [[3, 3], [6, 7], [9, 12], [11, 14]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,guards = [[0, 0], [19, 19], [0, 19], [19, 0]],walls = [[5, 5], [15, 15], [10, 10], [14, 14], [9, 9], [11, 11]]) == 318
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,guards = [[0, 0], [19, 19], [0, 19], [19, 0]],walls = [[5, 5], [15, 15], [10, 10], [14, 14], [9, 9], [11, 11]]) == 318: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [6, 6], [7, 7], [8, 8], [9, 9]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [6, 6], [7, 7], [8, 8], [9, 9]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 20,guards = [[2, 2], [5, 5], [8, 8]],walls = [[3, 3], [7, 7], [11, 11], [13, 13]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 20,guards = [[2, 2], [5, 5], [8, 8]],walls = [[3, 3], [7, 7], [11, 11], [13, 13]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(m = 45,n = 45,guards = [[10, 10], [20, 20], [30, 30], [40, 40]],walls = [[12, 12], [18, 18], [22, 22], [28, 28], [32, 32], [38, 38]]) == 1675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 45,n = 45,guards = [[10, 10], [20, 20], [30, 30], [40, 40]],walls = [[12, 12], [18, 18], [22, 22], [28, 28], [32, 32], [38, 38]]) == 1675: {e}')
    
    total += 1
    try:
        result = candidate(m = 18,n = 18,guards = [[9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],walls = [[0, 0], [17, 17], [1, 1], [16, 16], [8, 8], [9, 9]]) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 18,n = 18,guards = [[9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],walls = [[0, 0], [17, 17], [1, 1], [16, 16], [8, 8], [9, 9]]) == 164: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]],walls = [[0, 7], [7, 0], [7, 7], [7, 14], [14, 7]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]],walls = [[0, 7], [7, 0], [7, 7], [7, 14], [14, 7]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 9,guards = [[1, 1], [1, 8], [4, 4], [5, 5]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [5, 7], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 9,guards = [[1, 1], [1, 8], [4, 4], [5, 5]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [5, 7], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 12,guards = [[2, 2], [2, 9], [9, 2], [9, 9], [5, 5]],walls = [[3, 3], [3, 8], [8, 3], [8, 8], [6, 6]]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 12,guards = [[2, 2], [2, 9], [9, 2], [9, 9], [5, 5]],walls = [[3, 3], [3, 8], [8, 3], [8, 8], [6, 6]]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 8,guards = [[2, 1], [5, 3], [8, 5]],walls = [[1, 2], [4, 4], [7, 6], [10, 7]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 8,guards = [[2, 1], [5, 3], [8, 5]],walls = [[1, 2], [4, 4], [7, 6], [10, 7]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,guards = [[1, 1], [1, 7], [7, 1], [7, 7]],walls = [[2, 2], [2, 6], [6, 2], [6, 6], [3, 3], [3, 5], [5, 3], [5, 5]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,guards = [[1, 1], [1, 7], [7, 1], [7, 7]],walls = [[2, 2], [2, 6], [6, 2], [6, 6], [3, 3], [3, 5], [5, 3], [5, 5]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,guards = [[25, 25], [50, 50], [75, 75]],walls = [[10, 10], [20, 20], [30, 30], [40, 40], [55, 55], [60, 60], [65, 65], [70, 70], [80, 80], [90, 90]]) == 9399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,guards = [[25, 25], [50, 50], [75, 75]],walls = [[10, 10], [20, 20], [30, 30], [40, 40], [55, 55], [60, 60], [65, 65], [70, 70], [80, 80], [90, 90]]) == 9399: {e}')
    
    total += 1
    try:
        result = candidate(m = 25,n = 25,guards = [[12, 12], [13, 13], [14, 14]],walls = [[0, 0], [24, 24], [5, 5], [20, 20], [10, 10], [15, 15]]) == 478
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 25,n = 25,guards = [[12, 12], [13, 13], [14, 14]],walls = [[0, 0], [24, 24], [5, 5], [20, 20], [10, 10], [15, 15]]) == 478: {e}')
    
    total += 1
    try:
        result = candidate(m = 11,n = 7,guards = [[3, 1], [6, 4], [8, 6]],walls = [[1, 0], [2, 3], [4, 5], [5, 6], [7, 2]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 11,n = 7,guards = [[3, 1], [6, 4], [8, 6]],walls = [[1, 0], [2, 3], [4, 5], [5, 6], [7, 2]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[3, 3], [3, 6], [6, 3], [6, 6]],walls = [[2, 2], [2, 7], [7, 2], [7, 7], [4, 4], [4, 5], [5, 4], [5, 5]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[3, 3], [3, 6], [6, 3], [6, 6]],walls = [[2, 2], [2, 7], [7, 2], [7, 7], [4, 4], [4, 5], [5, 4], [5, 5]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 12,guards = [[1, 5], [4, 7], [6, 3]],walls = [[0, 3], [3, 5], [5, 8], [7, 10]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 12,guards = [[1, 5], [4, 7], [6, 3]],walls = [[0, 3], [3, 5], [5, 8], [7, 10]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,guards = [[2, 2], [3, 3], [4, 4]],walls = [[1, 1], [5, 5], [6, 6], [7, 7], [0, 0], [1, 6], [6, 1], [5, 7], [7, 5]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,guards = [[2, 2], [3, 3], [4, 4]],walls = [[1, 1], [5, 5], [6, 6], [7, 7], [0, 0], [1, 6], [6, 1], [5, 7], [7, 5]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(m = 16,n = 16,guards = [[8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],walls = [[0, 0], [1, 1], [15, 15], [14, 14], [7, 7], [6, 6]]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 16,n = 16,guards = [[8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],walls = [[0, 0], [1, 1], [15, 15], [14, 14], [7, 7], [6, 6]]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[0, 0], [7, 7], [3, 3], [5, 5], [2, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[0, 0], [7, 7], [3, 3], [5, 5], [2, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[0, 0], [19, 19], [9, 9], [14, 14], [15, 5], [5, 15], [10, 0], [10, 19]]) == 303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[0, 0], [19, 19], [9, 9], [14, 14], [15, 5], [5, 15], [10, 0], [10, 19]]) == 303: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,guards = [[1, 1], [1, 6], [6, 1], [6, 6]],walls = [[2, 3], [2, 5], [5, 2], [5, 5]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,guards = [[1, 1], [1, 6], [6, 1], [6, 6]],walls = [[2, 3], [2, 5], [5, 2], [5, 5]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7,guards = [[1, 1], [1, 5], [5, 1], [5, 5]],walls = [[0, 3], [3, 0], [3, 6], [6, 3]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7,guards = [[1, 1], [1, 5], [5, 1], [5, 5]],walls = [[0, 3], [3, 0], [3, 6], [6, 3]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 5,guards = [[0, 0], [0, 4], [5, 0], [5, 4]],walls = [[1, 2], [2, 2], [3, 2], [4, 2], [6, 2], [7, 2], [8, 2], [9, 2]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 5,guards = [[0, 0], [0, 4], [5, 0], [5, 4]],walls = [[1, 2], [2, 2], [3, 2], [4, 2], [6, 2], [7, 2], [8, 2], [9, 2]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(m = 70,n = 70,guards = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]],walls = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65]]) == 4090
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 70,n = 70,guards = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]],walls = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65]]) == 4090: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],walls = [[1, 1], [1, 9], [9, 1], [9, 9], [0, 0], [0, 9], [9, 0], [5, 1], [5, 9]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],walls = [[1, 1], [1, 9], [9, 1], [9, 9], [0, 0], [0, 9], [9, 0], [5, 1], [5, 9]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 10,guards = [[0, 0], [0, 9], [4, 0], [4, 9]],walls = [[2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 10,guards = [[0, 0], [0, 9], [4, 0], [4, 9]],walls = [[2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[0, 0], [0, 9], [9, 0], [9, 9]],walls = [[2, 2], [2, 7], [7, 2], [7, 7]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[0, 0], [0, 9], [9, 0], [9, 9]],walls = [[2, 2], [2, 7], [7, 2], [7, 7]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7,guards = [[1, 1], [1, 5], [5, 1], [5, 5]],walls = [[2, 2], [2, 5], [5, 2], [5, 5], [3, 3]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7,guards = [[1, 1], [1, 5], [5, 1], [5, 5]],walls = [[2, 2], [2, 5], [5, 2], [5, 5], [3, 3]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [7, 7], [0, 7], [7, 0]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [7, 7], [0, 7], [7, 0]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[1, 1], [8, 8], [9, 9], [0, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[1, 1], [8, 8], [9, 9], [0, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [1, 2], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1], [6, 6]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [1, 2], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1], [6, 6]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [7, 7], [12, 12], [17, 17]]) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [7, 7], [12, 12], [17, 17]]) == 285: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,guards = [[10, 10], [40, 50], [70, 80]],walls = [[15, 15], [30, 30], [60, 60], [85, 85]]) == 9405
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,guards = [[10, 10], [40, 50], [70, 80]],walls = [[15, 15], [30, 30], [60, 60], [85, 85]]) == 9405: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[0, 0], [19, 19], [5, 10], [10, 15], [15, 5], [5, 15], [10, 5]]) == 331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[0, 0], [19, 19], [5, 10], [10, 15], [15, 5], [5, 15], [10, 5]]) == 331: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,guards = [[2, 2], [7, 7], [12, 12]],walls = [[3, 3], [4, 4], [5, 5], [6, 6], [8, 8], [9, 9], [10, 10], [11, 11], [13, 13], [14, 14]]) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,guards = [[2, 2], [7, 7], [12, 12]],walls = [[3, 3], [4, 4], [5, 5], [6, 6], [8, 8], [9, 9], [10, 10], [11, 11], [13, 13], [14, 14]]) == 134: {e}')
    
    total += 1
    try:
        result = candidate(m = 18,n = 10,guards = [[3, 3], [7, 3], [11, 3], [3, 7], [7, 7], [11, 7]],walls = [[2, 2], [2, 8], [8, 2], [8, 8], [5, 5]]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 18,n = 10,guards = [[3, 3], [7, 3], [11, 3], [3, 7], [7, 7], [11, 7]],walls = [[2, 2], [2, 8], [8, 2], [8, 8], [5, 5]]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 5,guards = [[2, 1], [7, 3]],walls = [[1, 1], [1, 3], [3, 1], [3, 3], [5, 1], [5, 3], [8, 1], [8, 3]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 5,guards = [[2, 1], [7, 3]],walls = [[1, 1], [1, 3], [3, 1], [3, 3], [5, 1], [5, 3], [8, 1], [8, 3]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,guards = [[2, 2], [5, 5], [8, 8]],walls = [[3, 3], [6, 6], [9, 9], [4, 4], [7, 7], [10, 10]]) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,guards = [[2, 2], [5, 5], [8, 8]],walls = [[3, 3], [6, 6], [9, 9], [4, 4], [7, 7], [10, 10]]) == 138: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [4, 4], [6, 6], [8, 8], [12, 12], [14, 14], [16, 16], [18, 18]]) == 281
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [4, 4], [6, 6], [8, 8], [12, 12], [14, 14], [16, 16], [18, 18]]) == 281: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7,guards = [[0, 0], [0, 6], [6, 0], [6, 6], [3, 3]],walls = [[1, 1], [1, 5], [5, 1], [5, 5], [2, 2], [2, 4], [4, 2], [4, 4]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7,guards = [[0, 0], [0, 6], [6, 0], [6, 6], [3, 3]],walls = [[1, 1], [1, 5], [5, 1], [5, 5], [2, 2], [2, 4], [4, 2], [4, 4]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,guards = [[1, 1], [1, 7], [7, 1], [7, 7], [3, 3], [3, 4], [4, 3], [4, 4]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,guards = [[1, 1], [1, 7], [7, 1], [7, 7], [3, 3], [3, 4], [4, 3], [4, 4]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7,guards = [[1, 3], [2, 4], [3, 5], [4, 1], [5, 2], [6, 3]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7,guards = [[1, 3], [2, 4], [3, 5], [4, 1], [5, 2], [6, 3]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 10,guards = [[2, 2], [2, 3], [3, 2], [3, 3], [5, 5], [6, 6], [7, 7], [8, 8]],walls = [[1, 1], [1, 2], [1, 3], [1, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 9]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 10,guards = [[2, 2], [2, 3], [3, 2], [3, 3], [5, 5], [6, 6], [7, 7], [8, 8]],walls = [[1, 1], [1, 2], [1, 3], [1, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 9]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 12,guards = [[3, 3], [6, 6], [9, 9]],walls = [[2, 2], [4, 4], [5, 5], [7, 7], [8, 8], [10, 10], [11, 11], [0, 0], [1, 1]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 12,guards = [[3, 3], [6, 6], [9, 9]],walls = [[2, 2], [4, 4], [5, 5], [7, 7], [8, 8], [10, 10], [11, 11], [0, 0], [1, 1]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(m = 14,n = 14,guards = [[2, 2], [2, 11], [11, 2], [11, 11]],walls = [[3, 3], [3, 10], [10, 3], [10, 10], [5, 5], [5, 8], [8, 5], [8, 8]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 14,n = 14,guards = [[2, 2], [2, 11], [11, 2], [11, 11]],walls = [[3, 3], [3, 10], [10, 3], [10, 10], [5, 5], [5, 8], [8, 5], [8, 8]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 12,guards = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],walls = [[0, 0], [11, 11], [10, 10], [9, 9], [8, 8]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 12,guards = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],walls = [[0, 0], [11, 11], [10, 10], [9, 9], [8, 8]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[1, 1], [1, 8], [8, 1], [8, 8], [4, 4]],walls = [[0, 0], [0, 9], [9, 0], [9, 9], [2, 2], [2, 7], [7, 2], [7, 7]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[1, 1], [1, 8], [8, 1], [8, 8], [4, 4]],walls = [[0, 0], [0, 9], [9, 0], [9, 9], [2, 2], [2, 7], [7, 2], [7, 7]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[4, 3], [4, 5], [5, 4], [3, 4]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[4, 3], [4, 5], [5, 4], [3, 4]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,guards = [[2, 3], [4, 5], [6, 7]],walls = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,guards = [[2, 3], [4, 5], [6, 7]],walls = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == 139: {e}')
    
    total += 1
    try:
        result = candidate(m = 80,n = 80,guards = [[10, 10], [30, 30], [50, 50], [70, 70]],walls = [[15, 15], [35, 35], [55, 55], [75, 75]]) == 5772
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 80,n = 80,guards = [[10, 10], [30, 30], [50, 50], [70, 70]],walls = [[15, 15], [35, 35], [55, 55], [75, 75]]) == 5772: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6,guards = [[1, 1], [1, 4], [4, 1], [4, 4]],walls = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6,guards = [[1, 1], [1, 4], [4, 1], [4, 4]],walls = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4]],walls = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4]],walls = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(m = 25,n = 15,guards = [[3, 4], [8, 9], [13, 14], [18, 1], [23, 6]],walls = [[2, 5], [7, 10], [12, 13], [17, 2], [22, 7]]) == 195
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 25,n = 15,guards = [[3, 4], [8, 9], [13, 14], [18, 1], [23, 6]],walls = [[2, 5], [7, 10], [12, 13], [17, 2], [22, 7]]) == 195: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 20,guards = [[5, 5], [7, 7], [10, 10]],walls = [[3, 3], [12, 12], [8, 8], [6, 6]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 20,guards = [[5, 5], [7, 7], [10, 10]],walls = [[3, 3], [12, 12], [8, 8], [6, 6]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [3, 3], [4, 4], [6, 6], [7, 7], [8, 8], [9, 9], [11, 11], [12, 12], [13, 13], [14, 14], [16, 16], [17, 17], [18, 18], [19, 19]]) == 274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [3, 3], [4, 4], [6, 6], [7, 7], [8, 8], [9, 9], [11, 11], [12, 12], [13, 13], [14, 14], [16, 16], [17, 17], [18, 18], [19, 19]]) == 274: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 50,guards = [[10, 10], [20, 20], [30, 30], [40, 40]],walls = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45]]) == 2111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 50,guards = [[10, 10], [20, 20], [30, 30], [40, 40]],walls = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45]]) == 2111: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 5,guards = [[1, 1], [1, 3], [3, 1], [3, 3]],walls = [[0, 0], [0, 4], [4, 0], [4, 4], [2, 2]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 5,guards = [[1, 1], [1, 3], [3, 1], [3, 3]],walls = [[0, 0], [0, 4], [4, 0], [4, 4], [2, 2]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 50,guards = [[25, 25], [25, 26], [24, 25]],walls = [[24, 24], [24, 26], [26, 25], [26, 26]]) == 2421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 50,guards = [[25, 25], [25, 26], [24, 25]],walls = [[24, 24], [24, 26], [26, 25], [26, 26]]) == 2421: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 20,guards = [[2, 2], [5, 5], [7, 7], [10, 10]],walls = [[1, 1], [3, 3], [8, 8], [12, 12], [14, 19]]) == 171
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 20,guards = [[2, 2], [5, 5], [7, 7], [10, 10]],walls = [[1, 1], [3, 3], [8, 8], [12, 12], [14, 19]]) == 171: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 10,guards = [[1, 2], [3, 7]],walls = [[1, 1], [1, 3], [2, 1], [2, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 8], [1, 9], [2, 8], [2, 9], [3, 8], [3, 9], [4, 8], [4, 9]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 10,guards = [[1, 2], [3, 7]],walls = [[1, 1], [1, 3], [2, 1], [2, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 8], [1, 9], [2, 8], [2, 9], [3, 8], [3, 9], [4, 8], [4, 9]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 7,guards = [[1, 1], [5, 5]],walls = [[2, 2], [2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3], [4, 4]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 7,guards = [[1, 1], [5, 5]],walls = [[2, 2], [2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3], [4, 4]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(m = 30,n = 30,guards = [[1, 1], [2, 2], [3, 3], [4, 4]],walls = [[5, 5], [6, 6], [7, 7], [8, 8]]) == 672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30,n = 30,guards = [[1, 1], [2, 2], [3, 3], [4, 4]],walls = [[5, 5], [6, 6], [7, 7], [8, 8]]) == 672: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,guards = [[3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13]],walls = [[1, 1], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14]]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,guards = [[3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13]],walls = [[1, 1], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14]]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],walls = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],walls = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 12,guards = [[3, 3], [4, 4], [5, 5], [6, 6]],walls = [[1, 1], [2, 2], [7, 7], [8, 8], [9, 9], [10, 10]]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 12,guards = [[3, 3], [4, 4], [5, 5], [6, 6]],walls = [[1, 1], [2, 2], [7, 7], [8, 8], [9, 9], [10, 10]]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 6,guards = [[0, 0], [5, 5]],walls = [[1, 1], [1, 4], [2, 2], [2, 3], [3, 2], [3, 3], [4, 1], [4, 4]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 6,guards = [[0, 0], [5, 5]],walls = [[1, 1], [1, 4], [2, 2], [2, 3], [3, 2], [3, 3], [4, 1], [4, 4]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],walls = [[0, 0], [8, 8], [1, 1], [7, 7], [2, 2], [3, 3]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],walls = [[0, 0], [8, 8], [1, 1], [7, 7], [2, 2], [3, 3]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,guards = [[2, 2], [7, 7], [12, 12]],walls = [[0, 0], [5, 5], [10, 10], [14, 14]]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,guards = [[2, 2], [7, 7], [12, 12]],walls = [[0, 0], [5, 5], [10, 10], [14, 14]]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,guards = [[2, 2], [5, 5], [8, 8], [11, 11]],walls = [[3, 3], [6, 6], [9, 9], [12, 12], [0, 0], [14, 14]]) == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,guards = [[2, 2], [5, 5], [8, 8], [11, 11]],walls = [[3, 3], [6, 6], [9, 9], [12, 12], [0, 0], [14, 14]]) == 115: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 10,guards = [[5, 5], [10, 5], [14, 5]],walls = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [11, 5], [12, 5], [13, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 10,guards = [[5, 5], [10, 5], [14, 5]],walls = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [11, 5], [12, 5], [13, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 11,guards = [[1, 3], [4, 6], [6, 8]],walls = [[0, 1], [2, 4], [3, 5], [5, 7], [6, 9]]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 11,guards = [[1, 3], [4, 6], [6, 8]],walls = [[0, 1], [2, 4], [3, 5], [5, 7], [6, 9]]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,guards = [[1, 2], [2, 1], [3, 3], [6, 6], [8, 8]],walls = [[0, 0], [4, 4], [5, 5], [9, 9]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,guards = [[1, 2], [2, 1], [3, 3], [6, 6], [8, 8]],walls = [[0, 0], [4, 4], [5, 5], [9, 9]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[3, 3], [4, 4], [6, 6], [7, 7], [9, 9], [11, 11], [13, 13], [14, 14], [16, 16], [17, 17], [19, 19]]) == 278
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[3, 3], [4, 4], [6, 6], [7, 7], [9, 9], [11, 11], [13, 13], [14, 14], [16, 16], [17, 17], [19, 19]]) == 278: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 4,n = 6,guards = [[0, 0], [1, 1], [2, 3]],walls = [[0, 1], [2, 2], [1, 4]]) == 7
    assert candidate(m = 3,n = 3,guards = [[1, 1]],walls = [[0, 1], [1, 0], [2, 1], [1, 2]]) == 4
    assert candidate(m = 5,n = 5,guards = [[2, 2]],walls = [[0, 0], [4, 4]]) == 14
    assert candidate(m = 10,n = 10,guards = [[3, 3], [6, 6]],walls = [[1, 1], [8, 8]]) == 62
    assert candidate(m = 6,n = 6,guards = [[1, 1], [4, 4]],walls = [[2, 2], [3, 3]]) == 14
    assert candidate(m = 12,n = 12,guards = [[1, 1], [5, 5], [9, 9]],walls = [[2, 2], [6, 6], [10, 10], [3, 3], [7, 7], [11, 11]]) == 75
    assert candidate(m = 10,n = 10,guards = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],walls = [[1, 1]]) == 49
    assert candidate(m = 10,n = 5,guards = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]],walls = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4]]) == 1
    assert candidate(m = 20,n = 10,guards = [[5, 2], [10, 7], [15, 3], [18, 8]],walls = [[0, 5], [4, 9], [9, 4], [14, 8], [19, 3], [7, 0]]) == 104
    assert candidate(m = 15,n = 20,guards = [[2, 5], [4, 8], [10, 15]],walls = [[3, 3], [6, 7], [9, 12], [11, 14]]) == 200
    assert candidate(m = 20,n = 20,guards = [[0, 0], [19, 19], [0, 19], [19, 0]],walls = [[5, 5], [15, 15], [10, 10], [14, 14], [9, 9], [11, 11]]) == 318
    assert candidate(m = 10,n = 10,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [6, 6], [7, 7], [8, 8], [9, 9]]) == 20
    assert candidate(m = 15,n = 20,guards = [[2, 2], [5, 5], [8, 8]],walls = [[3, 3], [7, 7], [11, 11], [13, 13]]) == 200
    assert candidate(m = 45,n = 45,guards = [[10, 10], [20, 20], [30, 30], [40, 40]],walls = [[12, 12], [18, 18], [22, 22], [28, 28], [32, 32], [38, 38]]) == 1675
    assert candidate(m = 18,n = 18,guards = [[9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],walls = [[0, 0], [17, 17], [1, 1], [16, 16], [8, 8], [9, 9]]) == 164
    assert candidate(m = 20,n = 20,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 220
    assert candidate(m = 15,n = 15,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]],walls = [[0, 7], [7, 0], [7, 7], [7, 14], [14, 7]]) == 3
    assert candidate(m = 6,n = 9,guards = [[1, 1], [1, 8], [4, 4], [5, 5]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [5, 7], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8]]) == 8
    assert candidate(m = 12,n = 12,guards = [[2, 2], [2, 9], [9, 2], [9, 9], [5, 5]],walls = [[3, 3], [3, 8], [8, 3], [8, 8], [6, 6]]) == 76
    assert candidate(m = 12,n = 8,guards = [[2, 1], [5, 3], [8, 5]],walls = [[1, 2], [4, 4], [7, 6], [10, 7]]) == 41
    assert candidate(m = 9,n = 9,guards = [[1, 1], [1, 7], [7, 1], [7, 7]],walls = [[2, 2], [2, 6], [6, 2], [6, 6], [3, 3], [3, 5], [5, 3], [5, 5]]) == 41
    assert candidate(m = 100,n = 100,guards = [[25, 25], [50, 50], [75, 75]],walls = [[10, 10], [20, 20], [30, 30], [40, 40], [55, 55], [60, 60], [65, 65], [70, 70], [80, 80], [90, 90]]) == 9399
    assert candidate(m = 25,n = 25,guards = [[12, 12], [13, 13], [14, 14]],walls = [[0, 0], [24, 24], [5, 5], [20, 20], [10, 10], [15, 15]]) == 478
    assert candidate(m = 11,n = 7,guards = [[3, 1], [6, 4], [8, 6]],walls = [[1, 0], [2, 3], [4, 5], [5, 6], [7, 2]]) == 32
    assert candidate(m = 10,n = 10,guards = [[3, 3], [3, 6], [6, 3], [6, 6]],walls = [[2, 2], [2, 7], [7, 2], [7, 7], [4, 4], [4, 5], [5, 4], [5, 5]]) == 56
    assert candidate(m = 8,n = 12,guards = [[1, 5], [4, 7], [6, 3]],walls = [[0, 3], [3, 5], [5, 8], [7, 10]]) == 45
    assert candidate(m = 8,n = 8,guards = [[2, 2], [3, 3], [4, 4]],walls = [[1, 1], [5, 5], [6, 6], [7, 7], [0, 0], [1, 6], [6, 1], [5, 7], [7, 5]]) == 16
    assert candidate(m = 16,n = 16,guards = [[8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]],walls = [[0, 0], [1, 1], [15, 15], [14, 14], [7, 7], [6, 6]]) == 94
    assert candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[0, 0], [7, 7], [3, 3], [5, 5], [2, 2]]) == 0
    assert candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[0, 0], [19, 19], [9, 9], [14, 14], [15, 5], [5, 15], [10, 0], [10, 19]]) == 303
    assert candidate(m = 8,n = 8,guards = [[1, 1], [1, 6], [6, 1], [6, 6]],walls = [[2, 3], [2, 5], [5, 2], [5, 5]]) == 32
    assert candidate(m = 7,n = 7,guards = [[1, 1], [1, 5], [5, 1], [5, 5]],walls = [[0, 3], [3, 0], [3, 6], [6, 3]]) == 21
    assert candidate(m = 10,n = 5,guards = [[0, 0], [0, 4], [5, 0], [5, 4]],walls = [[1, 2], [2, 2], [3, 2], [4, 2], [6, 2], [7, 2], [8, 2], [9, 2]]) == 16
    assert candidate(m = 70,n = 70,guards = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]],walls = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65]]) == 4090
    assert candidate(m = 10,n = 10,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],walls = [[1, 1], [1, 9], [9, 1], [9, 9], [0, 0], [0, 9], [9, 0], [5, 1], [5, 9]]) == 3
    assert candidate(m = 5,n = 10,guards = [[0, 0], [0, 9], [4, 0], [4, 9]],walls = [[2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8]]) == 16
    assert candidate(m = 10,n = 10,guards = [[0, 0], [0, 9], [9, 0], [9, 9]],walls = [[2, 2], [2, 7], [7, 2], [7, 7]]) == 60
    assert candidate(m = 7,n = 7,guards = [[1, 1], [1, 5], [5, 1], [5, 5]],walls = [[2, 2], [2, 5], [5, 2], [5, 5], [3, 3]]) == 23
    assert candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [7, 7], [0, 7], [7, 0]]) == 5
    assert candidate(m = 10,n = 10,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[1, 1], [8, 8], [9, 9], [0, 0]]) == 12
    assert candidate(m = 7,n = 7,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],walls = [[0, 0], [1, 2], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1], [6, 6]]) == 11
    assert candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [7, 7], [12, 12], [17, 17]]) == 285
    assert candidate(m = 100,n = 100,guards = [[10, 10], [40, 50], [70, 80]],walls = [[15, 15], [30, 30], [60, 60], [85, 85]]) == 9405
    assert candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[0, 0], [19, 19], [5, 10], [10, 15], [15, 5], [5, 15], [10, 5]]) == 331
    assert candidate(m = 15,n = 15,guards = [[2, 2], [7, 7], [12, 12]],walls = [[3, 3], [4, 4], [5, 5], [6, 6], [8, 8], [9, 9], [10, 10], [11, 11], [13, 13], [14, 14]]) == 134
    assert candidate(m = 18,n = 10,guards = [[3, 3], [7, 3], [11, 3], [3, 7], [7, 7], [11, 7]],walls = [[2, 2], [2, 8], [8, 2], [8, 8], [5, 5]]) == 115
    assert candidate(m = 10,n = 5,guards = [[2, 1], [7, 3]],walls = [[1, 1], [1, 3], [3, 1], [3, 3], [5, 1], [5, 3], [8, 1], [8, 3]]) == 31
    assert candidate(m = 15,n = 15,guards = [[2, 2], [5, 5], [8, 8]],walls = [[3, 3], [6, 6], [9, 9], [4, 4], [7, 7], [10, 10]]) == 138
    assert candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [4, 4], [6, 6], [8, 8], [12, 12], [14, 14], [16, 16], [18, 18]]) == 281
    assert candidate(m = 7,n = 7,guards = [[0, 0], [0, 6], [6, 0], [6, 6], [3, 3]],walls = [[1, 1], [1, 5], [5, 1], [5, 5], [2, 2], [2, 4], [4, 2], [4, 4]]) == 8
    assert candidate(m = 8,n = 8,guards = [[1, 1], [1, 7], [7, 1], [7, 7], [3, 3], [3, 4], [4, 3], [4, 4]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]) == 12
    assert candidate(m = 7,n = 7,guards = [[1, 3], [2, 4], [3, 5], [4, 1], [5, 2], [6, 3]],walls = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6]]) == 0
    assert candidate(m = 12,n = 10,guards = [[2, 2], [2, 3], [3, 2], [3, 3], [5, 5], [6, 6], [7, 7], [8, 8]],walls = [[1, 1], [1, 2], [1, 3], [1, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 9]]) == 30
    assert candidate(m = 12,n = 12,guards = [[3, 3], [6, 6], [9, 9]],walls = [[2, 2], [4, 4], [5, 5], [7, 7], [8, 8], [10, 10], [11, 11], [0, 0], [1, 1]]) == 72
    assert candidate(m = 14,n = 14,guards = [[2, 2], [2, 11], [11, 2], [11, 11]],walls = [[3, 3], [3, 10], [10, 3], [10, 10], [5, 5], [5, 8], [8, 5], [8, 8]]) == 136
    assert candidate(m = 12,n = 12,guards = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],walls = [[0, 0], [11, 11], [10, 10], [9, 9], [8, 8]]) == 31
    assert candidate(m = 10,n = 10,guards = [[1, 1], [1, 8], [8, 1], [8, 8], [4, 4]],walls = [[0, 0], [0, 9], [9, 0], [9, 9], [2, 2], [2, 7], [7, 2], [7, 7]]) == 41
    assert candidate(m = 9,n = 9,guards = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],walls = [[4, 3], [4, 5], [5, 4], [3, 4]]) == 14
    assert candidate(m = 15,n = 15,guards = [[2, 3], [4, 5], [6, 7]],walls = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == 139
    assert candidate(m = 80,n = 80,guards = [[10, 10], [30, 30], [50, 50], [70, 70]],walls = [[15, 15], [35, 35], [55, 55], [75, 75]]) == 5772
    assert candidate(m = 6,n = 6,guards = [[1, 1], [1, 4], [4, 1], [4, 4]],walls = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3]]) == 10
    assert candidate(m = 8,n = 8,guards = [[1, 1], [2, 2], [3, 3], [4, 4]],walls = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]) == 30
    assert candidate(m = 25,n = 15,guards = [[3, 4], [8, 9], [13, 14], [18, 1], [23, 6]],walls = [[2, 5], [7, 10], [12, 13], [17, 2], [22, 7]]) == 195
    assert candidate(m = 15,n = 20,guards = [[5, 5], [7, 7], [10, 10]],walls = [[3, 3], [12, 12], [8, 8], [6, 6]]) == 200
    assert candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[2, 2], [3, 3], [4, 4], [6, 6], [7, 7], [8, 8], [9, 9], [11, 11], [12, 12], [13, 13], [14, 14], [16, 16], [17, 17], [18, 18], [19, 19]]) == 274
    assert candidate(m = 50,n = 50,guards = [[10, 10], [20, 20], [30, 30], [40, 40]],walls = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45]]) == 2111
    assert candidate(m = 8,n = 5,guards = [[1, 1], [1, 3], [3, 1], [3, 3]],walls = [[0, 0], [0, 4], [4, 0], [4, 4], [2, 2]]) == 13
    assert candidate(m = 50,n = 50,guards = [[25, 25], [25, 26], [24, 25]],walls = [[24, 24], [24, 26], [26, 25], [26, 26]]) == 2421
    assert candidate(m = 15,n = 20,guards = [[2, 2], [5, 5], [7, 7], [10, 10]],walls = [[1, 1], [3, 3], [8, 8], [12, 12], [14, 19]]) == 171
    assert candidate(m = 5,n = 10,guards = [[1, 2], [3, 7]],walls = [[1, 1], [1, 3], [2, 1], [2, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 8], [1, 9], [2, 8], [2, 9], [3, 8], [3, 9], [4, 8], [4, 9]]) == 21
    assert candidate(m = 7,n = 7,guards = [[1, 1], [5, 5]],walls = [[2, 2], [2, 3], [2, 4], [3, 2], [3, 4], [4, 2], [4, 3], [4, 4]]) == 17
    assert candidate(m = 30,n = 30,guards = [[1, 1], [2, 2], [3, 3], [4, 4]],walls = [[5, 5], [6, 6], [7, 7], [8, 8]]) == 672
    assert candidate(m = 15,n = 15,guards = [[3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13]],walls = [[1, 1], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14]]) == 73
    assert candidate(m = 10,n = 10,guards = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],walls = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 28
    assert candidate(m = 12,n = 12,guards = [[3, 3], [4, 4], [5, 5], [6, 6]],walls = [[1, 1], [2, 2], [7, 7], [8, 8], [9, 9], [10, 10]]) == 58
    assert candidate(m = 6,n = 6,guards = [[0, 0], [5, 5]],walls = [[1, 1], [1, 4], [2, 2], [2, 3], [3, 2], [3, 3], [4, 1], [4, 4]]) == 8
    assert candidate(m = 9,n = 9,guards = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],walls = [[0, 0], [8, 8], [1, 1], [7, 7], [2, 2], [3, 3]]) == 12
    assert candidate(m = 15,n = 15,guards = [[2, 2], [7, 7], [12, 12]],walls = [[0, 0], [5, 5], [10, 10], [14, 14]]) == 140
    assert candidate(m = 15,n = 15,guards = [[2, 2], [5, 5], [8, 8], [11, 11]],walls = [[3, 3], [6, 6], [9, 9], [12, 12], [0, 0], [14, 14]]) == 115
    assert candidate(m = 15,n = 10,guards = [[5, 5], [10, 5], [14, 5]],walls = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [11, 5], [12, 5], [13, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 99
    assert candidate(m = 7,n = 11,guards = [[1, 3], [4, 6], [6, 8]],walls = [[0, 1], [2, 4], [3, 5], [5, 7], [6, 9]]) == 29
    assert candidate(m = 10,n = 10,guards = [[1, 2], [2, 1], [3, 3], [6, 6], [8, 8]],walls = [[0, 0], [4, 4], [5, 5], [9, 9]]) == 21
    assert candidate(m = 20,n = 20,guards = [[5, 5], [10, 10], [15, 15]],walls = [[3, 3], [4, 4], [6, 6], [7, 7], [9, 9], [11, 11], [13, 13], [14, 14], [16, 16], [17, 17], [19, 19]]) == 278


