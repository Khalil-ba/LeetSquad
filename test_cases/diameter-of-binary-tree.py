def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 4, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 4, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, -7, -3, None, None, -9, -3, 9, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, -7, -3, None, None, -9, -3, 9, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 2, None, 3, None, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 2, None, 3, None, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 2])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 2])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, None, None, None, None, 6])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, None, None, None, None, 6])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, 12, 13, 14, 15, None, None, None, None, 16])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, 12, 13, 14, 15, None, None, None, None, 16])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, None, 8, 9, None, None, None, None, 10])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, None, 8, 9, None, None, None, None, 10])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, 8, 9])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, 8, 9])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, 6])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, 6])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 4, None, 6, 7, 8, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 4, None, 6, 7, 8, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, 6, 7, None, None, 8, None, None, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, 6, 7, None, None, 8, None, None, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 10, 11, None, None, 12, 13])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 10, 11, None, None, 12, 13])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, None, 7, 8, None, None, 9, None, None, 10, 11])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, None, 7, 8, None, None, 9, None, None, 10, 11])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, None, 10, 11])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, None, 10, 11])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, None, None, 9, None, None, None, None, 10, None, None, None, None, 11])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, None, None, 9, None, None, None, None, 10, None, None, None, None, 11])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None, 10, 11])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None, 10, 11])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, None, None, None, 7, None, None, 8, None, None, None, None, None, None, 9, None, None, 10])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, None, None, None, 7, None, None, 8, None, None, None, None, None, None, 9, None, None, 10])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, None, None, 6, 7, None, 8, None, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, None, None, 6, 7, None, 8, None, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, None, 6])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, None, 6])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, None, None, 11, 12])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, None, None, 11, 12])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, None, 7, None, 8])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, None, 7, None, 8])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, None, None, None, None, None, 4, None, None, None, None, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, None, None, None, None, None, 4, None, None, None, None, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, None, 7, None, None, 8, None, 9])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, None, 7, None, None, 8, None, 9])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, None, 3, None, None, None, 4, None, None, None, None, 5, None, None, None, None, None, 6])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, None, 3, None, None, None, 4, None, None, None, None, 5, None, None, None, None, None, 6])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11, None, 12])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11, None, 12])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, 12, 13])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, 12, 13])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, 10, None, None, 11, None, None, 12])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, 10, None, None, 11, None, None, 12])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, None, 9, 10, 11])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, None, 9, 10, 11])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, 8, 9, None, None, 10])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, 8, 9, None, None, 10])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, None, 12, 13])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, None, 12, 13])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, 10, 11, 12])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, 10, 11, 12])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, 10, 11, 12, 13, 14, 15])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, 10, 11, 12, 13, 14, 15])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7])) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 4
    assert candidate(root = tree_node([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 4
    assert candidate(root = tree_node([3, 1, 4, None, 2])) == 3
    assert candidate(root = tree_node([1, 2, 3])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5])) == 4
    assert candidate(root = tree_node([1, 2, None, 4, 5])) == 2
    assert candidate(root = tree_node([1, 2])) == 1
    assert candidate(root = tree_node([4, -7, -3, None, None, -9, -3, 9, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2])) == 8
    assert candidate(root = tree_node([4, 2, None, 3, None, 1])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5])) == 3
    assert candidate(root = tree_node([3, 1, 2])) == 2
    assert candidate(root = tree_node([1])) == 0
    assert candidate(root = tree_node([1, None, 2, None, 3])) == 2
    assert candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5])) == 1
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8])) == 7
    assert candidate(root = tree_node([1, None, 2, 3, None, None, 4, 5, None, None, None, None, None, None, 6])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, 11, 12, 13, 14, 15, None, None, None, None, 16])) == 8
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, None, None, 8, 9, None, None, None, None, 10])) == 6
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, 8, 9])) == 6
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == 8
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, None, None, None, None, 5, None, None, None, None, 6])) == 3
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8])) == 6
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, None, 4, None, 6, 7, 8, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, None, None, 6, 7, None, None, 8, None, None, 9])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 10, 11, None, None, 12, 13])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, None, 7, 8, None, None, 9, None, None, 10, 11])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, None, 10, 11])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, None, None, 9, None, None, None, None, 10, None, None, None, None, 11])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, None, 11, None, None, 12, None, None, 13, None, None, 14])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None, 10, 11])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, None, None, None, None, 7, None, None, 8, None, None, None, None, None, None, 9, None, None, 10])) == 6
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, None, 6, 7, None, 8, None, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, None, 6])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, None, None, 11, 12])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, 6, None, None, 7, None, 8])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, None, None, None, None, None, None, 4, None, None, None, None, 5])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, None, 7, None, None, 8, None, 9])) == 5
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, None, 4, None, None, None, None, 5, None, None, None, None, None, 6])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12, None, None, 13])) == 10
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, 10, None, 11, None, 12])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, 12, 13])) == 7
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 6
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 14
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, None, 5, 6, None, None, 7, 8, None, None, 9, 10])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, None, None, 7, 8, None, None, None, None, 9])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9])) == 5
    assert candidate(root = tree_node([1, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6, None, None, 7, None, None, 8, None, None, 9, None, None, 10])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, 6, 7])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, None, None, None, 10, None, None, 11, None, None, 12])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6])) == 5
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, None, None, 9, 10, 11])) == 7
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, 8, 9, None, None, 10])) == 7
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 7
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 9
    assert candidate(root = tree_node([1, 2, None, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 11
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, 10, 11, None, None, None, None, None, 12, 13])) == 8
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, 8, 9, 10, 11, 12, 13])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, 10, 11, 12])) == 6
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 11
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, 10, 11, 12, 13, 14, 15])) == 7
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, 5, None, 6, None, 7])) == 6


