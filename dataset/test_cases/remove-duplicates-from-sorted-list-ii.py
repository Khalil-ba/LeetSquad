def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -100, -99, -98, -98, -97, -96, -96, -95])), list_node([-99, -97, -95]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -100, -99, -98, -98, -97, -96, -96, -95])), list_node([-99, -97, -95])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5])), list_node([2, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5])), list_node([2, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 5, 5])), list_node([1, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 5, 5])), list_node([1, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, 100, -100, 100])), list_node([-100, 100, -100, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, 100, -100, 100])), list_node([-100, 100, -100, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([1])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 3])), list_node([2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 3])), list_node([2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, 100])), list_node([-100, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, 100])), list_node([-100, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 5])), list_node([1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 5])), list_node([1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -99, -99, -98, -97, -97, -96])), list_node([-100, -98, -96]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -99, -99, -98, -97, -97, -96])), list_node([-100, -98, -96])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -99, -98, -98, -97, -97, -96, -95, -94, -94, -93])), list_node([-100, -99, -96, -95, -93]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -99, -98, -98, -97, -97, -96, -95, -94, -94, -93])), list_node([-100, -99, -96, -95, -93])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 4, 5])), list_node([1, 2, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 4, 5])), list_node([1, 2, 5])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 0, 0])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 0, 0])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10, 10, 10, 11, 12, 12, 13])), list_node([1, 3, 5, 6, 7, 9, 11, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10, 10, 10, 11, 12, 12, 13])), list_node([1, 3, 5, 6, 7, 9, 11, 13])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7])), list_node([7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7])), list_node([7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11])), list_node([1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11])), list_node([1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10, 11, 12, 12, 12, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 20, 20])), list_node([2, 3, 4, 6, 7, 9, 11, 13, 14, 16, 18, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10, 11, 12, 12, 12, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 20, 20])), list_node([2, 3, 4, 6, 7, 9, 11, 13, 14, 16, 18, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -1, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5])), list_node([3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -1, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5])), list_node([3, 4])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25, 25, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25, 25, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6])), list_node([1])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 14, 15, 16, 16, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 14, 15, 16, 16, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 10])), list_node([6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 10])), list_node([6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([-100, -100, -99, -99, -98, -98, -97, -97, -96, -96])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([-100, -100, -99, -99, -98, -98, -97, -97, -96, -96])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20])), list_node([1, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20])), list_node([1, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10])), list_node([1, 2, 3, 4, 6, 7, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10])), list_node([1, 2, 3, 4, 6, 7, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10])), list_node([1, 2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10])), list_node([1, 2, 3, 4])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([2, 3, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([2, 3, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 4])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -100, -100, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9])), list_node([4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -100, -100, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9])), list_node([4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-10, -10, -9, -9, -8, -8, -7, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 5])), list_node([-6, -5, -4, -3, -2, -1, 1, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-10, -10, -9, -9, -8, -8, -7, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 5])), list_node([-6, -5, -4, -3, -2, -1, 1, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 11])), list_node([1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 11])), list_node([1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9])), list_node([1])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16])), list_node([2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16])), list_node([2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -100, 0, 0, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9, 9])), list_node([1, 3, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -100, 0, 0, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9, 9])), list_node([1, 3, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10])), list_node([1])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -50, -50, -10, 0, 0, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 100])), list_node([-100, -10, 1, 4, 6, 7, 9, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -50, -50, -10, 0, 0, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 100])), list_node([-100, -10, 1, 4, 6, 7, 9, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 3, 4, 5, 5, 5])), list_node([2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 3, 4, 5, 5, 5])), list_node([2, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([-10, -10, -9, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([-10, -10, -9, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5])), list_node([2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5])), list_node([2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5])), list_node([-1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5])), list_node([-1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10, 10, 10])), list_node([4, 7, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10, 10, 10])), list_node([4, 7, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6])), list_node([2, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6])), list_node([2, 6])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -100, -50, -50, 0, 0, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6])), list_node([1, 3, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -100, -50, -50, 0, 0, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6])), list_node([1, 3, 6])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7])), list_node([3, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7])), list_node([3, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9])), list_node([4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9])), list_node([4])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([-10, -10, -10, -9, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 50, 51, 51, 52, 52, 53, 53, 54, 54, 55, 55, 56, 56, 57, 57, 58, 58, 59, 59, 60, 60, 61, 61, 62, 62, 63, 63, 64, 64, 65, 65, 66, 66, 67, 67, 68, 68, 69, 69, 70, 70, 71, 71, 72, 72, 73, 73, 74, 74, 75, 75, 76, 76, 77, 77, 78, 78, 79, 79, 80, 80, 81, 81, 82, 82, 83, 83, 84, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 89, 90, 90, 91, 91, 92, 92, 93, 93, 94, 94, 95, 95, 96, 96, 97, 97, 98, 98, 99, 99, 100, 100])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([-10, -10, -10, -9, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 50, 51, 51, 52, 52, 53, 53, 54, 54, 55, 55, 56, 56, 57, 57, 58, 58, 59, 59, 60, 60, 61, 61, 62, 62, 63, 63, 64, 64, 65, 65, 66, 66, 67, 67, 68, 68, 69, 69, 70, 70, 71, 71, 72, 72, 73, 73, 74, 74, 75, 75, 76, 76, 77, 77, 78, 78, 79, 79, 80, 80, 81, 81, 82, 82, 83, 83, 84, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 89, 90, 90, 91, 91, 92, 92, 93, 93, 94, 94, 95, 95, 96, 96, 97, 97, 98, 98, 99, 99, 100, 100])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 2])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10])), list_node([6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10])), list_node([6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])), list_node([2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])), list_node([2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5, -4, -4, -3, -3, -2, -1, -1, 0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 6])), list_node([-5, -2, 1, 4, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5, -4, -4, -3, -3, -2, -1, -1, 0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 6])), list_node([-5, -2, 1, 4, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15])), list_node([1, 3, 4, 6, 8, 9, 10, 12, 13, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15])), list_node([1, 3, 4, 6, 8, 9, 10, 12, 13, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -99, -99, -98, -98, -97, -96, -96, -96, -95, -94, -94, -93, -92, -91, -91, -90, -89, -89, -88, -87, -87, -87, -86, -85, -85, -84, -83, -83, -83, -82, -81, -81, -80, -79, -79, -78, -77, -77, -76, -75, -75, -74, -73, -73, -72, -71, -71, -70, -69, -69, -68, -67, -67, -66, -65, -65, -64, -63, -63, -62, -61, -61, -60, -59, -59, -58, -57, -57, -56, -55, -55, -54, -53, -53, -52, -51, -51, -50, -49, -49, -48, -47, -47, -46, -45, -45, -44, -43, -43, -42, -41, -41, -40, -39, -39, -38, -37, -37, -36, -35, -35, -34, -33, -33, -32, -31, -31, -30, -29, -29, -28, -27, -27, -26, -25, -25, -24, -23, -23, -22, -21, -21, -20, -19, -19, -18, -17, -17, -16, -15, -15, -14, -13, -13, -12, -11, -11, -10, -9, -9, -8, -7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([-100, -97, -95, -93, -92, -90, -88, -86, -84, -82, -80, -78, -76, -74, -72, -70, -68, -66, -64, -62, -60, -58, -56, -54, -52, -50, -48, -46, -44, -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -99, -99, -98, -98, -97, -96, -96, -96, -95, -94, -94, -93, -92, -91, -91, -90, -89, -89, -88, -87, -87, -87, -86, -85, -85, -84, -83, -83, -83, -82, -81, -81, -80, -79, -79, -78, -77, -77, -76, -75, -75, -74, -73, -73, -72, -71, -71, -70, -69, -69, -68, -67, -67, -66, -65, -65, -64, -63, -63, -62, -61, -61, -60, -59, -59, -58, -57, -57, -56, -55, -55, -54, -53, -53, -52, -51, -51, -50, -49, -49, -48, -47, -47, -46, -45, -45, -44, -43, -43, -42, -41, -41, -40, -39, -39, -38, -37, -37, -36, -35, -35, -34, -33, -33, -32, -31, -31, -30, -29, -29, -28, -27, -27, -26, -25, -25, -24, -23, -23, -22, -21, -21, -20, -19, -19, -18, -17, -17, -16, -15, -15, -14, -13, -13, -12, -11, -11, -10, -9, -9, -8, -7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([-100, -97, -95, -93, -92, -90, -88, -86, -84, -82, -80, -78, -76, -74, -72, -70, -68, -66, -64, -62, -60, -58, -56, -54, -52, -50, -48, -46, -44, -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -99, -99, -98, -98, -97, -96, -96, -95, -94, -93, -93, -92])), list_node([-100, -97, -95, -94, -92]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -99, -99, -98, -98, -97, -96, -96, -95, -94, -93, -93, -92])), list_node([-100, -97, -95, -94, -92])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11])), list_node([2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11])), list_node([2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 12])), list_node([1, 2, 4, 7, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 12])), list_node([1, 2, 4, 7, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 14, 14, 15])), list_node([1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 14, 14, 15])), list_node([1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30, 30])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30, 30])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 20, 20])), list_node([4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 20, 20])), list_node([4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -99, -98, -98, -97, -96, -95, -95, -94, -94, -93, -92, -92, -91, -91])), list_node([-100, -99, -97, -96, -93]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -99, -98, -98, -97, -96, -95, -95, -94, -94, -93, -92, -92, -91, -91])), list_node([-100, -99, -97, -96, -93])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6])), list_node([3, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6])), list_node([3, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8])), list_node([1, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8])), list_node([1, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert candidate(head = list_node([])) == None
    assert is_same_list(candidate(head = list_node([-100, -100, -99, -98, -98, -97, -96, -96, -95])), list_node([-99, -97, -95]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5])), list_node([2, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 5, 5])), list_node([1, 4]))
    assert is_same_list(candidate(head = list_node([-100, 100, -100, 100])), list_node([-100, 100, -100, 100]))
    assert is_same_list(candidate(head = list_node([1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([1]))
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 3])), list_node([2, 3]))
    assert is_same_list(candidate(head = list_node([-100, 100])), list_node([-100, 100]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 5])), list_node([1, 3]))
    assert is_same_list(candidate(head = list_node([-100, -99, -99, -98, -97, -97, -96])), list_node([-100, -98, -96]))
    assert is_same_list(candidate(head = list_node([-100, -99, -98, -98, -97, -97, -96, -95, -94, -94, -93])), list_node([-100, -99, -96, -95, -93]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 4, 5])), list_node([1, 2, 5]))
    assert candidate(head = list_node([0, 0, 0, 0, 0])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 1])) == None
    assert candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10, 10, 10, 11, 12, 12, 13])), list_node([1, 3, 5, 6, 7, 9, 11, 13]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7])), list_node([7]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11])), list_node([1, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10, 11, 12, 12, 12, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 20, 20])), list_node([2, 3, 4, 6, 7, 9, 11, 13, 14, 16, 18, 19]))
    assert is_same_list(candidate(head = list_node([-1, -1, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5])), list_node([3, 4]))
    assert candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25, 25, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30]))
    assert candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6])), list_node([1]))
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 14, 15, 16, 16, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 10])), list_node([6, 7, 8, 9]))
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])) == None
    assert candidate(head = list_node([-100, -100, -99, -99, -98, -98, -97, -97, -96, -96])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20])), list_node([1, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10])), list_node([1, 2, 3, 4, 6, 7, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10])), list_node([1, 2, 3, 4]))
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([2, 3, 6]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 4]))
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == None
    assert is_same_list(candidate(head = list_node([-100, -100, -100, 0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9])), list_node([4]))
    assert is_same_list(candidate(head = list_node([-10, -10, -9, -9, -8, -8, -7, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 5])), list_node([-6, -5, -4, -3, -2, -1, 1, 4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 11])), list_node([1, 2]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9])), list_node([1]))
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16])), list_node([2]))
    assert is_same_list(candidate(head = list_node([-100, -100, 0, 0, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9, 9])), list_node([1, 3, 7]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10])), list_node([1]))
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == None
    assert is_same_list(candidate(head = list_node([-100, -50, -50, -10, 0, 0, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 100])), list_node([-100, -10, 1, 4, 6, 7, 9, 100]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 3, 4, 5, 5, 5])), list_node([2, 3, 4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])) == None
    assert candidate(head = list_node([-10, -10, -9, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5])), list_node([2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([-1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5])), list_node([-1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    assert candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10, 10, 10])), list_node([4, 7, 9]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6])), list_node([2, 6]))
    assert candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 10, 10, 10, 10])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17])) == None
    assert is_same_list(candidate(head = list_node([-100, -100, -50, -50, 0, 0, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6])), list_node([1, 3, 6]))
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7])), list_node([3, 7]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9])), list_node([4]))
    assert candidate(head = list_node([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])) == None
    assert candidate(head = list_node([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert candidate(head = list_node([-10, -10, -10, -9, -9, -8, -8, -7, -7, -6, -6, -5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 50, 51, 51, 52, 52, 53, 53, 54, 54, 55, 55, 56, 56, 57, 57, 58, 58, 59, 59, 60, 60, 61, 61, 62, 62, 63, 63, 64, 64, 65, 65, 66, 66, 67, 67, 68, 68, 69, 69, 70, 70, 71, 71, 72, 72, 73, 73, 74, 74, 75, 75, 76, 76, 77, 77, 78, 78, 79, 79, 80, 80, 81, 81, 82, 82, 83, 83, 84, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 89, 90, 90, 91, 91, 92, 92, 93, 93, 94, 94, 95, 95, 96, 96, 97, 97, 98, 98, 99, 99, 100, 100])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 2]))
    assert candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9])) == None
    assert candidate(head = list_node([0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10])), list_node([6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])), list_node([2]))
    assert is_same_list(candidate(head = list_node([-5, -4, -4, -3, -3, -2, -1, -1, 0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 6])), list_node([-5, -2, 1, 4, 6]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15])), list_node([1, 3, 4, 6, 8, 9, 10, 12, 13, 15]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])), list_node([1]))
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert is_same_list(candidate(head = list_node([-100, -99, -99, -98, -98, -97, -96, -96, -96, -95, -94, -94, -93, -92, -91, -91, -90, -89, -89, -88, -87, -87, -87, -86, -85, -85, -84, -83, -83, -83, -82, -81, -81, -80, -79, -79, -78, -77, -77, -76, -75, -75, -74, -73, -73, -72, -71, -71, -70, -69, -69, -68, -67, -67, -66, -65, -65, -64, -63, -63, -62, -61, -61, -60, -59, -59, -58, -57, -57, -56, -55, -55, -54, -53, -53, -52, -51, -51, -50, -49, -49, -48, -47, -47, -46, -45, -45, -44, -43, -43, -42, -41, -41, -40, -39, -39, -38, -37, -37, -36, -35, -35, -34, -33, -33, -32, -31, -31, -30, -29, -29, -28, -27, -27, -26, -25, -25, -24, -23, -23, -22, -21, -21, -20, -19, -19, -18, -17, -17, -16, -15, -15, -14, -13, -13, -12, -11, -11, -10, -9, -9, -8, -7, -7, -6, -5, -5, -4, -3, -3, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([-100, -97, -95, -93, -92, -90, -88, -86, -84, -82, -80, -78, -76, -74, -72, -70, -68, -66, -64, -62, -60, -58, -56, -54, -52, -50, -48, -46, -44, -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2]))
    assert is_same_list(candidate(head = list_node([-100, -99, -99, -98, -98, -97, -96, -96, -95, -94, -93, -93, -92])), list_node([-100, -97, -95, -94, -92]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11])), list_node([2, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 10, 10, 11, 11, 12, 12, 12, 12, 12])), list_node([1, 2, 4, 7, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 14, 14, 15])), list_node([1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 15]))
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert is_same_list(candidate(head = list_node([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30, 30])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 20, 20])), list_node([4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19]))
    assert is_same_list(candidate(head = list_node([-100, -99, -98, -98, -97, -96, -95, -95, -94, -94, -93, -92, -92, -91, -91])), list_node([-100, -99, -97, -96, -93]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6])), list_node([3, 6]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8])), list_node([1, 8]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))


