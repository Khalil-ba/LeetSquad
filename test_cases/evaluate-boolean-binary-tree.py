def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 1, None, None, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 1, None, None, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 1, None, None, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 1, None, None, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, None, None, 1, 1, None, None, None, None])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, None, None, 1, 1, None, None, None, None])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 1, 1, 0, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 1, 1, 0, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, None, None, 0, 0, None, None, 1, 0, None, None, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, None, None, 0, 0, None, None, 1, 0, None, None, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 0, 0, None, None, None, None])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 0, 0, None, None, None, None])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 0, 1, None, None, None, None])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 0, 1, None, None, None, None])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 3, 0, 1, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 3, 0, 1, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, None, None, 0, 1, None, None, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, None, None, 0, 1, None, None, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 0, 0, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 0, 0, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 2, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 2, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 1, 0, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 1, 0, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 0, 1, 1, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 0, 1, 1, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 1, None, None, None, None])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 1, None, None, None, None])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 3, 2, 2, 2, 3, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 3, 2, 2, 2, 3, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 3, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 3, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 3, 3, 2, 2, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 3, 3, 2, 2, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, 2, 1, 0, 1, None, None, None, None, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, 2, 1, 0, 1, None, None, None, None, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 3, 1, 3, 0, 1, 0, 1, 3, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 3, 1, 3, 0, 1, 0, 1, 3, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, 2, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, 2, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 3, 1, 3, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 3, 1, 3, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 2, 3, 2, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 2, 3, 2, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 3, 2, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 3, 2, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 0, 1, 3, 1, 0, 0, 1, 1, 0, 1, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 0, 1, 3, 1, 0, 0, 1, 1, 0, 1, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 3, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 3, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 3, 2, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 3, 2, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 2, 0, 0, 1, 3, 1, 0, 1, 3, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 2, 0, 0, 1, 3, 1, 0, 1, 3, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 0, 1, 1, 0, 3, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 0, 1, 1, 0, 3, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 2, 1, 0, 1, 2, 1, 0, 0, 1, 1, 0, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 2, 1, 0, 1, 2, 1, 0, 0, 1, 1, 0, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 1, 2, 1, 3, 0, 0, 0, 1, 1, 0, 1, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 1, 2, 1, 3, 0, 0, 0, 1, 1, 0, 1, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 2, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 2, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 2, 1, 1, 0, 2, 0, 1, 1, 0, 2, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 2, 1, 1, 0, 2, 0, 1, 1, 0, 2, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 3, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 3, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 1, 0, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 1, 0, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, 1, 1, 1, 1, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, 1, 1, 1, 1, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, 0, 1, 2, 1, 3, 0, 1, 0, 1, 3, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, 0, 1, 2, 1, 3, 0, 1, 0, 1, 3, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 1, 0, 3, 1, 1, 0, 0, 1, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 1, 0, 3, 1, 1, 0, 0, 1, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 1, 0, 1, 0, 3, 1, 0, 1, 0, 3, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 1, 0, 1, 0, 3, 1, 0, 1, 0, 3, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 2, 0, 0, 1, 3, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 2, 0, 0, 1, 3, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 3, 2, 3, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 3, 2, 3, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 2, 3, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 2, 3, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 2, 2, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 2, 2, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 3, 3, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 3, 3, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 3, 3, 1, 1, 3, 1, 0, 3, 0, 1, 3, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 3, 3, 1, 1, 3, 1, 0, 3, 0, 1, 3, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 3, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 3, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 2, 3, 0, 3, 1, 1, 0, 3, 0, 1, 1, 0, 1, 0, 3, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 2, 3, 0, 3, 1, 1, 0, 3, 0, 1, 1, 0, 1, 0, 3, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 2, 1, 3, 0, 1, 0, 0, 1, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 2, 1, 3, 0, 1, 0, 0, 1, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 3, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 3, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 3, 2, 3, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 3, 2, 3, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 2, 2, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 2, 2, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 2, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 2, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 2, 3, 0, 1, 1, None, None, None, None, 0, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 2, 3, 0, 1, 1, None, None, None, None, 0, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 3, 3, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 3, 3, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 3, 3, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 3, 3, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 3, 2, 2, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 3, 2, 2, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 3, 3, 1, 1, 0, 2, 1, 0, 1, 2, 1, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 3, 3, 1, 1, 0, 2, 1, 0, 1, 2, 1, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 3, 1, 0, 1, 2, 0, 1, 0, 2, 1, 0, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 3, 1, 0, 1, 2, 0, 1, 0, 2, 1, 0, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 2, 3, 1, 2, 0, 1, 0, 0, 1, 0, 1, 1, 0])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 2, 3, 1, 2, 0, 1, 0, 0, 1, 0, 1, 1, 0])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 2, 3, 1, 3, 3, 1, 0, 1, 0, 1, 0, 0, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 2, 3, 1, 3, 3, 1, 0, 1, 0, 1, 0, 0, 1])) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([3, 1, 1, None, None, 0, 0])) == False
    assert candidate(root = tree_node([2, 3, 1, None, None, 0, 1])) == True
    assert candidate(root = tree_node([2, 3, 2, None, None, 1, 1, None, None, None, None])) == True
    assert candidate(root = tree_node([2, 1, 1])) == True
    assert candidate(root = tree_node([2, 3, 3, 1, 1, 0, 0])) == True
    assert candidate(root = tree_node([3, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1])) == True
    assert candidate(root = tree_node([3, 2, 2, None, None, 0, 0, None, None, 1, 0, None, None, 1, 1])) == True
    assert candidate(root = tree_node([3, 0, 0, None, None, None, None])) == False
    assert candidate(root = tree_node([3, 0, 1, None, None, None, None])) == False
    assert candidate(root = tree_node([3, 0, 0])) == False
    assert candidate(root = tree_node([2, 3, 3, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0])) == False
    assert candidate(root = tree_node([3, 0, 1])) == False
    assert candidate(root = tree_node([2, 2, 3, 0, 1, 0, 1])) == True
    assert candidate(root = tree_node([2, 3, 2, None, None, 0, 1, None, None, 0, 1])) == True
    assert candidate(root = tree_node([0])) == False
    assert candidate(root = tree_node([2, 3, 3, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([3, 2, 2, 0, 0, 1, 1])) == False
    assert candidate(root = tree_node([3, 3, 2, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 1, 3, None, None, 0, 1])) == True
    assert candidate(root = tree_node([2, 2, 2, 1, 0, 0, 1])) == True
    assert candidate(root = tree_node([2, 3, 2, 0, 1, 1, 0])) == True
    assert candidate(root = tree_node([2, 1, 1, None, None, None, None])) == True
    assert candidate(root = tree_node([3, 2, 3, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])) == False
    assert candidate(root = tree_node([2, 2, 3, 2, 2, 2, 3, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([2, 2, 3, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([2, 3, 2, 3, 3, 2, 2, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == True
    assert candidate(root = tree_node([3, 2, 2, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([3, 2, 3, 2, 1, 0, 1, None, None, None, None, 1, 0])) == False
    assert candidate(root = tree_node([2, 2, 3, 1, 3, 0, 1, 0, 1, 3, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 3, 2, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0])) == False
    assert candidate(root = tree_node([2, 2, 3, 1, 3, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0])) == False
    assert candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 3, 2, 2, 3, 2, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 3, 2, 3, 2, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])) == True
    assert candidate(root = tree_node([2, 3, 2, 0, 1, 3, 1, 0, 0, 1, 1, 0, 1, 1, 0])) == False
    assert candidate(root = tree_node([2, 3, 2, 3, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([2, 3, 2, 3, 2, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 3, 3, 2, 0, 0, 1, 3, 1, 0, 1, 3, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 2, 0, 1, 1, 0, 3, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 3, 2, 2, 1, 0, 1, 2, 1, 0, 0, 1, 1, 0, 0])) == True
    assert candidate(root = tree_node([2, 2, 2, 1, 2, 1, 3, 0, 0, 0, 1, 1, 0, 1, 0])) == True
    assert candidate(root = tree_node([3, 3, 3, 2, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 3, 3, 2, 1, 1, 0, 2, 0, 1, 1, 0, 2, 0, 1])) == False
    assert candidate(root = tree_node([3, 2, 2, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])) == False
    assert candidate(root = tree_node([2, 3, 2, 3, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 2, 1, 0, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 3, 1, 1, 1, 1, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0])) == False
    assert candidate(root = tree_node([3, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 3, 0, 1, 2, 1, 3, 0, 1, 0, 1, 3, 0, 1])) == False
    assert candidate(root = tree_node([2, 3, 2, 1, 0, 3, 1, 1, 0, 0, 1, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([3, 2, 2, 1, 0, 1, 0, 3, 1, 0, 1, 0, 3, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([3, 2, 2, 2, 0, 0, 1, 3, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 2, 3, 2, 3, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1])) == False
    assert candidate(root = tree_node([2, 3, 3, 2, 3, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 3, 3, 2, 2, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0])) == True
    assert candidate(root = tree_node([3, 2, 2, 3, 3, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 2, 2, 3, 3, 1, 1, 3, 1, 0, 3, 0, 1, 3, 0])) == True
    assert candidate(root = tree_node([2, 3, 3, 3, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 1])) == False
    assert candidate(root = tree_node([2, 1, 2, 3, 0, 3, 1, 1, 0, 3, 0, 1, 1, 0, 1, 0, 3, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0])) == False
    assert candidate(root = tree_node([3, 2, 2, 2, 1, 3, 0, 1, 0, 0, 1, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([2, 2, 3, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])) == True
    assert candidate(root = tree_node([2, 2, 3, 2, 3, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1])) == True
    assert candidate(root = tree_node([3, 3, 3, 2, 2, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1])) == False
    assert candidate(root = tree_node([2, 3, 2, 3, 2, 3, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == True
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 2, 2, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1])) == False
    assert candidate(root = tree_node([2, 2, 2, 3, 3, 3, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 1, 2, 3, 0, 1, 1, None, None, None, None, 0, 0])) == True
    assert candidate(root = tree_node([2, 3, 3, 3, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 2, 3, 3, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == False
    assert candidate(root = tree_node([2, 3, 2, 2, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0])) == False
    assert candidate(root = tree_node([3, 2, 3, 3, 1, 1, 0, 2, 1, 0, 1, 2, 1, 0, 0])) == False
    assert candidate(root = tree_node([3, 2, 2, 3, 1, 0, 1, 2, 0, 1, 0, 2, 1, 0, 0])) == False
    assert candidate(root = tree_node([3, 3, 2, 3, 1, 2, 0, 1, 0, 0, 1, 0, 1, 1, 0])) == False
    assert candidate(root = tree_node([3, 2, 2, 3, 1, 3, 3, 1, 0, 1, 0, 1, 0, 0, 1])) == False


