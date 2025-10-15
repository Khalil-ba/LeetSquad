def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, None, 0])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, None, 0])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, None, 0, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, None, 0, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, None, 0, 0])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, None, 0, 0])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, None, 0, None, 0, None, None, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, None, 0, None, 0, None, None, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, None, 0, None, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, None, 0, None, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, 0, None, 0, 0, None, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, 0, None, 0, 0, None, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, None, 0, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, None, 0, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, None, None, None, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, None, None, None, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, None, 0, 0, None, 0, 0, 0, None, None, 0, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, None, 0, 0, None, 0, 0, 0, None, None, 0, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, None, 0, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, None, 0, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, None, 0, 0, None, 0, None, None, 0, None, 0, None, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, None, 0, 0, None, 0, None, None, 0, None, 0, None, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, None, 0, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, None, 0, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, None, 0, None, 0, 0, 0, 0, 0, None, None, 0, None, 0, None, 0])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, None, 0, None, 0, 0, 0, 0, 0, None, None, 0, None, 0, None, 0])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None, None])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, None, 0, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, None, 0, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, 0, 0, None, None, None, 0, 0, 0, None, None, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, 0, 0, None, None, None, 0, 0, 0, None, None, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, None, 0, 0, None, None, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, None, 0, 0, None, None, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, None, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, None, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, 0, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, 0, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, 0])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, 0])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, None, None, 0, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, None, None, 0, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, None, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, None, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, None, 0, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, None, 0, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, 0, None, 0, None, 0, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, 0, None, 0, None, 0, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, None, 0, None, 0, None, None, 0, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, None, 0, None, 0, None, None, 0, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, 0, None, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, 0, None, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, None, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, None, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, None, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, None, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, 0])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, 0])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, None, 0, 0, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, None, 0, 0, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, None, 0, 0, 0, 0, None, None, None, None, None, None, None, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, None, 0, 0, 0, 0, None, None, None, None, None, None, None, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, 0, None, 0, 0, None, 0, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, 0, None, 0, 0, None, 0, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, 0, None, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, 0, None, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, None, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, None, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, None, None, 0, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, None, None, 0, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, None, None, 0, 0, None, None])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, None, None, 0, 0, None, None])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, 0, None, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, 0, None, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, 0, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, 0, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, 0, None, 0, None, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, 0, None, 0, None, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, None, 0, 0, None, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, None, 0, 0])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, None, 0, 0, None, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, None, 0, 0])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, None, 0, None, None, None])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, None, 0, None, None, None])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, 0, 0, None, None, 0, 0, None, 0, None, 0, None, 0, None, 0, None, None, 0, None, 0])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, 0, 0, None, None, 0, 0, None, 0, None, 0, None, 0, None, 0, None, None, 0, None, 0])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, None, None, None, 0, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, None, None, None, 0, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, None, 0, None, None, 0, 0, None, 0])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, None, 0, None, None, 0, 0, None, 0])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, None, None, 0, 0, 0, None])) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, None, None, 0, 0, 0, None])) == 4: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 7: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([0, None, 0, None, 0])) == 1
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, None, 0, 0])) == 1
    assert candidate(root = tree_node([0, 0, None, 0, None, 0, None, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0])) == 2
    assert candidate(root = tree_node([0])) == 1
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, 0, None, 0, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, None, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, None, None, None, 0])) == 2
    assert candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, None, 0, 0, None, 0, 0, 0, None, None, 0, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, None, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, 0, None, 0, None, None, 0, None, 0, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None])) == 8
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, None, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 9
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, None, 0, None, 0, 0, 0, 0, 0, None, None, 0, None, 0, None, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None, None])) == 4
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, None, 0, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, None, 0, 0, 0, None, None, None, 0, 0, 0, None, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, None, 0, 0, None, None, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, None, 0, 0, None])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, None, None, None, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0, None, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, None, None, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0])) == 6
    assert candidate(root = tree_node([0, 0, None, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, None, None, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, 0, None, 0, None, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 15
    assert candidate(root = tree_node([0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, None, 0, None, 0, None, None, 0, None])) == 3
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, 0, None, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None])) == 5
    assert candidate(root = tree_node([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, None, 0])) == 10
    assert candidate(root = tree_node([0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0])) == 11
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, None, 0, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, None, 0, 0, 0, 0, None, None, None, None, None, None, None, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0])) == 7
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, 0, None, 0, 0, None, 0, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0])) == 2
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, None, 0, None, None, None, None, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, None, None, 0, 0, None, None])) == 5
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, None, 0, None, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, 0, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, None, 0, 0, None, 0, None, 0, None, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, None, 0, 0, 0, None, 0, 0, None, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, None, 0, 0])) == 8
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, None, 0, None, None, None])) == 3
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, 0, 0, None, None, 0, 0, None, 0, None, 0, None, 0, None, 0, None, None, 0, None, 0])) == 6
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 10
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, None, 0, None, None, None, 0, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, None, 0, 0, 0, None, None, 0, 0, None, None, 0, 0])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, None, 0, None, None, 0, 0, None, 0])) == 3
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 5
    assert candidate(root = tree_node([0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, None, None, 0, 0, 0, None])) == 4
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0])) == 7


