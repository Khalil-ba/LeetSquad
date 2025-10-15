def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2], [3, 4]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2], [3, 4]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0], [0, 2]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0], [0, 2]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 2, 1], [2, 1, 0, 2], [1, 0, 2, 1], [2, 1, 0, 2]]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 2, 1], [2, 1, 0, 2], [1, 0, 2, 1], [2, 1, 0, 2]]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 0, 0, 1], [0, 5, 0, 2], [0, 0, 5, 3], [1, 2, 3, 4]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 0, 0, 1], [0, 5, 0, 2], [0, 0, 5, 3], [1, 2, 3, 4]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [2, 0, 1, 0, 2], [0, 0, 0, 0, 0], [1, 0, 2, 0, 1]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [2, 0, 1, 0, 2], [0, 0, 0, 0, 0], [1, 0, 2, 0, 1]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [5, 3, 1, 3, 5], [1, 5, 3, 5, 1]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [5, 3, 1, 3, 5], [1, 5, 3, 5, 1]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3, 4], [1, 0, 3, 2, 4], [2, 3, 0, 4, 1], [3, 2, 4, 0, 2], [4, 4, 1, 2, 0]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3, 4], [1, 0, 3, 2, 4], [2, 3, 0, 4, 1], [3, 2, 4, 0, 2], [4, 4, 1, 2, 0]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 1, 1, 1], [1, 4, 1, 1], [1, 1, 4, 1], [1, 1, 1, 4]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 1, 1, 1], [1, 4, 1, 1], [1, 1, 4, 1], [1, 1, 1, 4]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 1], [1, 2, 3], [4, 5, 6]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 1], [1, 2, 3], [4, 5, 6]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 0, 0], [0, 2, 0, 0], [0, 0, 4, 0], [0, 0, 0, 1]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 0, 0], [0, 2, 0, 0], [0, 0, 4, 0], [0, 0, 0, 1]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 0, 0, 0], [0, 9, 0, 0], [0, 0, 9, 0], [0, 0, 0, 9]]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 0, 0, 0], [0, 9, 0, 0], [0, 0, 9, 0], [0, 0, 0, 9]]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 5, 5, 3], [4, 7, 6, 2], [1, 3, 4, 0], [3, 1, 2, 5]]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 5, 5, 3], [4, 7, 6, 2], [1, 3, 4, 0], [3, 1, 2, 5]]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [3, 5, 7, 5, 3]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [3, 5, 7, 5, 3]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 0, 5, 0, 0], [0, 0, 5, 0, 0], [5, 5, 5, 5, 5], [0, 0, 5, 0, 0], [0, 0, 5, 0, 0]]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 0, 5, 0, 0], [0, 0, 5, 0, 0], [5, 5, 5, 5, 5], [0, 0, 5, 0, 0], [0, 0, 5, 0, 0]]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 10, 10], [10, 1, 10], [10, 10, 10]]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 10, 10], [10, 1, 10], [10, 10, 10]]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 0, 0], [0, 3, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 0, 0], [0, 3, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [3, 5, 7, 5, 3]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [3, 5, 7, 5, 3]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 0, 0, 0, 0], [0, 5, 0, 0, 0], [0, 0, 5, 0, 0], [0, 0, 0, 5, 0], [0, 0, 0, 0, 5]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 0, 0, 0, 0], [0, 5, 0, 0, 0], [0, 0, 5, 0, 0], [0, 0, 0, 5, 0], [0, 0, 0, 0, 5]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [4, 2, 1, 2, 4], [2, 4, 2, 4, 2]]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [4, 2, 1, 2, 4], [2, 4, 2, 4, 2]]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 10, 10], [10, 0, 10], [10, 10, 10]]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 10, 10], [10, 0, 10], [10, 10, 10]]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 5, 5, 5], [5, 1, 1, 5], [5, 1, 1, 5], [5, 5, 5, 5]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 5, 5, 5], [5, 1, 1, 5], [5, 1, 1, 5], [5, 5, 5, 5]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 8, 3], [3, 7, 2], [6, 4, 1]]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 8, 3], [3, 7, 2], [6, 4, 1]]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 1, 3], [0, 2, 4], [6, 0, 0]]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 1, 3], [0, 2, 4], [6, 0, 0]]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 5, 2, 4, 3], [3, 4, 1, 5, 2], [2, 1, 4, 3, 5]]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 5, 2, 4, 3], [3, 4, 1, 5, 2], [2, 1, 4, 3, 5]]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 4, 4], [4, 0, 4], [4, 4, 4]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 4, 4], [4, 0, 4], [4, 4, 4]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 4, 0], [0, 2, 0, 0], [1, 0, 3, 0], [0, 0, 0, 3]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 4, 0], [0, 2, 0, 0], [1, 0, 3, 0], [0, 0, 0, 3]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [5, 3, 1, 3, 5], [2, 4, 6, 4, 2]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [5, 3, 1, 3, 5], [2, 4, 6, 4, 2]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 0, 0, 0], [0, 20, 0, 0], [0, 0, 30, 0], [0, 0, 0, 40]]) == 204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 0, 0, 0], [0, 20, 0, 0], [0, 0, 30, 0], [0, 0, 0, 40]]) == 204: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 3, 1], [4, 2, 0], [1, 4, 2]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 3, 1], [4, 2, 0], [1, 4, 2]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1], [2, 4, 6, 8, 10]]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1], [2, 4, 6, 8, 10]]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12], [12, 11, 10, 9, 8, 7]]) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12], [12, 11, 10, 9, 8, 7]]) == 158: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3, 4], [5, 4, 3, 2, 1], [4, 5, 6, 7, 8], [3, 2, 1, 0, 9], [2, 3, 4, 5, 6]]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3, 4], [5, 4, 3, 2, 1], [4, 5, 6, 7, 8], [3, 2, 1, 0, 9], [2, 3, 4, 5, 6]]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[2, 2, 2, 2], [2, 1, 1, 2], [2, 1, 1, 2], [2, 2, 2, 2]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[2, 2, 2, 2], [2, 1, 1, 2], [2, 1, 1, 2], [2, 2, 2, 2]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 3], [0, 4, 0], [3, 0, 3]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 3], [0, 4, 0], [3, 0, 3]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 0, 0, 0], [0, 4, 0, 0], [0, 0, 4, 0], [0, 0, 0, 4]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 0, 0, 0], [0, 4, 0, 0], [0, 0, 4, 0], [0, 0, 0, 4]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 0, 3, 3], [0, 2, 0, 0, 0], [0, 0, 4, 0, 0], [3, 0, 0, 3, 3], [3, 0, 0, 3, 3]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 0, 3, 3], [0, 2, 0, 0, 0], [0, 0, 4, 0, 0], [3, 0, 0, 3, 3], [3, 0, 0, 3, 3]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[4, 0, 0], [0, 0, 0], [0, 0, 4]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[4, 0, 0], [0, 0, 0], [0, 0, 4]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, 0, 4], [2, 1, 0, 4, 3], [1, 0, 4, 3, 2]]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, 0, 4], [2, 1, 0, 4, 3], [1, 0, 4, 3, 2]]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 2, 3, 4], [8, 7, 6, 5]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 2, 3, 4], [8, 7, 6, 5]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[5, 0, 0, 0], [0, 5, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[5, 0, 0, 0], [0, 5, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[3, 1, 4], [2, 5, 6], [7, 8, 9]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[3, 1, 4], [2, 5, 6], [7, 8, 9]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[0, 1, 2, 3], [3, 2, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[0, 1, 2, 3], [3, 2, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(grid = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]) == 249: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 21
    assert candidate(grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 14
    assert candidate(grid = [[2]]) == 5
    assert candidate(grid = [[1, 2], [3, 4]]) == 17
    assert candidate(grid = [[1, 0], [0, 2]]) == 8
    assert candidate(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
    assert candidate(grid = [[1, 0, 2, 1], [2, 1, 0, 2], [1, 0, 2, 1], [2, 1, 0, 2]]) == 27
    assert candidate(grid = [[5, 0, 0, 1], [0, 5, 0, 2], [0, 0, 5, 3], [1, 2, 3, 4]]) == 48
    assert candidate(grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [2, 0, 1, 0, 2], [0, 0, 0, 0, 0], [1, 0, 2, 0, 1]]) == 21
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [5, 3, 1, 3, 5], [1, 5, 3, 5, 1]]) == 75
    assert candidate(grid = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]) == 56
    assert candidate(grid = [[0, 1, 2, 3, 4], [1, 0, 3, 2, 4], [2, 3, 0, 4, 1], [3, 2, 4, 0, 2], [4, 4, 1, 2, 0]]) == 60
    assert candidate(grid = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]) == 26
    assert candidate(grid = [[4, 1, 1, 1], [1, 4, 1, 1], [1, 1, 4, 1], [1, 1, 1, 4]]) == 48
    assert candidate(grid = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]) == 15
    assert candidate(grid = [[3, 0, 1], [1, 2, 3], [4, 5, 6]]) == 35
    assert candidate(grid = [[3, 0, 0, 0], [0, 2, 0, 0], [0, 0, 4, 0], [0, 0, 0, 1]]) == 24
    assert candidate(grid = [[9, 0, 0, 0], [0, 9, 0, 0], [0, 0, 9, 0], [0, 0, 0, 9]]) == 76
    assert candidate(grid = [[10, 5, 5, 3], [4, 7, 6, 2], [1, 3, 4, 0], [3, 1, 2, 5]]) == 69
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [3, 5, 7, 5, 3]]) == 80
    assert candidate(grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 9
    assert candidate(grid = [[0, 0, 5, 0, 0], [0, 0, 5, 0, 0], [5, 5, 5, 5, 5], [0, 0, 5, 0, 0], [0, 0, 5, 0, 0]]) == 59
    assert candidate(grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 11
    assert candidate(grid = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]) == 40
    assert candidate(grid = [[10, 10, 10], [10, 1, 10], [10, 10, 10]]) == 69
    assert candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 15
    assert candidate(grid = [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]) == 51
    assert candidate(grid = [[3, 0, 0, 0], [0, 3, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3]]) == 28
    assert candidate(grid = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]) == 40
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [2, 4, 6, 4, 2], [3, 5, 7, 5, 3]]) == 80
    assert candidate(grid = [[5, 0, 0, 0, 0], [0, 5, 0, 0, 0], [0, 0, 5, 0, 0], [0, 0, 0, 5, 0], [0, 0, 0, 0, 5]]) == 55
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [4, 2, 1, 2, 4], [2, 4, 2, 4, 2]]) == 71
    assert candidate(grid = [[10, 10, 10], [10, 0, 10], [10, 10, 10]]) == 68
    assert candidate(grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 35
    assert candidate(grid = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 75
    assert candidate(grid = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]) == 16
    assert candidate(grid = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]) == 33
    assert candidate(grid = [[5, 5, 5, 5], [5, 1, 1, 5], [5, 1, 1, 5], [5, 5, 5, 5]]) == 56
    assert candidate(grid = [[5, 8, 3], [3, 7, 2], [6, 4, 1]]) == 47
    assert candidate(grid = [[5, 1, 3], [0, 2, 4], [6, 0, 0]]) == 33
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 5, 2, 4, 3], [3, 4, 1, 5, 2], [2, 1, 4, 3, 5]]) == 74
    assert candidate(grid = [[4, 4, 4], [4, 0, 4], [4, 4, 4]]) == 32
    assert candidate(grid = [[3, 0, 4, 0], [0, 2, 0, 0], [1, 0, 3, 0], [0, 0, 0, 3]]) == 30
    assert candidate(grid = [[3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3]]) == 55
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 3, 1], [5, 3, 1, 3, 5], [2, 4, 6, 4, 2]]) == 75
    assert candidate(grid = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]) == 46
    assert candidate(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]) == 14
    assert candidate(grid = [[10, 0, 0, 0], [0, 20, 0, 0], [0, 0, 30, 0], [0, 0, 0, 40]]) == 204
    assert candidate(grid = [[5, 3, 1], [4, 2, 0], [1, 4, 2]]) == 32
    assert candidate(grid = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 5, 7, 9], [9, 7, 5, 3, 1], [2, 4, 6, 8, 10]]) == 103
    assert candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [2, 4, 6, 8, 10, 12], [12, 11, 10, 9, 8, 7]]) == 158
    assert candidate(grid = [[0, 1, 2, 3, 4], [5, 4, 3, 2, 1], [4, 5, 6, 7, 8], [3, 2, 1, 0, 9], [2, 3, 4, 5, 6]]) == 87
    assert candidate(grid = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11], [11, 9, 7, 5, 3, 1], [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]) == 136
    assert candidate(grid = [[2, 2, 2, 2], [2, 1, 1, 2], [2, 1, 1, 2], [2, 2, 2, 2]]) == 32
    assert candidate(grid = [[3, 0, 3], [0, 4, 0], [3, 0, 3]]) == 25
    assert candidate(grid = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]) == 105
    assert candidate(grid = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]) == 33
    assert candidate(grid = [[4, 0, 0, 0], [0, 4, 0, 0], [0, 0, 4, 0], [0, 0, 0, 4]]) == 36
    assert candidate(grid = [[3, 0, 0, 3, 3], [0, 2, 0, 0, 0], [0, 0, 4, 0, 0], [3, 0, 0, 3, 3], [3, 0, 0, 3, 3]]) == 41
    assert candidate(grid = [[1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1]]) == 19
    assert candidate(grid = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]) == 21
    assert candidate(grid = [[4, 0, 0], [0, 0, 0], [0, 0, 4]]) == 18
    assert candidate(grid = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 12
    assert candidate(grid = [[5, 4, 3, 2, 1], [4, 3, 2, 1, 0], [3, 2, 1, 0, 4], [2, 1, 0, 4, 3], [1, 0, 4, 3, 2]]) == 63
    assert candidate(grid = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == 16
    assert candidate(grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 24
    assert candidate(grid = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 2, 3, 4], [8, 7, 6, 5]]) == 72
    assert candidate(grid = [[5, 0, 0, 0], [0, 5, 0, 0], [0, 0, 5, 0], [0, 0, 0, 5]]) == 44
    assert candidate(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 51
    assert candidate(grid = [[3, 1, 4], [2, 5, 6], [7, 8, 9]]) == 52
    assert candidate(grid = [[0, 1, 2, 3], [3, 2, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == 28
    assert candidate(grid = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]) == 249


