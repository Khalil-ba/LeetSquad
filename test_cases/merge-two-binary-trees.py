def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([2, 4, 6, 8])), tree_node([7, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([2, 4, 6, 8])), tree_node([7, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([4, 5, 6])), tree_node([7, 9, 11, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([4, 5, 6])), tree_node([7, 9, 11, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, None, None, None, None, 8]),root2 = tree_node([7, 4, 5, None, None, None, None, 3, 6, 9])), tree_node([12, 7, 11, 2, 4, None, None, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, None, None, None, None, 8]),root2 = tree_node([7, 4, 5, None, None, None, None, 3, 6, 9])), tree_node([12, 7, 11, 2, 4, None, None, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([0, -1, -2, -3, -4])), tree_node([3, 3, 3, -2, -2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([0, -1, -2, -3, -4])), tree_node([3, 3, 3, -2, -2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, None, 3]),root2 = tree_node([1, None, 2, None, 3])), tree_node([2, 2, 2, 3, None, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, None, 3]),root2 = tree_node([1, None, 2, None, 3])), tree_node([2, 2, 2, 3, None, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, -2, 3]),root2 = tree_node([-4, 5, -6])), tree_node([-3, 3, -3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, -2, 3]),root2 = tree_node([-4, 5, -6])), tree_node([-3, 3, -3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([1])), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([1])), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([7, 6, 5, 4, 3, 2, 1])), tree_node([8, 8, 8, 8, 8, 8, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([7, 6, 5, 4, 3, 2, 1])), tree_node([8, 8, 8, 8, 8, 8, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([2, 1, 3])), tree_node([7, 4, 5, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([2, 1, 3])), tree_node([7, 4, 5, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 6, 2, 4, None, 7]),root2 = tree_node([1, 2, None, 3, None, 6, 8])), tree_node([6, 5, 6, 5, 4, None, 7, 6, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 6, 2, 4, None, 7]),root2 = tree_node([1, 2, None, 3, None, 6, 8])), tree_node([6, 5, 6, 5, 4, None, 7, 6, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 15, 50, 10, 20]),root2 = tree_node([10, 20, 60, 5, 15, 55, 65])), tree_node([15, 35, 110, 15, 35, 55, 65]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 15, 50, 10, 20]),root2 = tree_node([10, 20, 60, 5, 15, 55, 65])), tree_node([15, 35, 110, 15, 35, 55, 65])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([2, None, 3, None, 4])), tree_node([3, None, 5, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([2, None, 3, None, 4])), tree_node([3, None, 5, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([-1, -2, -3]),root2 = tree_node([-4, -5, -6])), tree_node([-5, -7, -9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([-1, -2, -3]),root2 = tree_node([-4, -5, -6])), tree_node([-5, -7, -9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([1, 2, 3, 4])), tree_node([6, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([1, 2, 3, 4])), tree_node([6, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7])), tree_node([2, 4, 6, 8, 10, 12, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7])), tree_node([2, 4, 6, 8, 10, 12, 14])): {e}')
    
    total += 1
    try:
        result = candidate(root1 = tree_node([]),root2 = tree_node([])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root1 = tree_node([]),root2 = tree_node([])) == None: {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([2, 1, None, 3, None])), tree_node([3, 1, 2, 3, None, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([2, 1, None, 3, None])), tree_node([3, 1, 2, 3, None, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([1, 2])), tree_node([2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([1, 2])), tree_node([2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([4, 3, None, 1, 2]),root2 = tree_node([4, 3, None, 2, 1])), tree_node([8, 6, None, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([4, 3, None, 1, 2]),root2 = tree_node([4, 3, None, 2, 1])), tree_node([8, 6, None, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 10, 15]),root2 = tree_node([3, 6, 9, 12, 15, 18, 21])), tree_node([8, 16, 24, 12, 15, 18, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 10, 15]),root2 = tree_node([3, 6, 9, 12, 15, 18, 21])), tree_node([8, 16, 24, 12, 15, 18, 21])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([4, 1, 2])), tree_node([7, 5, 7, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([4, 1, 2])), tree_node([7, 5, 7, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5]),root2 = tree_node([5, None, 4, None, 3, None, 2, None, 1])), tree_node([6, None, 6, None, 6, None, 6, None, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5]),root2 = tree_node([5, None, 4, None, 3, None, 2, None, 1])), tree_node([6, None, 6, None, 6, None, 6, None, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([4, 5, 6, 7, 8, 9, 10])), tree_node([5, 5, 8, 7, 8, 9, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([4, 5, 6, 7, 8, 9, 10])), tree_node([5, 5, 8, 7, 8, 9, 13])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3])), tree_node([4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3])), tree_node([4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 8]),root2 = tree_node([1, 2, 3])), tree_node([6, 5, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 8]),root2 = tree_node([1, 2, 3])), tree_node([6, 5, 11])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3, 4, 5, 6])), tree_node([4, 6, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3, 4, 5, 6])), tree_node([4, 6, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([])), tree_node([1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([])), tree_node([1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([8, 9, 10, 11, 12, 13, 14])), tree_node([9, 11, 13, 15, 17, 19, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([8, 9, 10, 11, 12, 13, 14])), tree_node([9, 11, 13, 15, 17, 19, 21])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, 3]),root2 = tree_node([4, 5, 6])), tree_node([5, 7, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, 3]),root2 = tree_node([4, 5, 6])), tree_node([5, 7, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3, 4, 5])), tree_node([4, 6, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3, 4, 5])), tree_node([4, 6, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2]),root2 = tree_node([3, 4])), tree_node([4, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2]),root2 = tree_node([3, 4])), tree_node([4, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([10, 15, 12, 8, None, 9, 10]),root2 = tree_node([12, 13, 10, 9, None, 10, 11])), tree_node([22, 28, 22, 17, None, 19, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([10, 15, 12, 8, None, 9, 10]),root2 = tree_node([12, 13, 10, 9, None, 10, 11])), tree_node([22, 28, 22, 17, None, 19, 21])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5]),root2 = tree_node([5, 4, 3, 2, 1])), tree_node([6, 6, 6, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5]),root2 = tree_node([5, 4, 3, 2, 1])), tree_node([6, 6, 6, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([4, None, 5, None, 6])), tree_node([5, None, 7, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([4, None, 5, None, 6])), tree_node([5, None, 7, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([3, None, 2, None, 1])), tree_node([4, None, 4, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([3, None, 2, None, 1])), tree_node([4, None, 4, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 3, None, 5, 3]),root2 = tree_node([2, 1, 3, None, 4, None, 7])), tree_node([3, 4, 3, 5, 7, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 3, None, 5, 3]),root2 = tree_node([2, 1, 3, None, 4, None, 7])), tree_node([3, 4, 3, 5, 7, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([3, 5, 2, 6, 7]),root2 = tree_node([4, 1, 2, None, None, 3, 8])), tree_node([7, 6, 4, 6, 7, 3, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([3, 5, 2, 6, 7]),root2 = tree_node([4, 1, 2, None, None, 3, 8])), tree_node([7, 6, 4, 6, 7, 3, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([2, 4, 6])), tree_node([5, 8, 11, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([2, 4, 6])), tree_node([5, 8, 11, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5]),root2 = tree_node([1, None, 2, None, 3, None, 4, None, 5])), tree_node([2, None, 4, None, 6, None, 8, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5]),root2 = tree_node([1, None, 2, None, 3, None, 4, None, 5])), tree_node([2, None, 4, None, 6, None, 8, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([6, 7, 8, 9, 10])), tree_node([9, 11, 13, 10, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([6, 7, 8, 9, 10])), tree_node([9, 11, 13, 10, 12])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 8]),root2 = tree_node([6, 2, 4])), tree_node([11, 5, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 8]),root2 = tree_node([6, 2, 4])), tree_node([11, 5, 12])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),root2 = tree_node([6, 5, 4, 3, 2, 1])), tree_node([7, 5, 6, 3, 2, 1, 3, None, None, None, None, None, None, None, 4, None, 5, None, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),root2 = tree_node([6, 5, 4, 3, 2, 1])), tree_node([7, 5, 6, 3, 2, 1, 3, None, None, None, None, None, None, None, 4, None, 5, None, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([])), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([])), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, None, 9, None, None, 2, 6, None, None, None, None, None, 7]),root2 = tree_node([5, 3, 8, 1, None, None, 9, None, 4, None, 7, None, None, 2, 6])), tree_node([10, 6, 16, 2, 4, None, 18, None, 4, 2, 6, None, 7, None, None, None, None, None, 7, 2, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, None, 9, None, None, 2, 6, None, None, None, None, None, 7]),root2 = tree_node([5, 3, 8, 1, None, None, 9, None, 4, None, 7, None, None, 2, 6])), tree_node([10, 6, 16, 2, 4, None, 18, None, 4, 2, 6, None, 7, None, None, None, None, None, 7, 2, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, 7, 10]),root2 = tree_node([3, 2, 5, None, 4, None, 6])), tree_node([8, 5, 13, 1, 8, 7, 16]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, 7, 10]),root2 = tree_node([3, 2, 5, None, 4, None, 6])), tree_node([8, 5, 13, 1, 8, 7, 16])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, None, 9]),root2 = tree_node([7, 2, 10, None, None, 6, None])), tree_node([12, 5, 18, 1, 4, 6, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, None, 9]),root2 = tree_node([7, 2, 10, None, None, 6, None])), tree_node([12, 5, 18, 1, 4, 6, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([100, -99, 98]),root2 = tree_node([99, 100, -99])), tree_node([199, 1, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([100, -99, 98]),root2 = tree_node([99, 100, -99])), tree_node([199, 1, -1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([3, 4, 6])), tree_node([8, 7, 8, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([3, 4, 6])), tree_node([8, 7, 8, 1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, None, 3]),root2 = tree_node([2, 4])), tree_node([3, 4, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, None, 3]),root2 = tree_node([2, 4])), tree_node([3, 4, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, 3]),root2 = tree_node([])), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, 3]),root2 = tree_node([])), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([1, 2, 3])), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([1, 2, 3])), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 3, None, None, 2]),root2 = tree_node([2, None, 3, None, 4])), tree_node([3, 3, 3, None, 2, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 3, None, None, 2]),root2 = tree_node([2, None, 3, None, 4])), tree_node([3, 3, 3, None, 2, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([2, None, 3])), tree_node([3, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([2, None, 3])), tree_node([3, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([10, 15, 20]),root2 = tree_node([20, 15, 10])), tree_node([30, 30, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([10, 15, 20]),root2 = tree_node([20, 15, 10])), tree_node([30, 30, 30])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([])), tree_node([1, 2, 3, 4, 5, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([])), tree_node([1, 2, 3, 4, 5, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 3, 2, 5]),root2 = tree_node([2, 1, 3, None, 4, None, 7])), tree_node([3, 4, 5, 5, 4, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 3, 2, 5]),root2 = tree_node([2, 1, 3, None, 4, None, 7])), tree_node([3, 4, 5, 5, 4, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([2, 1, 3])), tree_node([2, 1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([2, 1, 3])), tree_node([2, 1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5]),root2 = tree_node([6, 7, 8, 9, 10])), tree_node([7, 9, 11, 13, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5]),root2 = tree_node([6, 7, 8, 9, 10])), tree_node([7, 9, 11, 13, 15])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([2, 4, 6, 8])), tree_node([7, 7, 8, 9]))
    assert is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([4, 5, 6])), tree_node([7, 9, 11, 1, 2]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 6, 2, 4, None, None, 1, None, None, None, None, None, None, 8]),root2 = tree_node([7, 4, 5, None, None, None, None, 3, 6, 9])), tree_node([12, 7, 11, 2, 4, None, None, 1]))
    assert is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([0, -1, -2, -3, -4])), tree_node([3, 3, 3, -2, -2]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, None, 3]),root2 = tree_node([1, None, 2, None, 3])), tree_node([2, 2, 2, 3, None, None, 3]))
    assert is_same_tree(candidate(root1 = tree_node([1, -2, 3]),root2 = tree_node([-4, 5, -6])), tree_node([-3, 3, -3]))
    assert is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([1])), tree_node([1]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([7, 6, 5, 4, 3, 2, 1])), tree_node([8, 8, 8, 8, 8, 8, 8]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([2, 1, 3])), tree_node([7, 4, 5, 1]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 6, 2, 4, None, 7]),root2 = tree_node([1, 2, None, 3, None, 6, 8])), tree_node([6, 5, 6, 5, 4, None, 7, 6, 8]))
    assert is_same_tree(candidate(root1 = tree_node([5, 15, 50, 10, 20]),root2 = tree_node([10, 20, 60, 5, 15, 55, 65])), tree_node([15, 35, 110, 15, 35, 55, 65]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([2, None, 3, None, 4])), tree_node([3, None, 5, None, 7]))
    assert is_same_tree(candidate(root1 = tree_node([-1, -2, -3]),root2 = tree_node([-4, -5, -6])), tree_node([-5, -7, -9]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([1, 2, 3, 4])), tree_node([6, 5, 5, 5]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7])), tree_node([2, 4, 6, 8, 10, 12, 14]))
    assert candidate(root1 = tree_node([]),root2 = tree_node([])) == None
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([2, 1, None, 3, None])), tree_node([3, 1, 2, 3, None, None, 3]))
    assert is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([1, 2])), tree_node([2, 2]))
    assert is_same_tree(candidate(root1 = tree_node([4, 3, None, 1, 2]),root2 = tree_node([4, 3, None, 2, 1])), tree_node([8, 6, None, 3, 3]))
    assert is_same_tree(candidate(root1 = tree_node([5, 10, 15]),root2 = tree_node([3, 6, 9, 12, 15, 18, 21])), tree_node([8, 16, 24, 12, 15, 18, 21]))
    assert is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([4, 1, 2])), tree_node([7, 5, 7, 1, 2]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5]),root2 = tree_node([5, None, 4, None, 3, None, 2, None, 1])), tree_node([6, None, 6, None, 6, None, 6, None, 6]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([4, 5, 6, 7, 8, 9, 10])), tree_node([5, 5, 8, 7, 8, 9, 13]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3])), tree_node([4, 2]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 8]),root2 = tree_node([1, 2, 3])), tree_node([6, 5, 11]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3, 4, 5, 6])), tree_node([4, 6, 5, 6]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([])), tree_node([1, 2]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([8, 9, 10, 11, 12, 13, 14])), tree_node([9, 11, 13, 15, 17, 19, 21]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, 3]),root2 = tree_node([4, 5, 6])), tree_node([5, 7, 9]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2]),root2 = tree_node([3, 4, 5])), tree_node([4, 6, 5]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2]),root2 = tree_node([3, 4])), tree_node([4, 4, 2]))
    assert is_same_tree(candidate(root1 = tree_node([10, 15, 12, 8, None, 9, 10]),root2 = tree_node([12, 13, 10, 9, None, 10, 11])), tree_node([22, 28, 22, 17, None, 19, 21]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5]),root2 = tree_node([5, 4, 3, 2, 1])), tree_node([6, 6, 6, 6, 6]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([4, None, 5, None, 6])), tree_node([5, None, 7, None, 9]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3]),root2 = tree_node([3, None, 2, None, 1])), tree_node([4, None, 4, None, 4]))
    assert is_same_tree(candidate(root1 = tree_node([1, 3, None, 5, 3]),root2 = tree_node([2, 1, 3, None, 4, None, 7])), tree_node([3, 4, 3, 5, 7, None, 7]))
    assert is_same_tree(candidate(root1 = tree_node([3, 5, 2, 6, 7]),root2 = tree_node([4, 1, 2, None, None, 3, 8])), tree_node([7, 6, 4, 6, 7, 3, 8]))
    assert is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([2, 4, 6])), tree_node([5, 8, 11, 1, 2]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5]),root2 = tree_node([1, None, 2, None, 3, None, 4, None, 5])), tree_node([2, None, 4, None, 6, None, 8, None, 10]))
    assert is_same_tree(candidate(root1 = tree_node([3, 4, 5, 1, 2]),root2 = tree_node([6, 7, 8, 9, 10])), tree_node([9, 11, 13, 10, 12]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 8]),root2 = tree_node([6, 2, 4])), tree_node([11, 5, 12]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),root2 = tree_node([6, 5, 4, 3, 2, 1])), tree_node([7, 5, 6, 3, 2, 1, 3, None, None, None, None, None, None, None, 4, None, 5, None, 6]))
    assert is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([])), tree_node([1]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, None, 9, None, None, 2, 6, None, None, None, None, None, 7]),root2 = tree_node([5, 3, 8, 1, None, None, 9, None, 4, None, 7, None, None, 2, 6])), tree_node([10, 6, 16, 2, 4, None, 18, None, 4, 2, 6, None, 7, None, None, None, None, None, 7, 2, 6]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, 7, 10]),root2 = tree_node([3, 2, 5, None, 4, None, 6])), tree_node([8, 5, 13, 1, 8, 7, 16]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 8, 1, 4, None, 9]),root2 = tree_node([7, 2, 10, None, None, 6, None])), tree_node([12, 5, 18, 1, 4, 6, 9]))
    assert is_same_tree(candidate(root1 = tree_node([100, -99, 98]),root2 = tree_node([99, 100, -99])), tree_node([199, 1, -1]))
    assert is_same_tree(candidate(root1 = tree_node([5, 3, 2, 1]),root2 = tree_node([3, 4, 6])), tree_node([8, 7, 8, 1]))
    assert is_same_tree(candidate(root1 = tree_node([1, None, 3]),root2 = tree_node([2, 4])), tree_node([3, 4, 3]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, 3]),root2 = tree_node([])), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([1, 2, 3])), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(root1 = tree_node([1, 3, None, None, 2]),root2 = tree_node([2, None, 3, None, 4])), tree_node([3, 3, 3, None, 2, None, 4]))
    assert is_same_tree(candidate(root1 = tree_node([1]),root2 = tree_node([2, None, 3])), tree_node([3, None, 3]))
    assert is_same_tree(candidate(root1 = tree_node([10, 15, 20]),root2 = tree_node([20, 15, 10])), tree_node([30, 30, 30]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7]),root2 = tree_node([])), tree_node([1, 2, 3, 4, 5, 6, 7]))
    assert is_same_tree(candidate(root1 = tree_node([1, 3, 2, 5]),root2 = tree_node([2, 1, 3, None, 4, None, 7])), tree_node([3, 4, 5, 5, 4, None, 7]))
    assert is_same_tree(candidate(root1 = tree_node([]),root2 = tree_node([2, 1, 3])), tree_node([2, 1, 3]))
    assert is_same_tree(candidate(root1 = tree_node([1, 2, 3, 4, 5]),root2 = tree_node([6, 7, 8, 9, 10])), tree_node([7, 9, 11, 13, 15]))


