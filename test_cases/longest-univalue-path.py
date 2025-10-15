def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 1, 1, None, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 1, 1, None, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 4, 5, 4, 4, None, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 4, 5, 4, 4, None, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, 1, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, 1, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, None, None, 3, 3, 3, 3, None, None, None, None, 4, 4, 4, 4, None, None, None, None, None, None, 5, 5, 5, 5])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, None, None, 3, 3, 3, 3, None, None, None, None, 4, 4, 4, 4, None, None, None, None, None, None, 5, 5, 5, 5])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 1, 1, 5, 5, 1, 1, None, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 1, 1, 5, 5, 1, 1, None, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 2, 3, 3, 3, None, 3, None, None, 3, None, 3])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 2, 3, 3, 3, None, 3, None, None, 3, None, 3])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, None, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, None, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 3, 3])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 3, 3])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, 1, 1, None, 1, None, None, 1, None, 1])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, 1, 1, None, 1, None, None, 1, None, 1])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, None, 5, 5, 5, 5, None, None, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, None, 5, 5, 5, 5, None, None, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 4, 4, 4, 4, 1, 1, 4, None, None, None, None, None, None, 4])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 4, 4, 4, 4, 1, 1, 4, None, None, None, None, None, None, 4])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 2, 1, 1, 2, 2, 1, None, 1, None, 2, None, 2, None, 2])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 2, 1, 1, 2, 2, 1, None, 1, None, 2, None, 2, None, 2])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 4, None, 4, 4, 4, None, None, 4, 4, None, 4, None, None, 4])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 4, None, 4, 4, 4, None, None, 4, 4, None, 4, None, None, 4])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, None, None, 1, 1, None, 1, 1, None, 1])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, None, None, 1, 1, None, 1, 1, None, 1])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, None, 2, 2, None, 2, None, 2, None, 2, None, 2, None])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, None, 2, 2, None, 2, None, 2, None, 2, None, 2, None])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 4, 4, 4, 4, 1, 1, 4, 4, 4, 4, 2, 2, 2, 2])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 4, 4, 4, 4, 1, 1, 4, 4, 4, 4, 2, 2, 2, 2])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, None, 1, None, 1, 1, None, 1, None, 1, None, 1])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, None, 1, None, 1, 1, None, 1, None, 1, None, 1])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, None, None, 1, 1, 1, 1, None, None, None, None, 1, 1, 1, 1, 1, 1, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, None, None, 1, 1, 1, 1, None, None, None, None, 1, 1, 1, 1, 1, 1, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, None, 3])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, None, 3])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, None, 5, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, None, 5, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, None, None, None, None, None, None, 4, 4])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, None, None, None, None, None, None, 4, 4])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 1, 1, 5, 5, None, None, 5, 5, 5, None, None, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 1, 1, 5, 5, None, None, 5, 5, 5, None, None, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 4, 5, 4, 4, None, 5, 1, 1, 1, 1, None, 5, 5, 5, 1, 1, 1, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 4, 5, 4, 4, None, 5, 1, 1, 1, 1, None, 5, 5, 5, 1, 1, 1, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, 4, 5, 5, None, 5, 5, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, 4, 5, 5, None, 5, 5, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 1, None, 2, None, 5, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 1, None, 2, None, 5, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, None, None, 4, 4, None, None, 5, 5])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, None, None, 4, 4, None, None, 5, 5])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, None, 2, 2, None, None, 2, 2, None, None, 2, 2, 2])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, None, 2, 2, None, None, 2, 2, None, None, 2, 2, 2])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, None, None, None, None, 3, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, None, None, None, None, 3, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 2, 1, None, 2, 1, None, None, None, 1, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 2, 1, None, 2, 1, None, None, None, 1, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, None, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, None, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, None, 5, 5, 5, 5, None, None, 5, 5, None, None, 5, 5, None, None, 5])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, None, 5, 5, 5, 5, None, None, 5, 5, None, None, 5, 5, None, None, 5])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 1, 1, None, 1, 1, None, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 1, 1, None, 1, 1, None, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, None, None, None, None, 4, 4])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, None, None, None, None, 4, 4])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 1, 1, 3, 1, 1, None, None, None, None, None, None, 1, 1, 1])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 1, 1, 3, 1, 1, None, None, None, None, None, None, 1, 1, 1])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, None, None, None, None, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, None, None, None, None, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, None, None, 3, None, 3, None, None, 3])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, None, None, 3, None, 3, None, None, 3])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, None, None, 1, None, None, None, None, 1, None, None, None, 1])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, None, None, 1, None, None, None, None, 1, None, None, None, 1])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, None, 3, 3, None, None, 3, 3, 3, None, None, 3, 3])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, None, 3, 3, None, None, 3, 3, 3, None, None, 3, 3])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, 5, 5, None, 5, None, 5, 5, None, 5, 5])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, 5, 5, None, 5, None, 5, 5, None, 5, 5])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 4, 4, 5, 5, None, None, 4, 4, None, None, 4, 4])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 4, 4, 5, 5, None, None, 4, 4, None, None, 4, 4])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 5, 1, 1, 5, 5, None, None, None, None, 5, 5])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 5, 1, 1, 5, 5, None, None, None, None, 5, 5])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, 1, 1, None, 1])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, 1, 1, None, 1])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, None, None, 1, 1, None, None, 1, 1])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, None, None, 1, 1, None, None, 1, 1])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, None, 1, 1, 1, None, None, 1, 1, None, 1, 1, 1, None, 1])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, None, 1, 1, 1, None, None, 1, 1, None, 1, 1, 1, None, 1])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, None, 2, None, 2, 2, None, 2, 2, None, 2])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, None, 2, None, 2, 2, None, 2, 2, None, 2])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, None, None, 5, 5, 5, 5, None, None, 5, 5, 5, 5])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, None, None, 5, 5, 5, 5, None, None, 5, 5, 5, 5])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, None, 3, None, 3, 3, None, None, 3])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, None, 3, None, 3, 3, None, None, 3])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, None, 1, None, 1, 1, 1, None, 1, None, 1, 1, 1, None, 1, None, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, None, 1, None, 1, 1, 1, None, 1, None, 1, 1, 1, None, 1, None, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, None, 5, 5, None, None, 5, None, 5, 5, None, 5, None, 5, None, 5])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, None, 5, 5, None, None, 5, None, 5, 5, None, 5, None, 5, None, 5])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, 1, 1, 1, 1])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, 1, 1, 1, 1])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, None, None, None, 5, 5, None, 5, 5, 5, None, 5, 5, None, 5])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, None, None, None, 5, 5, None, 5, 5, 5, None, 5, 5, None, 5])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, None, 2, 2, None, 2, None, 2, 2, None, 2, 2])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, None, 2, 2, None, 2, None, 2, 2, None, 2, 2])) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 0
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == 0
    assert candidate(root = tree_node([5, 4, 5, 1, 1, None, 5])) == 2
    assert candidate(root = tree_node([1, 4, 5, 4, 4, None, 5])) == 2
    assert candidate(root = tree_node([1, None, 1, None, 1, 1, None])) == 3
    assert candidate(root = tree_node([1, 2])) == 0
    assert candidate(root = tree_node([1, 1, 1, 1])) == 3
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5])) == 5
    assert candidate(root = tree_node([])) == 0
    assert candidate(root = tree_node([1, 2, 2, None, None, 3, 3, 3, 3, None, None, None, None, 4, 4, 4, 4, None, None, None, None, None, None, 5, 5, 5, 5])) == 2
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == 0
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 10
    assert candidate(root = tree_node([5, 4, 5, 1, 1, 5, 5, 1, 1, None, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5
    assert candidate(root = tree_node([1, 2, 2, 2, 3, 3, 3, None, 3, None, None, 3, None, 3])) == 1
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, None, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 3, 3])) == 2
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, 1, 1, None, 1, None, None, 1, None, 1])) == 7
    assert candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, None, 5, 5, 5, 5, None, None, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 5
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 8
    assert candidate(root = tree_node([1, 4, 4, 4, 4, 1, 1, 4, None, None, None, None, None, None, 4])) == 3
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 2, 2, 1, None, 1, None, 2, None, 2, None, 2])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11
    assert candidate(root = tree_node([4, 4, None, 4, 4, 4, None, None, 4, 4, None, 4, None, None, 4])) == 7
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, None, 1, 1, None, 1, 1, None, 1])) == 5
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 8
    assert candidate(root = tree_node([2, 2, 2, None, 2, 2, None, 2, None, 2, None, 2, None, 2, None])) == 8
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 8
    assert candidate(root = tree_node([1, 4, 4, 4, 4, 1, 1, 4, 4, 4, 4, 2, 2, 2, 2])) == 4
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 12
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5])) == 5
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8
    assert candidate(root = tree_node([1, 1, 1, 1, None, 1, None, 1, 1, None, 1, None, 1, None, 1])) == 7
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, None, None, 1, 1, 1, 1, None, None, None, None, 1, 1, 1, 1, 1, 1, 1])) == 9
    assert candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4])) == 2
    assert candidate(root = tree_node([3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3])) == 8
    assert candidate(root = tree_node([1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3])) == 3
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, None, 3])) == 7
    assert candidate(root = tree_node([1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == 9
    assert candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, None, 5, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, None, None, 5])) == 8
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, None, None, None, None, None, None, 4, 4])) == 0
    assert candidate(root = tree_node([1, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 6
    assert candidate(root = tree_node([5, 5, 5, 1, 1, 5, 5, None, None, 5, 5, 5, None, None, 5])) == 4
    assert candidate(root = tree_node([1, 4, 5, 4, 4, None, 5, 1, 1, 1, 1, None, 5, 5, 5, 1, 1, 1, 1])) == 2
    assert candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, 4, None, 4, 5, 5, None, 5, 5, 5])) == 4
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 0
    assert candidate(root = tree_node([2, 2, 2, 2, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 13
    assert candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 1, None, 2, None, 5, 5])) == 3
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == 0
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3, None, None, 3])) == 11
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, None, None, 4, 4, None, None, 5, 5])) == 0
    assert candidate(root = tree_node([1, 2, 2, None, 2, 2, None, None, 2, 2, None, None, 2, 2, 2])) == 3
    assert candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, None, None, None, None, 3, None])) == 3
    assert candidate(root = tree_node([1, 1, 2, 1, None, 2, 1, None, None, None, 1, 1])) == 2
    assert candidate(root = tree_node([5, 5, 5, 5, 5, None, 5, None, None, 5, 5, 5, None, None, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 9
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, None, 5, 5, 5, 5, None, None, 5, 5, None, None, 5, 5, None, None, 5])) == 9
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == 0
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == 0
    assert candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 1, 1, None, 1, 1, None, 1])) == 2
    assert candidate(root = tree_node([7, 7, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7, None, None, 7, 7, 7])) == 11
    assert candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, 4, None, None, None, None, 4, 4])) == 4
    assert candidate(root = tree_node([1, 2, 1, 1, 3, 1, 1, None, None, None, None, None, None, 1, 1, 1])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9
    assert candidate(root = tree_node([5, 4, 5, 4, 4, None, 5, None, None, None, None, 5, 5, None, None, 5, 5, None, None, 5, 5])) == 5
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 11
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 7
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9
    assert candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, None, None, 3, None, 3, None, None, 3])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, None, None, 1, None, None, None, None, 1, None, None, None, 1])) == 4
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, None, 3, 3, None, None, 3, 3, 3, None, None, 3, 3])) == 7
    assert candidate(root = tree_node([1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2])) == 4
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 6
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == 2
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == 4
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4])) == 0
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, 5, 5, None, 5, None, 5, 5, None, 5, 5])) == 7
    assert candidate(root = tree_node([5, 4, 5, 4, 4, 5, 5, None, None, 4, 4, None, None, 4, 4])) == 3
    assert candidate(root = tree_node([5, 4, 5, 1, 1, 5, 5, None, None, None, None, 5, 5])) == 3
    assert candidate(root = tree_node([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 6
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1, 1, None, 1, 1, None, 1])) == 6
    assert candidate(root = tree_node([1, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == 12
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, None, 1, 1, None, None, 1, 1])) == 5
    assert candidate(root = tree_node([1, 1, 1, 1, None, 1, 1, 1, None, None, 1, 1, None, 1, 1, 1, None, 1])) == 8
    assert candidate(root = tree_node([2, 2, 2, None, 2, None, 2, 2, None, 2, 2, None, 2])) == 7
    assert candidate(root = tree_node([5, 5, 5, 5, 5, None, None, 5, 5, 5, 5, None, None, 5, 5, 5, 5])) == 6
    assert candidate(root = tree_node([1, 2, 2, None, 3, None, 3, 3, None, None, 3])) == 1
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == 9
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 10
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 11
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 8
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 9
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == 7
    assert candidate(root = tree_node([1, 1, 1, None, 1, None, 1, 1, 1, None, 1, None, 1, 1, 1, None, 1, None, 1])) == 9
    assert candidate(root = tree_node([5, None, 5, 5, None, None, 5, None, 5, 5, None, 5, None, 5, None, 5])) == 8
    assert candidate(root = tree_node([1, None, 1, None, 1, None, 1, None, 1, None, 1, 1, 1, 1, 1])) == 7
    assert candidate(root = tree_node([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7])) == 0
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, None, None, None, None, 5, 5, None, 5, 5, 5, None, 5, 5, None, 5])) == 7
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 7
    assert candidate(root = tree_node([1, 2, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3])) == 4
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == 8
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, None, 2, 2, None, 2, None, 2, 2, None, 2, 2])) == 7


