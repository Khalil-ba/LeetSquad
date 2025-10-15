def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1]),distance = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1]),distance = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4]),distance = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4]),distance = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]),distance = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]),distance = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, None, None, None, 9]),distance = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, None, None, None, 9]),distance = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),distance = 7) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),distance = 7) == 56: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7, None, None, None, None, 8, 9, None, None, None, None, 10, 11, None, None, None, None, 12, 13, None, None, None, None, 14, 15, None, None, None, None, 16, 17, None, None, None, None, 18, 19, None, None, None, None, 20, 21]),distance = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7, None, None, None, None, 8, 9, None, None, None, None, 10, 11, None, None, None, None, 12, 13, None, None, None, None, 14, 15, None, None, None, None, 16, 17, None, None, None, None, 18, 19, None, None, None, None, 20, 21]),distance = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, None, None, 8, 9]),distance = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, None, None, 8, 9]),distance = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, 7, None, None, None, 8, None, 9, None, None, 10, None, None, None, None, None, None, None, None, None, 11, None, None, None, None, None, None, None, None, None, 12, None, None, None, None, None, None, None, None, None, 13, None, None, None, None, None, None, None, None, None, 14, None, None, None, None, None, None, None, None, None, 15]),distance = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, 7, None, None, None, 8, None, 9, None, None, 10, None, None, None, None, None, None, None, None, None, 11, None, None, None, None, None, None, None, None, None, 12, None, None, None, None, None, None, None, None, None, 13, None, None, None, None, None, None, None, None, None, 14, None, None, None, None, None, None, None, None, None, 15]),distance = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12]),distance = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12]),distance = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30]),distance = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30]),distance = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),distance = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),distance = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None]),distance = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None]),distance = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, None, 6, None, None, None, None, None, 7]),distance = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, None, 6, None, None, None, None, None, 7]),distance = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, 10, None, None, None, None, None, 11, None, 12, 13, None, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, 10, None, None, None, None, None, 11, None, 12, 13, None, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),distance = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),distance = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),distance = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),distance = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25]),distance = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25]),distance = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, 9, 10, 11, 12, None, None, 13, 14, None, None, 15, 16]),distance = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, 9, 10, 11, 12, None, None, 13, 14, None, None, 15, 16]),distance = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, None, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),distance = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, None, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),distance = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),distance = 5) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),distance = 5) == 45: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13]),distance = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13]),distance = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, 12, 14]),distance = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, 12, 14]),distance = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, None, None, None, 10, 11, None, None, None, None, None, None, None, None, 12]),distance = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, None, None, None, 10, 11, None, None, None, None, None, None, None, None, 12]),distance = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),distance = 6) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),distance = 6) == 38: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, None, 9]),distance = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, None, 9]),distance = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, 10, 11, None, None, None, None, None, None, 12, 13, None, None, None, None, None, None, 14, 15]),distance = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, 10, 11, None, None, None, None, None, None, 12, 13, None, None, None, None, None, None, 14, 15]),distance = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),distance = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),distance = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None, None, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None, None, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, 7, None, None, None, 8, 9, 10, None, None, None, None, None, None, None, None, None, None, 11]),distance = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, 7, None, None, None, 8, 9, 10, None, None, None, None, None, None, None, None, None, None, 11]),distance = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),distance = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),distance = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),distance = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),distance = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 4, None, 2, None, 3, 6, 7, None, 8, None, 9, 10, 11, None, None, None, None, None, None]),distance = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 4, None, 2, None, 3, 6, 7, None, 8, None, 9, 10, 11, None, None, None, None, None, None]),distance = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),distance = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),distance = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40, None, 41, None, 42, None, 43, None, 44, None, 45, None, 46, None, 47, None, 48, None, 49, None, 50]),distance = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40, None, 41, None, 42, None, 43, None, 44, None, 45, None, 46, None, 47, None, 48, None, 49, None, 50]),distance = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19, None, None, None, None, None, None, None, None, 2, None, 9]),distance = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19, None, None, None, None, None, None, None, None, 2, None, 9]),distance = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, None, 10, None, None, 11]),distance = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, None, 10, None, None, 11]),distance = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),distance = 6) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),distance = 6) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, 8, 9]),distance = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, 8, 9]),distance = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]),distance = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]),distance = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9, None, None, None, None, None, None, None, None, None, 10]),distance = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9, None, None, None, None, None, None, None, None, None, 10]),distance = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),distance = 4) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),distance = 4) == 24: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, 8, 9, None, None, None, None, 10, None, 11, None, None, None, None, None, None, None, None, None]),distance = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, 8, 9, None, None, None, None, 10, None, 11, None, None, None, None, None, None, None, None, None]),distance = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15]),distance = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15]),distance = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, 10, None, None, 11, None, None, 12]),distance = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, 10, None, None, 11, None, None, 12]),distance = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),distance = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),distance = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, None, 41, None, 42]),distance = 4) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, None, 41, None, 42]),distance = 4) == 26: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),distance = 10) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),distance = 10) == 300: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, None, None]),distance = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, None, None]),distance = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, None, None, 7]),distance = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, None, None, 7]),distance = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, None, None, None, None, None, None, 7, 8, None, None, None, None, None, None, None, None, 9, 10, None, None, None, None, None, None, None, None, None, 11, 12, None, None, None, None, None, None, None, None, None, 13, 14, None, None, None, None, None, None, None, None, None, 15, 16, None, None, None, None, None, None, None, None, None, 17, 18]),distance = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, None, None, None, None, None, None, 7, 8, None, None, None, None, None, None, None, None, 9, 10, None, None, None, None, None, None, None, None, None, 11, 12, None, None, None, None, None, None, None, None, None, 13, 14, None, None, None, None, None, None, None, None, None, 15, 16, None, None, None, None, None, None, None, None, None, 17, 18]),distance = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9]),distance = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9]),distance = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 43, 55, 70, 81, 93, 3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 61, 67, 73, 77, 83, 89, 95, None, 10, 19, 28, 35, 41, 47, 53, 59, 65, 71, 75, 79, 85, 91, 97, None, 13, 23, 32, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100, None, None, None, 16, 22, 29, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, None, None, None, None, None, 20, 26, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, None, None, None, None, None, None, None, None, 24, 30, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95, None, None, None, None, None, None, None, None, None, 28, 33, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98, None, None, None, None, None, None, None, None, None, None, None, 32, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, None, None, None, None, None, None, None, None, None, None, None, None, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100]),distance = 5) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 43, 55, 70, 81, 93, 3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 61, 67, 73, 77, 83, 89, 95, None, 10, 19, 28, 35, 41, 47, 53, 59, 65, 71, 75, 79, 85, 91, 97, None, 13, 23, 32, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100, None, None, None, 16, 22, 29, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, None, None, None, None, None, 20, 26, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, None, None, None, None, None, None, None, None, 24, 30, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95, None, None, None, None, None, None, None, None, None, 28, 33, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98, None, None, None, None, None, None, None, None, None, None, None, 32, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, None, None, None, None, None, None, None, None, None, None, None, None, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100]),distance = 5) == 118: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([31, 30, 48, 29, 38, 39, 49, 27, None, None, None, None, None, None, None, 28, None, 26, None, None, None, None, None, None]),distance = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([31, 30, 48, 29, 38, 39, 49, 27, None, None, None, None, None, None, None, 28, None, 26, None, None, None, None, None, None]),distance = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16]),distance = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16]),distance = 7) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1]),distance = 1) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 5) == 6
    assert candidate(root = tree_node([1, 2, 3, None, 4]),distance = 3) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 3) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),distance = 1) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 2) == 4
    assert candidate(root = tree_node([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]),distance = 3) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 3) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, None, None, None, 9]),distance = 4) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),distance = 7) == 56
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7, None, None, None, None, 8, 9, None, None, None, None, 10, 11, None, None, None, None, 12, 13, None, None, None, None, 14, 15, None, None, None, None, 16, 17, None, None, None, None, 18, 19, None, None, None, None, 20, 21]),distance = 8) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, None, None, 8, 9]),distance = 5) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, 7, None, None, None, 8, None, 9, None, None, 10, None, None, None, None, None, None, None, None, None, 11, None, None, None, None, None, None, None, None, None, 12, None, None, None, None, None, None, None, None, None, 13, None, None, None, None, None, None, None, None, None, 14, None, None, None, None, None, None, None, None, None, 15]),distance = 6) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12]),distance = 6) == 0
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30]),distance = 4) == 0
    assert candidate(root = tree_node([2, 1, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 6) == 0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]),distance = 6) == 0
    assert candidate(root = tree_node([8, 5, 9, 4, 6, 10, 11, 3, 7, None, None, None, None, None, None, None, 2, None, None, None, None, None, None, None]),distance = 3) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, None, 6, None, None, None, None, None, 7]),distance = 6) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, 8, 9, 10, None, None, None, None, None, 11, None, 12, 13, None, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 6) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),distance = 3) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),distance = 3) == 7
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25]),distance = 6) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, 9, 10, 11, 12, None, None, 13, 14, None, None, 15, 16]),distance = 5) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, None, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),distance = 3) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),distance = 5) == 45
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13]),distance = 7) == 0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, 12, 14]),distance = 5) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9, None, None, None, None, None, 10, 11, None, None, None, None, None, None, None, None, 12]),distance = 4) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),distance = 6) == 38
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, None, 9]),distance = 5) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 5) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, 10, 11, None, None, None, None, None, None, 12, 13, None, None, None, None, None, None, 14, 15]),distance = 3) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),distance = 2) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None, None, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 5) == 6
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, 7, None, None, None, 8, 9, 10, None, None, None, None, None, None, None, None, None, None, 11]),distance = 5) == 6
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20]),distance = 10) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),distance = 5) == 0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),distance = 2) == 0
    assert candidate(root = tree_node([5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 4) == 12
    assert candidate(root = tree_node([5, 1, 4, None, 2, None, 3, 6, 7, None, 8, None, 9, 10, 11, None, None, None, None, None, None]),distance = 5) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),distance = 5) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25, None, 26, None, 27, None, 28, None, 29, None, 30, None, 31, None, 32, None, 33, None, 34, None, 35, None, 36, None, 37, None, 38, None, 39, None, 40, None, 41, None, 42, None, 43, None, 44, None, 45, None, 46, None, 47, None, 48, None, 49, None, 50]),distance = 6) == 0
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 17, 19, None, None, None, None, None, None, None, None, 2, None, 9]),distance = 4) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, None, 10, None, None, 11]),distance = 5) == 0
    assert candidate(root = tree_node([5, 4, 8, 11, None, 17, 4, 7, 1, None, None, 5, 3]),distance = 6) == 10
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, 8, 9]),distance = 3) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]),distance = 3) == 25
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 5) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),distance = 4) == 12
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9, None, None, None, None, None, None, None, None, None, 10]),distance = 5) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]),distance = 4) == 24
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, 8, 9, None, None, None, None, 10, None, 11, None, None, None, None, None, None, None, None, None]),distance = 4) == 3
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14, None, None, 15]),distance = 4) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, 10, None, None, 11, None, None, 12]),distance = 4) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),distance = 5) == 17
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, None, 41, None, 42]),distance = 4) == 26
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),distance = 10) == 300
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None, None, None]),distance = 3) == 4
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, None, None, 6, None, None, 7]),distance = 5) == 3
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),distance = 7) == 0
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, None, None, None, None, None, None, 7, 8, None, None, None, None, None, None, None, None, 9, 10, None, None, None, None, None, None, None, None, None, 11, 12, None, None, None, None, None, None, None, None, None, 13, 14, None, None, None, None, None, None, None, None, None, 15, 16, None, None, None, None, None, None, None, None, None, 17, 18]),distance = 5) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9]),distance = 4) == 8
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 31, 43, 55, 70, 81, 93, 3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 61, 67, 73, 77, 83, 89, 95, None, 10, 19, 28, 35, 41, 47, 53, 59, 65, 71, 75, 79, 85, 91, 97, None, 13, 23, 32, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100, None, None, None, 16, 22, 29, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, None, None, None, None, None, 20, 26, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, None, None, None, None, None, None, None, None, 24, 30, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95, None, None, None, None, None, None, None, None, None, 28, 33, 38, 44, 50, 56, 62, 68, 74, 80, 86, 92, 98, None, None, None, None, None, None, None, None, None, None, None, 32, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97, None, None, None, None, None, None, None, None, None, None, None, None, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100]),distance = 5) == 118
    assert candidate(root = tree_node([31, 30, 48, 29, 38, 39, 49, 27, None, None, None, None, None, None, None, 28, None, 26, None, None, None, None, None, None]),distance = 2) == 1
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16]),distance = 7) == 0


