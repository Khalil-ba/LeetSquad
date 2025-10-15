def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9, 8, 7]),l2 = list_node([1, 2, 3])), list_node([0, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9, 8, 7]),l2 = list_node([1, 2, 3])), list_node([0, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4, 1])), list_node([7, 0, 8, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4, 1])), list_node([7, 0, 8, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([9, 8, 7, 6, 5])), list_node([0, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([9, 8, 7, 6, 5])), list_node([0, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([5, 5, 5]),l2 = list_node([5, 5, 5, 5, 5])), list_node([0, 1, 1, 6, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([5, 5, 5]),l2 = list_node([5, 5, 5, 5, 5])), list_node([0, 1, 1, 6, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9]),l2 = list_node([9, 9, 9, 9])), list_node([8, 9, 9, 9, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9]),l2 = list_node([9, 9, 9, 9])), list_node([8, 9, 9, 9, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]),l2 = list_node([1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]),l2 = list_node([1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9])), list_node([0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9])), list_node([0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0]),l2 = list_node([9, 9, 9, 9])), list_node([0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0]),l2 = list_node([9, 9, 9, 9])), list_node([0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),l2 = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),l2 = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([0, 0, 9])), list_node([1, 8, 8, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([0, 0, 9])), list_node([1, 8, 8, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([2, 4, 6]),l2 = list_node([1, 3, 5])), list_node([3, 7, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([2, 4, 6]),l2 = list_node([1, 3, 5])), list_node([3, 7, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 1, 1]),l2 = list_node([9, 9, 9])), list_node([0, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 1, 1]),l2 = list_node([9, 9, 9])), list_node([0, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 8]),l2 = list_node([0])), list_node([1, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 8]),l2 = list_node([0])), list_node([1, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 8]),l2 = list_node([0])), list_node([1, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 8]),l2 = list_node([0])), list_node([1, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5])), list_node([5, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5])), list_node([5, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([9, 1])), list_node([0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([9, 1])), list_node([0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([7, 2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([2, 9, 8, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([7, 2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([2, 9, 8, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1]),l2 = list_node([1, 2, 3, 4, 5])), list_node([2, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1]),l2 = list_node([1, 2, 3, 4, 5])), list_node([2, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([6, 4, 5]),l2 = list_node([0, 4, 5])), list_node([6, 8, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([6, 4, 5]),l2 = list_node([0, 4, 5])), list_node([6, 8, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([5]),l2 = list_node([5])), list_node([0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([5]),l2 = list_node([5])), list_node([0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([7, 2, 4, 3]),l2 = list_node([5, 6, 4, 2])), list_node([2, 9, 8, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([7, 2, 4, 3]),l2 = list_node([5, 6, 4, 2])), list_node([2, 9, 8, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 2]),l2 = list_node([3, 4, 5, 6])), list_node([4, 6, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 2]),l2 = list_node([3, 4, 5, 6])), list_node([4, 6, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9, 9, 9]),l2 = list_node([1])), list_node([0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9, 9, 9]),l2 = list_node([1])), list_node([0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9, 9]),l2 = list_node([1])), list_node([0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9, 9]),l2 = list_node([1])), list_node([0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9])), list_node([0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9])), list_node([0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([9, 8, 7])), list_node([0, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([9, 8, 7])), list_node([0, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([7, 8, 9])), list_node([8, 0, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([7, 8, 9])), list_node([8, 0, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([4, 5, 6])), list_node([5, 7, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([4, 5, 6])), list_node([5, 7, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([5, 4, 3, 2, 1])), list_node([6, 6, 6, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([5, 4, 3, 2, 1])), list_node([6, 6, 6, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([0, 0, 1]),l2 = list_node([0, 0, 1])), list_node([0, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([0, 0, 1]),l2 = list_node([0, 0, 1])), list_node([0, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9, 9]),l2 = list_node([1, 1, 1])), list_node([0, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9, 9]),l2 = list_node([1, 1, 1])), list_node([0, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([6, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([3, 4, 2])), list_node([9, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([6, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([3, 4, 2])), list_node([9, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9]),l2 = list_node([1])), list_node([0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9]),l2 = list_node([1])), list_node([0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([1])), list_node([2, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([1])), list_node([2, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([4, 5, 6])), list_node([5, 7, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([4, 5, 6])), list_node([5, 7, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([2, 5, 8])), list_node([3, 3, 8, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([2, 5, 8])), list_node([3, 3, 8, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9]),l2 = list_node([9, 9, 9, 9])), list_node([8, 9, 9, 9, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9]),l2 = list_node([9, 9, 9, 9])), list_node([8, 9, 9, 9, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([3, 2, 1]),l2 = list_node([9, 8, 7])), list_node([2, 1, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([3, 2, 1]),l2 = list_node([9, 8, 7])), list_node([2, 1, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([1, 2, 3, 4, 5])), list_node([2, 4, 6, 8, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([1, 2, 3, 4, 5])), list_node([2, 4, 6, 8, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([0]),l2 = list_node([0])), list_node([0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([0]),l2 = list_node([0])), list_node([0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([2, 4, 9]),l2 = list_node([5, 6, 4, 9])), list_node([7, 0, 4, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([2, 4, 9]),l2 = list_node([5, 6, 4, 9])), list_node([7, 0, 4, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([2, 4, 3, 2, 5, 5, 5]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8, 2, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([2, 4, 3, 2, 5, 5, 5]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8, 2, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0]),l2 = list_node([9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0]),l2 = list_node([9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([2, 4, 6, 8]),l2 = list_node([1, 3, 5, 7])), list_node([3, 7, 1, 6, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([2, 4, 6, 8]),l2 = list_node([1, 3, 5, 7])), list_node([3, 7, 1, 6, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([9]),l2 = list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([9]),l2 = list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([0, 1]),l2 = list_node([0, 1])), list_node([0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([0, 1]),l2 = list_node([0, 1])), list_node([0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(l1 = list_node([7, 1, 6]),l2 = list_node([5, 9, 2])), list_node([2, 1, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(l1 = list_node([7, 1, 6]),l2 = list_node([5, 9, 2])), list_node([2, 1, 9])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(l1 = list_node([9, 8, 7]),l2 = list_node([1, 2, 3])), list_node([0, 1, 1, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4, 1])), list_node([7, 0, 8, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([9, 8, 7, 6, 5])), list_node([0, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([5, 5, 5]),l2 = list_node([5, 5, 5, 5, 5])), list_node([0, 1, 1, 6, 5]))
    assert is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9]),l2 = list_node([9, 9, 9, 9])), list_node([8, 9, 9, 9, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]),l2 = list_node([1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9])), list_node([0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0]),l2 = list_node([9, 9, 9, 9])), list_node([0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),l2 = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([0, 0, 9])), list_node([1, 8, 8, 1]))
    assert is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([2, 4, 6]),l2 = list_node([1, 3, 5])), list_node([3, 7, 1, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 1, 1]),l2 = list_node([9, 9, 9])), list_node([0, 1, 1, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 8]),l2 = list_node([0])), list_node([1, 8]))
    assert is_same_list(candidate(l1 = list_node([1, 8]),l2 = list_node([0])), list_node([1, 8]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5])), list_node([5, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([9, 1])), list_node([0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([7, 2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([2, 9, 8, 3]))
    assert is_same_list(candidate(l1 = list_node([1]),l2 = list_node([1, 2, 3, 4, 5])), list_node([2, 2, 3, 4, 5]))
    assert is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([6, 4, 5]),l2 = list_node([0, 4, 5])), list_node([6, 8, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([5]),l2 = list_node([5])), list_node([0, 1]))
    assert is_same_list(candidate(l1 = list_node([7, 2, 4, 3]),l2 = list_node([5, 6, 4, 2])), list_node([2, 9, 8, 5]))
    assert is_same_list(candidate(l1 = list_node([1, 2]),l2 = list_node([3, 4, 5, 6])), list_node([4, 6, 5, 6]))
    assert is_same_list(candidate(l1 = list_node([9, 9, 9]),l2 = list_node([1])), list_node([0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([9, 9]),l2 = list_node([1])), list_node([0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([1]),l2 = list_node([9])), list_node([0, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([9, 8, 7])), list_node([0, 1, 1, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([7, 8, 9])), list_node([8, 0, 3, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),l2 = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([4, 5, 6])), list_node([5, 7, 9]))
    assert is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([5, 4, 3, 2, 1])), list_node([6, 6, 6, 6, 6]))
    assert is_same_list(candidate(l1 = list_node([0, 0, 1]),l2 = list_node([0, 0, 1])), list_node([0, 0, 2]))
    assert is_same_list(candidate(l1 = list_node([9, 9]),l2 = list_node([1, 1, 1])), list_node([0, 1, 2]))
    assert is_same_list(candidate(l1 = list_node([6, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([3, 4, 2])), list_node([9, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([9]),l2 = list_node([1])), list_node([0, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),l2 = list_node([1])), list_node([2, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(l1 = list_node([1, 2, 3]),l2 = list_node([4, 5, 6])), list_node([5, 7, 9]))
    assert is_same_list(candidate(l1 = list_node([1, 8, 9]),l2 = list_node([2, 5, 8])), list_node([3, 3, 8, 1]))
    assert is_same_list(candidate(l1 = list_node([9, 9, 9, 9, 9, 9, 9]),l2 = list_node([9, 9, 9, 9])), list_node([8, 9, 9, 9, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([3, 2, 1]),l2 = list_node([9, 8, 7])), list_node([2, 1, 9]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 6, 4])), list_node([6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),l2 = list_node([5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]))
    assert is_same_list(candidate(l1 = list_node([1, 2, 3, 4, 5]),l2 = list_node([1, 2, 3, 4, 5])), list_node([2, 4, 6, 8, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([0]),l2 = list_node([0])), list_node([0]))
    assert is_same_list(candidate(l1 = list_node([2, 4, 9]),l2 = list_node([5, 6, 4, 9])), list_node([7, 0, 4, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([2, 4, 3]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8]))
    assert is_same_list(candidate(l1 = list_node([2, 4, 3, 2, 5, 5, 5]),l2 = list_node([5, 6, 4])), list_node([7, 0, 8, 2, 5, 5, 5]))
    assert is_same_list(candidate(l1 = list_node([1, 0, 0, 0, 0]),l2 = list_node([9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([2, 4, 6, 8]),l2 = list_node([1, 3, 5, 7])), list_node([3, 7, 1, 6, 1]))
    assert is_same_list(candidate(l1 = list_node([9]),l2 = list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(l1 = list_node([0, 1]),l2 = list_node([0, 1])), list_node([0, 2]))
    assert is_same_list(candidate(l1 = list_node([7, 1, 6]),l2 = list_node([5, 9, 2])), list_node([2, 1, 9]))


