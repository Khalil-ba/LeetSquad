def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 0, 0, 0], [0, 10, 0, 0], [0, 0, 10, 0], [0, 0, 0, 10]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 0, 0, 0], [0, 10, 0, 0], [0, 0, 10, 0], [0, 0, 0, 10]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 3, 3, 2], [4, 4, 4, 4], [3, 4, 5, 4], [2, 3, 4, 5]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 3, 3, 2], [4, 4, 4, 4], [3, 4, 5, 4], [2, 3, 4, 5]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 3, 7, 8], [4, 4, 6, 6], [1, 2, 3, 4], [8, 7, 5, 3]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 3, 7, 8], [4, 4, 6, 6], [1, 2, 3, 4], [8, 7, 5, 3]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2], [3, 4]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2], [3, 4]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[50, 0, 0], [0, 0, 0], [0, 0, 50]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[50, 0, 0], [0, 0, 0], [0, 0, 50]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[50, 50], [50, 50]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[50, 50], [50, 50]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 6, 2, 5, 3, 4], [4, 3, 5, 2, 6, 1], [2, 4, 6, 1, 5, 3], [3, 1, 4, 6, 1, 2]]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 6, 2, 5, 3, 4], [4, 3, 5, 2, 6, 1], [2, 4, 6, 1, 5, 3], [3, 1, 4, 6, 1, 2]]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 9, 9, 9, 9], [9, 0, 0, 0, 9], [9, 0, 1, 0, 9], [9, 0, 0, 0, 9], [9, 9, 9, 9, 9]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 9, 9, 9, 9], [9, 0, 0, 0, 9], [9, 0, 1, 0, 9], [9, 0, 0, 0, 9], [9, 9, 9, 9, 9]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 20, 30], [30, 20, 10], [10, 30, 20], [20, 10, 30]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 20, 30], [30, 20, 10], [10, 30, 20], [20, 10, 30]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 1], [1, 6, 5, 4, 3, 2], [3, 2, 1, 6, 5, 4], [4, 5, 6, 1, 2, 3]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 1], [1, 6, 5, 4, 3, 2], [3, 2, 1, 6, 5, 4], [4, 5, 6, 1, 2, 3]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 0, 8, 6, 8], [5, 9, 3, 6, 4], [6, 4, 1, 3, 9], [7, 8, 9, 1, 6], [3, 5, 2, 4, 8]]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 0, 8, 6, 8], [5, 9, 3, 6, 4], [6, 4, 1, 3, 9], [7, 8, 9, 1, 6], [3, 5, 2, 4, 8]]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 3, 4, 5, 1], [1, 2, 3, 4, 5], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [3, 4, 5, 1, 2]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 3, 4, 5, 1], [1, 2, 3, 4, 5], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [3, 4, 5, 1, 2]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[8, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11]]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[8, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11]]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 5, 2, 0, 4], [8, 3, 10, 10, 10], [9, 5, 3, 10, 6], [2, 6, 6, 9, 4], [3, 2, 3, 4, 2]]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 5, 2, 0, 4], [8, 3, 10, 10, 10], [9, 5, 3, 10, 6], [2, 6, 6, 9, 4], [3, 2, 3, 4, 2]]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 15, 7, 12, 8], [3, 18, 6, 9, 5], [14, 1, 17, 11, 10], [13, 16, 4, 2, 19], [1, 20, 16, 2, 0]]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 15, 7, 12, 8], [3, 18, 6, 9, 5], [14, 1, 17, 11, 10], [13, 16, 4, 2, 19], [1, 20, 16, 2, 0]]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 10, 10, 10], [10, 0, 0, 10], [10, 0, 0, 10], [10, 10, 10, 10]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 10, 10, 10], [10, 0, 0, 10], [10, 0, 0, 10], [10, 10, 10, 10]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 6, 3, 8, 7, 2], [5, 4, 1, 10, 6, 1], [3, 9, 3, 2, 7, 2], [8, 1, 9, 1, 1, 1], [2, 3, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 6, 3, 8, 7, 2], [5, 4, 1, 10, 6, 1], [3, 9, 3, 2, 7, 2], [8, 1, 9, 1, 1, 1], [2, 3, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[20, 10, 30, 50, 40], [30, 20, 40, 60, 50], [10, 30, 50, 70, 60], [40, 50, 70, 90, 80], [50, 60, 80, 100, 90]]) == 330
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[20, 10, 30, 50, 40], [30, 20, 40, 60, 50], [10, 30, 50, 70, 60], [40, 50, 70, 90, 80], [50, 60, 80, 100, 90]]) == 330: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 15, 20, 25, 30, 35], [35, 30, 25, 20, 15, 10], [10, 35, 15, 30, 20, 25], [25, 20, 30, 15, 35, 10], [30, 10, 20, 35, 15, 25], [15, 25, 35, 10, 20, 30]]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 15, 20, 25, 30, 35], [35, 30, 25, 20, 15, 10], [10, 35, 15, 30, 20, 25], [25, 20, 30, 15, 35, 10], [30, 10, 20, 35, 15, 25], [15, 25, 35, 10, 20, 30]]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 8, 8, 8, 3], [8, 4, 4, 4, 8], [8, 4, 4, 4, 8], [8, 4, 4, 4, 8], [3, 8, 8, 8, 3]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 8, 8, 8, 3], [8, 4, 4, 4, 8], [8, 4, 4, 4, 8], [8, 4, 4, 4, 8], [3, 8, 8, 8, 3]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 1, 9, 1, 5], [1, 1, 1, 1, 1], [9, 1, 9, 1, 9], [1, 1, 1, 1, 1], [5, 1, 9, 1, 5]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 1, 9, 1, 5], [1, 1, 1, 1, 1], [9, 1, 9, 1, 9], [1, 1, 1, 1, 1], [5, 1, 9, 1, 5]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 8, 4, 6, 2], [6, 3, 1, 7, 3], [7, 1, 4, 2, 8], [2, 8, 3, 7, 4], [1, 6, 2, 5, 9]]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 8, 4, 6, 2], [6, 3, 1, 7, 3], [7, 1, 4, 2, 8], [2, 8, 3, 7, 4], [1, 6, 2, 5, 9]]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[40, 10, 50, 20, 30], [10, 20, 30, 40, 50], [50, 30, 20, 10, 40], [20, 40, 10, 30, 50], [30, 50, 40, 20, 10]]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[40, 10, 50, 20, 30], [10, 20, 30, 40, 50], [50, 30, 20, 10, 40], [20, 40, 10, 30, 50], [30, 50, 40, 20, 10]]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 5, 5, 5, 5, 5, 5], [5, 0, 0, 0, 0, 0, 5], [5, 0, 5, 5, 5, 0, 5], [5, 0, 5, 0, 5, 0, 5], [5, 0, 5, 5, 5, 0, 5], [5, 0, 0, 0, 0, 0, 5], [5, 5, 5, 5, 5, 5, 5]]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 5, 5, 5, 5, 5, 5], [5, 0, 0, 0, 0, 0, 5], [5, 0, 5, 5, 5, 0, 5], [5, 0, 5, 0, 5, 0, 5], [5, 0, 5, 5, 5, 0, 5], [5, 0, 0, 0, 0, 0, 5], [5, 5, 5, 5, 5, 5, 5]]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 0, 0, 2, 2], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [2, 0, 0, 2, 2], [2, 2, 2, 2, 2]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 0, 0, 2, 2], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [2, 0, 0, 2, 2], [2, 2, 2, 2, 2]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 0, 10, 15, 20], [15, 20, 5, 0, 10], [0, 10, 15, 20, 5], [20, 5, 0, 10, 15], [10, 15, 20, 5, 0]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 0, 10, 15, 20], [15, 20, 5, 0, 10], [0, 10, 15, 20, 5], [20, 5, 0, 10, 15], [10, 15, 20, 5, 0]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0, 0, 1], [0, 2, 0, 0, 0, 2, 0], [0, 0, 3, 0, 3, 0, 0], [0, 0, 0, 4, 0, 0, 0], [0, 0, 3, 0, 3, 0, 0], [0, 2, 0, 0, 0, 2, 0], [1, 0, 0, 0, 0, 0, 1]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0, 0, 1], [0, 2, 0, 0, 0, 2, 0], [0, 0, 3, 0, 3, 0, 0], [0, 0, 0, 4, 0, 0, 0], [0, 0, 3, 0, 3, 0, 0], [0, 2, 0, 0, 0, 2, 0], [1, 0, 0, 0, 0, 0, 1]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 8, 4, 0, 0, 0], [4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 8, 4, 0, 0, 0], [4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 0], [2, 3, 4, 5, 0, 1], [3, 4, 5, 0, 1, 2], [4, 5, 0, 1, 2, 3], [5, 0, 1, 2, 3, 4]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 0], [2, 3, 4, 5, 0, 1], [3, 4, 5, 0, 1, 2], [4, 5, 0, 1, 2, 3], [5, 0, 1, 2, 3, 4]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 5, 7, 2, 8], [1, 3, 6, 4, 5], [8, 4, 1, 9, 2], [3, 8, 6, 7, 1], [2, 6, 5, 4, 3]]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 5, 7, 2, 8], [1, 3, 6, 4, 5], [8, 4, 1, 9, 2], [3, 8, 6, 7, 1], [2, 6, 5, 4, 3]]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[30, 0, 9, 20, 40], [15, 25, 10, 35, 20], [20, 15, 5, 45, 30], [30, 40, 25, 10, 5], [5, 30, 35, 20, 45]]) == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[30, 0, 9, 20, 40], [15, 25, 10, 35, 20], [20, 15, 5, 45, 30], [30, 40, 25, 10, 5], [5, 30, 35, 20, 45]]) == 366: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 1, 0, 0, 1], [0, 3, 0, 0, 0, 0, 3, 0], [0, 0, 5, 0, 0, 5, 0, 0], [0, 0, 0, 7, 7, 0, 0, 0], [0, 0, 0, 7, 7, 0, 0, 0], [0, 0, 5, 0, 0, 5, 0, 0], [0, 3, 0, 0, 0, 0, 3, 0], [1, 0, 0, 1, 0, 0, 0, 1]]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 1, 0, 0, 1], [0, 3, 0, 0, 0, 0, 3, 0], [0, 0, 5, 0, 0, 5, 0, 0], [0, 0, 0, 7, 7, 0, 0, 0], [0, 0, 0, 7, 7, 0, 0, 0], [0, 0, 5, 0, 0, 5, 0, 0], [0, 3, 0, 0, 0, 0, 3, 0], [1, 0, 0, 1, 0, 0, 0, 1]]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 2, 3, 4, 5], [1, 6, 7, 8, 9], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [9, 8, 7, 6, 10]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 2, 3, 4, 5], [1, 6, 7, 8, 9], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [9, 8, 7, 6, 10]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [1, 1, 1, 1, 1]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [1, 1, 1, 1, 1]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[15, 0, 0, 0, 10], [5, 0, 0, 0, 5], [10, 0, 0, 0, 5], [5, 0, 0, 0, 10], [10, 0, 0, 0, 15]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[15, 0, 0, 0, 10], [5, 0, 0, 0, 5], [10, 0, 0, 0, 5], [5, 0, 0, 0, 10], [10, 0, 0, 0, 15]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 20, 30, 40, 50], [40, 30, 20, 10, 0], [50, 40, 30, 20, 10], [0, 10, 20, 30, 40], [5, 15, 25, 35, 45]]) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 20, 30, 40, 50], [40, 30, 20, 10, 0], [50, 40, 30, 20, 10], [0, 10, 20, 30, 40], [5, 15, 25, 35, 45]]) == 375: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 20, 30, 40, 50], [9, 19, 29, 39, 49], [8, 18, 28, 38, 48], [7, 17, 27, 37, 47], [6, 16, 26, 36, 46]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 20, 30, 40, 50], [9, 19, 29, 39, 49], [8, 18, 28, 38, 48], [7, 17, 27, 37, 47], [6, 16, 26, 36, 46]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 100, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0], [0, 0, 0, 100, 0, 0, 0], [0, 0, 0, 0, 100, 0, 0], [0, 0, 0, 0, 0, 100, 0], [0, 0, 0, 0, 0, 0, 100]]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 100, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0], [0, 0, 0, 100, 0, 0, 0], [0, 0, 0, 0, 100, 0, 0], [0, 0, 0, 0, 0, 100, 0], [0, 0, 0, 0, 0, 0, 100]]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 8, 4, 10], [2, 4, 5, 7, 1], [9, 2, 6, 3, 8], [0, 3, 1, 0, 9], [5, 5, 5, 5, 5]]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 8, 4, 10], [2, 4, 5, 7, 1], [9, 2, 6, 3, 8], [0, 3, 1, 0, 9], [5, 5, 5, 5, 5]]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[8, 2, 5, 9], [7, 5, 8, 8], [9, 8, 7, 6], [2, 8, 5, 9]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[8, 2, 5, 9], [7, 5, 8, 8], [9, 8, 7, 6], [2, 8, 5, 9]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[20, 10, 0, 10, 20], [10, 20, 30, 20, 10], [0, 30, 40, 30, 0], [10, 20, 30, 20, 10], [20, 10, 0, 10, 20]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[20, 10, 0, 10, 20], [10, 20, 30, 20, 10], [0, 30, 40, 30, 0], [10, 20, 30, 20, 10], [20, 10, 0, 10, 20]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [3, 4, 5, 6, 7]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [3, 4, 5, 6, 7]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[7, 0, 1, 2, 5], [4, 0, 0, 0, 0], [6, 0, 0, 0, 0], [0, 0, 1, 0, 0], [5, 0, 5, 0, 5]]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[7, 0, 1, 2, 5], [4, 0, 0, 0, 0], [6, 0, 0, 0, 0], [0, 0, 1, 0, 0], [5, 0, 5, 0, 5]]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 2, 7, 4], [4, 0, 9, 6], [3, 6, 1, 8], [9, 5, 4, 2]]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 2, 7, 4], [4, 0, 9, 6], [3, 6, 1, 8], [9, 5, 4, 2]]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 1, 4, 1, 5, 9], [2, 6, 5, 3, 5, 9], [5, 0, 5, 0, 5, 0], [2, 6, 5, 3, 5, 9], [5, 0, 5, 0, 5, 0], [3, 1, 4, 1, 5, 9]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 1, 4, 1, 5, 9], [2, 6, 5, 3, 5, 9], [5, 0, 5, 0, 5, 0], [2, 6, 5, 3, 5, 9], [5, 0, 5, 0, 5, 0], [3, 1, 4, 1, 5, 9]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 8, 7, 6, 5, 4], [8, 9, 6, 7, 5, 4], [7, 6, 9, 8, 4, 5], [6, 7, 8, 9, 5, 4], [5, 4, 7, 6, 9, 8], [4, 5, 6, 7, 8, 9]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 8, 7, 6, 5, 4], [8, 9, 6, 7, 5, 4], [7, 6, 9, 8, 4, 5], [6, 7, 8, 9, 5, 4], [5, 4, 7, 6, 9, 8], [4, 5, 6, 7, 8, 9]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 8, 7, 6], [6, 5, 4, 3], [3, 4, 5, 6], [7, 8, 9, 10]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 8, 7, 6], [6, 5, 4, 3], [3, 4, 5, 6], [7, 8, 9, 10]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 4, 8, 7, 10], [3, 5, 6, 4, 9], [7, 1, 2, 8, 3], [6, 5, 4, 2, 1], [8, 6, 7, 3, 5]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 4, 8, 7, 10], [3, 5, 6, 4, 9], [7, 1, 2, 8, 3], [6, 5, 4, 2, 1], [8, 6, 7, 3, 5]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12], [12, 10, 8, 6, 4, 2]]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12], [12, 10, 8, 6, 4, 2]]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 3, 3, 3, 3], [3, 3, 3, 3, 5], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 5, 3, 3, 3]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 3, 3, 3, 3], [3, 3, 3, 3, 5], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 5, 3, 3, 3]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 10, 0, 10], [10, 0, 10, 0], [0, 10, 0, 10], [10, 0, 10, 0]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 10, 0, 10], [10, 0, 10, 0], [0, 10, 0, 10], [10, 0, 10, 0]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 10, 10, 1], [1, 1, 1, 10], [10, 1, 1, 1], [1, 10, 1, 10]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 10, 10, 1], [1, 1, 1, 10], [10, 1, 1, 1], [1, 10, 1, 10]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[30, 10, 20, 40, 50], [25, 35, 15, 45, 55], [60, 50, 40, 30, 20], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45]]) == 385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[30, 10, 20, 40, 50], [25, 35, 15, 45, 55], [60, 50, 40, 30, 20], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45]]) == 385: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 9, 9, 9], [9, 0, 0, 9], [9, 0, 0, 9], [9, 9, 9, 9]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 9, 9, 9], [9, 0, 0, 9], [9, 0, 0, 9], [9, 9, 9, 9]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[20, 0, 15, 10, 25], [5, 10, 8, 12, 18], [0, 5, 0, 5, 0], [15, 12, 8, 6, 14], [25, 18, 14, 10, 9]]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[20, 0, 15, 10, 25], [5, 10, 8, 12, 18], [0, 5, 0, 5, 0], [15, 12, 8, 6, 14], [25, 18, 14, 10, 9]]) == 104: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0
    assert candidate(grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]) == 35
    assert candidate(grid = [[10, 0, 0, 0], [0, 10, 0, 0], [0, 0, 10, 0], [0, 0, 0, 10]]) == 120
    assert candidate(grid = [[5, 3, 3, 2], [4, 4, 4, 4], [3, 4, 5, 4], [2, 3, 4, 5]]) == 14
    assert candidate(grid = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 0
    assert candidate(grid = [[5, 3, 7, 8], [4, 4, 6, 6], [1, 2, 3, 4], [8, 7, 5, 3]]) == 24
    assert candidate(grid = [[1, 2], [3, 4]]) == 1
    assert candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 6
    assert candidate(grid = [[50, 0, 0], [0, 0, 0], [0, 0, 50]]) == 100
    assert candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
    assert candidate(grid = [[50, 50], [50, 50]]) == 0
    assert candidate(grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 4
    assert candidate(grid = [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]) == 18
    assert candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 6, 2, 5, 3, 4], [4, 3, 5, 2, 6, 1], [2, 4, 6, 1, 5, 3], [3, 1, 4, 6, 1, 2]]) == 94
    assert candidate(grid = [[9, 9, 9, 9, 9], [9, 0, 0, 0, 9], [9, 0, 1, 0, 9], [9, 0, 0, 0, 9], [9, 9, 9, 9, 9]]) == 80
    assert candidate(grid = [[10, 20, 30], [30, 20, 10], [10, 30, 20], [20, 10, 30]]) == 120
    assert candidate(grid = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]]) == 55
    assert candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 6, 1], [1, 6, 5, 4, 3, 2], [3, 2, 1, 6, 5, 4], [4, 5, 6, 1, 2, 3]]) == 90
    assert candidate(grid = [[2, 0, 8, 6, 8], [5, 9, 3, 6, 4], [6, 4, 1, 3, 9], [7, 8, 9, 1, 6], [3, 5, 2, 4, 8]]) == 67
    assert candidate(grid = [[2, 3, 4, 5, 1], [1, 2, 3, 4, 5], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [3, 4, 5, 1, 2]]) == 50
    assert candidate(grid = [[8, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11]]) == 42
    assert candidate(grid = [[10, 5, 2, 0, 4], [8, 3, 10, 10, 10], [9, 5, 3, 10, 6], [2, 6, 6, 9, 4], [3, 2, 3, 4, 2]]) == 64
    assert candidate(grid = [[10, 15, 7, 12, 8], [3, 18, 6, 9, 5], [14, 1, 17, 11, 10], [13, 16, 4, 2, 19], [1, 20, 16, 2, 0]]) == 151
    assert candidate(grid = [[10, 10, 10, 10], [10, 0, 0, 10], [10, 0, 0, 10], [10, 10, 10, 10]]) == 40
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]) == 2
    assert candidate(grid = [[9, 6, 3, 8, 7, 2], [5, 4, 1, 10, 6, 1], [3, 9, 3, 2, 7, 2], [8, 1, 9, 1, 1, 1], [2, 3, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2]]) == 80
    assert candidate(grid = [[20, 10, 30, 50, 40], [30, 20, 40, 60, 50], [10, 30, 50, 70, 60], [40, 50, 70, 90, 80], [50, 60, 80, 100, 90]]) == 330
    assert candidate(grid = [[10, 15, 20, 25, 30, 35], [35, 30, 25, 20, 15, 10], [10, 35, 15, 30, 20, 25], [25, 20, 30, 15, 35, 10], [30, 10, 20, 35, 15, 25], [15, 25, 35, 10, 20, 30]]) == 450
    assert candidate(grid = [[3, 8, 8, 8, 3], [8, 4, 4, 4, 8], [8, 4, 4, 4, 8], [8, 4, 4, 4, 8], [3, 8, 8, 8, 3]]) == 56
    assert candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]) == 54
    assert candidate(grid = [[5, 1, 9, 1, 5], [1, 1, 1, 1, 1], [9, 1, 9, 1, 9], [1, 1, 1, 1, 1], [5, 1, 9, 1, 5]]) == 16
    assert candidate(grid = [[2, 8, 4, 6, 2], [6, 3, 1, 7, 3], [7, 1, 4, 2, 8], [2, 8, 3, 7, 4], [1, 6, 2, 5, 9]]) == 58
    assert candidate(grid = [[40, 10, 50, 20, 30], [10, 20, 30, 40, 50], [50, 30, 20, 10, 40], [20, 40, 10, 30, 50], [30, 50, 40, 20, 10]]) == 450
    assert candidate(grid = [[5, 5, 5, 5, 5, 5, 5], [5, 0, 0, 0, 0, 0, 5], [5, 0, 5, 5, 5, 0, 5], [5, 0, 5, 0, 5, 0, 5], [5, 0, 5, 5, 5, 0, 5], [5, 0, 0, 0, 0, 0, 5], [5, 5, 5, 5, 5, 5, 5]]) == 85
    assert candidate(grid = [[2, 0, 0, 2, 2], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [2, 0, 0, 2, 2], [2, 2, 2, 2, 2]]) == 14
    assert candidate(grid = [[5, 0, 10, 15, 20], [15, 20, 5, 0, 10], [0, 10, 15, 20, 5], [20, 5, 0, 10, 15], [10, 15, 20, 5, 0]]) == 250
    assert candidate(grid = [[1, 0, 0, 0, 0, 0, 1], [0, 2, 0, 0, 0, 2, 0], [0, 0, 3, 0, 3, 0, 0], [0, 0, 0, 4, 0, 0, 0], [0, 0, 3, 0, 3, 0, 0], [0, 2, 0, 0, 0, 2, 0], [1, 0, 0, 0, 0, 0, 1]]) == 56
    assert candidate(grid = [[2, 8, 4, 0, 0, 0], [4, 4, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 14
    assert candidate(grid = [[0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 0], [2, 3, 4, 5, 0, 1], [3, 4, 5, 0, 1, 2], [4, 5, 0, 1, 2, 3], [5, 0, 1, 2, 3, 4]]) == 90
    assert candidate(grid = [[9, 5, 7, 2, 8], [1, 3, 6, 4, 5], [8, 4, 1, 9, 2], [3, 8, 6, 7, 1], [2, 6, 5, 4, 3]]) == 62
    assert candidate(grid = [[30, 0, 9, 20, 40], [15, 25, 10, 35, 20], [20, 15, 5, 45, 30], [30, 40, 25, 10, 5], [5, 30, 35, 20, 45]]) == 366
    assert candidate(grid = [[1, 0, 0, 0, 1, 0, 0, 1], [0, 3, 0, 0, 0, 0, 3, 0], [0, 0, 5, 0, 0, 5, 0, 0], [0, 0, 0, 7, 7, 0, 0, 0], [0, 0, 0, 7, 7, 0, 0, 0], [0, 0, 5, 0, 0, 5, 0, 0], [0, 3, 0, 0, 0, 0, 3, 0], [1, 0, 0, 1, 0, 0, 0, 1]]) == 110
    assert candidate(grid = [[10, 2, 3, 4, 5], [1, 6, 7, 8, 9], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [9, 8, 7, 6, 10]]) == 52
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [1, 1, 1, 1, 1]]) == 32
    assert candidate(grid = [[15, 0, 0, 0, 10], [5, 0, 0, 0, 5], [10, 0, 0, 0, 5], [5, 0, 0, 0, 10], [10, 0, 0, 0, 15]]) == 20
    assert candidate(grid = [[10, 20, 30, 40, 50], [40, 30, 20, 10, 0], [50, 40, 30, 20, 10], [0, 10, 20, 30, 40], [5, 15, 25, 35, 45]]) == 375
    assert candidate(grid = [[10, 20, 30, 40, 50], [9, 19, 29, 39, 49], [8, 18, 28, 38, 48], [7, 17, 27, 37, 47], [6, 16, 26, 36, 46]]) == 40
    assert candidate(grid = [[0, 0, 0, 0, 0, 0, 0], [0, 100, 0, 0, 0, 0, 0], [0, 0, 100, 0, 0, 0, 0], [0, 0, 0, 100, 0, 0, 0], [0, 0, 0, 0, 100, 0, 0], [0, 0, 0, 0, 0, 100, 0], [0, 0, 0, 0, 0, 0, 100]]) == 3000
    assert candidate(grid = [[1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1]]) == 0
    assert candidate(grid = [[3, 0, 8, 4, 10], [2, 4, 5, 7, 1], [9, 2, 6, 3, 8], [0, 3, 1, 0, 9], [5, 5, 5, 5, 5]]) == 63
    assert candidate(grid = [[8, 2, 5, 9], [7, 5, 8, 8], [9, 8, 7, 6], [2, 8, 5, 9]]) == 28
    assert candidate(grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]]) == 180
    assert candidate(grid = [[3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3]]) == 0
    assert candidate(grid = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]) == 90
    assert candidate(grid = [[20, 10, 0, 10, 20], [10, 20, 30, 20, 10], [0, 30, 40, 30, 0], [10, 20, 30, 20, 10], [20, 10, 0, 10, 20]]) == 200
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [3, 4, 5, 6, 7]]) == 40
    assert candidate(grid = [[7, 0, 1, 2, 5], [4, 0, 0, 0, 0], [6, 0, 0, 0, 0], [0, 0, 1, 0, 0], [5, 0, 5, 0, 5]]) == 31
    assert candidate(grid = [[5, 2, 7, 4], [4, 0, 9, 6], [3, 6, 1, 8], [9, 5, 4, 2]]) == 46
    assert candidate(grid = [[3, 1, 4, 1, 5, 9], [2, 6, 5, 3, 5, 9], [5, 0, 5, 0, 5, 0], [2, 6, 5, 3, 5, 9], [5, 0, 5, 0, 5, 0], [3, 1, 4, 1, 5, 9]]) == 52
    assert candidate(grid = [[9, 8, 7, 6, 5, 4], [8, 9, 6, 7, 5, 4], [7, 6, 9, 8, 4, 5], [6, 7, 8, 9, 5, 4], [5, 4, 7, 6, 9, 8], [4, 5, 6, 7, 8, 9]]) == 90
    assert candidate(grid = [[9, 8, 7, 6], [6, 5, 4, 3], [3, 4, 5, 6], [7, 8, 9, 10]]) == 19
    assert candidate(grid = [[9, 4, 8, 7, 10], [3, 5, 6, 4, 9], [7, 1, 2, 8, 3], [6, 5, 4, 2, 1], [8, 6, 7, 3, 5]]) == 54
    assert candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12], [12, 10, 8, 6, 4, 2]]) == 110
    assert candidate(grid = [[5, 3, 3, 3, 3], [3, 3, 3, 3, 5], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 5, 3, 3, 3]]) == 12
    assert candidate(grid = [[0, 10, 0, 10], [10, 0, 10, 0], [0, 10, 0, 10], [10, 0, 10, 0]]) == 80
    assert candidate(grid = [[1, 10, 10, 1], [1, 1, 1, 10], [10, 1, 1, 1], [1, 10, 1, 10]]) == 90
    assert candidate(grid = [[30, 10, 20, 40, 50], [25, 35, 15, 45, 55], [60, 50, 40, 30, 20], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45]]) == 385
    assert candidate(grid = [[9, 9, 9, 9], [9, 0, 0, 9], [9, 0, 0, 9], [9, 9, 9, 9]]) == 36
    assert candidate(grid = [[20, 0, 15, 10, 25], [5, 10, 8, 12, 18], [0, 5, 0, 5, 0], [15, 12, 8, 6, 14], [25, 18, 14, 10, 9]]) == 104


