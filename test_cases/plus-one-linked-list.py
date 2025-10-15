def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 2, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 2, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 6, 6, 9, 2, 4, 8, 7, 4, 6, 7, 4, 4, 5, 5, 5, 4, 6, 7, 8, 4, 7, 3, 6, 9, 7, 8, 5, 4, 3, 2, 1])), list_node([7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 6, 6, 9, 2, 4, 8, 7, 4, 6, 7, 4, 4, 5, 5, 5, 4, 6, 7, 8, 4, 7, 3, 6, 9, 7, 8, 5, 4, 3, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 6, 6, 9, 2, 4, 8, 7, 4, 6, 7, 4, 4, 5, 5, 5, 4, 6, 7, 8, 4, 7, 3, 6, 9, 7, 8, 5, 4, 3, 2, 1])), list_node([7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 6, 6, 9, 2, 4, 8, 7, 4, 6, 7, 4, 4, 5, 5, 5, 4, 6, 7, 8, 4, 7, 3, 6, 9, 7, 8, 5, 4, 3, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 2, 4, 3])), list_node([7, 2, 4, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 2, 4, 3])), list_node([7, 2, 4, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9])), list_node([1, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9])), list_node([1, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1])), list_node([2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1])), list_node([2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9])), list_node([1, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9])), list_node([1, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 9, 9])), list_node([1, 3, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 9, 9])), list_node([1, 3, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0])), list_node([1, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0])), list_node([1, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 9, 9, 9])), list_node([2, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 9, 9, 9])), list_node([2, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 8])), list_node([9, 9, 9, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 8])), list_node([9, 9, 9, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 9, 9, 9])), list_node([9, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 9, 9, 9])), list_node([9, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 3, 2, 1])), list_node([4, 3, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 3, 2, 1])), list_node([4, 3, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0])), list_node([1, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0])), list_node([1, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 3, 2, 1, 0, 9, 8, 7, 6, 5])), list_node([4, 3, 2, 1, 0, 9, 8, 7, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 3, 2, 1, 0, 9, 8, 7, 6, 5])), list_node([4, 3, 2, 1, 0, 9, 8, 7, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 0, 0, 0, 0, 0, 0, 0, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 0, 0, 0, 0, 0, 0, 0, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 0, 0, 9, 9, 9])), list_node([1, 2, 0, 1, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 0, 0, 9, 9, 9])), list_node([1, 2, 0, 1, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5])), list_node([9, 8, 7, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5])), list_node([9, 8, 7, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 0, 0, 4, 0, 0, 5, 0, 0])), list_node([2, 3, 0, 0, 4, 0, 0, 5, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 0, 0, 4, 0, 0, 5, 0, 0])), list_node([2, 3, 0, 0, 4, 0, 0, 5, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 9, 0, 9, 9])), list_node([1, 9, 1, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 9, 0, 9, 9])), list_node([1, 9, 1, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 0])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 0])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 0, 0, 9, 9, 0, 0, 9, 9])), list_node([9, 9, 0, 0, 9, 9, 0, 1, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 0, 0, 9, 9, 0, 0, 9, 9])), list_node([9, 9, 0, 0, 9, 9, 0, 1, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 0, 0, 0, 5])), list_node([5, 0, 0, 0, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 0, 0, 0, 5])), list_node([5, 0, 0, 0, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 0, 9, 0, 9])), list_node([9, 0, 9, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 0, 9, 0, 9])), list_node([9, 0, 9, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 0, 0, 0, 0])), list_node([1, 2, 3, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 0, 0, 0, 0])), list_node([1, 2, 3, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 0, 0, 9, 9])), list_node([5, 0, 1, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 0, 0, 9, 9])), list_node([5, 0, 1, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 0, 0, 0, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 1, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 0, 0, 0, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 1, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 1])), list_node([0, 0, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 1])), list_node([0, 0, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 9, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 9, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 0, 9, 0, 9, 0, 9])), list_node([9, 0, 9, 0, 9, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 0, 9, 0, 9, 0, 9])), list_node([9, 0, 9, 0, 9, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 0, 9, 0, 9, 0, 9, 0, 9])), list_node([9, 0, 9, 0, 9, 0, 9, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 0, 9, 0, 9, 0, 9, 0, 9])), list_node([9, 0, 9, 0, 9, 0, 9, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 2, 4]))
    assert is_same_list(candidate(head = list_node([7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 6, 6, 9, 2, 4, 8, 7, 4, 6, 7, 4, 4, 5, 5, 5, 4, 6, 7, 8, 4, 7, 3, 6, 9, 7, 8, 5, 4, 3, 2, 1])), list_node([7, 2, 8, 5, 0, 9, 1, 2, 9, 5, 6, 6, 9, 2, 4, 8, 7, 4, 6, 7, 4, 4, 5, 5, 5, 4, 6, 7, 8, 4, 7, 3, 6, 9, 7, 8, 5, 4, 3, 2, 2]))
    assert is_same_list(candidate(head = list_node([7, 2, 4, 3])), list_node([7, 2, 4, 4]))
    assert is_same_list(candidate(head = list_node([0])), list_node([1]))
    assert is_same_list(candidate(head = list_node([9, 9, 9])), list_node([1, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1])), list_node([2]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9])), list_node([1, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 9, 9])), list_node([1, 3, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 0, 0])), list_node([1, 0, 1]))
    assert is_same_list(candidate(head = list_node([1, 9, 9, 9])), list_node([2, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 8])), list_node([9, 9, 9, 9]))
    assert is_same_list(candidate(head = list_node([8, 9, 9, 9])), list_node([9, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([4, 3, 2, 1])), list_node([4, 3, 2, 2]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0])), list_node([1, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 2]))
    assert is_same_list(candidate(head = list_node([4, 3, 2, 1, 0, 9, 8, 7, 6, 5])), list_node([4, 3, 2, 1, 0, 9, 8, 7, 6, 6]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 6]))
    assert is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1]))
    assert is_same_list(candidate(head = list_node([9, 0, 0, 0, 0, 0, 0, 0, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 1, 0]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 0, 0, 9, 9, 9])), list_node([1, 2, 0, 1, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
    assert is_same_list(candidate(head = list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([5, 0, 5, 0, 5, 0, 5, 0, 5, 1]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5])), list_node([9, 8, 7, 6, 6]))
    assert is_same_list(candidate(head = list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
    assert is_same_list(candidate(head = list_node([2, 3, 0, 0, 4, 0, 0, 5, 0, 0])), list_node([2, 3, 0, 0, 4, 0, 0, 5, 0, 1]))
    assert is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 9, 0, 9, 9])), list_node([1, 9, 1, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 0])), list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2]))
    assert is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 1]))
    assert is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([5, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([6, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([9, 9, 0, 0, 9, 9, 0, 0, 9, 9])), list_node([9, 9, 0, 0, 9, 9, 0, 1, 0, 0]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]))
    assert is_same_list(candidate(head = list_node([5, 0, 0, 0, 5])), list_node([5, 0, 0, 0, 6]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]))
    assert is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([9, 0, 9, 0, 9])), list_node([9, 0, 9, 1, 0]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 0, 0, 0, 0])), list_node([1, 2, 3, 0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 2]))
    assert is_same_list(candidate(head = list_node([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 0, 2]))
    assert is_same_list(candidate(head = list_node([5, 0, 0, 9, 9])), list_node([5, 0, 1, 0, 0]))
    assert is_same_list(candidate(head = list_node([9, 0, 0, 0, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 1, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 6]))
    assert is_same_list(candidate(head = list_node([8, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([9, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 1])), list_node([0, 0, 0, 2]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 1])), list_node([0, 0, 0, 0, 0, 2]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 9, 0]))
    assert is_same_list(candidate(head = list_node([9, 9, 9, 9, 9])), list_node([1, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([9, 0, 9, 0, 9, 0, 9])), list_node([9, 0, 9, 0, 9, 1, 0]))
    assert is_same_list(candidate(head = list_node([9, 0, 9, 0, 9, 0, 9, 0, 9])), list_node([9, 0, 9, 0, 9, 0, 9, 1, 0]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))


