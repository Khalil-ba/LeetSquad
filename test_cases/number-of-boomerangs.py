def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [0, 0], [0, 1]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [0, 0], [0, 1]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [0, 2]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [0, 2]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, 2], [2, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, 2], [2, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10000, 10000], [-10000, -10000], [0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10000, 10000], [-10000, -10000], [0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [1, 1], [2, 2]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [1, 1], [2, 2]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [1, 1], [2, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [1, 1], [2, 0]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [0, 0], [1, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [0, 0], [1, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [2, 3], [3, 2], [1, 2], [2, 1]]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [2, 3], [3, 2], [1, 2], [2, 1]]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 2], [2, 1], [1, 2]]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 2], [2, 1], [1, 2]]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-2, -2], [-1, -1], [1, 1], [2, 2], [-3, -3], [3, 3], [-4, -4], [4, 4]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-2, -2], [-1, -1], [1, 1], [2, 2], [-3, -3], [3, 3], [-4, -4], [4, 4]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [0, -1], [1, 0], [0, 1], [0, 0]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [0, -1], [1, 0], [0, 1], [0, 0]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [1, 1], [2, 2], [3, 3], [4, 4], [-1, 1], [1, -1], [-2, -2], [-3, -3], [-4, -4]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [1, 1], [2, 2], [3, 3], [4, 4], [-1, 1], [1, -1], [-2, -2], [-3, -3], [-4, -4]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [2, 1]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [2, 1]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, 0], [2, 0], [0, 1], [0, 2], [2, 1], [2, 2], [1, 2], [2, 1]]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, 0], [2, 0], [0, 1], [0, 2], [2, 1], [2, 2], [1, 2], [2, 1]]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [3, 4], [4, 5]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [3, 4], [4, 5]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [4, 0], [4, 2], [0, 4], [2, 4], [4, 4]]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [4, 0], [4, 2], [0, 4], [2, 4], [4, 4]]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 10], [10, 5], [10, 10], [7, 7], [8, 8]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 10], [10, 5], [10, 10], [7, 7], [8, 8]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [-1, 1], [1, -1]]) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [-1, 1], [1, -1]]) == 48: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2], [2, 0], [0, 2], [3, 0], [0, 3]]) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2], [2, 0], [0, 2], [3, 0], [0, 3]]) == 192: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10000, -10000], [10000, 10000], [0, 0], [5000, 5000], [-5000, -5000], [2000, 2000], [-2000, -2000]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10000, -10000], [10000, 10000], [0, 0], [5000, 5000], [-5000, -5000], [2000, 2000], [-2000, -2000]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [0, 2], [0, 3], [0, 4]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [0, 2], [0, 3], [0, 4]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, 0], [2, 0], [2, 1], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2]]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, 0], [2, 0], [2, 1], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2]]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4]]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4]]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10000, 10000], [10001, 10001], [10002, 10002], [10003, 10003], [10004, 10004]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10000, 10000], [10001, 10001], [10002, 10002], [10003, 10003], [10004, 10004]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [101, 101], [102, 102], [100, 102], [102, 100], [101, 100], [100, 101], [102, 101], [101, 102]]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [101, 101], [102, 102], [100, 102], [102, 100], [101, 100], [100, 101], [102, 101], [101, 102]]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [-1, 1], [-2, 2], [-3, 3], [1, -1], [2, -2], [3, -3]]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [-1, 1], [-2, 2], [-3, 3], [1, -1], [2, -2], [3, -3]]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [0, 0], [1, 0], [0, -1], [0, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [0, 0], [1, 0], [0, -1], [0, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [10000, 10000], [-10000, -10000], [10000, -10000], [-10000, 10000]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [10000, 10000], [-10000, -10000], [10000, -10000], [-10000, 10000]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3], [4, 4]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3], [4, 4]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3], [4, 3], [4, 4], [5, 4]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3], [4, 3], [4, 4], [5, 4]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 1], [1, 2]]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 1], [1, 2]]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 2], [1, -2], [2, 4], [2, -4], [-1, 2], [-1, -2]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 2], [1, -2], [2, 4], [2, -4], [-1, 2], [-1, -2]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [10, 0], [20, 0], [0, 10], [10, 10], [20, 10], [0, 20], [10, 20], [20, 20]]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [10, 0], [20, 0], [0, 10], [10, 10], [20, 10], [0, 20], [10, 20], [20, 20]]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1], [0, 2], [1, 2], [2, 2], [3, 2]]) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1], [0, 2], [1, 2], [2, 2], [3, 2]]) == 164: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [1, 1], [1, -1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [1, 1], [1, -1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, 0], [0, 1], [2, 2], [2, 0], [0, 2]]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, 0], [0, 1], [2, 2], [2, 0], [0, 2]]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1000, -1000], [-1000, -999], [-999, -1000], [-999, -999], [-1001, -1001], [-1001, -1000], [-1000, -1001]]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1000, -1000], [-1000, -999], [-999, -1000], [-999, -999], [-1001, -1001], [-1001, -1000], [-1000, -1001]]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [1, 1], [0, 1], [0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [1, 1], [0, 1], [0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, 5], [-3, -3], [-1, 1], [-2, -2], [0, 0], [2, 2], [3, 3], [5, -5], [4, 4]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, 5], [-3, -3], [-1, 1], [-2, -2], [0, 0], [2, 2], [3, 3], [5, -5], [4, 4]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [0, 0], [1, 0], [0, 1], [0, -1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [0, 0], [1, 0], [0, 1], [0, -1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [10, 20], [20, 20], [20, 10], [10, 15]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [10, 20], [20, 20], [20, 10], [10, 15]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [1, 0], [0, 1], [2, 0], [0, 2]]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [1, 0], [0, 1], [2, 0], [0, 2]]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1], [-1, 2], [0, 2], [1, 2]]) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1], [-1, 2], [0, 2], [1, 2]]) == 164: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [0, 1], [1, -1], [-2, 0], [0, 2], [2, -2], [-3, 0], [0, 3], [3, -3], [-4, 0]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [0, 1], [1, -1], [-2, 0], [0, 2], [2, -2], [-3, 0], [0, 3], [3, -3], [-4, 0]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10000, -10000], [-9999, -9999], [-9998, -9998], [-9997, -9997], [-9996, -9996]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10000, -10000], [-9999, -9999], [-9998, -9998], [-9997, -9997], [-9996, -9996]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, 2], [2, 1], [2, 2]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, 2], [2, 1], [2, 2]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2], [2, 1], [1, 2], [2, 2], [3, 3]]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2], [2, 1], [1, 2], [2, 2], [3, 3]]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [101, 100], [100, 101], [101, 101], [102, 102], [102, 101], [101, 102]]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [101, 100], [100, 101], [101, 101], [102, 102], [102, 101], [101, 102]]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1], [1, 3], [3, 1], [3, 3], [2, 3], [3, 2]]) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1], [1, 3], [3, 1], [3, 3], [2, 3], [3, 2]]) == 92: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [0, 0]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [0, 0]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2], [1, 2], [2, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2], [1, 2], [2, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2], [1, 2]]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2], [1, 2]]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [101, 100], [100, 101], [101, 101], [100, 99], [101, 99], [99, 100], [99, 101], [99, 99]]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [101, 100], [100, 101], [101, 101], [100, 99], [101, 99], [99, 100], [99, 101], [99, 99]]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [1, 0], [0, 1]]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [1, 0], [0, 1]]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 2], [2, 1], [2, 3], [3, 2], [1, 3]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 2], [2, 1], [2, 3], [3, 2], [1, 3]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0]]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0]]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [0, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [0, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1]]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1]]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [-5, 0], [0, -5], [0, 0], [2, 2], [3, 3], [4, 4]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [-5, 0], [0, -5], [0, 0], [2, 2], [3, 3], [4, 4]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]) == 60: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == 8
    assert candidate(points = [[1, 0], [0, 0], [0, 1]]) == 2
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5]]) == 4
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [0, 2]]) == 4
    assert candidate(points = [[0, 0], [1, 0], [2, 0]]) == 2
    assert candidate(points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]) == 20
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [1, 4]]) == 4
    assert candidate(points = [[0, 0], [1, 1], [1, 2], [2, 0]]) == 4
    assert candidate(points = [[10000, 10000], [-10000, -10000], [0, 0]]) == 2
    assert candidate(points = [[1, 1], [2, 2], [3, 3]]) == 2
    assert candidate(points = [[1, 1], [2, 2], [1, 1], [2, 2]]) == 16
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1]]) == 8
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3]]) == 4
    assert candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1]]) == 8
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [2, 0]]) == 8
    assert candidate(points = [[-1, 0], [0, 0], [1, 0]]) == 2
    assert candidate(points = [[1, 1]]) == 0
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [2, 3], [3, 2], [1, 2], [2, 1]]) == 38
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 2], [2, 1], [1, 2]]) == 38
    assert candidate(points = [[-2, -2], [-1, -1], [1, 1], [2, 2], [-3, -3], [3, 3], [-4, -4], [4, 4]]) == 16
    assert candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]) == 8
    assert candidate(points = [[-1, 0], [0, -1], [1, 0], [0, 1], [0, 0]]) == 20
    assert candidate(points = [[-1, -1], [1, 1], [2, 2], [3, 3], [4, 4], [-1, 1], [1, -1], [-2, -2], [-3, -3], [-4, -4]]) == 48
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [2, 1]]) == 24
    assert candidate(points = [[0, 0], [1, 1], [1, 0], [2, 0], [0, 1], [0, 2], [2, 1], [2, 2], [1, 2], [2, 1]]) == 136
    assert candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]) == 40
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 40
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 8
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]) == 64
    assert candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 8
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [3, 4], [4, 5]]) == 16
    assert candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [4, 0], [4, 2], [0, 4], [2, 4], [4, 4]]) == 88
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 40
    assert candidate(points = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]]) == 40
    assert candidate(points = [[5, 5], [5, 10], [10, 5], [10, 10], [7, 7], [8, 8]]) == 16
    assert candidate(points = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]) == 24
    assert candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [-1, 1], [1, -1]]) == 48
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 1], [1, 3], [3, 1], [2, 3], [3, 2], [2, 0], [0, 2], [3, 0], [0, 3]]) == 192
    assert candidate(points = [[-10000, -10000], [10000, 10000], [0, 0], [5000, 5000], [-5000, -5000], [2000, 2000], [-2000, -2000]]) == 10
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [0, 2], [0, 3], [0, 4]]) == 18
    assert candidate(points = [[0, 0], [1, 1], [1, 0], [2, 0], [2, 1], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2]]) == 104
    assert candidate(points = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 4]]) == 104
    assert candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 12
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 18
    assert candidate(points = [[10000, 10000], [10001, 10001], [10002, 10002], [10003, 10003], [10004, 10004]]) == 8
    assert candidate(points = [[100, 100], [101, 101], [102, 102], [100, 102], [102, 100], [101, 100], [100, 101], [102, 101], [101, 102]]) == 88
    assert candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 12
    assert candidate(points = [[-1, -1], [0, 0], [1, 1], [2, 2], [3, 3], [-1, 1], [-2, 2], [-3, 3], [1, -1], [2, -2], [3, -3]]) == 78
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]) == 40
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 40
    assert candidate(points = [[0, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]) == 20
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]) == 20
    assert candidate(points = [[-1, 0], [0, 0], [1, 0], [0, -1], [0, 1]]) == 20
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13]]) == 72
    assert candidate(points = [[0, 0], [10000, 10000], [-10000, -10000], [10000, -10000], [-10000, 10000]]) == 20
    assert candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1]]) == 12
    assert candidate(points = [[0, 0], [0, 5], [5, 0], [5, 5], [2, 2], [3, 3], [4, 4]]) == 24
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3], [4, 3], [4, 4], [5, 4]]) == 40
    assert candidate(points = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 1], [1, 2]]) == 38
    assert candidate(points = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2]]) == 24
    assert candidate(points = [[0, 0], [1, 2], [1, -2], [2, 4], [2, -4], [-1, 2], [-1, -2]]) == 18
    assert candidate(points = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]) == 40
    assert candidate(points = [[0, 0], [10, 0], [20, 0], [0, 10], [10, 10], [20, 10], [0, 20], [10, 20], [20, 20]]) == 88
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]) == 8
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]) == 18
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1], [0, 2], [1, 2], [2, 2], [3, 2]]) == 164
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [1, 1], [1, -1]]) == 20
    assert candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1]]) == 20
    assert candidate(points = [[0, 0], [1, 1], [1, 0], [0, 1], [2, 2], [2, 0], [0, 2]]) == 42
    assert candidate(points = [[-1000, -1000], [-1000, -999], [-999, -1000], [-999, -999], [-1001, -1001], [-1001, -1000], [-1000, -1001]]) == 38
    assert candidate(points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]]) == 40
    assert candidate(points = [[0, 0], [1, 0], [1, 1], [0, 1], [0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5]]) == 60
    assert candidate(points = [[-5, 5], [-3, -3], [-1, 1], [-2, -2], [0, 0], [2, 2], [3, 3], [5, -5], [4, 4]]) == 32
    assert candidate(points = [[-1, 0], [0, 0], [1, 0], [0, 1], [0, -1]]) == 20
    assert candidate(points = [[10, 10], [10, 20], [20, 20], [20, 10], [10, 15]]) == 12
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [1, 0], [0, 1], [2, 0], [0, 2]]) == 42
    assert candidate(points = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1], [-1, 2], [0, 2], [1, 2]]) == 164
    assert candidate(points = [[-1, 0], [0, 1], [1, -1], [-2, 0], [0, 2], [2, -2], [-3, 0], [0, 3], [3, -3], [-4, 0]]) == 32
    assert candidate(points = [[-10000, -10000], [-9999, -9999], [-9998, -9998], [-9997, -9997], [-9996, -9996]]) == 8
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]) == 88
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1]]) == 6
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2]]) == 24
    assert candidate(points = [[0, 0], [1, 1], [1, 2], [2, 1], [2, 2]]) == 12
    assert candidate(points = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12]]) == 12
    assert candidate(points = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]) == 12
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2], [2, 1], [1, 2], [2, 2], [3, 3]]) == 104
    assert candidate(points = [[100, 100], [101, 100], [100, 101], [101, 101], [102, 102], [102, 101], [101, 102]]) == 38
    assert candidate(points = [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1], [1, 3], [3, 1], [3, 3], [2, 3], [3, 2]]) == 92
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]) == 40
    assert candidate(points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]) == 12
    assert candidate(points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]) == 24
    assert candidate(points = [[-1, 0], [1, 0], [0, -1], [0, 1], [0, 0]]) == 20
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12]]) == 60
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 8
    assert candidate(points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 40
    assert candidate(points = [[0, 0], [1, 1], [2, 2], [1, 2], [2, 1]]) == 12
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 0], [0, 2], [1, 2]]) == 38
    assert candidate(points = [[100, 100], [101, 100], [100, 101], [101, 101], [100, 99], [101, 99], [99, 100], [99, 101], [99, 99]]) == 88
    assert candidate(points = [[-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [1, 0], [0, 1]]) == 26
    assert candidate(points = [[0, 0], [1, 2], [2, 1], [2, 3], [3, 2], [1, 3]]) == 18
    assert candidate(points = [[0, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [4, 0]]) == 94
    assert candidate(points = [[-1, 0], [0, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]) == 88
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1]]) == 38
    assert candidate(points = [[-5, -5], [-5, 0], [0, -5], [0, 0], [2, 2], [3, 3], [4, 4]]) == 18
    assert candidate(points = [[0, 0], [1, 0], [0, 1], [1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]) == 60


