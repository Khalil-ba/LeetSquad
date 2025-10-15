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
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, None, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, None, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 49: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5, None, 7, 8, None, None, 9, None, None, 10])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5, None, 7, 8, None, None, 9, None, None, 10])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, None, 8])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, None, 8])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, 8, 9, None, None, None, None, 10, None, None, 11])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, 8, 9, None, None, None, None, 10, None, None, 11])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, None, 5, 3, None, 9, 6, 7, None, 8, None, None, None, 9, None, None, None, None, 10])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, None, 5, 3, None, 9, 6, 7, None, 8, None, None, None, 9, None, None, None, None, 10])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, None, 5, 3, None, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, None, 5, 3, None, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, 8, None, 10, None, None, 11, None, None, None, None, None, None, None, 12])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, 8, None, 10, None, None, 11, None, None, None, None, None, None, None, 12])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, 3, 9, 6, 7, None, None, None, None, 8, None, None, 10, None, None, None, 11, None, 12])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, 3, 9, 6, 7, None, None, None, None, 8, None, None, 10, None, None, None, 11, None, 12])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, 8, None, None, None, None, None, None, None, 17])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, 8, None, None, None, None, None, None, None, 17])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, 8])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, 8])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 4, None, None, None, 8, None, None, None, None, None, None, None, 16])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 4, None, None, None, 8, None, None, None, None, None, None, None, 16])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == 65: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, 5, 6, None, 7, None, None, 8, None, 9, None, 10])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, 5, 6, None, 7, None, None, 8, None, 9, None, 10])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, None, None, 8, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, None, None, 8, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12, None, None, 13, None, None, 14, None, None, 15])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12, None, None, 13, None, None, 14, None, None, 15])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, None, None, None, 9, 6, None, 7])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, None, None, None, 9, 6, None, 7])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, None, None, 9, 6, None, None, 7, None, None, None, None, None, 8, None, None, None, 10])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, None, None, 9, 6, None, None, 7, None, None, None, None, None, 8, None, None, None, 10])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 4, 6, 7, None, 9, 10, 11, None, None, 12, None, None, 13, None, None, None, None, 14, None, None, None, None, 15])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 4, 6, 7, None, 9, 10, 11, None, None, 12, None, None, 13, None, None, None, None, 14, None, None, None, None, 15])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, 3, None, None, None, None, 4])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, 3, None, None, None, None, 4])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, 9, 6, 7, 8, 10, 11, 12, 13, 14, 15])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, 9, 6, 7, 8, 10, 11, 12, 13, 14, 15])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, None, 5, 4, None, None, 8, None, None, 7, 9, 10])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, None, 5, 4, None, None, 8, None, None, 7, 9, 10])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, None, None, 8])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, None, None, 8])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, 7, None, None, None, 8])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, 7, None, None, None, 8])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, None, 5, 3, None, 9, 6, None, 7, None, None, 8])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, None, 5, 3, None, 9, 6, None, 7, None, None, 8])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, None, None, None, None, 6, None, 7])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, None, None, None, None, 6, None, 7])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, None, 5, None, 6])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, None, 5, None, 6])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, 7, None, None, None, None, None, 8, 9, 10])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, 7, None, None, None, None, None, 8, 9, 10])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, None, None, None, None, 8, 9, None, None, None, None, 10, 11])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, None, None, None, None, 8, 9, None, None, None, None, 10, 11])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, None, 7, None, None, 8, None, None, None, 11, None, None, None, 12, None, None, None, 13])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, None, 7, None, None, 8, None, None, None, 11, None, None, None, 12, None, None, None, 13])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 7, 8, None, None, None, None, 10, 11])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 7, 8, None, None, None, None, 10, 11])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, None, 7, None, 8, None, 9])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, None, 7, None, 8, None, 9])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, None, None, 8])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, None, None, 8])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, 6, None, None, None, None, 7, None, None, None, None, 8])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, 6, None, None, None, None, 7, None, None, None, None, 8])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, 7, None, 8, 9, 10, None, None, None, None, None, None, 11])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, 7, None, 8, 9, 10, None, None, None, None, None, None, 11])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, None, 4, 5, 6, None, 7, None, 8, None, 9, None, 10])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, None, 4, 5, 6, None, 7, None, 8, None, 9, None, 10])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 65: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, None, 8, None, None, 11])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, None, 8, None, None, 11])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 4, None, 9, None, None, 6, 7, 8, 9])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 4, None, 9, None, None, 6, 7, 8, 9])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 3, 2, None, 4, None, 5, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 3, 2, None, 4, None, 5, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, None, 7, 8, None, None, None, None, 10])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, None, 7, 8, None, None, None, None, 10])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, None, None, None, None, 8, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, None, None, None, None, 8, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, 6, None, None, None, None, 7, None, None, 8, None, None, None, None, 9, None, None, 10, None, None, 11, None, 12])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, 6, None, None, None, None, 7, None, None, 8, None, None, None, None, 9, None, None, 10, None, None, 11, None, 12])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, 5, 6, None, 7, None, 8, 9])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, 5, 6, None, 7, None, 8, 9])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, 8, None, 9])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, 8, None, 9])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9, None, None, None, None, 10])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9, None, None, None, None, 10])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, 9, 8, 6, None, 7, None, None, None, 10, None, None, 11])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, 9, 8, 6, None, 7, None, None, None, 10, None, None, 11])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, 9, 8, 6, None, None, None, None, 7, None, None, 10])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, 9, 8, 6, None, None, None, None, 7, None, None, 10])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, None, 5, 9, None, 6, 7, None, None, None, 8, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, None, 5, 9, None, 6, 7, None, None, None, 8, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, None, 5, 3])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, None, 5, 3])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, 7, 8, None, None, 10, None, None, None, 11, None, None, None, 12, None, None, None, 13, None, None, None, 14, None, None, None, 15])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, 7, 8, None, None, 10, None, None, None, 11, None, None, None, 12, None, None, None, 13, None, None, None, 14, None, None, None, 15])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, 3, None, 2, None, None, 5, 6, None, None, 7, 8, None, None, 9, None, None, None, None, None, 10])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, 3, None, 2, None, None, 5, 6, None, None, 7, 8, None, None, 9, None, None, None, None, None, 10])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, 8, None, 7])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, 8, None, 7])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, 6, None, None, 7])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, 6, None, None, 7])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, None, 6, None, None, None, None, None, None, 7])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, None, 6, None, None, None, None, None, None, 7])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 49: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == 49: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 25: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, 7])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, 7])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, 3, None, 4, None, None, 5])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, 3, None, 4, None, None, 5])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, 8, None, None, None, None, None, None, None, 17, None, None, None, None, None, None, None, None, None, None, None, None, None, 18])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, 8, None, None, None, None, None, None, None, 17, None, None, None, None, None, None, None, None, None, None, None, None, None, 18])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12, None, None, 13])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12, None, None, 13])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, None, None, 2])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, None, None, 2])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, None, None, 5, 9, None, None, None, 7, None, None, None, None, 8, 9])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, None, None, 5, 9, None, None, None, 7, None, None, None, None, 8, 9])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, 8, None, None, 10, 11, None, None, None, None, 12, None, 13])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, 8, None, None, 10, 11, None, None, None, None, 12, None, 13])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, None, None, 9, None, None, None, 10])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, None, None, 9, None, None, None, 10])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9, None, None, None, None, 10, None, None, 11, None, 12, None, 13, None, 14, None, 15])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9, None, None, None, None, 10, None, None, 11, None, 12, None, 13, None, 14, None, 15])) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7])) == 5
    assert candidate(root = tree_node([1, 3, 2, 5])) == 2
    assert candidate(root = tree_node([1, None, 2])) == 1
    assert candidate(root = tree_node([1])) == 1
    assert candidate(root = tree_node([1, 3, None, None, 5])) == 1
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 49
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 7, 8, None, None, 9, None, None, 10])) == 6
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, None, 8])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7, 8, 9, None, None, None, None, 10, None, None, 11])) == 2
    assert candidate(root = tree_node([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) == 8
    assert candidate(root = tree_node([1, 3, None, 5, 3, None, 9, 6, 7, None, 8, None, None, None, 9, None, None, None, None, 10])) == 5
    assert candidate(root = tree_node([1, 3, None, 5, 3, None, 9])) == 2
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, 8, None, 10, None, None, 11, None, None, None, None, None, None, None, 12])) == 8
    assert candidate(root = tree_node([1, 3, 2, 5, None, 3, 9, 6, 7, None, None, None, None, 8, None, None, 10, None, None, None, 11, None, 12])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, 8, None, None, None, None, None, None, None, 17])) == 8
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, 8])) == 4
    assert candidate(root = tree_node([1, 2, None, 4, None, None, None, 8, None, None, None, None, None, None, None, 16])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16])) == 65
    assert candidate(root = tree_node([1, 3, 2, None, 5, 6, None, 7, None, None, 8, None, 9, None, 10])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, None, 7, None, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12, None, None, 13, None, None, 14, None, None, 15])) == 14
    assert candidate(root = tree_node([1, None, 3, None, None, None, 9, 6, None, 7])) == 1
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])) == 8
    assert candidate(root = tree_node([1, 3, 2, None, None, None, 9, 6, None, None, 7, None, None, None, None, None, 8, None, None, None, 10])) == 2
    assert candidate(root = tree_node([1, 3, 2, 5, 4, 6, 7, None, 9, 10, 11, None, None, 12, None, None, 13, None, None, None, None, 14, None, None, None, None, 15])) == 10
    assert candidate(root = tree_node([1, None, 2, None, None, None, 3, None, None, None, None, 4, None, None, None, None, 5])) == 1
    assert candidate(root = tree_node([1, None, 2, None, None, 3, None, None, None, None, 4])) == 1
    assert candidate(root = tree_node([1, 3, 2, 5, 3, 9, 6, 7, 8, 10, 11, 12, 13, 14, 15])) == 8
    assert candidate(root = tree_node([1, 3, 2, None, None, 5, 4, None, None, 8, None, None, 7, 9, 10])) == 2
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, None, None, 8])) == 7
    assert candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, 7, None, None, None, 8])) == 7
    assert candidate(root = tree_node([1, 3, None, 5, 3, None, 9, 6, None, 7, None, None, 8])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, None, None, None, None, 6, None, 7])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 15
    assert candidate(root = tree_node([1, 3, 2, None, None, 5, None, 6])) == 2
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 2
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12])) == 14
    assert candidate(root = tree_node([1, None, 2, None, None, 3, None, None, 4, None, None, 5, None, None, 6])) == 1
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, 7, None, None, None, None, None, 8, 9, 10])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, None, 6, 7, None, None, None, None, None, None, 8, 9, None, None, None, None, 10, 11])) == 3
    assert candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, None, 7, None, None, 8, None, None, None, 11, None, None, None, 12, None, None, None, 13])) == 6
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 7, 8, None, None, None, None, 10, 11])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, None, 7, None, 8, None, 9])) == 8
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 1
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, None, None, 8])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, 6, None, None, None, None, 7, None, None, None, None, 8])) == 4
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, None, 7, None, 8, 9, 10, None, None, None, None, None, None, 11])) == 5
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, 5, 6, None, 7, None, 8, None, 9, None, 10])) == 5
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 13
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == 1
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 65
    assert candidate(root = tree_node([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 8
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, None, None, None, None, 8, None, None, 11])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 4, None, 9, None, None, 6, 7, 8, 9])) == 6
    assert candidate(root = tree_node([1, None, 3, 2, None, 4, None, 5, 6, None, 7, None, 8, None, 9, None, 10, None, 11])) == 5
    assert candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, None, 7, 8, None, None, None, None, 10])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, None, None, 5, None, None, 6, 7, None, None, None, None, None, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, 6, None, None, None, None, 7, None, None, 8, None, None, None, None, 9, None, None, 10, None, None, 11, None, 12])) == 4
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == 1
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9])) == 4
    assert candidate(root = tree_node([1, 3, 2, None, 5, 6, None, 7, None, 8, 9])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, 6, None, 7, None, 8, None, 9])) == 7
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9, None, None, None, None, 10])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, 3, 9, 8, 6, None, 7, None, None, None, 10, None, None, 11])) == 7
    assert candidate(root = tree_node([1, 3, 2, 5, 3, 9, 8, 6, None, None, None, None, 7, None, None, 10])) == 6
    assert candidate(root = tree_node([1, 3, 2, None, None, 5, 9, None, 6, 7, None, None, None, 8, 9])) == 2
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == 1
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10])) == 13
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6])) == 1
    assert candidate(root = tree_node([1, 3, None, 5, 3])) == 2
    assert candidate(root = tree_node([1, 3, 2, 5, None, 9, 6, 7, 8, None, None, 10, None, None, None, 11, None, None, None, 12, None, None, None, 13, None, None, None, 14, None, None, None, 15])) == 7
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11])) == 14
    assert candidate(root = tree_node([1, 3, 2, None, 3, None, 2, None, None, 5, 6, None, None, 7, 8, None, None, 9, None, None, None, None, None, 10])) == 3
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 1
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, 8, None, 7])) == 7
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, None, 6, None, 7, None, 8, None, 9])) == 5
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, 6, None, None, 7])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, None, None, None, 6, None, None, None, None, None, None, 7])) == 4
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])) == 49
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])) == 49
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])) == 25
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 8
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, None, None, 6, None, None, 7])) == 4
    assert candidate(root = tree_node([1, None, 2, 3, None, 4, None, None, 5])) == 1
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, 8, None, None, None, None, None, None, None, 17, None, None, None, None, None, None, None, None, None, None, None, None, None, 18])) == 7
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 10, None, None, 11, None, None, None, None, 12, None, None, 13])) == 14
    assert candidate(root = tree_node([1, 3, None, None, 2])) == 1
    assert candidate(root = tree_node([1, 3, 2, None, None, 5, 9, None, None, None, 7, None, None, None, None, 8, 9])) == 2
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, None, None, 8, None, None, 10, 11, None, None, None, None, 12, None, 13])) == 7
    assert candidate(root = tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7, None, 8, None, None, None, 9, None, None, None, 10])) == 7
    assert candidate(root = tree_node([1, 3, 2, 5, 3, None, 9, None, None, 6, None, None, None, None, 7, None, None, None, None, 8, None, None, None, None, 9, None, None, None, None, 10, None, None, 11, None, 12, None, 13, None, 14, None, 15])) == 4


