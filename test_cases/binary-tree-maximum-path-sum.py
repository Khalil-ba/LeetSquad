def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-3])) == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-3])) == -3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, -3])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, -3])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-2, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-2, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == 42: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 48: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 48: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, -1, -2, 1, 1, -3, -4, -5, -6])) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, -1, -2, 1, 1, -3, -4, -5, -6])) == 43: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 55: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])) == 440: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, 2, -3, 4, -5, 6, -7, 8, -9, None, None, None, None, None, -10])) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, 2, -3, 4, -5, 6, -7, 8, -9, None, None, None, None, None, -10])) == 16: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 30, 15, 25, 10, 35, -10, -5, None, None, None, None, None, None])) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 30, 15, 25, 10, 35, -10, -5, None, None, None, None, None, None])) == 160: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 36: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 5, 15, -5, 3, None, 7, -1, None, -2, 4, None, None, 8])) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 5, 15, -5, 3, None, 7, -1, None, -2, 4, None, None, 8])) == 24: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 6, -3, None, None, -6, 2, None, None, 2, 2, None, -1, -6, -6, -6])) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 6, -3, None, None, -6, 2, None, None, 2, 2, None, -1, -6, -6, -6])) == 16: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 30, 10, 40, 25, 35, 5, 15, 32, 45, 22, 28, 33, 42, 1, 9, 11, 19, 31, 37, 43, 48, 0, 4, 8, 14, 16, 18, 21, 24, 27, 29, 34, 36, 39, 41, 44, 46, 47, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 30, 10, 40, 25, 35, 5, 15, 32, 45, 22, 28, 33, 42, 1, 9, 11, 19, 31, 37, 43, 48, 0, 4, 8, 14, 16, 18, 21, 24, 27, 29, 34, 36, 39, 41, 44, 46, 47, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 351: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, None, -2, None, -3, None, -4, -5, None])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, None, -2, None, -3, None, -4, -5, None])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -5, 7, -4, None, None, 6, -3, -1, 8, 9, None, None, None, None, None, 10])) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -5, 7, -4, None, None, 6, -3, -1, 8, 9, None, None, None, None, None, 10])) == 33: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, -10, None, None, 15, 7, None, None, None, 1, None, None, -1, None, -5])) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, -10, None, None, 15, 7, None, None, None, 1, None, None, -1, None, -5])) == 24: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -1, -2, 1, -3, -4, -5, -6, -7])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -1, -2, 1, -3, -4, -5, -6, -7])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -2, 9, 3, 1, None, None, None, None, None, None, None, -10])) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -2, 9, 3, 1, None, None, None, None, None, None, None, -10])) == 52: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 27: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, -50, 40, 20, None, -60, 30, None, 10, None, -5])) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, -50, 40, 20, None, -60, 30, None, 10, None, -5])) == 120: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, -5, 6, 8, -4, -6, None, 7, 9])) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, -5, 6, 8, -4, -6, None, 7, 9])) == 58: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, 2, 2, None, 3, None, 3, None, 4, None, 4])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, 2, 2, None, 3, None, 3, None, 4, None, 4])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -10, 20, None, None, 15, 6, None, None, -5, 12, 11, 13, -14])) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -10, 20, None, None, 15, 6, None, None, -5, 12, 11, 13, -14])) == 53: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -20, -30, -40, None, -50, -60, None, None, -70, -80, -90, None, None, -100])) == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -20, -30, -40, None, -50, -60, None, None, -70, -80, -90, None, None, -100])) == -10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 40, 60, 90, 125, 175, 250, 350])) == 1175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 40, 60, 90, 125, 175, 250, 350])) == 1175: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -2, -3, 1, 2, -1, -1, -2, None, -3, None, -2, -2])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -2, -3, 1, 2, -1, -1, -2, None, -3, None, -2, -2])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 12, 3, 8, 99, -100, 5, None, 4, 2, 1, None, None, None, None, None, None, None, -99])) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 12, 3, 8, 99, -100, 5, None, 4, 2, 1, None, None, None, None, None, None, None, -99])) == 159: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, 50, -25, 25, -12, 12, -6, 6, -3, 3, -1, 1, 0, -100, 100, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, 50, -25, 25, -12, 12, -6, 6, -3, 3, -1, 1, 0, -100, 100, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 181: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, None, None, 9])) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, None, None, 9])) == 52: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 44: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -10, 20, 15, 10, None, -25, 6, None, None, -3, None, 4])) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -10, 20, 15, 10, None, -25, 6, None, None, -3, None, 4])) == 32: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -2, -3, -4, -5])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -2, -3, -4, -5])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -5, 6, 9])) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -5, 6, 9])) == 50: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, 3, 4, None, None, -6, None, -7, None, None, 8, 9])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, 3, 4, None, None, -6, None, -7, None, None, 8, 9])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 5, 20, 15, 25, None, None, None, -5, 30, None])) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 5, 20, 15, 25, None, None, None, -5, 30, None])) == 75: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -2, 15, 20, -5, None, 7, None, 1, None, 3, 9])) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -2, 15, 20, -5, None, 7, None, 1, None, 3, 9])) == 60: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 101: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -5, -1, None, -9, -4, None, None, -3, None, -8])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -5, -1, None, -9, -4, None, None, -3, None, -8])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 69: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 3, 10, -1, None, -15, 9, None, None, None, -1])) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 3, 10, -1, None, -15, 9, None, None, None, -1])) == 59: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -10, 20, 15, 7, -2, None, None, None, None, None, 5, 1, None, None, None, -1])) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -10, 20, 15, 7, -2, None, None, None, None, None, 5, 1, None, None, None, -1])) == 28: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 2, 10, 8, 34, 7, 6, 1, None, None, None, None, None, 9, 8, 7])) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 2, 10, 8, 34, 7, 6, 1, None, None, None, None, None, 9, 8, 7])) == 71: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, 5])) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, 5])) == 53: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, -14, 16, 18, None, None, None, None, None, None, None, -19])) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, -14, 16, 18, None, None, None, None, None, None, None, -19])) == 64: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 44: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 2, 5, None, None, 6, 3, None, None, 9, None, None, 12, 15, 7])) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 2, 5, None, None, 6, 3, None, None, 9, None, None, 12, 15, 7])) == 50: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -10, 7, 8, None, 15, None, -8, None, 5, None, 9, 6, 11, None, None, None, None, None, None, None, None, None, None, None])) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -10, 7, 8, None, 15, None, -8, None, 5, None, 9, 6, 11, None, None, None, None, None, None, None, None, None, None, None])) == 38: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19, None, 2, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19, None, 2, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 82: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, None, 9, -6, 3, None, None, None, -2])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, None, 9, -6, 3, None, None, None, -2])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30])) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30])) == 44: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20])) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20])) == 48: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, None, None, None, None, 2, None, 1, None, -1, None, None, None, -2])) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, None, None, None, None, 2, None, 1, None, -1, None, None, None, -2])) == 42: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -1, None, -2])) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -1, None, -2])) == 48: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, 200, -75, 25, 150, 250, -100, None, 20, None, -50, None, 30, 40])) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, 200, -75, 25, 150, 250, -100, None, 20, None, -50, None, 30, 40])) == 640: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, None, -2, None, -3, None, -4, None, -5])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, None, -2, None, -3, None, -4, None, -5])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 0, -1, -3, None, -10, None, None, -5])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 0, -1, -3, None, -10, None, None, -5])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -10, 5, None, None, -5, 6])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -10, 5, None, None, -5, 6])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40, None, None, None, -40, None, None, -50, -60, None, None, -70, -80])) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40, None, None, None, -40, None, None, -50, -60, None, None, -70, -80])) == 90: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40])) == 820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40])) == 820: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7])) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7])) == -1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 12, None, 2, 1, None, None, -5])) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 12, None, 2, 1, None, None, -5])) == 66: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, -4, -8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -5, 6, 9, -3])) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, -4, -8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -5, 6, 9, -3])) == 26: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -1, -2, 1, -4, -5, -6])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -1, -2, 1, -4, -5, -6])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) == 119: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -5, 6, None, 5, None, 7])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -5, 6, None, 5, None, 7])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 14, 15, 16, 17, 18, 19])) == 284
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 14, 15, 16, 17, 18, 19])) == 284: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, -2, 5, -6, None, None, 4, None, None, -8, None, None, 7])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, -2, 5, -6, None, None, 4, None, None, -8, None, None, 7])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 20, 30, 10, 40, 25, 35, 5, 15, 32, 45, 23, 27, 33, 47, 1, 9, 11, 19, 31, 34, 39, 44, 46, 48])) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 20, 30, 10, 40, 25, 35, 5, 15, 32, 45, 23, 27, 33, 47, 1, 9, 11, 19, 31, 34, 39, 44, 46, 48])) == 325: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 45: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, -1, None, -9])) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, -1, None, -9])) == 48: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, -10, None, None, 15, 20, 1, None, -1, None, -5, None, 4, None, -6])) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, -10, None, None, 15, 20, 1, None, -1, None, -5, None, 4, None, -6])) == 32: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 29: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, 3, -4, None, 5, -6, 7, None, None, 8, None, 9])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, 3, -4, None, 5, -6, 7, None, None, 8, None, 9])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, 3, 4, None, 5, -6, None, None, 7, -8, 9, -10, None, None, None, None, 11])) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, 3, 4, None, 5, -6, None, None, 7, -8, 9, -10, None, None, None, None, 11])) == 29: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -10, 20, 15, 7, None, -5, 20, 30])) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -10, 20, 15, 7, None, -5, 20, 30])) == 65: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, -3, 4, 5, None, 6, None, None, -8, -9])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, -3, 4, 5, None, 6, None, None, -8, -9])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 5, 9, None, -3, None, -8, None, -2, None, 7, -5, None, -1, None, 6, None, None, None, None, None, None, 8])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 5, 9, None, -3, None, -8, None, -2, None, 7, -5, None, -1, None, 6, None, None, None, None, None, None, 8])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])) == 16: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, -50, None, -100, -100, None, -50, -100, None, -150, -150])) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, -50, None, -100, -100, None, -50, -100, None, -150, -150])) == 100: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 30, 40, None, 50])) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 30, 40, None, 50])) == 127: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 15
    assert candidate(root = tree_node([2, -1])) == 2
    assert candidate(root = tree_node([-3])) == -3
    assert candidate(root = tree_node([1, 2, 3])) == 6
    assert candidate(root = tree_node([1, -2, -3])) == 1
    assert candidate(root = tree_node([-2, 1])) == 1
    assert candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == 42
    assert candidate(root = tree_node([1, 2])) == 3
    assert candidate(root = tree_node([1, None, 2])) == 3
    assert candidate(root = tree_node([0])) == 0
    assert candidate(root = tree_node([-1])) == -1
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 48
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([1, -2, -3, 1, 3, -2, None, -1])) == 3
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 48
    assert candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, -1, -2, 1, 1, -3, -4, -5, -6])) == 43
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 55
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])) == 440
    assert candidate(root = tree_node([-1, 2, -3, 4, -5, 6, -7, 8, -9, None, None, None, None, None, -10])) == 16
    assert candidate(root = tree_node([50, 20, 30, 15, 25, 10, 35, -10, -5, None, None, None, None, None, None])) == 160
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 36
    assert candidate(root = tree_node([-10, 5, 15, -5, 3, None, 7, -1, None, -2, 4, None, None, 8])) == 24
    assert candidate(root = tree_node([9, 6, -3, None, None, -6, 2, None, None, 2, 2, None, -1, -6, -6, -6])) == 16
    assert candidate(root = tree_node([50, 20, 30, 10, 40, 25, 35, 5, 15, 32, 45, 22, 28, 33, 42, 1, 9, 11, 19, 31, 37, 43, 48, 0, 4, 8, 14, 16, 18, 21, 24, 27, 29, 34, 36, 39, 41, 44, 46, 47, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 351
    assert candidate(root = tree_node([1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7, None, -8, None, -9])) == 1
    assert candidate(root = tree_node([-1, None, -2, None, -3, None, -4, -5, None])) == -1
    assert candidate(root = tree_node([2, -5, 7, -4, None, None, 6, -3, -1, 8, 9, None, None, None, None, None, 10])) == 33
    assert candidate(root = tree_node([10, 9, -10, None, None, 15, 7, None, None, None, 1, None, None, -1, None, -5])) == 24
    assert candidate(root = tree_node([2, -1, -2, 1, -3, -4, -5, -6, -7])) == 2
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -2, 9, 3, 1, None, None, None, None, None, None, None, -10])) == 52
    assert candidate(root = tree_node([-1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 27
    assert candidate(root = tree_node([100, -50, -50, 40, 20, None, -60, 30, None, 10, None, -5])) == 120
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, -5, 6, 8, -4, -6, None, 7, 9])) == 58
    assert candidate(root = tree_node([-1, 2, 2, None, 3, None, 3, None, 4, None, 4])) == 17
    assert candidate(root = tree_node([0, -10, 20, None, None, 15, 6, None, None, -5, 12, 11, 13, -14])) == 53
    assert candidate(root = tree_node([-10, -20, -30, -40, None, -50, -60, None, None, -70, -80, -90, None, None, -100])) == -10
    assert candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 40, 60, 90, 125, 175, 250, 350])) == 1175
    assert candidate(root = tree_node([-1, -2, -3, 1, 2, -1, -1, -2, None, -3, None, -2, -2])) == 2
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 6, 12, 3, 8, 99, -100, 5, None, 4, 2, 1, None, None, None, None, None, None, None, -99])) == 159
    assert candidate(root = tree_node([100, -50, 50, -25, 25, -12, 12, -6, 6, -3, 3, -1, 1, 0, -100, 100, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 181
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, None, None, 9])) == 52
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 44
    assert candidate(root = tree_node([1, -10, 20, 15, 10, None, -25, 6, None, None, -3, None, 4])) == 32
    assert candidate(root = tree_node([-1, -2, -3, -4, -5])) == -1
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -5, 6, 9])) == 50
    assert candidate(root = tree_node([1, -2, 3, 4, None, None, -6, None, -7, None, None, 8, 9])) == 10
    assert candidate(root = tree_node([-10, 5, 20, 15, 25, None, None, None, -5, 30, None])) == 75
    assert candidate(root = tree_node([10, -2, 15, 20, -5, None, 7, None, 1, None, 3, 9])) == 60
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 101
    assert candidate(root = tree_node([2, -5, -1, None, -9, -4, None, None, -3, None, -8])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 69
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 3, 10, -1, None, -15, 9, None, None, None, -1])) == 59
    assert candidate(root = tree_node([0, -10, 20, 15, 7, -2, None, None, None, None, None, 5, 1, None, None, None, -1])) == 28
    assert candidate(root = tree_node([10, 2, 10, 8, 34, 7, 6, 1, None, None, None, None, None, 9, 8, 7])) == 71
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, None, 5])) == 53
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1, -14, 16, 18, None, None, None, None, None, None, None, -19])) == 64
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 44
    assert candidate(root = tree_node([0, 2, 5, None, None, 6, 3, None, None, 9, None, None, 12, 15, 7])) == 50
    assert candidate(root = tree_node([0, -10, 7, 8, None, 15, None, -8, None, 5, None, 9, 6, 11, None, None, None, None, None, None, None, None, None, None, None])) == 38
    assert candidate(root = tree_node([1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19, None, 2, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 82
    assert candidate(root = tree_node([-1, None, 9, -6, 3, None, None, None, -2])) == 12
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30])) == 44
    assert candidate(root = tree_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20])) == 48
    assert candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, None, None, None, None, 2, None, 1, None, -1, None, None, None, -2])) == 42
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 0
    assert candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32])) == -1
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -1, None, -2])) == 48
    assert candidate(root = tree_node([100, -50, 200, -75, 25, 150, 250, -100, None, 20, None, -50, None, 30, 40])) == 640
    assert candidate(root = tree_node([-1, None, -2, None, -3, None, -4, None, -5])) == -1
    assert candidate(root = tree_node([9, 4, 0, -1, -3, None, -10, None, None, -5])) == 13
    assert candidate(root = tree_node([0, -10, 5, None, None, -5, 6])) == 11
    assert candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40, None, None, None, -40, None, None, -50, -60, None, None, -70, -80])) == 90
    assert candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == -1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40])) == 820
    assert candidate(root = tree_node([-1, None, -2, None, -3, None, -4, None, -5, None, -6, None, -7])) == -1
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 12, None, 2, 1, None, None, -5])) == 66
    assert candidate(root = tree_node([5, -4, -8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, -1, None, -5, 6, 9, -3])) == 26
    assert candidate(root = tree_node([2, -1, -2, 1, -4, -5, -6])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])) == 119
    assert candidate(root = tree_node([2, -5, 6, None, 5, None, 7])) == 15
    assert candidate(root = tree_node([100, 50, 50, 25, 25, 25, 25, 12, 13, 14, 15, 16, 17, 18, 19])) == 284
    assert candidate(root = tree_node([3, -2, 5, -6, None, None, 4, None, None, -8, None, None, 7])) == 12
    assert candidate(root = tree_node([50, 20, 30, 10, 40, 25, 35, 5, 15, 32, 45, 23, 27, 33, 47, 1, 9, 11, 19, 31, 34, 39, 44, 46, 48])) == 325
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 45
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, -1, None, -9])) == 48
    assert candidate(root = tree_node([10, 9, -10, None, None, 15, 20, 1, None, -1, None, -5, None, 4, None, -6])) == 32
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 29
    assert candidate(root = tree_node([1, -2, 3, -4, None, 5, -6, 7, None, None, 8, None, 9])) == 19
    assert candidate(root = tree_node([1, -2, 3, 4, None, 5, -6, None, None, 7, -8, 9, -10, None, None, None, None, 11])) == 29
    assert candidate(root = tree_node([10, -10, 20, 15, 7, None, -5, 20, 30])) == 65
    assert candidate(root = tree_node([1, -2, -3, 4, 5, None, 6, None, None, -8, -9])) == 7
    assert candidate(root = tree_node([-10, 5, 9, None, -3, None, -8, None, -2, None, 7, -5, None, -1, None, 6, None, None, None, None, None, None, 8])) == 9
    assert candidate(root = tree_node([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])) == 16
    assert candidate(root = tree_node([100, -50, -50, None, -100, -100, None, -50, -100, None, -150, -150])) == 100
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 30, 40, None, 50])) == 127


