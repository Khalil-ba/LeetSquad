def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 1])), list_node([2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 1])), list_node([2])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4])), list_node([1, 2, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4])), list_node([1, 2, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 4, 7, 1, 2, 6])), list_node([1, 3, 4, 1, 2, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 4, 7, 1, 2, 6])), list_node([1, 3, 4, 1, 2, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6])), list_node([1, 2, 3, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6])), list_node([1, 2, 3, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19, 21])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99999, 99998, 99997, 99996, 99994, 99993, 99992, 99991]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99999, 99998, 99997, 99996, 99994, 99993, 99992, 99991])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([31, 29, 27, 25, 23, 21, 19, 17, 13, 11, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([31, 29, 27, 25, 23, 21, 19, 17, 13, 11, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])), list_node([1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])), list_node([1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])), list_node([1, 2, 3, 4, 6, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])), list_node([1, 2, 3, 4, 6, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 1])), list_node([1, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 1])), list_node([1, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([21, 19, 17, 15, 13, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([21, 19, 17, 15, 13, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([5, 4, 3, 2, 1, 0, -1, -2, -4, -5, -6, -7, -8, -9, -10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([5, 4, 3, 2, 1, 0, -1, -2, -4, -5, -6, -7, -8, -9, -10])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])), list_node([100000, 99999, 99998, 99996, 99995]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])), list_node([100000, 99999, 99998, 99996, 99995])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 4, 7, 1, 2, 6, 8])), list_node([1, 3, 4, 7, 2, 6, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 4, 7, 1, 2, 6, 8])), list_node([1, 3, 4, 7, 2, 6, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2])), list_node([9, 8, 7, 6, 5, 4, 2, 1, 0, -1, -2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2])), list_node([9, 8, 7, 6, 5, 4, 2, 1, 0, -1, -2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])), list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])), list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21])), list_node([21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21])), list_node([21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 1, 4, 7, 6, 2, 8, 9])), list_node([5, 3, 1, 4, 6, 2, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 1, 4, 7, 6, 2, 8, 9])), list_node([5, 3, 1, 4, 6, 2, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([5, 4, 3, 2, 1, -1, -2, -3, -4, -5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([5, 4, 3, 2, 1, -1, -2, -3, -4, -5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100, 110]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100, 110])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80])), list_node([10, 20, 30, 40, 60, 70, 80]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80])), list_node([10, 20, 30, 40, 60, 70, 80])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 8, 7, 6, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 8, 7, 6, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17])), list_node([1, 3, 5, 7, 11, 13, 15, 17]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17])), list_node([1, 3, 5, 7, 11, 13, 15, 17])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])), list_node([2, 4, 6, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])), list_node([2, 4, 6, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 3, 2, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 3, 2, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 2, 1])), list_node([1, 2, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 2, 1])), list_node([1, 2, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 88, 77, 66, 55, 44, 33, 22, 11])), list_node([99, 88, 77, 66, 44, 33, 22, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 88, 77, 66, 55, 44, 33, 22, 11])), list_node([99, 88, 77, 66, 44, 33, 22, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 9, 1, 7, 4])), list_node([5, 3, 8, 6, 9, 1, 7, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 9, 1, 7, 4])), list_node([5, 3, 8, 6, 9, 1, 7, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])), list_node([1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 25, 27, 29]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])), list_node([1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 25, 27, 29])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 3]))
    assert is_same_list(candidate(head = list_node([2, 1])), list_node([2]))
    assert candidate(head = list_node([1])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 2])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4])), list_node([1, 2, 4]))
    assert is_same_list(candidate(head = list_node([1, 3, 4, 7, 1, 2, 6])), list_node([1, 3, 4, 1, 2, 6]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6])), list_node([1, 2, 3, 5, 6]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]))
    assert is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19, 21]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 9, 8, 7, 6, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60]))
    assert is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99999, 99998, 99997, 99996, 99994, 99993, 99992, 99991]))
    assert is_same_list(candidate(head = list_node([31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([31, 29, 27, 25, 23, 21, 19, 17, 13, 11, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])), list_node([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11]))
    assert is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])), list_node([1000, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])), list_node([1, 2, 3, 4, 6, 7, 8]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 1])), list_node([1, 2, 1]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100]))
    assert is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([21, 19, 17, 15, 13, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([5, 4, 3, 2, 1, 0, -1, -2, -4, -5, -6, -7, -8, -9, -10]))
    assert candidate(head = list_node([5])) == None
    assert is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])), list_node([100000, 99999, 99998, 99996, 99995]))
    assert is_same_list(candidate(head = list_node([1, 3, 4, 7, 1, 2, 6, 8])), list_node([1, 3, 4, 7, 2, 6, 8]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2])), list_node([9, 8, 7, 6, 5, 4, 2, 1, 0, -1, -2]))
    assert is_same_list(candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])), list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]))
    assert is_same_list(candidate(head = list_node([21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21])), list_node([21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]))
    assert is_same_list(candidate(head = list_node([5, 3, 1, 4, 7, 6, 2, 8, 9])), list_node([5, 3, 1, 4, 6, 2, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([5, 4, 3, 2, 1, -1, -2, -3, -4, -5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100, 110]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80])), list_node([10, 20, 30, 40, 60, 70, 80]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 8, 7, 6, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17])), list_node([1, 3, 5, 7, 11, 13, 15, 17]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])), list_node([2, 4, 6, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([9, 8, 7, 6, 5, 3, 2, 1, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 1])), list_node([1, 2, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])), list_node([1, 3, 5, 7, 9, 13, 15, 17, 19]))
    assert is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]))
    assert is_same_list(candidate(head = list_node([99, 88, 77, 66, 55, 44, 33, 22, 11])), list_node([99, 88, 77, 66, 44, 33, 22, 11]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
    assert is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 9, 1, 7, 4])), list_node([5, 3, 8, 6, 9, 1, 7, 4]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])), list_node([1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 25, 27, 29]))


