def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 6, 7, 8, 9])), list_node([1, 1, 3, 5, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 6, 7, 8, 9])), list_node([1, 1, 3, 5, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([2, 4, 6, 9, 1, 3, 5, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([2, 4, 6, 9, 1, 3, 5, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0])), list_node([0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0])), list_node([0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9])), list_node([1, 9, 9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9])), list_node([1, 9, 9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 8, 9])), list_node([3, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 8, 9])), list_node([3, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([2, 4, 6, 9, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([2, 4, 6, 9, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 0, 0])), list_node([1, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 0, 0])), list_node([1, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0])), list_node([2, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0])), list_node([2, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 7, 8, 9, 0])), list_node([1, 3, 5, 7, 8, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 7, 8, 9, 0])), list_node([1, 3, 5, 7, 8, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 0, 8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 0, 8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4])), list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4])), list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6])), list_node([7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6])), list_node([7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])), list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])), list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 8, 9, 0, 1, 2, 3, 4, 5, 6])), list_node([1, 5, 7, 8, 0, 2, 4, 6, 9, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 8, 9, 0, 1, 2, 3, 4, 5, 6])), list_node([1, 5, 7, 8, 0, 2, 4, 6, 9, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 1, 3, 5, 7, 9])), list_node([4, 9, 3, 6, 0, 2, 7, 1, 5, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 1, 3, 5, 7, 9])), list_node([4, 9, 3, 6, 0, 2, 7, 1, 5, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9])), list_node([1, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9])), list_node([1, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 3, 2, 1])), list_node([8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 3, 2, 1])), list_node([8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 3, 2, 1, 0])), list_node([8, 6, 4, 2, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 3, 2, 1, 0])), list_node([8, 6, 4, 2, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 5, 6, 7, 8, 9, 0, 1, 2, 3])), list_node([9, 1, 3, 5, 7, 8, 0, 2, 4, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 5, 6, 7, 8, 9, 0, 1, 2, 3])), list_node([9, 1, 3, 5, 7, 8, 0, 2, 4, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 5, 3, 0, 8, 6, 4, 2, 1, 9, 7, 5, 3, 0, 8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 5, 3, 0, 8, 6, 4, 2, 1, 9, 7, 5, 3, 0, 8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 0, 5, 0, 5])), list_node([1, 0, 1, 0, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 0, 5, 0, 5])), list_node([1, 0, 1, 0, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 7, 5, 3, 0, 8, 6, 4, 2, 1, 9, 7, 5, 3, 0, 8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 7, 5, 3, 0, 8, 6, 4, 2, 1, 9, 7, 5, 3, 0, 8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1])), list_node([1, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1])), list_node([1, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 9, 7, 5, 3, 0, 8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 9, 7, 5, 3, 0, 8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9])), list_node([2, 7, 1, 5, 8, 2, 7, 1, 5, 8, 2, 7, 1, 5, 8, 2, 7, 1, 5, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9])), list_node([2, 7, 1, 5, 8, 2, 7, 1, 5, 8, 2, 7, 1, 5, 8, 2, 7, 1, 5, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([2, 4, 6, 9, 1, 3, 5, 7, 8, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([2, 4, 6, 9, 1, 3, 5, 7, 8, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([8, 6, 4, 3, 9, 7, 5, 3, 0, 8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([8, 6, 4, 3, 9, 7, 5, 3, 0, 8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([1, 9, 7, 5, 3, 0, 8, 6, 4, 2, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([1, 9, 7, 5, 3, 0, 8, 6, 4, 2, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5])), list_node([5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5])), list_node([5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2])), list_node([4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2])), list_node([4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0])), list_node([7, 3, 8, 5, 1, 6, 2, 9, 4, 0, 7, 3, 8, 5, 1, 6, 2, 9, 4, 0, 7, 3, 8, 5, 1, 6, 2, 9, 4, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0])), list_node([7, 3, 8, 5, 1, 6, 2, 9, 4, 0, 7, 3, 8, 5, 1, 6, 2, 9, 4, 0, 7, 3, 8, 5, 1, 6, 2, 9, 4, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 7, 2, 8, 9, 4, 6, 2, 3, 1])), list_node([7, 4, 5, 7, 8, 9, 2, 4, 6, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 7, 2, 8, 9, 4, 6, 2, 3, 1])), list_node([7, 4, 5, 7, 8, 9, 2, 4, 6, 2])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([5, 6, 7, 8, 9])), list_node([1, 1, 3, 5, 7, 8]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([2, 4, 6, 9, 1, 3, 5, 7, 8]))
    assert is_same_list(candidate(head = list_node([0])), list_node([0]))
    assert is_same_list(candidate(head = list_node([9, 9, 9])), list_node([1, 9, 9, 8]))
    assert is_same_list(candidate(head = list_node([1, 8, 9])), list_node([3, 7, 8]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([2, 4, 6, 9, 0]))
    assert is_same_list(candidate(head = list_node([5, 0, 0])), list_node([1, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0])), list_node([2, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([6, 7, 8, 9, 0])), list_node([1, 3, 5, 7, 8, 0]))
    assert is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 0, 8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]))
    assert is_same_list(candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4])), list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8]))
    assert is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
    assert is_same_list(candidate(head = list_node([3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6])), list_node([7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 3, 8, 7, 2]))
    assert is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])), list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
    assert is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]))
    assert is_same_list(candidate(head = list_node([7, 8, 9, 0, 1, 2, 3, 4, 5, 6])), list_node([1, 5, 7, 8, 0, 2, 4, 6, 9, 1, 2]))
    assert is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 1, 3, 5, 7, 9])), list_node([4, 9, 3, 6, 0, 2, 7, 1, 5, 8]))
    assert is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
    assert is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]))
    assert is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0]))
    assert is_same_list(candidate(head = list_node([7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9])), list_node([1, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 8]))
    assert is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
    assert is_same_list(candidate(head = list_node([4, 3, 2, 1])), list_node([8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]))
    assert is_same_list(candidate(head = list_node([4, 3, 2, 1, 0])), list_node([8, 6, 4, 2, 0]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
    assert is_same_list(candidate(head = list_node([4, 5, 6, 7, 8, 9, 0, 1, 2, 3])), list_node([9, 1, 3, 5, 7, 8, 0, 2, 4, 6]))
    assert is_same_list(candidate(head = list_node([5, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))
    assert is_same_list(candidate(head = list_node([7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 5, 3, 0, 8, 6, 4, 2, 1, 9, 7, 5, 3, 0, 8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([5, 0, 5, 0, 5])), list_node([1, 0, 1, 0, 1, 0]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
    assert is_same_list(candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 7, 5, 3, 0, 8, 6, 4, 2, 1, 9, 7, 5, 3, 0, 8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])), list_node([1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6]))
    assert is_same_list(candidate(head = list_node([9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1])), list_node([1, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 2]))
    assert is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 9, 7, 5, 3, 0, 8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0, 4, 9, 3, 6, 0]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9])), list_node([2, 7, 1, 5, 8, 2, 7, 1, 5, 8, 2, 7, 1, 5, 8, 2, 7, 1, 5, 8]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([2, 4, 6, 9, 1, 3, 5, 7, 8, 0]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 0, 2, 4, 6, 8, 0])), list_node([4, 9, 3, 6, 0, 4, 9, 3, 6, 0]))
    assert is_same_list(candidate(head = list_node([4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([8, 6, 4, 3, 9, 7, 5, 3, 0, 8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([1, 9, 7, 5, 3, 0, 8, 6, 4, 2, 0]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]))
    assert is_same_list(candidate(head = list_node([4, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
    assert is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]))
    assert is_same_list(candidate(head = list_node([2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5, 8, 2, 5])), list_node([5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 0]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2])), list_node([4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8]))
    assert is_same_list(candidate(head = list_node([3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0])), list_node([7, 3, 8, 5, 1, 6, 2, 9, 4, 0, 7, 3, 8, 5, 1, 6, 2, 9, 4, 0, 7, 3, 8, 5, 1, 6, 2, 9, 4, 0]))
    assert is_same_list(candidate(head = list_node([3, 7, 2, 8, 9, 4, 6, 2, 3, 1])), list_node([7, 4, 5, 7, 8, 9, 2, 4, 6, 2]))


