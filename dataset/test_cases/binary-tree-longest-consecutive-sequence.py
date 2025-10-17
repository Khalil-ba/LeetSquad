def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, 2, None, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, 2, None, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, None, 1, None, None, 4, None, 5, None, 6])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, None, 1, None, None, 4, None, 5, None, 6])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 4, None, None, None, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 4, None, None, None, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 0, 3])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 0, 3])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, 4, None, None, None, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, 4, None, None, None, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, 3, 7, 2, 8, 1, 9, None, None, None, None, None, None, 0, 10])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, 3, 7, 2, 8, 1, 9, None, None, None, None, None, None, 0, 10])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 29, 31, 28, 32, 27, 33, 26, 34, 25, 35, 24, 36, 23, 37])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 29, 31, 28, 32, 27, 33, 26, 34, 25, 35, 24, 36, 23, 37])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, None, 5, 4, 6, None, None, None, 7, 8, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, None, 5, 4, 6, None, None, None, 7, 8, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, 6, 7, None, None, None, 8, None, 9])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, 6, 7, None, None, None, 8, None, 9])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, 7, 10])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, 7, 10])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, 0, 2, 9, None, None, None, None, None, None, None, 14, 16, 17, 19, 21, 24, 26])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, 0, 2, 9, None, None, None, None, None, None, None, 14, 16, 17, 19, 21, 24, 26])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 2, 7, None, 20, 1, None, 6, 8, None, None, None, 25])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 2, 7, None, 20, 1, None, 6, 8, None, None, None, 25])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 12, None, 22, None, 13, None, 23, None, 40])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 12, None, 22, None, 13, None, 23, None, 40])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, 9, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, 9, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 25, 10, 18, None, 30, 5, 13, 17, 19, 28, 32, None, 14, None, None, None, None, None, None, None, None, None, None, None])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 25, 10, 18, None, 30, 5, 13, 17, 19, 28, 32, None, 14, None, None, None, None, None, None, None, None, None, None, None])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, 8, None, 12, None, 7, None, 13, None, None, None, None, 14])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, 8, None, 12, None, 7, None, 13, None, None, None, None, 14])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 14, 8, None, 11, 15, 7, 6, 12, 16, 5, 4, 13, 17, 3, 2, 1, None, None, None, None, None, None, None, None, None, 18])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 14, 8, None, 11, 15, 7, 6, 12, 16, 5, 4, 13, 17, 3, 2, 1, None, None, None, None, None, None, None, None, None, 18])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 7, 3, None, 2, 8, 1, None, None, None, None, None, 6, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 7, 3, None, 2, 8, 1, None, None, None, None, None, 6, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, 6, None, None, None, None, None, 10])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, 6, None, None, None, None, None, 10])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, 4, None, None, None, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, 4, None, None, None, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, 8, 10, None, 12, None, None, 9, None, None, 11, None, 13])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, 8, 10, None, 12, None, None, 9, None, None, 11, None, 13])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, None, 6, None, None, 7])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, None, 6, None, None, 7])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, 2, None, 1, 4, 3, None, None, 5, None, 6])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, 2, None, 1, 4, 3, None, None, 5, None, 6])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, 4, None, None, None, None, 5, 6, 7])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, 4, None, None, None, None, 5, 6, 7])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, 6, None, None, None, None, 10, None, None, None, 11])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, 6, None, None, None, None, 10, None, None, None, 11])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 1, 4, None, 9, None, 2, None, None, None, 10])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 1, 4, None, 9, None, 2, None, None, None, 10])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7, None, 8])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7, None, 8])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, None, None, None, None, 8])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, None, None, None, None, 8])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, None, None, 11, 13, 16, 18, 22, 27, None, 9, None, None, None, None, 19, None, None, None, None, 21, None, None, 23, None, None, 24, None, None, None, 26, None, None, 28])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, None, None, 11, 13, 16, 18, 22, 27, None, 9, None, None, None, None, 19, None, None, None, None, 21, None, None, 23, None, None, 24, None, None, None, 26, None, None, 28])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, None, None, 8, None, 4, None, None, 11, 12])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, None, None, 8, None, 4, None, None, 11, 12])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, None, 12, None, 13, None, 14, None, 15])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, None, 12, None, 13, None, 14, None, 15])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 4, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 4, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, None, None, 12, None, None, 13, None, None, None, None, 14, None, None, 15])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, None, None, 12, None, None, 13, None, None, None, None, 14, None, None, 15])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, 2, None, 1, 4, None, None, None, None, 5, 6, None, 7])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, 2, None, 1, 4, None, None, None, None, 5, 6, None, 7])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, None, 2, None, 3, None, 4, None, None, None, 6, None, 7])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, None, 2, None, 3, None, 4, None, None, None, 6, None, 7])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 7, 13, 19, 22, 27, 33, 42, 47, 2, 6, 8, 11, 14, 16, 18, 21, 23, 26, 29, 31, 34, 37, 41, 44, 46, 49, 1, 4, 9, 12, 15, 24, 28, 30, 32, 36, 38, 39, 43, 47, 50])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 7, 13, 19, 22, 27, 33, 42, 47, 2, 6, 8, 11, 14, 16, 18, 21, 23, 26, 29, 31, 34, 37, 41, 44, 46, 49, 1, 4, 9, 12, 15, 24, 28, 30, 32, 36, 38, 39, 43, 47, 50])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9, 10, None, None, None, None, None, 11, 12, None, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9, 10, None, None, None, None, None, 11, 12, None, None])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, 6, 7])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, 6, 7])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 6, None, 2, None, 8, 3, None, 4, None, 7, None, 9])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 6, None, 2, None, 8, 3, None, 4, None, 7, None, 9])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, 8, None, 12, None, 7, None, 13, None, 6, None, 14, None, 5, None, 15])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, 8, None, 12, None, 7, None, 13, None, 6, None, 14, None, 5, None, 15])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 18: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 4, None, None, 5, None, None, None, None, None, None, 6, 7])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 4, None, None, 5, None, None, None, None, None, None, 6, 7])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, None, None, 9, 10])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, None, None, 9, 10])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, 4, None, None, None, 5, None, None, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, 4, None, None, None, 5, None, None, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, 4, None, None, None, 5, 6, None, None, 7, 8])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, 4, None, None, None, 5, 6, None, None, 7, 8])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 20: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, None, 13, None, 12, None, None, None, 14, None, 15])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, None, 13, None, 12, None, None, None, 14, None, 15])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, 3.5, None, None, None, None, None, 7, None, None, None, None, None, 10, None, None])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, 3.5, None, None, None, None, None, 7, None, None, None, None, None, 10, None, None])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 9, 11, None, 10, None, 12, None, None, 11, None, None, None, 13])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 9, 11, None, 10, None, 12, None, None, 11, None, None, None, 13])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, None, None, None, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, None, None, None, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, None, 3, 2, None, 1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, None, 3, 2, None, 1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4, None, None, None, None, None, None, None, 5, 5, 5, 5, None, None, None, None, 5, 5, 5, 5, None, None, None, None, 6, 6, 6, 6, None, None, None, None, 6, 6, 6, 6, None, None, None, None, 7, 7, 7, 7, None, None, None, None, 7, 7, 7, 7])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4, None, None, None, None, None, None, None, 5, 5, 5, 5, None, None, None, None, 5, 5, 5, 5, None, None, None, None, 6, 6, 6, 6, None, None, None, None, 6, 6, 6, 6, None, None, None, None, 7, 7, 7, 7, None, None, None, None, 7, 7, 7, 7])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, 4, None, None, None, 5, None, None, 6, None, None, 7, None, None, 8])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, 4, None, None, None, 5, None, None, 6, None, None, 7, None, None, 8])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, 16])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, 16])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, 2, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, 2, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 8, 2, 4, 7, 9, 1, None, 5, 6, None, None, None, None, None, 10, None, None, 11, None, None, None, 12])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 8, 2, 4, 7, 9, 1, None, 5, 6, None, None, None, None, None, 10, None, None, 11, None, None, None, 12])) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5])) == 2
    assert candidate(root = tree_node([2, None, 3, 2, None, 1])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 5
    assert candidate(root = tree_node([3, 2, None, 1, None, None, 4, None, 5, None, 6])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 6
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5])) == 3
    assert candidate(root = tree_node([1, 3, 2, 4, None, None, None, 5])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 8
    assert candidate(root = tree_node([1, None, 2, None, 0, 3])) == 2
    assert candidate(root = tree_node([2, 1, 3])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 4
    assert candidate(root = tree_node([1, 3, 2])) == 2
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7])) == 1
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([1, None, 2, 3, 4, None, None, None, 5])) == 3
    assert candidate(root = tree_node([3, 1, 4, None, 2])) == 2
    assert candidate(root = tree_node([5, 4, 6, 3, 7, 2, 8, 1, 9, None, None, None, None, None, None, 0, 10])) == 2
    assert candidate(root = tree_node([30, 29, 31, 28, 32, 27, 33, 26, 34, 25, 35, 24, 36, 23, 37])) == 2
    assert candidate(root = tree_node([1, None, 3, None, 5, 4, 6, None, None, None, 7, 8, 9])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 10
    assert candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, 6, 7, None, None, None, 8, None, 9])) == 3
    assert candidate(root = tree_node([2, None, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 4
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, None, None, None, None, 7, 10])) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25, 0, 2, 9, None, None, None, None, None, None, None, 14, 16, 17, 19, 21, 24, 26])) == 3
    assert candidate(root = tree_node([10, 5, 15, 2, 7, None, 20, 1, None, 6, 8, None, None, None, 25])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 2
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, None, None, 12, None, 22, None, 13, None, 23, None, 40])) == 1
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8, 1, None, None, None, None, None, 9, None])) == 3
    assert candidate(root = tree_node([20, 15, 25, 10, 18, None, 30, 5, 13, 17, 19, 28, 32, None, 14, None, None, None, None, None, None, None, None, None, None, None])) == 2
    assert candidate(root = tree_node([10, 9, 11, 8, None, 12, None, 7, None, 13, None, None, None, None, 14])) == 5
    assert candidate(root = tree_node([10, 9, 14, 8, None, 11, 15, 7, 6, 12, 16, 5, 4, 13, 17, 3, 2, 1, None, None, None, None, None, None, None, None, None, 18])) == 2
    assert candidate(root = tree_node([5, 4, 7, 3, None, 2, 8, 1, None, None, None, None, None, 6, 9])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 2
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, 6, None, None, None, None, None, 10])) == 2
    assert candidate(root = tree_node([1, None, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 1
    assert candidate(root = tree_node([1, 3, 2, None, 4, None, None, None, 5])) == 3
    assert candidate(root = tree_node([10, 9, 11, 8, 10, None, 12, None, None, 9, None, None, 11, None, 13])) == 3
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, None, 6, None, None, 7])) == 3
    assert candidate(root = tree_node([2, None, 3, 2, None, 1, 4, 3, None, None, 5, None, 6])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, 4, None, None, None, None, 5, 6, 7])) == 4
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 7, 9, 1, None, 6, None, None, None, None, 10, None, None, None, 11])) == 3
    assert candidate(root = tree_node([5, 3, 8, 1, 4, None, 9, None, 2, None, None, None, 10])) == 3
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7, None, 8])) == 6
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 13
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 2
    assert candidate(root = tree_node([1, None, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, None, 7, None, None, None, None, 8])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 11
    assert candidate(root = tree_node([5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 11
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, None, None, 11, 13, 16, 18, 22, 27, None, 9, None, None, None, None, 19, None, None, None, None, 21, None, None, 23, None, None, 24, None, None, None, 26, None, None, 28])) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, 9, None, None, None, None, 8, None, 4, None, None, 11, 12])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 15
    assert candidate(root = tree_node([10, 9, 11, None, 12, None, 13, None, 14, None, 15])) == 2
    assert candidate(root = tree_node([1, 3, 2, 4, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 2
    assert candidate(root = tree_node([10, 9, 11, None, None, 12, None, None, 13, None, None, None, None, 14, None, None, 15])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 9
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 2
    assert candidate(root = tree_node([2, None, 3, 2, None, 1, 4, None, None, None, None, 5, 6, None, 7])) == 2
    assert candidate(root = tree_node([5, 1, None, 2, None, 3, None, 4, None, None, None, 6, None, 7])) == 4
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 17, 25, 35, 48, 3, 7, 13, 19, 22, 27, 33, 42, 47, 2, 6, 8, 11, 14, 16, 18, 21, 23, 26, 29, 31, 34, 37, 41, 44, 46, 49, 1, 4, 9, 12, 15, 24, 28, 30, 32, 36, 38, 39, 43, 47, 50])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9, 10, None, None, None, None, None, 11, 12, None, None])) == 4
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, 6, 7])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10])) == 6
    assert candidate(root = tree_node([5, 1, 6, None, 2, None, 8, 3, None, 4, None, 7, None, 9])) == 3
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 18
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, None, 17, None, 18, None, 19, None, 20, None, 21, None, 22, None, 23, None, 24, None, 25])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 2
    assert candidate(root = tree_node([10, 9, 11, 8, None, 12, None, 7, None, 13, None, 6, None, 14, None, 5, None, 15])) == 6
    assert candidate(root = tree_node([1, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 18
    assert candidate(root = tree_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 2
    assert candidate(root = tree_node([1, 3, 2, 4, None, None, 5, None, None, None, None, None, None, 6, 7])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, None, None, 9, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 2
    assert candidate(root = tree_node([1, 3, 2, None, 4, None, None, None, 5, None, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, 4, None, None, None, 5, 6, None, None, 7, 8])) == 4
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == 20
    assert candidate(root = tree_node([10, 9, 11, None, 13, None, 12, None, None, None, 14, None, 15])) == 3
    assert candidate(root = tree_node([5, 3, 8, 2, 4, 6, 9, 1, None, 3.5, None, None, None, None, None, 7, None, None, None, None, None, 10, None, None])) == 2
    assert candidate(root = tree_node([1, None, 3, 2, 4, None, None, None, 5, None, 6, None, 7])) == 5
    assert candidate(root = tree_node([10, 9, 11, None, 10, None, 12, None, None, 11, None, None, None, 13])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, None, None, None, 9])) == 2
    assert candidate(root = tree_node([2, None, 3, 2, None, 1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 2
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4, None, None, None, None, None, None, None, 5, 5, 5, 5, None, None, None, None, 5, 5, 5, 5, None, None, None, None, 6, 6, 6, 6, None, None, None, None, 6, 6, 6, 6, None, None, None, None, 7, 7, 7, 7, None, None, None, None, 7, 7, 7, 7])) == 5
    assert candidate(root = tree_node([1, None, 2, 3, 4, None, None, None, 5, None, None, 6, None, None, 7, None, None, 8])) == 3
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == 1
    assert candidate(root = tree_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, 16])) == 2
    assert candidate(root = tree_node([1, None, 3, 2, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9])) == 5
    assert candidate(root = tree_node([7, 3, 8, 2, 4, 7, 9, 1, None, 5, 6, None, None, None, None, None, 10, None, None, 11, None, None, None, 12])) == 3


