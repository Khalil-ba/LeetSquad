def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 1]],topRight = [[3, 3], [4, 4], [6, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 1]],topRight = [[3, 3], [4, 4], [6, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[2, 2], [4, 4], [6, 6]],topRight = [[4, 4], [6, 6], [8, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[2, 2], [4, 4], [6, 6]],topRight = [[4, 4], [6, 6], [8, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [3, 1]],topRight = [[2, 2], [4, 4], [4, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [3, 1]],topRight = [[2, 2], [4, 4], [4, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2]],topRight = [[3, 3], [4, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2]],topRight = [[3, 3], [4, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [5, 5]],topRight = [[2, 2], [4, 4], [6, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [5, 5]],topRight = [[2, 2], [4, 4], [6, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 1]],topRight = [[2, 2], [2, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 1]],topRight = [[2, 2], [2, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 3], [1, 5]],topRight = [[5, 5], [5, 7], [5, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 3], [1, 5]],topRight = [[5, 5], [5, 7], [5, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3]],topRight = [[4, 4], [5, 5], [6, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3]],topRight = [[4, 4], [5, 5], [6, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [1, 2]],topRight = [[3, 3], [4, 4], [3, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [1, 2]],topRight = [[3, 3], [4, 4], [3, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [6, 1], [1, 6], [6, 6]],topRight = [[5, 5], [7, 3], [3, 7], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [6, 1], [1, 6], [6, 6]],topRight = [[5, 5], [7, 3], [3, 7], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[2, 2], [3, 4], [5, 3], [6, 6]],topRight = [[4, 4], [7, 5], [6, 6], [8, 8]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[2, 2], [3, 4], [5, 3], [6, 6]],topRight = [[4, 4], [7, 5], [6, 6], [8, 8]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [3, 1]],topRight = [[3, 3], [5, 5], [5, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [3, 1]],topRight = [[3, 3], [5, 5], [5, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[5, 5], [6, 8], [8, 9], [10, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[5, 5], [6, 8], [8, 9], [10, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 5], [5, 7], [7, 9], [9, 11]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 5], [5, 7], [7, 9], [9, 11]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[2, 2], [3, 3], [5, 5], [7, 7]],topRight = [[4, 4], [6, 6], [8, 8], [10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[2, 2], [3, 3], [5, 5], [7, 7]],topRight = [[4, 4], [6, 6], [8, 8], [10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[2, 2], [2, 2], [2, 2], [2, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[2, 2], [2, 2], [2, 2], [2, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[10, 10], [11, 11], [12, 12], [13, 13]]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[10, 10], [11, 11], [12, 12], [13, 13]]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [5, 5], [10, 10], [15, 15]],topRight = [[4, 4], [8, 8], [13, 13], [18, 18]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [5, 5], [10, 10], [15, 15]],topRight = [[4, 4], [8, 8], [13, 13], [18, 18]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [9, 9], [12, 12]],topRight = [[2, 2], [5, 5], [8, 8], [11, 11], [14, 14]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [9, 9], [12, 12]],topRight = [[2, 2], [5, 5], [8, 8], [11, 11], [14, 14]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7]],topRight = [[5, 5], [6, 8], [7, 10], [8, 12]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7]],topRight = [[5, 5], [6, 8], [7, 10], [8, 12]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [5, 1], [9, 1], [13, 1]],topRight = [[3, 5], [7, 5], [11, 5], [15, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [5, 1], [9, 1], [13, 1]],topRight = [[3, 5], [7, 5], [11, 5], [15, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [5, 5], [9, 9]],topRight = [[3, 3], [7, 7], [11, 11]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [5, 5], [9, 9]],topRight = [[3, 3], [7, 7], [11, 11]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [5, 5], [9, 9], [13, 13]],topRight = [[3, 3], [7, 7], [11, 11], [15, 15]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [5, 5], [9, 9], [13, 13]],topRight = [[3, 3], [7, 7], [11, 11], [15, 15]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [3, 1], [5, 5]],topRight = [[2, 2], [4, 4], [4, 2], [6, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [3, 1], [5, 5]],topRight = [[2, 2], [4, 4], [4, 2], [6, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[5, 5], [5, 7], [5, 9], [5, 11]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[5, 5], [5, 7], [5, 9], [5, 11]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[5, 5], [10, 10], [15, 15], [20, 20]],topRight = [[10, 10], [15, 15], [20, 20], [25, 25]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[5, 5], [10, 10], [15, 15], [20, 20]],topRight = [[10, 10], [15, 15], [20, 20], [25, 25]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 2], [1, 3], [1, 4]],topRight = [[10, 10], [10, 11], [10, 12], [10, 13]]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 2], [1, 3], [1, 4]],topRight = [[10, 10], [10, 11], [10, 12], [10, 13]]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 1], [1, 2], [2, 2]],topRight = [[4, 4], [5, 4], [4, 5], [5, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 1], [1, 2], [2, 2]],topRight = [[4, 4], [5, 4], [4, 5], [5, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9]],topRight = [[5, 5], [5, 7], [5, 9], [5, 11], [5, 13]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9]],topRight = [[5, 5], [5, 7], [5, 9], [5, 11], [5, 13]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[5, 5], [5, 5], [5, 5], [5, 5]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[5, 5], [5, 5], [5, 5], [5, 5]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11]],topRight = [[3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11]],topRight = [[3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 4], [5, 5], [8, 8], [11, 11]],topRight = [[3, 3], [7, 7], [10, 10], [13, 13], [15, 15]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 4], [5, 5], [8, 8], [11, 11]],topRight = [[3, 3], [7, 7], [10, 10], [13, 13], [15, 15]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 2], [5, 4], [7, 6], [9, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 2], [5, 4], [7, 6], [9, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [5, 5]],topRight = [[3, 3], [5, 5], [7, 7]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [5, 5]],topRight = [[3, 3], [5, 5], [7, 7]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [6, 1], [11, 1], [1, 6], [6, 6], [11, 6]],topRight = [[6, 6], [11, 6], [16, 6], [6, 11], [11, 11], [16, 11]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [6, 1], [11, 1], [1, 6], [6, 6], [11, 6]],topRight = [[6, 6], [11, 6], [16, 6], [6, 11], [11, 11], [16, 11]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [10, 10], [20, 20], [30, 30]],topRight = [[5, 5], [15, 15], [25, 25], [35, 35]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [10, 10], [20, 20], [30, 30]],topRight = [[5, 5], [15, 15], [25, 25], [35, 35]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]],topRight = [[2, 2], [3, 2], [4, 2], [5, 2], [6, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]],topRight = [[2, 2], [3, 2], [4, 2], [5, 2], [6, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[7, 2], [7, 4], [7, 6], [7, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[7, 2], [7, 4], [7, 6], [7, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [10, 10], [20, 20], [30, 30]],topRight = [[15, 15], [25, 25], [35, 35], [45, 45]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [10, 10], [20, 20], [30, 30]],topRight = [[15, 15], [25, 25], [35, 35], [45, 45]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [4, 4], [7, 7]],topRight = [[2, 2], [5, 5], [8, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [4, 4], [7, 7]],topRight = [[2, 2], [5, 5], [8, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [10, 10]],topRight = [[4, 4], [7, 7], [11, 11], [15, 15]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [10, 10]],topRight = [[4, 4], [7, 7], [11, 11], [15, 15]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 3], [3, 4], [4, 5], [5, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 3], [3, 4], [4, 5], [5, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [5, 5], [9, 9]],topRight = [[10, 10], [12, 12], [14, 14]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [5, 5], [9, 9]],topRight = [[10, 10], [12, 12], [14, 14]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [5, 7]],topRight = [[3, 3], [4, 5], [6, 7], [8, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [5, 7]],topRight = [[3, 3], [4, 5], [6, 7], [8, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [1, 2], [3, 3]],topRight = [[3, 3], [4, 4], [3, 4], [5, 5]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [1, 2], [3, 3]],topRight = [[3, 3], [4, 4], [3, 4], [5, 5]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7], [8, 9]],topRight = [[2, 2], [5, 6], [7, 8], [9, 10], [11, 12]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7], [8, 9]],topRight = [[2, 2], [5, 6], [7, 8], [9, 10], [11, 12]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [5, 5], [9, 9], [13, 13]],topRight = [[4, 4], [8, 8], [12, 12], [16, 16]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [5, 5], [9, 9], [13, 13]],topRight = [[4, 4], [8, 8], [12, 12], [16, 16]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[3, 3], [3, 5], [3, 7], [3, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[3, 3], [3, 5], [3, 7], [3, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[2, 3], [4, 1], [6, 5], [8, 7]],topRight = [[4, 5], [6, 3], [8, 7], [10, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[2, 3], [4, 1], [6, 5], [8, 7]],topRight = [[4, 5], [6, 3], [8, 7], [10, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[10, 10], [20, 20], [30, 30], [40, 40]],topRight = [[20, 20], [30, 30], [40, 40], [50, 50]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[10, 10], [20, 20], [30, 30], [40, 40]],topRight = [[20, 20], [30, 30], [40, 40], [50, 50]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7]],topRight = [[4, 4], [6, 6], [8, 8], [10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7]],topRight = [[4, 4], [6, 6], [8, 8], [10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 2], [1, 3], [1, 4]],topRight = [[2, 4], [2, 5], [2, 6], [2, 7]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 2], [1, 3], [1, 4]],topRight = [[2, 4], [2, 5], [2, 6], [2, 7]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 1], [1, 3], [3, 3]],topRight = [[4, 2], [6, 2], [4, 6], [6, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 1], [1, 3], [3, 3]],topRight = [[4, 2], [6, 2], [4, 6], [6, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[5, 5], [6, 6], [7, 7], [8, 8]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[5, 5], [6, 6], [7, 7], [8, 8]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [5, 5], [3, 3]],topRight = [[4, 4], [7, 7], [6, 6]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [5, 5], [3, 3]],topRight = [[4, 4], [7, 7], [6, 6]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]],topRight = [[2, 4], [6, 8], [10, 12], [14, 16], [18, 20]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]],topRight = [[2, 4], [6, 8], [10, 12], [14, 16], [18, 20]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[2, 3], [4, 3], [6, 3], [8, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[2, 3], [4, 3], [6, 3], [8, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [10, 10], [15, 15]],topRight = [[2, 2], [3, 3], [12, 12], [16, 16]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [10, 10], [15, 15]],topRight = [[2, 2], [3, 3], [12, 12], [16, 16]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1]],topRight = [[4, 10], [5, 10], [6, 10], [7, 10]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1]],topRight = [[4, 10], [5, 10], [6, 10], [7, 10]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [10, 1], [1, 10], [10, 10]],topRight = [[10, 10], [20, 10], [10, 20], [20, 20]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [10, 1], [1, 10], [10, 10]],topRight = [[10, 10], [20, 10], [10, 20], [20, 20]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[10, 10], [10, 10], [10, 10], [10, 10]]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[10, 10], [10, 10], [10, 10], [10, 10]]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1]],topRight = [[4, 2], [5, 2], [6, 2], [7, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1]],topRight = [[4, 2], [5, 2], [6, 2], [7, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [10, 1], [1, 10], [10, 10]],topRight = [[5, 5], [15, 5], [5, 15], [15, 15]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [10, 1], [1, 10], [10, 10]],topRight = [[5, 5], [15, 5], [5, 15], [15, 15]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[2, 2], [4, 2], [6, 2], [8, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[2, 2], [4, 2], [6, 2], [8, 2]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 2], [2, 1], [2, 2]],topRight = [[3, 3], [3, 4], [4, 3], [4, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 2], [2, 1], [2, 2]],topRight = [[3, 3], [3, 4], [4, 3], [4, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 10], [10, 20], [20, 30]],topRight = [[10, 20], [20, 30], [30, 40]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 10], [10, 20], [20, 30]],topRight = [[10, 20], [20, 30], [30, 40]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2]],topRight = [[3, 3], [3, 4], [4, 3], [4, 4], [5, 3], [5, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2]],topRight = [[3, 3], [3, 4], [4, 3], [4, 4], [5, 3], [5, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9]],topRight = [[4, 5], [6, 8], [8, 11], [10, 13], [12, 15]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9]],topRight = [[4, 5], [6, 8], [8, 11], [10, 13], [12, 15]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [4, 4], [7, 7], [10, 10]],topRight = [[5, 5], [8, 8], [11, 11], [13, 13]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [4, 4], [7, 7], [10, 10]],topRight = [[5, 5], [8, 8], [11, 11], [13, 13]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [4, 4], [7, 7], [10, 10]],topRight = [[3, 3], [6, 6], [9, 9], [12, 12]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [4, 4], [7, 7], [10, 10]],topRight = [[3, 3], [6, 6], [9, 9], [12, 12]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 5], [1, 9], [1, 13]],topRight = [[10, 10], [10, 15], [10, 19], [10, 23]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 5], [1, 9], [1, 13]],topRight = [[10, 10], [10, 15], [10, 19], [10, 23]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [4, 4], [6, 6], [8, 8]],topRight = [[3, 3], [7, 7], [10, 10], [12, 12]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [4, 4], [6, 6], [8, 8]],topRight = [[3, 3], [7, 7], [10, 10], [12, 12]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9]],topRight = [[2, 2], [2, 4], [2, 6], [2, 8], [2, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9]],topRight = [[2, 2], [2, 4], [2, 6], [2, 8], [2, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 2], [4, 4], [6, 6], [8, 8]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 2], [4, 4], [6, 6], [8, 8]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 4], [3, 7], [4, 10], [5, 13]],topRight = [[6, 6], [7, 9], [8, 12], [9, 15], [10, 18]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 4], [3, 7], [4, 10], [5, 13]],topRight = [[6, 6], [7, 9], [8, 12], [9, 15], [10, 18]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[10, 10], [20, 20], [30, 30]],topRight = [[20, 20], [30, 30], [40, 40]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[10, 10], [20, 20], [30, 30]],topRight = [[20, 20], [30, 30], [40, 40]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[2, 2], [5, 5], [8, 8], [11, 11], [14, 14]],topRight = [[4, 4], [7, 7], [10, 10], [13, 13], [16, 16]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[2, 2], [5, 5], [8, 8], [11, 11], [14, 14]],topRight = [[4, 4], [7, 7], [10, 10], [13, 13], [16, 16]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[2, 2], [6, 6], [10, 10], [14, 14]],topRight = [[4, 4], [8, 8], [12, 12], [16, 16]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[2, 2], [6, 6], [10, 10], [14, 14]],topRight = [[4, 4], [8, 8], [12, 12], [16, 16]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [2, 2], [5, 5], [7, 7]],topRight = [[3, 3], [6, 6], [8, 8], [10, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [2, 2], [5, 5], [7, 7]],topRight = [[3, 3], [6, 6], [8, 8], [10, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [1, 5], [5, 1], [5, 5]],topRight = [[5, 5], [5, 9], [9, 5], [9, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [1, 5], [5, 1], [5, 5]],topRight = [[5, 5], [5, 9], [9, 5], [9, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[3, 3], [5, 3], [7, 3], [9, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[3, 3], [5, 3], [7, 3], [9, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 10], [5, 15], [10, 20], [15, 25]],topRight = [[10, 20], [20, 25], [25, 30], [30, 35]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 10], [5, 15], [10, 20], [15, 25]],topRight = [[10, 20], [20, 25], [25, 30], [30, 35]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[6, 6], [7, 7], [8, 8], [9, 9]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[6, 6], [7, 7], [8, 8], [9, 9]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [8, 8]],topRight = [[4, 4], [6, 6], [9, 9], [11, 11]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [8, 8]],topRight = [[4, 4], [6, 6], [9, 9], [11, 11]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 2], [5, 3], [7, 4]],topRight = [[2, 2], [4, 3], [6, 4], [8, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 2], [5, 3], [7, 4]],topRight = [[2, 2], [4, 3], [6, 4], [8, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1], [9, 1]],topRight = [[2, 2], [4, 2], [6, 2], [8, 2], [10, 2]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1], [9, 1]],topRight = [[2, 2], [4, 2], [6, 2], [8, 2], [10, 2]]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 1]],topRight = [[3, 3], [4, 4], [6, 6]]) == 1
    assert candidate(bottomLeft = [[2, 2], [4, 4], [6, 6]],topRight = [[4, 4], [6, 6], [8, 8]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 3], [3, 1]],topRight = [[2, 2], [4, 4], [4, 2]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6]]) == 1
    assert candidate(bottomLeft = [[1, 1], [2, 2]],topRight = [[3, 3], [4, 4]]) == 1
    assert candidate(bottomLeft = [[1, 1], [3, 3], [5, 5]],topRight = [[2, 2], [4, 4], [6, 6]]) == 0
    assert candidate(bottomLeft = [[1, 1], [1, 1]],topRight = [[2, 2], [2, 2]]) == 1
    assert candidate(bottomLeft = [[1, 1], [1, 3], [1, 5]],topRight = [[5, 5], [5, 7], [5, 9]]) == 4
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3]],topRight = [[4, 4], [5, 5], [6, 6]]) == 4
    assert candidate(bottomLeft = [[1, 1], [2, 2], [1, 2]],topRight = [[3, 3], [4, 4], [3, 4]]) == 1
    assert candidate(bottomLeft = [[1, 1], [6, 1], [1, 6], [6, 6]],topRight = [[5, 5], [7, 3], [3, 7], [10, 10]]) == 0
    assert candidate(bottomLeft = [[2, 2], [3, 4], [5, 3], [6, 6]],topRight = [[4, 4], [7, 5], [6, 6], [8, 8]]) == 1
    assert candidate(bottomLeft = [[1, 1], [3, 3], [3, 1]],topRight = [[3, 3], [5, 5], [5, 3]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[5, 5], [6, 8], [8, 9], [10, 10]]) == 4
    assert candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 5], [5, 7], [7, 9], [9, 11]]) == 1
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]]) == 9
    assert candidate(bottomLeft = [[2, 2], [3, 3], [5, 5], [7, 7]],topRight = [[4, 4], [6, 6], [8, 8], [10, 10]]) == 1
    assert candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[2, 2], [2, 2], [2, 2], [2, 2]]) == 1
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[10, 10], [11, 11], [12, 12], [13, 13]]) == 64
    assert candidate(bottomLeft = [[1, 1], [5, 5], [10, 10], [15, 15]],topRight = [[4, 4], [8, 8], [13, 13], [18, 18]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [9, 9], [12, 12]],topRight = [[2, 2], [5, 5], [8, 8], [11, 11], [14, 14]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7]],topRight = [[5, 5], [6, 8], [7, 10], [8, 12]]) == 9
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 9
    assert candidate(bottomLeft = [[1, 1], [5, 1], [9, 1], [13, 1]],topRight = [[3, 5], [7, 5], [11, 5], [15, 5]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 4
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 4
    assert candidate(bottomLeft = [[1, 1], [5, 5], [9, 9]],topRight = [[3, 3], [7, 7], [11, 11]]) == 0
    assert candidate(bottomLeft = [[1, 1], [5, 5], [9, 9], [13, 13]],topRight = [[3, 3], [7, 7], [11, 11], [15, 15]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 3], [3, 1], [5, 5]],topRight = [[2, 2], [4, 4], [4, 2], [6, 6]]) == 0
    assert candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[5, 5], [5, 7], [5, 9], [5, 11]]) == 4
    assert candidate(bottomLeft = [[5, 5], [10, 10], [15, 15], [20, 20]],topRight = [[10, 10], [15, 15], [20, 20], [25, 25]]) == 0
    assert candidate(bottomLeft = [[1, 1], [1, 2], [1, 3], [1, 4]],topRight = [[10, 10], [10, 11], [10, 12], [10, 13]]) == 64
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 4
    assert candidate(bottomLeft = [[1, 1], [2, 1], [1, 2], [2, 2]],topRight = [[4, 4], [5, 4], [4, 5], [5, 5]]) == 4
    assert candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9]],topRight = [[5, 5], [5, 7], [5, 9], [5, 11], [5, 13]]) == 4
    assert candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[5, 5], [5, 5], [5, 5], [5, 5]]) == 16
    assert candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11]],topRight = [[3, 5], [5, 7], [7, 9], [9, 11], [11, 13], [13, 15]]) == 4
    assert candidate(bottomLeft = [[1, 1], [2, 4], [5, 5], [8, 8], [11, 11]],topRight = [[3, 3], [7, 7], [10, 10], [13, 13], [15, 15]]) == 4
    assert candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 2], [5, 4], [7, 6], [9, 8]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 3], [5, 5]],topRight = [[3, 3], [5, 5], [7, 7]]) == 0
    assert candidate(bottomLeft = [[1, 1], [6, 1], [11, 1], [1, 6], [6, 6], [11, 6]],topRight = [[6, 6], [11, 6], [16, 6], [6, 11], [11, 11], [16, 11]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]) == 0
    assert candidate(bottomLeft = [[1, 1], [10, 10], [20, 20], [30, 30]],topRight = [[5, 5], [15, 15], [25, 25], [35, 35]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]],topRight = [[2, 2], [3, 2], [4, 2], [5, 2], [6, 2]]) == 0
    assert candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[7, 2], [7, 4], [7, 6], [7, 8]]) == 0
    assert candidate(bottomLeft = [[1, 1], [10, 10], [20, 20], [30, 30]],topRight = [[15, 15], [25, 25], [35, 35], [45, 45]]) == 25
    assert candidate(bottomLeft = [[1, 1], [4, 4], [7, 7]],topRight = [[2, 2], [5, 5], [8, 8]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [10, 10]],topRight = [[4, 4], [7, 7], [11, 11], [15, 15]]) == 1
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 3], [3, 4], [4, 5], [5, 6]]) == 0
    assert candidate(bottomLeft = [[1, 1], [5, 5], [9, 9]],topRight = [[10, 10], [12, 12], [14, 14]]) == 25
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 16
    assert candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [5, 7]],topRight = [[3, 3], [4, 5], [6, 7], [8, 9]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [1, 2], [3, 3]],topRight = [[3, 3], [4, 4], [3, 4], [5, 5]]) == 1
    assert candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7], [8, 9]],topRight = [[2, 2], [5, 6], [7, 8], [9, 10], [11, 12]]) == 1
    assert candidate(bottomLeft = [[1, 1], [5, 5], [9, 9], [13, 13]],topRight = [[4, 4], [8, 8], [12, 12], [16, 16]]) == 0
    assert candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7]],topRight = [[3, 3], [3, 5], [3, 7], [3, 9]]) == 0
    assert candidate(bottomLeft = [[2, 3], [4, 1], [6, 5], [8, 7]],topRight = [[4, 5], [6, 3], [8, 7], [10, 9]]) == 0
    assert candidate(bottomLeft = [[10, 10], [20, 20], [30, 30], [40, 40]],topRight = [[20, 20], [30, 30], [40, 40], [50, 50]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7]],topRight = [[4, 4], [6, 6], [8, 8], [10, 10]]) == 1
    assert candidate(bottomLeft = [[1, 1], [1, 2], [1, 3], [1, 4]],topRight = [[2, 4], [2, 5], [2, 6], [2, 7]]) == 1
    assert candidate(bottomLeft = [[1, 1], [3, 1], [1, 3], [3, 3]],topRight = [[4, 2], [6, 2], [4, 6], [6, 6]]) == 1
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[2, 2], [3, 3], [4, 4], [5, 5]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4]],topRight = [[5, 5], [6, 6], [7, 7], [8, 8]]) == 9
    assert candidate(bottomLeft = [[1, 1], [5, 5], [3, 3]],topRight = [[4, 4], [7, 7], [6, 6]]) == 1
    assert candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]],topRight = [[2, 4], [6, 8], [10, 12], [14, 16], [18, 20]]) == 25
    assert candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[2, 3], [4, 3], [6, 3], [8, 3]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [10, 10], [15, 15]],topRight = [[2, 2], [3, 3], [12, 12], [16, 16]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1]],topRight = [[4, 10], [5, 10], [6, 10], [7, 10]]) == 4
    assert candidate(bottomLeft = [[1, 1], [10, 1], [1, 10], [10, 10]],topRight = [[10, 10], [20, 10], [10, 20], [20, 20]]) == 0
    assert candidate(bottomLeft = [[1, 1], [1, 1], [1, 1], [1, 1]],topRight = [[10, 10], [10, 10], [10, 10], [10, 10]]) == 81
    assert candidate(bottomLeft = [[1, 1], [2, 1], [3, 1], [4, 1]],topRight = [[4, 2], [5, 2], [6, 2], [7, 2]]) == 1
    assert candidate(bottomLeft = [[1, 1], [10, 1], [1, 10], [10, 10]],topRight = [[5, 5], [15, 5], [5, 15], [15, 15]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[2, 2], [4, 2], [6, 2], [8, 2]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 1
    assert candidate(bottomLeft = [[1, 1], [1, 2], [2, 1], [2, 2]],topRight = [[3, 3], [3, 4], [4, 3], [4, 4]]) == 1
    assert candidate(bottomLeft = [[1, 10], [10, 20], [20, 30]],topRight = [[10, 20], [20, 30], [30, 40]]) == 0
    assert candidate(bottomLeft = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2]],topRight = [[3, 3], [3, 4], [4, 3], [4, 4], [5, 3], [5, 4]]) == 1
    assert candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9]],topRight = [[4, 5], [6, 8], [8, 11], [10, 13], [12, 15]]) == 16
    assert candidate(bottomLeft = [[1, 1], [4, 4], [7, 7], [10, 10]],topRight = [[5, 5], [8, 8], [11, 11], [13, 13]]) == 1
    assert candidate(bottomLeft = [[1, 1], [2, 3], [3, 5], [4, 7]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8]]) == 0
    assert candidate(bottomLeft = [[1, 1], [4, 4], [7, 7], [10, 10]],topRight = [[3, 3], [6, 6], [9, 9], [12, 12]]) == 0
    assert candidate(bottomLeft = [[1, 1], [1, 5], [1, 9], [1, 13]],topRight = [[10, 10], [10, 15], [10, 19], [10, 23]]) == 36
    assert candidate(bottomLeft = [[1, 1], [4, 4], [6, 6], [8, 8]],topRight = [[3, 3], [7, 7], [10, 10], [12, 12]]) == 4
    assert candidate(bottomLeft = [[1, 1], [1, 3], [1, 5], [1, 7], [1, 9]],topRight = [[2, 2], [2, 4], [2, 6], [2, 8], [2, 10]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 3], [4, 5], [6, 7]],topRight = [[3, 2], [4, 4], [6, 6], [8, 8]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 4], [3, 7], [4, 10], [5, 13]],topRight = [[6, 6], [7, 9], [8, 12], [9, 15], [10, 18]]) == 4
    assert candidate(bottomLeft = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11]],topRight = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12]]) == 0
    assert candidate(bottomLeft = [[10, 10], [20, 20], [30, 30]],topRight = [[20, 20], [30, 30], [40, 40]]) == 0
    assert candidate(bottomLeft = [[2, 2], [5, 5], [8, 8], [11, 11], [14, 14]],topRight = [[4, 4], [7, 7], [10, 10], [13, 13], [16, 16]]) == 0
    assert candidate(bottomLeft = [[2, 2], [6, 6], [10, 10], [14, 14]],topRight = [[4, 4], [8, 8], [12, 12], [16, 16]]) == 0
    assert candidate(bottomLeft = [[2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[3, 3], [4, 4], [5, 5], [6, 6]]) == 0
    assert candidate(bottomLeft = [[1, 1], [2, 2], [5, 5], [7, 7]],topRight = [[3, 3], [6, 6], [8, 8], [10, 10]]) == 1
    assert candidate(bottomLeft = [[1, 1], [1, 5], [5, 1], [5, 5]],topRight = [[5, 5], [5, 9], [9, 5], [9, 9]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1]],topRight = [[3, 3], [5, 3], [7, 3], [9, 3]]) == 0
    assert candidate(bottomLeft = [[1, 10], [5, 15], [10, 20], [15, 25]],topRight = [[10, 20], [20, 25], [25, 30], [30, 35]]) == 25
    assert candidate(bottomLeft = [[2, 2], [3, 3], [4, 4], [5, 5]],topRight = [[6, 6], [7, 7], [8, 8], [9, 9]]) == 9
    assert candidate(bottomLeft = [[1, 1], [3, 3], [6, 6], [8, 8]],topRight = [[4, 4], [6, 6], [9, 9], [11, 11]]) == 1
    assert candidate(bottomLeft = [[1, 1], [3, 2], [5, 3], [7, 4]],topRight = [[2, 2], [4, 3], [6, 4], [8, 5]]) == 0
    assert candidate(bottomLeft = [[1, 1], [3, 1], [5, 1], [7, 1], [9, 1]],topRight = [[2, 2], [4, 2], [6, 2], [8, 2], [10, 2]]) == 0


