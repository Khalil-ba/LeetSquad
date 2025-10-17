def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 1) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 4) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 11,q = 13) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 11,q = 13) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 12, 18, None, None, 22, 28, None, None, None, None]),p = 12,q = 28) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 12, 18, None, None, 22, 28, None, None, None, None]),p = 12,q = 28) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 9,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 9,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 3,q = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 3,q = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 5,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 5,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 1,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 1,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 3,q = 18) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 3,q = 18) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 10]),p = 2,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 10]),p = 2,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 9, None, None, 13, 14]),p = 12,q = 14) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 9, None, None, 13, 14]),p = 12,q = 14) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 6,q = 9) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 6,q = 9) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),p = 3,q = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),p = 3,q = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]),p = 50,q = 75) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]),p = 50,q = 75) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18, None, None, 19, 20, None, None, 21, 22]),p = 21,q = 22) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18, None, None, 19, 20, None, None, 21, 22]),p = 21,q = 22) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 1,q = 31) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 1,q = 31) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 10,q = 9) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 10,q = 9) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, None]),p = 1,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, None]),p = 1,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 15,q = 25) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 15,q = 25) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, None, None, None, None, None, 7]),p = 2,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, None, None, None, None, None, 7]),p = 2,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 1,q = 32) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 1,q = 32) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 25, 40, 20, 28, 35, 50, 15, 22, 26, 29, 32, 38, 45, 55]),p = 26,q = 38) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 25, 40, 20, 28, 35, 50, 15, 22, 26, 29, 32, 38, 45, 55]),p = 26,q = 38) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 47, None, None, 8, 13, None, 22, None, None, None, None, 42, 46]),p = 35,q = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 47, None, None, 8, 13, None, 22, None, None, None, None, 42, 46]),p = 35,q = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 6,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 6,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 14,q = 19) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 14,q = 19) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, 7, 8, 1, 9, None, None, None, None, 10, None, None, None, None, 11]),p = 2,q = 11) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, 7, 8, 1, 9, None, None, None, None, 10, None, None, None, None, 11]),p = 2,q = 11) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 14,q = 13) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 14,q = 13) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None]),p = 10,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None]),p = 10,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18, None, None, 19, 20]),p = 19,q = 20) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18, None, None, 19, 20]),p = 19,q = 20) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 9,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 9,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 1,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 1,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 12,q = 17) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 12,q = 17) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 5,q = 9) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 5,q = 9) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None]),p = 6,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None]),p = 6,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 11,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 11,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]),p = 80,q = 140) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]),p = 80,q = 140) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 3,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 3,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, None, 14, None, None, None, None, None, None, None, None, None, 15]),p = 13,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, None, 14, None, None, None, None, None, None, None, None, None, 15]),p = 13,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 7,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 7,q = 4) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 30,q = 13) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 30,q = 13) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 3,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 3,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 2,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 2,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 5,q = 14) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 5,q = 14) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),p = 80,q = 140) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),p = 80,q = 140) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, None, None, 7, None, 8]),p = 6,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, None, None, 7, None, 8]),p = 6,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5, 6, 7, 8, 9, None, None, 10, 11, None, None, None, None, None, None, None, None, None, 12, 13, None, None, None, None, None, None, None, None, None, None, 14, 15]),p = 8,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5, 6, 7, 8, 9, None, None, 10, 11, None, None, None, None, None, None, None, None, None, 12, 13, None, None, None, None, None, None, None, None, None, None, 14, 15]),p = 8,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 14) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 14) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 35, 60, 90, 125, 175, 250, 350, 5, 15, 30, 40, 55, 65, 85, 95, 115, 135, 165, 185, 235, 275, 325, 375]),p = 10,q = 95) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 35, 60, 90, 125, 175, 250, 350, 5, 15, 30, 40, 55, 65, 85, 95, 115, 135, 165, 185, 235, 275, 325, 375]),p = 10,q = 95) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1]),p = 2,q = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1]),p = 2,q = 1) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 2,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 2,q = 4) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 6,q = 11) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 6,q = 11) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 4,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 4,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),p = 3,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),p = 3,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),p = 12,q = 25) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),p = 12,q = 25) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16]),p = 6,q = 16) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16]),p = 6,q = 16) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),p = 10,q = 30) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),p = 10,q = 30) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, None, None, None, None, 51, None, None, None, None, 52, None, None, None, None, 53, None, None, None, None, 54, None, None, None, None, 55, None, None, None, None, 56, None, None, None, None, 57, None, None, None, None, 58, None, None, None, None, 59, None, None, None, None, 60]),p = 51,q = 59) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, None, None, None, None, 51, None, None, None, None, 52, None, None, None, None, 53, None, None, None, None, 54, None, None, None, None, 55, None, None, None, None, 56, None, None, None, None, 57, None, None, None, None, 58, None, None, None, None, 59, None, None, None, None, 60]),p = 51,q = 59) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 9,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 9,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70]),p = -20,q = -50) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70]),p = -20,q = -50) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, None, None, 17, None, None, 18, None, None, None, None, 19, None, 20, None, None, 21, None, None, None, None, 22, None, None, None, None, 23, None, None, None, None, 24, None, None, None, None, None, None, 25]),p = 18,q = 25) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, None, None, 17, None, None, 18, None, None, None, None, 19, None, 20, None, None, 21, None, None, None, None, 22, None, None, None, None, 23, None, None, None, None, 24, None, None, None, None, None, None, 25]),p = 18,q = 25) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 15,q = 18) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 15,q = 18) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 1,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 1,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 2,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 2,q = 4) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),p = 17,q = 49) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),p = 17,q = 49) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, 11, 12]),p = 6,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, 11, 12]),p = 6,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 10,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 10,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 9, 10, None, None, 11, 12]),p = 2,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 9, 10, None, None, 11, 12]),p = 2,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 2,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 2,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 3,q = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 3,q = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 3,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 3,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18]),p = 11,q = 18) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18]),p = 11,q = 18) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),p = 15,q = 20) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),p = 15,q = 20) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 60, 10, 20, 45, 75, None, None, 12, 18, None, None, None, None, 40, 50]),p = 12,q = 50) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 60, 10, 20, 45, 75, None, None, 12, 18, None, None, None, None, 40, 50]),p = 12,q = 50) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 16,q = 18) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 16,q = 18) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 2,q = 31) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 2,q = 31) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 16,q = 30) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 16,q = 30) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),p = 6,q = 18) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),p = 6,q = 18) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 10, None, None, 11]),p = 2,q = 11) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 10, None, None, 11]),p = 2,q = 11) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 19, 3, 7, None, 20, 1, None, 6, 8]),p = 6,q = 20) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 19, 3, 7, None, 20, 1, None, 6, 8]),p = 6,q = 20) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 10,q = 18) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 10,q = 18) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 2,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 2,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 2,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 2,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, None, None, None, None, 13, None, None, None, None, None, None, None, 14, None, 15]),p = 15,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, None, None, None, None, 13, None, None, None, None, None, None, None, 14, None, 15]),p = 15,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 2,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 2,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 14) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 14) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 11) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 11) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 15,q = 20) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 15,q = 20) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 6,q = 11) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 6,q = 11) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 8,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 8,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 2,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 2,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 3,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 3,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 2,q = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 2,q = 1) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 20,q = 27) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 20,q = 27) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 1,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 1,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 13, 14]),p = 13,q = 14) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 13, 14]),p = 13,q = 14) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 1,q = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 1,q = 3) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 11) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 11) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 5,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 5,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 20,q = 25) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 20,q = 25) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 7,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 7,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 1,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 1,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 2,q = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 2,q = 3) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1]),p = 1,q = 2) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1]),p = 1,q = 2) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 1,q = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 1,q = 3) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, 6]),p = 4,q = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, 6]),p = 4,q = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 3,q = 2) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 3,q = 2) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 1,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 1,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13]),p = 9,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13]),p = 9,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 1,q = 10) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 1,q = 10) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, None, 3, None, 1]),p = 2,q = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, None, 3, None, 1]),p = 2,q = 3) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),p = 2,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),p = 2,q = 4) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 4,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 4,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 5,q = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 5,q = 3) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 8,q = 11) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 8,q = 11) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 3,q = 2) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 3,q = 2) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 14,q = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 14,q = 3) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 13) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 13) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 7,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 7,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 0,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 0,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 6,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 6,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 3,q = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 3,q = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 16,q = 9) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 16,q = 9) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 10,q = 11) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 10,q = 11) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 4,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 4,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 14) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 14) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 3,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 3,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 4,q = 5) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 4,q = 5) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2]),p = 1,q = 2) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2]),p = 1,q = 2) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 8,q = 9) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 8,q = 9) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 5,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 5,q = 4) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 7,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 7,q = 4) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, 12, 13, 14, 15, None, None, None, None, 16]),p = 14,q = 15) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, 12, 13, 14, 15, None, None, None, None, 16]),p = 14,q = 15) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 2,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 2,q = 4) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 11,q = 12) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 11,q = 12) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 1,q = 8) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 1,q = 8) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 7,q = 13) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 7,q = 13) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3]),p = 1,q = 3) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3]),p = 1,q = 3) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 5,q = 6) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 5,q = 6) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 3,q = 7) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 3,q = 7) == None: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, None, None, 7, 4]),p = 6,q = 4) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, None, None, 7, 4]),p = 6,q = 4) == None: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 1) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 4) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 5,q = 10) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 11,q = 13) == None
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 12, 18, None, None, 22, 28, None, None, None, None]),p = 12,q = 28) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 9,q = 10) == None
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 3,q = 5) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 5,q = 15) == None
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 1,q = 7) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 3,q = 18) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 10]),p = 2,q = 10) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, 9, None, None, 13, 14]),p = 12,q = 14) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 6,q = 9) == None
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5]),p = 3,q = 5) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]),p = 50,q = 75) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18, None, None, 19, 20, None, None, 21, 22]),p = 21,q = 22) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 1,q = 31) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 10,q = 9) == None
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, None]),p = 1,q = 6) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 15,q = 25) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, None, None, None, None, None, 7]),p = 2,q = 7) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 1,q = 32) == None
    assert candidate(root = tree_node([30, 25, 40, 20, 28, 35, 50, 15, 22, 26, 29, 32, 38, 45, 55]),p = 26,q = 38) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 15) == None
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 47, None, None, 8, 13, None, 22, None, None, None, None, 42, 46]),p = 35,q = 5) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 6,q = 7) == None
    assert candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 14,q = 19) == None
    assert candidate(root = tree_node([5, 3, 6, 2, 4, 7, 8, 1, 9, None, None, None, None, 10, None, None, None, None, 11]),p = 2,q = 11) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 14,q = 13) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None]),p = 10,q = 7) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18, None, None, 19, 20]),p = 19,q = 20) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 9,q = 10) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 1,q = 10) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 15) == None
    assert candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 12,q = 17) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 5,q = 9) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None]),p = 6,q = 10) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 15) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 11,q = 12) == None
    assert candidate(root = tree_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]),p = 80,q = 140) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 3,q = 12) == None
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, None, None, None, 14, None, None, None, None, None, None, None, None, None, 15]),p = 13,q = 10) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 7,q = 4) == None
    assert candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 30,q = 13) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 3,q = 7) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 2,q = 8) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 5,q = 14) == None
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),p = 80,q = 140) == None
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, None, None, 7, None, 8]),p = 6,q = 8) == None
    assert candidate(root = tree_node([1, 2, 3, None, 5, 6, 7, 8, 9, None, None, 10, 11, None, None, None, None, None, None, None, None, None, 12, 13, None, None, None, None, None, None, None, None, None, None, 14, 15]),p = 8,q = 15) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 14) == None
    assert candidate(root = tree_node([100, 50, 200, 25, 75, 150, 300, 10, 35, 60, 90, 125, 175, 250, 350, 5, 15, 30, 40, 55, 65, 85, 95, 115, 135, 165, 185, 235, 275, 325, 375]),p = 10,q = 95) == None
    assert candidate(root = tree_node([2, 1]),p = 2,q = 1) == None
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 2,q = 4) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 6,q = 11) == None
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 4,q = 6) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),p = 3,q = 7) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),p = 12,q = 25) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16]),p = 6,q = 16) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),p = 10,q = 30) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, None, None, None, None, 51, None, None, None, None, 52, None, None, None, None, 53, None, None, None, None, 54, None, None, None, None, 55, None, None, None, None, 56, None, None, None, None, 57, None, None, None, None, 58, None, None, None, None, 59, None, None, None, None, 60]),p = 51,q = 59) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 9,q = 12) == None
    assert candidate(root = tree_node([-10, -20, -30, -40, -50, -60, -70]),p = -20,q = -50) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, None, None, 17, None, None, 18, None, None, None, None, 19, None, 20, None, None, 21, None, None, None, None, 22, None, None, None, None, 23, None, None, None, None, 24, None, None, None, None, None, None, 25]),p = 18,q = 25) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 15,q = 18) == None
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 1,q = 6) == None
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 2,q = 4) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 15) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 10) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),p = 17,q = 49) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, 11, 12]),p = 6,q = 12) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 10,q = 15) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 9, 10, None, None, 11, 12]),p = 2,q = 10) == None
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),p = 2,q = 6) == None
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 3,q = 5) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 3,q = 10) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16, None, None, 17, 18]),p = 11,q = 18) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),p = 15,q = 20) == None
    assert candidate(root = tree_node([30, 15, 60, 10, 20, 45, 75, None, None, 12, 18, None, None, None, None, 40, 50]),p = 12,q = 50) == None
    assert candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 16,q = 18) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 2,q = 31) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 16,q = 30) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),p = 6,q = 18) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5, None, None, None, None, None, 10, None, None, 11]),p = 2,q = 11) == None
    assert candidate(root = tree_node([10, 5, 19, 3, 7, None, 20, 1, None, 6, 8]),p = 6,q = 20) == None
    assert candidate(root = tree_node([30, 15, None, 10, 18, None, 12, 13, None, 16, 17, 19, None, 14]),p = 10,q = 18) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 2,q = 15) == None
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),p = 2,q = 15) == None
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, None, None, None, None, 13, None, None, None, None, None, None, None, 14, None, 15]),p = 15,q = 12) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 2,q = 7) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 14) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 11) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 15,q = 20) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 6,q = 11) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 8,q = 12) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 2,q = 8) == None
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, 5, None, 6]),p = 3,q = 6) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10]),p = 2,q = 1) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),p = 20,q = 27) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 1,q = 15) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, 13, 14]),p = 13,q = 14) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 1,q = 3) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 11) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 6,q = 7) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, None, None, 11, 12]),p = 5,q = 8) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 20,q = 25) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, 9, 10, None, None, 11, 12]),p = 7,q = 12) == None
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9]),p = 1,q = 7) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 2,q = 3) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 5) == None
    assert candidate(root = tree_node([1]),p = 1,q = 2) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 8) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 1,q = 3) == None
    assert candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, 6]),p = 4,q = 5) == None
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 3,q = 2) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 1,q = 7) == None
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13]),p = 9,q = 12) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 1,q = 10) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 7) == None
    assert candidate(root = tree_node([4, 2, None, 3, None, 1]),p = 2,q = 3) == None
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, None, 1]),p = 2,q = 4) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 6) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 4,q = 6) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 5,q = 3) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 8,q = 11) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 3,q = 2) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 14,q = 3) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 8,q = 13) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 7,q = 8) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 0,q = 8) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 6,q = 7) == None
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 3,q = 5) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 2,q = 8) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 16,q = 9) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 16]),p = 10,q = 11) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 4,q = 6) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 10,q = 14) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 4,q = 12) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 3,q = 7) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),p = 4,q = 5) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 6,q = 7) == None
    assert candidate(root = tree_node([1, 2]),p = 1,q = 2) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 8,q = 9) == None
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 5,q = 4) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 7,q = 4) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, 12, 13, 14, 15, None, None, None, None, 16]),p = 14,q = 15) == None
    assert candidate(root = tree_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),p = 2,q = 4) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),p = 11,q = 12) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),p = 1,q = 8) == None
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),p = 7,q = 13) == None
    assert candidate(root = tree_node([2, 1, 3]),p = 1,q = 3) == None
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5]),p = 5,q = 6) == None
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),p = 3,q = 7) == None
    assert candidate(root = tree_node([3, 5, 1, 6, 2, None, None, 7, 4]),p = 6,q = 4) == None


