def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, None, 2])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, None, 2])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, None, None, 2])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, None, None, 2])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 9, -20, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 9, -20, 10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 10, None, None, 8, 12, 1, None, None, 9, 11, 13])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 10, None, None, 8, 12, 1, None, None, 9, 11, 13])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, None, None, None, None, None, None, 18, 22])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, None, None, None, None, None, None, 18, 22])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, 4, 10, 18, 2, 5, 9, 12, 8, 16, 14, 19])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, 4, 10, 18, 2, 5, 9, 12, 8, 16, 14, 19])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 5, 18, 2, 8, 15, 25, 1, 3, 7, 10, 13, 17, 22, 27, None, None, None, None, 6, 9, None, None, None, None, 14, None, 11, 16, 19, 21, 24, 23, 26, 28, 29, 30])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 5, 18, 2, 8, 15, 25, 1, 3, 7, 10, 13, 17, 22, 27, None, None, None, None, 6, 9, None, None, None, None, 14, None, 11, 16, 19, 21, 24, 23, 26, 28, 29, 30])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 5, 20, 35, 50, 1, 7, 10, 25, 33, 40, 48, 60])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 5, 20, 35, 50, 1, 7, 10, 25, 33, 40, 48, 60])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, None, None, 4, None, 9, 11, 13, 14])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, None, None, 4, None, 9, 11, 13, 14])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 7, None, 14, None, None, 16, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 7, None, 14, None, None, 16, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 80, 20, 40, 70, 90, 10, 25, 35, 50, 65, 75, 85, 95, 5, 15, 22, 28, 32, 45, 48, 63, 73, 82, 88, 93, 98, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 80, 20, 40, 70, 90, 10, 25, 35, 50, 65, 75, 85, 95, 5, 15, 22, 28, 32, 45, 48, 63, 73, 82, 88, 93, 98, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 9, 1, 5, 8, 10, 0, 2, 4, 6, None, None, None, None, None, 11])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 9, 1, 5, 8, 10, 0, 2, 4, 6, None, None, None, None, None, 11])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 6, 1, 4, 3, 8, None, None, None, None, 7, 9])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 6, 1, 4, 3, 8, None, None, None, None, 7, 9])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 10, 2, 7, 9, 11, 1, 3, 6, None, None, None, None, None, 4])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 10, 2, 7, 9, 11, 1, 3, 6, None, None, None, None, None, 4])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 7, 11, 13])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 7, 11, 13])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 8, 1, 4, None, 10, None, None, 3, 6])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 8, 1, 4, None, 10, None, None, 3, 6])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 5, 12, 16, 25, 3, 7, 11, 13, 14, 17, 22, 30])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 5, 12, 16, 25, 3, 7, 11, 13, 14, 17, 22, 30])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 9, 15, 5, 11, 13, 18, 3, 6, 8, 10, 14, 16, 17, 19])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 9, 15, 5, 11, 13, 18, 3, 6, 8, 10, 14, 16, 17, 19])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 30, 10, 18, 25, 35, 5, 11, 16, 19, None, None, 14])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 30, 10, 18, 25, 35, 5, 11, 16, 19, None, None, 14])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 30, 10, 25, 28, 40, 5, 12, 18, 27, 35, 38, 45, 50])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 30, 10, 25, 28, 40, 5, 12, 18, 27, 35, 38, 45, 50])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 15, 8, None, None, 12, 20])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 15, 8, None, None, 12, 20])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 4, 20, None, None, 15, 60, None, None, 10, 25, None, None, 7, 12, None, 30])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 4, 20, None, None, 15, 60, None, None, 10, 25, None, None, 7, 12, None, 30])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45, None, None, 2, 8, 14, 16, 21, 24, 27, 31, 34, 37, 42, 48, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45, None, None, 2, 8, 14, 16, 21, 24, 27, 31, 34, 37, 42, 48, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([250, 125, 375, 62, 187, 312, 437, 31, 93, 156, 221, 278, 363, 412, 492, None, None, 15, 46, 78, 138, 171, 206, 254, 341, 400, 458, 518, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([250, 125, 375, 62, 187, 312, 437, 31, 93, 156, 221, 278, 363, 412, 492, None, None, 15, 46, 78, 138, 171, 206, 254, 341, 400, 458, 518, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, None, None, 18, 25, 35, 48, None, None, None, None, 22, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, None, None, 18, 25, 35, 48, None, None, None, None, 22, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 23, 35, 48, 1, 8, 11, 13, 16, 18, 21, 22, 27, 33, 42, 47, 53, None, 4, None, None, 6, 9, None, None, 14, None, 7, 10, None, None, None, None, 19, None, 24, None, 26, 28, 29, None, 31, 34, None, None, 38, None, 41, 43, None, 46, None, 49, None, 51, 52, None, 54, None, 55])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 23, 35, 48, 1, 8, 11, 13, 16, 18, 21, 22, 27, 33, 42, 47, 53, None, 4, None, None, 6, 9, None, None, 14, None, 7, 10, None, None, None, None, 19, None, 24, None, 26, 28, 29, None, 31, 34, None, None, 38, None, 41, 43, None, 46, None, 49, None, 51, 52, None, 54, None, 55])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 10, 25, 35, 45, 65, 75, 85, 105])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 10, 25, 35, 45, 65, 75, 85, 105])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 10, 15, 3, None, None, 20, None, None, None, 25])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 10, 15, 3, None, None, 20, None, None, None, 25])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, 5.5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, 5.5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 6, 7, 11, 13, 14, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 6, 7, 11, 13, 14, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 180, 5, 15, 28, 45, 65, 75, 105, 135, 155, 170, 190, None, None, None, None, 20, 35, None, 53, None, None, None, None, None, 54, None, 78, None, None, None, None, None, 115, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 180, 5, 15, 28, 45, 65, 75, 105, 135, 155, 170, 190, None, None, None, None, 20, 35, None, 53, None, None, None, None, None, 54, None, 78, None, None, None, None, None, 115, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 20, 50, 10, 25, 40, 60, None, None, 15, 27, 35, 55, 45, 65])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 20, 50, 10, 25, 40, 60, None, None, 15, 27, 35, 55, 45, 65])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, None, 2, None, 4, 6, 9, 11, 13])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, None, 2, None, 4, 6, 9, 11, 13])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 7, 10, 6, 8, 11, 12, 5, None, None, None, 13, 14])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 7, 10, 6, 8, 11, 12, 5, None, None, None, 13, 14])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 7, 12, 16, 25, 2, 6, 11, 14, 13, 17, 21, 30])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 7, 12, 16, 25, 2, 6, 11, 14, 13, 17, 21, 30])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 17, 21, 27, 26, 35])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 17, 21, 27, 26, 35])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([12, 9, 15, 6, 10, 13, 18, 2, 7, 8, 11, 14, 16, 17, 20])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([12, 9, 15, 6, 10, 13, 18, 2, 7, 8, 11, 14, 16, 17, 20])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, 5, 1, 3, 6, 7, 0, None, None, None, None, None, None, 8])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, 5, 1, 3, 6, 7, 0, None, None, None, None, None, None, 8])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, None, None, 6, 25, 4, None, 11, 17])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, None, None, 6, 25, 4, None, 11, 17])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([60, 30, 80, 10, 40, 70, 90, 5, 25, 35, 55, 65, 85, 95, None, 1, None, 15, 28, 40, 53, 63, 75, 88, 93, 100, None, None, 11, None, 26, None, 36, 45, 54, 64, 76, 89, None, None, None, None, None, 101])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([60, 30, 80, 10, 40, 70, 90, 5, 25, 35, 55, 65, 85, 95, None, 1, None, 15, 28, 40, 53, 63, 75, 88, 93, 100, None, None, 11, None, 26, None, 36, 45, 54, 64, 76, 89, None, None, None, None, None, 101])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 10, 2, 7, None, 15, 1, None, 6, 9, 12, 18, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 10, 2, 7, None, 15, 1, None, 6, 9, 12, 18, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 30, 60, 80, 110, 140, 180, 220, None, 12, 28, None, 55, 85, 105, 135, 165, 195, 210, 225, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 17, None, None, 100])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 30, 60, 80, 110, 140, 180, 220, None, 12, 28, None, 55, 85, 105, 135, 165, 195, 210, 225, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 17, None, None, 100])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 180, 5, 15, 28, 40, 65, 85, 105, 135, 155, 170, 190])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 180, 5, 15, 28, 40, 65, 85, 105, 135, 155, 170, 190])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 8, 14, 19, 24, 31, 47, 49, None, None, None, None, None, None, None, None, 9, None, None, 16, None, None, None, None, 23, None, None, None, None, 32, None, None, None, None, 46, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 8, 14, 19, 24, 31, 47, 49, None, None, None, None, None, None, None, None, 9, None, None, 16, None, None, None, None, 23, None, None, None, None, 32, None, None, None, None, 46, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 5, 12, 3, 7, 10, 15, 2, 4, 6, 8, 11, 13, 14, 17])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 5, 12, 3, 7, 10, 15, 2, 4, 6, 8, 11, 13, 14, 17])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 20, 40, 10, 25, 35, 50, 5, 15, None, None, 22, None, 27, 33, None, 45, 48, 55])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 20, 40, 10, 25, 35, 50, 5, 15, None, None, 22, None, 27, 33, None, 45, 48, 55])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, 8, 16])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, 8, 16])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, 7, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, 7, 10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 12, 3, 7, 10, 15, 2, 4, 6, 9, 11, 13, 14, 16])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 12, 3, 7, 10, 15, 2, 4, 6, 9, 11, 13, 14, 16])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, 16, 19, 21, 24, 28, 32, 3, 7, 11, 13, 17, 23, 27, 31])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, 16, 19, 21, 24, 28, 32, 3, 7, 11, 13, 17, 23, 27, 31])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 5, 12, 3, 7, 11, 14, 2, 4, 6, 8, 10, 13, None, None, None, None, None, None, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 5, 12, 3, 7, 11, 14, 2, 4, 6, 8, 10, 13, None, None, None, None, None, None, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([22, 10, 30, 5, 15, 25, 40, 2, 7, 13, 18, 21, 35, 38, 45, 1, 3, 6, 8, 11, 14, 17, 20, 24, 28, 33, 36, 43, 41, 44, 47, 48, 4, 9, 12, 16, 19, 23, 27, 29, 32, 34, 37, 42, 46, 49, 50, 51])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([22, 10, 30, 5, 15, 25, 40, 2, 7, 13, 18, 21, 35, 38, 45, 1, 3, 6, 8, 11, 14, 17, 20, 24, 28, 33, 36, 43, 41, 44, 47, 48, 4, 9, 12, 16, 19, 23, 27, 29, 32, 34, 37, 42, 46, 49, 50, 51])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([90, 60, 120, 30, 70, 100, 150, 10, 50, 65, 80, 95, 110, 140, 160, 5, 25, 45, 55, 75, 85, 92, 105, 125, 135, 155, 170, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([90, 60, 120, 30, 70, 100, 150, 10, 50, 65, 80, 95, 110, 140, 160, 5, 25, 45, 55, 75, 85, 92, 105, 125, 135, 155, 170, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 8, 12, 18, 22, 28, 32, 38, None, None, 4, None, 6, None, None, None, 9, None, None, 11, None, None, 14, None, None, 16, None, None, 19, None, None, 23, None, None, 27, None, None, 31, None, None, 34, None, None, 37, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 8, 12, 18, 22, 28, 32, 38, None, None, 4, None, 6, None, None, None, 9, None, None, 11, None, None, 14, None, None, 16, None, None, 19, None, None, 23, None, None, 27, None, None, 31, None, None, 34, None, None, 37, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, None, 12, 17, 25, 8, None, None, 13, None, 19, 16, 23])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, None, 12, 17, 25, 8, None, None, 13, None, 19, 16, 23])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, None, None, 5, 15, 30, 45, 65, 85, 95, 105, 120, 130, 145, 155, 170, 185, 195, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, None, None, 5, 15, 30, 45, 65, 85, 95, 105, 120, 130, 145, 155, 170, 185, 195, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 7, 11, 13, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 7, 11, 13, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([35, 20, 55, 10, 30, 50, 60, None, None, 25, 34, 45, 56, None, None, 27, 32, None, 33, 40, 47, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([35, 20, 55, 10, 30, 50, 60, None, None, 25, 34, 45, 56, None, None, 27, 32, None, 33, 40, 47, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, None, None, 10, 40, 60, 90, 110, 140, 160, 190, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, None, None, 10, 40, 60, 90, 110, 140, 160, 190, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, None, 25, 35, 55, 65, 75, 90])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, None, 25, 35, 55, 65, 75, 90])) == None: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([2, 3, 1])) == None
    assert candidate(root = tree_node([3, 1, 4, None, None, 2])) == None
    assert candidate(root = tree_node([5, 1, 4, None, None, 3, 6])) == None
    assert candidate(root = tree_node([1, 3, None, None, 2])) == None
    assert candidate(root = tree_node([3, 2, 1])) == None
    assert candidate(root = tree_node([5, 3, 9, -20, 10])) == None
    assert candidate(root = tree_node([10, 5, 15, None, None, 6, 20])) == None
    assert candidate(root = tree_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(root = tree_node([7, 3, 10, None, None, 8, 12, 1, None, None, 9, 11, 13])) == None
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 16, 25, None, None, None, None, None, None, 18, 22])) == None
    assert candidate(root = tree_node([7, 3, 15, None, 4, 10, 18, 2, 5, 9, 12, 8, 16, 14, 19])) == None
    assert candidate(root = tree_node([12, 5, 18, 2, 8, 15, 25, 1, 3, 7, 10, 13, 17, 22, 27, None, None, None, None, 6, 9, None, None, None, None, 14, None, 11, 16, 19, 21, 24, 23, 26, 28, 29, 30])) == None
    assert candidate(root = tree_node([30, 15, 45, 5, 20, 35, 50, 1, 7, 10, 25, 33, 40, 48, 60])) == None
    assert candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, None, None, 4, None, 9, 11, 13, 14])) == None
    assert candidate(root = tree_node([15, 10, 20, 5, 12, 18, 25, 3, 7, None, 14, None, None, 16, None, None, None, None, None])) == None
    assert candidate(root = tree_node([60, 30, 80, 20, 40, 70, 90, 10, 25, 35, 50, 65, 75, 85, 95, 5, 15, 22, 28, 32, 45, 48, 63, 73, 82, 88, 93, 98, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([7, 3, 9, 1, 5, 8, 10, 0, 2, 4, 6, None, None, None, None, None, 11])) == None
    assert candidate(root = tree_node([5, 2, 6, 1, 4, 3, 8, None, None, None, None, 7, 9])) == None
    assert candidate(root = tree_node([8, 5, 10, 2, 7, 9, 11, 1, 3, 6, None, None, None, None, None, 4])) == None
    assert candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 7, 11, 13])) == None
    assert candidate(root = tree_node([5, 2, 8, 1, 4, None, 10, None, None, 3, 6])) == None
    assert candidate(root = tree_node([15, 10, 20, 5, 12, 16, 25, 3, 7, 11, 13, 14, 17, 22, 30])) == None
    assert candidate(root = tree_node([12, 9, 15, 5, 11, 13, 18, 3, 6, 8, 10, 14, 16, 17, 19])) == None
    assert candidate(root = tree_node([20, 15, 30, 10, 18, 25, 35, 5, 11, 16, 19, None, None, 14])) == None
    assert candidate(root = tree_node([20, 15, 30, 10, 25, 28, 40, 5, 12, 18, 27, 35, 38, 45, 50])) == None
    assert candidate(root = tree_node([10, 15, 8, None, None, 12, 20])) == None
    assert candidate(root = tree_node([9, 4, 20, None, None, 15, 60, None, None, 10, 25, None, None, 7, 12, None, 30])) == None
    assert candidate(root = tree_node([25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22, 28, 32, 38, 45, None, None, 2, 8, 14, 16, 21, 24, 27, 31, 34, 37, 42, 48, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([250, 125, 375, 62, 187, 312, 437, 31, 93, 156, 221, 278, 363, 412, 492, None, None, 15, 46, 78, 138, 171, 206, 254, 341, 400, 458, 518, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, None, None, 18, 25, 35, 48, None, None, None, None, 22, None, None, None, None])) == None
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 23, 35, 48, 1, 8, 11, 13, 16, 18, 21, 22, 27, 33, 42, 47, 53, None, 4, None, None, 6, 9, None, None, 14, None, 7, 10, None, None, None, None, 19, None, 24, None, 26, 28, 29, None, 31, 34, None, None, 38, None, 41, 43, None, 46, None, 49, None, 51, 52, None, 54, None, 55])) == None
    assert candidate(root = tree_node([60, 30, 90, 20, 40, 70, 100, 10, 25, 35, 45, 65, 75, 85, 105])) == None
    assert candidate(root = tree_node([5, 10, 15, 3, None, None, 20, None, None, None, 25])) == None
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, 5.5])) == None
    assert candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 6, 7, 11, 13, 14, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 80, 110, 140, 160, 180, 5, 15, 28, 45, 65, 75, 105, 135, 155, 170, 190, None, None, None, None, 20, 35, None, 53, None, None, None, None, None, 54, None, 78, None, None, None, None, None, 115, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([30, 20, 50, 10, 25, 40, 60, None, None, 15, 27, 35, 55, 45, 65])) == None
    assert candidate(root = tree_node([7, 3, 10, 1, 5, 8, 12, None, 2, None, 4, 6, 9, 11, 13])) == None
    assert candidate(root = tree_node([9, 7, 10, 6, 8, 11, 12, 5, None, None, None, 13, 14])) == None
    assert candidate(root = tree_node([15, 10, 20, 7, 12, 16, 25, 2, 6, 11, 14, 13, 17, 21, 30])) == None
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, None, 17, 21, 27, 26, 35])) == None
    assert candidate(root = tree_node([12, 9, 15, 6, 10, 13, 18, 2, 7, 8, 11, 14, 16, 17, 20])) == None
    assert candidate(root = tree_node([4, 2, 5, 1, 3, 6, 7, 0, None, None, None, None, None, None, 8])) == None
    assert candidate(root = tree_node([15, 10, 20, None, None, 6, 25, 4, None, 11, 17])) == None
    assert candidate(root = tree_node([60, 30, 80, 10, 40, 70, 90, 5, 25, 35, 55, 65, 85, 95, None, 1, None, 15, 28, 40, 53, 63, 75, 88, 93, 100, None, None, 11, None, 26, None, 36, 45, 54, 64, 76, 89, None, None, None, None, None, 101])) == None
    assert candidate(root = tree_node([8, 5, 10, 2, 7, None, 15, 1, None, 6, 9, 12, 18, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 200, 10, 30, 60, 80, 110, 140, 180, 220, None, 12, 28, None, 55, 85, 105, 135, 165, 195, 210, 225, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 17, None, None, 100])) == None
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 180, 5, 15, 28, 40, 65, 85, 105, 135, 155, 170, 190])) == None
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 8, 14, 19, 24, 31, 47, 49, None, None, None, None, None, None, None, None, 9, None, None, 16, None, None, None, None, 23, None, None, None, None, 32, None, None, None, None, 46, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([9, 5, 12, 3, 7, 10, 15, 2, 4, 6, 8, 11, 13, 14, 17])) == None
    assert candidate(root = tree_node([30, 20, 40, 10, 25, 35, 50, 5, 15, None, None, 22, None, 27, 33, None, 45, 48, 55])) == None
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20, None, None, 8, 16])) == None
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, 7, 10])) == None
    assert candidate(root = tree_node([8, 5, 12, 3, 7, 10, 15, 2, 4, 6, 9, 11, 13, 14, 16])) == None
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 12, 16, 19, 21, 24, 28, 32, 3, 7, 11, 13, 17, 23, 27, 31])) == None
    assert candidate(root = tree_node([9, 5, 12, 3, 7, 11, 14, 2, 4, 6, 8, 10, 13, None, None, None, None, None, None, 1])) == None
    assert candidate(root = tree_node([22, 10, 30, 5, 15, 25, 40, 2, 7, 13, 18, 21, 35, 38, 45, 1, 3, 6, 8, 11, 14, 17, 20, 24, 28, 33, 36, 43, 41, 44, 47, 48, 4, 9, 12, 16, 19, 23, 27, 29, 32, 34, 37, 42, 46, 49, 50, 51])) == None
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == None
    assert candidate(root = tree_node([90, 60, 120, 30, 70, 100, 150, 10, 50, 65, 80, 95, 110, 140, 160, 5, 25, 45, 55, 75, 85, 92, 105, 125, 135, 155, 170, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 1, 8, 12, 18, 22, 28, 32, 38, None, None, 4, None, 6, None, None, None, 9, None, None, 11, None, None, 14, None, None, 16, None, None, 19, None, None, 23, None, None, 27, None, None, 31, None, None, 34, None, None, 37, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([15, 10, 20, None, 12, 17, 25, 8, None, None, 13, None, 19, 16, 23])) == None
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 40, 60, 90, 110, 140, 160, 190, None, None, 5, 15, 30, 45, 65, 85, 95, 105, 120, 130, 145, 155, 170, 185, 195, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([8, 3, 10, 1, 5, 9, 12, None, 2, 4, 7, 11, 13, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([35, 20, 55, 10, 30, 50, 60, None, None, 25, 34, 45, 56, None, None, 27, 32, None, 33, 40, 47, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, None, None, 10, 40, 60, 90, 110, 140, 160, 190, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == None
    assert candidate(root = tree_node([50, 30, 70, 20, 40, 60, 80, None, 25, 35, 55, 65, 75, 90])) == None


