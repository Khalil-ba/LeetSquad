def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 6) == [[1, 2, 3, 4, 5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 6) == [[1, 2, 3, 4, 5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4]],r = 1,c = 4) == [[1, 2, 3, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4]],r = 1,c = 4) == [[1, 2, 3, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 2) == [[1, 2], [3, 4], [5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 2) == [[1, 2], [3, 4], [5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 1) == [[1, 2, 3], [4, 5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 1) == [[1, 2, 3], [4, 5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 3) == [[1, 2, 3], [4, 5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 3) == [[1, 2, 3], [4, 5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 3) == [[1, 2, 3], [4, 5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 3) == [[1, 2, 3], [4, 5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 1) == [[1, 2, 3], [4, 5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 1) == [[1, 2, 3], [4, 5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 1,c = 9) == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 1,c = 9) == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 1,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 1,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4]],r = 2,c = 2) == [[1, 2], [3, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4]],r = 2,c = 2) == [[1, 2], [3, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4]],r = 2,c = 4) == [[1, 2], [3, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4]],r = 2,c = 4) == [[1, 2], [3, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 4,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 4,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 8,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 8,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 9,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 9,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 2,c = 2) == [[1, 2, 3], [4, 5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 2,c = 2) == [[1, 2, 3], [4, 5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 6,c = 1) == [[1], [2], [3], [4], [5], [6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 6,c = 1) == [[1], [2], [3], [4], [5], [6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 3,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 3,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4]],r = 4,c = 1) == [[1], [2], [3], [4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4]],r = 4,c = 1) == [[1], [2], [3], [4]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 2,c = 3) == [[1, 2, 3], [4, 5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 2,c = 3) == [[1, 2, 3], [4, 5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]],r = 2,c = 6) == [[10, 20, 30, 40, 50, 60], [70, 80, 90, 100, 110, 120]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]],r = 2,c = 6) == [[10, 20, 30, 40, 50, 60], [70, 80, 90, 100, 110, 120]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 20,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 20,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[5, 6, 7], [8, 9, 10]],r = 6,c = 1) == [[5], [6], [7], [8], [9], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[5, 6, 7], [8, 9, 10]],r = 6,c = 1) == [[5], [6], [7], [8], [9], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 12,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 12,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 20,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 20,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 8,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 8,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 12,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 12,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]],r = 1,c = 16) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]],r = 1,c = 16) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 4,c = 1) == [[1, 2, 3, 4], [5, 6, 7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 4,c = 1) == [[1, 2, 3, 4], [5, 6, 7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],r = 9,c = 1) == [[10], [20], [30], [40], [50], [60], [70], [80], [90]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],r = 9,c = 1) == [[10], [20], [30], [40], [50], [60], [70], [80], [90]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],r = 2,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],r = 2,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 18,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 18,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 16,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 16,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 8) == [[1, 2], [3, 4], [5, 6], [7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 8) == [[1, 2], [3, 4], [5, 6], [7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 4,c = 2) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 4,c = 2) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1000, -1000, 500], [-500, 1000, -1000], [0, 0, 0]],r = 3,c = 3) == [[1000, -1000, 500], [-500, 1000, -1000], [0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1000, -1000, 500], [-500, 1000, -1000], [0, 0, 0]],r = 3,c = 3) == [[1000, -1000, 500], [-500, 1000, -1000], [0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]],r = 3,c = 3) == [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]],r = 3,c = 3) == [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 1,c = 20) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 1,c = 20) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4]],r = 4,c = 1) == [[1], [2], [3], [4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4]],r = 4,c = 1) == [[1], [2], [3], [4]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 1,c = 15) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 1,c = 15) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 3,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 3,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],r = 9,c = 1) == [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],r = 9,c = 1) == [[0], [0], [0], [0], [0], [0], [0], [0], [0]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 6,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 6,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 1,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 1,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 8,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 8,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],r = 1,c = 9) == [[-1, -2, -3, -4, -5, -6, -7, -8, -9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],r = 1,c = 9) == [[-1, -2, -3, -4, -5, -6, -7, -8, -9]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 2,c = 5) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 2,c = 5) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 3,c = 7) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 3,c = 7) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 8,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 8,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 2,c = 5) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 2,c = 5) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 9,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 9,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 1,c = 15) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 1,c = 15) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 4,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 4,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 15,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 15,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12]],r = 2,c = 6) == [[-1, 2, -3, 4, -5, 6], [-7, 8, -9, 10, -11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12]],r = 2,c = 6) == [[-1, 2, -3, 4, -5, 6], [-7, 8, -9, 10, -11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],r = 3,c = 3) == [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],r = 3,c = 3) == [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 1,c = 18) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 1,c = 18) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 2,c = 10) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 2,c = 10) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 1,c = 12) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 1,c = 12) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 5,c = 2) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 5,c = 2) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 15,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 15,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 4,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 4,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6]],r = 3,c = 2) == [[1, 2], [3, 4], [5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6]],r = 3,c = 2) == [[1, 2], [3, 4], [5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],r = 4,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],r = 4,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],r = 2,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],r = 2,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 2,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 2,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],r = 10,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],r = 10,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 1,c = 19) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 1,c = 19) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],r = 5,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],r = 5,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 4,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 4,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 2,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 2,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2], [3, 4], [5, 6]],r = 1,c = 3) == [[1, 2], [3, 4], [5, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2], [3, 4], [5, 6]],r = 1,c = 3) == [[1, 2], [3, 4], [5, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 2,c = 9) == [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 2,c = 9) == [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 1,c = 12) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 1,c = 12) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 5,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 5,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],r = 16,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],r = 16,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 1,c = 16) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 1,c = 16) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 1,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 1,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 3,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 3,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 3,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 3,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(mat = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]],r = 5,c = 3) == [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(mat = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]],r = 5,c = 3) == [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150]]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 6) == [[1, 2, 3, 4, 5, 6]]
    assert candidate(mat = [[1, 2], [3, 4]],r = 1,c = 4) == [[1, 2, 3, 4]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 2) == [[1, 2], [3, 4], [5, 6]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 1) == [[1, 2, 3], [4, 5, 6]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 3) == [[1, 2, 3], [4, 5, 6]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 3,c = 3) == [[1, 2, 3], [4, 5, 6]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 1,c = 1) == [[1, 2, 3], [4, 5, 6]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 1,c = 9) == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 1,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8]]
    assert candidate(mat = [[1, 2], [3, 4]],r = 2,c = 2) == [[1, 2], [3, 4]]
    assert candidate(mat = [[1, 2], [3, 4]],r = 2,c = 4) == [[1, 2], [3, 4]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 4,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 8,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 9,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 2,c = 2) == [[1, 2, 3], [4, 5, 6]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 6,c = 1) == [[1], [2], [3], [4], [5], [6]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 3,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert candidate(mat = [[1, 2], [3, 4]],r = 4,c = 1) == [[1], [2], [3], [4]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6]],r = 2,c = 3) == [[1, 2, 3], [4, 5, 6]]
    assert candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]],r = 2,c = 6) == [[10, 20, 30, 40, 50, 60], [70, 80, 90, 100, 110, 120]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 20,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
    assert candidate(mat = [[5, 6, 7], [8, 9, 10]],r = 6,c = 1) == [[5], [6], [7], [8], [9], [10]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 12,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 20,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 8,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 12,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]],r = 1,c = 16) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8]],r = 4,c = 1) == [[1, 2, 3, 4], [5, 6, 7, 8]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    assert candidate(mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]],r = 9,c = 1) == [[10], [20], [30], [40], [50], [60], [70], [80], [90]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],r = 2,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 18,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 16,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 8) == [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 4,c = 2) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    assert candidate(mat = [[1000, -1000, 500], [-500, 1000, -1000], [0, 0, 0]],r = 3,c = 3) == [[1000, -1000, 500], [-500, 1000, -1000], [0, 0, 0]]
    assert candidate(mat = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]],r = 3,c = 3) == [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 1,c = 20) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
    assert candidate(mat = [[1, 2], [3, 4]],r = 4,c = 1) == [[1], [2], [3], [4]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 1,c = 15) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 3,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    assert candidate(mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]],r = 9,c = 1) == [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 6,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 1,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8]]
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 8,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    assert candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],r = 1,c = 9) == [[-1, -2, -3, -4, -5, -6, -7, -8, -9]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 2,c = 5) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 3,c = 7) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    assert candidate(mat = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]],r = 6,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 8,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 5,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 2,c = 5) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 9,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]]
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 1,c = 15) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 2,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 4,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8]],r = 4,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],r = 15,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]],r = 3,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert candidate(mat = [[-1, 2, -3, 4], [-5, 6, -7, 8], [-9, 10, -11, 12]],r = 2,c = 6) == [[-1, 2, -3, 4, -5, 6], [-7, 8, -9, 10, -11, 12]]
    assert candidate(mat = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],r = 3,c = 3) == [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 1,c = 18) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 2,c = 10) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],r = 1,c = 12) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 5,c = 2) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 15,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 4,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6]],r = 3,c = 2) == [[1, 2], [3, 4], [5, 6]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],r = 4,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],r = 2,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 2,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],r = 10,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],r = 1,c = 19) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],r = 5,c = 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 4,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 2,c = 8) == [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    assert candidate(mat = [[1, 2], [3, 4], [5, 6]],r = 1,c = 3) == [[1, 2], [3, 4], [5, 6]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 2,c = 9) == [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],r = 1,c = 12) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
    assert candidate(mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],r = 5,c = 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],r = 16,c = 1) == [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16]]
    assert candidate(mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],r = 1,c = 16) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],r = 1,c = 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert candidate(mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],r = 3,c = 6) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
    assert candidate(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]],r = 3,c = 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    assert candidate(mat = [[10, 20, 30, 40, 50], [60, 70, 80, 90, 100], [110, 120, 130, 140, 150]],r = 5,c = 3) == [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120], [130, 140, 150]]


