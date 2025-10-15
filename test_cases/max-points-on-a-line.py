def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [0, 1], [1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [0, 1], [1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 8]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 8]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-4, -4], [-8, -582], [-5, -26], [0, 3], [-1, 1], [0, -7], [1, -1], [5, 5], [-8, -6722], [-6, -576], [-6, -3608]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-4, -4], [-8, -582], [-5, -26], [0, 3], [-1, 1], [0, -7], [1, -1], [5, 5], [-8, -6722], [-6, -576], [-6, -3608]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [2, 2], [3, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [2, 2], [3, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 65536], [65536, 0], [65536, 65536], [0, 65536]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 65536], [65536, 0], [65536, 65536], [0, 65536]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, -1], [2, 2], [2, -2], [3, 3], [3, -3], [4, 4], [4, -4], [5, 5], [5, -5], [6, 6], [6, -6], [7, 7], [7, -7], [8, 8], [8, -8], [9, 9], [9, -9], [10, 10], [10, -10]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, -1], [2, 2], [2, -2], [3, 3], [3, -3], [4, 4], [4, -4], [5, 5], [5, -5], [6, 6], [6, -6], [7, 7], [7, -7], [8, 8], [8, -8], [9, 9], [9, -9], [10, 10], [10, -10]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 65536], [65536, 1], [233, 233], [65536, 233], [233, 65536], [0, 1], [1, 0], [1, 2], [2, 1], [65535, 65535]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 65536], [65536, 1], [233, 233], [65536, 233], [233, 65536], [0, 1], [1, 0], [1, 2], [2, 1], [65535, 65535]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 5], [5, 7], [6, 9], [7, 11], [8, 13], [9, 15]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 5], [5, 7], [6, 9], [7, 11], [8, 13], [9, 15]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 6], [2, 2], [2, 7], [3, 3], [3, 8], [4, 4], [4, 9], [5, 5], [5, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 6], [2, 2], [2, 7], [3, 3], [3, 8], [4, 4], [4, 9], [5, 5], [5, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [1, 15], [2, 14], [3, 13], [4, 12], [5, 11], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6], [11, 5], [12, 4], [13, 3], [14, 2], [15, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [1, 15], [2, 14], [3, 13], [4, 12], [5, 11], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6], [11, 5], [12, 4], [13, 3], [14, 2], [15, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10000, -10000], [10000, 10000], [5000, 5000], [0, 0], [-5000, -5000]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10000, -10000], [10000, 10000], [5000, 5000], [0, 0], [-5000, -5000]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [2, 1], [3, 2], [4, 3], [3, 1], [4, 2], [5, 3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [2, 1], [3, 2], [4, 3], [3, 1], [4, 2], [5, 3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, -10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, -10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -2], [0, -1], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -2], [0, -1], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 4], [5, 5], [6, 6], [7, 8], [9, 9], [10, 10], [11, 12], [13, 13], [14, 14], [15, 16], [17, 17], [18, 18], [19, 20], [21, 21], [22, 22], [23, 24], [25, 25], [26, 26], [27, 28]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 4], [5, 5], [6, 6], [7, 8], [9, 9], [10, 10], [11, 12], [13, 13], [14, 14], [15, 16], [17, 17], [18, 18], [19, 20], [21, 21], [22, 22], [23, 24], [25, 25], [26, 26], [27, 28]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 8], [6, 11], [7, 14], [8, 17]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 8], [6, 11], [7, 14], [8, 17]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 1], [2, 2], [3, 3], [4, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 1], [2, 2], [3, 3], [4, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2], [5, 1], [5, 2], [6, 1], [6, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2], [5, 1], [5, 2], [6, 1], [6, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 4], [2, 6], [2, 8], [3, 3], [3, 6], [3, 9], [3, 12]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 4], [2, 6], [2, 8], [3, 3], [3, 6], [3, 9], [3, 12]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10000, -10000], [10000, 10000], [5000, 5000], [-5000, -5000], [0, 0], [2500, 2500], [-2500, -2500], [7500, 7500], [-7500, -7500], [10000, -10000], [-10000, 10000]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10000, -10000], [10000, 10000], [5000, 5000], [-5000, -5000], [0, 0], [2500, 2500], [-2500, -2500], [7500, 7500], [-7500, -7500], [10000, -10000], [-10000, 10000]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 6], [2, 2], [2, 5], [3, 3], [3, 4], [4, 4], [4, 3], [5, 5], [5, 2], [6, 6], [6, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 6], [2, 2], [2, 5], [3, 3], [3, 4], [4, 4], [4, 3], [5, 5], [5, 2], [6, 6], [6, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16], [1, 17], [1, 18], [1, 19], [1, 20]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16], [1, 17], [1, 18], [1, 19], [1, 20]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 3], [3, 6], [4, 10], [5, 15], [6, 21], [7, 28], [8, 36], [9, 45]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 3], [3, 6], [4, 10], [5, 15], [6, 21], [7, 28], [8, 36], [9, 45]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 2], [3, 3], [4, 4], [5, 5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 2], [3, 3], [4, 4], [5, 5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [3, 1], [4, 1], [5, 1], [2, 2], [3, 2], [4, 2], [5, 2]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [3, 1], [4, 1], [5, 1], [2, 2], [3, 2], [4, 2], [5, 2]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [-1, -1], [2, 2], [-2, -2], [3, 3], [-3, -3], [4, 4], [-4, -4], [5, 5], [-5, -5]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [-1, -1], [2, 2], [-2, -2], [3, 3], [-3, -3], [4, 4], [-4, -4], [5, 5], [-5, -5]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [5, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [5, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 13], [8, 15], [9, 17], [10, 19]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 13], [8, 15], [9, 17], [10, 19]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-100, 100], [0, 0], [100, -100], [50, 50], [75, 25], [25, 75], [0, 100], [100, 0]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-100, 100], [0, 0], [100, -100], [50, 50], [75, 25], [25, 75], [0, 100], [100, 0]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 3], [2, 6], [3, 9], [4, 12], [5, 15]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 3], [2, 6], [3, 9], [4, 12], [5, 15]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19], [20, 20]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19], [20, 20]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [3, 2], [4, 6], [5, 5], [6, 4], [7, 7], [8, 9], [9, 8]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [3, 2], [4, 6], [5, 5], [6, 4], [7, 7], [8, 9], [9, 8]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 3], [3, 4], [4, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 3], [3, 4], [4, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 2], [2, 4], [2, 6], [2, 8], [2, 10]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 2], [2, 4], [2, 6], [2, 8], [2, 10]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9], [-10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9], [-10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [0, 0], [5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [0, 0], [5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10000, 10000], [10000, -10000], [0, 0], [5000, 5000], [-5000, -5000], [2000, 2000], [-2000, -2000], [3000, 3000], [-3000, -3000]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10000, 10000], [10000, -10000], [0, 0], [5000, 5000], [-5000, -5000], [2000, 2000], [-2000, -2000], [3000, 3000], [-3000, -3000]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1000, -1000], [-1000, -999], [-1000, -998], [-1000, -997], [-1000, -996], [-1000, -995], [-1000, -994], [-1000, -993], [-1000, -992], [-1000, -991], [-1000, -990]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1000, -1000], [-1000, -999], [-1000, -998], [-1000, -997], [-1000, -996], [-1000, -995], [-1000, -994], [-1000, -993], [-1000, -992], [-1000, -991], [-1000, -990]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [1, 2], [2, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [1, 2], [2, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3], [3, 4], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3], [3, 4], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [0, 1], [1, 2], [2, 3], [3, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [0, 1], [1, 2], [2, 3], [3, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 6], [5, 5], [6, 8], [7, 7], [8, 10], [9, 9], [10, 12]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 6], [5, 5], [6, 8], [7, 7], [8, 10], [9, 9], [10, 12]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5], [6, 6], [6, 6]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5], [6, 6], [6, 6]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 12]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 12]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [5, 5], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [5, 5], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 6
    assert candidate(points = [[0, 0], [1, 1], [0, 1], [1, 0]]) == 2
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 6
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4]]) == 4
    assert candidate(points = [[1, 1], [2, 2], [2, 3], [3, 2], [3, 3]]) == 3
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 8]]) == 4
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 5
    assert candidate(points = [[-4, -4], [-8, -582], [-5, -26], [0, 3], [-1, 1], [0, -7], [1, -1], [5, 5], [-8, -6722], [-6, -576], [-6, -3608]]) == 2
    assert candidate(points = [[-1, -1], [2, 2], [3, 3]]) == 3
    assert candidate(points = [[1, 1], [1, 1], [1, 1]]) == 3
    assert candidate(points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
    assert candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 6
    assert candidate(points = [[1, 1]]) == 1
    assert candidate(points = [[1, 1], [2, 2], [3, 3]]) == 3
    assert candidate(points = [[0, 0], [1, 65536], [65536, 0], [65536, 65536], [0, 65536]]) == 3
    assert candidate(points = [[0, 0], [1, 1], [1, -1], [2, 2], [2, -2], [3, 3], [3, -3], [4, 4], [4, -4], [5, 5], [5, -5], [6, 6], [6, -6], [7, 7], [7, -7], [8, 8], [8, -8], [9, 9], [9, -9], [10, 10], [10, -10]]) == 11
    assert candidate(points = [[0, 0], [1, 65536], [65536, 1], [233, 233], [65536, 233], [233, 65536], [0, 1], [1, 0], [1, 2], [2, 1], [65535, 65535]]) == 3
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3], [3, 3], [4, 4], [4, 4], [4, 4]]) == 12
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 5], [5, 7], [6, 9], [7, 11], [8, 13], [9, 15]]) == 7
    assert candidate(points = [[1, 1], [1, 6], [2, 2], [2, 7], [3, 3], [3, 8], [4, 4], [4, 9], [5, 5], [5, 10]]) == 5
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [1, 15], [2, 14], [3, 13], [4, 12], [5, 11], [6, 10], [7, 9], [8, 8], [9, 7], [10, 6], [11, 5], [12, 4], [13, 3], [14, 2], [15, 1]]) == 16
    assert candidate(points = [[-10000, -10000], [10000, 10000], [5000, 5000], [0, 0], [-5000, -5000]]) == 5
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]]) == 15
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5], [1, 6], [2, 7], [3, 8], [4, 9]]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 9
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]]) == 10
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 5
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [2, 1], [3, 2], [4, 3], [3, 1], [4, 2], [5, 3]]) == 3
    assert candidate(points = [[-10, -10], [0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]]) == 7
    assert candidate(points = [[-1, -2], [0, -1], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == 9
    assert candidate(points = [[1, 1], [2, 2], [3, 4], [5, 5], [6, 6], [7, 8], [9, 9], [10, 10], [11, 12], [13, 13], [14, 14], [15, 16], [17, 17], [18, 18], [19, 20], [21, 21], [22, 22], [23, 24], [25, 25], [26, 26], [27, 28]]) == 14
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]]) == 5
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 6
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 8
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 8], [6, 11], [7, 14], [8, 17]]) == 5
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 1], [2, 2], [3, 3], [4, 4]]) == 5
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 9
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]) == 3
    assert candidate(points = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2], [5, 1], [5, 2], [6, 1], [6, 2]]) == 6
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 4], [2, 6], [2, 8], [3, 3], [3, 6], [3, 9], [3, 12]]) == 4
    assert candidate(points = [[-10000, -10000], [10000, 10000], [5000, 5000], [-5000, -5000], [0, 0], [2500, 2500], [-2500, -2500], [7500, 7500], [-7500, -7500], [10000, -10000], [-10000, 10000]]) == 9
    assert candidate(points = [[1, 1], [1, 6], [2, 2], [2, 5], [3, 3], [3, 4], [4, 4], [4, 3], [5, 5], [5, 2], [6, 6], [6, 1]]) == 6
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 10
    assert candidate(points = [[1, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]) == 5
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 7
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16], [1, 17], [1, 18], [1, 19], [1, 20]]) == 20
    assert candidate(points = [[0, 0], [1, 1], [2, 3], [3, 6], [4, 10], [5, 15], [6, 21], [7, 28], [8, 36], [9, 45]]) == 2
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 2], [3, 3], [4, 4], [5, 5]]) == 5
    assert candidate(points = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8], [-9, -9]]) == 9
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5]]) == 7
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 8
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [3, 1], [4, 1], [5, 1], [2, 2], [3, 2], [4, 2], [5, 2]]) == 5
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [5, 1], [6, 2], [7, 3], [8, 4], [9, 5]]) == 10
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]) == 4
    assert candidate(points = [[0, 0], [1, 1], [-1, -1], [2, 2], [-2, -2], [3, 3], [-3, -3], [4, 4], [-4, -4], [5, 5], [-5, -5]]) == 11
    assert candidate(points = [[1, 1], [2, 1], [1, 2], [2, 2], [3, 3], [3, 4], [4, 3], [4, 4], [5, 5], [5, 6]]) == 5
    assert candidate(points = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]]) == 9
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16]]) == 15
    assert candidate(points = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 13], [8, 15], [9, 17], [10, 19]]) == 10
    assert candidate(points = [[-100, 100], [0, 0], [100, -100], [50, 50], [75, 25], [25, 75], [0, 100], [100, 0]]) == 5
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 3], [2, 6], [3, 9], [4, 12], [5, 15]]) == 5
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == 11
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19], [20, 20]]) == 20
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 7
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]]) == 11
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 6
    assert candidate(points = [[1, 1], [2, 3], [3, 2], [4, 6], [5, 5], [6, 4], [7, 7], [8, 9], [9, 8]]) == 3
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]) == 10
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 3], [3, 4], [4, 4]]) == 4
    assert candidate(points = [[1, 1], [1, 1], [1, 1], [1, 1], [2, 2], [2, 2], [2, 2], [2, 2], [3, 3], [3, 3]]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10]]) == 8
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]) == 9
    assert candidate(points = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9], [2, 2], [2, 4], [2, 6], [2, 8], [2, 10]]) == 5
    assert candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9], [-10, 10]]) == 10
    assert candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20]]) == 10
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4]]) == 4
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 9
    assert candidate(points = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18]]) == 10
    assert candidate(points = [[-5, -5], [0, 0], [5, 5], [10, 10], [15, 15], [20, 20], [25, 25], [30, 30], [35, 35], [40, 40]]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20]]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 5
    assert candidate(points = [[-10000, 10000], [10000, -10000], [0, 0], [5000, 5000], [-5000, -5000], [2000, 2000], [-2000, -2000], [3000, 3000], [-3000, -3000]]) == 7
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21]]) == 17
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 10
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]) == 3
    assert candidate(points = [[-1000, -1000], [-1000, -999], [-1000, -998], [-1000, -997], [-1000, -996], [-1000, -995], [-1000, -994], [-1000, -993], [-1000, -992], [-1000, -991], [-1000, -990]]) == 11
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [1, 2], [2, 3]]) == 4
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 11
    assert candidate(points = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9]]) == 9
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12]]) == 6
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0]]) == 21
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]) == 10
    assert candidate(points = [[1, 1], [1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3], [3, 4], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 14
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]]) == 5
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 10
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 5], [2, 4], [3, 3], [4, 2], [5, 1]]) == 6
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [0, 1], [1, 2], [2, 3], [3, 4]]) == 4
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]) == 5
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 6], [5, 5], [6, 8], [7, 7], [8, 10], [9, 9], [10, 12]]) == 6
    assert candidate(points = [[1, 1], [1, 1], [2, 2], [2, 2], [3, 3], [3, 3], [4, 4], [4, 4], [5, 5], [5, 5], [6, 6], [6, 6]]) == 12
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17], [18, 18], [19, 19]]) == 20
    assert candidate(points = [[1, 1], [2, 2], [3, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 8
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 12]]) == 6
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]) == 4
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [5, 5], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 10


