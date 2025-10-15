def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, -3])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, -3])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, -3, 4, None, None, -4])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, -3, 4, None, None, -4])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 7, 0, 7, -8, None, None])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 7, 0, 7, -8, None, None])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([989, None, 10250, 98693, -89388, None, None, None, -32127])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([989, None, 10250, 98693, -89388, None, None, None, -32127])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10000, 10000, -10000, 10000, -10000, 10000, -10000])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10000, 10000, -10000, 10000, -10000, 10000, -10000])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, None, 8, None, 9, 10])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, None, 8, None, 9, 10])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -2, -3, -4, None, None, -5, None, -6, None, None, None, None, None, -7])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -2, -3, -4, None, None, -5, None, -6, None, None, None, None, None, -7])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, -1000, 2000, 3000, -4000, 5000, None, -6000, None, 7000, None, 8000, None, 9000, None, 10000])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, -1000, 2000, 3000, -4000, 5000, None, -6000, None, 7000, None, 8000, None, 9000, None, 10000])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, None, None, 20])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, None, None, 20])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, None, None, -1, None, -1, 8])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, None, None, -1, None, -1, 8])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -5, 3, 4, -6, 10, -15, 0, 2, None, -8, None, 9, None, None, None, None, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -5, 3, 4, -6, 10, -15, 0, 2, None, -8, None, 9, None, None, None, None, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 5, None, None, 10, None, None, -10, None, None, -20, None, None, 30, None, None, 40, None, None, -50, None, None, -60])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 5, None, None, 10, None, None, -10, None, None, -20, None, None, 30, None, None, 40, None, None, -50, None, None, -60])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 2, 5, 3, None, 9, 0, 2])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 2, 5, 3, None, 9, 0, 2])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 2, None, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 2, None, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, None, None, 16, 17, None, None, 32, 33])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, None, None, 16, 17, None, None, 32, 33])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, 12, 20])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, 12, 20])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -200, 300, -1000, 500, -1500, 700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -200, 300, -1000, 500, -1500, 700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -100, 100, -100, 100, -100, 100, -100, 100, 100, -100, -100, 100, 100, -100])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -100, 100, -100, 100, -100, 100, -100, 100, 100, -100, -100, 100, 100, -100])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, 4, None, 5, 6, 7, None, None, 8, None, None, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, 4, None, 5, 6, 7, None, None, 8, None, None, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, -4, 6, -7, 8, 9, -10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, -4, 6, -7, 8, 9, -10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, -32])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, -32])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -200, 300, 400, None, -500, 600, None, None, 700, -800, None, None, 900])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -200, 300, 400, None, -500, 600, None, None, 700, -800, None, None, 900])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 98, 102, None, None, 96, 104, 95, 99, 101, 103, 97, 105, None, None, None, None, None, None, None, None, 94, None, None, 93, None, None, 92, None, None, 91, None, None, 90, None, None, 89, None, None, 88, None, None, 87, None, None, 86, None, None, 85, None, None, 84, None, None, 83, None, None, 82, None, None, 81, None, None, 80])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 98, 102, None, None, 96, 104, 95, 99, 101, 103, 97, 105, None, None, None, None, None, None, None, None, 94, None, None, 93, None, None, 92, None, None, 91, None, None, 90, None, None, 89, None, None, 88, None, None, 87, None, None, 86, None, None, 85, None, None, 84, None, None, 83, None, None, 82, None, None, 81, None, None, 80])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, -5, None, -1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, -5, None, -1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, None, 30])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, None, 30])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, -2, -3, -4, 5, None, -6, None, -7, None, -8, None, -9])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, -2, -3, -4, 5, None, -6, None, -7, None, -8, None, -9])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, -100, -200, -300, -400, -500])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, -100, -200, -300, -400, -500])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 25, 20, 10, 5, None, None, None, None, 30])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 25, 20, 10, 5, None, None, None, None, 30])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, 8, None, None, 9, 10, None, None, 11, 12])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, 8, None, None, 9, 10, None, None, 11, 12])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 93, 97, 103, 107, 115, 125])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 93, 97, 103, 107, 115, 125])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5, None, 7, None, None, None, None, 14, None, None, 28])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5, None, 7, None, None, None, None, 14, None, None, 28])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, -1, -2, -3, -4, -5, -6, -7, -8])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, -1, -2, -3, -4, -5, -6, -7, -8])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, -6, 6, None, 7, 8, 9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, -6, 6, None, 7, 8, 9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, -10, None, -10, None, -10, None, -10])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, -10, None, -10, None, -10, None, -10])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, 16, 19])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, 16, 19])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, 12, None, None, 13, 14, 15])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, 12, None, None, 13, 14, 15])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8])) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([1, -1, 2, -2, 3, -3, 4])) == 3
    assert candidate(root = tree_node([5, 2, -3])) == 1
    assert candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70])) == 1
    assert candidate(root = tree_node([1, -2, -3, 4, None, None, -4])) == 1
    assert candidate(root = tree_node([1, 7, 0, 7, -8, None, None])) == 2
    assert candidate(root = tree_node([989, None, 10250, 98693, -89388, None, None, None, -32127])) == 2
    assert candidate(root = tree_node([5])) == 1
    assert candidate(root = tree_node([-10000, 10000, -10000, 10000, -10000, 10000, -10000])) == 2
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, None, 8, None, 9, 10])) == 4
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 3
    assert candidate(root = tree_node([-1, -2, -3, -4, None, None, -5, None, -6, None, None, None, None, None, -7])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9, 10, 11, 12, 13, 14, 15])) == 5
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20])) == 4
    assert candidate(root = tree_node([1000, -1000, 2000, 3000, -4000, 5000, None, -6000, None, 7000, None, 8000, None, 9000, None, 10000])) == 5
    assert candidate(root = tree_node([100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100, -100, 100])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 5
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, None, None, 20])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 6
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, None, None, -1, None, -1, 8])) == 3
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
    assert candidate(root = tree_node([10, -5, 3, 4, -6, 10, -15, 0, 2, None, -8, None, 9, None, None, None, None, None, 5])) == 1
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) == 5
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 4
    assert candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == 3
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, 5, None, None, 10, None, None, -10, None, None, -20, None, None, 30, None, None, 40, None, None, -50, None, None, -60])) == 2
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 0, 2, 5, 3, None, 9, 0, 2])) == 4
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, None, 2, None, 1])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, None, None, 16, 17, None, None, 32, 33])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5])) == 4
    assert candidate(root = tree_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])) == 1
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8])) == 2
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, 12, 20])) == 4
    assert candidate(root = tree_node([100, -200, 300, -1000, 500, -1500, 700, 800, -900, 1000, -1100, 1200, -1300, 1400, -1500])) == 1
    assert candidate(root = tree_node([100, -100, 100, -100, 100, -100, 100, -100, 100, 100, -100, -100, 100, 100, -100])) == 1
    assert candidate(root = tree_node([1, None, 2, 3, 4, None, 5, 6, 7, None, None, 8, None, None, 9])) == 4
    assert candidate(root = tree_node([5, -4, 6, -7, 8, 9, -10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])) == 4
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190])) == 4
    assert candidate(root = tree_node([1000, 500, 1500, 250, 750, 1250, 1750, 125, 375, 625, 875, 1125, 1375, 1625, 1875])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, -32])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5])) == 2
    assert candidate(root = tree_node([100, -200, 300, 400, None, -500, 600, None, None, 700, -800, None, None, 900])) == 5
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15
    assert candidate(root = tree_node([100, 98, 102, None, None, 96, 104, 95, 99, 101, 103, 97, 105, None, None, None, None, None, None, None, None, 94, None, None, 93, None, None, 92, None, None, 91, None, None, 90, None, None, 89, None, None, 88, None, None, 87, None, None, 86, None, None, 85, None, None, 84, None, None, 83, None, None, 82, None, None, 81, None, None, 80])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
    assert candidate(root = tree_node([5, 2, -5, None, -1])) == 1
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, None, None, None, 30])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 5
    assert candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 5
    assert candidate(root = tree_node([1, None, -2, -3, -4, 5, None, -6, None, -7, None, -8, None, -9])) == 1
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 5
    assert candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == 1
    assert candidate(root = tree_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, -100, -200, -300, -400, -500])) == 3
    assert candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 25, 20, 10, 5, None, None, None, None, 30])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, 8, None, None, 9, 10, None, None, 11, 12])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 4
    assert candidate(root = tree_node([100, 90, 110, 80, 95, 105, 120, 70, 85, 93, 97, 103, 107, 115, 125])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 5
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 7, None, None, None, None, 14, None, None, 28])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4
    assert candidate(root = tree_node([-10, 9, 20, None, None, 15, 7, -1, -2, -3, -4, -5, -6, -7, -8])) == 2
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 5
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 5
    assert candidate(root = tree_node([5, -6, 6, None, 7, 8, 9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50])) == 4
    assert candidate(root = tree_node([10, 9, -10, None, -10, None, -10, None, -10])) == 1
    assert candidate(root = tree_node([1, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 1
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6, None, 11, 14, 16, 19])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, 10, 11, 12, None, None, 13, 14, 15])) == 8
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1, None, None, None, None])) == 3
    assert candidate(root = tree_node([10, 9, 20, None, None, 15, 7, 1, 2, 3, 4, 5, 6, 7, 8])) == 2


