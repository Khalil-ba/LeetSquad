def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, None, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, None, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 5, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 5, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 1, 1, 1, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 1, 1, 1, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6, 6, 6, 6, 6, 6, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6, 6, 6, 6, 6, 6, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, None, 2, 2, None, 2, None, 2, None, 2, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, None, 2, 2, None, 2, None, 2, None, 2, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, None, 9, None, 9, None, 9, None])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, None, 9, None, 9, None, 9, None])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, None, 9, None, 9])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, None, 9, None, 9])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 10, 10, None, 10, 10, None, 10, None, 10, 10, 10, None, 10])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 10, 10, None, 10, 10, None, 10, None, 10, 10, 10, None, 10])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, 4, None, None, 4, 4, None, 4, 4, 4, None, 4, 4, None, None, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, 4, None, None, 4, 4, None, 4, 4, 4, None, 4, 4, None, None, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, None, 6, 6, 6, None, None, 6, 6, 6, None, 6, 6, 6, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, None, 6, 6, 6, None, None, 6, 6, 6, None, 6, 6, 6, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, None, None, None, 1, 1, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, None, None, None, 1, 1, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 6, 6, 6, None, 6, 6, 6, None, 6, 6, 6, 6, None, 6, 6, 6, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 6, 6, 6, None, 6, 6, 6, None, 6, 6, 6, 6, None, 6, 6, 6, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, None, None, None, None, None, None, None, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, None, None, None, None, None, None, None, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, 9, 9, None, 9, None, 9, 9, 9, 9, 9])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, 9, 9, None, 9, None, 9, 9, 9, 9, 9])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, None, None, 6, 6, 6, 6, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, None, None, 6, 6, 6, 6, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, None, 3, None, 3, None, 3])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, None, 3, None, 3, None, 3])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, None, 3, 3, None, 3, 3, 3, None, 3])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, None, 3, 3, None, 3, 3, 3, None, 3])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, None, 10, None, 10, None, 10])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, None, 10, None, 10, None, 10])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, None, 7, None, 7, None, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, None, 7, None, 7, None, 7])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, None, 4, None, 4, None, 4, 4, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, None, 4, None, 4, None, 4, 4, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, None, None, 7, 7, None, None, 7, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, None, None, 7, 7, None, None, 7, 7])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, None, None, 10, None, 10, None, 10, None, 10, None, 10, None, 10])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, None, None, 10, None, 10, None, 10, None, 10, None, 10, None, 10])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, 7])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, 7])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, 4])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, 4])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, 6])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, 6])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 2, 1, 1, 1, 1, None, 1, 1, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 2, 1, 1, 1, 1, None, 1, 1, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 1, None, 1, None, 1, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 1, None, 1, None, 1, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, None, 3, 3, 3, None, None, 3])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, None, 3, 3, 3, None, None, 3])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 2, 1, 1, None, None, None, None, 1, 1, 1, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 2, 1, 1, None, None, None, None, 1, 1, 1, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 2, 1, 1, None, 1, None, 1, None, 1, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 2, 1, 1, None, 1, None, 1, None, 1, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 1, 1, 1, None, 1, None, 1, None, 1, None, 1])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 1, 1, 1, None, 1, None, 1, None, 1, None, 1])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 5])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 5])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, None, None, 2, 2, 2, 2, 2, 2, 2, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, None, None, 2, 2, 2, 2, 2, 2, 2, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, 9, None, None, 9, 9, 9, 9, 9])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, 9, None, None, 9, 9, 9, 9, 9])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, 5, 5, 5, 5, 5])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, 5, 5, 5, 5, 5])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 8, None, 8, None, 8, None, 8, None, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 8, None, 8, None, 8, None, 8, None, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 8, 8, 8, 8, 8, None, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 8, 8, 8, 8, 8, None, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, None, 9, 9, 9, 9, 9, 9, 9])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, None, 9, 9, 9, 9, 9, 9, 9])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([6, 6, 6, 6, 6, 6, None, 6, 6, None, 6, 6, None, 6, 6])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([6, 6, 6, 6, 6, 6, None, 6, 6, None, 6, 6, None, 6, 6])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, None, 11, None, 11, None, 11, None, 11, None, 11])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, None, 11, None, 11, None, 11, None, 11, None, 11])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, None, 11, None, 11, None, 11, None, 11])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, None, 11, None, 11, None, 11, None, 11])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, None, None, 4, 4, None, None, 4])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, None, None, 4, 4, None, None, 4])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, 8])) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, 8])) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, None, 8, None, 8])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, None, 8, None, 8])) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, 7, 7, 7, 7, 7])) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, 7, 7, 7, 7, 7])) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 1, 1, 1, 1, None, 1])) == True
    assert candidate(root = tree_node([2, 2, 2, 5, 2])) == False
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 2])) == False
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0])) == True
    assert candidate(root = tree_node([1, 1, 2])) == False
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5])) == True
    assert candidate(root = tree_node([1, 2, 1, 1, 1, None, 1])) == False
    assert candidate(root = tree_node([0])) == True
    assert candidate(root = tree_node([5])) == True
    assert candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6, 6, 6, 6, 6, 6, 6])) == True
    assert candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == True
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, None, 2, 2, None, 2, None, 2, None, 2, 2])) == True
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, None, None, 9, None, 9, None, 9, None])) == True
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, None, 9, None, 9])) == True
    assert candidate(root = tree_node([10, 10, 10, None, 10, 10, None, 10, None, 10, 10, 10, None, 10])) == True
    assert candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, 4, None, None, 4, 4, None, 4, 4, 4, None, 4, 4, None, None, 4])) == True
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == True
    assert candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, None, 6, 6, 6, None, None, 6, 6, 6, None, 6, 6, 6, 6])) == True
    assert candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, None, None, None, 1, 1, 1, 1])) == True
    assert candidate(root = tree_node([6, 6, 6, 6, None, 6, 6, 6, None, 6, 6, 6, 6, None, 6, 6, 6, 6])) == True
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, None, None, None, None, None, None, None, 1, 1])) == True
    assert candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, 9, 9, None, 9, None, 9, 9, 9, 9, 9])) == True
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True
    assert candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, None, None, 6, 6, 6, 6, 6])) == True
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, None, 3, None, 3, None, 3])) == True
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, None, 3, 3, None, 3, 3, 3, None, 3])) == True
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True
    assert candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8, None, 8, 8, 8])) == True
    assert candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, None, 10, None, 10, None, 10])) == True
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, None, 7, None, 7, None, 7])) == True
    assert candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, None, 4, None, 4, None, 4, 4, 4])) == True
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, None, None, 7, 7, None, None, 7, 7])) == True
    assert candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, None, None, 10, None, 10, None, 10, None, 10, None, 10, None, 10])) == True
    assert candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, None, 6, 7])) == False
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, None, 3, 4])) == False
    assert candidate(root = tree_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, None, 6])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, 1])) == True
    assert candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True
    assert candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, None, 4, 5])) == False
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, None, 5, 6])) == False
    assert candidate(root = tree_node([1, 1, 2, 1, 1, 1, 1, None, 1, 1, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1, None, 1])) == False
    assert candidate(root = tree_node([1, 2, None, 1, None, 1, None, 1, None, 1])) == False
    assert candidate(root = tree_node([3, 3, 3, 3, None, 3, 3, 3, None, None, 3])) == True
    assert candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
    assert candidate(root = tree_node([1, 1, 2, 1, 1, None, None, None, None, 1, 1, 1, 1])) == False
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])) == False
    assert candidate(root = tree_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == True
    assert candidate(root = tree_node([1, 1, 2, 1, 1, None, 1, None, 1, None, 1, None, 1])) == False
    assert candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) == True
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
    assert candidate(root = tree_node([1, 2, 1, 1, 1, None, 1, None, 1, None, 1, None, 1])) == False
    assert candidate(root = tree_node([4, 4, 4, 4, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 4, None, 4, 4, 5])) == False
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, None, None, None, 2, 2, 2, 2, 2, 2, 2, 2])) == True
    assert candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, 9, None, None, 9, 9, 9, 9, 9])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, 5, 5, 5, 5, 5])) == True
    assert candidate(root = tree_node([8, 8, None, 8, None, 8, None, 8, None, 8])) == True
    assert candidate(root = tree_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2, None, 2])) == True
    assert candidate(root = tree_node([8, 8, 8, 8, 8, 8, None, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])) == True
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])) == True
    assert candidate(root = tree_node([9, 9, 9, 9, None, 9, 9, None, 9, 9, 9, 9, 9, 9, 9])) == True
    assert candidate(root = tree_node([6, 6, 6, 6, 6, 6, None, 6, 6, None, 6, 6, None, 6, 6])) == True
    assert candidate(root = tree_node([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, None, 11, None, 11, None, 11, None, 11, None, 11])) == True
    assert candidate(root = tree_node([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, None, 11, None, 11, None, 11, None, 11])) == True
    assert candidate(root = tree_node([4, 4, 4, 4, 4, None, 4, None, None, 4, 4, None, None, 4])) == True
    assert candidate(root = tree_node([10, 10, 10, 10, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10, None, 10, 10, 10])) == True
    assert candidate(root = tree_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == True
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, None, 7, 8])) == False
    assert candidate(root = tree_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, None, 8, None, 8])) == True
    assert candidate(root = tree_node([7, 7, 7, 7, 7, 7, 7, 7, None, 7, 7, 7, 7, 7, 7])) == True


