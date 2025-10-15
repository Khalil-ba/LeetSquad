def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(matrix = [[5, 2, 3], [1, 6, 4]],k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 2, 3], [1, 6, 4]],k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[5, 2, 3], [1, 6, 4], [7, 8, 9]],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 2, 3], [1, 6, 4], [7, 8, 9]],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 12, 3], [1, 6, 4], [7, 8, 9]],k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 12, 3], [1, 6, 4], [7, 8, 9]],k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 20], [30, 40]],k = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 20], [30, 40]],k = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0], [0, 0]],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0], [0, 0]],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[5, 2], [1, 6]],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 2], [1, 6]],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[5, 2, 3], [1, 6, 4]],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 2, 3], [1, 6, 4]],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2], [3, 4], [5, 6]],k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2], [3, 4], [5, 6]],k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[5, 2], [1, 6]],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 2], [1, 6]],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[5, 2], [1, 6]],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 2], [1, 6]],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2], [3, 4], [5, 6]],k = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2], [3, 4], [5, 6]],k = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000000, 999999, 999998], [999997, 999996, 999995], [999994, 999993, 999992]],k = 6) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000000, 999999, 999998], [999997, 999996, 999995], [999994, 999993, 999992]],k = 6) == 126: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]],k = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]],k = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[5, 8, 9, 12, 15], [14, 11, 10, 7, 4], [3, 6, 7, 10, 13], [12, 15, 14, 11, 8], [1, 4, 5, 8, 11]],k = 18) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 8, 9, 12, 15], [14, 11, 10, 7, 4], [3, 6, 7, 10, 13], [12, 15, 14, 11, 8], [1, 4, 5, 8, 11]],k = 18) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900], [1000, 1100, 1200]],k = 10) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900], [1000, 1100, 1200]],k = 10) == 172: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20]],k = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20]],k = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[8, 6, 2, 5, 8, 4, 9], [4, 5, 5, 6, 9, 8, 9], [7, 3, 8, 7, 5, 6, 2], [4, 3, 1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 0, 1]],k = 15) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[8, 6, 2, 5, 8, 4, 9], [4, 5, 5, 6, 9, 8, 9], [7, 3, 8, 7, 5, 6, 2], [4, 3, 1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 0, 1]],k = 15) == 11: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9, 11, 13], [15, 17, 19, 21, 23, 25, 27], [29, 31, 33, 35, 37, 39, 41]],k = 12) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9, 11, 13], [15, 17, 19, 21, 23, 25, 27], [29, 31, 33, 35, 37, 39, 41]],k = 12) == 14: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[25, 10, 15, 20], [5, 30, 35, 40], [45, 50, 55, 60], [65, 70, 75, 80]],k = 15) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[25, 10, 15, 20], [5, 30, 35, 40], [45, 50, 55, 60], [65, 70, 75, 80]],k = 15) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 25) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 25) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]],k = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]],k = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5], [3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4], [3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9], [7, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5]],k = 18) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5], [3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4], [3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9], [7, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5]],k = 18) == 9: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[9, 18, 27, 36, 45], [44, 35, 26, 17, 8], [7, 16, 25, 34, 43], [42, 33, 24, 15, 6], [5, 14, 23, 32, 41]],k = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[9, 18, 27, 36, 45], [44, 35, 26, 17, 8], [7, 16, 25, 34, 43], [42, 33, 24, 15, 6], [5, 14, 23, 32, 41]],k = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],k = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],k = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000000, 999999, 999998], [999997, 999996, 999995], [999994, 999993, 999992]],k = 9) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000000, 999999, 999998], [999997, 999996, 999995], [999994, 999993, 999992]],k = 9) == 123: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[5, 2, 15, 6, 3], [10, 1, 4, 7, 8], [3, 1, 9, 2, 12], [6, 14, 11, 13, 5], [1, 15, 8, 6, 7]],k = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 2, 15, 6, 3], [10, 1, 4, 7, 8], [3, 1, 9, 2, 12], [6, 14, 11, 13, 5], [1, 15, 8, 6, 7]],k = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 16) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 16) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]],k = 8) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]],k = 8) == 20: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[7, 1, 4, 2], [9, 6, 3, 8], [5, 0, 10, 12], [15, 11, 14, 13]],k = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[7, 1, 4, 2], [9, 6, 3, 8], [5, 0, 10, 12], [15, 11, 14, 13]],k = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30], [32, 34, 36, 38, 40], [42, 44, 46, 48, 50]],k = 14) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30], [32, 34, 36, 38, 40], [42, 44, 46, 48, 50]],k = 14) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],k = 12) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],k = 12) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[5, 2, 15, 10], [1, 6, 8, 3], [12, 4, 7, 9], [14, 11, 13, 5]],k = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[5, 2, 15, 10], [1, 6, 8, 3], [12, 4, 7, 9], [14, 11, 13, 5]],k = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[8, 12, 7, 3, 15], [9, 6, 11, 14, 4], [13, 8, 2, 5, 9], [1, 10, 7, 12, 8], [6, 4, 14, 3, 13]],k = 13) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[8, 12, 7, 3, 15], [9, 6, 11, 14, 4], [13, 8, 2, 5, 9], [1, 10, 7, 12, 8], [6, 4, 14, 3, 13]],k = 13) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[999999, 999999, 999999], [999999, 999999, 999999], [999999, 999999, 999999]],k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[999999, 999999, 999999], [999999, 999999, 999999], [999999, 999999, 999999]],k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 14) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 14) == 12: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[15, 9, 12, 3], [11, 6, 4, 14], [7, 8, 9, 13], [2, 5, 10, 1]],k = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[15, 9, 12, 3], [11, 6, 4, 14], [7, 8, 9, 13], [2, 5, 10, 1]],k = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],k = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],k = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],k = 12) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],k = 12) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[31, 41, 59, 26, 53], [58, 97, 93, 23, 84], [62, 64, 33, 83, 27], [95, 25, 43, 30, 48], [67, 47, 54, 90, 88]],k = 17) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[31, 41, 59, 26, 53], [58, 97, 93, 23, 84], [62, 64, 33, 83, 27], [95, 25, 43, 30, 48], [67, 47, 54, 90, 88]],k = 17) == 31: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[256, 512, 1024], [128, 256, 512], [64, 128, 256]],k = 5) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[256, 512, 1024], [128, 256, 512], [64, 128, 256]],k = 5) == 640: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[3, 1, 2], [4, 1, 1], [5, 10, 6]],k = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[3, 1, 2], [4, 1, 1], [5, 10, 6]],k = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[3, 6, 9, 12], [4, 7, 10, 13], [5, 8, 11, 14]],k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[3, 6, 9, 12], [4, 7, 10, 13], [5, 8, 11, 14]],k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[3, 8, 1], [9, 11, 13], [4, 7, 12]],k = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[3, 8, 1], [9, 11, 13], [4, 7, 12]],k = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000000, 0, 0, 0, 0, 0, 0], [0, 1000000, 0, 0, 0, 0, 0], [0, 0, 1000000, 0, 0, 0, 0], [0, 0, 0, 1000000, 0, 0, 0], [0, 0, 0, 0, 1000000, 0, 0], [0, 0, 0, 0, 0, 1000000, 0], [0, 0, 0, 0, 0, 0, 1000000]],k = 25) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000000, 0, 0, 0, 0, 0, 0], [0, 1000000, 0, 0, 0, 0, 0], [0, 0, 1000000, 0, 0, 0, 0], [0, 0, 0, 1000000, 0, 0, 0], [0, 0, 0, 0, 1000000, 0, 0], [0, 0, 0, 0, 0, 1000000, 0], [0, 0, 0, 0, 0, 0, 1000000]],k = 25) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]],k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]],k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[9, 8, 7, 6, 5, 4], [3, 2, 1, 0, 9, 8], [7, 6, 5, 4, 3, 2], [1, 0, 9, 8, 7, 6], [5, 4, 3, 2, 1, 0]],k = 30) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[9, 8, 7, 6, 5, 4], [3, 2, 1, 0, 9, 8], [7, 6, 5, 4, 3, 2], [1, 0, 9, 8, 7, 6], [5, 4, 3, 2, 1, 0]],k = 30) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[9, 11, 13, 15, 17, 19, 21], [23, 25, 27, 29, 31, 33, 35], [37, 39, 41, 43, 45, 47, 49]],k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[9, 11, 13, 15, 17, 19, 21], [23, 25, 27, 29, 31, 33, 35], [37, 39, 41, 43, 45, 47, 49]],k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],k = 14) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],k = 14) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000000, 999999, 999998, 999997], [999996, 999995, 999994, 999993], [999992, 999991, 999990, 999989]],k = 6) == 124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000000, 999999, 999998, 999997], [999996, 999995, 999994, 999993], [999992, 999991, 999990, 999989]],k = 6) == 124: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],k = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],k = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]],k = 13) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]],k = 13) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000000, 999999, 999998, 999997, 999996], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],k = 15) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000000, 999999, 999998, 999997, 999996], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],k = 15) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[7, 7, 7], [7, 7, 7], [7, 7, 7]],k = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[7, 7, 7], [7, 7, 7], [7, 7, 7]],k = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],k = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],k = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000000, 999999, 999998, 999997], [999996, 999995, 999994, 999993], [999992, 999991, 999990, 999989], [999988, 999987, 999986, 999985]],k = 10) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000000, 999999, 999998, 999997], [999996, 999995, 999994, 999993], [999992, 999991, 999990, 999989], [999988, 999987, 999986, 999985]],k = 10) == 120: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1000000, 200000, 30000], [4000, 5000, 6000], [70, 80, 900]],k = 8) == 799482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1000000, 200000, 30000], [4000, 5000, 6000], [70, 80, 900]],k = 8) == 799482: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [60, 70, 80, 90, 100], [55, 65, 75, 85, 95]],k = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [60, 70, 80, 90, 100], [55, 65, 75, 85, 95]],k = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]],k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]],k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[2, 4, 6, 8, 10, 12], [14, 16, 18, 20, 22, 24], [26, 28, 30, 32, 34, 36]],k = 17) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[2, 4, 6, 8, 10, 12], [14, 16, 18, 20, 22, 24], [26, 28, 30, 32, 34, 36]],k = 17) == 2: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 0]],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 0]],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[23, 56, 12, 78], [34, 89, 56, 45], [12, 34, 56, 78], [89, 56, 23, 12]],k = 10) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[23, 56, 12, 78], [34, 89, 56, 45], [12, 34, 56, 78], [89, 56, 23, 12]],k = 10) == 47: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],k = 5) == 384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],k = 5) == 384: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [20, 22, 24, 26, 28]],k = 12) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [20, 22, 24, 26, 28]],k = 12) == 7: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 16) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 16) == 0: {e}')
    
    total += 1
    try:
        result = candidate(matrix = [[3, 5, 11, 13], [8, 2, 12, 7], [4, 6, 9, 15], [1, 10, 3, 8]],k = 6) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(matrix = [[3, 5, 11, 13], [8, 2, 12, 7], [4, 6, 9, 15], [1, 10, 3, 8]],k = 6) == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(matrix = [[5, 2, 3], [1, 6, 4]],k = 5) == 4
    assert candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],k = 9) == 0
    assert candidate(matrix = [[5, 2, 3], [1, 6, 4], [7, 8, 9]],k = 9) == 0
    assert candidate(matrix = [[10, 12, 3], [1, 6, 4], [7, 8, 9]],k = 4) == 10
    assert candidate(matrix = [[10, 20], [30, 40]],k = 1) == 40
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],k = 5) == 2
    assert candidate(matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]],k = 4) == 1
    assert candidate(matrix = [[0, 0], [0, 0]],k = 1) == 0
    assert candidate(matrix = [[5, 2], [1, 6]],k = 1) == 7
    assert candidate(matrix = [[5, 2, 3], [1, 6, 4]],k = 1) == 7
    assert candidate(matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],k = 9) == 0
    assert candidate(matrix = [[1, 2], [3, 4], [5, 6]],k = 6) == 1
    assert candidate(matrix = [[5, 2], [1, 6]],k = 3) == 4
    assert candidate(matrix = [[5, 2], [1, 6]],k = 2) == 5
    assert candidate(matrix = [[1, 2], [3, 4], [5, 6]],k = 4) == 3
    assert candidate(matrix = [[1000000, 999999, 999998], [999997, 999996, 999995], [999994, 999993, 999992]],k = 6) == 126
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]],k = 25) == 2
    assert candidate(matrix = [[5, 8, 9, 12, 15], [14, 11, 10, 7, 4], [3, 6, 7, 10, 13], [12, 15, 14, 11, 8], [1, 4, 5, 8, 11]],k = 18) == 5
    assert candidate(matrix = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]],k = 5) == 1
    assert candidate(matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900], [1000, 1100, 1200]],k = 10) == 172
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]],k = 25) == 0
    assert candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],k = 10) == 0
    assert candidate(matrix = [[9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20]],k = 8) == 8
    assert candidate(matrix = [[8, 6, 2, 5, 8, 4, 9], [4, 5, 5, 6, 9, 8, 9], [7, 3, 8, 7, 5, 6, 2], [4, 3, 1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 0, 1]],k = 15) == 11
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 50) == 0
    assert candidate(matrix = [[1, 3, 5, 7, 9, 11, 13], [15, 17, 19, 21, 23, 25, 27], [29, 31, 33, 35, 37, 39, 41]],k = 12) == 14
    assert candidate(matrix = [[25, 10, 15, 20], [5, 30, 35, 40], [45, 50, 55, 60], [65, 70, 75, 80]],k = 15) == 8
    assert candidate(matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],k = 13) == 0
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 25) == 1
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]],k = 30) == 7
    assert candidate(matrix = [[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5], [3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4], [3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9], [7, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5]],k = 18) == 9
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 1) == 0
    assert candidate(matrix = [[9, 18, 27, 36, 45], [44, 35, 26, 17, 8], [7, 16, 25, 34, 43], [42, 33, 24, 15, 6], [5, 14, 23, 32, 41]],k = 20) == 8
    assert candidate(matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],k = 10) == 3
    assert candidate(matrix = [[1000000, 999999, 999998], [999997, 999996, 999995], [999994, 999993, 999992]],k = 9) == 123
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 30) == 0
    assert candidate(matrix = [[5, 2, 15, 6, 3], [10, 1, 4, 7, 8], [3, 1, 9, 2, 12], [6, 14, 11, 13, 5], [1, 15, 8, 6, 7]],k = 20) == 6
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 16) == 0
    assert candidate(matrix = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]],k = 8) == 20
    assert candidate(matrix = [[7, 1, 4, 2], [9, 6, 3, 8], [5, 0, 10, 12], [15, 11, 14, 13]],k = 7) == 8
    assert candidate(matrix = [[2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30], [32, 34, 36, 38, 40], [42, 44, 46, 48, 50]],k = 14) == 8
    assert candidate(matrix = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]],k = 12) == 1
    assert candidate(matrix = [[5, 2, 15, 10], [1, 6, 8, 3], [12, 4, 7, 9], [14, 11, 13, 5]],k = 10) == 6
    assert candidate(matrix = [[8, 12, 7, 3, 15], [9, 6, 11, 14, 4], [13, 8, 2, 5, 9], [1, 10, 7, 12, 8], [6, 4, 14, 3, 13]],k = 13) == 7
    assert candidate(matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],k = 1) == 0
    assert candidate(matrix = [[999999, 999999, 999999], [999999, 999999, 999999], [999999, 999999, 999999]],k = 9) == 0
    assert candidate(matrix = [[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],k = 14) == 12
    assert candidate(matrix = [[15, 9, 12, 3], [11, 6, 4, 14], [7, 8, 9, 13], [2, 5, 10, 1]],k = 7) == 8
    assert candidate(matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],k = 10) == 1
    assert candidate(matrix = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]],k = 10) == 8
    assert candidate(matrix = [[3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]],k = 15) == 0
    assert candidate(matrix = [[1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],k = 12) == 1
    assert candidate(matrix = [[31, 41, 59, 26, 53], [58, 97, 93, 23, 84], [62, 64, 33, 83, 27], [95, 25, 43, 30, 48], [67, 47, 54, 90, 88]],k = 17) == 31
    assert candidate(matrix = [[256, 512, 1024], [128, 256, 512], [64, 128, 256]],k = 5) == 640
    assert candidate(matrix = [[3, 1, 2], [4, 1, 1], [5, 10, 6]],k = 6) == 3
    assert candidate(matrix = [[3, 6, 9, 12], [4, 7, 10, 13], [5, 8, 11, 14]],k = 7) == 5
    assert candidate(matrix = [[3, 8, 1], [9, 11, 13], [4, 7, 12]],k = 6) == 10
    assert candidate(matrix = [[1000000, 0, 0, 0, 0, 0, 0], [0, 1000000, 0, 0, 0, 0, 0], [0, 0, 1000000, 0, 0, 0, 0], [0, 0, 0, 1000000, 0, 0, 0], [0, 0, 0, 0, 1000000, 0, 0], [0, 0, 0, 0, 0, 1000000, 0], [0, 0, 0, 0, 0, 0, 1000000]],k = 25) == 1000000
    assert candidate(matrix = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]],k = 25) == 0
    assert candidate(matrix = [[9, 8, 7, 6, 5, 4], [3, 2, 1, 0, 9, 8], [7, 6, 5, 4, 3, 2], [1, 0, 9, 8, 7, 6], [5, 4, 3, 2, 1, 0]],k = 30) == 0
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 25) == 0
    assert candidate(matrix = [[9, 11, 13, 15, 17, 19, 21], [23, 25, 27, 29, 31, 33, 35], [37, 39, 41, 43, 45, 47, 49]],k = 25) == 0
    assert candidate(matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]],k = 14) == 0
    assert candidate(matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],k = 20) == 1
    assert candidate(matrix = [[1000000, 999999, 999998, 999997], [999996, 999995, 999994, 999993], [999992, 999991, 999990, 999989]],k = 6) == 124
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],k = 1) == 1
    assert candidate(matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],k = 20) == 7
    assert candidate(matrix = [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],k = 15) == 5
    assert candidate(matrix = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12], [5, 7, 9, 11, 13]],k = 13) == 4
    assert candidate(matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],k = 25) == 0
    assert candidate(matrix = [[1000000, 999999, 999998, 999997, 999996], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],k = 15) == 1000000
    assert candidate(matrix = [[7, 7, 7], [7, 7, 7], [7, 7, 7]],k = 4) == 7
    assert candidate(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],k = 1) == 15
    assert candidate(matrix = [[1000000, 999999, 999998, 999997], [999996, 999995, 999994, 999993], [999992, 999991, 999990, 999989], [999988, 999987, 999986, 999985]],k = 10) == 120
    assert candidate(matrix = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],k = 3) == 7
    assert candidate(matrix = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]],k = 10) == 4
    assert candidate(matrix = [[1000000, 200000, 30000], [4000, 5000, 6000], [70, 80, 900]],k = 8) == 799482
    assert candidate(matrix = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [60, 70, 80, 90, 100], [55, 65, 75, 85, 95]],k = 15) == 10
    assert candidate(matrix = [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]],k = 15) == 0
    assert candidate(matrix = [[2, 4, 6, 8, 10, 12], [14, 16, 18, 20, 22, 24], [26, 28, 30, 32, 34, 36]],k = 17) == 2
    assert candidate(matrix = [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 0]],k = 10) == 0
    assert candidate(matrix = [[23, 56, 12, 78], [34, 89, 56, 45], [12, 34, 56, 78], [89, 56, 23, 12]],k = 10) == 47
    assert candidate(matrix = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],k = 25) == 0
    assert candidate(matrix = [[100, 200, 300], [400, 500, 600], [700, 800, 900]],k = 5) == 384
    assert candidate(matrix = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [20, 22, 24, 26, 28]],k = 12) == 7
    assert candidate(matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],k = 16) == 0
    assert candidate(matrix = [[3, 5, 11, 13], [8, 2, 12, 7], [4, 6, 9, 15], [1, 10, 3, 8]],k = 6) == 11


